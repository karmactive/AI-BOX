#!/usr/bin/env python3
import requests
import json
import base64
import os

# WordPress credentials
WP_URL = "https://thegametribune.com/wp-json/wp/v2/posts"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

# Create auth header
credentials = f"{USERNAME}:{PASSWORD}"
token = base64.b64encode(credentials.encode()).decode("utf-8")
headers = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/json"
}

# Read article content files
SCRATCHPAD = "/tmp/claude-0/-home-user-AI-BOX/c4b91599-9bb9-5ed5-bc39-fc73ead6959d/scratchpad/articles"

def read_file(filename):
    with open(os.path.join(SCRATCHPAD, filename), 'r') as f:
        return f.read()

# Articles data
articles = [
    {
        "title": "Halo Hits PS5 for the First Time in 25 Years — Campaign Evolved Early Access Is Live",
        "content": read_file("article1_halo.html"),
        "slug": "halo-campaign-evolved-early-access-ps5-first-time-july-2026",
        "categories": [27, 19, 1],  # Games, News, Latest
        "tags": [131, 553, 279, 65, 198],  # Xbox, Xbox Game Pass, PlayStation 5, Gaming News, Gaming
        "meta_desc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years. Unreal Engine 5 rebuild brings 4-player co-op, new missions, and Game Pass day-one access.",
        "focus_kw": "Halo Campaign Evolved PS5"
    },
    {
        "title": "JPO Rejects Nintendo Monster-Catching Patent Again, Cites Pokemon Fan Game as Prior Art",
        "content": read_file("article2_nintendo.html"),
        "slug": "jpo-rejects-nintendo-monster-catching-patent-palworld-lawsuit-2026",
        "categories": [27, 19, 1],  # Games, News, Latest
        "tags": [216, 226, 497, 65, 308],  # Nintendo, Japan, Gaming Industry, Gaming News, Pokémon GO
        "meta_desc": "Japan Patent Office rejects Nintendo's divisional monster-catching patent again, citing ARK and a Pokemon fan game as prior art. Here's what it means for the Palworld lawsuit.",
        "focus_kw": "Nintendo Palworld patent rejected"
    },
    {
        "title": "Wonder Man #5 Is Out — Gerry Duggan's Marvel Run Ends With No Clean Resolution",
        "content": read_file("article3_wonderman.html"),
        "slug": "wonder-man-issue-5-gerry-duggan-marvel-series-finale-2026",
        "categories": [28, 19, 1],  # Movies, News, Latest
        "tags": [197, 338, 122],  # Marvel, Comics, Hollywood
        "meta_desc": "Wonder Man #5 released July 22, 2026, ending Gerry Duggan's 5-issue Marvel series. Simon Williams confronts betrayal and an unresolved moral weight — with no tidy ending.",
        "focus_kw": "Wonder Man 5 Marvel Duggan"
    },
    {
        "title": "Star Wars Jedi: Fallen Order Manga Vol. 3 Confirmed for December 1, 2026",
        "content": read_file("article4_starwars.html"),
        "slug": "star-wars-jedi-fallen-order-manga-volume-3-december-2026",
        "categories": [27, 28, 19, 1],  # Games, Movies, News, Latest
        "tags": [345, 475, 280, 65],  # Star Wars, Manga, EA Games, Gaming News
        "meta_desc": "Panini Comics confirms Star Wars Jedi: Fallen Order Manga Vol. 3 for December 1, 2026. Cal Kestis faces a destroyed lightsaber and painful memories in 200 pages of adapted story.",
        "focus_kw": "Star Wars Jedi manga volume 3"
    }
]

results = []

for article in articles:
    payload = {
        "title": article["title"],
        "content": article["content"],
        "status": "publish",
        "slug": article["slug"],
        "categories": article["categories"],
        "tags": article["tags"],
        "meta": {
            "_yoast_wpseo_metadesc": article["meta_desc"],
            "_yoast_wpseo_focuskw": article["focus_kw"]
        }
    }

    print(f"\n--- Publishing: {article['title'][:60]}...")

    try:
        response = requests.post(
            WP_URL,
            headers=headers,
            data=json.dumps(payload),
            timeout=60,
            verify=True
        )

        if response.status_code in [200, 201]:
            post_data = response.json()
            post_id = post_data.get("id")
            post_url = post_data.get("link")
            print(f"✅ SUCCESS! Post ID: {post_id}")
            print(f"   URL: {post_url}")
            results.append({"title": article["title"], "id": post_id, "url": post_url, "status": "success"})
        else:
            print(f"❌ FAILED! Status: {response.status_code}")
            print(f"   Response: {response.text[:500]}")
            results.append({"title": article["title"], "status": "failed", "error": response.text[:200]})

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        results.append({"title": article["title"], "status": "error", "error": str(e)})

print("\n\n=== PUBLISHING RESULTS ===")
for r in results:
    print(f"\nTitle: {r['title'][:70]}")
    print(f"Status: {r['status']}")
    if r.get('url'):
        print(f"URL: {r['url']}")
    if r.get('error'):
        print(f"Error: {r.get('error', '')[:150]}")
