#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Set featured images for the 7 published Australia articles (271819-271825).
Active model (Claude) task — Haiku excluded per pipeline boundary.
Uses wp_api (env-var auth). Idempotent: skips posts that already have an image.
Images sourced from Wikimedia Commons (public-domain / CC) with credit + licence.
"""
import os, time, datetime, tempfile
from wp_api import api, upload_media, UA

TMP = tempfile.gettempdir()

# (post_id, commons thumburl, credit, licence)
MEDIA = [
 (271819,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Census_in_australia_2001.jpg/1280px-Census_in_australia_2001.jpg",
  "Census in Australia 2001, via Wikimedia Commons", "CC0"),
 (271820,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Bald_eagle_nest_noaa.jpg/1280px-Bald_eagle_nest_noaa.jpg",
  "Bald eagle nest, NOAA, via Wikimedia Commons", "Public domain"),
 (271821,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/RBA_Building_August_2025.jpg/1280px-RBA_Building_August_2025.jpg",
  "Reserve Bank of Australia building, Aug 2025, via Wikimedia Commons", "CC BY-SA 4.0"),
 (271822,
  "https://upload.wikimedia.org/wikipedia/commons/7/7a/Terremoto_de_Lorica_Cordoba.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
  "Terremoto de Lorica, Córdoba, Colombia, via Wikimedia Commons", "CC BY-SA 4.0"),
 (271823,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/2006_Dodge_Hornet_Concept.JPG/1280px-2006_Dodge_Hornet_Concept.JPG",
  "2006 Dodge Hornet Concept, via Wikimedia Commons", "CC BY 2.0"),
 (271824,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/2024_Mitsubishi_ASX_Leonberg_2024_IMG_1053.jpg/1280px-2024_Mitsubishi_ASX_Leonberg_2024_IMG_1053.jpg",
  "2024 Mitsubishi ASX, Leonberg, via Wikimedia Commons", "CC BY-SA 4.0"),
 (271825,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Mobile-phone-426559_1920.jpg/1280px-Mobile-phone-426559_1920.jpg",
  "Mobile phone, via Wikimedia Commons", "CC0"),
]

def download(url, fn):
    mime = "image/png" if url.lower().split("?")[0].endswith(".png") else "image/jpeg"
    for attempt in range(6):
        r = subprocess.run(["curl","-sL","--connect-timeout","30","--max-time","180",
                            "-A",UA,"-w","%{http_code}","-o",fn,url],
                           capture_output=True, text=True, timeout=240)
        code = (r.stdout or "").strip()[-3:]
        size = os.path.getsize(fn) if os.path.exists(fn) else 0
        if code == "200" and size >= 5000:
            return mime
        time.sleep(10 * (attempt + 1))
    raise SystemExit("DOWNLOAD FAIL %s" % url)

import subprocess

def main():
    sem = os.path.join(TMP, "featured_images_au_done.sem")
    if os.path.exists(sem) and "--force" not in os.sys.argv:
        print("Semaphore present — already done. Use --force to re-run.")
        return
    for pid, url, credit, lic in MEDIA:
        cur = api("GET", "posts/%d" % pid, ctx=True)
        if cur.get("featured_media"):
            print("SKIP post %d — already featured_media=%s" % (pid, cur["featured_media"]))
            continue
        ext = ".png" if url.lower().split("?")[0].endswith(".png") else ".jpg"
        fn = os.path.join(TMP, "feat_au_%d%s" % (pid, ext))
        mime = download(url, fn)
        mresp = upload_media(fn, mime)
        mid = mresp["id"]
        time.sleep(3)
        api("PUT", "media/%d" % mid,
            data={"alt_text": "%s (%s)" % (credit, lic),
                  "caption": "<p>%s — <em>%s</em></p>" % (credit, lic)}, ctx=True)
        time.sleep(3)
        api("PUT", "posts/%d" % pid, data={"featured_media": mid}, ctx=True)
        time.sleep(3)
        print("POST %d -> media %d assigned (%s)" % (pid, mid, lic))
    open(sem, "w").write(datetime.datetime.now(datetime.timezone.utc).isoformat())
    print("DONE — featured images set for Australia articles.")

if __name__ == "__main__":
    main()
