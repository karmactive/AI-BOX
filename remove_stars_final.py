#!/usr/bin/env python3
"""
Remove stars/asterisks from subheadings in published content
"""

import requests
import re
from requests.auth import HTTPBasicAuth

SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def clean_content(content):
    """Remove ** (bold) markers from subheadings"""
    # Remove ** from bold subheadings
    cleaned = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
    # Remove standalone asterisks
    cleaned = re.sub(r'^\s*\*+\s*$', '', cleaned, flags=re.MULTILINE)
    return cleaned

def update_post_clean(post_id):
    """Fetch, clean, and update post content"""
    try:
        # Get current content
        response = requests.get(
            f"{API_ENDPOINT}/posts/{post_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if response.status_code == 200:
            post = response.json()
            original_content = post.get('content', '')

            # Clean the content
            cleaned_content = clean_content(original_content)

            # Update post
            update_response = requests.post(
                f"{API_ENDPOINT}/posts/{post_id}",
                json={"content": cleaned_content},
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                timeout=10
            )

            if update_response.status_code == 200:
                return True
            else:
                print(f"Update error: {update_response.status_code}")
                return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("\n" + "=" * 70)
    print(" 🧹 REMOVING STARS FROM SUBHEADINGS")
    print("=" * 70 + "\n")

    print("📱 Story 3: iPhone 18 Pro (Post ID: 6417)")
    if update_post_clean(6417):
        print("   ✅ Stars removed from subheadings")
    else:
        print("   ⚠️ Could not update")

    print("\n🎬 Story 4: Kaylee Hottle (Post ID: 6418)")
    if update_post_clean(6418):
        print("   ✅ Stars removed from subheadings")
    else:
        print("   ⚠️ Could not update")

    print("\n" + "=" * 70)
    print(" ✅ CLEANUP COMPLETE")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
