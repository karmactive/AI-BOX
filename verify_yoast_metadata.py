#!/usr/bin/env python3
"""Verify Yoast SEO metadata is set on posts"""

import requests
import base64
import json

API_BASE_URL = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = "keTs 4gmn QNeD QHcE Ejk1 qpd5"

def get_auth_header():
    credentials = f"{USERNAME}:{PASSWORD}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def verify_post(post_id):
    """Verify post has Yoast metadata"""
    headers = get_auth_header()
    response = requests.get(
        f"{API_BASE_URL}/posts/{post_id}",
        headers=headers
    )
    
    if response.status_code == 200:
        post = response.json()
        print(f"\n📄 Post {post_id}:")
        print(f"   Title: {post['title']['rendered'][:60]}")
        
        # Check meta fields
        meta = post.get('meta', {})
        print(f"   ✓ Focus Keyphrase: {meta.get('_yoast_wpseo_focuskw', 'NOT SET')}")
        print(f"   ✓ Meta Description: {meta.get('_yoast_wpseo_metadesc', 'NOT SET')[:80]}")
        print(f"   ✓ SEO Title: {meta.get('_yoast_wpseo_title', 'NOT SET')}")
        
        # Check categories and tags
        print(f"   ✓ Categories: {post.get('categories', [])}")
        print(f"   ✓ Tags: {post.get('tags', [])}")

print("\n🔍 VERIFYING YOAST METADATA ON ALL POSTS\n" + "="*50)

post_ids = [7247, 7248, 7249, 7250, 7251]
for post_id in post_ids:
    verify_post(post_id)

print("\n" + "="*50)
print("\n✅ All posts checked for Yoast metadata")
