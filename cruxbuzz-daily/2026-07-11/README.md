# CruxBuzz Daily Entertainment Routine — July 11, 2026

Two fresh US entertainment stories (both broke within the last 24 hours; no overlap with prior runs — this is the first dated folder in the repo).

## Story 1 — Ariana Grande exits American Horror Story Season 13
Folder: `story-1-ariana-grande-ahs13/`
- `editorial-package.md` — story rationale, verified facts, missing-angle strategy, SEO/AEO keywords, internal links, first-hand external sources, feature image with caption/alt/title (Joella Marano, Wikimedia Commons, CC BY-SA 2.0).
- `interactive-article.html` — WordPress Custom-HTML-block piece (gothic FX palette): tappable six-beat timeline, stat tiles, animated tour-vs-shoot calendar-collision graphic, tap-to-reveal cast tracker, AEO FAQ accordion, intro/conclusion text with internal + external backlinks baked in. No H1, no feature image inside; one licensed image sits between sections. Self-contained, mobile-safe, scoped CSS (`ahs13x-`).

## Story 2 — Live-action Moana's opening weekend vs. Evil Dead Burn
Folder: `story-2-moana-live-action-box-office/`
- `editorial-package.md` — same structure; feature image (Eva Rinaldi, Wikimedia Commons, CC BY-SA 2.0).
- `interactive-article.html` — ocean-palette dashboard: weekend scoreboard tiles, animated tap-for-detail ranked chart of Disney remake openings, Moana-vs-Evil-Dead-Burn face-off panel, first-hand quote cards (Johnson, Laga'aia, Cravalho), FAQ accordion, intro/conclusion with backlinks. Same technical constraints, scoped CSS (`mo26x-`).

## Publishing notes
- Add the H1 title and the feature image in WordPress (both are specified in each editorial package); the HTML block deliberately contains neither.
- Box office figures are trade-reported estimates as of Saturday morning; refresh the scoreboard numbers Sunday if publishing after Comscore estimates land.
- This build environment's network policy blocks direct page loads, so every link (internal + external) was verified through current search-index listings instead of live fetches; none showed signs of rot, but click-test them once in the WP editor before publish.
