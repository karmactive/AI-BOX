#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
echo "=== Live HTTP status for each published URL ==="
for u in \
  "https://www.karmactive.com/bbc-weather-cuts-heatwave/" \
  "https://www.karmactive.com/south-west-water-hosepipe-ban-drought/" \
  "https://www.karmactive.com/colombia-earthquake-seismic-preparedness/" \
  "https://www.karmactive.com/mounjaro-deaths-mhra-regulatory-capture/" \
  "https://www.karmactive.com/new-forest-fire-climate-drought-emergency/" ; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -A "$UA" "$u")
  echo "$code  $u"
done
echo
echo "=== Yoast meta render check (ART1 bbc-weather) ==="
curl -s -A "$UA" "https://www.karmactive.com/bbc-weather-cuts-heatwave/?nocache=1" \
  | grep -o '<meta name="description"[^>]*>' | head -1
curl -s -A "$UA" "https://www.karmactive.com/bbc-weather-cuts-heatwave/?nocache=1" \
  | grep -o '<meta name="keywords"[^>]*>' | head -1
echo
echo "=== confirm one internal+external anchor renders (ART2) ==="
curl -s -A "$UA" "https://www.karmactive.com/south-west-water-hosepipe-ban-drought/?nocache=1" \
  | grep -o 'href="https://www.southwestwater.co.uk/"' | head -1
curl -s -A "$UA" "https://www.karmactive.com/south-west-water-hosepipe-ban-drought/?nocache=1" \
  | grep -o 'href="https://www.karmactive.com/southern-water-bans-tankers-billionaire-estate-drought/"' | head -1