# Stage 2 — First Draft Articles (Stage 3B Corrected)
**Date:** September 17, 2026 | **Site:** Karmactive.com

---

---

# ARTICLE 1 — US-CHINA AI ARMS RACE

**Search headline:** US-China AI arms race raises one question: what guardrails could Trump and Xi actually agree on?

**Social headline:** The US and China are racing on AI, but can they agree on rules for the most dangerous systems?

**Meta:** US-China AI competition is intensifying as leaders face pressure to establish guardrails for military AI, autonomous systems and critical infrastructure.

---

The question worth asking before the Trump-Xi meeting is not whether the US and China can sign a sweeping AI treaty. It's whether they can agree on a far narrower set of rules before the competition produces a crisis no one intended.

As the two governments prepare for September 2026 talks, AI governance has emerged as a prominent issue in discussions surrounding the planned Trump-Xi meeting, alongside trade, technology and chip controls. The pressure to establish some kind of shared framework is growing from multiple directions, including international bodies and research institutions that have spent years trying to define what agreement is even possible.

The immediate backdrop is a competition that neither side shows signs of slowing. The US has restricted advanced chip exports to China while pushing domestic AI development. China has accelerated its own investment. Both countries are developing and integrating AI for military applications, while researchers and policymakers are debating whether governance mechanisms are keeping pace.

**What a narrow agreement could actually look like**

The most concrete proposals in circulation do not attempt to govern the entire AI sector. They focus on military AI — specifically, where humans must stay in control and where AI-enabled systems should not be allowed to operate without human authorisation.

Researchers involved in a Brookings-Tsinghua Track II dialogue have proposed that both governments commit to keeping humans responsible for any decision involving attacks on nuclear command systems and critical infrastructure. They also propose establishing crisis-management mechanisms so that if autonomous systems behave in unexpected ways, the two sides have a direct channel to communicate before a situation escalates.

Those proposals are not yet government policy on either side. They are proposals from researchers for a narrower set of safeguards that could provide a starting point for bilateral discussions.

UN Secretary-General António Guterres has pressed for AI guardrails at the international level, calling for frameworks that are safe, transparent and accountable. The UN has established an Independent International Scientific Panel on AI to provide scientific evidence to support AI governance discussions. Neither mechanism is a substitute for direct agreement between Washington and Beijing, but both reflect the scale of pressure on governments to act.

Researchers argue that both countries have an interest in reducing the risk of accidental escalation involving AI-enabled military systems. That shared logic is precisely why military AI safeguards — rather than broader AI governance — may be the only place where real progress is possible in the short term.

**What both sides have not agreed on**

The harder questions concern everything beyond crisis communication and nuclear-adjacent systems. AI development timelines, data access, model training, civilian applications and the definition of "dual-use" AI remain contested at every level. Chip controls are a continuing source of tension rather than a foundation for cooperation.

The September meetings are unlikely to resolve all of those deeper disagreements, particularly where the two governments' technology and security interests diverge. What they might produce is an acknowledgment that military AI, at minimum, requires human control over the most consequential decisions. That would be a starting point, not a solution — but a starting point is what the current situation lacks.

Further reporting will clarify the governments' positions as official statements emerge.

---

---

# ARTICLE 2 — CISCO SECURE EMAIL GATEWAY VULNERABILITY

**Headline:** Cisco Secure Email Gateway zero-day hits 9.8 severity as attackers gain root-level access

**Meta:** Cisco's CVE-2026-76461 carries a 9.8 severity rating and can give unauthenticated attackers root-level access through malicious email processing.

---

If your organisation runs Cisco Secure Email Gateway, there is a patching decision to make now, not later. Cisco has confirmed a critical vulnerability that lets an unauthenticated attacker execute commands with root-level access — and says there is no workaround.

CVE-2026-76461 is a SQL injection flaw in the AsyncOS email-parsing function of Cisco Secure Email Gateway. Cisco classifies the vulnerability as Critical and assigns it a CVSS base score of 9.8. The attack path does not require credentials: an attacker can reach root-level command execution by sending a malicious email to an affected system.

Cisco's advisory confirms active exploitation in the wild. It provides fixed software and says customers should move to patched versions immediately. Cisco says no workaround is available and directs customers to fixed software.

**What IT administrators need to do**

Organisations running Cisco Secure Email Gateway should identify affected versions through Cisco's advisory and apply the available software fix. Given the email-based attack vector, security practitioners should not treat perimeter filtering as a substitute for applying Cisco's fixed software.

The Cisco advisory makes clear that this is an email-parsing issue, not a configuration problem. Affected Secure Email Gateway installations that process incoming email may be exposed, depending on the affected software version. Cisco's advisory identifies affected software and fixed releases.

Separate from CVE-2026-76461, Cisco issued a September 2026 hardening release for Identity Services Engine covering a different set of vulnerabilities, including authentication bypass and remote code execution. Administrators managing both products should treat these as separate patching exercises. The ISE vulnerabilities have their own CVEs and their own fixed-software requirements. Combining the two into a single remediation plan risks missing specific version requirements for each product.

The most important distinction for administrators is that CVE-2026-76461 affects Cisco Secure Email Gateway only. The ISE advisory does not apply to that product, and the email gateway advisory does not apply to ISE.

**What is CVE-2026-76461?**

CVE-2026-76461 is a critical SQL injection vulnerability in Cisco Secure Email Gateway's AsyncOS email-parsing functionality. Cisco assigns it a CVSS score of 9.8. An unauthenticated remote attacker can execute arbitrary commands with root privileges by sending a specially crafted email. Cisco states there is no workaround and directs customers to fixed software versions listed in the security advisory.

Cisco's security advisories are available directly through its security advisory portal. Organisations with active support contracts should consult their Cisco account team if they need assistance identifying their software version or planning the upgrade.

---

---

# ARTICLE 3 — ATO SHADOW ECONOMY CRACKDOWN

**Headline:** ATO shadow economy crackdown sends prosecutions up 80% as fines pass $2.7 million

**Meta:** ATO data shows more than 350 successful shadow-economy prosecutions over two years, with court fines exceeding $2.7 million.

---

The Australian Taxation Office has released figures showing that non-lodgment prosecutions increased by more than 80% over the past two years — and the consequences for those found guilty go well beyond the tax owed.

More than 350 individuals and entities were successfully prosecuted over the past two years. Courts imposed more than $2.7 million in fines across those cases. More than 305 resulted in convictions. The ATO has been running a dedicated shadow-economy enforcement campaign that covers unreported income, cash payments used to avoid tax obligations, and failures to lodge returns or meet superannuation requirements.

For affected businesses and individuals, the result of a criminal conviction is not simply a fine. The ATO says the consequences of conviction can extend beyond fines, affecting a person's reputation, professional life and, in some cases, the future of a business.

**Where prosecutions are concentrated**

The geographic breakdown shows that enforcement activity is not spread evenly across Australia. Queensland accounted for 28% of successful non-lodgment prosecutions. Western Australia came in at 26%. New South Wales was responsible for 20% and Victoria for 17%. Together, Queensland, WA and NSW made up nearly three-quarters of all cases.

The ATO defines shadow-economy activity as economic activity deliberately hidden from authorities. That covers a wide range of conduct: businesses taking cash payments and not declaring them, workers being paid off the books, and entities failing to lodge tax returns or pay compulsory superannuation. The common thread is that the income, activity or obligation is deliberately kept out of the official record.

The practical question for small-business operators and self-employed individuals is where the ATO's enforcement focus lands. Non-lodgment — failure to file a tax return — is one of the most commonly prosecuted categories. The ATO previously reported receiving 250,000 community tip-offs about tax avoidance and dishonest behaviour between July 2019 and October 2024, reflecting the scale of community reporting that feeds its enforcement work.

**What counts as shadow economy activity in Australia?**

The ATO uses the term for economic activity deliberately hidden from authorities, including undeclared income, cash payments designed to avoid tax obligations, and failures involving tax or superannuation. Its current enforcement campaign includes non-lodgment prosecutions, with more than 350 successful prosecutions reported over the past two years. A conviction can carry consequences beyond fines, including effects on business viability.

The ATO has indicated that shadow-economy enforcement will remain a priority. Small-business operators and sole traders should review whether income, lodgment obligations, employee payments and superannuation contributions are fully compliant.

---

---

# ARTICLE 4 — NEIL GEHRING / OLYMPIC NATIONAL PARK

**Headline:** Missing Olympic National Park hiker Neil Gehring found dead after two-week search

**Meta:** Neil Gehring was reported missing after a planned cross-country Olympic National Park traverse; search teams later recovered his body.

---

Neil Gehring, a 26-year-old hiker who went missing in Olympic National Park on August 31, has been found dead. Search-and-rescue teams recovered his body from the northwest slope of Mount Appleton on September 13, after investigators analysed additional cellphone location data. His body was transferred to the Clallam County Coroner's Office at approximately 8 p.m. that evening.

Gehring left the Madison Falls Trailhead on August 31 with a planned cross-country route: from Boulder Lake to Appleton Pass and back to Madison Falls. He was reported overdue on September 2 at 6:30 a.m. The National Park Service launched a search involving aerial teams, ground crews, drones and dogs.

As the search continued, the NPS said investigators were seeking new clues and asked the public for any relevant information. The investigation remained ongoing at the time of that update.

The route Gehring had planned was a cross-country traverse, not a marked-trail outing. That distinction matters for anyone trying to understand the search geography and the scale of the operation the NPS undertook over nearly two weeks.

The NPS has not released a cause of death. The investigation is ongoing. Any details about the circumstances of his death should come from official NPS or law-enforcement releases.

NPS advises hikers to leave a trip plan with a trusted person and carry appropriate navigation and emergency equipment.

---

---

# ARTICLE 5 — CANYON GRAIL CF SLX 7 DI2

**Headline:** Canyon Grail Gen 3 brings 57mm tyres to a race-focused gravel bike with a $4,999 CF SLX model

**Meta:** Canyon's third-generation Grail adds 57mm tyre clearance, aero updates and Shimano GRX Di2, with the CF SLX 7 Di2 priced at $4,999.

---

The tyre clearance question in gravel racing has a new reference point. Canyon has increased the maximum tyre clearance from 42mm on the previous generation to 57mm on the new model, while keeping the design explicitly aimed at race-pace aerodynamics.

The 2027 Grail launches with three model tiers: CF SLX, CFR and CF. The CF SLX 7 Di2 is the most accessible of the carbon builds, priced at $4,999 in the US. It comes with Shimano GRX Di2 electronic shifting, Canyon GR 50 CF carbon wheels and 45mm Schwalbe G-One R tyres. Listed weight is 21.08 lb (9.56 kg). The drivetrain is one-by.

For riders deciding whether the jump from a previous-generation Grail or a competitor is worth making, the 57mm clearance is the number that changes the calculation. At 57mm (2.25 inches), the new version can take tyres that were previously the territory of adventure or bikepacking bikes, while Canyon says it retained aerodynamic performance benchmarked at 35 km/h.

**What the 57mm clearance actually means on a race bike**

The aerodynamic development target matters as much as the clearance number itself. Canyon says the new bike was benchmarked for aerodynamic performance at a 35 km/h gravel-racing pace. The frame is not simply a more capable all-rounder — it is designed to accommodate larger tyres without sacrificing the aerodynamic properties that matter in a gravel race.

The PACE Bar, Canyon's adjustable handlebar system, allows riders to change the cockpit width and flare angle without replacing bars or stem. That adjustability is useful for riders who compete on courses ranging from fast gravel roads to rougher terrain requiring a wider, more stable hand position.

At $4,999 for the CF SLX 7 Di2, the new Grail sits in a competitive price bracket against Specialized, Trek and other manufacturers offering comparable electronic-shifting gravel bikes. The CF SLX frame is one of Canyon's carbon construction tiers; the CFR sits above it in the range for riders prioritising maximum weight savings.

Canyon sells directly online in the US, so buyers purchase through Canyon rather than through a traditional dealer.

The practical question for a gravel cyclist considering the CF SLX 7 Di2 is not whether 57mm clearance is better than 42mm in the abstract. It's whether the courses they race require that volume, and whether the aerodynamic benchmark at 35 km/h is relevant to their actual race speeds. For riders who spend most of their race time on smoother fast gravel, the clearance increase may be more headroom than they use. For riders tackling rougher terrain where tyre choice was previously a compromise, the new clearance removes a constraint that the previous generation imposed.

**What is new on the Canyon Grail Gen 3?**

The third-generation Grail increases maximum tyre clearance from 42mm to 57mm, introduces an aero design benchmarked at 35 km/h and updates the frame geometry across the range. The CF SLX 7 Di2 comes with Shimano GRX Di2 electronic shifting, Canyon GR 50 CF carbon wheels and 45mm Schwalbe G-One R tyres at a listed US price of $4,999. The PACE Bar adjustable cockpit system is included across the range.

Canyon confirmed availability through its direct online sales channel in the US and other markets at launch.

---

---

# ARTICLE 6 — BOTOX / OCD / BODY DYSMORPHIC DISORDER

**Headline:** NICE launches consultation on updated BDD and OCD guidance but wanting Botox does not mean you have OCD

**Meta:** NICE has opened a consultation on updated OCD and BDD guidelines; existing NICE guidance already asks clinicians to consider BDD in some cosmetic patients, but wanting Botox does not mean someone has OCD.

---

If you've seen headlines suggesting that wanting Botox means you have OCD, that is not what the NICE guidance says. The actual clinical recommendation is more specific — and more limited — than most of the coverage implies.

NICE opened a public consultation on September 17, 2026 on updated OCD and body dysmorphic disorder (BDD) guidelines, with final publication expected in February 2027. Existing NICE guidance (CG31) already recommends that healthcare professionals consider BDD in people at higher risk of the condition, and in people seeking cosmetic or dermatological procedures under specified circumstances. Where BDD is suspected or diagnosed, NICE recommends assessment by a suitably experienced mental-health professional.

That recommendation is conditional and professional-facing, not a blanket statement about cosmetic treatment patients. It does not say that wanting Botox, fillers or other cosmetic procedures is evidence of a mental-health condition. It says that clinicians should consider whether BDD is present in certain higher-risk groups.

BDD is a recognised condition in which a person becomes preoccupied with a perceived physical flaw — often one that others cannot see or consider minor — to a degree that causes significant distress or interferes with daily life. It is distinct from general dissatisfaction with appearance, and it is distinct from the decision to have a cosmetic procedure.

**What the NICE guidance actually requires**

The existing guidance recommends that professionals use specific assessment questions when BDD is a concern, and refer for specialist mental-health assessment where it is suspected or diagnosed. It does not require a psychological assessment for all cosmetic patients. The focus is on identifying people who may be experiencing significant distress linked to body image in a way that could affect the appropriateness of a cosmetic procedure for them specifically.

For patients considering Botox or other cosmetic treatments, the practical implication is that a clinician may ask about body image and how a patient feels about their appearance. That is not an accusation of mental illness — it is part of a clinical picture that good practice already encourages.

The current situation is that existing NICE CG31 guidance is in place, while an updated guideline is under development through the consultation that opened today. The cosmetic screening element is one component of the broader OCD and BDD clinical framework, not the purpose of the guidance as a whole.

**Does wanting Botox mean you have OCD?**

No. NICE guidance does not say that wanting Botox means a person has OCD. It recommends that clinicians consider possible body dysmorphic disorder in certain people seeking cosmetic or dermatological treatment, particularly those at higher risk. Suspected BDD should be assessed appropriately rather than inferred from a person's decision to seek cosmetic treatment. OCD and BDD are separate conditions, though they share some features.

The NICE guidance is available in full through the NICE website for patients who want to read the specific recommendations rather than rely on media summaries of them.

---

---

# ARTICLE 7 — FEDERAL RESERVE RATE HIKE

**Headline:** Fed raises interest rate to 3.75%-4% as inflation remains elevated

**Meta:** The Federal Reserve raised its benchmark rate by 25 basis points to 3.75%-4%, citing elevated inflation and resilient economic activity.

---

The Federal Reserve has raised its benchmark interest rate by a quarter of a percentage point, bringing the federal funds target range to 3.75%-4%. The decision came from a unanimous 12-0 vote by the Federal Open Market Committee.

The Fed's statement says inflation remains elevated and that the rate increase supports returning inflation to the Committee's 2% target over time. It also says domestic spending is resilient, productivity growth is strong and capital investment is robust — conditions the Committee used to justify holding policy at a restrictive level rather than holding or cutting.

For US borrowers and savers, the rate level matters more than the size of this particular move. At 3.75%-4%, the federal funds rate remains well above where it sat through most of the decade before 2022. That level feeds through to credit cards, auto loans, home equity lines of credit, and adjustable-rate mortgages — products that reprice relatively quickly when the policy rate changes. Fixed-rate mortgages move more independently, tracking long-term bond yields rather than the Fed's overnight rate directly.

**What the rate level means for borrowers and savers**

Variable-rate debt — including most credit cards and many home equity products — tends to follow the federal funds rate with a short lag. Borrowers with variable-rate debt can be affected by changes in the federal funds rate, although the timing and size of the effect vary by product.

Savers in high-yield deposit accounts and money-market funds have benefited from the same rate environment. Rates on those products have been meaningfully higher than they were during the near-zero rate era. Whether that continues depends on the Fed's next moves.

The 12–0 vote means none of the FOMC members who voted at the meeting dissented from the decision. In recent years, FOMC decisions have sometimes drawn dissents from members who wanted faster or slower action.

President Trump has publicly called for lower interest rates on multiple occasions. The Fed's statement does not mention Trump's calls for lower rates and instead cites inflation and economic conditions.

The Fed's next scheduled meeting will provide the next formal opportunity to reassess the rate path. Markets will be watching upcoming inflation data closely for signs of whether further increases are likely or whether the current rate is sufficient to bring inflation back to target.

**What did the Fed do and why?**

The Federal Reserve raised its federal funds target range by 25 basis points to 3.75%-4% at its September 2026 meeting, with a 12-0 unanimous vote. The Fed's statement cites elevated inflation and resilient economic activity as the basis for the decision. The rate increase is aimed at returning inflation to the Committee's 2% goal. The practical effect on consumers depends on the type of debt or savings product and how quickly each reprices in response to the policy rate.

---

---

# ARTICLE 8 — SO DELICIOUS FROZEN DESSERT RECALL

**Headline:** So Delicious frozen dessert recalled over possible stones as FDA lists affected UPC and dates

**Meta:** FDA says select So Delicious Salted Caramel Cluster frozen dessert pints may contain small stones or hard objects; check the UPC and best-by date.

---

Check your freezer before opening that pint. Danone USA has issued a voluntary recall of So Delicious Dairy Free Salted Caramel Cluster Non-Dairy Frozen Dessert, and the FDA has confirmed the recall covers specific products that may contain small stones or other hard objects.

Here are the details you need to check the label:

- **Product:** So Delicious Dairy Free Salted Caramel Cluster Non-Dairy Frozen Dessert pints
- **SKU:** 136603
- **UPC:** 744473476138
- **Affected best-by dates:** on or before April 3, 2028
- **Distribution:** US retail stores

If your pint matches all three identifiers — SKU 136603, UPC 744473476138 and a best-by date on or before April 3, 2028 — do not eat it. The FDA notice says the potential foreign material consists of small stones or other hard objects associated with the cashew inclusions in the product.

No other So Delicious products are included in this recall. The FDA notice is explicit: no other codes, flavours or product lines are affected. If you have a different flavour or a different UPC, it is not part of this recall.

**What to do with the recalled product**

Consumers should not eat the affected product and should contact So Delicious Dairy Free Consumer Care for a replacement coupon or refund.

The recall was announced voluntarily by Danone USA on September 15, 2026. FDA confirmation followed the standard reporting process for voluntary food recalls.

**Which So Delicious ice cream is recalled?**

The recall covers So Delicious Dairy Free Salted Caramel Cluster Non-Dairy Frozen Dessert pints with SKU 136603, UPC 744473476138, and best-by dates on or before April 3, 2028. No other So Delicious products or flavours are included. Check your label against all three identifiers before deciding whether your product is affected.

---

---

# ARTICLE 9 — SEAN COMBS ATTORNEYS SEEK WITHDRAWAL

**Headline:** Sean Combs lawyers seek withdrawal from $100 million case amid unpaid-fee dispute

**Meta:** Attorneys in Sean Combs' $100 million defamation lawsuit are seeking court approval to withdraw, citing allegations of unpaid fees.

---

Lawyers representing Sean Combs in a $100 million defamation lawsuit have asked the court for permission to withdraw from the case, with a civil attorney alleging Combs has not paid legal fees for more than six months.

The firm has filed to withdraw; the court must address the request before the firm formally exits the case. Describing them as having already left the case would overstate where the proceedings currently stand.

The defamation lawsuit in question is separate from the criminal proceedings Combs faces. The $100 million civil case involves defamation claims, and the withdrawal motion relates specifically to the civil representation.

Combs has disputed the lawyers' characterisation, saying he chose to switch lawyers because he believed bills were excessive or included charges he had not approved.

The unpaid-fee allegations are claims made by the attorneys in their withdrawal filing, not findings by the court. The court has not adjudicated whether fees are owed or in what amount.

Coverage of the Combs civil and criminal matters continues to develop. The outcome of the withdrawal motion will be determined by the presiding judge.

---

---

# ARTICLE 10 — LENA DUNHAM WELCOMES DAUGHTER VIA SURROGACY

**Headline:** Lena Dunham welcomes first child with Luis Felber after sharing surrogacy journey

**Meta:** Lena Dunham has announced the birth of her first child with Luis Felber, sharing her journey to motherhood and surrogacy in a Vogue essay.

---

Lena Dunham has announced the birth of her first child, a daughter, with her husband Luis Felber. The announcement came through a personal essay published in Vogue, in which Dunham describes the path to parenthood and what it meant to prepare for a child through surrogacy.

The baby arrived 13 days late, according to Dunham's own account. The Vogue essay is the first-person source for the announcement, written in Dunham's voice and covering the emotional experience of becoming a mother, including meeting the surrogate who carried her daughter.

Dunham, 40, is best known for creating and starring in the HBO series Girls, which ran from 2012 to 2017.

Felber is a British-Peruvian musician. The couple married in 2021. This is the first child for both of them.

Dunham's account centres on the surrogacy journey and the preparation for parenthood rather than providing clinical or medical detail. The article should take the same approach: report what Dunham herself described, without adding medical or fertility context that she did not include in her own announcement.

---

---

# ARTICLE 11 — STELLANTIS / CHINESE EVS / LEAPMOTOR

**Headline:** Stellantis deepens Chinese EV strategy through Leapmotor partnership as global auto markets split

**Meta:** Stellantis already holds about 21% of Leapmotor and operates a 51%-49% joint venture expanding the Chinese EV brand outside Greater China.

---

The debate about whether Chinese electric vehicles will reshape Western auto markets often misses what is already in place. Stellantis is not evaluating a Chinese EV partnership — it built one. The question now is how far it goes.

Stellantis became Leapmotor's single largest shareholder in October 2023, acquiring approximately 21% of the Chinese EV maker. At the same time, the two companies launched Leapmotor International, a joint venture structured as 51% Stellantis and 49% Leapmotor. That JV holds exclusive rights to sell and manufacture Leapmotor products outside Greater China.

Leapmotor recorded 103,129 global deliveries in August 2026, up 80.72% year over year. Those numbers include Greater China, where Leapmotor operates independently of the JV. The international expansion through Leapmotor International is a separate track — one that Stellantis controls through its majority stake.

**What the Leapmotor structure means for Stellantis**

The corporate mechanism matters because it is often described in more speculative terms than the actual structure warrants. The arrangement is a joint venture with Stellantis holding 51%, rather than a conventional licensing agreement. It holds majority control of the entity that has exclusive distribution and manufacturing rights for Leapmotor products outside China. That is a direct route to EV product deployment in Europe and other markets.

The partnership gives Stellantis another route to deploy Leapmotor vehicles and components in markets outside Greater China. How that affects individual Stellantis brands remains a separate strategic question.

Stellantis has described global automotive markets as increasingly differentiated, while its current strategy includes partnerships intended to improve competitiveness and accelerate vehicle development.

The Leapmotor JV has been expanding into European markets through 2025 and 2026, with vehicles being offered through Stellantis dealer networks in several countries. That distribution infrastructure — built on decades of Stellantis market presence in Europe — is part of what Leapmotor International gains from the partnership that Leapmotor alone could not quickly replicate.

What that means for individual Stellantis brands specifically depends on decisions the company has not publicly confirmed. The Leapmotor partnership provides capability and product access. How Stellantis deploys that across Jeep, Citroën, Opel, Peugeot or other marques remains a strategic choice, not an announced plan. Claims that Chinese EVs will "save" or "rescue" particular Stellantis brands are not supported by what the company has disclosed — the structure supports product deployment, not a branded rescue programme.

**Does Stellantis own Leapmotor?**

Stellantis is Leapmotor's largest single shareholder with approximately 21% of the company. It also holds 51% of Leapmotor International, the joint venture with exclusive rights to sell and manufacture Leapmotor products outside Greater China. Stellantis does not own Leapmotor outright — Leapmotor is a publicly listed Chinese company — but it holds a controlling stake in the international distribution and manufacturing venture.

---

---

# STAGE 3B CORRECTIONS APPLIED — CHANGE LOG

## Article 1
- "one of the most contested items on the agenda" → "a prominent issue in discussions surrounding the planned Trump-Xi meeting"
- "at a pace that makes governance difficult to keep up with" → "while researchers and policymakers are debating whether governance mechanisms are keeping pace"
- "They represent what researchers believe is a realistic floor — the minimum both countries could accept without conceding anything fundamental about their own AI programs." → "They are proposals from researchers for a narrower set of safeguards that could provide a starting point for bilateral discussions."
- "An independent international scientific panel on AI has been established to provide the kind of evidence base that policy negotiations typically need." → "The UN has established an Independent International Scientific Panel on AI to provide scientific evidence to support AI governance discussions."
- "Both the US and China have an interest in preventing an accidental escalation triggered by an AI system making a decision no human authorised." → "Researchers argue that both countries have an interest in reducing the risk of accidental escalation involving AI-enabled military systems."
- Removed: "neither government has shown willingness to accept inspections or transparency mechanisms that would let the other confirm compliance." (unsupported sweeping claim)
- "The September meetings will not resolve those deeper disagreements." → "The September meetings are unlikely to resolve all of those deeper disagreements, particularly where the two governments' technology and security interests diverge."
- "The outcome of the Trump-Xi discussions on AI is expected to become clearer in the days following the September meeting. Updates will follow as the official positions develop." → "Further reporting will clarify the governments' positions as official statements emerge."

## Article 2
- "That score places it in the highest tier of severity." → "Cisco classifies the vulnerability as Critical and assigns it a CVSS base score of 9.8."
- "There is no configuration change or network control that removes the risk on its own." → "Cisco says no workaround is available and directs customers to fixed software."
- "Relying on perimeter controls to block exploitation is not a substitute for patching, given that the attack vector is email — traffic that most network configurations are designed to accept." → "Given the email-based attack vector, security practitioners should not treat perimeter filtering as a substitute for applying Cisco's fixed software."
- "which means any system that receives external email is potentially exposed." → "Affected Secure Email Gateway installations that process incoming email may be exposed, depending on the affected software version. Cisco's advisory identifies affected software and fixed releases."

## Article 3
- "criminal prosecutions for shadow-economy activity have increased by more than 80%" → "non-lodgment prosecutions increased by more than 80%"
- "over 2024–25 and 2025–26" → "over the past two years"
- "It can affect business licensing, access to finance, insurance and the ability to continue operating." → "The ATO says the consequences of conviction can extend beyond fines, affecting a person's reputation, professional life and, in some cases, the future of a business."
- Tip-off reference reframed: "The ATO previously reported receiving 250,000 community tip-offs about tax avoidance and dishonest behaviour between July 2019 and October 2024, reflecting the scale of community reporting that feeds its enforcement work." (removed implication it was recent/causal to 2026 figures)
- "A conviction can carry consequences beyond fines, including effects on business viability and access to finance." → removed "access to finance" (not in primary source)

## Article 4
- Added specific recovery details from NPS: northwest slope of Mount Appleton, September 13, Clallam County Coroner's Office, approximately 8 p.m.; body found after cellphone location data analysis
- Removed generic cross-country terrain safety paragraph (not specific to this incident)
- "the NPS recommends filing a detailed trip plan with rangers, carrying appropriate navigation equipment and having a clear turnaround time that triggers a welfare check if missed." → "NPS advises hikers to leave a trip plan with a trusted person and carry appropriate navigation and emergency equipment."
- Removed editor's note (verification gap now resolved)

## Article 5
- "a combination that the previous generation couldn't offer." → "Canyon has increased the maximum tyre clearance from 42mm on the previous generation to 57mm on the new model"
- "It runs Shimano GRX Di2 electronic shifting, Canyon GR 50 carbon wheels and 28-inch wheels." → "It comes with Shimano GRX Di2 electronic shifting, Canyon GR 50 CF carbon wheels and 45mm Schwalbe G-One R tyres." (removed incorrect "28-inch wheels")
- Removed: "At 42mm, the previous Grail sat at the narrower end of the gravel-race segment." (unsupported comparative)
- "That means the designers were not simply making the bike more capable at lower speeds with bigger tyres — they were trying to keep aerodynamic drag competitive at the speeds gravel racers actually ride." → "Canyon says the new bike was benchmarked for aerodynamic performance at a 35 km/h gravel-racing pace."
- "The PACE Bar, Canyon's adjustable handlebar system, is carried over from the previous generation and allows riders to change the cockpit width and flare angle without replacing bars or stem." → removed "is carried over from the previous generation and" (unverified claim)
- "The CF SLX frame is Canyon's mid-tier carbon construction;" → "The CF SLX frame is one of Canyon's carbon construction tiers;" (removed editorial "mid-tier" characterisation)
- "what the website shows is what you pay." → "Canyon sells directly online in the US, so buyers purchase through Canyon rather than through a traditional dealer."
- PAA block updated: "The CF SLX 7 Di2 adds Shimano GRX Di2 electronic shifting and Canyon GR 50 carbon wheels" → "comes with Shimano GRX Di2 electronic shifting, Canyon GR 50 CF carbon wheels and 45mm Schwalbe G-One R tyres"; "The PACE Bar adjustable cockpit system continues from the previous generation." → "The PACE Bar adjustable cockpit system is included across the range."

## Article 6
- Headline changed: "New UK cosmetic guidance raises BDD screening questions..." → "NICE launches consultation on updated BDD and OCD guidance but wanting Botox does not mean you have OCD" (existing CG31 is not new guidance; what is new is the consultation opened September 17, 2026)
- Meta updated to reflect consultation status
- Opening: "not what the new guidance says" → "not what the NICE guidance says"
- Second paragraph rewritten to correctly distinguish existing CG31 guidance from the new consultation (opened September 17, 2026, publication expected February 2027)
- Removed unsourced sentence: "The UK's aesthetic industry has faced increasing pressure to improve screening processes following cases where patients with undiagnosed BDD received procedures that worsened their distress rather than relieving it."
- "NICE's OCD and BDD guidance forms part of a broader set of clinical standards on how mental-health conditions intersect with physical health care. The cosmetic screening element is one component, not the purpose of the guidance as a whole." → "The current situation is that existing NICE CG31 guidance is in place, while an updated guideline is under development through the consultation that opened today. The cosmetic screening element is one component of the broader OCD and BDD clinical framework, not the purpose of the guidance as a whole."
- "The guidance recommends..." → "The existing guidance recommends..." (precision)

## Article 7
- "Borrowers carrying balances on those products are already feeling the effect of the rate increases the Fed has made over the past two years, and this move extends that period of elevated borrowing costs." → "Borrowers with variable-rate debt can be affected by changes in the federal funds rate, although the timing and size of the effect vary by product."
- "The unanimous 12-0 vote removes any ambiguity about internal dissent." → "The 12–0 vote means none of the FOMC members who voted at the meeting dissented from the decision."
- "but the decision makes clear that the Committee is following its own assessment of inflation and economic conditions." → "The Fed's statement does not mention Trump's calls for lower rates and instead cites inflation and economic conditions."

## Article 8
- "Danone's standard recall guidance is to discard the product or return it to the store where it was purchased for a full refund. Check with the retailer directly if you have questions about the return process." → "Consumers should not eat the affected product and should contact So Delicious Dairy Free Consumer Care for a replacement coupon or refund." (matches FDA/company actual instructions)
- Removed: "There is no indication at this stage that any injuries have been reported, but the FDA advises consumers to act on the recall information regardless." (not stated in primary source)
- Removed: "Consuming hard foreign objects in food can cause dental or other injuries." (generic safety claim not in primary source)

## Article 9
- "the lawyers have asked to leave, but a judge must grant the request before the withdrawal takes effect." → "The firm has filed to withdraw; the court must address the request before the firm formally exits the case."
- Removed: "Multiple law firms have faced similar situations in high-profile matters where a client's ability or willingness to pay becomes an issue during extended litigation." (irrelevant and unsupported)
- Removed: "If the court grants the withdrawal, Combs would need new civil representation for the defamation matter or would proceed without counsel, which courts generally allow but typically seek to avoid in complex civil litigation. A judge considering a withdrawal motion weighs the attorney's right to be paid against the potential disruption to the proceedings." (unsourced general legal claims)
- Added: "Combs has disputed the lawyers' characterisation, saying he chose to switch lawyers because he believed bills were excessive or included charges he had not approved." (balance required; sourced to Just Jared/reported response)

## Article 10
- Removed entire endometriosis/fertility history paragraph (unnecessary sensitive medical context not from current Vogue announcement)
- "Felber is a British musician." → "Felber is a British-Peruvian musician." (factual correction per LA Times)
- Removed speculative closing sentence: "This is breaking entertainment news. As with most celebrity birth announcements, further details — including the daughter's name, if Dunham and Felber choose to share it publicly — may follow in subsequent reporting."

## Article 11
- Subheading: "What the Leapmotor structure means for Stellantis brands" → "What the Leapmotor structure means for Stellantis" (removed "brands" given speculative brand-level claims removed)
- "Stellantis does not simply license Leapmotor technology or source vehicles at arm's length. It holds majority control..." → "The arrangement is a joint venture with Stellantis holding 51%, rather than a conventional licensing agreement. It holds majority control..."
- "For Stellantis brands like Jeep, Citroën and Opel, the question of how Chinese EV technology enters their lineups is partly strategic and partly structural. Leapmotor International gives Stellantis a vehicle — literally and organisationally — to deploy EV products that it does not have to develop from the ground up." → "The partnership gives Stellantis another route to deploy Leapmotor vehicles and components in markets outside Greater China. How that affects individual Stellantis brands remains a separate strategic question."
- Removed entirely: "Stellantis CEO Carlos Tavares has acknowledged that global auto markets are splitting, with competitive dynamics in Europe and the US diverging from each other and from China. Chinese EV makers, led by BYD and others, have achieved cost structures that established Western and Japanese automakers have struggled to match. For Stellantis, the Leapmotor partnership offers a path to competitive EV products in markets where its own development pipeline may be too slow or too expensive." (Tavares is no longer CEO; cost structure claim unsourced; development pipeline claim speculative)
- Replaced with: "Stellantis has described global automotive markets as increasingly differentiated, while its current strategy includes partnerships intended to improve competitiveness and accelerate vehicle development."

## Internal links
All articles retain placeholder notes for 2–4 internal Karmactive URLs to be inserted at publication. Actual URLs cannot be verified until supplied; link verification remains a pre-publication step.

## Process check
- All 11 articles reviewed sentence by sentence against Stage 3A findings
- Every flagged correction applied
- No sentences changed that did not require a correction
- No new facts introduced beyond what Stage 3A verified sources establish
- Banned words: none present
- Environmental angle: not applicable across all 11, correctly maintained
