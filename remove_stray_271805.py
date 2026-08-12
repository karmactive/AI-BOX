import os, subprocess, json
BASE="C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP="https://www.karmactive.com/wp-json/wp/v2"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
PASS=open(BASE+"wp_pass.txt").read().strip()
def put(pid,p):
    return json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}","-X","PUT",
        f"{WP}/posts/{pid}?context=edit","-H","Content-Type: application/json",
        "-d",json.dumps(p,ensure_ascii=False)],capture_output=True,text=True,timeout=120).stdout)
def get(u):
    return json.loads(subprocess.run(["curl","-s","-A",UA,"-u",f"Karmactive Staff:{PASS}",u],
                       capture_output=True,text=True,timeout=90).stdout)

# trash the stray duplicate 271805 (recoverable)
r=put(271805,{"status":"trash"})
print("271805 ->", r.get("status"), "(id", r.get("id"), ")")

# confirm only 271822 remains for colombia
print("\nRemaining Colombia posts:")
for pid in [271805,271822]:
    d=get(f"{WP}/posts/{pid}?context=edit")
    print(f"  {pid}: status={d.get('status')} title={d.get('title',{}).get('rendered','')}")
