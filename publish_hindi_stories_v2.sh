#!/bin/bash

set -e

# API Configuration
NEWSPANDIT_URL="https://newspandit.com"
API_ENDPOINT="$NEWSPANDIT_URL/wp-json/wp/v2/posts"
USERNAME="NewsPandit Staff"
PASSWORD="GSIf avuF lFp3 2ZtN aSQx iAMQ"

echo "=========================================="
echo "NewsPandit Hindi Stories Publisher v2"
echo "=========================================="
echo ""

# Fetch category IDs
echo "Fetching categories..."
CATEGORIES=$(curl -s "$NEWSPANDIT_URL/wp-json/wp/v2/categories?per_page=100" | jq -r '.[] | "\(.slug):\(.id)"')

# Create category mapping
declare -A CATEGORY_MAP
while IFS=: read -r slug id; do
    CATEGORY_MAP["$slug"]=$id
done <<< "$CATEGORIES"

# Display categories found
echo "Categories found:"
for slug in "${!CATEGORY_MAP[@]}"; do
    echo "  $slug: ${CATEGORY_MAP[$slug]}"
done
echo ""

# Fetch tag IDs
echo "Fetching tags..."
TAGS=$(curl -s "$NEWSPANDIT_URL/wp-json/wp/v2/tags?per_page=100" | jq -r '.[] | "\(.slug):\(.id)"')

# Create tag mapping
declare -A TAG_MAP
while IFS=: read -r slug id; do
    TAG_MAP["$slug"]=$id
done <<< "$TAGS"

echo "Tags found: $(echo "${!TAG_MAP[@]}" | wc -w)"
echo ""

# Function to convert category slugs to IDs
get_category_ids() {
    local categories_str=$1
    local ids=()
    
    for cat in $(echo "$categories_str" | jq -r '.[]'); do
        if [[ -n "${CATEGORY_MAP[$cat]}" ]]; then
            ids+=("${CATEGORY_MAP[$cat]}")
        fi
    done
    
    echo "[$(IFS=,; echo "${ids[*]}")]"
}

# Function to convert tag slugs to IDs
get_tag_ids() {
    local tags_str=$1
    local ids=()
    
    for tag in $(echo "$tags_str" | jq -r '.[]'); do
        if [[ -n "${TAG_MAP[$tag]}" ]]; then
            ids+=("${TAG_MAP[$tag]}")
        fi
    done
    
    echo "[$(IFS=,; echo "${ids[*]}")]"
}

# Function to publish a story
publish_story() {
    local json_file=$1
    local story_name=$2

    echo "Publishing: $story_name"
    echo "File: $json_file"

    # Read the JSON
    local title=$(jq -r '.title' "$json_file")
    local content=$(jq -r '.content' "$json_file")
    local slug=$(jq -r '.slug' "$json_file")
    local excerpt=$(jq -r '.excerpt' "$json_file")
    local meta_desc=$(jq -r '.meta_description' "$json_file")
    local categories=$(jq -c '.categories' "$json_file")
    local tags=$(jq -c '.tags' "$json_file")
    
    # Get category and tag IDs
    local cat_ids=$(get_category_ids "$categories")
    local tag_ids=$(get_tag_ids "$tags")
    
    echo "  Categories: $categories -> IDs: $cat_ids"
    echo "  Tags: $tags -> IDs: $tag_ids"
    
    # Create payload
    local payload=$(jq -n \
        --arg title "$title" \
        --arg content "$content" \
        --arg slug "$slug" \
        --arg excerpt "$excerpt" \
        --argjson categories "$cat_ids" \
        --argjson tags "$tag_ids" \
        '{
            title: $title,
            content: $content,
            status: "publish",
            slug: $slug,
            excerpt: $excerpt,
            categories: $categories,
            tags: $tags,
            meta: {
                "_yoast_wpseo_metadesc": $excerpt
            }
        }')
    
    # Publish
    local response=$(curl -s -X POST "$API_ENDPOINT" \
        -H "Content-Type: application/json" \
        -u "$USERNAME:$PASSWORD" \
        -d "$payload")

    # Check response
    if echo "$response" | jq -e '.id' > /dev/null 2>&1; then
        local post_id=$(echo "$response" | jq -r '.id')
        local post_url=$(echo "$response" | jq -r '.link')
        echo "✓ Published! ID: $post_id"
        echo "  URL: $post_url"
        echo ""
        return 0
    else
        echo "✗ Failed!"
        echo "$response" | jq '.'
        echo ""
        return 1
    fi
}

# Publish stories
PUBLISHED=0
FAILED=0

if publish_story "story_1_cricket_match_hindi.json" "Story 1: Cricket Match (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

if publish_story "story_2_rain_cloud_hindi.json" "Story 2: Rain Cloud (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

if publish_story "story_3_jana_nayagan_hindi.json" "Story 3: Jana Nayagan (Hindi)"; then
    ((PUBLISHED++))
else
    ((FAILED++))
fi

# Summary
echo "=========================================="
echo "Summary: Published $PUBLISHED, Failed $FAILED"
echo "=========================================="

if [ $FAILED -eq 0 ]; then
    echo "✓ All Hindi stories published successfully!"
    exit 0
else
    echo "✗ Some stories failed"
    exit 1
fi
