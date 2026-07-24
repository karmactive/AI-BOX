#!/usr/bin/env python3
"""
Fix Yoast SEO via REST API - Add Meta Description, Focus Keyphrase, and SEO Title
Uses existing categories only - no new categories created
"""

import requests
import base64
import json
import sys
from datetime import datetime

# Configuration
API_BASE_URL = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = "keTs 4gmn QNeD QHcE Ejk1 qpd5"

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def get_auth_header():
    """Generate Basic Auth header"""
    credentials = f"{USERNAME}:{PASSWORD}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def get_category_id(category_name):
    """Get existing category ID from name - DO NOT CREATE"""
    try:
        headers = get_auth_header()
        response = requests.get(
            f"{API_BASE_URL}/categories",
            params={"search": category_name, "per_page": 100},
            headers=headers
        )
        if response.status_code == 200:
            categories = response.json()
            if categories:
                return categories[0]['id']
            else:
                print(f"{RED}✗ Category '{category_name}' not found (existing only){RESET}")
                return None
    except Exception as e:
        print(f"{RED}Error fetching category: {e}{RESET}")
    return None

def get_or_create_tags(tag_names):
    """Get or create tags and return their IDs"""
    tag_ids = []
    try:
        headers = get_auth_header()
        for tag_name in tag_names:
            response = requests.get(
                f"{API_BASE_URL}/tags",
                params={"search": tag_name},
                headers=headers
            )
            if response.status_code == 200:
                tags = response.json()
                if tags:
                    tag_ids.append(tags[0]['id'])
                else:
                    # Create new tag if doesn't exist
                    response = requests.post(
                        f"{API_BASE_URL}/tags",
                        json={"name": tag_name},
                        headers=headers
                    )
                    if response.status_code == 201:
                        tag_ids.append(response.json()['id'])
    except Exception as e:
        print(f"{RED}Error processing tags: {e}{RESET}")
    return tag_ids

def update_post_yoast(post_id, post_data):
    """Update post with Yoast SEO metadata via post meta fields"""
    try:
        headers = get_auth_header()
        headers["Content-Type"] = "application/json"

        # Get category ID
        category_id = get_category_id(post_data["category"])
        if not category_id:
            print(f"{RED}✗ Cannot update post {post_id} - category '{post_data['category']}' not found{RESET}")
            return False

        # Get tag IDs
        tag_ids = get_or_create_tags(post_data["tags"])

        # Prepare update data with Yoast meta fields
        update_data = {
            "categories": [category_id],
            "tags": tag_ids,
            "meta": {
                "_yoast_wpseo_metadesc": post_data["meta_description"],
                "_yoast_wpseo_focuskw": post_data["focus_keyphrase"],
                "_yoast_wpseo_title": post_data.get("seo_title", post_data["title"]),
            }
        }

        # Update post
        response = requests.post(
            f"{API_BASE_URL}/posts/{post_id}",
            json=update_data,
            headers=headers
        )

        if response.status_code == 200:
            print(f"{GREEN}✓ Updated post {post_id}: {post_data['title'][:50]}{RESET}")
            print(f"  Category: {post_data['category']}")
            print(f"  Tags: {', '.join(post_data['tags'][:3])}")
            print(f"  Focus Keyphrase: {post_data['focus_keyphrase']}")
            print(f"  Meta Description: {post_data['meta_description'][:80]}...")
            return True
        else:
            print(f"{RED}✗ Failed to update post {post_id}{RESET}")
            print(f"  Status: {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return False

    except Exception as e:
        print(f"{RED}Error updating post: {e}{RESET}")
        return False

def main():
    """Main function"""
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}Yoast SEO Fix - Add Focus Keyphrases, Meta Descriptions, and Tags{RESET}")
    print(f"{BLUE}Using EXISTING Categories Only - No New Categories Created{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")

    # Articles to fix with complete Yoast metadata
    articles = [
        {
            "post_id": 7247,
            "title": "Halo Campaign Evolved Launches with Unreal Engine 5 Graphics, Seamless Zones, and Four-Player Online Co-Op",
            "category": "Gaming News",
            "tags": ["Gaming News", "Halo Campaign Evolved", "Unreal Engine 5", "First Person Shooter"],
            "focus_keyphrase": "Halo Campaign Evolved Graphics",
            "meta_description": "Halo Campaign Evolved launches with complete Unreal Engine 5 rebuild featuring Nanite/Lumen graphics, seamless zone transitions, four-player online co-op, three new missions, difficulty modifiers, and collectible Skulls.",
            "seo_title": "Halo Campaign Evolved Graphics & Unreal Engine 5 Features 2026"
        },
        {
            "post_id": 7248,
            "title": "Marvel Tokon Fighting Souls Debuts August 6 with 4v4 Tag Team Mechanics and 20-Character Launch Roster",
            "category": "Gaming News",
            "tags": ["Fighting Games", "Marvel Games", "Arc System Works", "Fighting Game News"],
            "focus_keyphrase": "Marvel Tokon Fighting Souls",
            "meta_description": "Marvel Tokon: Fighting Souls launches August 6, 2026 on PS5/PC with 4v4 tag team mechanics, 20-character roster, Vital Gauge system, Wall Breaks gameplay, and Phoenix Cyclops as first Year 1 DLC character.",
            "seo_title": "Marvel Tokon Fighting Souls: 4v4 Tag Team Fighting Game August 2026"
        },
        {
            "post_id": 7249,
            "title": "Palworld Fortnite Crossover Speculation Escalates After Epic Games Survey and 40 Million Player Achievement",
            "category": "Gaming News",
            "tags": ["Battle Royale Games", "Palworld", "Fortnite", "Gaming Crossovers"],
            "focus_keyphrase": "Palworld Fortnite Crossover Speculation",
            "meta_description": "Palworld Fortnite crossover speculation grows following Epic Games survey and developer comments. Palworld reached 40M players with 722K Steam concurrent peak, positioning it as Pokemon crossover alternative.",
            "seo_title": "Palworld Fortnite Crossover Speculation After Epic Games Survey"
        },
        {
            "post_id": 7250,
            "title": "Riot Games Suspends Valorant Pro Ardiis from VCT Co-Streaming Over Discriminatory Comments During Game Changers",
            "category": "Esports News",
            "tags": ["Esports News", "Valorant", "VCT Esports", "Esports Controversy"],
            "focus_keyphrase": "Ardiis VCT Suspension Controversy",
            "meta_description": "Riot Games suspended Valorant pro Ardiis from VCT co-streaming through August 19 after discriminatory comments during Game Changers broadcast. NAVI also suspended collaboration with the $140K earning professional.",
            "seo_title": "Ardiis VCT Suspension: Riot Games Valorant Professional Conduct"
        },
        {
            "post_id": 7251,
            "title": "EA Sports FC 27 Launches September 25 with Kylian Mbappé and Jude Bellingham as Cover Stars",
            "category": "Gaming News",
            "tags": ["Sports Games", "EA Sports FC", "Football Games", "Gaming Releases"],
            "focus_keyphrase": "EA Sports FC 27 Release",
            "meta_description": "EA Sports FC 27 launches September 25, 2026 across PC, PlayStation, Xbox, and Nintendo Switch. Kylian Mbappé returns as cover star (fourth appearance) alongside Jude Bellingham in Ultimate Plus Edition.",
            "seo_title": "EA Sports FC 27: Mbappé & Bellingham Cover Stars September Release"
        }
    ]

    print(f"{YELLOW}Total articles to fix: {len(articles)}{RESET}")
    print(f"{YELLOW}Categories: Gaming News, Esports News (EXISTING ONLY){RESET}\n")

    # Test connection
    print(f"{BLUE}Testing API connection...{RESET}")
    try:
        headers = get_auth_header()
        response = requests.get(f"{API_BASE_URL}/posts/7247", headers=headers)
        if response.status_code == 200:
            print(f"{GREEN}✓ API connection successful!{RESET}\n")
        else:
            print(f"{RED}✗ API connection failed (status {response.status_code}){RESET}")
            return False
    except Exception as e:
        print(f"{RED}✗ Connection error: {e}{RESET}")
        return False

    # Fix each article
    fixed_count = 0
    failed_count = 0

    for i, article in enumerate(articles, 1):
        print(f"{BLUE}[{i}/{len(articles)}] Processing: {article['title'][:60]}...{RESET}")

        if update_post_yoast(article["post_id"], article):
            fixed_count += 1
        else:
            failed_count += 1

        print()

    # Summary
    print(f"{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}Yoast SEO Fix Summary{RESET}")
    print(f"{BLUE}{'='*70}{RESET}")
    print(f"{GREEN}✓ Updated: {fixed_count}/{len(articles)}{RESET}")
    if failed_count > 0:
        print(f"{RED}✗ Failed: {failed_count}/{len(articles)}{RESET}")
    print(f"\nFixed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

    if fixed_count == len(articles):
        print(f"{GREEN}✓ ALL ARTICLES UPDATED WITH YOAST METADATA!{RESET}")
        print(f"\nMetadata added via REST API:")
        print(f"  ✓ Focus keyphrases")
        print(f"  ✓ Meta descriptions")
        print(f"  ✓ SEO titles")
        print(f"  ✓ Categories (existing)")
        print(f"  ✓ Tags")
        print(f"\nRemaining tasks (WordPress Admin):")
        print(f"  [ ] Add featured images to each article")
        print(f"  [ ] Set alt text on featured images")
        print(f"  [ ] Verify Yoast green checkmarks")
        return True
    else:
        print(f"{RED}✗ Some articles failed to update.{RESET}\n")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
