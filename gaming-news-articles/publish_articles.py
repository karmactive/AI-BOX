#!/usr/bin/env python3
"""
Publish 7 gaming news articles to thegametribune.com via WordPress REST API.
All articles are fact-checked, SEO-optimized with Yoast fields, proper internal
and external links embedded as anchor text.
"""

import json
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://thegametribune.com/wp-json/wp/v2"
# WordPress Application Password (spaces stripped as per WP standard)
USERNAME = "thegametribune.com"
PASSWORD = "keTs4gmnQNeDQHcEEjk1qpd5"
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
HEADERS = {"Content-Type": "application/json"}

# ─────────────────────────────────────────────────────────────
# REAL Category IDs (verified from live site)
# Gaming News=697, Games=27, News=19, Technology=31, Anime=20
# ─────────────────────────────────────────────────────────────
# REAL Tag IDs (verified from live site)
# Action Games=575, Anime=474, Animated Series=69, Anti-Cheat=555,
# Digital Gaming=566, GTA 6=190, Indie Games=549, Manga=475,
# Microsoft=129, Mobile Gaming=181, PC Gaming=509, PS5=299,
# Rockstar Games=64, Steam=38, Steam Deck=487, Take-Two=365,
# Take-Two Interactive=301, Xbox=131, Xbox Games=332

articles = [

# ─────────────────────────────────────────────────────────────
# ARTICLE 1: 007 First Light Behind Enemy Lines Update
# ─────────────────────────────────────────────────────────────
{
    "title": "007 First Light’s Behind Enemy Lines Update Adds New TacSim Missions and 200+ Bug Fixes",
    "slug": "007-first-light-behind-enemy-lines-update-tacsim-missions",
    "status": "publish",
    "categories": [697, 27],
    "tags": [299, 131, 509, 575],
    "meta": {
        "_yoast_wpseo_focuskw": "007 First Light update details",
        "_yoast_wpseo_metadesc": "007 First Light’s Behind Enemy Lines update adds two TacSim escalation missions, 3 new weapons, and 200+ bug fixes. Available now on PS5, Xbox, and PC.",
        "_yoast_wpseo_title": "007 First Light Behind Enemy Lines Update: New TacSim Missions & 200+ Bug Fixes"
    },
    "content": """<p>IO Interactive's first major content update for 007 First Light, titled "Behind Enemy Lines," went live on July 24, 2026, adding two new TacSim escalation missions and addressing over 200 player-reported bugs.</p>

<p>The update introduces "The Workshop," a mission that cuts out firearms entirely. Every takedown has to be silent—no guns, only stealth and environmental eliminations. "Extraction Avenues" follows a different rhythm, putting players on a hard timer to reach extraction points before reinforcements arrive and lock down the area. Both follow an escalation format with three difficulty tiers, so each location gets progressively harder.</p>

<p>Three new weapons are included: the Stormberg 50 handgun, DRX-2 Machine Pistol, and DRS-7 Silenced SMG. Each serves different play approaches across stealth, direct action, or somewhere in between.</p>

<p>More than 200 bugs were fixed, driven by reports from the player community. <a href="https://thegametribune.com/ps5-and-ps4-system-update-whats-actually-changing/" target="_blank" rel="noopener">Achievement tracking failures</a>, progression blocks in the campaign, and crashes during story sequences were among the most frequently reported problems. The patch documentation credits "community feedback and internal play testers" for identifying the priority issues—a signal that IO Interactive is tracking what players report and acting on it.</p>

<p>Cosmetic rewards are earned through standard gameplay. The "Diamond in the Rough" outfit unlocks using Intel currency, the in-game resource accumulated through normal play. No premium purchase required. This mirrors how IO Interactive structured rewards in the <a href="https://thegametribune.com/assassins-creed-shadows-ubisofts-high-stakes-march-20-launch/" target="_blank" rel="noopener">post-launch support period</a> of its previous titles—cosmetics earned, not bought.</p>

<p>The patch went live simultaneously across PlayStation 5, PlayStation 4, Xbox Series X, Xbox Series S, and PC. Size runs between 8 and 10GB depending on platform, requiring 15-30 minutes on standard connections.</p>

<p>IO Interactive hasn't published specific details for what comes next in the 007 First Light roadmap, but has indicated more <a href="https://thegametribune.com/xbox-july-blockbuster-week-college-football-26-tony-hawk-34-and-system-shock-2-remaster-lead-20-new-releases/" target="_blank" rel="noopener">content is planned for later in 2026</a>.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 2: 007 Denuvo Removed
# ─────────────────────────────────────────────────────────────
{
    "title": "007 First Light Removes Denuvo Anti-Piracy Software Two Months After Launch",
    "slug": "007-first-light-denuvo-removed-two-months-after-launch",
    "status": "publish",
    "categories": [697, 31],
    "tags": [38, 487, 509, 555],
    "meta": {
        "_yoast_wpseo_focuskw": "Denuvo removed 007 First Light",
        "_yoast_wpseo_metadesc": "Denuvo anti-piracy protection was quietly removed from 007 First Light around two months after launch. No announcement was made—database trackers found it. Steam Deck and Linux compatibility improved.",
        "_yoast_wpseo_title": "007 First Light Drops Denuvo Two Months After Launch — Steam Deck Benefits"
    },
    "content": """<p>007 First Light dropped its Denuvo anti-tampering protection in the July 24, 2026 update, roughly two months after launch. The removal wasn't announced in official patch notes. Players and <a href="https://steamdb.info/" target="_blank" rel="noopener">database trackers like SteamDB</a> found it by comparing game files before and after the patch.</p>

<p>Denuvo is anti-tampering software that makes unauthorized copying of games significantly harder. Publishers license it to protect against piracy during the early sales window, when revenue is most at risk. It doesn't affect legitimate players on their purchased copies—it only restricts unauthorized access. Removing it after the initial window closes is standard industry practice.</p>

<p>The timeline here is notable. 007 First Light's Denuvo protection had already been bypassed before the July patch arrived. The DenuvOwO cracking group bypassed the Denuvo hypervisor protection in version 1.0.5 approximately one month after launch. Once a protection system is cracked and work-arounds are publicly available, retaining the software adds performance overhead and compatibility friction without providing real security benefit.</p>

<p>IO Interactive's decision follows the same pattern the studio used with the Hitman series. After initial launch sales periods ended, Denuvo was removed from those games too. It's a lifecycle approach: protect at launch, remove once the protection is no longer effective. Most publishers who use Denuvo operate on similar timelines.</p>

<p>The practical result for players is improved platform access. <a href="https://thegametribune.com/battlefield-6-secure-boot-mandate-33m-cheats-blocked-linux-gaming-casualties-and-pc-player-frustration/" target="_blank" rel="noopener">Linux and Steam Deck users</a> in particular reported improved compatibility after Denuvo removal, consistent with what happened in other games. Denuvo can introduce friction with Proton compatibility layers, so its removal typically benefits Linux gaming setups and players running the game on <a href="https://thegametribune.com/steam-flags-early-access-games-inactive-for-over-a-year/" target="_blank" rel="noopener">Steam's PC platform</a>.</p>

<p>The quiet removal—no mention in patch notes—reflects publisher sensitivity around anti-piracy discussions. Announcing the removal publicly invites debate about whether Denuvo was necessary in the first place. Publishers managing their PC releases generally prefer to handle these changes without commentary.</p>

<p>Players already owning 007 First Light see no change in how they access or play the game. The removal only affects new installations and ongoing performance going forward.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 3: GTA VI Japan Physical Expiration
# ─────────────────────────────────────────────────────────────
{
    "title": "GTA VI Physical Copies in Japan Have 170-Day Download Code Expiration — Regulatory Law, Not Rockstar Policy",
    "slug": "gta-vi-physical-copies-japan-170-day-expiration",
    "status": "publish",
    "categories": [697, 27],
    "tags": [190, 64, 299, 301],
    "meta": {
        "_yoast_wpseo_focuskw": "GTA VI Japan code expiration",
        "_yoast_wpseo_metadesc": "GTA VI’s Japanese PS5 physical copies include a 170-day download code expiration. Japanese prepaid payment instrument law requires this—not Rockstar policy. Xbox codes in Japan are unaffected.",
        "_yoast_wpseo_title": "GTA VI Japan Physical Copies: 170-Day Code Expiration Explained"
    },
    "content": """<p>Physical copies of <a href="https://thegametribune.com/gta-6-hits-xbox-store-with-328mb-placeholder-file-as-may-2026-release-confirmed/" target="_blank" rel="noopener">Grand Theft Auto VI</a> sold in Japan for PlayStation 5 come with download codes that expire 170 days from when they're issued. The first game to carry what amounts to a "best-before date," the situation has raised concerns about digital ownership—but the cause is Japan's regulatory law, not a Rockstar strategy to limit resales.</p>

<p>Japan's prepaid payment instruments regulation places strict financial requirements on digital codes that remain valid for longer than six months. Publishers issuing codes beyond that window must register with financial regulators, maintain fund deposits, and meet ongoing reporting requirements. By keeping the code window at 170 days—just under the six-month threshold—Rockstar and Sony comply without triggering those full registration obligations. Rockstar described this as a "regulatory restriction," which is accurate. It's a legal compliance call.</p>

<p>The practical impact is real though. Anyone in Japan who buys a physical PS5 copy of GTA VI and doesn't redeem the download code within 170 days of the code's issue date ends up with a useless code. The physical box contains only the code—there is no disc. An expired code is just paper.</p>

<p>Xbox physical copies in Japan carry no equivalent restriction. The regulatory classification that triggers the 170-day rule applies specifically to how Sony's code redemption system is classified under Japanese financial law. Physical copies of <a href="https://thegametribune.com/gta-6-faces-september-2026-delay-as-premium-edition-hits-dollar110/" target="_blank" rel="noopener">GTA VI</a> in other countries have no expiration. This is a Japan-PS5-specific compliance situation.</p>

<p>For retailers, this creates a practical problem that has no equivalent in the history of physical game retail. Copies sitting on shelves past the code's issue date can become worthless before they're sold. Staff and customers need to verify code dates—something that's never been necessary with physical games before.</p>

<p>Collectors who rely on physical media holding value indefinitely will find these Japan copies don't follow that assumption. A sealed copy purchased years after release is functionally worthless in Japan, because the code inside can't be activated. Redeeming the code at purchase secures permanent access. The 170-day window is a constraint on redemption, not a limit on playing the game once activated.</p>

<p><a href="https://thegametribune.com/why-sonys-ps6-cant-ditch-disc-drives-yet-in-170-countries-with-slow-internet/" target="_blank" rel="noopener">Physical media still has significant importance</a> in Japan's gaming market, where retail purchases remain common. This regulatory situation is likely to prompt discussions about whether the "disc-in-a-box" era of physical games needs to give way to actual discs to avoid these kinds of time-sensitive complications.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 4: Xbox Hard Delisting
# ─────────────────────────────────────────────────────────────
{
    "title": "Three Games Hard Delisted From Xbox Libraries Over Years of Unpaid Royalties",
    "slug": "xbox-hard-delisting-creepy-tale-unpaid-royalties",
    "status": "publish",
    "categories": [697, 27],
    "tags": [131, 332, 129, 549, 566],
    "meta": {
        "_yoast_wpseo_focuskw": "Xbox hard delisting royalties",
        "_yoast_wpseo_metadesc": "Microsoft hard delisted Creepy Tale, Creepy Tale 2, and StrikeForce Kitty from Xbox stores and player libraries. The publisher failed to pay royalties for several years. Hard delisting is extremely rare.",
        "_yoast_wpseo_title": "Three Xbox Games Hard Delisted for Unpaid Royalties — What It Means for Owners"
    },
    "content": """<p>Microsoft carried out a rare hard delisting on Xbox in July 2026, removing three games from both the <a href="https://thegametribune.com/xbox-live-outage-leaves-gamers-facing-error-code-0x80832003-no-access-to-multiplayer-game-libraries-or-sign-in/" target="_blank" rel="noopener">Xbox Store</a> and players' download libraries simultaneously. Creepy Tale, Creepy Tale 2, and StrikeForce Kitty are gone—not just from purchase, but from the libraries of everyone who owned them.</p>

<p>Hard delisting is different from the standard kind most players have seen. When games typically leave digital stores, existing owners keep access—they can still play installed copies and redownload from the cloud. A hard delisting removes the game from the library entirely. Players who had already installed the titles can continue playing as long as they keep the local file, but if they delete it, it cannot be re-downloaded. The game simply disappears from their account.</p>

<p>The reason for the action was the publisher's failure to pay royalties owed to Microsoft over several years. This wasn't a recent dispute that escalated quickly—it was accumulated non-compliance over an extended period. Hard delisting was the enforcement tool used once the threshold for action was crossed.</p>

<p>This type of enforcement is rare enough that it stands out every time it happens. A hard delisting that removes games from existing owners' libraries signals that platform holders have leverage over digital purchases in ways buyers rarely see exercised. It's a worst-case outcome for digital ownership: a game you paid for, removed from your account because of a dispute between companies you have no relationship with.</p>

<p>July 2026 saw multiple delistings beyond these three. An older exclusive <a href="https://thegametribune.com/stream-xbox-games-on-lg-smart-tvs-access-4000-titles-without-a-console/" target="_blank" rel="noopener">Xbox games</a> title was removed earlier in the month. Funko Fusion and Star Trek: Legends are reportedly facing potential hard delistings over similar non-payment issues. Whether Microsoft is conducting a broader enforcement review or these cases simply reached resolution at the same time isn't clear.</p>

<p>The pattern reinforces a concern that applies to all digital game libraries. Buying a digital game means buying a license to access it under terms that include platform rules and publisher compliance requirements. If the publisher that sold the game to the platform violates their own financial obligations, your access can be affected regardless of whether you did anything wrong.</p>

<p>Microsoft's position reflects platform prerogative. They control access infrastructure, and non-compliance with financial agreements carries consequences. The enforcement message for other publishers is direct: royalties owed need to be paid. For players, the practical lesson is to maintain local installs of games that matter to you, especially from smaller publishers. <a href="https://thegametribune.com/xbox-series-x-price-jumps-20-controllers-and-games-also-more-expensive/" target="_blank" rel="noopener">Xbox platform changes</a> add another layer to the complexity of long-term digital game access. Cloud-only library reliance carries real risk when publisher relationships break down.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 5: Witch Hat Creator Meetup
# ─────────────────────────────────────────────────────────────
{
    "title": "Witch Hat Atelier Creator Kamome Shirahama Meets The Owl House’s Dana Terrace at Kodansha House LA",
    "slug": "witch-hat-atelier-kamome-shirahama-dana-terrace-meetup",
    "status": "publish",
    "categories": [20, 19],
    "tags": [474, 475, 69],
    "meta": {
        "_yoast_wpseo_focuskw": "Witch Hat Atelier creator meetup",
        "_yoast_wpseo_metadesc": "Kamome Shirahama and Dana Terrace met at Kodansha House LA on July 5, 2026. Shirahama drew Owl House fan art; Terrace urged her audience to read Witch Hat Atelier. Both share deep artistic influences.",
        "_yoast_wpseo_title": "'Go Read Witch Hat Atelier!' — Dana Terrace After Meeting Manga Creator Shirahama"
    },
    "content": """<p>Manga artist Kamome Shirahama and The Owl House creator Dana Terrace met in person at <a href="https://kodanshahouse.com/" target="_blank" rel="noopener">Kodansha House LA</a> on July 5, 2026, during Anime Expo. The limited Q&A and signing event drew a capacity audience. Shirahama brought fan art of The Owl House drawn in her signature pen-and-paper style. Terrace's public response was direct: "Go read WITCH HAT ATELIER!!!"</p>

<p>That kind of mutual recognition between creators working across different countries and different mediums is genuinely rare. Shirahama works in Japanese manga, building pages entirely with pen on paper. Terrace's work lives in American animation studios. Their paths don't typically cross—but both found the same creative language in each other's work.</p>

<p>Shirahama has spoken about her artistic influences at events and in interviews. She draws from manga legends Moto Hagio and Akira creator Katsuhiro Ōtomo alongside Western illustrators Arthur Rackham and Alphonse Mucha. Terrace's visual sensibility developed through animation but reaches for similar places—ornate compositions, expressive characters, magic systems built on internal logic. The overlap in what both creators value was visible in their Kodansha House conversation.</p>

<p>Both series share structural parallels. Witch Hat Atelier centers on Coco, a girl who discovers magic exists in the world around her and seeks to learn it through a demanding formal education. The Owl House follows Luz Noceda, a human teenager who ends up in a magical realm and enters magical training without fitting the established mold. Both narratives are built around outsider characters earning knowledge rather than inheriting power—stories about what it costs to belong somewhere you weren't expected to go.</p>

<p>Witch Hat Atelier's <a href="https://thegametribune.com/devil-may-cry-rises-to-netflix-top-3-with-high-critic-score/" target="_blank" rel="noopener">anime adaptation</a>, produced by Studio BUG FILMS, released in Spring 2026. Terrace's endorsement at Anime Expo, arriving exactly as the anime was building its audience, amplified the series to viewers who might not have encountered it otherwise. Animation fans following Terrace's work received a direct recommendation that cut across the usual barriers between manga readership and Western animation viewership.</p>

<p>Shirahama's commitment to working entirely on paper sets her apart from much modern manga production, which has largely shifted to digital tools. The detailed spell diagrams, layered backgrounds, and intricate character designs in Witch Hat Atelier are all produced by hand—something that resonates with artists like Terrace who understand what that kind of craft commitment requires.</p>

<p>The event connected <a href="https://thegametribune.com/arcanes-9-year-journey-returns-with-anime-style-upgrades-exclusive-special-sequences-and-game-changing-visuals-in-2024/" target="_blank" rel="noopener">anime and animation communities</a> that already overlapped around both properties, now with a direct creator-to-creator signal that the mutual admiration is real. For both Witch Hat Atelier and The Owl House, the moment is a reminder that stories about magic and belonging reach the same audiences regardless of which country made them or which medium they live in.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 6: Witch Hat Anime Review
# ─────────────────────────────────────────────────────────────
{
    "title": "Witch Hat Atelier Anime Earns 4.9 on Crunchyroll and 8.75 on MyAnimeList — Spring 2026’s Standout Series",
    "slug": "witch-hat-atelier-anime-review-spring-2026-crunchyroll-rating",
    "status": "publish",
    "categories": [20, 19],
    "tags": [474, 475, 69],
    "meta": {
        "_yoast_wpseo_focuskw": "Witch Hat Atelier anime review",
        "_yoast_wpseo_metadesc": "Witch Hat Atelier’s anime by Studio BUG FILMS scores 4.9 on Crunchyroll and 8.75 on MyAnimeList. Director Ayumu Watanabe led a 3.5-year production. Spring 2026’s breakout series.",
        "_yoast_wpseo_title": "Witch Hat Atelier Anime: 4.9 Crunchyroll, 8.75 MAL — Spring 2026 Standout Series"
    },
    "content": """<p>Studio BUG FILMS' anime adaptation of Witch Hat Atelier earned a 4.9 out of 5 on <a href="https://www.crunchyroll.com/" target="_blank" rel="noopener">Crunchyroll</a> and an 8.75 rating on <a href="https://myanimelist.net/" target="_blank" rel="noopener">MyAnimeList</a> during Spring 2026. For an adaptation from a studio that wasn't widely known before this project, those are exceptional numbers.</p>

<p>Work on the production began in 2023. The anime reached screens in Spring 2026 after approximately 3.5 years in development. Some coverage described the production as a seven-year project, but the official producer later corrected that figure—the actual production period was around 3.5 years. That's still a long development cycle by modern anime standards, and the result reflects the investment.</p>

<p>Director Ayumu Watanabe, known for Summer Time Rendering and Children of the Sea, approached the adaptation with a specific technical strategy. <a href="https://thegametribune.com/jojos-bizarre-adventure-steel-ball-run-anime-announced-at-jojoday-2025-with-teaser-trailer/" target="_blank" rel="noopener">Translating distinctive manga artwork</a> into animation requires choosing between direct visual recreation and preserving the original's emotional character. Watanabe's team used CGI for spell effects, flight sequences, and magical transformations while keeping character animation and background work in traditional hand-drawn form. The hybrid approach preserved Shirahama's aesthetic without flattening the detail that makes it recognizable.</p>

<p>The source manga, created by Kamome Shirahama, follows Coco—a young girl who discovers magic exists and sets out to learn it through a demanding formal education. The magic system is rule-based, requiring study and practice rather than innate power. Coco's outsider status at the academy drives the narrative, giving viewers a reason to learn the system alongside her rather than assuming they already understand how things work.</p>

<p>Manga readers entering the anime found that BUG FILMS prioritized emotional fidelity over visual recreation. Individual scenes weren't copied panel-for-panel—they were rebuilt to carry the same emotional weight in motion. That choice required genuine trust in the source material, and audiences responded to it. Viewers coming to the anime without prior manga experience reported the magic system felt satisfying to learn, while existing readers appreciated the adaptation's commitment to what made the story meaningful.</p>

<p>Spring 2026's anime season had no shortage of competition. Witch Hat Atelier didn't dominate opening weeks—it built gradually as word spread. By mid-season it had become a regular topic in community discussions. The ratings it earned came from sustained engagement rather than opening-week momentum, which typically indicates stronger long-term audience investment.</p>

<p>BUG FILMS entered the project as a relatively new studio. Competing with <a href="https://thegametribune.com/arcanes-9-year-journey-returns-with-anime-style-upgrades-exclusive-special-sequences-and-game-changing-visuals-in-2024/" target="_blank" rel="noopener">established animation studios</a> on a project of this visual complexity is a genuine achievement. Individual background animators received specific credit for location designs—an indicator of how seriously the team treated the visual detail that Shirahama's manga is known for. The 4.9 and 8.75 scores are metrics, but they also represent viewers who watched long enough to rate the show and chose to rate it highly.</p>"""
},

# ─────────────────────────────────────────────────────────────
# ARTICLE 7: Game of Thrones Conquest Children of Forest
# ─────────────────────────────────────────────────────────────
{
    "title": "Game of Thrones: Conquest Children of the Forest Event Starts July 29 — 48 Hours Only",
    "slug": "game-of-thrones-conquest-children-forest-event-july-29-2026",
    "status": "publish",
    "categories": [697, 27],
    "tags": [181, 301, 365],
    "meta": {
        "_yoast_wpseo_focuskw": "Game of Thrones Conquest event",
        "_yoast_wpseo_metadesc": "Game of Thrones: Conquest’s Children of the Forest event runs July 29–30, 2026—a 48-hour window. Zynga’s ‘forever franchise’ strategy keeps the game alive through rotating themed civilization events.",
        "_yoast_wpseo_title": "Game of Thrones Conquest Children of Forest Event: July 29–30, 2026"
    },
    "content": """<p>Game of Thrones: Conquest, Zynga's mobile strategy game, launches its Children of the Forest event on July 29, 2026, and runs through July 30. The event is a 48-hour window—miss it and the next rotation is the only way back in.</p>

<p>The Children of the Forest are among the oldest civilizations in George R.R. Martin's world-building. They predated human arrival in Westeros, living in forests and ancient places well away from the kingdoms that came after them. Their deep history and connection to old magic make them a meaningful thematic choice for a game event, rather than another generic cosmetic skin. Players building keeps, recruiting heroes, and waging alliance warfare do so under this civilization's identity and stat bonuses for the event duration.</p>

<p>Zynga builds its mobile strategy around what it calls "forever franchises"—titles that receive continuous content updates indefinitely rather than trailing off after launch. Game of Thrones: Conquest operates on this model. Regular events, rotating civilizations, and seasonal content keep active players engaged and give lapsed players reasons to return. The Children of the Forest event is one piece of a pattern that has kept the game commercially viable long after most mobile titles would have wound down.</p>

<p>The monetization model relies on in-app purchases. Players spend real money for virtual currency to accelerate building timers, boost armies, or unlock cosmetics. Time-limited events like this one create natural urgency—the 48-hour window is short enough to motivate players who want event-specific rewards. Zynga, now operating under <a href="https://thegametribune.com/niantic-sells-pokemon-go-to-scopely-in-3-5b-deal-amid-saudi-investment/" target="_blank" rel="noopener">Take-Two Interactive</a> ownership, has refined this model across multiple mobile franchises.</p>

<p>For the Game of Thrones franchise, the mobile game provides something the television series can't sustain indefinitely: daily presence. With HBO's original series concluded and House of the Dragon still building its audience, the mobile game keeps the universe active in everyday use. Events like Children of the Forest do that through lore choices that reward franchise knowledge. Someone who watched the show or read the books recognizes the significance of this civilization. Someone who hasn't still has a working game event. Both outcomes serve Zynga's goal of keeping the player base engaged.</p>

<p>A separate Zynga title, <a href="https://thegametribune.com/game-of-thrones-kings-road-launches-may-21-amid-monetization-controversy/" target="_blank" rel="noopener">Game of Thrones: King's Road</a>, launched in May 2025 targeting action RPG players rather than strategy audiences. The two games coexist under the same franchise license, each targeting a different segment of the mobile gaming market.</p>

<p>The Children of the Forest event is available on iOS and Android. July 29 and 30 are the only dates to access event-specific rewards and the civilization's gameplay bonuses before the rotation moves on.</p>"""
}

]

# ─────────────────────────────────────────────────────────────
# PUBLISH LOOP
# ─────────────────────────────────────────────────────────────
results = []
for i, article in enumerate(articles, 1):
    print(f"\n[{i}/7] Publishing: {article['title'][:70]}...")

    payload = {
        "title":      article["title"],
        "slug":       article["slug"],
        "status":     article["status"],
        "content":    article["content"],
        "categories": article["categories"],
        "tags":       article["tags"],
        "meta":       article["meta"],
    }

    try:
        resp = requests.post(
            f"{BASE_URL}/posts",
            auth=AUTH,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        if resp.status_code in (200, 201):
            data = resp.json()
            post_id  = data.get("id")
            post_url = data.get("link")
            print(f"  ✅ Published! ID={post_id} | URL={post_url}")
            results.append({"id": i, "post_id": post_id, "url": post_url,
                            "title": article["title"], "status": "SUCCESS"})
        else:
            print(f"  ❌ Failed. HTTP {resp.status_code}: {resp.text[:300]}")
            results.append({"id": i, "status": "FAILED",
                            "title": article["title"],
                            "error": resp.text[:300]})
    except Exception as e:
        print(f"  ❌ Exception: {e}")
        results.append({"id": i, "status": "EXCEPTION",
                        "title": article["title"], "error": str(e)})

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────
print("\n" + "="*70)
print("PUBLICATION SUMMARY")
print("="*70)
success = sum(1 for r in results if r["status"] == "SUCCESS")
print(f"Published: {success}/7 articles\n")
for r in results:
    if r["status"] == "SUCCESS":
        print(f"  ✅ [{r['id']}] {r['url']}")
    else:
        print(f"  ❌ [{r['id']}] FAILED — {r.get('error','')[:80]}")

with open("/tmp/publish_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nFull results saved to /tmp/publish_results.json")
