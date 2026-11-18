# Karmactive: Stage 2 First Drafts

**Batch date:** 18 November 2026
**Source:** Stage 1 plan (Stages 1a and 1b)
**Status:** Internal first drafts. Do not publish until the checks in each entry are cleared.

---

## Batch status (Step 9 publishing order)

| # | Story | Status | Reason |
|---|---|---|---|
| 1 | Iran strikes on US air bases in Kuwait and Bahrain | **HOLD** | No November 17–18 attack found. The documented strikes are from June and July 2026. |
| 2 | Classified JWICS / NSA network outage | **HOLD** | No outage found in searches. The whole premise is unconfirmed. |
| 3 | FBI ARTEX AI tool warning | **DRAFT** | FBI alert confirmed (issued November 13). Unconfirmed details removed. |
| 4 | Outages hit flights, banks and tech | **DRAFT (narrowed)** | Four outages confirmed on different dates. FAA stop was November 13, not November 17. |
| 5 | Apple and Marriott cloud outage | **HOLD** | Apple sign-in outage found (November 10). No Apple Pay or Marriott impact found. |
| 6 | DOJ VA benefits fraud crackdown | **HOLD** | No DOJ sweep or Houston defendant found. |
| 7 | Orange County deputy on leave over ICE conversation | **DRAFT** | Internal review confirmed in reporting dated November 14. |
| 8 | Fiona the hippo ate a hat | **DRAFT** | Zoo statement of November 16 confirmed. |
| 10 | Anne Hathaway and late pregnancy | **DRAFT (reframed)** | Pregnancy announced June 19, 2026. Birth not confirmed, so the headline changed. |
| 9 | Voyager 1 reaches one light-day | **DRAFT (timing-dependent)** | Crossing set for November 18. Confirm it before publishing. Distance corrected. |
| 11 | Leonid meteor shower peak | **DRAFT** | Peak of November 17–18 confirmed. Fireball and trail claims removed. |
| — | Canada Alert Ready test | **HOLD** | No November 18, 2026 test found. Not in the Step 9 ranking. |

**Ordering note:** Story 12 (Canada) has no Step 9 rank. Its header says "Priority 1," which Story 1 also carries. I left it last. Please confirm where it goes.

**Corrections to the Stage 1 brief**
- **Voyager 1 distance:** about 16.1 billion miles (25.9 billion km). The brief's 15.98 billion miles and 25.7 billion km do not match each other or its own calculation.
- **FAA ground stop:** Friday, November 13, not November 17.
- **Anne Hathaway:** the pregnancy was announced in June. No birth is confirmed.
- **Fiona's gap:** about one foot, per the zoo's account as reported. The brief says 3 inches.
- **Leonids:** the rate of about 15 an hour is an ideal-conditions figure. The Moon was up, so "moonless" is wrong. The brief's "8 to 12 fireballs per hour" contradicts its own 15 figure, so it is removed.
- **Story 4 internal link:** the Trump $50B air traffic control slug is not in Karmactive's sitemap. Replaced.

---

## 1. Iran strikes on US air bases in Kuwait and Bahrain. HOLD

**Not drafted as breaking news.** Two searches found no attack on Ali Al Salem (Kuwait) or Isa Air Base (Bahrain) dated November 17–18, 2026.

**Confirmed earlier in 2026:**
- **June:** Iran's Revolutionary Guard claimed strikes on Ali Al Salem and Sheikh Isa air bases. Kuwait's military said drones hit Kuwait International Airport's Terminal 1.
- **June:** US strikes on Qeshm Island were described by CENTCOM as "self-defense." The accounts of what was hit differ. CENTCOM said radar and command sites. Iran's Guard said telecom towers.
- **July 8:** the Guard claimed joint missile and drone attacks on US sites in Bahrain and Kuwait. A US official said US strikes hit Iranian air defenses and anti-ship missile sites.

**Brief claims not found:** 24 drones with 21 intercepted; the 03:15 strike time; the 14% freight premium; three tankers rerouted; "no US fatalities" from CENTCOM; closed civilian corridors; the analysis that Iran targeted logistics hubs rather than carrier groups.

**To unblock:** confirm a November 17–18 attack through CENTCOM or official Kuwaiti or Bahraini statements. If the attack is one of the June or July events, this is older news and its Step 9 rank should drop.

---

## 2. Classified JWICS / NSA network outage. HOLD

**Not drafted.** Two searches found no JWICS (Joint Worldwide Intelligence Communications System) outage in November 2026 and no NSA statement about one.

- The November 13 FAA ground stop was unrelated.
- Older background only: the NSA's 2000 network failure was a software problem, not an attack, according to the agency's own assessment. Do not use it as the story.

**Brief claims not supported:** the cryptographic key rotation cause, the "orphaned" domain controllers, the ODNI notice, the Pentagon CIO statement, the House committee inquiry, and the "no breach" finding.

**To unblock:** an official NSA, ODNI or Defense Department statement, or wire-service reporting, that confirms the outage, its dates and its cause.

---

## 3. FBI ARTEX AI tool warning. DRAFT

**Headline:** FBI ARTEX AI Tool Warning: How Hackers Use Open-Source AI for Machine-Speed Attacks

The FBI ARTEX AI tool warning applies to any company that runs cloud accounts or admin logins reachable from the internet. The FBI says criminals are using an open-source AI tool called ARTEX to break into networks. In some cases, the tool reached privileged access in under three hours. The advice is practical, and most of it comes down to reducing what is exposed online.

On November 13, 2026, the FBI issued a FLASH alert, a short, urgent notice sent to security teams. It covers ARTEX, an open-source framework built for autonomous penetration testing. Penetration testing means attacking your own systems to find weak spots before criminals do. ARTEX is written in the Go programming language and has no AI model of its own. Instead, it connects to outside large language models, the AI systems behind chatbots. Those include tools from Anthropic and OpenAI. The FBI says some intrusions moved from first targeting to privileged access in under three hours. Reported victims include companies in financial services, government, technology, defense and telecoms, plus law firms. Researchers counted between roughly 1,465 and more than 1,600 ARTEX management consoles exposed on the public internet.

If you manage cloud accounts, remote admin tools or AI agents that connect to company systems, the FBI's main advice is to shrink what faces the internet. Start by listing every login page, API address and admin console reachable from outside. Close or restrict any you do not need. Rotate any access keys that may have been exposed. Require phishing-resistant multi-factor sign-in for admin accounts. The last three steps are general security practice.

## How ARTEX Works and Why It Moves Fast

ARTEX works like a checklist that writes its own next step. The outside AI model reads what each action finds, decides what to try next and sends the next command. The FBI says that loop can run with little human intervention. Speed is the main concern. A three-hour window leaves little time for a person to notice an alert, investigate it and respond.

The tool's history is also complicated. Its developer reportedly made the code closed-source after attacks began. Copies still circulate through community forks, archived versions and localized editions. A commercial version, ARTEX PRO, also exists. Because copies are not limited to one country, organizations outside the United States face the same risk.

Coverage of the advisory links it to an October supply-chain attack. In a supply-chain attack, criminals compromise a trusted supplier to reach its customers. Reports say one such incident, involving ConnectWise Cloud Backup, gave hackers access to some Microsoft 365 customer environments.

Autonomous software is drawing scrutiny elsewhere too. Karmactive has reported on [complex autonomous software systems operating without human oversight](https://www.karmactive.com/tesla-blocks-austin-robotaxi-records-as-waymo-already-operates-in-city-and-nhtsa-investigates-safety/) in robotaxi testing, and on [sophisticated AI-driven automation increasingly deployed by malicious actors](https://www.karmactive.com/whatsapp-scam-alert-ai-feature/) in messaging scams.

ARTEX is an open-source AI framework built for penetration testing, which security teams use to probe their own networks for weak spots. Criminals have since repurposed it to run intrusions with little human help.

ARTEX has no AI model of its own, so blocking one AI provider is unlikely to stop it. The tool can connect to several models from different providers. That is our inference from how the tool is built, not a finding from the FBI. The more reliable defense is to fix the exposed systems the tool attacks.

The FBI says ARTEX can reach privileged access in under three hours. Its main advice is to find and reduce internet-facing systems now. Teams that have not mapped those systems yet should start this week, before an attacker does. Copies remain in circulation through forks and localized versions, so the risk is not limited to one country.

**Writer notes (not for publication):**
- **Length:** about 690 words against a 680 target. One subhead, placed before the depth block, matches the 500–800 word tier.
- **Confirmed:** FLASH date (November 13); Go language; connection to outside models; under-three-hour privileged access; victim sectors; exposed-console range; closed-source history, forks and ARTEX PRO; ConnectWise link as reported in coverage of the advisory; the FBI's top recommendation.
- **Removed as unverified:** 164-minute time-to-compromise; residential-proxy evasion; scans against utility control systems; the developer name; the claim that ARTEX rewrites commands from error logs; CISA mitigations; the threat-intelligence telemetry claims.
- **Links:** two included. Editor to confirm both linked articles support the sentences around them.
- **Regional angle:** the brief flagged the UK. No UK-specific facts were verified, so the article covers the point through the spread of copies. Add UK sourcing if the UK angle should be explicit.

---

## 4. Outages hit flights, banks and tech. DRAFT (narrowed)

**Headline:** Outages Hit Flights, Banks and Tech: Was It a Coordinated Attack?

Flights stopped, bank payments stalled, and Microsoft and Apple services went down within one week. Many people asked the same question: was someone running a coordinated attack on the country's systems? Here is what has been reported so far, with dates, and what officials and companies have said.

Four outages hit separate US services between November 10 and November 16, 2026. Apple reported a worldwide sign-in failure on Tuesday, November 10. It blocked access to iCloud, Mail, Calendar, Game Center and the App Store for roughly 90 minutes to just under two hours. Microsoft's Outlook, Teams and Copilot (its AI assistant) went down on Thursday, November 12. Microsoft said the outage followed a network change and an issue during a capacity upgrade. On Friday, November 13, the Federal Aviation Administration (FAA) ordered a nationwide ground stop, which halts departures, for about four hours. Chase's online banking and Zelle, a bank-to-bank payment service, were delayed on Monday, November 16. Officials said they saw no sign of a coordinated attack behind the FAA stop.

If you bank with Chase or send Zelle payments, check pending transfers before you send the same payment again. Some payments held up during the delay may still go through, and resending could pay the same person twice. If you plan to fly, check your airline's app before you leave for the airport. The FAA lifted its ground stop the same evening, but disruption carried into the weekend.

## Four Separate Failures, One Shared Week

Each outage had its own reported cause, and some causes are still disputed. Transportation Secretary Sean Duffy blamed overloaded routers in a decades-old communications network. The FAA later pointed to an upgrade that moved part of its network from copper wire to fiber-optic cable at a communications node in Arkansas, according to coverage. Officials ruled out a link between the FAA stop and Microsoft's outage. Apple later said all of the affected services had been restored.

Chase's cause is also reported differently. One account said the bank blamed a software bug and not a cyberattack. Another said the fault was in its own data-center hardware. Chase has not said which systems failed or how many customers were affected. Early Warning Services, which runs Zelle, said its network was fully operational. It said delays came from the other side of some transfers.

Chase has had earlier problems. Karmactive has covered [earlier payment processing delays at JPMorgan Chase](https://www.karmactive.com/chase-software-bug-outage-zelle-delays/). Airline IT failures have also grounded flights before. [Alaska Airlines' IT outage and the FAA ground stop that followed](https://www.karmactive.com/alaska-airlines-it-outage-faa-ground-stop-cancellations-oct-24-2025/) is one example.

Many online services share parts of the internet's infrastructure, such as login systems, network routing and cloud hosting. When one shared part fails, problems can spread to services that look unrelated. That is a general point about modern systems, not a finding about these four events.

Was the US hit by a coordinated cyberattack? Nothing in the public reporting so far shows one. Officials said they saw no sign of a cyberattack behind the FAA stop. The four incidents hit different companies, different systems and different days.

Each outage hit a different company's systems, and they happened across six days. That spread makes the week look like a single event. Read one at a time, each has its own reported cause. That is our inference about why the questions spread. It is not an official finding.

Four outages in one week hit flights, bank payments and tech services. The FAA's cause is still disputed, and Chase has not said which systems failed. Check pending payments before you resend them, and check flight status before you travel.

**Writer notes (not for publication):**
- **Length:** about 720 words against a 750 target. One subhead, before the depth block.
- **Date corrections:** FAA stop moved from November 17 to November 13. Microsoft outage placed on Thursday, November 12. Apple sign-in outage (November 10) added, since the brief omitted it.
- **Removed as unverified:** the CISA, ODNI and DHS joint statement; the "30-year-old multiplexer"; the "five outages, four stacks" count; the Microsoft and JPMorgan "micro-patch" causes; the conspiracy framing; the bipartisan Senate scrutiny; the 24–48 hour settlement delays.
- **Links:** the Trump $50B air traffic control slug is not in the sitemap, so it was replaced with the Alaska Airlines article. The brief's anchor for the Chase article said "multi-day"; the neutral anchor used here avoids that claim. Editor to confirm the Chase article's content.
- **Attribution:** every claim about cause is attributed. Keep it that way in edits.

---

## 5. Apple and Marriott cloud outage. HOLD

**Not drafted as written.** Searches found an Apple outage, but not the one the brief describes.

- **Found:** an Apple sign-in outage on Tuesday, November 10, 2026. It was reported worldwide and affected iCloud, Mail, Calendar, Contacts, Game Center and the App Store. Apple's status page logged it from 5:49 p.m. ET. Reports put the duration at roughly 90 minutes to 1 hour 46 minutes. Apple later said all outages were resolved.
- **Not found:** an Apple Pay impact on November 10 (the reports do not list it); an Apple Pay failure on November 17; the 08:45 ET configuration change; any Marriott digital-key or check-in problem.
- **Dedup:** Karmactive's sitemap already has an article titled "Apple Pay global outage hits 3,000 users." The brief says NEW. Check before drafting.

**To unblock:** an Apple statement or status history covering Apple Pay on the stated date, plus a Marriott statement. If only the November 10 sign-in outage holds up, the story is eight days old and needs a new angle rather than a breaking draft.

---

## 6. DOJ VA benefits fraud crackdown. HOLD

**Not drafted.** Two searches found no DOJ VA benefits sweep in November 2026, no Houston prosthetics indictment, and no record of the named defendant.

**Related but different:**
- The DOJ's National Fraud Enforcement Division was created on April 7, 2026.
- A multi-week DOJ fraud sweep was reported, with no clear dates.
- The June 2026 National Health Care Fraud Takedown included a VA Office of Inspector General portion tied to about $21.4 million in VA losses.
- A Florida defendant pleaded guilty to receiving about $250,000 in VA benefits.
- An October 2026 case charged 15 people in a $2 billion health care fraud scheme. It involved Medicare and private insurance, not VA benefits.

**Brief claims not verified:** the 15 defendants, the Houston press conference, the $182,000 total, the 1,437 transactions, the November 2020–August 2025 period, and the defendant's role.

**To unblock:** the DOJ press release and the Southern District of Texas indictment. Do not name the defendant until the court record is checked.

---

## 7. Orange County deputy on leave over ICE conversation. DRAFT

**Headline:** California Sheriff's Deputy Placed on Leave After Video Shows Conversation With ICE Agents

If you live in California, you may be asking whether local officers are helping federal immigration agents. A surveillance video from an Orange County jail has raised that question. The sheriff's department has opened an internal investigation into two of its employees.

The Orange County Sheriff's Department placed a deputy and a sheriff's special officer on administrative leave after surveillance video showed them talking with Immigration and Customs Enforcement (ICE) agents outside the jail in Santa Ana. The footage is from October 31, 2026. It shows the two employees leaving the building and speaking with the agents for about five seconds. The agents were in an unmarked black SUV parked on a public street. A second vehicle arrived shortly after the employees left. The agents then entered a public courtyard and arrested a man who appeared to be hiding there, the department said. A family member identified him as Jesús Esparza. NBC Los Angeles reported that he had been visiting his son at Men's Central Jail.

If you live in California, the state's SB 54 law still sets the rules for how local officers can work with immigration agents. SB 54, also called the California Values Act, has applied since 2018. This case tests how those rules apply to contact outside a jail. It does not change the law. The internal review will decide whether the two employees broke department policy or state rules. No findings had been announced as of the latest reporting.

## The Boundaries of California's SB 54 Sanctuary Law

SB 54 limits what local agencies can do to help immigration enforcement. Local staff generally cannot use public resources to assist federal immigration agents. Local jails generally cannot hold people on immigration requests alone. The law also restricts sharing non-public information, such as release dates, with immigration agents. Lawsuits over local involvement in immigration enforcement have been filed in other cases, including [civil rights claims and municipal legal challenges surrounding immigration enforcement](https://www.karmactive.com/carlos-jimenez-ice-lawsuit-25-million-2/).

The open question here is location. The contact happened in a public area outside the jail, not inside it. Whether a brief conversation outside a jail counts as using local resources is what the review has to answer. Federal courts are also ruling on immigration detention rules, as [a recent appeals court ruling on detention without bond](https://www.karmactive.com/5th-circuit-ice-detention-without-bond-immigration-ruling-2026/) shows.

Why was the Orange County sheriff's deputy placed on leave? The department placed a deputy and a sheriff's special officer on administrative leave after video showed them speaking with ICE agents outside the jail. Administrative leave means time away from duty while a review is underway. The department opened a personnel investigation to determine whether the conversation tipped off agents.

The man arrested was a visitor, according to reporting, not someone being held in the jail at the time. That raises a question the reporting has not answered: whether SB 54's limits apply to people who are visiting rather than in custody.

The department has placed two employees on leave and opened an internal investigation. No findings have been announced. SB 54 has applied in California since 2018. The outcome of the review will show how state rules apply to contact outside a jail.

**Writer notes (not for publication):**
- **Length:** about 555 words against a 500 target. The SB 54 explanation is kept because the depth block needs it. Trim if needed.
- **Confirmed:** the October 31 incident; about five seconds of conversation; unmarked black SUV on a public street; second vehicle; arrest in a public courtyard; administrative leave; personnel investigation; the detainee had been visiting his son.
- **Removed as unverified:** Sheriff Don Barnes statements and quotes; the detainee's age; the "Santa Ana Intake Release Center" name; the "58 counties" claim; the "never booked" claim; the Board of Supervisors inquiry; any finding of an SB 54 violation.
- **Naming decision for the editor:** the article names the arrested man, based on a family member's identification reported by Telemundo and NBC Los Angeles. Choose between naming him and describing him as "a man."
- **Legal check:** the SB 54 points (no holds on immigration requests alone; limits on sharing release dates) come from general knowledge of the statute, not from its text. Verify with the statute or counsel before publishing.
- **Links:** the Jimenez article is relevant. The brief's second link (a Meta fine) is off-topic, so it was replaced with the Fifth Circuit detention article from the sitemap.

---

## 8. Fiona the hippo ate a hat at Cincinnati Zoo. DRAFT

**Headline:** Fiona the Hippo Eats Hat at Cincinnati Zoo: Health Update and What Happens Next

Fans of Fiona, the Cincinnati Zoo's best-known hippo, want to know whether she is okay after swallowing a knit hat. The zoo says she is under round-the-clock veterinary watch. Staff hope she will pass the hat without intervention. Here is what the zoo has said so far.

The Cincinnati Zoo & Botanical Garden said on November 16, 2026, that Fiona is receiving veterinary care after swallowing a knit hat that got into her enclosure. A visitor tossed the hat into the air near her habitat at Hippo Cove. A ceiling fan caught it and sent it through a one-foot opening above the viewing windows, the zoo said. Fiona is off exhibit while the situation is resolved. The zoo's care team is "cautiously optimistic that she will pass it and return to her usual self."

If you are following Fiona's recovery or planning a visit, check the zoo's website or social media first. Fiona is off exhibit for now, and the zoo says it will share updates as it learns more. Keep hats, bottles and phones away from railings and open windows.

Visitor behavior around hippos has drawn attention before. A viral baby hippo at another zoo prompted concern over [visitor behavior and animal safety at high-profile zoological exhibits](https://www.karmactive.com/as-baby-hippo-moo-deng-goes-viral-with-2-8-million-tiktok-fans-khao-kheow-zoo-struggles-with-visitor-misconduct-and-animal-safety/). Captive hippo care depends on [specialized captive hippo veterinary care and habitat management protocols](https://www.karmactive.com/endangered-pygmy-hippo-born-at-virginia-zoo-a-rare-addition-to-the-fewer-than-2500-left-in-the-wild/) that keep both animals and guests safe. Vets watch appetite, droppings and behavior closely, because those signs help them decide whether an object will pass on its own.

How is Fiona the hippo doing after eating a hat? Fiona is under round-the-clock veterinary watch at the Cincinnati Zoo. Staff are cautiously optimistic that she will pass the knit hat without intervention. She remains off exhibit, and the zoo says it will post updates as it learns more.

A playful toss, a ceiling fan and a narrow opening above the glass combined to send the hat into the enclosure. The zoo's spokesperson said such an event would be hard to repeat on purpose. "We probably couldn't make that happen again if we tried," the spokesperson said. "It was clearly an accident."

Fiona remains under veterinary care, and the zoo has not announced surgery. The zoo says it will share updates on its channels as the situation develops. For now, the outcome depends on whether the hat passes.

**Writer notes (not for publication):**
- **Length:** about 430 words against a 420 target. No subheadings, as the under-500 rule requires.
- **Confirmed:** the zoo's November 16 statement; the knit hat; the visitor toss; the ceiling fan; the one-foot opening; off-exhibit status; "cautiously optimistic"; the spokesperson's "clearly an accident" quote.
- **Removed as unverified:** laxatives, fiber feeding and fluids; normal appetite and output; "no impaction"; the November 15 ingestion date; Dr. Mark Campbell; the 24-hour framing (the zoo said round-the-clock); visitor safety rules.
- **Check before publishing:** the brief's 3-inch gap conflicts with the one-foot figure in coverage. Confirm against the zoo's own bulletin.
- **Links:** both are relevant. Editor to confirm the anchor sentences fit.

---

## 10. Anne Hathaway and late pregnancy. DRAFT (reframed)

**Headline:** Is Late Pregnancy a Myth? What Doctors Say After Anne Hathaway's Third Pregnancy Announcement

Is late pregnancy a myth? No, but it becomes much less common with age. Anne Hathaway's third pregnancy has people asking how likely a natural pregnancy is after 40. Here is what medical experts say, in plain terms.

Anne Hathaway announced in June 2026 that she is pregnant with her third child. She shared the news on June 19 in a social media video showing her baby bump. Her husband, Adam Shulman, is the father. The couple already has two sons, Jonathan, 10, and Jack, 6. Hathaway turned 44 on November 12, 2026. Later, she said paparazzi photos had effectively forced the couple's hand, so they chose to announce it themselves. As of this writing, no birth announcement has been confirmed.

If you are in your 40s and planning a pregnancy, timing matters more than many people expect. Fertility falls with age, and the decline speeds up after 35. Medical guidance generally says to see a doctor sooner if you are over 35, and sooner again if you are over 40. Waiting a full year before asking for help may be too long for many women in that age group.

## Is Late Pregnancy a Myth? What the Science Says About Conception Over 40

Natural conception gets harder with age. Think of the ovaries' egg supply as a savings account that does not refill. Both the number of eggs and their quality decline. Eggs also carry more chromosome errors as women age, which raises the risk of miscarriage. [VERIFY: current ACOG figure for natural conception chance per menstrual cycle at age 40 and above.]

Births to women aged 40 to 44 have risen since 1990. [VERIFY: CDC/NCHS birth figures and year.] Part of that rise reflects fertility treatment and egg freezing, which let some women conceive at older ages. [VERIFY: share of births to women over 43 that involve assisted reproductive technology, from the CDC ART report.]

Celebrity pregnancies can make natural conception after 40 look common. Medical experts usually describe it as possible but uncommon. Once a baby arrives, [clinical guidance and healthcare protocols surrounding infant wellness and perinatal safety](https://www.karmactive.com/newborn-vitamin-k-shot-refusals-infant-bleeding-surge-2/) also shapes how newborns are cared for.

Can you get pregnant naturally at 44? Yes, a natural pregnancy at 44 is possible, but it is uncommon. Fertility declines with age, and the chance of chromosome problems in eggs rises. Many pregnancies at this age use fertility treatment, such as IVF or donor eggs. A doctor can estimate your own chances through testing.

Public figures often have access to IVF, egg freezing or donor eggs. Those options can make a pregnancy at 44 look more typical than it is for most women. This is our inference from how these stories are usually told, not a finding from a study.

Late pregnancy is possible, but it becomes less common with age. Hathaway's announcement has drawn attention to the question. If you are over 35 and trying to conceive, a fertility check can help you decide your next step.

**Writer notes (not for publication):**
- **Length:** about 580 words against a 600 target. The three VERIFY markers must be filled from primary sources, which will add about 60 words.
- **Headline changed:** the brief said "welcomes baby at 44." No birth is confirmed. The June 19 pregnancy announcement is confirmed.
- **Age:** 44 comes from Hathaway's birth date (November 12, 1982), taken from background knowledge, not from the searches (June coverage said 43). Verify before publishing.
- **Removed as unverified or likely wrong:** the "buzzer-beater" Seth Meyers claim; the newborn chest-carrier sighting; "more than 65% of births over 43 use ART or frozen eggs" (not verifiable, and likely wrong); the "births up 130% since 1990" figure (replaced with a VERIFY marker); the "three months of trying" rule (replaced with general guidance; check ACOG's exact wording).
- **Links:** only one relevant link was found in the brief's list. The standing-study link is off-topic and was dropped. Add a second fertility or maternal-health article from the sitemap.
- **UK angle:** the brief flagged the UK. No UK data is included. If the UK angle stays, add data from the UK fertility regulator (HFEA) before publishing.

---

## 9. NASA's Voyager 1 reaches one light-day from Earth. DRAFT (timing-dependent)

**Headline:** Voyager 1 One Light Day From Earth: The Science Behind the Historic Milestone

Voyager 1 is set to reach one light-day from Earth today, November 18, 2026. That means a radio message sent from Earth now would take a full day to arrive. Earlier estimates pointed to November 13 and November 15, and the date has since moved to today. Here is what the milestone means, and what it does not change.

One light-day is the distance light covers in 24 hours. That works out to about 25.9 billion kilometers, or roughly 16.1 billion miles. It is about 173 times the distance from Earth to the Sun. Voyager 1 launched in September 1977. It is the first human-made object to reach this distance, according to coverage of the milestone. Published timings differ slightly. One set puts the crossing at 06:16 UTC (Coordinated Universal Time) on November 18, and another at 10:16 UTC. At the time of writing, a confirmed crossing had not been reported.

If you follow the mission, expect long delays. A command NASA sends today takes about 24 hours to reach the spacecraft, and the reply takes about 24 hours to return. Voyager 1 is still transmitting, but most of its instruments have stopped working. NASA turned off one instrument in April 2026 to save power. Updates are likely to be slow and limited.

## Orbital Mechanics: How Voyager 1 Overtook Voyager 2

Voyager 1 is now farther out than its twin, Voyager 2, even though it launched after it. Voyager 2 launched 16 days before Voyager 1. Engineers sent Voyager 1 on a faster, flatter path. That route passed close to Jupiter and Saturn's moon Titan, but it gave up the close visits to Uranus and Neptune that Voyager 2 later made. Voyager 2 is projected to reach the same distance around 2035. Radio messages travel at the speed of light, so the delay is fixed by distance. The team has worked through [extreme electrical constraints and previous deep space communication recovery efforts](https://www.karmactive.com/nasas-voyager-1-returns-to-full-operations-after-signal-loss-while-operating-on-razor-thin-power-margins/) before.

How far is one light-day from Earth in miles? One light-day is about 16.1 billion miles, or 25.9 billion kilometers. Light covers that distance in exactly 24 hours in a vacuum. No other human-made object has traveled this far.

Voyager 1 still sends data across more than 16 billion miles, but its power is shrinking. Its generators run on plutonium that decays over time. NASA has had to shut off instruments to stretch what is left. Managing aging generators on interstellar probes is an ongoing task, as [the technical management of aging radioisotope thermoelectric generators on interstellar probes](https://www.karmactive.com/nasa-powers-down-voyager-2-plasma-instrument-what-this-means-for-the-12-8-billion-mile-journey/) shows.

Voyager 1 reaches one light-day from Earth today, after launching in 1977. The crossing does not change anything physical about the spacecraft. It marks a distance no other human-made object has reached. Voyager 2 is expected to follow around 2035.

**Writer notes (not for publication):**
- **Length:** about 620 words against a 620 target. One subhead, before the depth block.
- **Corrected:** the distance. The brief's 15.98 billion miles and 25.7 billion km do not match its own calculation of 2.59 × 10^10 km.
- **Removed as unverified:** the 220-watt power figure; the 160-bit telemetry packet claim; the "cryogenic receivers" claim; the JPL forecast of telemetry into 2028.
- **Publish condition:** do not publish until NASA or JPL confirms the crossing. Two UTC times are in circulation, so keep the time generic unless confirmed. If confirmed, change "set to reach" to "reached" and update the headline.
- **Follow-up framing:** the hook now shows the new date. The brief says a November 15 Karmactive article previewed the event. I did not verify that article, so do not link back to it until it is confirmed.

---

## 11. Leonid meteor shower peak. DRAFT

**Headline:** Leonid Meteor Shower Peak November 2026: How to Still Catch Shooting Stars This Week

Missed the Leonid meteor shower peak overnight? You can still catch shooting stars this week. The Moon is up, so the sky will not be perfectly dark. Here is how and when to look.

The Leonid meteor shower peaked overnight on November 17 and 18, 2026. Under ideal dark skies, it produces about 15 meteors an hour. That figure is a zenithal hourly rate, or ZHR, meaning the count an observer would see under perfect conditions. Typical forecasts run from 10 to 15 an hour. The meteors come from comet 55P/Tempel-Tuttle and appear to spread out from the constellation Leo. They hit the atmosphere at about 71 kilometers per second. The Moon was up for much of the night, which hides fainter meteors. No major outburst was predicted for 2026.

If you missed the peak, you can still look this week. Activity stays low into late November, so expect fewer meteors each night. For the best chance, go somewhere dark, away from street lights. Give your eyes about 20 minutes to adjust. The hours before dawn are best, after the Moon has set.

Meteors appear across the whole sky, including areas far from the radiant in Leo. Meteors close to the radiant look short, because they fly almost straight toward you. Looking away from Leo gives a wider view. Lie back on a blanket for the widest view. Keep phone screens dim, since bright light reduces night vision. Karmactive has also covered [rare astronomical night-sky viewing opportunities and cometary debris observations](https://www.karmactive.com/skywatchers-get-ready-comet-nishimuras-400-year-return-lights-up-the-night/).

What is the best time to see the Leonid meteor shower? The best time is the hours before dawn, after the Moon has set and the sky has darkened. The shower peaked overnight on November 17 and 18. Activity is lower through late November, so the early-morning hours still offer the best odds.

Many people stare straight at Leo, the radiant. That is not the best spot. Meteors near the radiant look short and foreshortened. Looking away from it gives longer streaks across the sky, which are easier to follow.

The Leonids peaked overnight on November 17 and 18, but the shower is not over. A dark, wide view and patience give you the best odds. Expect fewer meteors than at the peak, and dress warmly for late-night viewing.

**Writer notes (not for publication):**
- **Length:** about 440 words against a 430 target. No subheadings, as the under-500 rule requires.
- **Removed as unverified or contradictory:** "8 to 12 fireballs per hour" (contradicts the 15 ZHR figure); the 45-degree and green-trail direction advice; the Mars and Jupiter pairing; the "waxing moon sets by 00:15" timing; the "active through November 30" end date (replaced with "late November," so check the IMO end date); the 2032–2033 storm cycle.
- **Corrected:** the brief called the sky "moonless." The Moon was up. Moon illumination estimates disagree (roughly 41% to 53%), so no percentage is given.
- **Links:** both are relevant. Editor to confirm the anchor sentences fit.

---

## 12. Canada Alert Ready test, November 18, 2026. HOLD

**Not drafted.** Two searches found no Alert Ready test for November 18, 2026, and no provincial schedule for that date.

**Found:**
- Nationwide Alert Ready tests on Wednesday, November 19, 2025, and Wednesday, May 6, 2026. Quebec was excluded from the May test.
- Reporting says the CRTC requires at least one test a year, and that each province decides whether to take part.
- The brief's date may be a mix-up with the November 19, 2025 test. That is a guess, not a finding.

**Brief claims not supported:** the November 18 date; the provincial times (9:55 a.m. NST and the rest); "mandatory" nationwide testing; the silent-mode vibration claim; the "78% of alerts were weather" figure; the claim that only LTE-connected phones receive alerts; the opt-out answer.

**To unblock:** an official Alert Ready or Pelmorex notice naming November 18, 2026 and listing times by province, checked on alertready.ca. Confirm before drafting, because the window is hours long. If there is no notice, drop the story.

---

## Final check against the brief

- **Banned words:** scanned before saving. The drafts use none of the listed phrases.
- **Attribution:** every disputed claim is attributed to the reporting or the official who made it.
- **Unverified facts:** removed from the drafts, or marked VERIFY, or the whole story held. None is presented as fact.
- **Internal links:** all links use slugs confirmed in the Karmactive sitemap, except the Trump slug, which was replaced.
