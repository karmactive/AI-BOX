"""
Fix tags and categories for all 7 published articles.
"""

import requests
from requests.auth import HTTPBasicAuth
import json

BASE_URL = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = "keTs4gmnQNeDQHcEEjk1qpd5"
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)

# Real Category IDs
CATEGORIES = {
    "Gaming News": 697,
    "Games": 27,
    "News": 19,
    "Technology": 31,
    "Anime": 20,
}

# Tag mapping per article
ARTICLE_TAGS = {
    7295: ["Game Updates", "007 First Light", "IO Interactive", "PlayStation", "PC Gaming"],
    7296: ["DRM Technology", "Denuvo Removal", "Steam Deck Gaming", "PC Gaming", "007 First Light"],
    7297: ["GTA VI News", "Digital Ownership", "PlayStation Games", "Gaming Regulations"],
    7298: ["Xbox Games", "Game Delisting", "Digital Ownership", "Platform Policy", "Indie Games"],
    7299: ["Anime News", "Manga Creators", "Creator Interviews", "Witch Hat Atelier"],
    7300: ["Anime Reviews", "Spring 2026 Anime", "Animation Quality", "Manga Adaptation"],
    7301: ["Mobile Games", "Game of Thrones", "Live Service", "Game Events", "Strategy Games"],
}

ARTICLE_CATEGORIES = {
    7295: ["Games", "Gaming News"],
    7296: ["Gaming News", "Technology"],
    7297: ["Games", "Gaming News"],
    7298: ["Games", "Gaming News"],
    7299: ["Anime", "News"],
    7300: ["Anime", "News"],
    7301: ["Games", "Gaming News"],
}

print("Fetching all existing tags...")
r = requests.get(f"{BASE_URL}/tags?per_page=100", auth=AUTH)
all_tags = r.json()
tag_map = {tag['name']: tag['id'] for tag in all_tags}

print(f"Found {len(tag_map)} existing tags\n")

# Create missing tags
tags_to_create = set()
for post_id, tags in ARTICLE_TAGS.items():
    for tag in tags:
        if tag not in tag_map:
            tags_to_create.add(tag)

print(f"Creating {len(tags_to_create)} new tags...")

for tag_name in tags_to_create:
    r = requests.post(
        f"{BASE_URL}/tags",
        auth=AUTH,
        json={"name": tag_name}
    )
    if r.status_code in [200, 201]:
        tag_map[tag_name] = r.json()['id']
        print(f"  ✅ {tag_name} (ID {tag_map[tag_name]})")
    elif r.status_code == 400 and "term_exists" in r.text:
        # Tag exists, fetch its ID
        r2 = requests.get(f"{BASE_URL}/tags?search={tag_name}", auth=AUTH)
        if r2.json():
            tag_map[tag_name] = r2.json()[0]['id']
            print(f"  ℹ️  {tag_name} exists (ID {tag_map[tag_name]})")
    else:
        print(f"  ❌ {tag_name}: {r.status_code}")

# Update articles
print("\n" + "="*70)
print("UPDATING ARTICLES")
print("="*70 + "\n")

for post_id in sorted(ARTICLE_TAGS.keys()):
    tag_names = ARTICLE_TAGS[post_id]
    category_names = ARTICLE_CATEGORIES[post_id]
    
    tag_ids = [tag_map[t] for t in tag_names]
    category_ids = [CATEGORIES[c] for c in category_names]
    
    print(f"Post {post_id}:")
    print(f"  Tags: {', '.join(tag_names)}")
    print(f"  Categories: {', '.join(category_names)}")
    
    r = requests.post(
        f"{BASE_URL}/posts/{post_id}",
        auth=AUTH,
        json={
            "tags": tag_ids,
            "categories": category_ids,
        }
    )
    
    if r.status_code in [200, 201]:
        print(f"  ✅ UPDATED\n")
    else:
        print(f"  ❌ ERROR {r.status_code}\n")

print("="*70)
print("✅ ALL TAGS AND CATEGORIES FIXED")
print("="*70)
