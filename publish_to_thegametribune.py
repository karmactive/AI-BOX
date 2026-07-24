#!/usr/bin/env python3
"""
The Game Tribune REST API Publisher
Publishes all 5 gaming news articles to thegametribune.com
"""

import requests
import base64
import json
import sys
from datetime import datetime
from html.parser import HTMLParser

# Configuration
API_BASE_URL = "https://thegametribune.com/wp-json/wp/v2"
USERNAME = "thegametribune.com"
PASSWORD = "keTs 4gmn QNeD QHcE Ejk1 qpd5"

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class HTMLContentExtractor(HTMLParser):
    """Extract article content from HTML"""
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.content = []
        self.capture = False

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.in_article = True
            self.capture = True
        elif self.in_article and tag in ["p", "h1", "h2", "h3", "a", "strong", "em"]:
            self.capture = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False
            self.capture = False

    def handle_data(self, data):
        if self.capture and self.in_article:
            self.content.append(data)

def get_auth_header():
    """Generate Basic Auth header"""
    credentials = f"{USERNAME}:{PASSWORD}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def extract_article_content(html_file):
    """Extract article content from HTML file"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract content between <article> tags
        start = content.find('<article>')
        end = content.find('</article>')
        if start != -1 and end != -1:
            article_html = content[start+9:end]
            return article_html
        return None
    except Exception as e:
        print(f"{RED}Error reading file {html_file}: {e}{RESET}")
        return None

def get_category_id(category_name):
    """Get category ID from name"""
    try:
        headers = get_auth_header()
        response = requests.get(
            f"{API_BASE_URL}/categories",
            params={"search": category_name},
            headers=headers
        )
        if response.status_code == 200:
            categories = response.json()
            if categories:
                return categories[0]['id']
    except Exception as e:
        print(f"{YELLOW}Warning: Could not fetch category ID: {e}{RESET}")
    return None

def get_or_create_tags(tag_names):
    """Get or create tags and return their IDs"""
    tag_ids = []
    try:
        headers = get_auth_header()
        for tag_name in tag_names:
            # Try to get existing tag
            response = requests.get(
                f"{API_BASE_URL}/tags",
                params={"search": tag_name},
                headers=headers
            )
            if response.status_code == 200:
                tags = response.json()
                if tags:
                    tag_ids.append(tags[0]['id'])
                else:
                    # Create new tag
                    response = requests.post(
                        f"{API_BASE_URL}/tags",
                        json={"name": tag_name},
                        headers=headers
                    )
                    if response.status_code == 201:
                        tag_ids.append(response.json()['id'])
    except Exception as e:
        print(f"{YELLOW}Warning: Could not process tags: {e}{RESET}")
    return tag_ids

def publish_article(article_data):
    """Publish article via REST API"""
    try:
        headers = get_auth_header()
        headers["Content-Type"] = "application/json"

        # Prepare post data
        post_data = {
            "title": article_data["title"],
            "content": article_data["content"],
            "excerpt": article_data["excerpt"],
            "slug": article_data["slug"],
            "status": "publish",
            "categories": [article_data["category_id"]] if article_data["category_id"] else [],
            "tags": article_data.get("tag_ids", [])
        }

        print(f"\n{BLUE}Publishing: {article_data['title']}{RESET}")
        print(f"Slug: {article_data['slug']}")

        response = requests.post(
            f"{API_BASE_URL}/posts",
            json=post_data,
            headers=headers
        )

        if response.status_code == 201:
            post_id = response.json()['id']
            post_url = response.json()['link']
            print(f"{GREEN}✓ Published successfully!{RESET}")
            print(f"Post ID: {post_id}")
            print(f"URL: {post_url}")
            return True
        else:
            print(f"{RED}✗ Publication failed!{RESET}")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"{RED}Error publishing article: {e}{RESET}")
        return False

def main():
    """Main publishing function"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}The Game Tribune REST API Publisher{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

    # Article data
    articles = [
        {
            "file": "STORY_1_HALO_COMPLETE.html",
            "title": "Halo Campaign Evolved Launches with Unreal Engine 5 Graphics, Seamless Zones, and Four-Player Online Co-Op",
            "slug": "halo-campaign-evolved-unreal-engine-5-features-2026",
            "category": "Gaming News",
            "tags": ["Gaming News", "Halo Campaign Evolved", "Unreal Engine 5", "First Person Shooter"],
            "excerpt": "Halo Campaign Evolved launches with complete Unreal Engine 5 rebuild featuring Nanite/Lumen graphics, seamless zone transitions, four-player online co-op, three new missions, difficulty modifiers, and collectible Skulls."
        },
        {
            "file": "STORY_2_MARVEL_COMPLETE.html",
            "title": "Marvel Tokon Fighting Souls Debuts August 6 with 4v4 Tag Team Mechanics and 20-Character Launch Roster",
            "slug": "marvel-tokon-fighting-souls-4v4-tag-team-august-2026",
            "category": "Gaming News",
            "tags": ["Fighting Games", "Marvel Games", "Arc System Works", "Fighting Game News"],
            "excerpt": "Marvel Tokon: Fighting Souls launches August 6, 2026 on PS5/PC with 4v4 tag team mechanics, 20-character roster, Vital Gauge system, Wall Breaks gameplay, and Phoenix Cyclops as first Year 1 DLC character."
        },
        {
            "file": "STORY_3_PALWORLD_COMPLETE.html",
            "title": "Palworld Fortnite Crossover Speculation Escalates After Epic Games Survey and 40 Million Player Achievement",
            "slug": "palworld-fortnite-crossover-epic-games-survey-2026",
            "category": "Gaming News",
            "tags": ["Battle Royale Games", "Palworld", "Fortnite", "Gaming Crossovers"],
            "excerpt": "Palworld Fortnite crossover speculation grows following Epic Games survey and developer comments. Palworld reached 40M players with 722K Steam concurrent peak, positioning it as Pokemon crossover alternative."
        },
        {
            "file": "STORY_4_ARDIIS_COMPLETE.html",
            "title": "Riot Games Suspends Valorant Pro Ardiis from VCT Co-Streaming Over Discriminatory Comments During Game Changers",
            "slug": "ardiis-valorant-vct-suspension-riot-games-conduct",
            "category": "Esports News",
            "tags": ["Esports News", "Valorant", "VCT Esports", "Esports Controversy"],
            "excerpt": "Riot Games suspended Valorant pro Ardiis from VCT co-streaming through August 19 after discriminatory comments during Game Changers broadcast. NAVI also suspended collaboration with the $140K earning professional."
        },
        {
            "file": "STORY_5_EAFC27_COMPLETE.html",
            "title": "EA Sports FC 27 Launches September 25 with Kylian Mbappé and Jude Bellingham as Cover Stars",
            "slug": "ea-sports-fc-27-mbappe-bellingham-september-2026-release",
            "category": "Gaming News",
            "tags": ["Sports Games", "EA Sports FC", "Football Games", "Gaming Releases"],
            "excerpt": "EA Sports FC 27 launches September 25, 2026 across PC, PlayStation, Xbox, and Nintendo Switch. Kylian Mbappé returns as cover star (fourth appearance) alongside Jude Bellingham in Ultimate Plus Edition."
        }
    ]

    print(f"\n{YELLOW}Total articles to publish: {len(articles)}{RESET}")
    print(f"Target: {API_BASE_URL}\n")

    # Test connection
    print(f"{BLUE}Testing API connection...{RESET}")
    try:
        headers = get_auth_header()
        response = requests.get(f"{API_BASE_URL}/posts", headers=headers, params={"per_page": 1})
        if response.status_code == 200:
            print(f"{GREEN}✓ API connection successful!{RESET}")
        else:
            print(f"{RED}✗ API connection failed (status {response.status_code}){RESET}")
            return False
    except Exception as e:
        print(f"{RED}✗ Connection error: {e}{RESET}")
        return False

    # Publish each article
    published_count = 0
    failed_count = 0

    for i, article in enumerate(articles, 1):
        print(f"\n{BLUE}[{i}/{len(articles)}] Processing: {article['title'][:60]}...{RESET}")

        # Extract content from HTML file
        content = extract_article_content(article["file"])
        if not content:
            print(f"{RED}✗ Failed to extract content from {article['file']}{RESET}")
            failed_count += 1
            continue

        # Get category ID
        category_id = get_category_id(article["category"])
        if not category_id:
            print(f"{YELLOW}Warning: Category '{article['category']}' not found, will proceed without category{RESET}")

        # Get or create tags
        tag_ids = get_or_create_tags(article["tags"])

        # Prepare article data
        article_data = {
            "title": article["title"],
            "content": content,
            "excerpt": article["excerpt"],
            "slug": article["slug"],
            "category_id": category_id,
            "tag_ids": tag_ids
        }

        # Publish
        if publish_article(article_data):
            published_count += 1
        else:
            failed_count += 1

        # Small delay between publications
        import time
        time.sleep(1)

    # Summary
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Publication Summary{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{GREEN}✓ Published: {published_count}/{len(articles)}{RESET}")
    if failed_count > 0:
        print(f"{RED}✗ Failed: {failed_count}/{len(articles)}{RESET}")
    print(f"\nPublished on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Target: thegametribune.com\n")

    if published_count == len(articles):
        print(f"{GREEN}✓ ALL ARTICLES PUBLISHED SUCCESSFULLY!{RESET}\n")
        print("Next steps:")
        print("1. Visit https://thegametribune.com to verify articles are live")
        print("2. Check each article for correct formatting and links")
        print("3. Share articles on social media")
        print("4. Monitor analytics for traffic and engagement")
        return True
    else:
        print(f"{RED}✗ Some articles failed to publish. Please review errors above.{RESET}\n")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
