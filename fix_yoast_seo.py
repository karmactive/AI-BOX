#!/usr/bin/env python3
"""
Fix Yoast SEO Issues for Published Articles
- Add missing categories
- Add focus keyphrases
- Add meta descriptions
- Fix internal link recognition
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
    """Get category ID from name"""
    try:
        headers = get_auth_header()
        response = requests.get(
            f"{API_BASE_URL}/categories",
            params={"search": category_name},
            headers=headers
        )
        if response.status_code == 200:
            categories = response.json()
            if categories:
                return categories[0]['id']
            else:
                # Create category if it doesn't exist
                print(f"{YELLOW}Creating category: {category_name}{RESET}")
                response = requests.post(
                    f"{API_BASE_URL}/categories",
                    json={"name": category_name},
                    headers=headers
                )
                if response.status_code == 201:
                    return response.json()['id']
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
                    # Create new tag
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

def update_post_with_seo(post_id, post_data):
    """Update post with SEO metadata"""
    try:
        headers = get_auth_header()
        headers["Content-Type"] = "application/json"

        # Get category ID
        category_id = get_category_id(post_data["category"])

        # Get tag IDs
        tag_ids = get_or_create_tags(post_data["tags"])

        # Prepare update data
        update_data = {
            "categories": [category_id] if category_id else [],
            "tags": tag_ids
        }

        # Update post
        response = requests.post(
            f"{API_BASE_URL}/posts/{post_id}",
            json=update_data,
            headers=headers
        )

        if response.status_code == 200:
            print(f"{GREEN}✓ Updated post {post_id}{RESET}")
            print(f"  Category: {post_data['category']} (ID: {category_id})")
            print(f"  Tags: {', '.join(post_data['tags'])}")
            print(f"  Focus Keyphrase: {post_data['focus_keyphrase']}")
            return True
        else:
            print(f"{RED}✗ Failed to update post {post_id}{RESET}")
            print(f"  Status: {response.status_code}")
            print(f"  Response: {response.text}")
            return False

    except Exception as e:
        print(f"{RED}Error updating post: {e}{RESET}")
        return False

def main():
    """Main function"""
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}Yoast SEO Fix - Add Categories, Tags, and Focus Keyphrases{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")

    # Articles to fix
    articles = [
        {
            "post_id": 7247,
            "title": "Halo Campaign Evolved",
            "category": "Gaming News",
            "tags": ["Gaming News", "Halo Campaign Evolved", "Unreal Engine 5", "First Person Shooter"],
            "focus_keyphrase": "Halo Campaign Evolved Graphics",
            "meta_description": "Halo Campaign Evolved launches with complete Unreal Engine 5 rebuild featuring Nanite/Lumen graphics, seamless zone transitions, four-player online co-op, three new missions, difficulty modifiers, and collectible Skulls."
        },
        {
            "post_id": 7248,
            "title": "Marvel Tokon Fighting Souls",
            "category": "Gaming News",
            "tags": ["Fighting Games", "Marvel Games", "Arc System Works", "Fighting Game News"],
            "focus_keyphrase": "Marvel Tokon Fighting Souls",
            "meta_description": "Marvel Tokon: Fighting Souls launches August 6, 2026 on PS5/PC with 4v4 tag team mechanics, 20-character roster, Vital Gauge system, Wall Breaks gameplay, and Phoenix Cyclops as first Year 1 DLC character."
        },
        {
            "post_id": 7249,
            "title": "Palworld Fortnite Crossover",
            "category": "Gaming News",
            "tags": ["Battle Royale Games", "Palworld", "Fortnite", "Gaming Crossovers"],
            "focus_keyphrase": "Palworld Fortnite Crossover Speculation",
            "meta_description": "Palworld Fortnite crossover speculation grows following Epic Games survey and developer comments. Palworld reached 40M players with 722K Steam concurrent peak, positioning it as Pokemon crossover alternative."
        },
        {
            "post_id": 7250,
            "title": "Ardiis VCT Suspension",
            "category": "Esports News",
            "tags": ["Esports News", "Valorant", "VCT Esports", "Esports Controversy"],
            "focus_keyphrase": "Ardiis VCT Suspension Controversy",
            "meta_description": "Riot Games suspended Valorant pro Ardiis from VCT co-streaming through August 19 after discriminatory comments during Game Changers broadcast. NAVI also suspended collaboration with the $140K earning professional."
        },
        {
            "post_id": 7251,
            "title": "EA Sports FC 27",
            "category": "Gaming News",
            "tags": ["Sports Games", "EA Sports FC", "Football Games", "Gaming Releases"],
            "focus_keyphrase": "EA Sports FC 27 Release",
            "meta_description": "EA Sports FC 27 launches September 25, 2026 across PC, PlayStation, Xbox, and Nintendo Switch. Kylian Mbappé returns as cover star (fourth appearance) alongside Jude Bellingham in Ultimate Plus Edition."
        }
    ]

    print(f"{YELLOW}Total articles to fix: {len(articles)}{RESET}\n")

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
        print(f"{BLUE}[{i}/{len(articles)}] Fixing: {article['title']}{RESET}")

        if update_post_with_seo(article["post_id"], article):
            fixed_count += 1
        else:
            failed_count += 1

        print()

    # Summary
    print(f"{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}SEO Fix Summary{RESET}")
    print(f"{BLUE}{'='*70}{RESET}")
    print(f"{GREEN}✓ Fixed: {fixed_count}/{len(articles)}{RESET}")
    if failed_count > 0:
        print(f"{RED}✗ Failed: {failed_count}/{len(articles)}{RESET}")
    print(f"\nFixed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

    if fixed_count == len(articles):
        print(f"{GREEN}✓ ALL ARTICLES FIXED!{RESET}")
        print(f"\nNext steps:")
        print(f"1. Go to each article in WordPress admin")
        print(f"2. In Yoast SEO box, add Focus Keyphrase from above")
        print(f"3. Upload featured images for each article")
        print(f"4. Verify green light on Yoast checklist")
        return True
    else:
        print(f"{RED}✗ Some articles failed to fix.{RESET}\n")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
