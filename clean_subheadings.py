#!/usr/bin/env python3
"""
Remove ** (bold/star) formatting from subheadings in article body
"""

import requests
import re
from requests.auth import HTTPBasicAuth

SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def remove_stars_from_subheadings(html_content):
    """
    Remove ** from subheadings while preserving HTML structure
    """
    # Remove ** from paragraphs that look like subheadings (usually short, bold lines)
    # Pattern: <p>**text**</p> → <p>text</p>
    cleaned = re.sub(r'<p><strong>(.*?)</strong></p>', r'<p>\1</p>', html_content)
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', cleaned)
    return cleaned

def update_post_content(post_id, post_name):
    """Fetch, clean and update post content"""
    try:
        print(f"\n{post_name}")
        print("-" * 70)

        # Get post with edit context to get raw content
        response = requests.get(
            f"{API_ENDPOINT}/posts/{post_id}?context=edit",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=15
        )

        if response.status_code == 200:
            post = response.json()
            content = post.get('content')

            if isinstance(content, dict):
                raw_content = content.get('raw', '')
            else:
                raw_content = content

            print(f"Original content length: {len(raw_content)} chars")

            # Clean the content
            cleaned_content = remove_stars_from_subheadings(raw_content)

            print(f"Cleaned content length: {len(cleaned_content)} chars")

            # Show what changed
            if cleaned_content != raw_content:
                print(f"✅ Changes detected: Removing ** from subheadings...")

                # Update the post
                update_response = requests.post(
                    f"{API_ENDPOINT}/posts/{post_id}",
                    json={"content": cleaned_content},
                    auth=HTTPBasicAuth(USERNAME, PASSWORD),
                    headers={"Content-Type": "application/json"},
                    timeout=15
                )

                if update_response.status_code == 200:
                    print(f"✅ Successfully updated post {post_id}")
                    return True
                else:
                    print(f"❌ Update failed: Status {update_response.status_code}")
                    print(f"   Response: {update_response.text[:200]}")
                    return False
            else:
                print(f"✅ Already clean: No ** markers found")
                return True

        else:
            print(f"❌ Could not fetch post: Status {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    print("\n" + "=" * 70)
    print(" 🧹 REMOVE STARS (*) FROM SUBHEADINGS IN ARTICLE BODY")
    print("=" * 70)

    print("\n📱 STORY 3: iPhone 18 Pro (Post ID: 6417)")
    result1 = update_post_content(6417, "iPhone 18 Pro Camera & Chip Upgrade")

    print("\n🎬 STORY 4: Kaylee Hottle (Post ID: 6418)")
    result2 = update_post_content(6418, "Kaylee Hottle - Godzilla vs Kong Actress")

    print("\n" + "=" * 70)
    if result1 and result2:
        print("✅ ALL SUBHEADINGS CLEANED - Stars removed from both stories!")
    else:
        print("⚠️ Some posts need review")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
