#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
# Combine all post URLs into one list
cat sitemaps/post.xml sitemaps/post2.xml sitemaps/post3.xml sitemaps/post4.xml \
    sitemaps/post5.xml sitemaps/post6.xml sitemaps/post7.xml sitemaps/post8.xml \
    | grep -oP '(?<=<loc>)[^<]+' > all_posts.txt
echo "TOTAL POST URLS: $(wc -l < all_posts.txt)"

echo "=== VERIFY FILE'S EMBEDDED INTERNAL LINKS EXIST ==="
for slug in \
  "uk-heatwave-deaths-2026" \
  "uk-farmers-harvest-crisis-2026-frosts-heavy-rain-food-security" \
  "indonesia-molucca-sea-earthquake-ternate-april-2026-tsunami-warning-lifted" \
  "philippines-cebu-6-9-earthquake-historic-churches-power-outage-deaths" \
  "medicare-glp1-obesity-coverage-balance-model-eli-lilly-2026" \
  "pacific-northwest-wildfire-smoke-seattle-portland-air-quality-2026" ; do
  hit=$(grep -c "$slug" all_posts.txt)
  echo "$hit  $slug"
done

echo
echo "=== HARVEST ADDITIONAL RELATED LIVE URLS BY TOPIC ==="
search_topic() {
  echo "--- TOPIC: $1 ---"
  grep -i "$1" all_posts.txt | head -8
}
search_topic "heatwave" 
search_topic "drought"
search_topic "water.*ban\|hosepipe\|south-west-water\|southwest-water"
search_topic "earthquake"
search_topic "mounjaro\|tirzepatide\|glp-1\|glp1"
search_topic "wildfire\|forest-fire\|forest fire"
search_topic "bbc.*weather\|weather.*cut\|weather.*presenter"
search_topic "environment-agency\|climate"
search_topic "pharmaceutical\|mhra\|eli-lilly"
