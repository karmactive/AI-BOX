#!/usr/bin/env python3
"""
PUBLISHER — executes staged POSTs to karmactive.com WP REST API.
Run by Haiku session (Claude stays out of publishing).
Reads posts.json (already prepared with resolved IDs) and wp_pass.txt.
Posts each article with status=publish, scheduled date, author, cats, tags,
meta description, focus keyphrase, and embedded external/internal links in body.
"""
import json, os, subprocess, sys

BASE = "C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP = "https://www.karmactive.com/wp-json/wp/v2"
USER = "Karmactive Staff"
PASS = open(BASE + "wp_pass.txt").read().strip()

posts = json.load(open(BASE + "posts.json", encoding="utf-8"))

def make_body(p):
    b = p["body"]
    # embed external + internal links as HTML at top of body
    links_html = ""
    if p.get("ext_link", {}).get("url"):
        e = p["ext_link"]
        links_html += f'<p><strong>External source:</strong> <a href="{e["url"]}" target="_blank" rel="noopener">{e["desc"] or e["url"]}</a></p>\n'
    if p.get("int_link", {}).get("url"):
        i = p["int_link"]
        links_html += f'<p><strong>Related:</strong> <a href="{i["url"]}" target="_blank" rel="noopener">{i["desc"] or i["url"]}</a></p>\n'
    return links_html + "\n" + b

def post_one(p):
    payload = {
        "title": p["title"],
        "content": make_body(p),
        "excerpt": p["excerpt"],
        "slug": p["slug"],
        "author": p["author"],
        "categories": p["categories"],
        "tags": p["tags"],
        "date": p["date"],
        "status": "publish",
        "meta": {
            "rank_math_description": p["meta_desc"],
            "rank_math_focus_keyword": p["focus_keyphrase"],
        },
    }
    out = subprocess.run(
        ["curl","-s","-u",f"{USER}:{PASS}","-X","POST",f"{WP}/posts",
         "-H","Content-Type: application/json",
         "-d",json.dumps(payload, ensure_ascii=False)],
        capture_output=True, text=True, timeout=60)
    try:
        r = json.loads(out.stdout)
    except Exception:
        return None, out.stdout[:300]
    if "id" in r:
        return r["id"], r.get("link")
    return None, out.stdout[:400]

print(f"Publishing {len(posts)} posts to {WP}/posts ...")
results = []
for idx, p in enumerate(posts, 1):
    pid, link = post_one(p)
    if pid:
        print(f"  [{idx}/{len(posts)}] OK id={pid} author={p['author_name']} | {link}")
        results.append({"title": p["title"], "id": pid, "link": link, "status": "published"})
    else:
        print(f"  [{idx}/{len(posts)}] FAIL {p['title'][:40]} -> {link}")
        results.append({"title": p["title"], "error": link, "status": "failed"})

json.dump(results, open(BASE + "publish_results.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("\nDONE. Results -> publish_results.json")
for r in results:
    print(f"  {r.get('status'):9} {r.get('id','-'):>6}  {r.get('title','')[:50]}")
