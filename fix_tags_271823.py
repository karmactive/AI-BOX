#!/usr/bin/env python3
import os, json, subprocess
BASE="C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP="https://www.karmactive.com/wp-json/wp/v2"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
PASS=open(BASE+"wp_pass.txt").read().strip()
def get(u): return json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}",u],capture_output=True,text=True,timeout=90).stdout)
def put(pid,p): return json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}","-X","PUT",f"{WP}/posts/{pid}?context=edit","-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],capture_output=True,text=True,timeout=120).stdout)

valid=set()
for line in open(BASE+"sitemap_tags.txt",encoding="utf-8"):
    s=line.strip().lower()
    if s: valid.add(s)

slugs=["automotive","nhtsa","recall","safety","stellantis"]  # consumer-protection -> nhtsa (valid in file)
slug2id={t["slug"].lower():t["id"] for pg in range(1,20) for t in (get(f"{WP}/tags?per_page=100&page={pg}") or []) if isinstance(t,dict)}
ids=[]
for s in slugs:
    if s not in valid:
        print(f"  !! {s} not in file"); continue
    if s not in slug2id:
        r=json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}","-X","POST",f"{WP}/tags?context=edit","-H","Content-Type: application/json","-d",json.dumps({"name":s.replace('-',' ').title(),"slug":s})],capture_output=True,text=True,timeout=60).stdout)
        slug2id[s]=r["id"]
    ids.append(slug2id[s])
r=put(271823,{"tags":ids})
print("271823 tags:", r.get("tags"), "slugs:", slugs)
