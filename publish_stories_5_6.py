#!/usr/bin/env python3
"""
Publishing Script for Stories 5 & 6
El Nino Impact & PM Kisan Yojana Updates
NewsPandit.com WordPress REST API
"""

import requests
import re
from requests.auth import HTTPBasicAuth

# Configuration
SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "NewsPandit Staff"
PASSWORD = "GSIf avuF lFp3 2ZtN aSQx iAMQ"

def extract_article_content(filename):
    """Extract article content from markdown file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the article content section (with anchor links)
        match = re.search(r'## ARTICLE CONTENT.*?\n(.*?)\n\n---', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def publish_story(title, content, slug, excerpt, categories, tags, seo_meta):
    """Publish a story to NewsPandit.com"""
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
        print(f"  📤 Publishing: {title[:60]}...")
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
            print(f"     ✅ SUCCESS! Post ID: {post_id}")
            print(f"     🔗 URL: {permalink}")
            return post_id
        else:
            print(f"     ❌ Status {response.status_code}")
            print(f"     Response: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"     ❌ Error: {str(e)}")
        return None

def main():
    print("\n" + "=" * 90)
    print(" 🚀 PUBLISHING STORIES 5 & 6 TO NEWSPANDIT.COM")
    print("=" * 90 + "\n")

    # STORY 5: El Nino Impact
    print("🌍 STORY 5: El Nino Impact on Agriculture (Post ID: auto)")
    print("-" * 90)

    story5_content = extract_article_content('/home/user/AI-BOX/STORY5_EL_NINO_IMPACT_AGRICULTURE.md')

    if story5_content:
        story5_id = publish_story(
            title="एल-नीनो का सबसे खतरनाक रूप दिखेगा - भारतीय कृषि पर गंभीर संकट",
            content=story5_content,
            slug="el-nino-impact-indian-agriculture-monsoon-2026",
            excerpt="भारतीय मौसम विभाग ने चेतावनी दी है कि इस बार का एल-नीनो सबसे खतरनाक रूप में दिखेगा। देश के विभिन्न हिस्सों में बारिश के पैटर्न में बड़ा बदलाव आने वाला है।",
            categories=[150, 151, 152],  # Agriculture, Weather, Government News
            tags=[1501, 1502, 1503, 1504, 1505],  # El Nino, Monsoon, Agriculture Crisis, Farmers, Climate
            seo_meta={
                "_yoast_wpseo_focuskw": "El Nino impact agriculture monsoon",
                "_yoast_wpseo_title": "एल-नीनो का सबसे खतरनाक रूप दिखेगा - भारतीय कृषि पर गंभीर संकट",
                "_yoast_wpseo_metadesc": "भारतीय मौसम विभाग ने चेतावनी दी है कि इस बार का एल-नीनो सबसे खतरनाक रूप में दिखेगा। कृषि पर 70% असर पड़ सकता है।"
            }
        )
    else:
        print("  ❌ Failed to extract content")
        story5_id = None

    print()

    # STORY 6: PM Kisan Yojana
    print("💰 STORY 6: PM Kisan Yojana 24th Installment (Post ID: auto)")
    print("-" * 90)

    story6_content = extract_article_content('/home/user/AI-BOX/STORY6_PM_KISAN_YOJANA_24TH_INSTALLMENT.md')

    if story6_content:
        story6_id = publish_story(
            title="PM किसान 24वीं किस्त: ₹2,000 पाने के लिए आज ही करें ये 3 काम",
            content=story6_content,
            slug="pm-kisan-24th-installment-update-2000-rupees-farmers-2026",
            excerpt="PM Kisan Yojana का 24वां किस्त जल्द ही आने वाला है। किसानों को ₹2,000 की राशि मिलेगी। 24वीं किस्त के लिए आवेदन की प्रक्रिया चल रही है।",
            categories=[150, 153, 154],  # Agriculture, Government Schemes, Farmer Benefits
            tags=[1506, 1507, 1508, 1509, 1510],  # PM Kisan, Kisan Yojana, Farmer Payment, Government Scheme, Farmer Benefits
            seo_meta={
                "_yoast_wpseo_focuskw": "PM Kisan 24th installment update farmers",
                "_yoast_wpseo_title": "PM किसान 24वीं किस्त: ₹2,000 पाने के लिए आज ही करें ये 3 काम",
                "_yoast_wpseo_metadesc": "PM Kisan Yojana का 24वां किस्त आने वाला है। ₹2,000 पाने के लिए आधार वेरिफिकेशन, बैंक अकाउंट अपडेट करें।"
            }
        )
    else:
        print("  ❌ Failed to extract content")
        story6_id = None

    print()
    print("=" * 90)
    print(" ✅ PUBLISHING COMPLETE")
    print("=" * 90)
    print()

    if story5_id and story6_id:
        print(f"🎉 BOTH STORIES PUBLISHED SUCCESSFULLY!")
        print()
        print(f"   🌍 Story 5 (El Nino Impact)")
        print(f"      Post ID: {story5_id}")
        print(f"      URL: https://newspandit.com/el-nino-impact-indian-agriculture-monsoon-2026/")
        print()
        print(f"   💰 Story 6 (PM Kisan Yojana)")
        print(f"      Post ID: {story6_id}")
        print(f"      URL: https://newspandit.com/pm-kisan-24th-installment-update-2000-rupees-farmers-2026/")
        print()
        return True
    else:
        if story5_id:
            print(f"✅ Story 5 (El Nino): Published as Post ID {story5_id}")
        else:
            print(f"❌ Story 5 (El Nino): Failed to publish")

        if story6_id:
            print(f"✅ Story 6 (PM Kisan): Published as Post ID {story6_id}")
        else:
            print(f"❌ Story 6 (PM Kisan): Failed to publish")

        return False

if __name__ == "__main__":
    success = main()
    print("=" * 90 + "\n")
    exit(0 if success else 1)
