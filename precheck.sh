#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
B64=$(printf '%s' "$KARMACTIVE_WP_AUTH" | base64)
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
echo "=== SLUG EXISTENCE CHECK (expect empty arrays) ==="
for s in bbc-weather-cuts-heatwave south-west-water-hosepipe-ban-drought colombia-earthquake-seismic-preparedness mounjaro-deaths-mhra-regulatory-capture new-forest-fire-climate-drought-emergency; do
  echo "--- slug: $s ---"
  curl -s --max-time 40 -A "$UA" -H "Authorization: Basic $B64" \
    "https://www.karmactive.com/wp-json/wp/v2/posts?slug=$s&per_page=1&_fields=id,slug,title,status&status=publish,future,draft"
  echo
done
echo "=== TOPIC DUPLICATE SEARCH (distinctive nouns) ==="
for q in "bbc weather cuts" "south west water hosepipe ban" "colombia earthquake" "mounjaro deaths" "new forest fire"; do
  echo "--- topic: $q ---"
  curl -s --max-time 40 -A "$UA" -H "Authorization: Basic $B64" \
    "https://www.karmactive.com/wp-json/wp/v2/posts?search=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&per_page=3&_fields=id,slug,title,date,status&status=publish,future,draft"
  echo
done