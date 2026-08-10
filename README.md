# Karmactive Editorial Pipeline — Orchestration

Common ground: this OneDrive-synced git repo. Every tool READS and WRITES files here.
No human copy/paste. Hermes (orchestrator) watches the folders and moves work forward.

## Stages & which tool owns each (ZERO human involvement model)
1. STAGE 0 — Trends topics. Source: Hermes via web tools -> `stage0/topics.md`
2. STAGE 1 — Research angles. Owner: Claude CLI (`claude -p`) writes `stage1/<id>.md`
3. STAGE 2 — Draft. Owner: Claude CLI writes `stage2/<id>.md`
4. STAGE 3a — Multi-model fact-check. Owners:
     - ChatGPT  (browser automation of chatgpt.com) -> `stage3a/<id>_chatgpt.md`
     - Gemini   (browser automation of gemini.google.com) -> `stage3a/<id>_gemini.md`
     - Copilot  (browser automation of copilot.microsoft.com) -> `stage3a/<id>_copilot.md`
     - Hermes   (native review) -> `stage3a/<id>_hermes.md`
5. STAGE 3b — Corrections. Owner: Claude CLI writes `stage3b/<id>.md` (only flagged sentences changed)
6. STAGE 3 follow-up — self-audit. Owner: Claude CLI rewrites full if gaps found
7. STAGE 4 & 5 — SEO package (title, meta, slug, categories from sitemap, tags, focus keyphrase,
                anchored links, feature-image assignment). Owner: Hermes -> `stage4_5/<id>.md`
8. PUBLISH — WP REST API (www only). Owner: Hermes -> `published/<id>.json` (post id + verification)

## File naming
<id> = zero-padded article index, e.g. 01, 02 ... 08

## Common-ground rules (Hermes enforces)
- External links: anchored <a href> opening new tab with rel="noopener noreferrer"
- Internal karmactive links: plain descriptive anchor words
- Feature images: real, properly-licensed (Wikimedia Commons) + attribution caption; vision-verified
- Categories: only from karmactive XML sitemap; no invented categories
- No fabricated facts; banned words: tapestry/beacon/symphony

## Tool triggers (headless)
- Claude:  `claude -p "<prompt>"`  (needs one-time `claude /login`)
- ChatGPT/Gemini/Copilot: browser automation (Nous subscription) using logged-in session
- WP publish: Python requests to https://www.karmactive.com/wp-json/wp/v2/posts

## Status
- [x] Repo in OneDrive (cloud common ground)
- [x] Claude MCP -> OneDrive repo
- [ ] Claude CLI login (one-time, human)
- [ ] Browser automation login check for chatgpt/gemini/copilot
