#!/usr/bin/env python3
import os
"""
Use WordPress XML-RPC API to set Yoast SEO private meta fields.
XML-RPC can set arbitrary custom fields including underscore-prefixed private meta.
"""
import xmlrpc.client
import time

WP_XMLRPC = "https://thegametribune.com/xmlrpc.php"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

ARTICLES = [
    {
        "id": 7222,
        "focus_kw": "Halo Campaign Evolved PS5",
        "meta_desc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years. Unreal Engine 5 rebuild brings 4-player co-op, new missions, and Game Pass day-one access.",
        "yoast_title": "Halo Campaign Evolved PS5 Early Access Is Live",
    },
    {
        "id": 7223,
        "focus_kw": "Nintendo Palworld patent rejected",
        "meta_desc": "Japan Patent Office rejects Nintendo's divisional monster-catching patent again, citing ARK and a Pokemon fan game as prior art. Here's what it means for the Palworld lawsuit.",
        "yoast_title": "Nintendo Palworld Patent Rejected Again by JPO",
    },
    {
        "id": 7224,
        "focus_kw": "Wonder Man 5 Marvel Duggan",
        "meta_desc": "Wonder Man #5 released July 22, 2026, ending Gerry Duggan's 5-issue Marvel series. Simon Williams confronts betrayal and an unresolved moral weight — with no tidy ending.",
        "yoast_title": "Wonder Man #5: Gerry Duggan's Marvel Run Ends",
    },
    {
        "id": 7225,
        "focus_kw": "Star Wars Jedi manga volume 3",
        "meta_desc": "Panini Comics confirms Star Wars Jedi: Fallen Order Manga Vol. 3 for December 1, 2026. Cal Kestis faces a destroyed lightsaber and painful memories in 200 pages of adapted story.",
        "yoast_title": "Star Wars Jedi Manga Vol. 3 — December 2026",
    },
]

print("=== Connecting to WordPress XML-RPC ===")
try:
    server = xmlrpc.client.ServerProxy(WP_XMLRPC)
    # Test connection
    result = server.wp.getOptions(1, USERNAME, PASSWORD, ["software_version"])
    print(f"Connected! WP Version: {result}")
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

print("\n=== Getting existing custom fields for post 7222 ===")
try:
    post = server.wp.getPost(1, USERNAME, PASSWORD, 7222, ["custom_fields"])
    existing_fields = post.get("custom_fields", [])
    print(f"Existing custom fields count: {len(existing_fields)}")
    for field in existing_fields[:20]:
        key = field.get("key", "")
        if "yoast" in key.lower() or "wpseo" in key.lower():
            print(f"  Found Yoast field: id={field.get('id')}, key={key}, value={str(field.get('value',''))[:50]}")
except Exception as e:
    print(f"Error getting post: {e}")

print("\n=== Setting Yoast meta via XML-RPC for all articles ===")

for article in ARTICLES:
    post_id = article["id"]
    print(f"\nProcessing post {post_id}...")

    try:
        # Get current post to find existing field IDs
        post = server.wp.getPost(1, USERNAME, PASSWORD, post_id, ["custom_fields"])
        existing_fields = post.get("custom_fields", [])

        # Build ID map for existing fields
        field_id_map = {}
        for field in existing_fields:
            key = field.get("key", "")
            field_id = field.get("id", "")
            if key and field_id:
                field_id_map[key] = field_id

        print(f"  Existing Yoast fields: {[k for k in field_id_map.keys() if 'yoast' in k.lower() or 'wpseo' in k.lower()]}")

        # Prepare the custom fields to set
        target_fields = {
            "_yoast_wpseo_focuskw": article["focus_kw"],
            "_yoast_wpseo_metadesc": article["meta_desc"],
            "_yoast_wpseo_title": article["yoast_title"],
        }

        custom_fields = []
        for key, value in target_fields.items():
            field_entry = {"key": key, "value": value}
            # If field already exists, include its ID to update rather than create
            if key in field_id_map:
                field_entry["id"] = field_id_map[key]
            custom_fields.append(field_entry)

        # Edit the post with new custom fields
        post_data = {
            "custom_fields": custom_fields
        }

        result = server.wp.editPost(1, USERNAME, PASSWORD, post_id, post_data)
        print(f"  editPost result: {result}")

        # Verify the fields were set
        time.sleep(0.5)
        updated_post = server.wp.getPost(1, USERNAME, PASSWORD, post_id, ["custom_fields"])
        updated_fields = updated_post.get("custom_fields", [])
        for field in updated_fields:
            key = field.get("key", "")
            if key in target_fields:
                print(f"  ✅ {key} = {str(field.get('value',''))[:80]}")

        time.sleep(1)

    except Exception as e:
        print(f"  ❌ Error: {e}")

print("\n=== Done ===")
