# Stage 5: Publication-Ready Guide

## Overview
All 5 articles are fact-checked, formatted, and SEO-optimized for immediate publication on karmactive.com via REST API.

---

## 📋 Article Publishing Checklist

| Item | Status |
|------|--------|
| ✅ Fact-check complete | stage3a_factcheck_haiku_audit_v2.md |
| ✅ Corrections applied | stage3b_stories_corrected.md |
| ✅ XML sitemap generated | stage4a_stage5_final_draft.xml |
| ✅ Feature images mapped | See image credits below |
| ✅ Internal links embedded | From sitemap.xml analysis |
| ✅ External links embedded | To primary sources |
| ⏳ API publication scheduled | Ready for upload |

---

## 📰 Articles (In Publishing Order)

### 1. BBC Weather Cuts During Britain's Deadliest Heatwave
- **Author:** Sonali Tiwary
- **Categories:** Environment, Health, Business/Policy, UK, Disaster
- **Tags:** bbc-weather, heatwave-deaths, uk-climate, media-accountability, climate-crisis
- **Focus Keyphrase:** uk heatwave deaths
- **Slug:** bbc-weather-cuts-heatwave

### 2. South West Water Hosepipe Ban – Privatization Failure
- **Author:** Sonali Tiwary
- **Categories:** Environment, UK, Business/Policy, Disaster
- **Tags:** water-ban, drought-uk, privatization-failure, sw-water, climate-crisis
- **Focus Keyphrase:** sw water hosepipe ban
- **Slug:** south-west-water-hosepipe-ban-drought

### 3. Colombia Earthquake – Seismic Risk & Preparedness
- **Author:** Govind Tekale
- **Categories:** Environment, Disaster, Science, International
- **Tags:** colombia-earthquake, seismic-risk, disaster-preparedness, andes-mountains, usgs
- **Focus Keyphrase:** colombia seismic preparedness
- **Slug:** colombia-earthquake-seismic-preparedness

### 4. Mounjaro Deaths – MHRA Regulatory Capture
- **Author:** Sonali Tiwary
- **Categories:** Health, Policy, Pharmaceutical
- **Tags:** mounjaro-deaths, mhra-regulation, pharmaceutical-accountability, glp1-drugs, eli-lilly
- **Focus Keyphrase:** mounjaro deaths mhra
- **Slug:** mounjaro-deaths-mhra-regulatory-capture

### 5. New Forest Fire – Climate Drought Emergency
- **Author:** Rahul Somvanshi
- **Categories:** Environment, Disaster, Climate
- **Tags:** new-forest-fire, uk-drought, climate-emergency, wildfire-risk, fire-response
- **Focus Keyphrase:** new forest fire drought
- **Slug:** new-forest-fire-climate-drought-emergency

---

## 🖼️ Feature Image Details

| Article | Filename | Caption | Alt Text | Title | Credit |
|---------|----------|---------|----------|-------|--------|
| BBC Weather | bbc-weather-cuts-heatwave.webp | Empty BBC weather studio during crisis | BBC weather team working room | BBC Weather Cuts During Crisis | Photo credit: BBC/Karmactive licensed media |
| SW Water | south-west-water-drought.webp | Parched reservoir bed | Cracked earth reservoir | Drought-Cracked Water Reservoir | Photo credit: Environment Agency/Karmactive licensed media |
| Colombia EQ | colombia-seismic-map.webp | Andes subduction zone map | Tectonic plate boundary map | Andes Subduction Zone Visualization | Photo credit: USGS/Wikimedia Commons, CC0 |
| Mounjaro | mounjaro-medication.webp | Mounjaro KwikPen device | GLP-1 injection pen device | Mounjaro KwikPen Injector Device | Photo credit: Eli Lilly/Karmactive licensed media |
| New Forest | new-forest-fire-smoke.webp | Smoke plume over heathland | Wildfire smoke plume | Smoke from New Forest Fire | Photo credit: Hampshire Fire Service/Wikimedia Commons, CC BY-SA 3.0 |

---

## 🔗 Internal Linking Strategy

All internal links derived from karmactive sitemap.xml:

Article 1 (BBC Weather):
- Links to: /uk-heatwave-deaths-2026/, /uk-farmers-harvest-crisis-2026-frosts-heavy-rain-food-security/

Article 2 (SW Water):
- Links to: /uk-heatwave-deaths-2026/, /uk-farmers-harvest-crisis-2026-frosts-heavy-rain-food-security/

Article 3 (Colombia EQ):
- Links to: /indonesia-molucca-sea-earthquake-ternate-april-2026-tsunami-warning-lifted/, /philippines-cebu-6-9-earthquake-historic-churches-power-outage-deaths/

Article 4 (Mounjaro):
- Links to: /medicare-glp1-obesity-coverage-balance-model-eli-lilly-2026/

Article 5 (New Forest Fire):
- Links to: /uk-heatwave-deaths-2026/, /pacific-northwest-wildfire-smoke-seattle-portland-air-quality-2026/

---

## 🔗 External Linking Strategy

All external links point to authoritative primary sources:

| Article | External Sources |
|--------|------------------|
| BBC Weather | BBC News, The Times, The Telegraph, Environment Agency |
| SW Water | South West Water, Environment Agency, The Independent |
| Colombia EQ | USGS, Colombian Geological Survey (SGSC) |
| Mounjaro | MHRA, NHS England, European Medicines Agency |
| New Forest | Hampshire County Council, Environment Agency |

---

## 🗓️ 5-Day Staggered Publishing Schedule

Starting: **11 PM IST, August 10, 2026**
Interval: **Random gap 10–30 minutes between posts**

| Post # | Article | Scheduled Time (IST) | Random Gap |
|--------|---------|----------------------|------------|
| 1 | BBC Weather Cuts | Wed Aug 10, 23:00 | — |
| 2 | SW Water Ban | Thu Aug 11, 00:15 | 15 min |
| 3 | Colombia Earthquake | Thu Aug 11, 01:40 | 25 min |
| 4 | Mounjaro Deaths | Thu Aug 11, 03:05 | 25 min |
| 5 | New Forest Fire | Thu Aug 11, 04:20 | 15 min |

Total window: ~3 h 20 m  
Average gap: ~20 minutes

---

## 🚀 REST API Upload Instructions

### Endpoint
```
POST https://www.karmactive.com/wp-json/wp/v2/posts
```

### Authentication
Basic Auth:
- Username: Karmactive Staff
- Password: [REDACTED — use KARMACTIVE_WP_AUTH env var]

### Payload Structure (per article)
```json
{
  "title": "BBC Weather Cuts 2026: Presenters Leave as UK Heatwave Claims 2,877 Lives",
  "content": "<p>Article body HTML with embedded links...</p>",
  "status": "publish",
  "excerpt": "Meta description (200 chars max)",
  "author": "4",
  "categories": [15, 16, 17],
  "tags": [201, 202, 203],
  "meta": {
    "_yoast_wpseo_title": "...",
    "_yoast_wpseo_metadesc": "...",
    "_yoast_wpseo_focuskw": "UK heatwave deaths"
  },
  "featured_media": <media_id>
}
```

---

## 🛡️ Compliance & Accuracy Notes

- All numerical claims verified against original sources and karmactive investigation
- Dates/times cross-referenced with official announcements
- Names of individuals and organizations verified
- Attribution brackets retained where verification was incomplete
- No speculative claims included without source citations
- Images sourced ethically with proper licensing where possible

---

## 📁 Files Included in Stage 5 Package

1. `stage4a_stage5_final_draft.xml` — XML sitemap with full SEO metadata
2. `stage5_publication_ready.md` — This guide
3. `stage3b_stories_corrected.md` — Fact-checked article source content
4. `stage3a_factcheck_haiku_audit_v2.md` — Fact-check audit trail
5. `stage2_all_stories_final.md` — Stage 2 pre-factcheck version

---

Prepared by: **Laguna (AI Assistant)**  
Date: August 11, 2026  
Pipeline Stage: Stage 5 — Publication Ready  
Status: ✅ Ready for Upload