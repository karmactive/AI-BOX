import requests, json, sys

BASE_URL = "https://www.karmactive.com/wp-json/wp/v2"
AUTH = ("Karmactive Staff", "Z7fx zXV3 AeLb JC1Q Hid4 NmuF")

def publish_post(title, content, slug, categories, tags, excerpt, focus_kp):
    data = {
        "title": title,
        "content": content,
        "status": "publish",
        "slug": slug,
        "categories": categories,
        "tags": tags,
        "excerpt": excerpt,
    }
    resp = requests.post(f"{BASE_URL}/posts", auth=AUTH, json=data, timeout=60)
    if resp.status_code == 201:
        post = resp.json()
        print(f"  PUBLISHED: {post['link']}")
        return post
    else:
        print(f"  FAILED ({resp.status_code}): {resp.text[:400]}")
        return None

# ── ARTICLE 1: Social Security Email ──────────────────────────────────────────
print("\n[1/4] Publishing Social Security article...")
r1 = publish_post(
  title="SSA Commissioner's Email Claimed $7,500 in Senior Relief — Five Senators Call It Misleading",
  slug="social-security-bisignano-email-trump-misleading-seniors",
  categories=[63, 36, 1373],
  tags=[22046, 21073, 1104, 20276, 22035],
  excerpt="Social Security Commissioner Frank Bisignano emailed seniors crediting Trump with $7,500 in relief. Five Democratic senators say the claim was misleading and demand answers by August 11.",
  focus_kp="Social Security misleading email seniors",
  content="""<p>Social Security Commissioner Frank Bisignano sent an email to tens of millions of benefit recipients on July 2, 2026. The subject line read: &#8220;Making Life More Affordable for America&#8217;s Seniors.&#8221; The message repeatedly credited President Trump and his recent legislation. Now, five Democratic senators are demanding answers about whether that email was accurate.</p>

<p>The email referenced President Trump six times. It claimed &#8220;over 35 million American seniors received an average of $7,500 in relief this tax season.&#8221; It attributed this to the <a href="https://www.congress.gov/bill/119th-congress/house-bill/1" target="_blank" rel="noopener noreferrer">One Big Beautiful Bill Act</a> &#8212; known as the OBBBA &#8212; which Trump signed into law.</p>

<p>But what the OBBBA actually created is more limited than those words suggest.</p>

<p>The law established a $6,000 <a href="https://www.irs.gov/taxtopics/tc551" target="_blank" rel="noopener noreferrer">tax deduction</a> for Americans aged 65 and older. A deduction is not a payment. It is not a refund. A deduction reduces how much of a person&#8217;s income is subject to federal tax. A senior earning $40,000, for example, could lower their taxable income to $34,000. The actual dollar savings depend on the person&#8217;s tax bracket and overall situation. For many seniors with modest incomes who already owe little or no federal income tax, the benefit could be minimal &#8212; or nothing at all.</p>

<p>Critics also note that the OBBBA did not reduce or eliminate federal taxes on Social Security benefits themselves. That is a separate issue many seniors care about deeply. <a href="https://www.karmactive.com/medicare-part-b-premiums-jump-5-9-to-185-in-2025-can-a-50-social-security-boost-keep-up/">Taxing Social Security income has long been a point of contention</a>, with Medicare costs compounding the squeeze for many households. The OBBBA did not address it.</p>

<p>Senators Elizabeth Warren (MA), Ron Wyden (OR), Tammy Baldwin (WI), Sheldon Whitehouse (RI), and Ben Ray Luj&#225;n (NM) sent a <a href="https://www.warren.senate.gov/newsroom/press-releases/warren-wyden-baldwin-colleagues-press-bisignano-on-misleading-partisan-email-sent-to-social-security-beneficiaries" target="_blank" rel="noopener noreferrer">formal letter to Bisignano</a>. They said the email contained &#8220;misleading information&#8221; and questioned why an official government agency communication named the president six times. The letter also asks Bisignano to clarify what data was used to reach the $7,500 figure. They set a deadline of August 11, 2026, for a response.</p>

<p><a href="https://www.karmactive.com/medicare-part-b-premiums-jump-5-9-to-185-in-2025-can-a-50-social-security-boost-keep-up/">Social Security recipients have been under growing financial pressure</a>, facing rising Medicare premiums and cost-of-living challenges in recent years. An email from the <a href="https://www.ssa.gov" target="_blank" rel="noopener noreferrer">SSA</a> promising $7,500 in relief could easily be read as a direct payment &#8212; not a tax deduction that applies very differently depending on each person&#8217;s income and tax situation.</p>

<p>The broader concern is about the role of a federal agency in political messaging. <a href="https://www.karmactive.com/fluoride-in-u-s-water-trump-and-kennedys-2024-push-could-affect-209-million-americans/">Government agencies communicate with hundreds of millions of Americans</a>, and the framing of those communications carries real weight. When an official SSA notice reads more like a political talking point than a factual explanation of a benefit, critics argue it erodes public trust in the agency.</p>

<p>Bisignano has not publicly responded to the senators&#8217; letter. His office has until August 11 to reply.</p>

<p>The dispute ultimately centers on a simple factual question: did the OBBBA give seniors $7,500 in relief? The evidence says no &#8212; not in any direct or universal sense. It created a deduction that may help some and offer little to others. The email did not explain that difference, according to the senators.</p>"""
)

# ── ARTICLE 2: William Shatner ─────────────────────────────────────────────────
print("\n[2/4] Publishing William Shatner article...")
r2 = publish_post(
  title="William Shatner and Daughter Melanie Both Beat Stage 4 Cancer &#8212; Now They&#8217;re Telling Their Story",
  slug="william-shatner-daughter-melanie-stage-4-cancer-battle-2026",
  categories=[34, 63, 1723],
  tags=[1288, 19378, 22039, 20765, 20767],
  excerpt="William Shatner and his daughter Melanie Shatner Gretsch both faced Stage 4 cancer diagnoses within a year of each other. By late 2024, both were declared cancer-free.",
  focus_kp="William Shatner Stage 4 cancer daughter",
  content="""<p>William Shatner is 95. His daughter Melanie is 61. In the span of just over a year, both were diagnosed with Stage 4 cancer. Both came out the other side.</p>

<p>Melanie Shatner Gretsch found a lump in July 2022. Her diagnosis was HER2-positive Stage 4 <a href="https://www.karmactive.com/breast-cancer-rates-up-1-yearly-with-sharpest-rises-among-women-under-50-and-aapi-women-black-women-38-more-likely-to-die-despite-lower-incidence/">breast cancer</a>. HER2-positive means the cancer cells carry too much of a protein called HER2, which makes the cancer grow faster and more aggressively than other types. Breast cancer rates have been rising steadily, and HER2-positive cases are among the hardest to treat.</p>

<p>Melanie went through multiple rounds of chemotherapy, 30 radiation treatments, and a double mastectomy. That is a brutal sequence by any measure.</p>

<p>Then, in June 2023, her father was diagnosed with Stage 4 malignant <a href="https://www.aad.org/public/diseases/skin-cancer/types/common/melanoma" target="_blank" rel="noopener noreferrer">melanoma</a>. Melanoma is a skin cancer that, when it reaches Stage 4, has spread to other organs. In Shatner&#8217;s case, it had reached his lungs and brain. A visible lump on his cheek was what first drew attention. Surgeons removed a tumor from his face. He then spent two years on <a href="https://www.cancer.gov/about-cancer/treatment/types/immunotherapy" target="_blank" rel="noopener noreferrer">immunotherapy</a> &#8212; a treatment that activates the body&#8217;s own immune system to find and attack cancer cells.</p>

<p>Shatner did not go public with the diagnosis right away. He first talked about it in March 2024 at the American Academy of Dermatology&#8217;s annual meeting in San Diego.</p>

<p>Melanie said in a recent People magazine interview: &#8220;I remember vividly thinking, &#8216;I don&#8217;t have the strength to take care of myself and lose my father at the same time.&#8217;&#8221; That line carries the full weight of what this family went through. Two people she loves most &#8212; herself and her father &#8212; both in the fight at the same time.</p>

<p>By late 2024, both had been declared cancer-free. No evidence of disease.</p>

<p>Advances in <a href="https://www.karmactive.com/the-dawn-of-a-new-era-in-cancer-treatment-the-story-of-aoh1996/">cancer treatment</a> have changed what &#8220;Stage 4&#8221; can mean. Immunotherapy in particular has shifted outcomes for <a href="https://www.cancer.gov/about-cancer/treatment/types/immunotherapy" target="_blank" rel="noopener noreferrer">melanoma patients</a> in ways that were not possible a decade ago. Shatner&#8217;s two-year immunotherapy run is part of that story.</p>

<p>Now the two are sharing what they went through. In July 2026, they appeared on the cover of People magazine. They are also launching a podcast called &#8220;No Time but Now,&#8221; where they plan to talk about their experience facing cancer together.</p>

<p>Shatner has spoken openly for years about mortality. At 95, after two years of cancer treatment, he is still here. So is his daughter.</p>

<p>Sometimes the story is just that simple.</p>"""
)

# ── ARTICLE 3: Glacier Bear Attack ────────────────────────────────────────────
print("\n[3/4] Publishing Glacier bear attack article...")
r3 = publish_post(
  title="Glacier National Park Grizzly Bear Attack Kills Hiker in First Fatal Encounter Since 1998",
  slug="glacier-national-park-fatal-grizzly-bear-attack-2026-anthony-pollio",
  categories=[63, 2756, 1373],
  tags=[256, 21713, 666, 3118, 393],
  excerpt="A grizzly bear killed Anthony Pollio, 33, on a night hike at Glacier National Park in May 2026 — the park's first fatal bear attack in 28 years. What investigators found.",
  focus_kp="Glacier National Park grizzly bear attack",
  content="""<p>A grizzly bear killed a Florida man hiking alone at Glacier National Park on the night of May 3, 2026, in what became the park&#8217;s first fatal bear attack in 28 years.</p>

<p>Anthony Pollio, 33, of Davie, Florida, was hiking the Mount Brown Lookout Trail on the park&#8217;s west side. He was midway through a cross-country road trip. When he did not return to camp, he was reported missing on May 4. Park rangers launched a search using helicopters and infrared equipment over the following days.</p>

<p>On May 6, searchers found an empty GrizGuard bear spray canister in the brush beside the trail. Farther in, approximately 2.5 miles from the trailhead and 69 feet down a steep, wooded slope, they found Pollio&#8217;s remains.</p>

<p><strong>What the Investigation Found</strong></p>

<p>A board of review reconstructed the encounter using physical evidence: claw marks on a burned tree, a displaced stone, and the location of the spray canister. The evidence indicates the attack most likely occurred between approximately 11:15 p.m. and midnight. Pollio was hiking in near-darkness.</p>

<p>Investigators believe neither Pollio nor the bear detected each other until they were very close. The bear moved rapidly from behind fallen trees toward the trail. Pollio discharged the entire <a href="https://www.nps.gov/articles/bear-spray.htm" target="_blank" rel="noopener noreferrer">bear spray canister</a> during the initial assault. Whether the spray reached the bear could not be confirmed. After the attack, Pollio tumbled down the slope.</p>

<p>The <a href="https://www.nps.gov/glac/learn/news/grizzly-bear-death-in-park.htm" target="_blank" rel="noopener noreferrer">board of review report</a> was nearly complete as of July 16, 2026.</p>

<p>This was the tenth fatal bear encounter in <a href="https://www.karmactive.com/journey-through-northwestern-eden-an-insightful-travel-guide-to-glacier-national-park/">Glacier National Park</a> since 1967. The previous fatal attack occurred in 1998. Less than a month after Pollio&#8217;s death, a second bear attack &#8212; non-fatal &#8212; occurred in the park.</p>

<p><strong>Bear Spray Works &#8212; When You Can Use It</strong></p>

<p><a href="https://www.karmactive.com/court-ruling-saves-grizzly-bears-from-lethal-threat-at-yellowstone-in-defense-of-the-iconic/">Grizzly bears</a> are protected under federal law and are an established presence throughout the northern Rockies. Studies consistently show <a href="https://www.nps.gov/articles/bear-spray.htm" target="_blank" rel="noopener noreferrer">bear spray</a> reduces injury during encounters more effectively than firearms in many situations &#8212; but it has to reach the bear to work, and it requires time to deploy.</p>

<p>That is why timing and awareness matter. As <a href="https://www.karmactive.com/tourists-unsettling-behavior-provokes-wildlife-crisis-in-national-parks-beyond-selfies/">wildlife safety experts have repeatedly emphasized</a>, surprises are the most dangerous scenario in bear country.</p>

<p>Basic precautions that reduce risk:</p>
<ul>
<li>Hike during daylight hours, especially on forested, low-visibility trails</li>
<li>Make consistent noise &#8212; talk, clap, call out &#8212; to avoid startling bears</li>
<li>Carry bear spray in an accessible holster, not buried in a pack</li>
<li>Hike in groups when possible</li>
<li>Check trail conditions and recent <a href="https://www.nps.gov/glac/planyourvisit/bears.htm" target="_blank" rel="noopener noreferrer">wildlife activity reports</a> at the trailhead</li>
</ul>

<p><a href="https://www.karmactive.com/bear-break-ins-to-harmony-the-lake-tahoe-bear-drama-and-quest-for-coexistence/">Bear encounters</a> are uncommon, but the risk is real, particularly in dense terrain and low light. Evidence suggests Pollio had his bear spray and attempted to use it. The encounter, by all indications, happened too fast and too close to allow the spray to work as intended.</p>

<p>Glacier National Park remained open following the attack. Park officials reminded visitors to carry bear spray, make noise on the trail, and avoid hiking alone after dark.</p>"""
)

# ── ARTICLE 4: Shiloh Archaeology ─────────────────────────────────────────────
print("\n[4/4] Publishing Shiloh archaeology article...")
r4 = publish_post(
  title="Archaeologists Uncover Possible Tabernacle Site at Ancient Shiloh, Along With Priestly Artifacts",
  slug="ancient-shiloh-excavation-ark-covenant-tabernacle-finds-2026",
  categories=[3809, 7682, 4949],
  tags=[22559, 1182, 20718, 136, 22518],
  excerpt="Excavators at Tel Shiloh in Israel uncovered a monumental Iron Age structure matching the biblical Tabernacle's proportions, along with altar horns, murex shells, and priestly artifacts.",
  focus_kp="Shiloh Ark of Covenant excavation 2026",
  content="""<p>Archaeologists excavating the ancient site of Shiloh in Israel have uncovered the southern wall of a large monumental structure that may be connected to one of the most storied locations in the Bible &#8212; the place where the Ark of the Covenant was once kept.</p>

<p>The <a href="https://biblearchaeology.org/the-shiloh-excavation/" target="_blank" rel="noopener noreferrer">Associates for Biblical Research (ABR)</a> wrapped up their eighth season of excavations at Tel Shiloh in June 2026. The results are drawing attention from scholars and historians around the world.</p>

<p><strong>What Did They Find?</strong></p>

<p>The centerpiece of this season&#8217;s dig is the southern wall of a substantial Iron Age I building. Its east-west orientation and overall proportions closely match the biblical description of the <a href="https://www.karmactive.com/category/science/archaeology/">Tabernacle</a> &#8212; the portable sanctuary that, according to scripture, once housed the Ark of the Covenant.</p>

<p>For readers unfamiliar with it, the Ark of the Covenant was a sacred chest described in the Hebrew Bible as containing the stone tablets of the Ten Commandments. It was among the most revered objects in ancient Israelite religion. Shiloh is described in the Bible as the place where it rested for generations before being captured and later lost to history. The Ark itself has not been found.</p>

<p>The artifacts discovered in and around the monumental structure add to the picture. Researchers uncovered <a href="https://www.jpost.com/archaeology/article-863638" target="_blank" rel="noopener noreferrer">altar horns</a> &#8212; objects used in ancient Israelite religious worship &#8212; along with ceramic pomegranates, which were symbolic priestly items. They also found murex shells. These sea snails were used in antiquity to produce a rare, expensive blue-purple dye called tekhelet, which the Hebrew Bible associates with the garments worn by priests. The presence of these shells at this specific location is considered significant by the excavation team.</p>

<p>Three large Canaanite storage jars were also found, still containing charred remains of olives, wheat, and lentils &#8212; a snapshot of daily life preserved for roughly 3,000 years.</p>

<p><strong>Three Dig Areas, One Complex Story</strong></p>

<p>The excavation covers three distinct zones. One focuses on the site&#8217;s gate complex. Another centers on the monumental structure described above. The third is Area D, home to what archaeologists call a favissa &#8212; essentially a ritual disposal pit where sacred objects were buried when they were no longer in use. Priests in the ancient world could not simply throw away holy items, so they buried them ceremonially instead.</p>

<p>Separately, excavators also uncovered additional walls from Shiloh&#8217;s northern fortification system, along with artifacts from the Second Temple period &#8212; roughly 516 BC to 70 AD. These later finds come from a different part of the site and represent a distinct phase of Shiloh&#8217;s long history. <a href="https://www.karmactive.com/lightning-strikes-gold-the-discovery-of-a-never-before-seen-phosphorus-mineral-in-florida/">Like other landmark discoveries</a>, they remind us how much history remains buried underfoot.</p>

<p><strong>A Site With Deep Roots</strong></p>

<p>Shiloh has a layered past. It was first established around <a href="https://cris.tau.ac.il/en/publications/shiloh-the-archaeology-of-a-biblical-site/" target="_blank" rel="noopener noreferrer">1700 BC during the Middle Bronze II period</a>, expanded around 1600 BC, and was continuously occupied until roughly 1070 BC. It was later rebuilt during Iron Age II, between 980 and 587 BC. The site sits in the West Bank region of modern-day Israel.</p>

<p>No one is claiming the Tabernacle has been definitively identified. The evidence is suggestive, not conclusive. But for a site already rich in history, each new season adds another piece to a puzzle that has fascinated researchers for generations. <a href="https://www.karmactive.com/the-perseverance-rover-epic-discoveries-ancient-rivers-and-clues-to-extraterrestrial-life/">Exploration &#8212; whether on Earth or beyond &#8212; keeps rewriting what we know.</a></p>"""
)

print("\n\n=== FINAL SUMMARY ===")
for i, r in enumerate([r1, r2, r3, r4], 1):
    if r:
        print(f"Article {i}: PUBLISHED -> {r['link']}")
    else:
        print(f"Article {i}: FAILED")
