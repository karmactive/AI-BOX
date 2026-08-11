#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
B64=$(printf '%s' "$KARMACTIVE_WP_AUTH" | base64)
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
q() {
  echo "=== TAG search: $1 ==="
  curl -s --max-time 40 -A "$UA" -H "Authorization: Basic $B64" \
    "https://www.karmactive.com/wp-json/wp/v2/tags?search=$1&per_page=15&_fields=id,name,slug,count"
  echo
}
q "heatwave"
q "drought"
q "water"
q "earthquake"
q "seismic"
q "natural%20disaster"
q "wildfire"
q "forest%20fire"
q "mounjaro"
q "weight%20loss"
q "obesity"
q "pharmaceutical"
q "colombia"
q "extreme%20weather"
q "britain"
q "eli%20lilly"
