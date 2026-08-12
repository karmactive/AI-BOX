#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIX script (active model / Claude task): repair the 7 published Australia posts in place.
Fixes:
  A) SEO meta -> Yoast keys (_yoast_wpseo_metadesc 200c, _yoast_wpseo_focuskw 4w)
  B) Categories -> exactly the author's categories mapped to real slugs (no invented cats)
  C) Body -> render markdown as HTML + embed external/internal links as inline anchor text
Idempotent-ish; uses posts.json (already has body/excerpt/meta/ext_link/int_link) as source.
"""
import os, re, json, time, base64, subprocess
import markdown

BASE = "C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP = "https://www.karmactive.com/wp-json/wp/v2"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
PASS = open(os.path.join(BASE, "wp_pass.txt")).read().strip()
AUTH = "Basic " + base64.b64encode(("Karmactive Staff:" + PASS).encode()).decode()

# real slug -> id (from live WP)
SLUG_ID = {
 "australia":20133,"policy":19564,"technology":56,"conservation":6549,"wildlife":2756,
 "environment":16921,"business":31,"disaster":2515,"news":63,"mobility":2538,"electric":15129,
 "latest":1,"politics":36,"space":2546,"aviation":13038,"weather":None,"sustainability":57,  # weather filled below
}
# author -> categories (your mapping, mapped to existing slugs)
AUTHOR_CATS = {
 "sunita":      ["business","policy","news"],            # social welfare -> news (no welfare cat)
 "sonali":      ["aviation","space","disaster"],          # natural disaster -> disaster
 "rahul":       ["environment","technology","sustainability"],
 "govind":      ["politics","news","wildlife"],           # daily news -> news
 "karmactive staff": ["news","weather"],                  # recall -> news (no recall cat)
 "karmactive team":  ["technology","mobility","space"],   # tech -> technology
}
# fill weather id
def api_get(path):
    out = subprocess.run(["curl","-s","-A",UA,"-H","Authorization: "+AUTH,
                          f"{WP}/{path}"], capture_output=True, text=True, timeout=90).stdout
    return json.loads(out)
w = api_get("categories?slug=weather")
SLUG_ID["weather"] = w[0]["id"] if isinstance(w,list) and w else None

posts = json.load(open(os.path.join(BASE,"posts.json"), encoding="utf-8"))

def render_body_md(md):
    # convert markdown -> html with tables/footnotes/fenced code support
    return markdown.markdown(md, extensions=["extra","sane_lists","toc"])

def embed_links(html, ext, intr):
    # ext/intr: dicts with url + desc (anchor text)
    soup_safe = html
    # inject external link: wrap first occurrence of a likely keyword (source name) if present
    added_ext = added_int = False
    if ext and ext.get("url"):
        # try to anchor on the description's first significant word, else append a sourced line
        kw = re.split(r"\s+", ext.get("desc","source"))[0]
        m = re.search(r">([^<]*\b"+re.escape(kw)+r"\b[^<]*)<", soup_safe)
        if m:
            soup_safe = soup_safe[:m.start()] + \
                f'<a href="{ext["url"]}" target="_blank" rel="noopener">{m.group(1)}</a>' + \
                soup_safe[m.end():]
            added_ext = True
        if not added_ext:
            soup_safe += f'\n<p>Source: <a href="{ext["url"]}" target="_blank" rel="noopener">{ext.get("desc") or ext["url"]}</a></p>'
    if intr and intr.get("url"):
        # append a related-coverage block with proper anchor text
        soup_safe += f'\n<p><strong>Related coverage:</strong> <a href="{intr["url"]}" target="_blank" rel="noopener">{intr.get("desc") or intr["url"]}</a></p>'
        added_int = True
    return soup_safe

def put_post(pid, **data):
    payload = {}
    if "content" in data: payload["content"] = data["content"]
    if "categories" in data: payload["categories"] = data["categories"]
    if "tags" in data: payload["tags"] = data["tags"]
    if "meta" in data: payload["meta"] = data["meta"]
    if "excerpt" in data: payload["excerpt"] = data["excerpt"]
    out = subprocess.run(["curl","-s","-A",UA,"-H","Authorization: "+AUTH,
                          "-X","PUT",f"{WP}/posts/{pid}?context=edit",
                          "-H","Content-Type: application/json",
                          "-d",json.dumps(payload, ensure_ascii=False)],
                         capture_output=True, text=True, timeout=120).stdout
    return json.loads(out)

for p in posts:
    pid = p["id"]
    md = p.get("body","")
    html = render_body_md(md)
    html = embed_links(html, p.get("ext_link"), p.get("int_link"))
    cats = [SLUG_ID[s] for s in AUTHOR_CATS.get(p["author_name"], []) if SLUG_ID.get(s)]
    meta = {
        "_yoast_wpseo_metadesc": p["meta_desc"],
        "_yoast_wpseo_focuskw": p["focus_keyphrase"],
    }
    r = put_post(pid, content=html, categories=cats, tags=p["tags"], meta=meta, excerpt=p["excerpt"])
    ok = "id" in r
    new_cats = [c for c in (r.get("categories",[]) if ok else [])]
    print(f"POST {pid} ({p['author_name']}): {'OK' if ok else 'FAIL'} | cats={len(new_cats)} | "
          f"metadesc={len((r.get('meta') or {}).get('_yoast_wpseo_metadesc','') or '')}c | "
          f"focuskw={ (r.get('meta') or {}).get('_yoast_wpseo_focuskw','-') }")

print("\nDONE. Re-verify with _check_live.py")
