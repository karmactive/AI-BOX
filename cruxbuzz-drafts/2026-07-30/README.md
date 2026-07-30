# 2026-07-30 CruxBuzz daily content run — BLOCKED at publish step

Two fully researched, fact-checked, SEO/AEO-ready interactive HTML articles were produced but
**could not be published to cruxbuzz.com**: the WordPress Application Password provided in the
task (`CruxBuzz Staff` / `82Ov q03g L7Jy CTH1 Klqv grLn`) failed authentication.

## What was tried
- REST API Basic Auth (`/wp-json/wp/v2/users/me`) via both `curl -u` and an explicit
  `Authorization: Basic ...` header → **401 `rest_not_logged_in`** both times.
- The site's own `jwt-auth/v1/token` endpoint with the same credentials → **403 `invalid_credentials`**.
- The REST API itself works fine anonymously (`GET /wp-json/wp/v2/posts` → 200), so the site and API
  are healthy; only authentication is failing.

## Most likely cause
A clean core-level 401 on Application Password Basic Auth (rather than a WAF block page) is the
classic symptom of the web host **stripping the `Authorization` header before it reaches PHP** —
common on shared LiteSpeed/Hostinger hosting (confirmed via response headers: `server: LiteSpeed`,
`platform: hostinger`) unless a rewrite rule forwards it. This needs a server-side fix (e.g. an
`.htaccess` rule forwarding `HTTP_AUTHORIZATION`) or a fresh Application Password generated and
re-tested. It could also mean the WordPress login name differs from the display name "CruxBuzz Staff".

## What's ready to go
- `ariana-grande-hacker-lawsuit.html` + its `-METADATA.md` (title/meta/tags/category/slug/image/sources)
- `madison-beer-justin-herbert-engagement.html` + its `-METADATA.md`

Both are self-contained HTML (no `<h1>`, no feature image tag, no doctype/head/body) ready to paste
into a WordPress Custom HTML block, with internal cruxbuzz.com backlinks, first-hand external
sources, mobile-responsive interactive widgets, and passive/factual (non-analytical) conclusions
per the house style rules.

## Second known limitation: link verification
This session's network egress was restricted to cruxbuzz.com only — every other external host
(Wikimedia, NFL.com, Instagram, justice.gov, riaa.org, fbi.gov, even wikipedia.org/example.com)
returned 403 at the proxy level. All external source URLs were cross-corroborated via multiple
WebSearch results but **not** live HTTP-verified as functioning. A manual click-check of the
external links and the two Wikimedia image URLs is recommended before publishing.

## To publish once auth is fixed
1. Fix the Application Password auth (see above) and re-verify with:
   `curl -u "USERNAME:APP_PASSWORD" https://cruxbuzz.com/wp-json/wp/v2/users/me`
2. Manually click-verify the external + image links listed in each `-METADATA.md`.
3. Create the post via `POST /wp-json/wp/v2/posts` with the HTML as `content`, title/slug/excerpt
   from the metadata file, category/tag IDs looked up from `/wp-json/wp/v2/categories` and
   `/wp-json/wp/v2/tags`, and insert the feature image between the two paragraphs marked
   `<!-- FEATURE IMAGE GOES HERE -->` (do not set it as the WordPress featured image / no `<h1>`).
