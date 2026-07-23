#!/bin/bash
# Run this locally — the remote environment cannot reach giganectar.com
# Credentials: GigaNectar Team / lBFY E5XV zE9G 2nuf bU8Q p9LX

WP_USER="GigaNectar Team"
WP_PASS="lBFY E5XV zE9G 2nuf bU8Q p9LX"
WP_API="https://giganectar.com/wp-json/wp/v2/posts"

for story in story1_wildfires story2_houthi story3_lavrov story4_greece; do
  echo "Publishing $story..."
  curl -s -X POST "$WP_API" \
    -u "$WP_USER:$WP_PASS" \
    -H "Content-Type: application/json" \
    -d @"${story}.json" | python3 -m json.tool | grep -E '"id"|"link"|"status"'
  echo "---"
done
