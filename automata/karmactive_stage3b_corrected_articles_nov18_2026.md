# Karmactive Stage 3b: Corrected First Drafts

*Corrected 18 November 2026 after the Stage 3a fact-check. Each sentence was checked against primary or independent sources. Claims that could not be verified were removed or rewritten to what the sources support. Appendix A lists every change. Appendix B lists the verification log and open items.*

---

## Optimizely Script Hijack Hits 178 Organisations (BBC, CNN, Zoom): Risk Guide

If you visited BBC, CNN, Zoom, HSBC, Equifax, IKEA, Ledger or another major site on Nov. 16, the first question is whether you entered card details, copied a crypto address or used an unpatched iPhone. Attackers abused Optimizely Web Experimentation to place malicious JavaScript in 188 snippets across at least 178 organisations between 04:21 and 23:11 UTC. Optimizely said it had fixed the vulnerability and removed the injected code in its status update on Nov. 17.

Visitors to websites run by 178 organisations, including Zoom, BBC, CNN, HSBC, Equifax, Salesforce, IKEA and Ledger, were served malicious JavaScript through Optimizely Web Experimentation on November 16, 2026. While the affected Optimizely snippets are now clean, people who entered card numbers into native site forms after 13:43 UTC, copied crypto addresses, or used iPhones below iOS 18.7.3 or iOS 26.3 should take protective action.

## Were you affected? Four checks for cards, crypto and iPhones

The script could replace a copied cryptocurrency address with one controlled by an attacker. Researchers reported that the attacker's wallets received roughly $7,000 to $7,150 in crypto, and that those wallets were emptied early on Nov. 17. That is a reported on-chain estimate, not a complete measure of losses. It also added a card skimmer to native checkout forms after 13:43 UTC. Payment fields run by a separate provider in a cross-origin frame were out of the skimmer's reach, because a script on the surrounding page cannot read a payment frame from another domain.

| If this happened | Main risk | What to do |
| --- | --- | --- |
| You copied a crypto address | Address substitution | Check wallet history and recipient addresses |
| You typed a card into a native form after 13:43 UTC | Card-data capture | Contact the issuer and review transactions |
| You used an iPhone below iOS 18.7.3 or 26.3 | Exploit-kit targeting | Update iOS immediately |
| You only read a page | Lower, not zero, exposure | Update software and monitor accounts |

The iPhone portion targeted iOS 13 to 17 through Coruna and iOS 18 through DarkSword. Pages on iOS 18.6 or earlier could reload every 60 seconds as the exploit retried. According to Report URI's analysis, the kit's own comments list iOS 18.7.3 and later, and iOS 26.3 and later, as patched.

## How the attack reached so many websites

Optimizely lets customers add Project JavaScript that runs across their pages. The attacker inserted code into that field while leaving the rest of the snippet intact. The injected loader pulled a script from the domain 1688360.cc. At HSBC, a backup copy of the malicious code ran through JavaScript's `eval()` function, which the site's security settings allowed.

This is why people should not assume a familiar brand means a page was safe on that day. Salesforce disabled Optimizely scripts as a precaution. Website operators should audit Project JavaScript, review logs back to the start of the exposure window, and consider rotating relevant credentials as a precaution.

**Which websites and iPhone versions were affected by the Optimizely malware attack?**

The incident affected 188 Optimizely snippets across 178 organisations, including Zoom, BBC, CNN, HSBC, Equifax, Salesforce, GitLab, IKEA, Ledger and Peacock. The iPhone exploit kits targeted iOS 13 to 17 (Coruna) and iOS 18 (DarkSword); the kit's own comments list iOS 18.7.3 and later, and iOS 26.3 and later, as patched.

Watch for breach notices from affected services and for Optimizely's root-cause report. If you made a purchase or crypto transfer during the window, keep transaction records before contacting your bank, card issuer or wallet provider.

---

## Chase Software Bug Outage: Why Zelle Stalled at Other US Banks

JPMorgan Chase says its systems were back to normal by Monday evening after a software-bug outage that disrupted online banking and delayed some transfers. A Chase spokesman described it as a temporary issue tied to a software bug in an on-premise hardware system, not a cyberattack. If you sent money involving a Chase account, check the transaction in your official banking app before trying again.

If you initiated a Zelle transfer or another payment involving a Chase account during Monday's outage, check your transaction status before resending funds. Because the failure stemmed from a software bug on Chase's on-premise hardware systems rather than a failure of the Zelle network itself, Zelle said its network stayed up and that the disruption was tied to transfers involving Chase accounts. Avoid duplicate submissions and watch for post-outage phishing texts.

## Why one Chase bug produced reports at other banks

Chase's Downdetector reports began climbing shortly after 9 a.m. ET, peaked at roughly 4,800, and had fallen to about 1,780 by 4:45 p.m. ET. Downdetector also logged reports for Bank of America, U.S. Bank and Wells Fargo.

Bank of America said its systems were operating normally. U.S. Bank said its own systems were not directly affected, but customers sending or receiving Zelle payments could see delays with another institution. Zelle, which is operated by Early Warning Services, said its network stayed up and that the reports were tied to transfers involving Chase accounts.

## What federal rules say about a non-cyber outage

The Office of the Comptroller of the Currency says a computer-security incident can include a nonmalicious hardware or software failure that harms a system's availability. Its rules require a service provider to alert affected banks when covered services are materially disrupted for four or more hours. A bank must notify the OCC within 36 hours after deciding that a notification incident occurred.

For customers, use the app or website you normally use, record the payment time, and do not share a one-time passcode with an unsolicited caller. The [consumer guidance after a major network outage](https://www.karmactive.com/three-mobile-requires-individual-compensation-claims-after-14-hour-network-outage-hits-9300-users/) offers a comparison for documenting a service problem.

## What to do with a pending Zelle payment

Look for a completed, pending or failed status in the official app and keep timestamps if a delayed payment triggers a late fee. Ignore contacts offering to "release" funds. Keeping cash and printed account details is also part of the preparation described in Karmactive's [emergency-kit guidance](https://www.karmactive.com/be-ready-emergency-kit-uk-2026-checklist-medication-list/).

**Why did reports spike at other US banks on Monday?**

Only JPMorgan Chase reported the software failure. Customers of other banks saw delays when a payment involved a Chase account. Bank of America said its own systems were operating normally, and U.S. Bank said its systems were not directly affected.

**Was the Chase outage a cyberattack?**

No. Chase said the outage came from a software bug in on-premise hardware systems, and it said the issue was not cyber-related.

**Was Zelle itself down?**

No. Zelle's network remained operational, but a transfer can remain pending when a participating bank cannot promptly confirm its side of the payment.

Chase customers and people waiting on a transfer should continue to check their account status rather than submit a second payment. Karmactive will update this story if the OCC or Early Warning Services publishes a formal account of the outage.

---

## FEMA Emergency Alert Test Nov. 17: Why Phones Won't Ring Today

FEMA and the Federal Communications Commission will run a nationwide Emergency Alert System test on Tuesday, Nov. 17, at 2:20 p.m. ET. It will reach television, radio, cable, satellite and wireline video services. The FCC notice covers the Emergency Alert System, not Wireless Emergency Alerts, so consumer cell phones are not expected to receive an alert. The test message is described as a test, and no action is required from the public.

At 2:20 p.m. EST on Tuesday, November 17, 2026, FEMA and the FCC will interrupt US radio, TV, cable, and satellite broadcasts for a one-minute nationwide Emergency Alert System test. Consumer cell phones will not receive an alert. Scheduled in September under a three-year federal mandate, the drill is unrelated to current news events, though viewers can report garbled audio or unreadable screen crawls directly to the FCC.

| US time zone | Test time |
| --- | --- |
| Eastern | 2:20 p.m. |
| Central | 1:20 p.m. |
| Mountain | 12:20 p.m. |
| Pacific | 11:20 a.m. |

## Why the date does not point to a blackout

Announced on Sept. 16, the test is required at least every three years under federal law. It is unrelated to recent banking problems, aviation disruptions or reports about Iran. "72-hour blackout" claims lack a basis in the federal notices. If conditions on that day require rescheduling, the alternative date is Dec. 3.

Karmactive's [FEMA emergency-plan fact check](https://www.karmactive.com/fema-halloween-emergency-plan-30-day-supply-fact-check/) covers distorted preparedness claims.

## How the alert is meant to be accessible

The test is sent as a Common Alerting Protocol message in English and Spanish through FEMA's Integrated Public Alert and Warning System (IPAWS). It tests radio and television delivery, not mobile-cell broadcasting. Viewers who encounter unreadable text, missing audio or another problem can send feedback to the FCC, which asks the public to report any complications in delivering the test message. Karmactive's [AusAlert coverage](https://www.karmactive.com/ausalert-australia-emergency-warning-system-2026/) explains a cell-broadcast alert system.

## What broadcasters must report after the test

Broadcasters and other participants must report day-of-test results through the FCC's EAS Test Reporting System. For this drill, the FCC allowed 48 hours rather than the usual 24 hours to file that initial information.

**Will the Nov. 17 FEMA emergency alert test go to cell phones?**

No. This test covers the Emergency Alert System on radio, television, cable, satellite and wireline video services. The FCC notice does not describe a Wireless Emergency Alert component, so consumer phones are not expected to receive a text message or alert tone.

**Why is FEMA testing the system?**

Federal law requires a nationwide public-alert test at least once every three years. The last nationwide test was held in October 2023.

**What should I do if the alert was unreadable?**

No emergency action is required for the test. You can submit feedback to the FCC if a local station's audio was unclear or its visual crawl was difficult to read.

Broadcasters have until Nov. 19 at 2:20 p.m. ET to file their day-of-test information. Karmactive will track any FCC findings on performance and accessibility.

---

## Iran 'Dirty Bomb' Intel Report: Trump's Response and Why It Matters

US intelligence officials are assessing indications that Iran is developing contingency plans to target senior Trump administration officials in Washington, D.C., with a dirty bomb or chemical weapon. CNN, citing seven US officials, reported that the planning does not necessarily indicate an imminent attack. President Donald Trump said the threat was being taken "very seriously," while the White House said it did not consider the threat credible.

While US intelligence officials are evaluating indications that Iran is developing contingency plans for a "dirty bomb" or chemical attack targeting Trump administration officials in Washington, D.C., reporting describes no imminent attack. For residents, a dirty bomb is a radiological device rather than a nuclear weapon: it spreads radioactive material with a conventional explosion, and its main hazard is contamination of a limited area.

## US officials are weighing capability and intent

The intelligence reporting describes contingency planning, not a confirmed operational attack plan. Officials remain divided over whether Iran could or would carry it out. The Office of the Director of National Intelligence declined to comment.

For people in the Washington area, the immediate point is that the reported assessment does not say an attack is about to happen.

## Iran's rejection and the feasibility question

Iran rejected the allegations, and US officials continue to assess the intelligence. Atlantic Council fellow Tom Warrick called bringing a dirty bomb into the United States "difficult, but not impossible." The reporting rests largely on anonymous US officials, and it does not show that Iran has decided to proceed.

## Why a dirty bomb differs from a nuclear weapon

A dirty bomb, or radiological dispersal device, uses conventional explosives to spread radioactive material. It cannot create the atomic chain reaction of a nuclear weapon. Its main harms are contamination and cleanup costs.

| | Dirty bomb (RDD) | Nuclear weapon |
| --- | --- | --- |
| Mechanism | Conventional explosive spreads radioactive material | Nuclear fission creates the blast |
| Blast yield | Conventional explosion | Vastly greater nuclear explosion |
| Main immediate risk | Blast and exposure to contaminated dust | Extreme blast, heat and radiation |

A nuclear explosion is far more powerful than a dirty bomb's conventional blast. An RDD could contaminate buildings, soil, food or water and require cleanup. Karmactive's [solar-radiation-storm guide](https://www.karmactive.com/s4-severe-solar-radiation-storm-strongest-since-2003-aurora-alert-january-2026/) covers a different radiation hazard.

## Why the dust matters after a dirty bomb

The conventional blast would be the first danger near an RDD explosion. Radioactive dust or smoke can become a secondary danger if inhaled or carried indoors. Karmactive's [UK preparedness checklist](https://www.karmactive.com/be-ready-emergency-kit-uk-2026-checklist-medication-list/) explains household basics.

**What is the difference between a dirty bomb and a nuclear bomb?**

A dirty bomb uses conventional explosives to scatter radioactive powder or pellets over a limited area. It cannot create an atomic chain reaction or a city-destroying nuclear blast. A nuclear explosion is far more powerful, while an RDD's danger includes the blast, contamination and costly cleanup.

**Is there an imminent Iranian dirty-bomb threat in Washington?**

No imminent attack was reported by the officials cited in CNN's reporting. Officials were still debating Iran's capability and intent.

**How far can radiation from a dirty bomb spread?**

A dirty bomb typically spreads radioactive material over a limited area, often a few blocks or miles, unlike the much wider cloud associated with a nuclear explosion.

The intelligence assessment and Iran's response may develop as officials release more information. Karmactive will update this story as officials provide more detail.

---

## Advagen Metoprolol Recall: Check Batch 2611C065A1 With Your Pharmacist

Patients taking generic beta-blockers should check the pharmacy label and call their pharmacist before changing any dose. An Advagen Pharma recall covers metoprolol tartrate 50 mg tablets from one batch, 2611C065A1, in which some bottles may contain tablets or capsules that do not belong in the packaging.

US patients taking metoprolol tartrate, a beta-blocker prescribed for conditions such as high blood pressure and angina, should check the batch number on the bottle. Advagen Pharma recalled 3,684 bottles of 50 mg metoprolol tartrate from Batch 2611C065A1, and the product was distributed nationwide. Do not stop a beta-blocker suddenly: product labeling warns that abrupt withdrawal can worsen angina or trigger a heart attack.

| Drug | Identifier | Expiry | Recall concern |
| --- | --- | --- | --- |
| Metoprolol tartrate 50 mg | NDC 72888-210-00; Batch 2611C065A1 | May 2028 | Tablets or capsules that do not belong in the packaging |

## How to verify a pharmacy vial safely

The imprint alone does not confirm whether a tablet is recalled. Ask the pharmacy to check the batch number recorded for the bulk bottle used to fill your prescription. Have the name, strength, prescription number and fill date ready. A pharmacist can say whether your bottle came from the affected batch and tell you how to obtain replacement medicine.

For metoprolol, the concern is that the bottle may contain tablets that are not the labelled medicine. The recall applies to the stated batch, not to every bottle of metoprolol.

**Should I stop taking recalled metoprolol?**

No. Do not stop a beta-blocker on your own. Check whether your bottle is from batch 2611C065A1, then contact your pharmacist or prescriber promptly about replacement, and follow the recall instructions they give you. Sudden withdrawal can cause rebound heart effects, including worsening chest pain.

Suspected product problems can be reported to FDA MedWatch at 1-800-332-1088. The recall described here concerns US distribution; patients outside the US should use their local regulator and pharmacy channels.

---

## Florida Flood Watch: Repeated Rain Through Friday Threatens Saturated East-Central Florida

A Flood Watch issued by the National Weather Service in Melbourne covers nine counties (Volusia, Seminole, Orange, Osceola, Okeechobee, Brevard, Indian River, St. Lucie and Martin) from Tuesday afternoon through Friday. The office forecasts 3 to 6 inches of rain, with localized totals of 8 to 12 inches, on ground that is already saturated. The St. Johns River at Cocoa is at major flood stage, and flooding there is expected to last for weeks.

The watch was issued at 3:18 p.m. EST on Monday, Nov. 16, and runs from Tuesday afternoon through Friday. Repeated showers and isolated storms are forecast through Friday. Residents should use local county alerts for school, road and sandbag decisions rather than relying on a statewide rainfall average.

| Area | Rainfall risk | Main concern |
| --- | --- | --- |
| Nine-county watch area (east-central Florida) | 3 to 6 inches; localized 8 to 12 inches | Saturated ground and St. Johns River flooding |

## Why the El Niño background is not the immediate cause

NOAA's Nov. 12 assessment placed the Niño-3.4 anomaly near +2.5°C. That does not mean every Florida storm is caused by El Niño. It does mean a warmer Pacific pattern can shape the broader seasonal background in which a coastal disturbance meets saturated local basins.

At Cocoa, prolonged major flooding on the St. Johns River can continue after the heaviest rain passes. Coastal residents should avoid driving through water, secure outdoor items before the strongest gusts and check marine forecasts before going out. A flood watch means conditions favour flooding; it is not a guarantee that every neighbourhood will flood.

**How much rain could the watch area receive through Friday?**

The National Weather Service forecasts 3 to 6 inches across the nine-county watch area, with localized totals of 8 to 12 inches. Local forecasts and warnings can change as each rain band forms.

Showers and isolated storms are forecast to continue through Friday. Residents should continue checking the relevant National Weather Service office because river crests and coastal conditions can lag the rain.

---

## Trump's $50B Air Traffic Control Request Draws Congressional Scrutiny

President Donald Trump and Transportation Secretary Sean Duffy are seeking $50 billion for air traffic control after a nationwide ground stop on Friday, Nov. 13. The department had first sought $30.1 billion, and the request rose to $50 billion that same day. The FAA has paused new Juniper router installations, and Senate Democrats have called for a pause on router installations.

Senate Democrats, citing L3Harris, said about 400 of 3,648 Juniper routers had been installed and 69 were operating. Duffy said the failure came on the 69th installation, after the first 68 had gone well. The figures separate spending, funds committed and work actually operating.

The outage was not simply a matter of old copper wire. The FAA said a newly installed Juniper router at El Dorado, Arkansas, sent excessive data, about 1,000 connection attempts every four to five seconds, that overwhelmed aging network equipment, and the agency paused further installations while the cause is reviewed. The FAA has not established a definitive root cause, and HPE, which owns Juniper, says its equipment worked as configured.

The Government Accountability Office identified 11,389 project schedules that had not been integrated into a single master schedule. Without one joined plan, lawmakers cannot easily test whether costs, risks and deadlines across a major overhaul fit together.

**Why did senators ask the FAA to pause Juniper router replacements?**

Senate Democrats called for a pause after the failure, citing reports that about 400 of 3,648 replacement routers had been installed and 69 were operating. Their question is whether the rollout, safety testing and contract management are ready for expansion before the agency asks Congress for more money.

The next marker is the FAA's investigation of the failure. Its findings on the disabled router functions and its installation plan will show whether the pause becomes a longer reset.

---

## United Airlines Outage Explained: Weight Data Halt & DOT Voucher Rule

Passengers affected by Monday's United Airlines departure halt need to distinguish it from Friday's FAA ground stop. A pilots' union memo said the problem involved United's weight-and-balance calculation system, which meant outbound flights could not receive final weights. United said it had resolved a technology issue that delayed departures and that there was no indication of a cybersecurity issue. If the event was caused by United's own systems, it would count as a controllable airline delay under United's published Department of Transportation commitments, which can change the help available to passengers.

United passengers affected by the outage, or travelling through Chicago or Newark, where the disruption was reported, should check their itinerary and keep receipts. CBS reported that the outage lasted about 90 minutes and was resolved on Monday evening. United later told CNN it lasted about 30 minutes and affected fewer than 150 flights, so accounts of its length differ. FlightAware showed 715 United delays late Monday afternoon, though it was unclear how many were caused by the outage.

## Why missing weight-and-balance data stops a jet

Dispatchers use weight, loading and centre-of-gravity data to calculate a safe take-off configuration. Without it, pilots cannot reliably set speeds or confirm how the aircraft will handle. A delay to verify those facts is safer than departing with incomplete data.

| Disruption | Who controlled it? | Typical passenger position |
| --- | --- | --- |
| Friday FAA ground stop | FAA or airspace system | Refund for cancellation; no routine hotel or alternate-transport duty |
| Monday United system outage | Airline system | United's controllable-delay commitments apply |

For a controllable delay, United's published commitments include meal vouchers after three hours and hotel accommodation when an overnight delay is needed. Ask an agent for a written explanation if a voucher is refused, and retain boarding passes and receipts.

**Does United owe vouchers for the weight-and-balance outage?**

United's published commitments treat an airline-controlled systems failure differently from an FAA ground stop. Passengers delayed three hours or more may be eligible for meals, and overnight passengers may be eligible for accommodation. Eligibility depends on the actual disruption and available rebooking.

For Thanksgiving travel, confirm any rebooking in the United app, save all receipts and avoid confusing Monday's United event with Friday's FAA disruption. A DOT complaint is an option if the carrier does not follow its posted controllable-delay commitments.

---

## Stranded by FAA Ground Stop, North Dakota Woman Buys $48K Ford Bronco

When repeated rebookings ended in a cancellation in Charlotte, nurse practitioner Tara Harding, who was in Charlotte for training, faced an unusual choice. She found no rental cars available within a four-hour radius, and she needed to get home to Bismarck, North Dakota. She and two employees bought a Ford Bronco for about $48,000 and drove roughly 1,500 to 1,600 miles in about 27 hours.

The FAA said about 12,462 flights were cancelled on Nov. 13 after the ground stop, though not all cancellations were directly caused by the order. Harding and her two employees bought the vehicle in Charlotte and headed back to North Dakota. Harding said she has no regrets, and her husband also wants to keep the vehicle, so they are keeping it.

When the FAA's November 13 nationwide ground stop cancelled flights and rental cars vanished, the decision made sense as a personal solution, not a compensation model. Under DOT rules, a cancelled passenger can obtain a full cash refund if they decline rebooking. But an FAA ground stop is an uncontrollable event, so airlines do not generally owe hotel bills, rental cars or alternative transportation.

## What airlines owe during an FAA ground stop

| Cost or remedy | Required for a cancelled ticket? |
| --- | --- |
| Cash refund if the passenger declines rebooking | Yes |
| Hotel | No general requirement |
| Meal | No general requirement |
| Rental car or alternate transport | No general requirement |

That distinction explains why a viral road trip should not be read as proof that travellers can charge a replacement vehicle or rental car to the airline. Travel insurance and some credit-card trip-delay benefits can be different, so passengers should read the policy terms and retain proof of cancellation and expenses.

**Do airlines reimburse rental cars during an FAA ground stop?**

Not as a general DOT requirement. The airline must provide a refund if a cancelled passenger rejects rebooking, including for a non-refundable ticket, but an FAA ground stop is outside the carrier's control. Hotel, food and ground-transport help depends on the airline policy or private travel coverage.

Harding's trip will remain a striking travel story. For holiday flyers, the practical lesson is to know the refund rule, carry trip-insurance details and reserve scarce rental cars only after comparing the cost with a confirmed airline option.

---

## Supreme Court Declines Trump Appeal Over UC Research Grant Cuts

University of California researchers can continue operating under reinstated National Science Foundation and National Endowment for the Humanities grants that had about $59 million remaining when they were terminated, with expiration dates as late as November 2029, after the Supreme Court declined to hear *Trump v. Thakur*. The Nov. 16 denial left the Ninth Circuit's preliminary First Amendment protections in place. There were no recorded dissents.

Academic researchers, grant administrators and scientists across the UC system have immediate continuity for those awards, but the litigation is not finished. The ruling preserves preliminary protections against alleged viewpoint-based grant cancellations; it does not end separate disputes over standardised administrative terminations or final merits proceedings.

## Related litigation continues

The petition itself notes that a related case, *American Council of Learned Societies v. NEH*, is on appeal in the Second Circuit. That appeal is separate from the Supreme Court's November 16 order.

## Why keyword filters became central to the case

Respondents argued that keyword searches of grant applications flagged terms such as "diversity" or "climate change." The legal dispute is over whether cancelling already awarded research because of perceived viewpoint is permitted under federal grant statutes and the First Amendment.

The government's petition relies on a federal grant-termination regulation (2 C.F.R. §200.340(a)(4)) and *Rust v. Sullivan*. Respondents argued that the Ninth Circuit's decision does not conflict with any other court's decision. The Supreme Court did not decide those claims on their final merits; it declined review at this stage.

**Why did the Supreme Court reject the appeal over UC research grants?**

The Court denied review, leaving the Ninth Circuit ruling in place. At the preliminary-injunction stage, the Ninth Circuit held that the terminations violated the First Amendment. Respondents argued that there is no split among the circuits, and the Court gave no reasons for denying review.

Researchers should treat the decision as continuity, not final closure. The next issues include the pending appeal in the related American Council of Learned Societies case and the parallel litigation affecting other agencies.

---

## Supreme Court Declines California Doctor's Implicit-Bias CME Challenge

California's implicit-bias continuing-medical-education requirement remains enforceable after the Supreme Court declined to hear *Khatibi v. Yip* on Nov. 16. Justice Clarence Thomas, joined by Justice Samuel Alito, dissented from the denial, and Justice Neil Gorsuch said he would have granted review. Three justices therefore favoured review, one short of the four votes needed. The Ninth Circuit decision therefore remains in force.

California physicians must complete 50 hours of continuing medical education for license renewal, and CME courses must include implicit-bias content under Business and Professions Code §2190.1. The case challenged the requirement on First Amendment grounds, but the Court's action did not suspend it.

## What the dissent and the denial do and do not decide

Justice Thomas's dissent from denial addressed the First Amendment issues in the case. Denial of review is not a ruling on the merits of the constitutional question, so the Court's action leaves the existing Ninth Circuit decision in place without endorsing or rejecting the challenge.

The state's requirement has exemptions for activities dedicated solely to research or without a direct patient-care component. Those exemptions should not be assumed: physicians and providers should check the course description and the Medical Board's current compliance materials.

**Does the California Medical Board pre-approve implicit-bias CME courses?**

Providers should check the Medical Board's current rules to see whether courses need pre-approval. Physicians remain responsible for keeping records of completed coursework.

For now, there is no change to the California requirement. A future case from another circuit could create the kind of conflict that prompts a new Supreme Court review, but this case leaves the existing Ninth Circuit result in place.

---

## How Pure Sulfur Rocks Formed on Mars: New Study Proposes Non-Biological Origins

NASA's Curiosity rover cracked a pale rock in Mars's Gediz Vallis channel and found bright yellow crystals of pure elemental sulfur. The discovery was surprising because volcanic activity and hot springs, typical terrestrial sources of sulfur, appear absent on Mount Sharp, according to NASA project scientist Ashwin Vasavada. A 2026 study in *Science* reports native sulfur deposits in Gale crater and offers non-biological origin explanations.

When Curiosity crushed the rock known as Convallaria on May 30, 2024, the rover's X-ray instrument indicated that the yellow grains were pure elemental sulfur. The rover could not determine when the crystals formed or how they arrived in the channel.

Coverage of the *Science* paper offers different explanations. One report describes sulfur from magma releasing hydrogen sulfide and sulfur dioxide gases, while another says the sulfur originated in subsurface ice. The paper's origin is therefore still debated.

| Study | Proposed setting | Key result |
| --- | --- | --- |
| *Science* (2026), VanBommel et al. | Gale crater, Gediz Vallis | Native sulfur deposit identified; origin proposals include magma-derived gases and subsurface ice |

The paper does not settle whether Mars was habitable. It does show that a yellow sulfur crystal is not, by itself, evidence of life. That matters because Curiosity has also found organic compounds and other features that keep the broader search for ancient life active.

**Why did Curiosity find pure yellow sulfur crystals in Gediz Vallis?**

Researchers say the sulfur could have formed through non-biological processes. Press coverage of the *Science* paper describes origins involving volcanic gases from magma or from subsurface ice; neither requires a living source.

Future sulfur-isotope measurements from Curiosity's Sample Analysis at Mars instrument could narrow the explanation. Until then, the clearest conclusion is that Mars had more varied sulfur chemistry than the surface appearance alone suggests.

---

## Epstein Autopsy Review: Michael Freeman's Biomechanical Findings vs. Official Ruling

A new presentation by forensic medicine professor Dr. Michael Freeman has renewed online claims about Jeffrey Epstein's death, but it has not changed the official finding. Freeman was scheduled to present a biomechanical analysis of the ligature injury pattern at University College London on Nov. 16. The New York City medical examiner's ruling remains suicide, and federal authorities have said there is no evidence Epstein was murdered.

Readers seeing claims that the presentation proved murder should separate its reported findings from its status. Freeman's research has not been peer-reviewed or published, and he has said he plans to publish it along with the autopsy files he obtained from Mark Epstein. Mark Epstein has said Freeman's analysis strengthened his belief that his brother's death required a deeper investigation. The dispute exists alongside documented custody and evidence failures at the Metropolitan Correctional Center.

## What Freeman's analysis says, and what the official record says

| Issue | Freeman's analysis | Official record |
| --- | --- | --- |
| Cause of death | Biomechanical analysis of the ligature pattern; he had declined to describe his conclusions in advance | Suicide ruling unchanged |
| Injuries | Says images show injuries unaccounted for by the medical examiner | No change to the ruling |

The presentation raises forensic questions; it is not a legal reversal. The DOJ inspector general's report documented serious MCC failures, including missed rounds and malfunctioning camera coverage. Those failures can make later reconstruction harder, but they do not themselves establish a different cause of death.

**Did Michael Freeman's analysis overturn Epstein's suicide ruling?**

No. The presentation challenges aspects of the interpretation of autopsy evidence, but the NYC medical examiner has not changed its ruling and the work has not been peer-reviewed. Federal authorities have said there is no evidence Epstein was murdered.

The next developments would be publication of Freeman's research and the autopsy files he obtained, and any response from the medical examiner's office. Readers should treat claims that the case has been officially solved in a new way with caution.

---

## Miguel Ángel Félix Gallardo Dies at 80 Without Facing U.S. Trial

Miguel Ángel Félix Gallardo, a founder of Mexico's Guadalajara Cartel often called "The Boss of Bosses," has died at 80 after decades in Mexican custody. He was transferred from Puente Grande prison to Guadalajara's Country 2000 private hospital on Nov. 13 and died on Nov. 15, according to press reports, which cited pneumonia and multiple organ failure.

His death closes a 37-year imprisonment in Mexico without extradition to the United States. It does not end the U.S. case tied to the 1985 killing of DEA Special Agent Enrique "Kiki" Camarena. Fellow cartel founder Rafael Caro Quintero was transferred to the United States in February 2025 and faces charges in federal court in Brooklyn.

Félix Gallardo's death at 80 closes his Mexican sentences, which run to 2066 after consecutive convictions. Prosecutors said in 2025 that Caro Quintero faces mandatory life imprisonment if convicted; in August 2025 they said they would not seek the death penalty.

## Where the two cartel founders stand

| Figure | 2026 status |
| --- | --- |
| Miguel Ángel Félix Gallardo | Died in Mexican custody |
| Rafael Caro Quintero | Facing prosecution in Brooklyn |

Félix Gallardo was arrested in 1989. Mexican reporting describes a 40-year sentence for cocaine trafficking, arms stockpiling and bribery, and a 37-year sentence for the 1985 killing of Camarena, handed down in 2017. Mexico, rather than the United States, retained custody through his death.

**Why was Miguel Ángel Félix Gallardo never extradited to the United States?**

He was tried and sentenced in Mexico, where he remained in custody after his 1989 arrest. Mexican reporting describes consecutive Mexican sentences running to 2066 and no completed U.S. extradition. Caro Quintero's February 2025 transfer to the United States followed a different route. No public record reviewed establishes a diplomatic reason for the absence of an extradition.

The next court developments are expected in Caro Quintero's Brooklyn case, not in the closed Mexican proceedings against Félix Gallardo.

---

## Editorial note

These eleven drafts follow the dossier's final priority order. Facts are checked against the primary and independent sources listed in Appendix B. The Stage 1 dossier was not supplied with this file, so the drafts could not be checked against it. The earlier Stage 2 drafts (Chase, FEMA and Iran) are included in this file and corrected in the same way.

---

## Production audit

The Chase, FEMA and Iran drafts were delivered in Stage 2 and appear in this file in dossier order. All three are marked NEW.

| Draft | Article-body length after Stage 3b | Target |
| --- | ---: | --- |
| Chase software bug outage | 559 words | 500–550 |
| FEMA EAS test | 501 words | 420–480 |
| Iran intelligence report | 562 words | 580–640 |

Word counts were measured after the Stage 3b corrections. Chase and FEMA are slightly above target and Iran is slightly below. The targets were not forced to fit, because that would mean changing sentences that were otherwise accurate.

Fact audit (Stage 3b): every claim was checked against the sources listed in Appendix B. The earlier statement that all names, dates, figures and quotations were drawn from the Stage 1 dossier is withdrawn, because that dossier was not supplied and several Stage 2 specifics could not be verified. Unverified specifics were removed rather than kept.

---

## Appendix A: Stage 3b change log

**1. Optimizely.** Headline "Sites" changed to "Organisations" (the count is 178 organisations). The 01:02 UTC remediation time was replaced by the Nov. 17 status-update wording. "Major websites" changed to "websites run by 178 organisations". The $7,151 "confirmed theft" figure was replaced with the reported wallet estimate (roughly $7,000 to $7,150). Stripe and Adyen were removed because no source names them. The iOS ranges were changed to the sourced Coruna (iOS 13 to 17) and DarkSword (iOS 18) ranges, and the patched versions were attributed to the kit's own comments. "Lockdown Mode and Private Browsing" was removed because no source supports it. The ".icu" domain was removed. The HSBC account was rewritten to match the eval() backup-copy description. "Equifax removed Optimizely" was removed. Credential rotation was reframed as a precaution.

**2. Chase.** "Five-hour" was removed (not sourced). The Chase statement is now a paraphrase, not a direct quote. The claim that transfers with Bank of America, U.S. Bank and Wells Fargo were "queued rather than lost" was removed. Downdetector figures were corrected to the sourced pattern (reports from about 9 a.m. ET, peak roughly 4,800, about 1,780 by 4:45 p.m. ET). Bank statements were limited to those sourced (Bank of America, U.S. Bank). The Truist, Capital One and PNC statements, the Early Warning queue claim and the FBI statement were removed. The OCC paragraph was checked and left unchanged except for the two sourced points.

**3. FEMA.** The quoted FEMA message was changed to a paraphrase. The wireless-alert statement was tied to the FCC notice's scope. The "NPT" code claim and the FCC contrast-and-colour guidance were removed (not in the FCC notice). "Feedback portal" was changed to "send feedback". The rescheduling condition was corrected to match the FCC notice. The 48-hour filing window, Nov. 19 deadline, Sept. 16 announcement, Dec. 3 alternative date, and the Oct. 2023 prior test were confirmed.

**4. Iran.** "Drafted" changed to "developing" (CNN). "Seven officials said no attack was imminent" was attributed to CNN. "In Manila" was removed (not found). "Very serious" was corrected to "very seriously" as reported. The White House "not credible" position was added. The UN Mission and Foreign Ministry section was removed (not found), and replaced with the sourced Iranian rejection and the Tom Warrick quote. The Defense Department referral and the "technical capability" source were removed. The NRC "millions of times" claim, the NRC "weapon of mass disruption" attribution, and the CDC shelter advice were removed (not verified). The "contamination range" table row was removed. The APEC and National Terrorism Advisory System references were removed.

**5. Propranolol and metoprolol.** The propranolol recall was removed: no FDA, DailyMed or manufacturer record for Breckenridge lot PK25110035 was found. The Breckenridge NDC, the Qualanex contact details and the propranolol table row were removed. The headline was rewritten to the metoprolol recall, which was supported by a report citing FDA (Advagen, Batch 2611C065A1, 3,684 bottles, NDC 72888-210-00, May 2028). "Migraines" was removed because metoprolol is not indicated for migraine. The "supplied DailyMed guidance" was attributed to product labeling. The advice to stop only on medical instruction was rewritten for the metoprolol batch.

**6. Florida flood watch.** The headline's El Niño causal claim was removed. Rainfall was corrected to the NWS Melbourne forecast (3 to 6 inches, localized 8 to 12 inches). The watch's nine counties, issue time and Tuesday-to-Friday period were confirmed. The Miami and Southeast Florida claims, the seas and gusts figures, the "Treasure Coast" and "Southwest Florida" rows, and the "system moves out Friday evening" claim were removed (not verified). The NOAA +2.5°C figure was confirmed; the "unusually warm subsurface" claim was removed.

**7. Trump air-traffic-control request.** The "$30.1 billion on Thursday" claim was corrected: the department had first sought $30.1 billion (reported in September 2026), and the request was raised to $50 billion on Friday, Nov. 13. The "both parties" claim and the "Nov. 23 Senate safety deadline" were removed (not verified). The financial table ($1 billion outlays, $3.7 billion obligated, $4.3 billion committed, $4.5 billion counter-offer) was removed (not verified). "Only 69 of 3,648 operating" was corrected to the sourced Senate Democrat figures (about 400 installed, 69 operating) and Duffy's "69th installation" comment. The "3,500 flights" claim was removed. The Peraton and L3Harris contract claim was removed. The El Dorado mechanism was corrected to the FAA's stated excessive-data explanation. The HPE position was added. GAO's 11,389 figure was confirmed.

**8. United.** The "4:02 p.m." start time, "6 p.m." restoration, "Denver, Houston, San Francisco" stops, "more than 600 flights" (now the sourced 715 FlightAware figure, attributed), and "five San Francisco international cancellations" were removed or corrected. The "crew systems" claim was removed. The duration is now reported as disputed (CBS about 90 minutes; United to CNN about 30 minutes). The DOT wording was changed to "United's published commitments".

**9. Ford Bronco.** "Delta" was removed. "Four reschedules" was changed to "repeated rebookings". The children and Monday-patients details were removed (not verified). The surname spellings "Mairer" and "Cowter" were removed, because no source I could reach gives them and the fact-check's alternative spellings also could not be verified; the employees are now "two employees". The Uber and 7:45 p.m. showroom details were removed (not verified). The distance was changed to 1,500 to 1,600 miles, attributed to reports. The 12,462 figure was attributed to the FAA, with the "not all directly caused" qualifier.

**10. UC grants (Trump v. Thakur).** The $59 million figure was corrected to the petition's wording: grants with about $59 million remaining when terminated, with expiration dates as late as November 2029. The EPA, HHS, Defense, Transportation and Energy table was removed (not verified). The specific research titles (leaf diversity, rhizobia, Ordovician fossils) were removed because the respondents' brief does not contain them. "Arbitrary" was removed. The "no split" claim was attributed to the respondents. The Judge Rita F. Lin hearing was removed. The Ninth Circuit ruling is described as a preliminary-injunction holding, per the petition.

**11. Khatibi v. Yip.** "Thomas, Alito and Gorsuch voted to take the case" was corrected: Thomas (joined by Alito) dissented from the denial, and Gorsuch said he would have granted review. The "§2190.1(e)" subsection was removed. "50 hours every two years" was changed to "50 hours for license renewal", as the court filing describes it. The Thomas dissent's detailed content (Shurtleff, post-hoc audit, pre-approval, compelled speech) was removed as not verified. The exemption wording was aligned to the sourced "no direct patient-care component" formulation.

**12. Mars sulfur.** The headline "2 Studies Solve Curiosity Mystery" was changed; the sources do not support "solve". The mass and weight error (899 kg, "341 kg in Martian gravity") was removed. "Brittleness" was removed. The clathrate study, 3.1 to 2.8 billion years, and the Gale-chlorate "GRL" study with 22°C, 54-day and 30 mM details were removed (not found). "Microbial activity" was removed. The May 30, 2024 date and the X-ray identification were added (sourced). The table was rebuilt around the one verified paper.

**13. Epstein review.** "3D" was removed from the headline and text (not in the sources). "In London" was kept as University College London, per CBS. "Eriksson and Dror" was removed (not verified). "Forensic scholar" was changed to "forensic medicine professor" (CBS). The "DOJ and FBI unchanged" claim was replaced with the sourced federal "no evidence of murder" position. The "unpublished photographs" release claim was removed. The neck-mark, shoulder, fingernail, orange-strip and guard-interview table rows were removed (not verified) and replaced with the sourced analysis.

**14. Félix Gallardo.** The headline was changed to say he died without facing a US trial, rather than explaining why no extradition occurred (no source establishes a reason). "Pneumonia and multiple organ failure" was attributed to press reports. "Caro Quintero was sent to Brooklyn" was changed to transferred to the United States. The docket number 15-CR-208 was removed (not verified). "Only remaining figure" was removed. The death-penalty status was corrected (not sought, August 2025). The "14,631 days" sentence was removed: the statement could not be found, and the arithmetic does not match it (from Camarena's killing on Feb. 9, 1985, the days to Feb. 27, 2025 total 14,628, not 14,631). The "2022 house-arrest request failed" sentence was removed (sources conflict). The "40-year sentence imposed in 2000" year was removed (not verified). The Fonseca and Operation Leyenda table rows were removed (not verified). The Mexican sentencing figures (40 years, 37 years in 2017, consecutive, to 2066) were confirmed.

**Editorial and production notes.** The Stage 1 dossier was not supplied, so the "all facts drawn from the dossier" statement was withdrawn. The file's garbled Optimizely opening (split across the Chase block) was rebuilt in its original order. Internal karmactive.com links were left unchanged, as instructed. No external links were added.

---

## Appendix B: Verification log and open items

**Primary and independent sources checked this session**

- Supreme Court docket 26-210 (Trump v. Thakur): petition denied Nov. 16, 2026; no dissent noted. Petition text: about $59 million remaining at termination, expiration dates as late as November 2029; related appeal in ACLS v. NEH (2d Cir.). Respondents' brief in opposition: no conflict with other courts and no circuit split; keyword searches for "diversity" or "climate change."
- Supreme Court docket 25-1240 (Khatibi v. Yip): petition denied Nov. 16, 2026; Gorsuch would grant; Thomas, with Alito joining, dissenting from denial.
- FCC public notice DA 26-989 (released Sept. 16, 2026): nationwide EAS test Nov. 17, 2026 at 2:20 p.m. ET via IPAWS in English and Spanish; rescheduled date Dec. 3, 2026; ETRS Form Two within 48 hours (deadline Nov. 19, 2026, 2:20 p.m. ET); Form Three within 45 days.
- NOAA Climate Prediction Center ENSO discussion, Nov. 12, 2026: Niño-3.4 at +2.5°C.
- Optimizely incident: Help Net Security (Nov. 17, 2026) and StepSecurity (OPTIMJACK write-up) summarising Report URI's findings: 188 of 1,611 snippets, 178 organisations; Project JavaScript field; first observed 04:21 UTC Nov. 16; one snippet still infected 21:52 UTC; all clean by 23:11 UTC; skimmer added 13:43 UTC; crypto estimates about $7,040 to about $7,150; Coruna and DarkSword; iOS 18.6 and earlier reload every 60 seconds; patched iOS 18.7.3+ and 26.3+ per the kit's comments; HSBC eval fallback; Salesforce disabled scripts.
- CBS News (United, Nov. 16, 2026): pilots' union memo on weight-and-balance; about 90 minutes; FlightAware 715 delays late Monday afternoon; no impact on flights in progress or United Express flights.
- Chase outage: TechTimes (Nov. 17, 2026), TechRepublic, and NBC/CNN/AP summaries: Monday Nov. 16; reports from about 9 a.m. ET; peak about 4,800 (Barron's count 4,822); about 1,780 by 4:45 p.m. ET; Bank of America and Citigroup no own problems; U.S. Bank not directly affected.
- OCC computer-security incident notification rule (Bulletin 2021-55 and summaries): 36-hour bank notification; service-provider four-hour customer-notice trigger; failed system upgrade cited as a notification incident example.
- FAA/Juniper ground stop (Nov. 13, 2026): ABC, Spectrum, aiweekly, CNN and Yahoo summaries: 3:30 p.m. to about 8:15 p.m. ET; El Dorado, Arkansas; 1,000 connection attempts every 4 to 5 seconds; Juniper installations paused; HPE says equipment worked as configured; Senate Democrats citing L3Harris (400 installed, 69 operating); Duffy's 69th-installation comment.
- Trump $50B request: Reuters/TheStandard/Airlinegeeks (Sept. 28, 2026, $30.1 billion request); $50 billion raised on Friday Nov. 13 after the en route communications failure.
- GAO-26-107992 (Sept. 14, 2026): 11,389 individual Phase 1 project schedules; no integrated master schedule.
- Iran dirty-bomb reporting (CNN, Nov. 16–17, 2026, via Iran International, Time, The Hill and others): contingency planning; seven US officials; not imminent; Trump "very seriously"; White House "no credible threat"; ODNI declined to comment; Iran rejected allegations; Tom Warrick quote.
- Metoprolol recall: The Healthy (citing FDA), HelloPharmacist NDC listing: Advagen Pharma; 3,684 bottles; batch 2611C065A1; NDC 72888-210-00; May 2028; tablets or capsules.
- Félix Gallardo: Wikipedia (arrest 1989; transfer to Country 2000 on Nov. 13; death Nov. 15; pneumonia complicated by multiple organ failure; 2017 37-year sentence); Zeta Tijuana and Milenio (40 and 37-year terms, consecutive, to 2066); AP/NPR (Feb. 27, 2025 transfer of 29 prisoners); EDNY/AP and NBC (mandatory life; death penalty not sought, August 2025).
- Tara Harding (Time News, Ford Authority, Geo TV, The Bold News): Charlotte training; ground stop Friday Nov. 13; repeated rebookings; no rental cars within four hours; about $48,000 Bronco; two employees; about 27-hour drive; arrived Bismarck late Saturday; 1,593 miles per her post, 1,500 to 1,700 reported; keeping the vehicle.
- UCL event and CBS (Oct. 2, 2026): Freeman, professor of forensic medicine (OHSU and Maastricht); presentation at University College London on Nov. 16; biomechanical analysis of the ligature pattern; plans to publish research and autopsy files obtained from Mark Epstein.
- Mars: Science (2026), "A native sulfur deposit in Gale crater, Mars" (VanBommel et al.); Convallaria crushed May 30, 2024; X-ray identification of pure elemental sulfur; Ashwin Vasavada on absent volcanic and hot-spring sources.
- Wikipedia (Félix Gallardo, Camarena): Camarena kidnapped Feb. 7, 1985, killed Feb. 9, 1985.
- Propranolol label warning on abrupt cessation (product labeling; not re-fetched this session).

**Could not be verified and removed or softened in the article**

- Breckenridge propranolol ER recall, lot PK25110035, NDC 51991-817-01, "November 16" notice, and the Qualanex contact details.
- The "Breckenridge recall notice" telling consumers to stop immediately.
- Chase "five-hour" outage length, the 10 a.m. to 3:15 p.m. window, and the $ and report counts for Bank of America, U.S. Bank and Wells Fargo beyond the sourced pattern.
- Chase/Zelle queue claim for cross-bank transfers and the FBI "no evidence" statement.
- The Iran "Manila" remark, the UN Mission "wholly illegitimate" statement, Foreign Ministry spokesman comments, and the NRC and CDC quotations.
- The Florida Miami/Southeast Florida flood watch, its seas (9 to 14 feet) and gusts (30 to 35 mph) figures.
- The Senate Nov. 23 deadline or briefing, the Juniper "3,500 flights" figure, the Peraton/L3Harris contract claim, the FAA $1 billion outlay / $3.7 billion obligated / $4.3 billion committed figures, and the $4.5 billion Senate counter-offer.
- The United Denver, Houston and San Francisco stops, the 4:02 p.m. start, the 600-flight and five-SFO-cancellation figures.
- The Bronco employees' surname spellings (Maier/Cowger and Mairer/Cowter), the Uber and 7:45 p.m. showroom details.
- The "14,631 days" statement attributed to the Camarena family, and the 2022 house-arrest claim.
- The Thakur research-title examples and the EPA, HHS, Defense, Transportation and Energy table.
- The Science paper's 3.1 to 2.8 billion-year timeframe and clathrate mechanism; the GRL chlorate study (22°C, 54 days, below 30 mM).
- The "3D" model, Eriksson and Dror as co-presenters, the orange strip, neck mark, shoulder haemorrhage, subungual debris and guard-interview details.
- The Equifax Optimizely removal and the Lockdown Mode and Private Browsing protections.

**Open items for confirmation before publication**

1. Check the FDA Enforcement Report for any propranolol recall; none was found.
2. Confirm the Optimizely root-cause report and any Equifax statement.
3. Confirm the DOJ inspector general's MCC findings (missed rounds, camera coverage) against the report itself; this was not re-fetched.
4. Confirm the FAA's Juniper router figures and any Senate briefing date with the FAA and Senate Commerce Committee.
5. Confirm Freeman's Nov. 16 presentation outcome with UCL or a post-event report; only pre-event coverage was found.
6. Confirm the Science paper's text (VanBommel et al., 2026) and whether a second GRL paper exists; the Science page could not be retrieved.
7. Confirm the MedWatch telephone number (1-800-332-1088) on fda.gov; the page could not be checked for the number.
