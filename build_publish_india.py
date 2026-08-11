#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_publish_india.py — Publishes 8 India articles to karmactive.com via REST API
Uses credentials from environment (not hardcoded in files)
10-30 min random gaps, starting 1 hour ago
"""
import sys, re, json, subprocess, base64, time, random, datetime, html, os

W = "https://www.karmactive.com"

# Credentials — read from environment, NOT hardcoded in script
WP_USER = os.environ.get("WP_USER", "Karmactive Staff")
WP_PASS = os.environ.get("WP_PASS", "")
if not WP_PASS:
    print("ERROR: WP_PASS environment variable not set.")
    print("Usage: WP_PASS='your-app-password' python3 build_publish_india.py [--dry]")
    sys.exit(1)

USERPASS = f"{WP_USER}:{WP_PASS}"
B64 = base64.b64encode(USERPASS.encode()).decode()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# Category IDs from sitemap
CAT = {
    "aviation": 13038, "india": 115, "disaster": 2515,
    "health": 34, "latest": 1, "politics": 36,
    "business": 31, "policy": 19564,
    "environment": 16921, "wildlife": 2756,
    "technology": 56, "news": 63,
}

# Tag IDs from sitemap (verified against tags.json)
TAG = {
    "safety": 245, "public-health": 9693, "disease": 402, "health": 19649,
    "health-alert": 14497, "health-risks": 8814, "healthcare": 395,
    "policy": 7520, "government": 1104,
    "technology": 19636, "innovation": 4091,
    "wildlife-conservation": 9317, "biodiversity": 520, "birds": 232,
    "environment": 75, "environmental-conservation": 8415,
    "india": 19654, "natural-disaster": 89, "research": 619,
    "study": 4101, "emergency-response": 9570,
}

# Author IDs (from skill_wp.md)
AUTH = {
    "sunita": 57,       # Sunita Somvanshi
    "sonali": 224,      # Sonali Tiwary
    "govind": 3,        # Govind Tekale
    "rahul": 4,         # Rahul Somvanshi
    "karmactive-staff": 59,
    "karmactive-team": 1,
}

# Article metadata (titles, meta, focus, slug, author, cats, tags)
ARTS = [
    dict(
        title="Air India A320neo Triple Hydraulic Failure Leaves 17 Injured as DGCA Launches Serious Incident Probe",
        meta="Air India flight VT-EXO suffered triple hydraulic failure mid-cruise, injuring 17. DGCA launches Serious Incident probe with Airbus and BEA assistance.",
        focus="air india hydraulic failure",
        slug="air-india-a320neo-hydraulic-failure",
        author=AUTH["sonali"],
        cats=["aviation", "india", "disaster"],
        tags=["safety", "public-health", "disease"],
    ),
    dict(
        title="Delhi H1N1 Cases Jump 600% This Season—Monsoon Weather and H3N2 Co-Circulation Drive Surge",
        meta="Delhi records 1,344 H1N1 cases this season vs 229 last year. AIIMS confirms H3N2 co-circulating. Monsoon weather blamed for viral amplification.",
        focus="delhi h1n1 flu surge",
        slug="delhi-h1n1-flu-surge",
        author=AUTH["sunita"],
        cats=["health", "india", "latest"],
        tags=["disease", "public-health", "health", "health-alert"],
    ),
    dict(
        title="Allahabad HC Orders Release of Two Women Confined Since 2021 Over Religious Conversion—₹25 Lakh Compensation",
        meta="Allahabad HC orders release of two women confined since 2021 after Hindu-to-Islam conversion. Court awards ₹25 lakh, citing constitutional rights violations.",
        focus="allahabad hc conversion ruling",
        slug="allahabad-hc-religious-conversion-compensation",
        author=AUTH["govind"],
        cats=["india", "latest", "politics"],
        tags=["india", "policy", "government"],
    ),
    dict(
        title="Parliamentary Committee Demands Zuckerberg Apology After Modi Post Removal—Threatens Section 79",
        meta="India's Parliamentary Committee demands Mark Zuckerberg apologize for PM Modi's Facebook post removal. Threatens Section 79 safe harbor withdrawal.",
        focus="meta zuckerberg apology india",
        slug="meta-zuckerberg-apology-pm-modi-post",
        author=AUTH["govind"],
        cats=["india", "latest", "technology", "policy"],
        tags=["technology", "policy", "government"],
    ),
    dict(
        title="Jharkhand Students Demand JPSC Exam Probe After Alleged Irregularities—Police Hospitalize Protest Leader",
        meta="Jharkhand students demand CBI probe into JPSC irregularities. Police lathi-charge hospitalizes hunger striker Devendra Nath Mahto after 9-day fast.",
        focus="jharkhand student protest exam",
        slug="jharkhand-student-protests-recruitment-exam",
        author=AUTH["govind"],
        cats=["india", "latest", "politics"],
        tags=["india", "policy", "government"],
    ),
    dict(
        title="Parliament Passes UPI Tax Amendment Bill—Opposition Walkout Over US-India Data Sharing Concerns",
        meta="Parliament passes UPI taxation amendment. FM Sitharaman says UPI remains free for consumers as opposition CPI(M) and AAP walk out over US-India data sharing.",
        focus="upi transaction tax india",
        slug="upi-free-consumers-sitharaman-rajya-sabha",
        author=AUTH["sunita"],
        cats=["india", "business", "latest", "policy"],
        tags=["policy", "government", "technology"],
    ),
    dict(
        title="Rapper Santy Sharma Gets Death Threats Over Reservation Reform Campaign—YouTube Channel Permanently Deleted",
        meta="Rapper Santy Sharma receives death threats after launching reservation reform campaign. His 11-year YouTube channel was permanently deleted without explanation.",
        focus="santy sharma death threats",
        slug="santy-sharma-death-threats-reservation-reform",
        author=AUTH["govind"],
        cats=["india", "latest", "news"],
        tags=["india", "policy"],
    ),
    dict(
        title="India Donates Five Peacocks to UN Geneva—Reviving 45-Year Tradition from 1981 Indira Gandhi Gift",
        meta="India donates 5 peacocks (4 blue, 1 white) to UN Geneva's Ariana Park, reviving Indira Gandhi's 1981 tradition. Ambassador Arindam Bagchi presents birds.",
        focus="india peacocks un geneva",
        slug="india-donates-peacocks-un-geneva",
        author=AUTH["govind"],
        cats=["india", "environment", "wildlife"],
        tags=["wildlife-conservation", "biodiversity", "birds", "india"],
    ),
]

def api(method, path, data=None, ctx=False, retries=5):
    args = ["curl", "-s", "--retry", "5", "--retry-delay", "2", "--connect-timeout", "20", "--max-time", "90",
            "-A", UA, "-H", "Authorization: Basic " + B64, "-X", method]
    if data is not None:
        args += ["-H", "Content-Type: application/json", "--data", json.dumps(data, ensure_ascii=False)]
    url = W + "/wp-json/wp/v2/" + path + ("?context=edit" if ctx else "")
    args.append(url)
    for attempt in range(retries):
        try:
            out = subprocess.run(args, capture_output=True, text=True, timeout=120)
            if out.returncode != 0:
                time.sleep(2); continue
            if not out.stdout.strip():
                time.sleep(2); continue
            return json.loads(out.stdout)
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(2)
    raise SystemExit("API FAIL %s %s" % (method, path))

def parse_markdown_articles(path):
    """Parse stage5_publish_ready_india.md and extract article bodies."""
    txt = open(path, encoding="utf-8").read()
    articles = []
    # Split by ## Article markers
    sections = re.split(r'## Article \d+(?:\+?\d*)\s*(?:\([^)]*\))?:', txt)
    # First section is preamble, skip it
    sections = sections[1:]  # skip preamble
    for i, s in enumerate(sections):
        if not s.strip():
            continue
        # Find the body: everything from the first <p> or text after metadata
        # The body starts after the last --- before the actual content
        # Look for the first paragraph
        body_match = re.search(r'### (.+?)(?:\n---+|\n## Article|\Z)', s, re.S)
        if body_match:
            body = body_match.group(1).strip()
            # Clean up — convert newlines to <p> tags
            paragraphs = body.split('\n\n')
            html_body = '<p><em>Estimated reading time: %d minute%s</em></p>\n\n' % (
                max(1, round(len(body.split()) / 200)),
                "" if len(body.split()) / 200 == 1 else "s"
            )
            for p in paragraphs:
                p = p.strip()
                if p.startswith('### '):
                    html_body += p.replace('### ', '<h3>') + '</h3>\n\n'
                elif p.startswith('<h3>'):
                    html_body += p + '\n\n'
                elif p.startswith('<footer>'):
                    html_body += p + '\n\n'
                elif p.startswith('</footer>'):
                    html_body += p + '\n\n'
                elif not p or p.startswith('|'):
                    continue
                elif p.startswith('---'):
                    continue
                else:
                    html_body += '<p>' + p + '</p>\n\n'
            articles.append(html_body)
        else:
            articles.append('<p>Content pending.</p>')
    return articles

def main():
    DRY = "--dry" in sys.argv
    src = r"C:\Users\Hp\OneDrive\karmactive-pipeline\stage5_publish_ready_india.md"
    parsed = parse_markdown_articles(src)
    print("Parsed %d articles from %s" % (len(parsed), src))
    results = []
    # start 1 hour ago
    start = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=1)
    cur = start
    for i, a in enumerate(parsed):
        meta = ARTS[i]
        body = a
        nlinks = body.count('href=')
        mlen = len(meta["meta"])
        if mlen > 200:
            cut = meta["meta"][:200].rsplit(" ", 1)[0]
            meta["meta"] = cut + "…"
            mlen = len(meta["meta"])
        cat_ids = [CAT[c] for c in meta["cats"]]
        tag_ids = []
        for t in meta["tags"]:
            if t in TAG:
                tag_ids.append(TAG[t])
        date_gmt = cur.strftime("%Y-%m-%dT%H:%M:%S")
        if i < len(parsed) - 1:
            cur += datetime.timedelta(minutes=random.randint(10, 30))
        row = dict(n=i+1, title=meta["title"], slug=meta["slug"], focus=meta["focus"],
                   meta=meta["meta"], metalen=mlen, author=meta["author"],
                   cats=meta["cats"], cat_ids=cat_ids, tags=meta["tags"], tag_ids=tag_ids,
                   wc=len(body.split()), nlinks=nlinks, date_gmt=date_gmt,
                   body_paras=body.count("<p"), body=body)
        results.append(row)
        print("ART%d | title=%s" % (i+1, meta["title"][:70]))
        print("   slug=%s | focus=%s | metalen=%d | author=%d" % (meta["slug"], meta["focus"], mlen, meta["author"]))
        print("   cats=%s (ids %s)" % (meta["cats"], cat_ids))
        print("   tags=%s (ids %s)" % (meta["tags"], tag_ids))
        print("   wc=%d paras=%d links=%d date_gmt=%s" % (row["wc"], row["body_paras"], nlinks, date_gmt))
        if nlinks < 3:
            raise SystemExit("TOO FEW LINKS art %d: %d" % (i+1, nlinks))
    if DRY:
        print("\nDRY RUN OK — no network writes.")
        write_deliverable(results, [(r, "DRY", "dry") for r in results], parsed)
        return
    # ---- PUBLISH ----
    pub = []
    for r in results:
        exist = api("GET", "posts?slug=%s&per_page=1&_fields=id,status&status=publish,future,draft" % r["slug"])
        if exist:
            print("SKIP (exists) art%d slug=%s id=%s" % (r["n"], r["slug"], exist[0]["id"]))
            pub.append((r, exist[0]["id"], exist[0].get("status")))
            continue
        payload = dict(title=r["title"], slug=r["slug"], content=r["body"],
                       categories=r["cat_ids"], tags=r["tag_ids"], author=r["author"],
                       status="publish", date_gmt=r["date_gmt"])
        resp = api("POST", "posts", payload)
        pid = resp["id"]
        time.sleep(3)
        meta_payload = dict(meta={
            "_yoast_wpseo_metadesc": r["meta"],
            "_yoast_wpseo_focuskw": r["focus"],
            "_yoast_wpseo_title": r["title"],
        })
        api("PUT", "posts/%d" % pid, meta_payload, ctx=True)
        time.sleep(3)
        print("PUBLISHED art%d -> id=%s status=%s url=%s" % (r["n"], pid, resp.get("status"), resp.get("link")))
        pub.append((r, pid, resp.get("status")))
    # ---- AUDIT ----
    print("\n==== POST-PUBLISH AUDIT ====")
    for r, pid, st in pub:
        if isinstance(pid, int):
            chk = api("GET", "posts/%d" % pid, ctx=True)
            m = chk.get("meta", {})
            ok_t = bool(chk.get("title", {}).get("rendered"))
            ok_d = bool(m.get("_yoast_wpseo_metadesc"))
            ok_f = bool(m.get("_yoast_wpseo_focuskw"))
            ok_c = sorted(chk.get("categories", [])) == sorted(r["cat_ids"])
            ok_l = chk.get("content", {}).get("rendered", "").count("href=") >= 3
            print("id=%s TITLE:%s META:%s FOCUS:%s CATS:%s LINKS:%s status=%s" %
                  (pid, "Y" if ok_t else "N", "Y" if ok_d else "N", "Y" if ok_f else "N",
                   "Y" if ok_c else "N", "Y" if ok_l else "N", st))
    write_deliverable(results, pub, parsed)

def write_deliverable(results, pub, parsed):
    out = []
    out.append('<?xml version="1.0" encoding="UTF-8"?>')
    out.append('<html lang="en-US"><head><meta charset="UTF-8"/>')
    out.append('<title>karmactive India Publish Package — 8 Articles</title></head><body>')
    out.append('<h1>karmactive.com — India Article Package (8 Articles)</h1>')
    out.append('<p>Published backdated 1 hour with random 10–30 min gaps. Authored via REST API. Credentials not stored in files.</p>')
    for i, r in enumerate(results):
        pid, st = pub[i][1], pub[i][2]
        link = "https://www.karmactive.com/?p=%s" % pid if isinstance(pid, int) else "DRY RUN"
        out.append('<hr/><article>')
        out.append('<h2>ARTICLE %d — %s</h2>' % (r["n"], r["title"]))
        out.append('<p><strong>COMBINED TITLE:</strong> %s</p>' % r["title"])
        out.append('<p><strong>META DESCRIPTION (%d chars):</strong> %s</p>' % (r["metalen"], r["meta"]))
        out.append('<p><strong>FOCUS KEYPHRASE (4 words):</strong> %s</p>' % r["focus"])
        out.append('<p><strong>SEO SLUG:</strong> %s</p>' % r["slug"])
        out.append('<p><strong>CATEGORIES:</strong> %s</p>' % ", ".join(r["cats"]))
        out.append('<p><strong>TAGS:</strong> %s</p>' % ", ".join(r["tags"]))
        out.append('<p><strong>AUTHOR ID:</strong> %d &nbsp; <strong>STATUS:</strong> %s &nbsp; <strong>SCHEDULED date_gmt:</strong> %s</p>' % (r["author"], st, r["date_gmt"]))
        out.append('<p><strong>LIVE URL:</strong> <a href="%s">%s</a></p>' % (link, link))
        out.append('<p><strong>Word count:</strong> %d &nbsp; <strong>Internal+External links:</strong> %d</p>' % (r["wc"], r["nlinks"]))
        out.append('<h3>Body (with embedded links)</h3>')
        out.append(parsed[i])
        out.append('</article>')
    out.append('</body></html>')
    fn = r"C:\Users\Hp\OneDrive\karmactive-pipeline\stage4_stage5_published_india.html"
    with open(fn, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("\nWROTE deliverable: %s" % fn)

if __name__ == "__main__":
    main()
