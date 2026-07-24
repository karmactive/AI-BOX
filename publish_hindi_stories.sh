#!/bin/bash

# NewsPandit Hindi Stories Publication Script
# Publishes 3 Hindi articles to newspandit.com via WordPress REST API

set -e

# API Configuration
NEWSPANDIT_URL="https://newspandit.com"
API_ENDPOINT="$NEWSPANDIT_URL/wp-json/wp/v2/posts"
USERNAME="NewsPandit Staff"
PASSWORD="GSIf avuF lFp3 2ZtN aSQx iAMQ"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}NewsPandit Hindi Stories Publisher${NC}"
echo -e "${YELLOW}========================================${NC}"
echo ""

# Function to publish a story
publish_story() {
    local json_file=$1
    local story_name=$2

    echo -e "${YELLOW}Publishing: $story_name${NC}"
    echo "File: $json_file"

    # Read and prepare the JSON payload
    local payload=$(jq -c '{
        title: .title,
        content: .content,
        status: .status,
        slug: .slug,
        excerpt: .excerpt,
        meta: {
            "_yoast_wpseo_title": .yoast_seo.title,
            "_yoast_wpseo_metadesc": .yoast_seo.metaDescription,
            "_yoast_wpseo_focuskw": .yoast_seo.focusKeyphrase
        },
        categories: .categories,
        tags: .tags
    }' "$json_file")

    # Publish via REST API
    local response=$(curl -s -X POST "$API_ENDPOINT" \
        -H "Content-Type: application/json" \
        -u "$USERNAME:$PASSWORD" \
        -d "$payload")

    # Check if publication was successful
    if echo "$response" | jq -e '.id' > /dev/null 2>&1; then
        local post_id=$(echo "$response" | jq -r '.id')
        local post_url=$(echo "$response" | jq -r '.link')
        echo -e "${GREEN}✓ Published Successfully!${NC}"
        echo -e "  Post ID: ${GREEN}$post_id${NC}"
        echo -e "  URL: ${GREEN}$post_url${NC}"
        echo ""
        return 0
    else
        echo -e "${RED}✗ Publication Failed!${NC}"
        echo "Error Response:"
        echo "$response" | jq '.'
        echo ""
        return 1
    fi
}

# Publish Hindi Stories
PUBLISHED=0
FAILED=0

# Story 1: Cricket Match (Hindi)
if publish_story "story_1_cricket_match_hindi.json" "Zimbabwe vs India Cricket Match (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

# Story 2: Rain Cloud (Hindi)
if publish_story "story_2_rain_cloud_hindi.json" "India-South Korea Rain Cloud (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

# Story 3: Jana Nayagan (Hindi)
if publish_story "story_3_jana_nayagan_hindi.json" "Jana Nayagan Film Release (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

# Summary
echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}Publication Summary${NC}"
echo -e "${YELLOW}========================================${NC}"
echo -e "Total Stories: 3"
echo -e "${GREEN}Published: $PUBLISHED${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED${NC}"
fi
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All Hindi stories published successfully!${NC}"
    exit 0
else
    echo -e "${RED}✗ Some stories failed to publish. Please check the errors above.${NC}"
    exit 1
fi
