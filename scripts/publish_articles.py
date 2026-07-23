#!/usr/bin/env python3
"""Publish Karmactive article HTML files to WordPress via REST API."""

import os
import re
import json
import base64
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote
from urllib.error import HTTPError

WP_BASE = "https://www.karmactive.com/wp-json/wp/v2"
USERNAME = os.environ.get("WP_USERNAME", "")
PASSWORD = os.environ.get("WP_PASSWORD", "")

if not USERNAME or not PASSWORD:
    print("ERROR: WP_USERNAME and WP_PASSWORD environment variables must be set.")
    sys.exit(1)

AUTH_HEADER = "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
HEADERS = {"Authorization": AUTH_HEADER, "Content-Type": "application/json"}


def api_get(path):
    req = Request(f"{WP_BASE}/{path}", headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def api_post(path, data):
    body = json.dumps(data).encode()
    req = Request(f"{WP_BASE}/{path}", data=body, headers=HEADERS, method="POST")
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def get_or_create_term(taxonomy, name):
    """Return the WP term ID for name, creating it if it doesn't exist."""
    results = api_get(f"{taxonomy}?search={quote(name)}&per_page=100")
    for t in results:
        if t["name"].lower() == name.lower():
            return t["id"]
    result = api_post(taxonomy, {"name": name})
    return result["id"]


def slug_exists(slug):
    """Return post ID if a post with this slug already exists, else None."""
    results = api_get(f"posts?slug={quote(slug)}&status=any")
    return results[0]["id"] if results else None


def parse_article(filepath):
    """Parse an article HTML file and return a publish-ready dict."""
    text = Path(filepath).read_text(encoding="utf-8")

    m = re.search(r"<!--(.*?)-->", text, re.DOTALL)
    if not m:
        raise ValueError(f"No metadata comment block found in {filepath}")
    comment = m.group(1)
    body = text[m.end():].strip()

    def field(label):
        # Handles labels with parenthetical qualifiers, e.g. "Meta Description (175 chars)"
        fm = re.search(rf"{re.escape(label)}[^:\n]*:\s*(.+)", comment)
        return fm.group(1).strip() if fm else ""

    return {
        "title":          field("Title (under 120 chars)"),
        "slug":           field("Slug"),
        "content":        body,
        "meta_desc":      field("Meta Description"),
        "focus_kw":       field("Focus Key Phrase"),
        "categories_str": field("Categories"),
        "tags_str":       field("Tags"),
    }


def resolve_category_ids(categories_str):
    ids = []
    for part in categories_str.split("|"):
        part = part.strip()
        if not part:
            continue
        # "Health > Food & Drinks" — use full name for WP lookup first, then leaf
        try:
            ids.append(get_or_create_term("categories", part))
        except Exception:
            leaf = part.split(">")[-1].strip()
            ids.append(get_or_create_term("categories", leaf))
    return ids


def resolve_tag_ids(tags_str):
    ids = []
    for name in tags_str.split(","):
        name = name.strip()
        if name:
            ids.append(get_or_create_term("tags", name))
    return ids


def publish_article(filepath):
    art = parse_article(filepath)
    print(f"\n→ {art['title']}")
    print(f"  Slug: {art['slug']}")

    existing_id = slug_exists(art["slug"])
    if existing_id:
        print(f"  SKIP — post with this slug already exists (ID {existing_id})")
        return None

    print("  Resolving categories...")
    cat_ids = resolve_category_ids(art["categories_str"])

    print("  Resolving tags...")
    tag_ids = resolve_tag_ids(art["tags_str"])

    post_data = {
        "title":      art["title"],
        "slug":       art["slug"],
        "content":    art["content"],
        "status":     "publish",
        "categories": cat_ids,
        "tags":       tag_ids,
        "meta": {
            "_yoast_wpseo_metadesc":  art["meta_desc"],
            "_yoast_wpseo_focuskw":   art["focus_kw"],
            "rank_math_description":  art["meta_desc"],
            "rank_math_focus_keyword": art["focus_kw"],
        },
    }

    try:
        result = api_post("posts", post_data)
        print(f"  PUBLISHED — ID {result['id']}: {result['link']}")
        return result
    except HTTPError as e:
        body = e.read().decode()
        print(f"  ERROR {e.code}: {body}")
        raise


def main():
    articles_dir = Path(__file__).parent.parent / "articles"
    # Accept an optional date prefix argument, e.g. "2026-07-23"
    prefix = sys.argv[1] if len(sys.argv) > 1 else None

    if prefix:
        files = sorted(articles_dir.glob(f"{prefix}-story*.html"))
    else:
        files = sorted(articles_dir.glob("*.html"))

    if not files:
        print(f"No article files found in {articles_dir}")
        sys.exit(1)

    print(f"Found {len(files)} article(s) to publish:")
    for f in files:
        print(f"  {f.name}")

    failed = 0
    for filepath in files:
        try:
            publish_article(filepath)
        except Exception as e:
            print(f"  FAILED: {e}")
            failed += 1

    print(f"\nDone. {len(files) - failed} published, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
