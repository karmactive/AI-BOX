#!/usr/bin/env bash
cd /c/Users/Hp/OneDrive/karmactive-pipeline
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
# Fetch the category sitemap (name list)
curl -s --max-time 60 -A "$UA" "https://www.karmactive.com/category-sitemap.xml" -o sitemaps/cats.xml
echo "cats.xml urls: $(grep -c '<loc>' sitemaps/cats.xml)"

# Extract category NAMES from category-sitemap (the <loc> ends with /category-slug/)
echo "=== CATEGORY NAMES (from sitemap) ==="
grep -oP '(?<=<loc>)[^<]+' sitemaps/cats.xml | sed -E 's#.*/([^/]+)/?$#\1#' | sed 's/-/ /g' | sort -u > sitemap_categories.txt
cat sitemap_categories.txt

# Extract TAG NAMES from post_tag sitemaps
echo "=== TAG NAMES (from sitemap) ==="
cat sitemaps/tags1.xml sitemaps/tags2.xml | grep -oP '(?<=<loc>)[^<]+' | sed -E 's#.*/([^/]+)/?$#\1#' | sed 's/-/ /g' | sort -u > sitemap_tags.txt
wc -l sitemap_tags.txt
echo "(first 40)"
head -40 sitemap_tags.txt