#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, sys, tempfile, time, datetime

from wp_api import UA, api as curl_api, upload_media

TMP = tempfile.gettempdir()

# (post_id, image_url, credit, license)
MEDIA = [
 (271801,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Heat_wave_2018_07_280001_%2841929391560%29.jpg/1280px-Heat_wave_2018_07_280001_%2841929391560%29.jpg",
  "Heat wave 2018 (UK) by Tim Sackton, via Wikimedia Commons", "CC BY 2.0"),
 (271803,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Spruce_Run_Reservoir_drought_from_beach_%282%29%2C_Nov._2024.jpg/1280px-Spruce_Run_Reservoir_drought_from_beach_%282%29%2C_Nov._2024.jpg",
  "Spruce Run Reservoir drought, Nov 2024, via Wikimedia Commons", "CC BY-SA 4.0"),
 (271805,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/M_7.4_-_5_km_S_of_San_Jos%C3%A9_del_Palmar%2C_Colombia.png/1280px-M_7.4_-_5_km_S_of_San_Jos%C3%A9_del_Palmar%2C_Colombia.png",
  "USGS Shakemap — M7.4 San José del Palmar, Colombia, 2026-08-10", "Public domain (USGS)"),
 (271807,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Lilly_mounjaro_KwikPen_Tirzepatid_5_mg_per_dose_rate-9441.jpg/1280px-Lilly_mounjaro_KwikPen_Tirzepatid_5_mg_per_dose_rate-9441.jpg",
  "Lilly Mounjaro KwikPen (Tirzepatide), via Wikimedia Commons", "CC BY-SA 4.0"),
 (271809,
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Roadside_forest_fire_JEG7882.jpg/1280px-Roadside_forest_fire_JEG7882.jpg",
  "Roadside forest fire by P. Jeganathan, via Wikimedia Commons", "CC BY-SA 4.0"),
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
        # 429 / transient: back off and retry
        time.sleep(10 * (attempt + 1))
    raise SystemExit("DOWNLOAD FAIL %s (last code=%s size=%s)" % (url, code, size))


def main():
    sem = os.path.join(TMP, "featured_images_done.sem")
    if os.path.exists(sem) and "--force" not in sys.argv:
        print("Semaphore present — already done. Use --force to re-run.")
        return
    for pid, url, credit, lic in MEDIA:
        # idempotency: skip posts that already have a featured image
        cur = curl_api("GET", "posts/%d"%pid, ctx=True)
        if cur.get("featured_media"):
            print("SKIP post %d — already has featured_media=%s" % (pid, cur["featured_media"]))
            continue
        ext = ".png" if url.lower().split("?")[0].endswith(".png") else ".jpg"
        fn = os.path.join(TMP, "feat_%d%s" % (pid, ext))
        mime = download(url, fn)
        mresp = upload_media(fn, mime)
        mid = mresp["id"]
        time.sleep(3)
        curl_api("PUT", "media/%d"%mid,
                  data={"alt_text":"%s (%s)"%(credit, lic),
                        "caption":"<p>%s — <em>%s</em></p>"%(credit, lic)},
                  ctx=True)
        time.sleep(3)
        curl_api("PUT", "posts/%d"%pid, data={"featured_media":mid}, ctx=True)
        time.sleep(3)
        print("POST %d -> media id %d assigned (credit: %s)" % (pid, mid, credit))
    open(sem,"w").write(datetime.datetime.now(datetime.timezone.utc).isoformat())
    print("DONE — featured images set for all 5.")

if __name__ == "__main__":
    main()
