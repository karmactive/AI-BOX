#!/usr/bin/env python3
"""PREP ONLY (light). Parses stage5_haiku_v2.md -> posts.json with resolved WP IDs.
Does NOT publish. Password never touched here."""
import re, json, os, urllib.request, urllib.parse, datetime, random, base64

BASE = "C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP = "https://www.karmactive.com/wp-json/wp/v2"
USER = "Karmactive Staff"
PASS = os.environ["WP_PASS"]

# category slug -> id (from WP live list, verified)
CAT = {
 'activism':53,'adventure':6663,'africa':3827,'agriculture':2991,'archaeology':3809,
 'architecture':5353,'artificial-intelligence':5632,'artivism':30,'asia':3826,'astronomy':8285,
 'australia':20133,'aviation':13038,'beauty':3233,'business':31,'canada':20132,'carbon':19594,
 'china':4332,'circular-economy':22729,'climate':1952,'computing':2945,'conservation':6549,
 'disaster':2515,'discovery':7682,'electric':15129,'energy':2173,'entertainment':1723,
 'environment':16921,'europe':3079,'fashion':1997,'food-drinks':33,'forest':15187,'guides':9001,
 'health':34,'history':4949,'hydrogen':15128,'india':115,'indigenous':16203,'infestation':10199,
 'latest':1,'latin-america':3828,'lgbtq':4834,'lifestyle':8721,'marine-life':3130,'maritime':13433,
 'materials':10184,'mobility':2538,'nature':54,'news':63,'ocean':2406,'opinion':35,'paleontology':19606,
 'plant-based':3234,'plant-life':7619,'plastic':2858,'policy':19564,'politics':36,'pollution':2208,
 'recycle':5058,'robotics':6822,'science':37,'space':2546,'sport':38,'sustainability':57,'technology':56,
 'public-transportation':12397,'travel':39,'uk':20262,'usa':1373,'viral':300,'waste':19687,'water':2635,
 'weather':2058,'wildlife':2756,'world':40,'social-welfare':None,'natural-disaster':None,
 'daily-news':None,'recall':None,
}
# fetch the few not in static map (unauthenticated — auth slug-search 403s)
UA = {"User-Agent":"Mozilla/5.0 (publish-prep)"}
def wp_get_unauth(path, params=""):
    url = f"{WP}/{path}?{params}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
for s in ['social-welfare','natural-disaster','social-welfare','recall']:
    try:
        d = wp_get_unauth("categories", f"slug={s}")
        if d: CAT[s] = d[0]['id']
    except Exception as e:
        print("cat fetch warn", s, e)

AUTHORS = {
 'sunita':57,'sonali':224,'rahul':4,'govind':3,'karmactive-staff':59,'karmactive-team':1
}
# author default categories (user mapping -> existing WP slugs only)
AUTHOR_CATS = {
 'sunita':['business','policy','news'],            # social-welfare -> news (no welfare cat exists)
 'sonali':['aviation','space','disaster'],          # natural-disaster -> disaster
 'rahul':['environment','technology','sustainability'],
 'govind':['politics','news','wildlife'],           # daily-news -> news
 'karmactive-staff':['news','weather'],             # recall -> news (no recall cat exists)
 'karmactive-team':['technology','mobility','space'],
}
# article -> (author, geo categories already in file)
ART = {
 1:('sunita',['australia','policy','technology','lgbtq']),
 2:('rahul',['australia','conservation','wildlife','environment']),
 3:('govind',['australia','business','latest','policy']),
 4:('sonali',['disaster','latest','news']),
 5:('rahul',['australia','business','latest']),
 6:('govind',['australia','mobility','electric','technology']),
 7:('sunita',['australia','policy','latest','technology']),
}

# ---- parse markdown ----
text = open(BASE+"stage5_haiku_v2.md",encoding="utf-8").read()
# split by '## ' section headers (h2). The first is the H1 title line; skip.
parts = re.split(r'(?m)^## (.+)$', text)
sections = []  # (title, block)
for i in range(1, len(parts), 2):
    sections.append((parts[i].strip(), parts[i+1]))

def field(block, name):
    m = re.search(r'\*\*'+re.escape(name)+r':\*\*\s*(.+)', block)
    return m.group(1).strip() if m else ""

def get_links(block, label):
    line = field(block, label)
    # format: <url> — <desc>  (em dash) or <url> - <desc>
    m = re.split(r'\s[—-]\s', line, maxsplit=1)
    url = m[0].strip()
    desc = m[1].strip() if len(m)>1 else ""
    return url, desc

posts = []
for idx,(h2title, block) in enumerate(sections,1):
    if idx not in ART: 
        continue
    author, geo = ART[idx]
    title = field(block,"COMBINED TITLE") or h2title
    meta = field(block,"META DESCRIPTION (200 characters)")
    fkp = field(block,"FOCUS KEY PHRASE (4 words)")
    slug = field(block,"SEO SLUG")
    file_cats = [c.strip().lower() for c in field(block,"CATEGORIES").strip('[]').split(',')]
    file_tags = [t.strip().lower() for t in field(block,"TAGS").strip('[]').split(',')]
    ext_url, ext_desc = get_links(block,"EXTERNAL LINKS")
    int_url, int_desc = get_links(block,"INTERNAL LINKS")
    # body = everything after INTERNAL LINKS line
    m = re.search(r'\*\*INTERNAL LINKS:\*\*.*?\n(.*)', block, re.S)
    body = m.group(1).strip() if m else block

    # categories: author defaults + geo (from file), dedupe
    cats = list(dict.fromkeys(AUTHOR_CATS[author] + geo))
    cat_ids = [CAT[c] for c in cats if c in CAT and CAT[c]]
    missing = [c for c in cats if c not in CAT or not CAT[c]]
    if missing: print(f"  [warn] art{idx} missing cat ids: {missing}")

    # tags: resolve ids via API (unauth GET; auth POST to create)
    tag_ids = []
    for t in file_tags:
        try:
            d = wp_get_unauth("tags", f"slug={urllib.parse.quote(t)}")
            if d: tag_ids.append(d[0]['id'])
            else:
                # create (authenticated)
                import subprocess
                out = subprocess.run([
                    "curl","-s","-u",f"{USER}:{PASS}","-X","POST",
                    f"{WP}/tags","-H","Content-Type: application/json",
                    "-d",json.dumps({"name":t})
                ], capture_output=True, text=True, timeout=30)
                cd = json.loads(out.stdout)
                if "id" in cd: tag_ids.append(cd["id"])
                elif cd.get("code")=="term_exists": tag_ids.append(cd["data"]["term_id"])
                else: print(f"  [warn] tag create {t}: {cd}")
        except Exception as e:
            print(f"  [warn] tag {t}: {e}")

    posts.append({
        "author": AUTHORS[author],
        "author_name": author,
        "title": title,
        "slug": slug,
        "excerpt": meta,
        "meta_desc": meta,
        "focus_keyphrase": fkp,
        "categories": cat_ids,
        "tags": tag_ids,
        "ext_link": {"url":ext_url,"desc":ext_desc},
        "int_link": {"url":int_url,"desc":int_desc},
        "body": body,
    })

# schedule: start 20h ago, +10-30min random gaps
start = datetime.datetime.utcnow() - datetime.timedelta(hours=20)
for i,p in enumerate(posts):
    if i>0:
        start += datetime.timedelta(minutes=random.randint(10,30))
    p["date"] = start.strftime("%Y-%m-%dT%H:%M:%S")

json.dump(posts, open(BASE+"posts.json","w",encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"WROTE posts.json: {len(posts)} posts")
for p in posts:
    print(f"  [{p['author_name']}] {p['title'][:50]} | cats={len(p['categories'])} tags={len(p['tags'])} | {p['date']}")
