#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix tags on 5 posts: replace any tag not in sitemap_tags.txt with valid slugs."""
import os, json, subprocess, base64
BASE="C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP="https://www.karmactive.com/wp-json/wp/v2"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
PASS=open(BASE+"wp_pass.txt").read().strip()

def get(url):
    return json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}",url],
                       capture_output=True,text=True,timeout=90).stdout)
def put(pid,payload):
    out=subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}",
        "-X","PUT",f"{WP}/posts/{pid}?context=edit","-H","Content-Type: application/json",
        "-d",json.dumps(payload,ensure_ascii=False)],capture_output=True,text=True,timeout=120).stdout
    return json.loads(out)

# valid slugs from file
valid=set()
for line in open(BASE+"sitemap_tags.txt",encoding="utf-8"):
    s=line.strip().lower()
    if s: valid.add(s)

# corrected tags (slugs only)
NEW={
 271819:["cybersecurity","privacy","australia","digital","security"],
 271821:["economics","housing","policy","inflation","finance"],
 271822:["colombia","disaster","earthquake","emergency"],
 271824:["automotive","innovation","mitsubishi","vehicle","ev"],
 271825:["digital","media","policy","children","teenagers"],
}

# resolve slug->id (paginate)
slug2id={}
pg=1
while True:
    chunk=get(f"{WP}/tags?per_page=100&page={pg}")
    if not isinstance(chunk,list) or not chunk: break
    for t in chunk: slug2id[t["slug"].lower()]=t["id"]
    if len(chunk)<100: break
    pg+=1

for pid,slugs in NEW.items():
    ids=[]
    for s in slugs:
        if s not in valid:
            print(f"  !! {s} NOT in sitemap_tags.txt - SKIP"); continue
        if s not in slug2id:
            print(f"  ?? {s} in file but not on WP - will create"); 
            # create tag
            r=json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}",
                "-X","POST",f"{WP}/tags?context=edit","-H","Content-Type: application/json",
                "-d",json.dumps({"name":s.replace('-',' ').title(),"slug":s},ensure_ascii=False)],
                capture_output=True,text=True,timeout=60).stdout)
            if "id" in r: slug2id[s]=r["id"]
            else: print("  create failed",r); continue
        ids.append(slug2id[s])
    r=put(pid,{"tags":ids})
    ok="id" in r
    print(f"POST {pid}: {'OK' if ok else 'FAIL'} | tags={len(r.get('tags',[]))} | slugs={slugs}")
