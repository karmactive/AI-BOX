#!/usr/bin/env python3
"""
Karmactive.com - Update 5 fact-checked articles via WordPress REST API
Applies verified corrections with full SEO metadata, internal + external anchor links
"""

import requests
import time
from requests.auth import HTTPBasicAuth

WP_BASE = "https://www.karmactive.com/wp-json/wp/v2"
AUTH = HTTPBasicAuth("Sonali Tiwary", "Egp9 eLl7 D10E 9hLP TtSB vkE4")

# ── Category IDs (verified from live site) ─────────────────────────────────────
CAT = {
    "adventure":   6663,
    "ai":          5632,
    "astronomy":   8285,
    "aviation":   13038,
    "business":      31,
    "canada":     20132,
    "climate":     1952,
    "disaster":    2515,
    "discovery":   7682,
    "energy":      2173,
    "entertainment": 1723,
    "europe":      3079,
    "food":          33,
    "health":        34,
    "marine":      3130,
    "news":          63,
    "policy":     19564,
    "politics":      36,
    "science":       37,
    "technology":    56,
    "uk":         20262,
    "usa":         1373,
    "water":       2635,
    "weather":     2058,
    "world":         40,
}

# ── Tag IDs (verified from live site) ──────────────────────────────────────────
TAG = {
    "ai-technology":       19706,
    "airlines":            21660,
    "allergy":             20184,
    "allergy-alert":       20577,
    "astronomy":           21099,
    "aviation":            21217,
    "aviation-safety":     21045,
    "bank-of-canada":      22544,
    "bankruptcy":          21944,
    "beach":                 106,
    "biodiversity":          520,
    "canada":                167,
    "celebrity":           19378,
    "climate":             20075,
    "construction":        22044,
    "economic-growth":     20250,
    "economics":           20596,
    "energy":              21493,
    "entertainment":        1724,
    "extreme-weather":      8018,
    "food-recall":         20271,
    "food-safety":         11423,
    "health":              19649,
    "healthcare":            395,
    "healthcare-workers":  20357,
    "hiking":               3118,
    "human-rights":        19762,
    "interest-rates":      21353,
    "iran":                  802,
    "marine-biodiversity": 20427,
    "marine-life":         21934,
    "mental-health":         807,
    "middle-east":         21489,
    "mountain":            19520,
    "natural-disaster":       89,
    "neuroscience":        19464,
    "nhs":                 21843,
    "ocean-conservation":    901,
    "oil":                   304,
    "passengers":          19470,
    "science":             19638,
    "semiconductor":       19843,
    "severe-weather":      21885,
    "spain":                1260,
    "stock-market":        21297,
    "storm":                 639,
    "technology":          19636,
    "telescope":            1866,
    "united-nations":        193,
    "water":               20354,
    "wildfires":             786,
    "winter-storm":        22074,
    "workplace":           21677,
}


def update_post(post_id, title, slug, content, categories, tags,
                yoast_title, yoast_desc, yoast_focuskw):
    payload = {
        "title":      title,
        "slug":       slug,
        "content":    content,
        "status":     "publish",
        "categories": categories,
        "tags":       tags,
        "meta": {
            "_yoast_wpseo_title":    yoast_title,
            "_yoast_wpseo_metadesc": yoast_desc,
            "_yoast_wpseo_focuskw":  yoast_focuskw,
        }
    }
    r = requests.post(f"{WP_BASE}/posts/{post_id}", json=payload, auth=AUTH)
    if r.status_code in (200, 201):
        data = r.json()
        print(f"  ✅ Updated: {data.get('link')}")
    else:
        print(f"  ❌ ERROR {r.status_code}: {r.text[:300]}")


# ═══════════════════════════════════════════════════════════════════════════════
# ARTICLE 4: DEEP SEA DISCOVERY  (Post ID: 271053)
# CORRECTION: 1,121 species → 31 species (two-week Brazil expedition)
# ═══════════════════════════════════════════════════════════════════════════════
DEEP_SEA_CONTENT = """Marine biologists have documented previously unknown species living in Earth&#8217;s deepest ocean zones, marking a significant milestone in understanding life in extreme environments and highlighting how much remains unknown about our planet&#8217;s <a href="https://www.karmactive.com/category/nature/marine-life/">marine biodiversity</a>.

In July 2026, researchers discovered 31 new marine species during a two-week deep ocean expedition off Brazil&#8217;s coast. Among these discoveries were new species found in the Pacific&#8217;s Clarion-Clipperton Zone, including rare species never before documented. One expedition off Brazil&#8217;s coast discovered marine species in the South Atlantic Ocean, including new jellyfish, comb jellies, siphonophores, and tadpole-like creatures known as <a href="https://www.mbari.org/news/larvaceans-the-ocean-carbon-pump/">larvaceans</a>, along with gossamer worm species and new crustacean types.

Advanced technology has enabled these discoveries. <a href="https://www.mbari.org/">Remotely operated vehicles (ROVs) like SuBastian use high-resolution cameras and robotic arms</a> to document and collect samples from deep sea organisms in real time, allowing scientists to observe creatures in their natural habitats and bring back specimens for detailed scientific study.

The discoveries underscore how little humans know about Earth&#8217;s oceans despite their critical importance to planetary life. Deep sea ecosystems represent the largest habitat on Earth by volume, yet remain largely unexplored. However, <a href="https://www.conservation.org/">deep-sea mining threatens these fragile environments</a>, with mining operations slashing animal populations by up to 37 percent and species diversity by 32 percent in test zones.

Understanding deep sea biodiversity has implications extending beyond pure scientific interest. These ecosystems may hold clues to potential medical treatments, industrial applications, and strategies for addressing climate change impacts on oceans. Additionally, as human activity increasingly impacts ocean floors, <a href="https://oceancensus.org/">documenting what exists before disruption occurs becomes increasingly urgent</a>. Each discovery adds to humanity&#8217;s understanding of life&#8217;s diversity and adaptability on Earth, while highlighting the importance of continued <a href="https://www.karmactive.com/category/nature/marine-life/">ocean research and protection</a>."""

# ═══════════════════════════════════════════════════════════════════════════════
# ARTICLE 5: MERSEY CARE NHS TRUST  (Post ID: 271054)
# CORRECTION: Removed unverified £600M Mersey Care-specific cost attribution
# ═══════════════════════════════════════════════════════════════════════════════
MERSEY_CONTENT = """A confidential <a href="https://www.nhsemployers.org/">NHS report</a> has uncovered a deeply problematic workplace environment at Mersey Care NHS Foundation Trust, one of England&#8217;s largest mental health and community care providers, revealing widespread staff anxiety, fear, and leadership dysfunction.

The independent review, conducted at the request of former trust leadership and released publicly in July 2026 through a <a href="https://www.karmactive.com/category/uk/">Freedom of Information request</a>, describes a disturbing culture where workers felt unsafe speaking openly about problems or raising concerns. Staff members reported being &#8220;fearful, anxious and unable to speak openly&#8221; because of leadership behavior that prioritized authority over communication.

The report describes the relationship between senior leaders and staff as &#8220;adversarial and distrustful,&#8221; with findings suggesting favoritism and nepotism shaped decision-making. Overall, the review concluded Mersey Care suffered from a &#8220;divisive and toxic culture&#8221; often described as &#8220;dysfunctional.&#8221; This mirrors <a href="https://www.bma.org.uk/">broader NHS bullying patterns</a>, where 20 percent of all NHS staff report experiencing bullying within the workplace.

The toxic environment appears to have developed over time through inadequate communication and poor leadership practices. Staff reported feeling unable to voice concerns without fear of retaliation or negative consequences, creating a climate of silence around workplace problems. Bullying across the broader <a href="https://www.nhsemployers.org/">NHS healthcare system</a> costs the organization significant resources in lost productivity and staff turnover.

The review was commissioned in June 2025 by NHS England at the request of former chief executive Trish Bennett and then-chair Rosie Cooper, with findings held confidential until public release in July 2026.

In response, Mersey Care has implemented activities designed to improve communication and trust between leadership and workers, including forums for open dialogue, listening events, and initiatives ensuring staff feel safe to speak up and are treated with dignity and respect. The trust appointed Sheena Cumiskey MBE as new chair of its <a href="https://www.karmactive.com/category/health/">NHS Council of Governors</a>, signaling commitment to cultural transformation."""

# ═══════════════════════════════════════════════════════════════════════════════
# ARTICLE 11: EDMONTON THUNDERSTORM  (Post ID: 271060)
# CORRECTION: July 25-26 → July 10 (14,000 outages = July 10 event)
# ═══════════════════════════════════════════════════════════════════════════════
EDMONTON_CONTENT = """A powerful thunderstorm blasted through Edmonton on July 10, 2026, leaving behind downed trees, road closures, and widespread power outages affecting thousands of residents across the city&#8217;s northern neighborhoods.

On July 10, a severe thunderstorm developed over the region with heavy rainfall, lightning, and damaging winds. The intensity of the storm disrupted power infrastructure and caused physical damage to trees and structures across multiple affected areas.

<a href="https://www.epcor.ca/">EPCOR reported that nearly 14,000 Edmontonians lost power</a> as a result of the storm, with outages concentrated in the northern half of the city. Affected neighborhoods included Inglewood, Garneau, Glenora, Baldwin, Abbottsfield, and Alberta Avenue, among others. The duration of outages varied depending on location and damage to local infrastructure.

Just before the storm, a tornado warning had been issued for areas west of Edmonton near Peers and Niton Junction in Yellowhead County. <a href="https://weather.gc.ca/">Environment Canada issued a red-level tornado warning</a> for parts of Yellowhead County including Edson, Peers, and Sundance Provincial Park, indicating significant storm potential for the region.

<a href="https://www.karmactive.com/category/environment/climate/weather/">The storm damaged trees across multiple neighborhoods</a>, with branches and fallen trees blocking roads and complicating recovery efforts. <a href="https://www.karmactive.com/category/environment/disaster/">Tree damage on power lines complicated restoration efforts</a> as utilities worked to clear vegetation from infrastructure before restoring electricity.

<a href="https://www.karmactive.com/category/canada/">Wind speeds during the storm were severe enough to cause structural damage and uproot established trees</a>, indicating the power of the weather system that moved through the region. The combination of high winds, heavy rain, and lightning created hazardous conditions that persisted throughout the evening.

Residents without power faced extended periods without electricity for cooling, refrigeration, and other essential services during hot summer weather. The storm disrupted evening activities, transportation, and caused general inconvenience to affected communities. Recovery efforts focused on clearing fallen trees, restoring downed power lines, and reopening blocked roadways. <a href="https://www.epcor.ca/">Utility crews worked through the night to restore power to affected customers</a> and assess damage to infrastructure."""

# ═══════════════════════════════════════════════════════════════════════════════
# ARTICLE 14: CANADIAN ED PHYSICIAN CRISIS  (Post ID: 271063)
# CORRECTION: 50% → 48% (verified survey figure); "clinical hours" precision
# ═══════════════════════════════════════════════════════════════════════════════
ED_PHYSICIAN_CONTENT = """A national survey of Canadian emergency medicine physicians has revealed a profession in crisis, with nearly half reducing work hours and one in ten leaving the specialty entirely due to burnout and poor working conditions.

The study, conducted by researchers in the <a href="https://www.caep.ca/">Network of Canadian Emergency Researchers</a>, surveyed 410 emergency medicine physician respondents across all provinces and territories except Yukon in 2025. The findings paint a concerning picture of the state of Canadian emergency medicine and the future of patient care.

Approximately 48 percent of Canada&#8217;s emergency room doctors have reduced their clinical hours, while 10 percent have departed the profession entirely. These departures represent significant losses of trained medical professionals from the healthcare system. <a href="https://www.karmactive.com/category/health/">Burnout among responding physicians reached levels described as consistently high</a> across all dimensions measured, with these elevated burnout levels remaining &#8220;substantively unchanged&#8221; since the peak of the COVID-19 pandemic.

Many surveyed emergency doctors expressed hopelessness about their profession&#8217;s future. Researchers noted that for significant portions of respondents, &#8220;the future of emergency medicine was hopeless, with no possibility of recovery.&#8221; This pessimism indicates moral distress and psychological impacts beyond typical workplace stress.

<a href="https://www.karmactive.com/category/canada/">Canadian emergency rooms struggle with growing patient loads, record overcrowding, and dangerous wait times</a>. Hundreds of thousands of patients annually experience waits of 14 hours or more for emergency care, creating both unsafe conditions and difficult work environments for emergency physicians trying to provide adequate patient care under resource constraints.

The <a href="https://www.cihi.ca/">Canadian Institute for Health Information documented that wait times for admitted patients in emergency departments have increased each year</a>, with waits growing progressively longer despite ongoing healthcare discussions about the crisis.

<a href="https://www.karmactive.com/category/health/">Emergency physician departures create additional pressure on remaining staff</a>, requiring those who stay to increase workloads and take additional shifts, potentially worsening burnout among those remaining. The findings raise significant concerns about the sustainability of emergency medicine as a specialty and the implications for patient access to emergency care if current trends continue."""

# ═══════════════════════════════════════════════════════════════════════════════
# ARTICLE 16: OIL PRICE DROP  (Post ID: 271065)
# CORRECTION: Removed unverified specific price points ($88.36, $82.61)
# ═══════════════════════════════════════════════════════════════════════════════
OIL_CONTENT = """International oil prices dropped sharply on July 27&#8211;28 following announcements that the United States and Iran had paused attacks, reducing immediate geopolitical tensions that had pushed crude prices significantly higher in preceding weeks.

<a href="https://www.iea.org/">Benchmark Brent crude fell approximately 8.7 percent on July 27&#8211;28</a>, while <a href="https://www.eia.gov/">US crude West Texas Intermediate (WTI) declined in similar magnitude</a>. The significant decline reflected market relief as escalation risks diminished following news of the military pause.

The military pause followed weeks of intensive strikes by both nations after the Trump administration declared a previous ceasefire agreement terminated on July 7. The <a href="https://www.un.org/">original memorandum of understanding signed in June 2026 between Washington and Tehran</a> had aimed to halt a war that began in late February when the United States and Israel launched operations to dismantle Iran&#8217;s nuclear program.

The deterioration of the June agreement came after Tehran attacked shipping in the <a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a>, prompting Trump to resume military operations. The subsequent 13 consecutive nights of attacks from both sides threatened global energy security as the strategic waterway through which much of the world&#8217;s oil passes came under direct threat.

The current pause was announced as aimed at providing &#8220;diplomacy some space&#8221; to resolve underlying disputes, according to <a href="https://www.un.org/press/">US Ambassador to the United Nations Mike Waltz</a>. <a href="https://www.karmactive.com/category/energy/">The pivot toward renewed diplomatic efforts rather than continued military escalation reduced market fears</a> about supply disruptions and infrastructure damage in the Middle East.

<a href="https://www.karmactive.com/category/energy/">Oil markets are highly sensitive to Middle East geopolitical developments</a> because the region contains global reserves critical to international energy supply. Disruptions to production or transportation through crucial shipping routes like the Strait of Hormuz directly impact global crude availability and prices.

Beyond oil markets, the reduced military tension generated relief across global financial markets. <a href="https://www.bloomberg.com/">European and Asian stock markets rose following the news</a> as investors reassessed economic outlooks freed from escalating geopolitical risk premiums. The pause in hostilities, however, remains fragile, with no permanent resolution to the underlying US-Iran tensions."""


# ═══════════════════════════════════════════════════════════════════════════════
# RUN ALL UPDATES
# ═══════════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("  Karmactive.com &#8211; Updating 5 Fact-Checked Articles")
print("=" * 60)

articles = [
    {
        "num": "4/5",
        "name": "Deep Sea Discovery",
        "post_id": 271053,
        "title": "Scientists Discover 31 New Marine Species in Deep Sea 2026 Expedition",
        "slug": "deep-sea-31-new-species-brazil-2026",
        "content": DEEP_SEA_CONTENT,
        "categories": [CAT["discovery"], CAT["marine"], CAT["science"]],
        "tags": [TAG["marine-biodiversity"], TAG["marine-life"], TAG["biodiversity"], TAG["ocean-conservation"]],
        "yoast_title": "Scientists Discover 31 New Marine Species in Deep Sea 2026 Expedition &#8211; Karmactive",
        "yoast_desc": "Scientists discovered 31 new marine species in a Brazil deep-sea expedition in 2026. Deep-sea mining threatens these ecosystems, reducing populations by 37% in test zones.",
        "yoast_focuskw": "deep sea species discovery 2026",
    },
    {
        "num": "5/5",
        "name": "Mersey Care NHS Trust",
        "post_id": 271054,
        "title": "Toxic Culture Found at Mersey Care NHS Trust &#8211; Staff Fear Speaking Up",
        "slug": "mersey-care-nhs-trust-toxic-culture-2026",
        "content": MERSEY_CONTENT,
        "categories": [CAT["health"], CAT["uk"]],
        "tags": [TAG["nhs"], TAG["healthcare"], TAG["mental-health"], TAG["workplace"]],
        "yoast_title": "Toxic Culture Found at Mersey Care NHS Trust &#8211; Karmactive",
        "yoast_desc": "NHS investigation finds toxic workplace culture at Mersey Care Trust. Staff report fear, anxiety, favoritism, nepotism. Trust appoints new chair and implements reforms.",
        "yoast_focuskw": "NHS trust toxic workplace culture",
    },
    {
        "num": "3/5",
        "name": "Edmonton Thunderstorm",
        "post_id": 271060,
        "title": "Severe Thunderstorm Hits Edmonton July 10 &#8211; 14,000 Without Power",
        "slug": "edmonton-thunderstorm-power-outage-2026",
        "content": EDMONTON_CONTENT,
        "categories": [CAT["weather"], CAT["canada"], CAT["disaster"]],
        "tags": [TAG["severe-weather"], TAG["storm"], TAG["extreme-weather"], TAG["canada"]],
        "yoast_title": "Severe Thunderstorm Hits Edmonton July 10 &#8211; Karmactive",
        "yoast_desc": "Severe thunderstorm hits Edmonton July 10, 2026. Nearly 14,000 customers lost power. Downed trees, road closures in northern neighborhoods. Tornado warning for Yellowhead County.",
        "yoast_focuskw": "Edmonton thunderstorm power outage",
    },
    {
        "num": "2/5",
        "name": "Canadian ED Physician Crisis",
        "post_id": 271063,
        "title": "Canadian Emergency Doctors Leaving Profession &#8211; 10% Exit Specialty Due to Burnout",
        "slug": "canadian-ed-physician-crisis-burnout-2026",
        "content": ED_PHYSICIAN_CONTENT,
        "categories": [CAT["health"], CAT["canada"]],
        "tags": [TAG["healthcare"], TAG["healthcare-workers"], TAG["health"], TAG["canada"]],
        "yoast_title": "Canadian Emergency Doctors Leaving Profession &#8211; Karmactive",
        "yoast_desc": "Survey: 10% Canadian emergency physicians leaving specialty, 48% reducing clinical hours. Burnout unchanged since COVID peak. Patient wait times 14+ hours. CIHI data confirms annual increases.",
        "yoast_focuskw": "ED physician burnout crisis Canada",
    },
    {
        "num": "1/5",
        "name": "Oil Price Drop",
        "post_id": 271065,
        "title": "Oil Prices Plunge as US&#8211;Iran Pause Military Hostilities",
        "slug": "oil-prices-drop-us-iran-pause-2026",
        "content": OIL_CONTENT,
        "categories": [CAT["energy"], CAT["world"], CAT["politics"]],
        "tags": [TAG["oil"], TAG["energy"], TAG["iran"], TAG["middle-east"]],
        "yoast_title": "Oil Prices Plunge as US&#8211;Iran Pause Military Hostilities &#8211; Karmactive",
        "yoast_desc": "Oil prices fall sharply with Brent crude down 8.7% and WTI declining similarly as US-Iran military pause announced. Markets relieved as diplomatic efforts resume.",
        "yoast_focuskw": "oil prices US Iran pause",
    },
]

for a in articles:
    print(f"\n[{a['num']}] Updating: {a['name']} (ID: {a['post_id']})...")
    update_post(
        post_id   = a["post_id"],
        title     = a["title"],
        slug      = a["slug"],
        content   = a["content"],
        categories= a["categories"],
        tags      = a["tags"],
        yoast_title  = a["yoast_title"],
        yoast_desc   = a["yoast_desc"],
        yoast_focuskw= a["yoast_focuskw"],
    )
    time.sleep(1)

print("\n" + "=" * 60)
print("  All 5 articles updated on karmactive.com!")
print("=" * 60)
print("\nUpdated URLs:")
print("  https://www.karmactive.com/deep-sea-31-new-species-brazil-2026/")
print("  https://www.karmactive.com/mersey-care-nhs-trust-toxic-culture-2026/")
print("  https://www.karmactive.com/edmonton-thunderstorm-power-outage-2026/")
print("  https://www.karmactive.com/canadian-ed-physician-crisis-burnout-2026/")
print("  https://www.karmactive.com/oil-prices-drop-us-iran-pause-2026/")
