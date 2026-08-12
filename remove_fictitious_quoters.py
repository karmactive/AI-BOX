#!/usr/bin/env python3
"""Keep ONLY the eSafety Commissioner Julie Inman Grant quote on post 271819.
Remove every other blockquote from posts 271819-271825. All other content preserved.
Editor auth (Sunita Somvanshi). Evidence: prior live GET of all 7 posts."""
import os, subprocess, json, re

BASE = "C:/Users/Hp/OneDrive/karmactive-pipeline/"
WP = "https://www.karmactive.com/wp-json/wp/v2"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
USER = "Sunita Somvanshi"
PASS = open(BASE + "wp_pass_sunita.txt", encoding="utf-8").read().strip()
AUTH = f"{USER}:{PASS}"

# Only the Julie Inman Grant quote survives (on 271819). All other blockquotes go.
KEEP = {271819: "Julie Inman Grant", 271820: None, 271821: None,
        271822: None, 271823: None, 271824: None, 271825: None}

ids = [271819, 271820, 271821, 271822, 271823, 271824, 271825]

def put(pid, content):
    body = json.dumps({"content": content})
    out = subprocess.run(["curl", "-s", "-A", UA, "-u", AUTH, "-X", "POST",
        f"{WP}/posts/{pid}", "-H", "Content-Type: application/json", "--data", body],
        capture_output=True, text=True)
    d = json.loads(out.stdout)
    if "code" in d:
        return (f"ERR {d.get('code')}")
    return f"OK {d.get('id')}"

for pid in ids:
    out = subprocess.run(["curl", "-s", "-A", UA, "-u", AUTH, f"{WP}/posts/{pid}?context=edit"],
                         capture_output=True, text=True)
    raw = json.loads(out.stdout).get("content", {}).get("raw", "")
    before_bq = len(re.findall(r"<blockquote", raw))

    keep_speaker = KEEP[pid]
    def drop(m):
        blockhtml = m.group(0)
        txt = re.sub(r"<[^>]+>", " ", blockhtml)
        txt = re.sub(r"\s+", " ", txt).strip()
        if keep_speaker and keep_speaker in txt:
            return blockhtml  # preserve this quote
        return ""  # remove the blockquote element entirely
    raw_new = re.sub(r"<blockquote>.*?</blockquote>", drop, raw, flags=re.S)
    after_bq = len(re.findall(r"<blockquote", raw_new))
    removed = before_bq - after_bq
    status = put(pid, raw_new)
    print(f"{pid}: before={before_bq} after={after_bq} removed={removed} -> {status}")
