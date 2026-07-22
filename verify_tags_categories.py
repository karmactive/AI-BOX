#!/usr/bin/env python3
"""
Verify that tags and categories were successfully assigned
"""

import requests
from requests.auth import HTTPBasicAuth

SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def verify_post(post_id, post_name):
    """Verify categories and tags for a post"""
    try:
        response = requests.get(
            f"{API_ENDPOINT}/posts/{post_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if response.status_code == 200:
            post = response.json()
            categories = post.get('categories', [])
            tags = post.get('tags', [])

            print(f"\n{post_name}")
            print("-" * 60)
            print(f"Post ID: {post_id}")
            print(f"Categories: {categories if categories else '❌ MISSING'}")
            print(f"Tags: {tags if tags else '❌ MISSING'}")

            if categories and tags:
                print("✅ All set!")
                return True
            else:
                print("⚠️ Some data missing")
                return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("\n" + "=" * 60)
    print("VERIFICATION: Tags and Categories Status")
    print("=" * 60)

    result1 = verify_post(6417, "📱 Story 3: iPhone 18 Pro")
    result2 = verify_post(6418, "🎬 Story 4: Kaylee Hottle")

    print("\n" + "=" * 60)
    if result1 and result2:
        print("✅ VERIFICATION SUCCESSFUL - Both posts have categories and tags!")
    else:
        print("⚠️ Some posts still missing data - trying fallback method...")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
