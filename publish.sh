#!/bin/bash

################################################################################
# GigaNectar Article Publishing Script
# Securely publishes 4 tech news articles via REST API
#
# USAGE: ./publish.sh
#
# REQUIREMENTS:
# - curl installed
# - Valid GigaNectar API credentials
# - PUBLISH-VIA-API.json in same directory
################################################################################

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
API_ENDPOINT="${GIGANECTAR_API_ENDPOINT:-https://giganectar.com/wp-json/wp/v2/posts}"
API_USERNAME="${GIGANECTAR_API_USERNAME:-}"
API_PASSWORD="${GIGANECTAR_API_PASSWORD:-}"
JSON_FILE="PUBLISH-VIA-API.json"

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}GigaNectar Article Publisher${NC}"
echo -e "${BLUE}================================${NC}\n"

# Step 1: Validate configuration
echo -e "${YELLOW}[1] Validating configuration...${NC}"

if [ ! -f "$JSON_FILE" ]; then
    echo -e "${RED}❌ Error: $JSON_FILE not found${NC}"
    exit 1
fi

if [ -z "$API_ENDPOINT" ]; then
    echo -e "${RED}❌ Error: API_ENDPOINT not set${NC}"
    echo -e "Set with: export GIGANECTAR_API_ENDPOINT='your_api_endpoint'"
    exit 1
fi

if [ -z "$API_USERNAME" ] || [ -z "$API_PASSWORD" ]; then
    echo -e "${RED}❌ Error: API credentials not set${NC}"
    echo -e "Set with:"
    echo -e "  export GIGANECTAR_API_USERNAME='your_username'"
    echo -e "  export GIGANECTAR_API_PASSWORD='your_password'"
    exit 1
fi

echo -e "${GREEN}✓ Configuration valid${NC}\n"

# Step 2: Parse JSON and publish each article
echo -e "${YELLOW}[2] Parsing articles from JSON...${NC}"

# Count articles in JSON
ARTICLE_COUNT=$(jq 'length' "$JSON_FILE" 2>/dev/null || echo "0")

if [ "$ARTICLE_COUNT" -eq 0 ]; then
    echo -e "${RED}❌ Error: No articles found in $JSON_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Found $ARTICLE_COUNT articles to publish${NC}\n"

# Step 3: Publish each article
echo -e "${YELLOW}[3] Publishing articles...${NC}\n"

PUBLISHED_COUNT=0
FAILED_COUNT=0

for i in $(seq 0 $((ARTICLE_COUNT - 1))); do
    # Extract article data
    TITLE=$(jq -r ".[$i].title" "$JSON_FILE")
    SLUG=$(jq -r ".[$i].slug" "$JSON_FILE")
    CONTENT=$(jq -r ".[$i].content" "$JSON_FILE")
    EXCERPT=$(jq -r ".[$i].excerpt" "$JSON_FILE")
    STATUS=$(jq -r ".[$i].status" "$JSON_FILE")

    # Extract categories and tags
    CATEGORIES=$(jq -r ".[$i].categories | @json" "$JSON_FILE")
    TAGS=$(jq -r ".[$i].tags | @json" "$JSON_FILE")

    # Extract SEO metadata
    SEO_TITLE=$(jq -r ".[$i].seo.title_tag" "$JSON_FILE")
    SEO_DESC=$(jq -r ".[$i].seo.meta_description" "$JSON_FILE")
    FOCUS_KEYWORD=$(jq -r ".[$i].seo.focus_keyword" "$JSON_FILE")

    echo -e "${BLUE}Article $((i+1))/$ARTICLE_COUNT: $TITLE${NC}"
    echo -e "  Slug: $SLUG"

    # Create API payload
    PAYLOAD=$(cat <<EOF
{
  "title": "$TITLE",
  "content": $(echo "$CONTENT" | jq -Rs .),
  "excerpt": "$EXCERPT",
  "slug": "$SLUG",
  "status": "$STATUS",
  "categories": $CATEGORIES,
  "tags": $TAGS,
  "meta": {
    "seo_title": "$SEO_TITLE",
    "seo_description": "$SEO_DESC",
    "focus_keyword": "$FOCUS_KEYWORD"
  }
}
EOF
)

    # Publish to API
    RESPONSE=$(curl -s -w "\n%{http_code}" \
        -X POST "$API_ENDPOINT" \
        -H "Content-Type: application/json" \
        -u "$API_USERNAME:$API_PASSWORD" \
        -d "$PAYLOAD" 2>/dev/null)

    HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
    RESPONSE_BODY=$(echo "$RESPONSE" | sed '$d')

    # Check response
    if [[ "$HTTP_CODE" =~ ^(200|201)$ ]]; then
        POST_ID=$(echo "$RESPONSE_BODY" | jq -r '.id // "Unknown"' 2>/dev/null || echo "Unknown")
        echo -e "  ${GREEN}✓ Published (ID: $POST_ID, HTTP $HTTP_CODE)${NC}\n"
        ((PUBLISHED_COUNT++))
    else
        echo -e "  ${RED}✗ Failed (HTTP $HTTP_CODE)${NC}"
        echo -e "  ${RED}Response: $(echo "$RESPONSE_BODY" | jq -r '.message // .' 2>/dev/null || echo "$RESPONSE_BODY")${NC}\n"
        ((FAILED_COUNT++))
    fi
done

# Summary
echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}Publishing Summary${NC}"
echo -e "${BLUE}================================${NC}"
echo -e "Total Articles: $ARTICLE_COUNT"
echo -e "${GREEN}Published: $PUBLISHED_COUNT${NC}"
if [ "$FAILED_COUNT" -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED_COUNT${NC}"
else
    echo -e "${GREEN}Failed: 0${NC}"
fi

if [ "$FAILED_COUNT" -eq 0 ]; then
    echo -e "\n${GREEN}✓ All articles published successfully!${NC}\n"
    exit 0
else
    echo -e "\n${RED}✗ Some articles failed to publish${NC}"
    echo -e "Review the errors above and retry\n"
    exit 1
fi
