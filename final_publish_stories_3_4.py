#!/usr/bin/env python3
"""
Final Publishing Script for Stories 3 & 4
Extracts content from markdown files and publishes to NewsPandit.com
July 22, 2026
"""

import requests
import json
import re
from requests.auth import HTTPBasicAuth

# Configuration
SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "admin"
PASSWORD = "NewsPandit@2026"

def extract_article_content(filename):
    """Extract article content from markdown file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the article content section
        match = re.search(r'## ARTICLE CONTENT \(HINDI.*?\n(.*?)\n---', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def publish_story(title, content, slug, excerpt, categories, tags, seo_meta):
    """Publish a story to NewsPandit.com via WordPress REST API"""

    post_data = {
        "title": title,
        "content": content,
        "excerpt": excerpt,
        "slug": slug,
        "status": "publish",
        "categories": categories,
        "tags": tags,
        "meta": seo_meta
    }

    try:
        print(f"  Publishing: {title[:50]}...")
        response = requests.post(
            f"{API_ENDPOINT}/posts",
            json=post_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        if response.status_code in [200, 201]:
            result = response.json()
            post_id = result.get("id")
            permalink = result.get("link", "N/A")
            print(f"  ✅ Published! Post ID: {post_id}")
            print(f"     URL: {permalink}")
            return post_id
        else:
            print(f"  ❌ Status {response.status_code}: {response.text[:100]}")
            return None
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return None

def main():
    print("\n" + "=" * 80)
    print(" PUBLISHING STORIES 3 & 4 TO NEWSPANDIT.COM")
    print("=" * 80 + "\n")

    # STORY 3: iPhone 18 Pro
    print("📱 STORY 3: iPhone 18 Pro Camera & Chip Upgrade")
    print("-" * 80)

    story3_content = extract_article_content('/home/user/AI-BOX/STORY3_IPHONE_18_PRO_CAMERA_CHIP_UPGRADE.md')

    if story3_content:
        story3_id = publish_story(
            title="iPhone 18 Pro में आएगा शानदार कैमरा अपग्रेड - कीमत बढ़ेगी 300 डॉलर तक",
            content=story3_content,
            slug="iphone-18-pro-camera-chip-upgrade-lens-a18-2026",
            excerpt="iPhone 18 Pro में आएगा वेरिएबल अपरचर सेंसर, A18 Pro चिप और 12x ऑप्टिकल जूम कैमरा। कीमत में 300 डॉलर तक इजाफा हो सकता है।",
            categories=[789],  # Technology
            tags=[1001, 1002, 1003, 1004, 1005],  # Tags
            seo_meta={
                "_yoast_wpseo_focuskw": "iPhone 18 Pro camera upgrade",
                "_yoast_wpseo_title": "iPhone 18 Pro में आएगा शानदार कैमरा अपग्रेड - कीमत बढ़ेगी 300 डॉलर तक",
                "_yoast_wpseo_metadesc": "iPhone 18 Pro में आएगा वेरिएबल अपरचर सेंसर, A18 Pro चिप और 12x ऑप्टिकल जूम कैमरा। कीमत में 300 डॉलर तक इजाफा हो सकता है।"
            }
        )
    else:
        print("  ❌ Failed to extract content from markdown file")
        story3_id = None

    print()

    # STORY 4: Kaylee Hottle
    print("🎬 STORY 4: Kaylee Hottle - Godzilla vs Kong Actress Death")
    print("-" * 80)

    story4_content = extract_article_content('/home/user/AI-BOX/STORY4_KAYLEE_HOTTLE_ACTRESS_DEATH.md')

    if story4_content:
        story4_id = publish_story(
            title="Kaylee Hottle की दुःखद मौत - 'Godzilla vs Kong' की 18 साल की अभिनेत्री कार क्रैश में चली गईं",
            content=story4_content,
            slug="kaylee-hottle-actress-death-godzilla-kong-car-crash-2026",
            excerpt="Kaylee Hottle, 'Godzilla x Kong' की अभिनेत्री, कार क्रैश में 18 साल की उम्र में चली गईं। हॉलीवुड में गहरी शोक की लहर है।",
            categories=[534],  # Entertainment
            tags=[2001, 2002, 2003, 2004, 2005],  # Tags
            seo_meta={
                "_yoast_wpseo_focuskw": "Kaylee Hottle actress death",
                "_yoast_wpseo_title": "Kaylee Hottle की दुःखद मौत - 'Godzilla vs Kong' की 18 साल की अभिनेत्री",
                "_yoast_wpseo_metadesc": "Kaylee Hottle, 'Godzilla x Kong' की अभिनेत्री, कार क्रैश में 18 साल की उम्र में चली गईं। हॉलीवुड में गहरी शोक की लहर है।"
            }
        )
    else:
        print("  ❌ Failed to extract content from markdown file")
        story4_id = None

    print()
    print("=" * 80)
    print(" PUBLISHING SUMMARY")
    print("=" * 80)

    if story3_id:
        print(f"✅ Story 3 (iPhone 18 Pro): Published as Post ID {story3_id}")
    else:
        print(f"❌ Story 3 (iPhone 18 Pro): Failed to publish")

    if story4_id:
        print(f"✅ Story 4 (Kaylee Hottle): Published as Post ID {story4_id}")
    else:
        print(f"❌ Story 4 (Kaylee Hottle): Failed to publish")

    print("=" * 80 + "\n")

    return story3_id and story4_id

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
