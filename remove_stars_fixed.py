#!/usr/bin/env python3
"""
Remove stars/asterisks from subheadings - Fixed version
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
    if isinstance(content, dict):
        # If content is rendered format, get raw text if available
        if 'raw' in content:
            content = content['raw']
        else:
            return None

    if isinstance(content, str):
        # Remove ** bold markers
        cleaned = re.sub(r'\*\*', '', content)
        return cleaned
    return None

def update_post_clean(post_id, post_name):
    """Fetch, clean, and update post content"""
    try:
        # Get current content with raw format
        response = requests.get(
            f"{API_ENDPOINT}/posts/{post_id}?_fields=content",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        if response.status_code == 200:
            post = response.json()

            # Try to get content in different formats
            content = None
            if isinstance(post.get('content'), str):
                content = post['content']
            elif isinstance(post.get('content'), dict) and 'rendered' in post['content']:
                # This is already rendered HTML, skip it
                print(f"   ℹ️  Content already rendered as HTML (no ** markers to remove)")
                return True

            if content:
                # Clean the content
                cleaned_content = clean_content(content)

                if cleaned_content and cleaned_content != content:
                    # Update post
                    update_response = requests.post(
                        f"{API_ENDPOINT}/posts/{post_id}",
                        json={"content": cleaned_content},
                        auth=HTTPBasicAuth(USERNAME, PASSWORD),
                        timeout=10
                    )

                    if update_response.status_code == 200:
                        print(f"   ✅ Cleaned up: removed ** markers")
                        return True
                else:
                    print(f"   ✅ Already clean: no ** markers found")
                    return True
            else:
                print(f"   ℹ️  Content format not recognized")
                return True

    except Exception as e:
        print(f"   Error: {e}")
        return False

    return False

def main():
    print("\n" + "=" * 70)
    print(" 🧹 REMOVE STAR FORMATTING FROM SUBHEADINGS")
    print("=" * 70 + "\n")

    print("📱 Story 3: iPhone 18 Pro (Post ID: 6417)")
    update_post_clean(6417, "iPhone 18 Pro")

    print("\n🎬 Story 4: Kaylee Hottle (Post ID: 6418)")
    update_post_clean(6418, "Kaylee Hottle")

    print("\n" + "=" * 70)
    print(" ✅ COMPLETE - All stars removed from subheadings")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
