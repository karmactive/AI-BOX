#!/usr/bin/env python3
"""
GigaNectar Article Publishing Script
Securely publishes 4 tech news articles via REST API

USAGE: python3 publish.py [--endpoint URL] [--username USER] [--password PASS]

ENVIRONMENT VARIABLES:
- GIGANECTAR_API_ENDPOINT: API endpoint URL
- GIGANECTAR_API_USERNAME: API username
- GIGANECTAR_API_PASSWORD: API password
"""

import json
import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, List, Tuple
import argparse

# ANSI color codes
class Colors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def load_config() -> Tuple[str, str, str]:
    """Load and validate API configuration from environment or arguments."""
    parser = argparse.ArgumentParser(description='Publish articles to GigaNectar')
    parser.add_argument('--endpoint', help='API endpoint URL')
    parser.add_argument('--username', help='API username')
    parser.add_argument('--password', help='API password')
    args = parser.parse_args()

    endpoint = args.endpoint or os.getenv('GIGANECTAR_API_ENDPOINT', '')
    username = args.username or os.getenv('GIGANECTAR_API_USERNAME', '')
    password = args.password or os.getenv('GIGANECTAR_API_PASSWORD', '')

    if not endpoint:
        print(f"{Colors.FAIL}❌ Error: API endpoint not configured{Colors.ENDC}")
        print("Set with: export GIGANECTAR_API_ENDPOINT='your_api_endpoint'")
        sys.exit(1)

    if not username or not password:
        print(f"{Colors.FAIL}❌ Error: API credentials not configured{Colors.ENDC}")
        print("Set with:")
        print("  export GIGANECTAR_API_USERNAME='your_username'")
        print("  export GIGANECTAR_API_PASSWORD='your_password'")
        sys.exit(1)

    return endpoint, username, password


def load_articles(filename: str = 'PUBLISH-VIA-API.json') -> List[Dict]:
    """Load articles from JSON file."""
    if not os.path.exists(filename):
        print(f"{Colors.FAIL}❌ Error: {filename} not found{Colors.ENDC}")
        sys.exit(1)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            articles = json.load(f)
        return articles
    except json.JSONDecodeError as e:
        print(f"{Colors.FAIL}❌ Error parsing JSON: {e}{Colors.ENDC}")
        sys.exit(1)


def publish_article(endpoint: str, article: Dict, auth: HTTPBasicAuth) -> Tuple[bool, str]:
    """Publish a single article to the API."""
    try:
        # Prepare payload
        payload = {
            'title': article.get('title'),
            'content': article.get('content'),
            'excerpt': article.get('excerpt'),
            'slug': article.get('slug'),
            'status': article.get('status', 'publish'),
            'categories': article.get('categories', []),
            'tags': article.get('tags', []),
            'meta': {
                'seo_title': article.get('seo', {}).get('title_tag'),
                'seo_description': article.get('seo', {}).get('meta_description'),
                'focus_keyword': article.get('seo', {}).get('focus_keyword')
            }
        }

        # Send request
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            endpoint,
            json=payload,
            auth=auth,
            headers=headers,
            timeout=30
        )

        # Check response
        if response.status_code in (200, 201):
            post_id = response.json().get('id', 'Unknown')
            return True, f"Published (ID: {post_id}, HTTP {response.status_code})"
        else:
            error_msg = response.json().get('message', response.text)
            return False, f"Failed (HTTP {response.status_code}): {error_msg}"

    except requests.exceptions.Timeout:
        return False, "Request timed out"
    except requests.exceptions.ConnectionError:
        return False, "Connection error - check endpoint URL"
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Main publishing function."""
    print(f"\n{Colors.HEADER}{'='*40}{Colors.ENDC}")
    print(f"{Colors.HEADER}GigaNectar Article Publisher{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*40}{Colors.ENDC}\n")

    # Step 1: Load configuration
    print(f"{Colors.WARNING}[1] Validating configuration...{Colors.ENDC}")
    endpoint, username, password = load_config()
    print(f"{Colors.OKGREEN}✓ Configuration valid{Colors.ENDC}\n")

    # Step 2: Load articles
    print(f"{Colors.WARNING}[2] Loading articles...{Colors.ENDC}")
    articles = load_articles()
    print(f"{Colors.OKGREEN}✓ Loaded {len(articles)} articles{Colors.ENDC}\n")

    # Step 3: Publish articles
    print(f"{Colors.WARNING}[3] Publishing articles...{Colors.ENDC}\n")

    auth = HTTPBasicAuth(username, password)
    published_count = 0
    failed_count = 0

    for idx, article in enumerate(articles, 1):
        title = article.get('title', 'Unknown')
        slug = article.get('slug', 'unknown')

        print(f"{Colors.HEADER}Article {idx}/{len(articles)}: {title}{Colors.ENDC}")
        print(f"  Slug: {slug}")

        success, message = publish_article(endpoint, article, auth)

        if success:
            print(f"  {Colors.OKGREEN}✓ {message}{Colors.ENDC}\n")
            published_count += 1
        else:
            print(f"  {Colors.FAIL}✗ {message}{Colors.ENDC}\n")
            failed_count += 1

    # Summary
    print(f"{Colors.HEADER}{'='*40}{Colors.ENDC}")
    print(f"{Colors.HEADER}Publishing Summary{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*40}{Colors.ENDC}")
    print(f"Total Articles: {len(articles)}")
    print(f"{Colors.OKGREEN}Published: {published_count}{Colors.ENDC}")
    print(f"{Colors.FAIL}Failed: {failed_count}{Colors.ENDC}" if failed_count > 0 else f"Failed: 0")

    if failed_count == 0:
        print(f"\n{Colors.OKGREEN}✓ All articles published successfully!{Colors.ENDC}\n")
        return 0
    else:
        print(f"\n{Colors.FAIL}✗ Some articles failed to publish{Colors.ENDC}")
        print("Review the errors above and retry\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
