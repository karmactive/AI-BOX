#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
mkdir -p sitemaps
for n in "" 2 3 4 5 6 7 8; do
  echo "fetching post-sitemap${n}.xml"
  curl -s --max-time 60 -A "$UA" "https://www.karmactive.com/post-sitemap${n}.xml" -o "sitemaps/post${n}.xml"
done
curl -s --max-time 60 -A "$UA" "https://www.karmactive.com/post_tag-sitemap.xml" -o "sitemaps/tags1.xml"
curl -s --max-time 60 -A "$UA" "https://www.karmactive.com/post_tag-sitemap2.xml" -o "sitemaps/tags2.xml"
echo "--- sizes ---"
ls -la sitemaps/ | awk '{print $5, $9}'
echo "--- count URLs per file ---"
for f in sitemaps/post*.xml sitemaps/tags*.xml; do
  echo "$f: $(grep -c '<loc>' "$f")"
done
