#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Correct factual issues on live karmactive posts 271801 (BBC) and 271805 (Colombia)."""
import time

from wp_api import api

# ---------- ARTICLE 1: BBC — overstatement ----------
# Sources (Times/Telegraph/Standard, Aug 2026): the three are "considering taking
# voluntary redundancy"; none had accepted. Draft asserted they ARE leaving.
A1_TITLE_OLD = "BBC Weather Cuts 2026: Presenters Leave as UK Heatwave Claims 2,877 Lives"
A1_TITLE_NEW = "BBC Weather Cuts 2026: Presenters Weigh Exit as UK Heatwave Claims 2,877 Lives"

A1_REPL = [
 # lede
 ("Three of Britain's most experienced weather presenters are leaving the BBC, taking nearly nine decades of combined forecasting expertise with them.",
  "Three of Britain's most experienced weather presenters are considering taking voluntary redundancy from the BBC \u2014 a move that would take nearly nine decades of combined forecasting expertise with them. As of reporting, none has accepted the offer."),
 # departures section heading
 ("<p><strong>The Departures</strong></p>",
  "<p><strong>The Potential Departures</strong></p>"),
 # the assertion of departure
 ("Tomasz Schafernaker, Louise Lear, and Darren Bett represent 86 years of forecasting expertise. They join Carol Kirkwood, who took redundancy in January 2026 after 25 years at the BBC. Their departures represent the systematic dismantling of experienced weather communication when public trust in accurate forecasts is not valuable\u2014it is essential.",
  "Tomasz Schafernaker, Louise Lear, and Darren Bett represent 86 years of forecasting expertise, and all three are <a href=\"https://www.standard.co.uk/showbiz/bbc-weather-presenters-cuts-heatwave-b1292892.html\">reported to be weighing voluntary redundancy</a>. They would follow Carol Kirkwood, who did leave the BBC after 25 years on air. Should they go, it would mark the systematic dismantling of experienced weather communication at a moment when public trust in accurate forecasts is not merely valuable\u2014it is essential."),
]

# ---------- ARTICLE 3: Colombia — material omission ----------
# The quake killed 124+ (Wikipedia), 132 per Colombian Association of Capital Cities,
# 111 per President de la Espriella; 570-629 injured; 1,900+ missing.
A3_TITLE_OLD = "Colombia Earthquake 2026: 7.4-Magnitude Quake Exposes Preparedness Gaps"
A3_TITLE_NEW = "Colombia Earthquake 2026: 124+ Killed as 7.4 Quake Exposes Preparedness Gaps"

A3_CASUALTY_PARA = (
 "<p><strong>The Human Toll</strong></p>\n"
 "<p>The earthquake became the deadliest to strike Colombia this century. President Abelardo de la Espriella "
 "declared a national state of emergency and gave an initial toll of 111 dead. The Colombian Association of "
 "Capital Cities subsequently reported at least 132 killed and 570 injured, while "
 "<a href=\"https://www.reuters.com/world/earthquake-pacific-coast-shakes-colombian-capital-2026-08-10/\">Reuters</a> "
 "confirmed more than 100 dead as buildings pancaked and hospitals were damaged. Later tallies put the figure at "
 "124 or more killed, over 620 injured, and more than 1,900 people reported missing. Risaralda department alone "
 "accounted for at least 40 confirmed deaths. Rescue crews worked through the night to reach survivors trapped "
 "beneath rubble.</p>\n"
 "<p>These deaths are the measure of the preparedness gap. A magnitude 7.4 event is survivable with enforced "
 "seismic building codes; the toll reflects decades of construction that was never designed to withstand the "
 "forces this region reliably produces.</p>\n"
)

def patch_post(pid, title_old, title_new, replacements=None, insert_after=None, insert_html=None):
    p=api("GET","posts/%d"%pid,ctx=True)
    title=p["title"]["raw"]; content=p["content"]["raw"]
    orig_len=len(content)
    changes=[]

    if title.strip()==title_old:
        title=title_new; changes.append("title")
    elif title.strip()==title_new:
        changes.append("title(already)")
    else:
        raise SystemExit("post %d: unexpected title %r"%(pid,title))

    for old,new in (replacements or []):
        if old in content:
            content=content.replace(old,new,1); changes.append("repl:%s..."%old[:32])
        elif new in content:
            changes.append("repl(already):%s..."%old[:32])
        else:
            raise SystemExit("post %d: replacement target not found: %r"%(pid,old[:70]))

    if insert_html:
        if insert_html.strip()[:60] in content:
            changes.append("insert(already)")
        elif insert_after in content:
            content=content.replace(insert_after, insert_after+"\n\n"+insert_html, 1)
            changes.append("insert casualty section")
        else:
            raise SystemExit("post %d: insert anchor not found"%pid)

    api("PUT","posts/%d"%pid,{"title":title,"content":content},ctx=True)
    time.sleep(3)
    print("post %d patched: %s"%(pid,", ".join(changes)))
    print("   content %d -> %d chars"%(orig_len,len(content)))
    return title

def main():
    t1=patch_post(271801, A1_TITLE_OLD, A1_TITLE_NEW, replacements=A1_REPL)
    # Yoast: title + meta must match the corrected framing
    api("PUT","posts/271801",{"meta":{
        "_yoast_wpseo_title": t1,
        "_yoast_wpseo_metadesc": "With 2,877 heatwave deaths, Britain's deadliest heatwave coincides with BBC weather cuts as three top presenters weigh voluntary redundancy under \u00a3500M savings."}},
        ctx=True)
    time.sleep(3)

    anchor="<p>Within hours, \"earthquake today\" queries surged over 1,000%, and \"colombia earthquake\" emerged with 10,000+ searches. This is not anomaly. This is Colombia's geological reality: the nation sits atop one of Earth's most seismically unstable regions.</p>"
    t3=patch_post(271805, A3_TITLE_OLD, A3_TITLE_NEW,
                  insert_after=anchor, insert_html=A3_CASUALTY_PARA)
    api("PUT","posts/271805",{"meta":{
        "_yoast_wpseo_title": t3,
        "_yoast_wpseo_metadesc": "A 7.4-magnitude earthquake near San Jos\u00e9 del Palmar killed at least 124 people and injured over 620, exposing critical seismic vulnerabilities in western Colombia."}},
        ctx=True)
    time.sleep(3)
    print("DONE")

if __name__=="__main__":
    main()
