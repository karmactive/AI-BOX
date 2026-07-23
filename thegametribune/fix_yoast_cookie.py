#!/usr/bin/env python3
import os
"""
Use WordPress cookie auth + nonce to set Yoast meta.
This mirrors what the Gutenberg editor does when saving a post.
"""
import requests
import json
import base64
import re
import time

WP_URL = "https://thegametribune.com"
WP_API = f"{WP_URL}/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

session = requests.Session()

print("=== Step 1: Login to get session cookie ===")
login_data = {
    "log": USERNAME,
    "pwd": PASSWORD,
    "wp-submit": "Log In",
    "redirect_to": f"{WP_URL}/wp-admin/",
    "testcookie": "1"
}
# First, get the login page to set the testcookie
r0 = session.get(f"{WP_URL}/wp-login.php", timeout=30, verify=True)
print(f"Login page: {r0.status_code}")

# Set the test cookie
session.cookies.set("wordpress_test_cookie", "WP%20Cookie%20check", domain="thegametribune.com")

# Now login
r1 = session.post(
    f"{WP_URL}/wp-login.php",
    data=login_data,
    timeout=30,
    verify=True,
    allow_redirects=True
)
print(f"Login POST: {r1.status_code}, URL: {r1.url}")
print(f"Cookies after login: {[c.name for c in session.cookies]}")

# Check if we're logged in
is_logged_in = "wordpress_logged_in" in [c.name for c in session.cookies] or "wp-admin" in r1.url
print(f"Logged in: {is_logged_in}")

if not is_logged_in:
    print("Login failed! Checking response...")
    print(r1.text[:1000])
    exit(1)

print("\n=== Step 2: Get REST API nonce ===")
r2 = session.get(f"{WP_URL}/wp-admin/admin-ajax.php?action=rest-nonce", timeout=20, verify=True)
print(f"Nonce via ajax: {r2.status_code} - {r2.text[:100]}")

# Alternative: get nonce from admin page
r3 = session.get(f"{WP_URL}/wp-admin/post.php?post=7222&action=edit", timeout=30, verify=True)
print(f"Edit page: {r3.status_code}")

# Extract nonce from page
nonce_match = re.search(r'"nonce":"([a-f0-9]+)"', r3.text)
if not nonce_match:
    nonce_match = re.search(r'wpApiSettings.*?"nonce":"([a-f0-9]+)"', r3.text, re.DOTALL)
if not nonce_match:
    nonce_match = re.search(r'rest_nonce.*?["\']([a-f0-9]{10})["\']', r3.text)
if not nonce_match:
    # Try to find any nonce
    nonce_matches = re.findall(r'"nonce":"([a-f0-9]+)"', r3.text)
    print(f"All nonces found: {nonce_matches[:5]}")
    nonce = nonce_matches[0] if nonce_matches else None
else:
    nonce = nonce_match.group(1)

print(f"Nonce: {nonce}")

if not nonce:
    # Try getting nonce via wp_rest action
    r_nonce = session.post(
        f"{WP_URL}/wp-admin/admin-ajax.php",
        data={"action": "wc_get_nonce", "nonce_action": "wp_rest"},
        timeout=20, verify=True
    )
    print(f"Ajax nonce: {r_nonce.text[:200]}")

    # Try the standard endpoint
    r_nonce2 = session.get(
        f"{WP_URL}/wp-json/",
        timeout=20, verify=True
    )
    if r_nonce2.status_code == 200:
        # Extract nonce from response headers
        print(f"REST API headers: {dict(r_nonce2.headers)}")

print("\n=== Step 3: Try REST API with cookie auth + nonce ===")
if nonce:
    headers_cookie = {
        "X-WP-Nonce": nonce,
        "Content-Type": "application/json"
    }

    test_payload = {
        "meta": {
            "_yoast_wpseo_focuskw": "Halo Campaign Evolved PS5",
            "_yoast_wpseo_metadesc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years.",
            "_yoast_wpseo_title": "Halo Campaign Evolved PS5 Early Access Is Live",
        }
    }

    r4 = session.post(
        f"{WP_API}/posts/7222",
        headers=headers_cookie,
        data=json.dumps(test_payload),
        timeout=30, verify=True
    )
    print(f"Cookie+nonce PATCH: {r4.status_code}")
    if r4.status_code == 200:
        data = r4.json()
        print(f"Meta: {data.get('meta', {})}")
        print(f"Yoast head JSON: {str(data.get('yoast_head_json', {}))[:500]}")
    else:
        print(f"Error: {r4.text[:300]}")

print("\n=== Step 4: Try Yoast AJAX save ===")
# Yoast saves via its own AJAX action when used with classic editor
# action: wpseo_save_post
# But first we need a nonce specific to wpseo

# Look for wpseo nonce in the edit page
if r3.status_code == 200:
    wpseo_nonce_match = re.search(r'wpseo[_\s]nonce["\s:]*["\']([a-f0-9]+)["\']', r3.text, re.IGNORECASE)
    if not wpseo_nonce_match:
        wpseo_nonce_match = re.search(r'"nonce"\s*:\s*"([a-f0-9]+)"', r3.text)

    wpseo_nonce = wpseo_nonce_match.group(1) if wpseo_nonce_match else nonce
    print(f"Yoast nonce: {wpseo_nonce}")

    # Also look for the Yoast inline data
    yoast_data_match = re.search(r'yoastData\s*=\s*(\{.*?\});', r3.text, re.DOTALL)
    if yoast_data_match:
        print(f"Yoast inline data: {yoast_data_match.group(1)[:300]}")

    # Try wpseo save action
    wpseo_save_data = {
        "action": "wpseo_save",
        "post_id": "7222",
        "yoast_wpseo_focuskw": "Halo Campaign Evolved PS5",
        "yoast_wpseo_metadesc": "Halo: Campaign Evolved early access launches July 23 on PS5 for the first time in 25 years. Unreal Engine 5 rebuild brings 4-player co-op.",
        "yoast_wpseo_title": "Halo Campaign Evolved PS5 Early Access Is Live",
        "nonce": wpseo_nonce if 'wpseo_nonce' in dir() else nonce,
    }

    r5 = session.post(
        f"{WP_URL}/wp-admin/admin-ajax.php",
        data=wpseo_save_data,
        timeout=30, verify=True
    )
    print(f"Yoast AJAX save: {r5.status_code} - {r5.text[:200]}")

print("\n=== Step 5: Inspect available nonces in edit page ===")
if r3.status_code == 200:
    # Find all nonce-like patterns
    nonces = re.findall(r'"([a-zA-Z_]+nonce[a-zA-Z_]*)"\s*:\s*"([a-f0-9]+)"', r3.text, re.IGNORECASE)
    print(f"Nonces found in edit page:")
    for name, val in nonces[:20]:
        print(f"  {name}: {val}")

    # Look for Yoast-specific config
    yoast_sections = re.findall(r'(wpseo[A-Za-z]*)\s*=\s*\{[^}]{0,200}', r3.text)
    print(f"\nYoast JS variables: {yoast_sections[:10]}")
