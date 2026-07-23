#!/usr/bin/env python3
"""
Assign Categories and Tags to Stories 5 & 6
"""

import requests
from requests.auth import HTTPBasicAuth

SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def get_or_create_category(name):
    """Get or create category"""
    try:
        search_response = requests.get(
            f"{API_ENDPOINT}/categories?search={name}&per_page=100",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if search_response.status_code == 200:
            categories = search_response.json()
            if categories:
                print(f"  Found: {name} (ID: {categories[0]['id']})")
                return categories[0]['id']

        create_response = requests.post(
            f"{API_ENDPOINT}/categories",
            json={"name": name},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if create_response.status_code in [200, 201]:
            cat_id = create_response.json()['id']
            print(f"  Created: {name} (ID: {cat_id})")
            return cat_id
    except Exception as e:
        print(f"  Error: {e}")
    return None

def get_or_create_tag(name):
    """Get or create tag"""
    try:
        search_response = requests.get(
            f"{API_ENDPOINT}/tags?search={name}&per_page=100",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if search_response.status_code == 200:
            tags = search_response.json()
            if tags:
                print(f"  Found: {name} (ID: {tags[0]['id']})")
                return tags[0]['id']

        create_response = requests.post(
            f"{API_ENDPOINT}/tags",
            json={"name": name},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if create_response.status_code in [200, 201]:
            tag_id = create_response.json()['id']
            print(f"  Created: {name} (ID: {tag_id})")
            return tag_id
    except Exception as e:
        print(f"  Error: {e}")
    return None

def assign_to_post(post_id, categories, tags):
    """Assign to post"""
    try:
        response = requests.post(
            f"{API_ENDPOINT}/posts/{post_id}",
            json={"categories": categories, "tags": tags},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if response.status_code == 200:
            print(f"  ✅ Assigned to post {post_id}")
            return True
        else:
            print(f"  ⚠️ Status {response.status_code}")
            return False
    except Exception as e:
        print(f"  Error: {e}")
        return False

def main():
    print("\n" + "=" * 70)
    print(" 🏷️  ASSIGN TAGS AND CATEGORIES TO STORIES 5 & 6")
    print("=" * 70 + "\n")

    # Story 5: El Nino
    print("🌍 STORY 5: El Nino Impact (Post ID: 6436)")
    print("-" * 70)
    print("Creating Categories...")

    story5_categories = []
    for cat in ["Agriculture", "Weather News", "Government News"]:
        cat_id = get_or_create_category(cat)
        if cat_id:
            story5_categories.append(cat_id)

    print("Creating Tags...")
    story5_tags = []
    for tag in ["El Nino", "Monsoon", "Agriculture Crisis", "Farmers", "Climate Change"]:
        tag_id = get_or_create_tag(tag)
        if tag_id:
            story5_tags.append(tag_id)

    print("Assigning to Post...")
    assign_to_post(6436, story5_categories, story5_tags)

    print()

    # Story 6: PM Kisan
    print("💰 STORY 6: PM Kisan Yojana (Post ID: 6437)")
    print("-" * 70)
    print("Creating Categories...")

    story6_categories = []
    for cat in ["Agriculture", "Government Schemes", "Farmer Benefits"]:
        cat_id = get_or_create_category(cat)
        if cat_id:
            story6_categories.append(cat_id)

    print("Creating Tags...")
    story6_tags = []
    for tag in ["PM Kisan", "Kisan Yojana", "Farmer Payment", "Government Scheme", "Farmer Benefits"]:
        tag_id = get_or_create_tag(tag)
        if tag_id:
            story6_tags.append(tag_id)

    print("Assigning to Post...")
    assign_to_post(6437, story6_categories, story6_tags)

    print("\n" + "=" * 70)
    print(" ✅ COMPLETE - Tags and Categories Assigned!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
