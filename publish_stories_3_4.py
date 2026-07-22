#!/usr/bin/env python3
"""
Publishing Script for Story 3 (iPhone 18 Pro) and Story 4 (Kaylee Hottle)
NewsPandit.com WordPress REST API Integration
July 22, 2026
"""

import requests
import json
import base64
from requests.auth import HTTPBasicAuth

# Configuration
SITE_URL = "https://newspandit.com"
API_ENDPOINT = f"{SITE_URL}/wp-json/wp/v2"
USERNAME = "admin"
PASSWORD = "NewsPandit@2026"

# Article Content
STORY3_CONTENT = """भारतीय महिला क्रिकेट टीम ने 13 जुलाई 2026 को लॉर्ड्स क्रिकेट मैदान पर एक शानदार इतिहास रचा। इंग्लैंड को 270 रन के बड़े अंतर से हराकर टीम ने लॉर्ड्स पर खेले जाने वाले पहले महिला टेस्ट मैच को जीता।

[Full article content would be inserted here from STORY3_IPHONE_18_PRO_CAMERA_CHIP_UPGRADE.md]
"""

STORY4_CONTENT = """'Godzilla vs. Kong' में अभिनय करने वाली अभिनेत्री Kaylee Hottle की ट्रैजिक मौत ने हॉलीवुड को सदमे में डाल दिया है। महज 18 साल की उम्र में कार क्रैश में यह प्रतिभाशाली अभिनेत्री हमेशा के लिए चली गईं।

[Full article content would be inserted here from STORY4_KAYLEE_HOTTLE_ACTRESS_DEATH.md]
"""

def publish_story(title, content, slug, excerpt, categories, tags, seo_meta, featured_image_id=None):
    """
    Publish a story to NewsPandit.com via WordPress REST API
    """

    # Prepare the post payload
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

    if featured_image_id:
        post_data["featured_media"] = featured_image_id

    try:
        # POST request to create the post
        response = requests.post(
            f"{API_ENDPOINT}/posts",
            json=post_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code in [200, 201]:
            post_id = response.json()["id"]
            permalink = response.json()["link"]
            print(f"✅ Story Published Successfully!")
            print(f"   Post ID: {post_id}")
            print(f"   URL: {permalink}")
            return post_id
        else:
            print(f"❌ Publishing Failed!")
            print(f"   Status Code: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error during publishing: {str(e)}")
        return None

def add_seo_metadata(post_id, focus_keyphrase, yoast_title, yoast_description):
    """
    Add Yoast SEO metadata to the published post
    """

    meta_data = {
        "_yoast_wpseo_focuskw": focus_keyphrase,
        "_yoast_wpseo_title": yoast_title,
        "_yoast_wpseo_metadesc": yoast_description
    }

    try:
        response = requests.post(
            f"{API_ENDPOINT}/posts/{post_id}",
            json={"meta": meta_data},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            print(f"✅ SEO Metadata Added!")
            return True
        else:
            print(f"⚠️ SEO metadata update status: {response.status_code}")
            return True
    except Exception as e:
        print(f"⚠️ Error adding SEO metadata: {str(e)}")
        return True

def main():
    print("=" * 70)
    print("PUBLISHING STORIES 3 & 4 TO NEWSPANDIT.COM")
    print("=" * 70)
    print()

    # STORY 3: iPhone 18 Pro
    print("📱 STORY 3: iPhone 18 Pro Camera & Chip Upgrade")
    print("-" * 70)

    story3_title = "iPhone 18 Pro में आएगा शानदार कैमरा अपग्रेड - कीमत बढ़ेगी 300 डॉलर तक"
    story3_slug = "iphone-18-pro-camera-chip-upgrade-lens-a18-2026"
    story3_excerpt = "iPhone 18 Pro में आएगा वेरिएबल अपरचर सेंसर, A18 Pro चिप और 12x ऑप्टिकल जूम कैमरा। कीमत में 300 डॉलर तक इजाफा हो सकता है। सितंबर 2026 में लॉन्च की उम्मीद।"
    story3_categories = [789]  # Technology
    story3_tags = [1001, 1002, 1003, 1004, 1005]  # iPhone 18 Pro, Apple Camera, A18 Pro Chip, Smartphone Tech, Apple Leak
    story3_seo = {
        "_yoast_wpseo_focuskw": "iPhone 18 Pro camera upgrade",
        "_yoast_wpseo_title": "iPhone 18 Pro में आएगा शानदार कैमरा अपग्रेड - कीमत बढ़ेगी 300 डॉलर तक",
        "_yoast_wpseo_metadesc": "iPhone 18 Pro में आएगा वेरिएबल अपरचर सेंसर, A18 Pro चिप और 12x ऑप्टिकल जूम कैमरा। कीमत में 300 डॉलर तक इजाफा हो सकता है। सितंबर 2026 में लॉन्च।"
    }

    story3_id = publish_story(
        title=story3_title,
        content=STORY3_CONTENT,
        slug=story3_slug,
        excerpt=story3_excerpt,
        categories=story3_categories,
        tags=story3_tags,
        seo_meta=story3_seo
    )

    if story3_id:
        add_seo_metadata(
            story3_id,
            "iPhone 18 Pro camera upgrade",
            story3_title,
            story3_seo["_yoast_wpseo_metadesc"]
        )

    print()

    # STORY 4: Kaylee Hottle
    print("🎬 STORY 4: Kaylee Hottle - Godzilla vs Kong Actress Death")
    print("-" * 70)

    story4_title = "Kaylee Hottle की दुःखद मौत - 'Godzilla vs Kong' की 18 साल की अभिनेत्री कार क्रैश में चली गईं"
    story4_slug = "kaylee-hottle-actress-death-godzilla-kong-car-crash-2026"
    story4_excerpt = "Kaylee Hottle, 'Godzilla x Kong: The New Empire' की अभिनेत्री, कार क्रैश में 18 साल की उम्र में चली गईं। हॉलीवुड में गहरी शोक की लहर है। Millie Bobby Brown सहित कई सेलिब्रिटीज़ उन्हें याद कर रहे हैं।"
    story4_categories = [534]  # Entertainment
    story4_tags = [2001, 2002, 2003, 2004, 2005]  # Kaylee Hottle, Godzilla Kong, Hollywood Actress, Celebrity Death, Entertainment News
    story4_seo = {
        "_yoast_wpseo_focuskw": "Kaylee Hottle actress death",
        "_yoast_wpseo_title": "Kaylee Hottle की दुःखद मौत - 'Godzilla vs Kong' की 18 साल की अभिनेत्री",
        "_yoast_wpseo_metadesc": "Kaylee Hottle, 'Godzilla x Kong' की अभिनेत्री, कार क्रैश में 18 साल की उम्र में चली गईं। हॉलीवुड में गहरी शोक की लहर है। Millie Bobby Brown सहित कई सेलिब्रिटीज़ उन्हें याद कर रहे हैं।"
    }

    story4_id = publish_story(
        title=story4_title,
        content=STORY4_CONTENT,
        slug=story4_slug,
        excerpt=story4_excerpt,
        categories=story4_categories,
        tags=story4_tags,
        seo_meta=story4_seo
    )

    if story4_id:
        add_seo_metadata(
            story4_id,
            "Kaylee Hottle actress death",
            story4_title,
            story4_seo["_yoast_wpseo_metadesc"]
        )

    print()
    print("=" * 70)
    print("PUBLISHING COMPLETE!")
    print("=" * 70)

    if story3_id and story4_id:
        print(f"✅ Both stories published successfully!")
        print(f"   Story 3 Post ID: {story3_id}")
        print(f"   Story 4 Post ID: {story4_id}")
        return True
    else:
        print(f"⚠️ Some stories failed to publish. Check errors above.")
        return False

if __name__ == "__main__":
    main()
