#!/usr/bin/env python3
import requests
import json
import base64
import time

WP_BASE = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

credentials = f"{USERNAME}:{PASSWORD}"
token = base64.b64encode(credentials.encode()).decode("utf-8")
headers_json = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/json"
}
headers_form = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

ARTICLES = [
    {
        "id": 7222,
        "title": "Halo Hits PS5 for the First Time in 25 Years — Campaign Evolved Early Access Is Live",
        "yoast_title": "Halo Campaign Evolved PS5 Early Access Is Live",
        "focus_kw": "Halo Campaign Evolved PS5",
        "meta_desc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years. Unreal Engine 5 rebuild brings 4-player co-op, new missions, and Game Pass day-one access.",
        # Tags: Xbox (131), Xbox Game Pass (553), PlayStation 5 (279), Gaming News (65) — removed Gaming (198)
        "tags": [131, 553, 279, 65],
        "categories": [27, 19, 1],  # Games, News, Latest
        "new_intro": '<p>Halo: Campaign Evolved is now on PS5 — the first time in the franchise\'s 25-year history that a mainline Halo game has appeared on a Sony console. Early access went live today, July 23, 2026, at 8 AM Pacific, letting pre-order holders on PlayStation 5, Xbox Series X|S, Windows PC, and Steam boot up a completely rebuilt version of the original game before its July 28 public launch.</p>',
        "old_intro_start": "<p>After 25 years as an Xbox-only franchise"
    },
    {
        "id": 7223,
        "title": "JPO Rejects Nintendo Monster-Catching Patent Again, Cites Pokemon Fan Game as Prior Art",
        "yoast_title": "Nintendo Palworld Patent Rejected Again by JPO",
        "focus_kw": "Nintendo Palworld patent rejected",
        "meta_desc": "Japan Patent Office rejects Nintendo's divisional monster-catching patent again, citing ARK and a Pokemon fan game as prior art. Here's what it means for the Palworld lawsuit.",
        "tags": [216, 226, 497, 65, 308],  # Nintendo, Japan, Gaming Industry, Gaming News, Pokémon GO
        "categories": [27, 19, 1],  # Games, News, Latest
        "new_intro": "<p>Nintendo's Palworld patent has been rejected by Japan's patent office — for the second time. The Japan Patent Office (JPO) upheld its rejection of a divisional patent application tied to monster-capturing mechanics in mid-July 2026, dismissing Nintendo's counter-arguments in language observers described as unusually direct. The rejection is the latest setback in Nintendo's ongoing legal dispute with <a href=\"https://www.pocketpair.jp/\" target=\"_blank\" rel=\"noopener\">Pocketpair</a>, the developer of Palworld.</p>",
        "old_intro_start": "<p>Japan's patent office said no — again"
    },
    {
        "id": 7224,
        "title": "Wonder Man #5 Is Out — Gerry Duggan's Marvel Run Ends With No Clean Resolution",
        "yoast_title": "Wonder Man #5: Gerry Duggan's Marvel Run Ends",
        "focus_kw": "Wonder Man 5 Marvel Duggan",
        "meta_desc": "Wonder Man #5 released July 22, 2026, ending Gerry Duggan's 5-issue Marvel series. Simon Williams confronts betrayal and an unresolved moral weight — with no tidy ending.",
        "tags": [197, 338, 122],  # Marvel, Comics, Hollywood
        "categories": [28, 19, 1],  # Movies, News, Latest
        "new_intro": '<p>Wonder Man #5 is out, and Gerry Duggan\'s Marvel run on the character is now complete. Released July 22, 2026, the fifth and final issue of Wonder Man Vol. 4 closes a five-issue limited series that used a Hollywood backdrop to examine moral weight without offering a clean resolution. <a href="https://www.marvel.com/comics/issue/128947/wonder_man_2026_1" target="_blank" rel="noopener">The series</a> ran from March 2026 to July 2026.</p>',
        "old_intro_start": "<p>It started in March 2026."
    },
    {
        "id": 7225,
        "title": "Star Wars Jedi: Fallen Order Manga Vol. 3 Confirmed for December 1, 2026",
        "yoast_title": "Star Wars Jedi Manga Vol. 3 — December 2026",
        "focus_kw": "Star Wars Jedi manga volume 3",
        "meta_desc": "Panini Comics confirms Star Wars Jedi: Fallen Order Manga Vol. 3 for December 1, 2026. Cal Kestis faces a destroyed lightsaber and painful memories in 200 pages of adapted story.",
        "tags": [345, 475, 280, 65],  # Star Wars, Manga, EA Games, Gaming News
        "categories": [27, 28, 19, 1],  # Games, Movies, News, Latest
        "new_intro": '<p>Star Wars Jedi: Fallen Order manga volume 3 is confirmed for December 1, 2026. <a href="https://www.panini.co.uk/" target="_blank" rel="noopener">Panini Comics</a> announced the third volume of its manga adaptation of the 2019 Respawn Entertainment game, continuing the Cal Kestis story in print format ahead of any sequel game release.</p>',
        "old_intro_start": "<p>Cal Kestis is coming back to print."
    }
]

def get_current_content(post_id):
    resp = requests.get(
        f"{WP_BASE}/posts/{post_id}?context=edit",
        headers=headers_json,
        timeout=30,
        verify=True
    )
    if resp.status_code == 200:
        return resp.json().get("content", {}).get("raw", "")
    return None

def update_post(post_id, payload):
    resp = requests.post(
        f"{WP_BASE}/posts/{post_id}",
        headers=headers_json,
        data=json.dumps(payload),
        timeout=60,
        verify=True
    )
    return resp

def try_yoast_head_endpoint(post_id, focus_kw, meta_desc, seo_title):
    """Try Yoast's /yoast/v1/get_head endpoint approach or SEO data endpoint"""
    # Try posting directly to yoast indexables if available
    endpoints_to_try = [
        f"https://thegametribune.com/wp-json/yoast/v1/index_now",
    ]
    for ep in endpoints_to_try:
        try:
            r = requests.get(ep, headers=headers_json, timeout=10, verify=True)
            print(f"  Yoast endpoint {ep}: {r.status_code}")
        except:
            pass

def try_set_yoast_via_wc_namespace(post_id, focus_kw, meta_desc, seo_title):
    """Try setting via alternate meta key names"""
    results = {}

    # Method 1: no underscore prefix
    payload1 = {
        "meta": {
            "yoast_wpseo_focuskw": focus_kw,
            "yoast_wpseo_metadesc": meta_desc,
            "yoast_wpseo_title": seo_title,
        }
    }
    r1 = requests.post(f"{WP_BASE}/posts/{post_id}", headers=headers_json, data=json.dumps(payload1), timeout=30, verify=True)
    results["no_underscore"] = {"status": r1.status_code, "meta": r1.json().get("meta", {}) if r1.status_code == 200 else r1.text[:200]}

    time.sleep(0.5)

    # Method 2: via yoast_head_json (read-only but let's check)
    # Actually try the Yoast /wpseo-posts route
    r2 = requests.get(f"https://thegametribune.com/wp-json/yoast/v1/configuration", headers=headers_json, timeout=10, verify=True)
    results["yoast_config"] = {"status": r2.status_code, "body": r2.text[:300]}

    time.sleep(0.5)

    # Method 3: Try RankMath or Yoast custom routes
    r3 = requests.get(f"https://thegametribune.com/wp-json/", headers=headers_json, timeout=15, verify=True)
    if r3.status_code == 200:
        routes = list(r3.json().get("routes", {}).keys())
        yoast_routes = [r for r in routes if "yoast" in r.lower() or "seo" in r.lower() or "rank" in r.lower()]
        results["seo_routes"] = yoast_routes[:30]

    return results

print("=== STEP 1: Discover available SEO/Yoast REST routes ===")
r = requests.get("https://thegametribune.com/wp-json/", headers=headers_json, timeout=15, verify=True)
if r.status_code == 200:
    all_routes = list(r.json().get("routes", {}).keys())
    yoast_routes = [x for x in all_routes if "yoast" in x.lower() or "seo" in x.lower() or "rank" in x.lower() or "wpseo" in x.lower()]
    print(f"Found {len(yoast_routes)} SEO-related routes:")
    for route in yoast_routes:
        print(f"  {route}")
else:
    print(f"Failed to get routes: {r.status_code}")

print("\n=== STEP 2: Check Yoast namespace routes ===")
r2 = requests.get("https://thegametribune.com/wp-json/yoast/v1/", headers=headers_json, timeout=15, verify=True)
print(f"Yoast v1 namespace: {r2.status_code}")
if r2.status_code == 200:
    print(json.dumps(r2.json(), indent=2)[:2000])

print("\n=== STEP 3: Try setting meta with no-underscore keys ===")
test_id = 7222
test_payload = {
    "meta": {
        "yoast_wpseo_focuskw": "test keyphrase",
        "yoast_wpseo_metadesc": "test meta description here",
    }
}
r3 = requests.post(f"{WP_BASE}/posts/{test_id}", headers=headers_json, data=json.dumps(test_payload), timeout=30, verify=True)
print(f"No-underscore PATCH status: {r3.status_code}")
if r3.status_code == 200:
    print(f"Meta returned: {r3.json().get('meta', {})}")

print("\n=== STEP 4: Check what meta keys are registered for posts ===")
# Get post schema to see registered meta fields
r4 = requests.options(f"{WP_BASE}/posts", headers=headers_json, timeout=15, verify=True)
print(f"OPTIONS status: {r4.status_code}")
if r4.status_code == 200:
    schema = r4.json()
    meta_props = schema.get("schema", {}).get("properties", {}).get("meta", {}).get("properties", {})
    print(f"Registered meta properties: {list(meta_props.keys())}")

print("\n=== STEP 5: Update content with keyphrases in introductions ===")
SCRATCHPAD = "/tmp/claude-0/-home-user-AI-BOX/c4b91599-9bb9-5ed5-bc39-fc73ead6959d/scratchpad/articles"

import os

def read_file(filename):
    with open(os.path.join(SCRATCHPAD, filename), 'r') as f:
        return f.read()

article_files = {
    7222: "article1_halo.html",
    7223: "article2_nintendo.html",
    7224: "article3_wonderman.html",
    7225: "article4_starwars.html",
}

for article in ARTICLES:
    post_id = article["id"]
    filename = article_files[post_id]
    content = read_file(filename)

    # Replace intro paragraph
    old_start = article["old_intro_start"]
    new_intro = article["new_intro"]

    # Find the first <p> tag and replace the entire first paragraph
    import re
    # Match the first <p>...</p> block
    first_p_match = re.match(r'^(<p>.*?</p>)', content, re.DOTALL)
    if first_p_match:
        old_first_p = first_p_match.group(1)
        new_content = content.replace(old_first_p, new_intro, 1)
        print(f"\nPost {post_id}: Replaced intro paragraph")
        print(f"  Old: {old_first_p[:100]}...")
        print(f"  New: {new_intro[:100]}...")

        # Save updated content back to file
        with open(os.path.join(SCRATCHPAD, filename), 'w') as f:
            f.write(new_content)

        # Now PATCH the post content + tags + categories
        patch_payload = {
            "content": new_content,
            "tags": article["tags"],
            "categories": article["categories"],
            "title": article["title"],
            "slug": None,  # don't change slug
            "meta": {
                "_yoast_wpseo_metadesc": article["meta_desc"],
                "_yoast_wpseo_focuskw": article["focus_kw"],
                "_yoast_wpseo_title": article["yoast_title"],
                "yoast_wpseo_metadesc": article["meta_desc"],
                "yoast_wpseo_focuskw": article["focus_kw"],
                "yoast_wpseo_title": article["yoast_title"],
            }
        }
        # Remove None values
        patch_payload = {k: v for k, v in patch_payload.items() if v is not None}

        resp = update_post(post_id, patch_payload)
        print(f"  PATCH status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"  Meta returned: {data.get('meta', {})}")
            print(f"  Tags: {data.get('tags', [])}")
            print(f"  Categories: {data.get('categories', [])}")
        else:
            print(f"  Error: {resp.text[:300]}")

        time.sleep(1)
    else:
        print(f"\nPost {post_id}: Could not find first paragraph to replace")

print("\n=== STEP 6: Verify final state of each post ===")
for article in ARTICLES:
    post_id = article["id"]
    r = requests.get(f"{WP_BASE}/posts/{post_id}?context=edit", headers=headers_json, timeout=30, verify=True)
    if r.status_code == 200:
        data = r.json()
        print(f"\nPost {post_id} - {article['title'][:50]}...")
        print(f"  Tags: {data.get('tags', [])}")
        print(f"  Categories: {data.get('categories', [])}")
        print(f"  Meta: {data.get('meta', {})}")
        content_raw = data.get("content", {}).get("rendered", "")
        # Show first 200 chars of content
        import html
        text = re.sub('<[^<]+?>', '', content_raw)
        print(f"  Content start: {text[:200]}")
    time.sleep(0.5)
