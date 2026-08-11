#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, json, subprocess, base64, time, random, datetime, html, os

W = "https://www.karmactive.com"
# Credentials from environment only — never store in files
WP_USER = os.environ.get("WP_USER", "Karmactive Staff")
WP_PASS = os.environ.get("WP_PASS", "")
if not WP_PASS:
    print("ERROR: WP_PASS environment variable not set.")
    print("Usage: WP_PASS='your-app-password' python3 build_publish.py [--dry]")
    sys.exit(1)
USERPASS = f"{WP_USER}:{WP_PASS}"
B64 = base64.b64encode(USERPASS.encode()).decode()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# ---- Resolve IDs (verified live via API earlier) ----
CAT = {
    "environment": 16921, "health": 34, "uk": 20262, "disaster": 2515,
    "policy": 19564, "science": 37, "latin america": 3828, "climate": 1952,
}
TAG = {
    "heatwave": 22924, "extreme weather": 8018, "public health crisis": 14100, "health alert": 14497,
    "drought": 1270, "water scarcity": 869, "water conservation": 11070, "water shortage": 898,
    "earthquake": 1141, "seismic": 22776, "disaster": 21528, "colombia": 1194,
    "glp 1": 22990, "weight loss drugs": 22989, "wildfire": 7528, "climate crisis": 397,
}

# Per-article resolved taxonomy (Haiku mapping from sitemap)
ARTS = [
  dict(id=1, author=224,
       cats=["environment","health","uk","disaster"],
       tags=["heatwave","extreme weather","public health crisis","health alert"],
       focus="bbc weather cuts heatwave",
       meta="With 2,877 heatwave deaths, Britain's deadliest heatwave coincides with BBC weather cuts axing 60% of the national team under a £500M cost-saving programme."),
  dict(id=2, author=224,
       cats=["environment","uk","disaster","policy"],
       tags=["drought","water scarcity","water conservation","water shortage"],
       focus="sw water hosepipe ban",
       meta="South West Water imposes hosepipe ban on 1.5M customers as half of England enters drought status\u2014exposing decades of underinvestment since 1989 privatization."),
  dict(id=3, author=3,
       cats=["disaster","science","latin america"],
       tags=["earthquake","seismic","disaster","colombia"],
       focus="colombia earthquake preparedness gaps",
       meta="A 7.4-magnitude earthquake strikes western Colombia near San Jos\u00e9 del Palmar, exposing critical infrastructure vulnerabilities in a seismically active region."),
  dict(id=4, author=224,
       cats=["health","policy"],
       tags=["glp 1","weight loss drugs","public health crisis","health alert"],
       focus="mounjaro deaths mhra approval",
       meta="Mounjaro deaths in the UK hit 216\u2014raising questions about MHRA oversight as the regulator considers approving Foundayo, another Eli Lilly GLP-1 drug."),
  dict(id=5, author=4,
       cats=["environment","disaster","climate"],
       tags=["wildfire","drought","climate crisis","extreme weather"],
       focus="new forest fire drought",
       meta="A31 vehicle fire spreads into New Forest heathland as UK drought reaches critical levels\u2014160 emergency calls and 10 fire crews deployed."),
]

# Extra REAL internal links harvested from the live sitemap (verified live)
EXTRA_LINKS = {
  2: [("Southern Water", "https://www.karmactive.com/southern-water-bans-tankers-billionaire-estate-drought/")],
  4: [("GLP-1 weight-loss drug", "https://www.karmactive.com/weight-loss-jabs-linked-to-400-pancreas-problems-and-5-deaths-mhra-launches-genetic-study/")],
}

def api(method, path, data=None, ctx=False, retries=5):
    args = ["curl","-s","--retry","5","--retry-delay","2","--connect-timeout","20","--max-time","90",
            "-A",UA,"-H","Authorization: Basic "+B64,"-X",method]
    if data is not None:
        args += ["-H","Content-Type: application/json","--data",json.dumps(data,ensure_ascii=False)]
    url = W+"/wp-json/wp/v2/"+path + ("?context=edit" if ctx else "")
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
            if attempt == retries-1:
                raise
            time.sleep(2)
    raise SystemExit("API FAIL %s %s" % (method, path))

def parse_articles(path):
    txt = open(path, encoding="utf-8").read()
    blocks = re.split(r"<article>", txt)[1:]
    arts = []
    for b in blocks:
        b = b.split("</article>")[0]
        h1 = re.search(r"<h1>(.*?)</h1>", b, re.S).group(1).strip()
        # body = everything after </header> up to end (includes <p> body + <footer>)
        m = re.search(r"</header>(.*)", b, re.S)
        body = m.group(1).strip() if m else b
        # strip "Primary Sources" footer? keep it (adds external links). leave as is.
        # title/meta from header lines
        slug = re.search(r"<strong>Slug:</strong>\s*([^\n<]+)", b)
        slug = slug.group(1).strip() if slug else None
        arts.append(dict(h1=h1, body=body, slug=slug))
    return arts

def measure_meta(s):
    return len(s)

def build_body(raw_body, extra):
    # raw_body is HTML already (one <p> per para + <footer>). Prepend reading time.
    text = re.sub(r"<[^>]+>", " ", raw_body)
    text = re.sub(r"\s+", " ", text).strip()
    wc = len(text.split())
    rt = max(1, round(wc/200))
    out = '<p><em>Estimated reading time: %d minute%s</em></p>\n' % (rt, "" if rt==1 else "s")
    out += raw_body
    # inject extra internal links on verified anchors
    for phrase, url in (extra or []):
        if phrase in out:
            out = out.replace(phrase, '<a href="%s">%s</a>' % (url, phrase), 1)
        else:
            raise SystemExit("ANCHOR MISS: %r not in article body" % phrase)
    return out, wc

def main():
    DRY = "--dry" in sys.argv
    src = r"C:\Users\Hp\OneDrive\karmactive-pipeline\stage4_stage5_publish_ready.html"
    parsed = parse_articles(src)
    print("Parsed %d articles" % len(parsed))
    results = []
    # backdated start: server now - 18h (server UTC == 2026-08-11T09:53Z at check)
    start = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=18)
    cur = start
    for i, a in enumerate(parsed):
        meta = ARTS[i]
        body, wc = build_body(a["body"], EXTRA_LINKS.get(meta["id"]))
        nlinks = body.count('href=')
        mlen = measure_meta(meta["meta"])
        if mlen > 200:
            # trim to <=200 at last space
            cut = meta["meta"][:200].rsplit(" ",1)[0]
            meta["meta"] = cut + "\u2026"
            mlen = len(meta["meta"])
        cat_ids = [CAT[c] for c in meta["cats"]]
        tag_ids = [TAG[t] for t in meta["tags"]]
        date_gmt = cur.strftime("%Y-%m-%dT%H:%M:%S")
        if i < len(parsed)-1:
            cur += datetime.timedelta(minutes=random.randint(10,30))
        row = dict(n=meta["id"], title=a["h1"], slug=a["slug"], focus=meta["focus"],
                   meta=meta["meta"], metalen=mlen, author=meta["author"],
                   cats=meta["cats"], cat_ids=cat_ids, tags=meta["tags"], tag_ids=tag_ids,
                   wc=wc, nlinks=nlinks, date_gmt=date_gmt, body_paras=body.count("<p"), body=body)
        results.append(row)
        print("ART%d | title=%s" % (meta["id"], a["h1"][:70]))
        print("   slug=%s | focus=%s | metalen=%d | author=%s" % (a["slug"], meta["focus"], mlen, meta["author"]))
        print("   cats=%s (ids %s)" % (meta["cats"], cat_ids))
        print("   tags=%s (ids %s)" % (meta["tags"], tag_ids))
        print("   wc=%d paras=%d links=%d date_gmt=%s" % (wc, row["body_paras"], nlinks, date_gmt))
        if nlinks < 3:
            raise SystemExit("TOO FEW LINKS art %d: %d" % (meta["id"], nlinks))
    if DRY:
        print("\nDRY RUN OK \u2014 no network writes.")
        return
    # ---- PUBLISH ----
    pub = []
    for r in results:
        # idempotency
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
        meta_payload = dict(meta={"_yoast_wpseo_metadesc": r["meta"],
                                  "_yoast_wpseo_focuskw": r["focus"],
                                  "_yoast_wpseo_title": r["title"]})
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
            ok_t = bool(chk.get("title",{}).get("rendered"))
            ok_d = bool(m.get("_yoast_wpseo_metadesc"))
            ok_f = bool(m.get("_yoast_wpseo_focuskw"))
            ok_c = sorted(chk.get("categories",[])) == sorted(r["cat_ids"])
            ok_l = chk.get("content",{}).get("rendered","").count("href=") >= 3
            print("id=%s TITLE:%s META:%s FOCUS:%s CATS:%s LINKS:%s status=%s" %
                  (pid, "Y" if ok_t else "N", "Y" if ok_d else "N", "Y" if ok_f else "N",
                   "Y" if ok_c else "N", "Y" if ok_l else "N", st))
    # ---- WRITE CONSOLIDATED DELIVERABLE FILE ----
    write_deliverable(results, pub, parsed)

def write_deliverable(results, pub, parsed):
    # build consolidated HTML
    out = []
    out.append('<?xml version="1.0" encoding="UTF-8"?>')
    out.append('<html lang="en-US"><head><meta charset="UTF-8"/>')
    out.append('<title>karmactive Publish Package \u2014 5 Articles (Published)</title></head><body>')
    out.append('<h1>karmactive.com \u2014 Published Article Package</h1>')
    out.append('<p>Published backdated ~18h with random 10–30 min gaps. Authored via REST API with environment-based credentials.</p>')
    for i, r in enumerate(results):
        pid, st = pub[i][1], pub[i][2]
        link = "https://www.karmactive.com/?p=%s" % pid if isinstance(pid,int) else "EXISTS"
        out.append('<hr/><article>')
        out.append('<h2>ARTICLE %d \u2014 %s</h2>' % (r["n"], r["title"]))
        out.append('<p><strong>COMBINED TITLE:</strong> %s</p>' % r["title"])
        out.append('<p><strong>META DESCRIPTION (%d chars):</strong> %s</p>' % (r["metalen"], r["meta"]))
        out.append('<p><strong>FOCUS KEYPHRASE (4 words):</strong> %s</p>' % r["focus"])
        out.append('<p><strong>SEO SLUG:</strong> %s</p>' % r["slug"])
        out.append('<p><strong>CATEGORIES:</strong> %s</p>' % ", ".join(r["cats"]))
        out.append('<p><strong>TAGS:</strong> %s</p>' % ", ".join(r["tags"]))
        out.append('<p><strong>AUTHOR ID:</strong> %s &nbsp; <strong>STATUS:</strong> %s &nbsp; <strong>SCHEDULED date_gmt:</strong> %s</p>' % (r["author"], st, r["date_gmt"]))
        out.append('<p><strong>LIVE URL:</strong> <a href="%s">%s</a></p>' % (link, link))
        out.append('<p><strong>Word count:</strong> %d &nbsp; <strong>Internal+External links:</strong> %d</p>' % (r["wc"], r["nlinks"]))
        out.append('<h3>Body (with embedded links)</h3>')
        out.append(parsed[i]["body"])
        out.append('</article>')
    out.append('</body></html>')
    fn = r"C:\Users\Hp\OneDrive\karmactive-pipeline\stage4_stage5_published.html"
    open(fn,"w",encoding="utf-8").write("\n".join(out))
    print("\nWROTE deliverable: %s" % fn)

if __name__ == "__main__":
    main()
