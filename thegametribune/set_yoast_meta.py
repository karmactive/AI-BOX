#!/usr/bin/env python3
"""
Set Yoast SEO meta fields for Game Tribune articles via REST API.
Uses nested meta payload with both underscore and non-underscore variants.
"""
import requests
import json
import base64
import os
import time

WP_API = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

token = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

YOAST_DATA = {
    7222: {
        "_yoast_wpseo_focuskw": "Halo Campaign Evolved PS5",
        "_yoast_wpseo_metadesc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years. Unreal Engine 5 rebuild brings 4-player co-op, new missions, and Game Pass day-one access.",
        "_yoast_wpseo_title": "Halo Campaign Evolved PS5 Early Access Is Live",
    },
    7223: {
        "_yoast_wpseo_focuskw": "Nintendo Palworld patent rejected",
        "_yoast_wpseo_metadesc": "Japan Patent Office rejects Nintendo's divisional monster-catching patent again, citing ARK and a Pokemon fan game as prior art. Here's what it means for the Palworld lawsuit.",
        "_yoast_wpseo_title": "Nintendo Palworld Patent Rejected Again by JPO",
    },
    7224: {
        "_yoast_wpseo_focuskw": "Wonder Man 5 Marvel Duggan",
        "_yoast_wpseo_metadesc": "Wonder Man #5 released July 22, 2026, ending Gerry Duggan's 5-issue Marvel series. Simon Williams confronts betrayal and an unresolved moral weight — with no tidy ending.",
        "_yoast_wpseo_title": "Wonder Man #5: Gerry Duggan's Marvel Run Ends",
    },
    7225: {
        "_yoast_wpseo_focuskw": "Star Wars Jedi manga volume 3",
        "_yoast_wpseo_metadesc": "Panini Comics confirms Star Wars Jedi: Fallen Order Manga Vol. 3 for December 1, 2026. Cal Kestis faces a destroyed lightsaber and painful memories in 200 pages of adapted story.",
        "_yoast_wpseo_title": "Star Wars Jedi Manga Vol. 3 — December 2026",
    },
}

print("=== Setting Yoast SEO meta for all 4 posts ===\n")

for post_id, yoast_meta in YOAST_DATA.items():
    # Build meta with both underscore and non-underscore variants
    # (some Yoast versions respond to both)
    meta_payload = {
        **yoast_meta,
        "yoast_wpseo_focuskw": yoast_meta["_yoast_wpseo_focuskw"],
        "yoast_wpseo_metadesc": yoast_meta["_yoast_wpseo_metadesc"],
        "yoast_wpseo_title": yoast_meta["_yoast_wpseo_title"],
    }

    payload = {"meta": meta_payload}

    r = requests.patch(
        f"{WP_API}/posts/{post_id}",
        headers=headers,
        data=json.dumps(payload),
        timeout=30,
        verify=True
    )

    print(f"Post {post_id}: {r.status_code}")
    if r.status_code == 200:
        meta = r.json().get("meta", {})
        print(f"  Focus KW: {meta.get('_yoast_wpseo_focuskw', 'NOT SET')}")
        print(f"  Meta Desc: {meta.get('_yoast_wpseo_metadesc', 'NOT SET')[:70]}...")
        print(f"  SEO Title: {meta.get('_yoast_wpseo_title', 'NOT SET')}")
    else:
        print(f"  Error: {r.text[:200]}")

    time.sleep(0.5)

print("\nDone.")
