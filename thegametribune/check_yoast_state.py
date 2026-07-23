#!/usr/bin/env python3
import os
"""
Check current Yoast state and try remaining approaches to set meta.
"""
import requests
import json
import base64
import time

WP_URL = "https://thegametribune.com"
WP_API = f"{WP_URL}/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

credentials = f"{USERNAME}:{PASSWORD}"
token = base64.b64encode(credentials.encode()).decode("utf-8")
headers = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/json"
}

POST_IDS = [7222, 7223, 7224, 7225]

print("=== Check Yoast head JSON for each post ===")
for pid in POST_IDS:
    r = requests.get(
        f"{WP_API}/posts/{pid}?_fields=id,title,yoast_head_json,meta",
        headers=headers,
        timeout=30,
        verify=True
    )
    if r.status_code == 200:
        data = r.json()
        yoast = data.get("yoast_head_json", {})
        print(f"\nPost {pid}:")
        print(f"  Title tag: {yoast.get('title', 'NOT SET')}")
        print(f"  Meta desc: {str(yoast.get('description', 'NOT SET'))[:100]}")
        og_title = next((x.get('content') for x in yoast.get('og_title', []) if isinstance(x, dict)), yoast.get('og_title', 'NOT SET'))
        print(f"  OG title: {og_title}")
        schema = yoast.get('schema', {})
        print(f"  Schema @type: {schema.get('@type', 'N/A') if isinstance(schema, dict) else 'N/A'}")
    time.sleep(0.3)

print("\n=== Try Yoast /yoast/v1/available_posts endpoint ===")
r = requests.get(
    f"{WP_URL}/wp-json/yoast/v1/available_posts",
    headers=headers,
    timeout=15,
    verify=True
)
print(f"Status: {r.status_code}")
print(f"Response: {r.text[:300]}")

print("\n=== Try Yoast indexing POST to index post 7222 ===")
r = requests.post(
    f"{WP_URL}/wp-json/yoast/v1/indexing/posts",
    headers=headers,
    json={"limit": 1},
    timeout=20,
    verify=True
)
print(f"Status: {r.status_code}")
print(f"Response: {r.text[:300]}")

print("\n=== Try top-level wpseo fields in post PATCH ===")
# Some Yoast versions expose top-level fields directly (not under meta)
test_payload = {
    "wpseo_focuskw": "Halo Campaign Evolved PS5",
    "wpseo_metadesc": "Halo: Campaign Evolved early access launches July 23 on PS5.",
    "wpseo_title": "Halo Campaign Evolved PS5 Early Access Is Live",
}
r = requests.post(
    f"{WP_API}/posts/7222",
    headers=headers,
    data=json.dumps(test_payload),
    timeout=30,
    verify=True
)
print(f"Top-level wpseo PATCH: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    # Check if any wpseo field appears in response
    wpseo_keys = [k for k in data.keys() if 'wpseo' in k.lower() or 'yoast' in k.lower() or 'seo' in k.lower()]
    print(f"Yoast-related keys in response: {wpseo_keys}")
    yoast_head = data.get("yoast_head_json", {})
    if yoast_head:
        print(f"Yoast head title: {yoast_head.get('title', 'N/A')}")

print("\n=== Check post schema — what fields does it expose? ===")
r_opts = requests.options(f"{WP_API}/posts/7222", headers=headers, timeout=15, verify=True)
if r_opts.status_code == 200:
    schema = r_opts.json()
    props = schema.get("schema", {}).get("properties", {})
    yoast_props = {k: v for k, v in props.items() if "yoast" in k.lower() or "wpseo" in k.lower() or "seo" in k.lower()}
    print(f"Yoast/SEO properties in post schema: {list(yoast_props.keys())}")
    print(f"All response properties: {list(props.keys())[:30]}")

print("\n=== Check if Yoast has indexable REST endpoint ===")
for suffix in ["/yoast/v1/indexables", "/yoast/v1/indexables/1", "/yoast/v1/post_seo_data"]:
    r = requests.get(f"{WP_URL}/wp-json{suffix}", headers=headers, timeout=10, verify=True)
    print(f"  {suffix}: {r.status_code} - {r.text[:100]}")
    time.sleep(0.2)

print("\n=== Try REST API with application/x-www-form-urlencoded ===")
import urllib.parse
form_headers = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}
form_data = urllib.parse.urlencode({
    "meta[_yoast_wpseo_focuskw]": "Halo Campaign Evolved PS5",
    "meta[_yoast_wpseo_metadesc]": "Test meta desc",
})
r = requests.post(
    f"{WP_API}/posts/7222",
    headers=form_headers,
    data=form_data,
    timeout=30,
    verify=True
)
print(f"Form-encoded meta: {r.status_code}")
if r.status_code == 200:
    print(f"Meta: {r.json().get('meta', {})}")

print("\n=== Inspect full post response fields (7222) ===")
r = requests.get(
    f"{WP_API}/posts/7222?context=edit",
    headers=headers,
    timeout=30,
    verify=True
)
if r.status_code == 200:
    data = r.json()
    all_keys = list(data.keys())
    print(f"All response keys: {all_keys}")
    yoast_head = data.get("yoast_head_json", {})
    if isinstance(yoast_head, dict):
        print(f"\nYoast head JSON keys: {list(yoast_head.keys())}")
        print(f"Title: {yoast_head.get('title', 'N/A')}")
        desc = yoast_head.get('description', 'N/A')
        print(f"Description: {desc}")
