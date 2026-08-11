#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
B64=$(printf '%s' "$KARMACTIVE_WP_AUTH" | base64)
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
echo "=== Resolve chosen TAGS to IDs by slug ==="
for s in heatwave extreme-weather public-health-crisis health-alert drought water-scarcity water-conservation water-shortage earthquake seismic colombia glp-1 weight-loss-drugs public-health wildfire climate-crisis; do
  echo "--- $s ---"
  curl -s --max-time 40 -A "$UA" -H "Authorization: Basic $B64" \
    "https://www.karmactive.com/wp-json/wp/v2/tags?slug=$s&per_page=3&_fields=id,name,slug,count"
  echo
done