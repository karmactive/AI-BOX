FRESH STAGE 4/5 TASK — Haiku

You are producing the FINAL Stage 4/5 SEO-packaged file for 7 article sections (8 Australia stories, Census+RBA merged) that were already fact-checked and resolved in `stage3b_final.md`.

READ THESE FILES FIRST (they are in the working directory, granted via --add-dir):
- stage3b_final.md  → the 7 resolved article bodies. Copy each body VERBATIM into the output (keep all headings). Do NOT rewrite facts.
- sitemap_categories.txt → VALID category list. Use ONLY these, lowercase, no new categories.
- sitemap_tags.txt → VALID tag list. Pick 2–5 per article from here only.
- sitemaps/post*.xml → source of REAL internal links. Search them for a karmactive.com article URL that is TOPIC-RELEVANT to each story, and use its real URL + descriptive anchor text.

OUTPUT: write ONE file named `stage5_haiku_v2.md`.

FOR EACH of the 7 sections, output this EXACT labeled block (do not use YAML keys like title:/slug: — use the literal labels below):

## [COMBINED TITLE here]

- **COMBINED TITLE:** [one compelling headline]
- **META DESCRIPTION (200 characters):** [EXACTLY 200 characters including spaces — count carefully, then pad or trim to exactly 200]
- **FOCUS KEY PHRASE (4 words):** [exactly 4 words]
- **SEO SLUG:** [url-safe-hyphenated-lowercase]
- **CATEGORIES:** [2–4 from sitemap_categories.txt, lowercase, comma-separated in brackets]
- **TAGS:** [2–5 from sitemap_tags.txt in brackets]
- **EXTERNAL LINKS:** [1 official/gov URL + anchor text, e.g. https://www.abs.gov.au/census — ABS 2026 Census]
- **INTERNAL LINKS:** [1 REAL karmactive.com URL found in sitemaps/post*.xml that is TOPIC-RELEVANT + anchor text. If none matches, write "INTERNAL LINK NEEDED: <topic>" — NEVER invent a URL]

Then the article body copied verbatim from stage3b_final.md for that section.

CRITICAL RULES (these were failed last time — follow exactly):
1. META DESCRIPTION must be EXACTLY 200 characters. Not 188, not 292. Count and verify.
2. FOCUS KEY PHRASE must be EXACTLY 4 words.
3. INTERNAL LINKS must be TOPIC-RELEVANT. Census article → a census/data/privacy karmactive post. Social media ban → a youth/social-media/tech policy post. Do NOT link Census to a climate article or Social Ban to a wind-turbine article.
4. CATEGORIES: only from sitemap_categories.txt (australia, policy, business, environment, conservation, disaster, latest, news, technology, mobility, electric, lgbtq, wildlife, health, etc.). No invented categories.
5. TAGS: only from sitemap_tags.txt. 2–5 each.
6. Copy article bodies verbatim — do not alter the resolved facts.

The 7 sections (in order, matching stage3b_final.md):
1. Census Cyber-Battleground (Sunita) — cats: australia, policy, technology, lgbtq
2. Jackie's Wings Conservation (Rahul) — cats: australia, conservation, wildlife, environment
3. RBA Rates 4.35% (Govind) — cats: australia, business, latest, policy
4. Colombia Earthquake (Sonali) — cats: disaster, latest, news
5. Stellantis Recall (Rahul) — cats: australia, business, latest
6. Mitsubishi ASX VR-e EV (Govind) — cats: australia, mobility, electric, technology
7. Social Media Ban (Sunita) — cats: australia, policy, latest, technology

After writing the file, report: section count, each meta char count, each focus phrase word count, and which internal links you used (URL + whether topic-relevant).
