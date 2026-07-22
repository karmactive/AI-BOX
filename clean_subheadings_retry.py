#!/usr/bin/env python3
"""
Remove ** (bold/star) formatting from subheadings - Retry with longer timeout
"""

import requests
import re
import time
from requests.auth import HTTPBasicAuth

SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def clean_subheadings(text):
    """Remove ** from subheadings"""
    # Remove ** bold formatting
    return re.sub(r'\*\*(.+?)\*\*', r'\1', text)

def update_post(post_id, post_name):
    """Update post to remove ** from subheadings"""
    try:
        print(f"\n{post_name} (Post ID: {post_id})")
        print("-" * 70)
        print("Fetching content...")

        # Get post with longer timeout
        response = requests.get(
            f"{API_ENDPOINT}/posts/{post_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=30
        )

        if response.status_code == 200:
            post = response.json()
            content = post.get('content', '')

            print(f"✅ Fetched content ({len(str(content))} chars)")

            # Clean content
            if isinstance(content, str):
                cleaned = clean_subheadings(content)
            elif isinstance(content, dict) and 'rendered' in content:
                # Content is pre-rendered HTML
                cleaned = clean_subheadings(content['rendered'])
            else:
                cleaned = str(content)

            print(f"🧹 Cleaning subheadings...")

            # Update post
            print(f"📤 Uploading cleaned content...")
            update_response = requests.post(
                f"{API_ENDPOINT}/posts/{post_id}",
                json={"content": cleaned},
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                timeout=30
            )

            if update_response.status_code == 200:
                print(f"✅ Successfully updated - Stars removed from subheadings!")
                return True
            else:
                print(f"⚠️ Status {update_response.status_code}")
                return False

        else:
            print(f"❌ Could not fetch: Status {response.status_code}")
            return False

    except requests.exceptions.Timeout:
        print(f"⏱️ Request timed out - retrying...")
        time.sleep(2)
        return update_post(post_id, post_name)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    print("\n" + "=" * 70)
    print(" 🧹 REMOVE STARS FROM SUBHEADINGS")
    print("=" * 70)

    result1 = update_post(6417, "📱 Story 3: iPhone 18 Pro")
    time.sleep(1)
    result2 = update_post(6418, "🎬 Story 4: Kaylee Hottle")

    print("\n" + "=" * 70)
    if result1 and result2:
        print("✅ COMPLETE - All stars removed from subheadings!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
