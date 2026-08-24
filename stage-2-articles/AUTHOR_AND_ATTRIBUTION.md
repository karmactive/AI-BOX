# AUTHOR INFORMATION & ATTRIBUTION GUIDE
## Karmactive.COM Stage 2 Stories

**Template Created:** August 24, 2026  
**Purpose:** Standardize author bylines and credentials across all 5 stories  
**Status:** AWAITING AUTHOR ASSIGNMENT

---

## REQUIRED INFORMATION

### Author Details (TO BE FILLED IN):
```
Author Name: [REQUIRED]
Author Email: [OPTIONAL]
Author LinkedIn: [OPTIONAL]
Author Bio: [REQUIRED - 50-150 words]
Author Photo: [OPTIONAL - 200x200px minimum]
Author Credentials: [REQUIRED - specific beats/expertise]
Publication Role: Senior Journalist, Contributing Writer, Editor, etc.
```

---

## BYLINE FORMAT FOR ARTICLES

### Standard Byline (all 5 stories):
```html
<div class="article-byline">
  <strong>By:</strong> [Author Name]  
  <strong>Published:</strong> August 24, 2026  
  <strong>Updated:</strong> [If applicable]  
  <strong>Reading Time:</strong> [2-3 minutes per story]
</div>
```

### Markdown Format:
```markdown
**By:** [Author Name]  
**Publication Date:** August 24, 2026  
**Reading Time:** [2-3 minutes]
```

### HTML Format (for website):
```html
<p class="byline">
  <span class="label">By:</span> 
  <span class="author-name">[Author Name]</span><br>
  <span class="label">Published:</span> 
  <span class="publication-date">August 24, 2026</span><br>
  <span class="label">Reading Time:</span> 
  <span class="reading-time">[2-3 min]</span>
</p>
```

---

## AUTHOR BIO TEMPLATE (To be customized)

### Option 1 - Professional Bio (Standard):
```
[Author Name] is a veteran journalist with [X] years of experience 
covering [beats/topics] for major publications. [He/She/They] specializes 
in [specific expertise], bringing deep investigation and analysis to complex 
stories affecting [audience]. [Author Name] has contributed to 
[publications/outlets] and is a contributor to Karmactive.COM.
```

### Option 2 - Expanded Bio (For author page):
```
[Author Name] is a senior journalist with [X] years of experience in 
current events reporting. [His/Her/Their] coverage spans [topic areas], 
including international affairs, politics, sports, and weather-related 
disasters. [Author Name] holds a degree in [field] from [institution] and 
has won [awards/recognition] for investigative reporting. [He/She/They] is 
committed to factual, balanced reporting and has contributed to 
[news outlets]. [Author Name] is a regular contributor to Karmactive.COM.
```

### Option 3 - Concise Bio (For article footer):
```
[Author Name] is an experienced journalist covering current events, 
politics, sports, and breaking news for Karmactive.COM. Follow on 
[social platform]: @[handle].
```

---

## EXAMPLE IMPLEMENTATION

### If Author = "Sarah Mitchell" (Example - CUSTOMIZE AS NEEDED):

**Byline in Article:**
```
By: Sarah Mitchell  
Published: August 24, 2026  
Reading Time: 2-3 minutes
```

**Author Bio for Article Footer:**
```
Sarah Mitchell is a senior journalist with 15+ years of experience 
covering current events, international affairs, and breaking news. 
She specializes in fact-checked reporting on politics, sports, 
weather emergencies, and geopolitical tensions. Sarah holds an M.A. 
in Journalism from Columbia University and has contributed to major 
news outlets. She is a regular contributor to Karmactive.COM.
```

**Author Page/Social:**
```
Website: [author-domain]
LinkedIn: [linkedin-url]
Twitter: @[handle]
Email: [email]@karmactive.com
```

---

## WHERE BYLINES APPEAR

### 1. Article Header (REQUIRED)
- Position: Top of article, before headline
- Format: Text with publication date
- Display: Prominent, readable font size (14-16px)

### 2. Article Footer (RECOMMENDED)
- Position: After article body, before comments/related articles
- Format: Author photo (if available) + bio + social links
- Display: Separated section with gray background or border

### 3. Author Archive Page (RECOMMENDED)
- Position: If author page exists on site
- Format: Full bio + all published articles by author
- Display: Profile section + article grid/list

### 4. Author Search Result (OPTIONAL)
- Position: Search engine snippet
- Format: Author name in meta data
- Display: Structured data for Google author attribution

---

## SCHEMA.ORG AUTHOR MARKUP

### Person Schema (Author):
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "[Author Name]",
  "url": "[author-website-or-profile-url]",
  "image": "[author-photo-url]",
  "description": "[Author bio]",
  "sameAs": [
    "[LinkedIn-url]",
    "[Twitter-url]",
    "[Other-social-url]"
  ]
}
```

### NewsArticle Author Reference:
```json
"author": {
  "@type": "Person",
  "name": "[Author Name]",
  "url": "[author-profile-url]"
}
```

---

## SOCIAL MEDIA AUTHOR CREDIT

### Twitter Format:
```
"[Article Headline]" by [Author Name] | Karmactive.COM
https://www.karmactive.com/news/[article-slug]
@[author-handle] @karmactive
```

### LinkedIn Format:
```
Title: [Article Headline]
Body: Published on Karmactive.COM
Author: [Author Name]
Link: [article-url]
```

### Facebook Format:
```
Article: [Article Headline]
By: [Author Name]
Publication: Karmactive.COM
Link: [article-url]
```

---

## BYLINE CONSISTENCY CHECKLIST

- [ ] Author name matches across all publications
- [ ] Spelling is consistent (middle initials, full first name, etc.)
- [ ] Credentials are accurate and current
- [ ] Email address is correct (if public)
- [ ] Social media handles are verified
- [ ] Author photo is professional (if using)
- [ ] Bio is 50-150 words (if short version)
- [ ] Contact information is up-to-date
- [ ] Author page link works (if author page exists)
- [ ] Schema markup is properly formatted

---

## ARTICLE-SPECIFIC AUTHOR NOTES

### For Story 1 (Haaland/Manchester City):
**Specialty:** Sports reporting, Premier League coverage, fantasy sports analysis  
**Expertise Required:** Football/soccer knowledge, statistical analysis

### For Story 2 (Iran/Hormuz/Sanctions):
**Specialty:** Geopolitical reporting, international relations, trade/economics  
**Expertise Required:** Understanding of sanctions, maritime law, international policy

### For Story 3 (Karoline Leavitt/White House):
**Specialty:** Political reporting, government personnel, Trump administration coverage  
**Expertise Required:** Knowledge of White House operations, political transitions

### For Story 4 (Tropical Depression Moke/Weather):
**Specialty:** Weather reporting, disaster news, emergency management  
**Expertise Required:** Understanding of NOAA forecasts, meteorology basics, public safety

### For Story 5 (Navy Sailor Father/Immigration):
**Specialty:** Military news, immigration policy, human interest stories  
**Expertise Required:** Knowledge of military deployment, immigration law, USCIS procedures

---

## OPTIONAL: MULTIPLE AUTHORS

If stories have multiple authors or editors:

### Co-Author Format:
```
By: [Author 1] and [Author 2]
Edited by: [Editor Name]
Contributing Research: [Researcher Name]
```

### Contribution Levels:
```
Lead Author: [Name]
Contributing Author: [Name]
Fact-Checker: [Name]
Editor: [Name]
```

---

## IMPLEMENTATION CHECKLIST

### Before Publication:

- [ ] Author name confirmed and approved
- [ ] Author bio written and reviewed
- [ ] Author email/contact verified
- [ ] Social media handles verified
- [ ] Author photo (if using) obtained and optimized
- [ ] Byline format applied to all 5 articles
- [ ] Schema markup added to article headers
- [ ] Author page created (if applicable)
- [ ] Author bio proofread for accuracy
- [ ] Social media credit templates prepared
- [ ] All links to author resources tested

### After Publication:

- [ ] Bylines display correctly on website
- [ ] Author page ranks in search results
- [ ] Social sharing includes author credit
- [ ] Reader comments can reference author
- [ ] Author email receives inquiries (if public)

---

## AUTHOR CREDENTIALS FOR EACH STORY

### Recommended Author Types:

**Story 1 (Sports):**
- Sports journalist or sports reporter
- Experience with Premier League coverage
- Knowledge of Fantasy Premier League ecosystem

**Story 2 (Geopolitical):**
- International affairs reporter
- Geopolitical analyst
- Middle East/Asia policy specialist

**Story 3 (Politics):**
- Political reporter or correspondent
- White House or U.S. politics beat
- Knowledge of Trump administration

**Story 4 (Weather):**
- Weather reporter or meteorologist
- Disaster/emergency coverage specialist
- Public safety communication background

**Story 5 (Military/Immigration):**
- Military correspondent
- Immigration policy reporter
- Human interest/investigative reporter

---

## FINAL NOTES

- **Author consistency:** Use the same name format across all 5 stories if single author
- **Credentials matter:** Bylines establish credibility; ensure author matches story topic
- **Transparency:** Always disclose author and publication date
- **Updates:** Note if story has been updated after initial publication
- **Contact:** Provide author email only if author desires public contact

---

**Document Status:** TEMPLATE READY FOR AUTHOR ASSIGNMENT  
**Next Step:** Fill in author details and implement bylines across all 5 articles  
**Timeline:** Complete before final publication
