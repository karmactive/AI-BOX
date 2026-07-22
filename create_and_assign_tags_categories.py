#!/usr/bin/env python3
"""
Create Tags and Categories if they don't exist, then assign to posts
NewsPandit.com WordPress REST API
"""

import requests
import json
from requests.auth import HTTPBasicAuth

# Configuration
SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def get_or_create_category(name):
    """Get category ID or create if doesn't exist"""
    try:
        # First search for existing category
        search_response = requests.get(
            f"{API_ENDPOINT}/categories?search={name}&per_page=100",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if search_response.status_code == 200:
            categories = search_response.json()
            if categories:
                print(f"  Found existing category: {name} (ID: {categories[0]['id']})")
                return categories[0]['id']

        # Create new category
        create_response = requests.post(
            f"{API_ENDPOINT}/categories",
            json={"name": name},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if create_response.status_code in [200, 201]:
            cat_id = create_response.json()['id']
            print(f"  Created new category: {name} (ID: {cat_id})")
            return cat_id
    except Exception as e:
        print(f"  Error: {e}")

    return None

def get_or_create_tag(name):
    """Get tag ID or create if doesn't exist"""
    try:
        # First search for existing tag
        search_response = requests.get(
            f"{API_ENDPOINT}/tags?search={name}&per_page=100",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if search_response.status_code == 200:
            tags = search_response.json()
            if tags:
                print(f"  Found existing tag: {name} (ID: {tags[0]['id']})")
                return tags[0]['id']

        # Create new tag
        create_response = requests.post(
            f"{API_ENDPOINT}/tags",
            json={"name": name},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if create_response.status_code in [200, 201]:
            tag_id = create_response.json()['id']
            print(f"  Created new tag: {name} (ID: {tag_id})")
            return tag_id
    except Exception as e:
        print(f"  Error: {e}")

    return None

def assign_to_post(post_id, categories, tags):
    """Assign categories and tags to a post"""
    try:
        data = {
            "categories": categories,
            "tags": tags
        }

        response = requests.post(
            f"{API_ENDPOINT}/posts/{post_id}",
            json=data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            actual_cats = result.get('categories', [])
            actual_tags = result.get('tags', [])
            print(f"  ✅ Assigned to post {post_id}")
            print(f"     Categories: {actual_cats}")
            print(f"     Tags: {actual_tags}")
            return True
        else:
            print(f"  ❌ Status {response.status_code}: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"  Error: {e}")
        return False

def main():
    print("\n" + "=" * 90)
    print(" 🏷️  CREATE & ASSIGN TAGS AND CATEGORIES")
    print("=" * 90 + "\n")

    # Story 3: iPhone 18 Pro Categories
    print("📱 STORY 3: iPhone 18 Pro (Post ID: 6417)")
    print("-" * 90)
    print("Creating/Finding Categories...")

    story3_categories = []
    for cat_name in ["Technology", "Apple", "Smartphones"]:
        cat_id = get_or_create_category(cat_name)
        if cat_id:
            story3_categories.append(cat_id)

    print("\nCreating/Finding Tags...")
    story3_tags = []
    for tag_name in ["iPhone 18 Pro", "Apple Camera", "A18 Pro Chip", "Smartphone Technology", "Apple Leak"]:
        tag_id = get_or_create_tag(tag_name)
        if tag_id:
            story3_tags.append(tag_id)

    print("\nAssigning to Post...")
    assign_to_post(6417, story3_categories, story3_tags)

    print("\n")

    # Story 4: Kaylee Hottle Categories
    print("🎬 STORY 4: Kaylee Hottle (Post ID: 6418)")
    print("-" * 90)
    print("Creating/Finding Categories...")

    story4_categories = []
    for cat_name in ["Entertainment", "Hollywood News", "Celebrity News"]:
        cat_id = get_or_create_category(cat_name)
        if cat_id:
            story4_categories.append(cat_id)

    print("\nCreating/Finding Tags...")
    story4_tags = []
    for tag_name in ["Kaylee Hottle", "Godzilla vs Kong", "Hollywood Actress", "Celebrity Death", "Entertainment News"]:
        tag_id = get_or_create_tag(tag_name)
        if tag_id:
            story4_tags.append(tag_id)

    print("\nAssigning to Post...")
    assign_to_post(6418, story4_categories, story4_tags)

    print("\n" + "=" * 90)
    print(" ✅ TAGS AND CATEGORIES ASSIGNMENT COMPLETE")
    print("=" * 90)
    print("\nBoth posts should now display categories and tags in WordPress Admin.\n")

if __name__ == "__main__":
    main()
