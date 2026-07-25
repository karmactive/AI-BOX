# STORY 6: AWS OUTAGE - STAGE 2 RESEARCH & ENHANCEMENT

## KEY FINDINGS

**Two July 2026 Outages:**

**CloudFront Outage (July 16):**
- Duration: 3.5 hours
- Service: AWS CloudFront CDN
- Affected: VPC Origins customers
- Root Cause: Connection-management limit issue
- Impact: Websites showed 5xx errors
- Examples: HuggingFace, UK National Lottery, Tailscale, Ubiquiti

**US-West-2 Regional Outage (July 24):**
- Start Time: ~7:40 AM ET Friday  
- Duration: ~80 minutes
- Region: Oregon (US-WEST-2)
- Root Cause: Regional internet connectivity problem
- Services Affected: Initially 5 services, expanded to 7
- Impact: Cascaded to dependent services
- Examples: DoorDash, Reddit, Hulu, Apple Pay, PlayStation Network
- Services: Global Accelerator, Elastic Container Service, and others

**Context:**
- Third notable AWS incident in ~3 months
- May 2026: Data center thermal event
- June 2026: Network disruption
- Pattern: AWS reliability under scrutiny

---

## **SUGGESTIONS**

### Critical Missing Details
1. **Specific Duration** - Both outages' exact timelines
2. **Root Causes Explained** - Connection management limits, thermal issues
3. **Service Interdependency** - Why one region affected so many services
4. **Customer Impact Scale** - Millions of users affected
5. **Cascade Failure Mechanism** - How problem spread
6. **Recovery Process** - How AWS restored service
7. **Repeat Pattern** - Third incident in three months significance
8. **AWS's Market Position** - Massive market share making outages critical
9. **Multi-Region Strategy Failure** - Why redundancy didn't prevent
10. **Industry Implications** - What this means for cloud adoption

### Business Context
- AWS dominance (40%+ cloud market share)
- Outage concentration of risk in single provider
- Multi-cloud strategies becoming more important
- Incident frequency raising reliability concerns
- Customer SLA implications and penalties

### Technical Understanding
- VPC Origins and CloudFront architecture
- Regional vs global service model
- Cascade failure vs isolated failure
- Connection management system limitations
- Redundancy and failover mechanisms

---

## **ELABORATION**

### Outage Details (Must Include)
- Two separate but significant incidents
- July 16: 3.5-hour CloudFront CDN outage affecting content delivery
- July 24: 80-minute regional outage affecting 7 major services
- Both had cascading effects on dependent services
- Multiple major consumer/enterprise services affected
- Examples: DoorDash orders, Reddit posts, Apple Pay transactions

### AWS Market Impact (Should Include)
- AWS hosts 40%+ of cloud infrastructure
- Single outage affects millions of internet services
- Creates concentrated risk for internet reliability
- AWS's dominance makes failures highly visible
- Competitors (Azure, Google Cloud) gain attention during AWS outages

### Industry Lessons (Nice to Include)
- Multi-cloud strategies becoming necessity for critical services
- Cloud provider redundancy essential for business continuity
- Reliability expectations need matching with actual uptime
- Single cloud provider dependence creates systemic risk
- Configuration management and thermal monitoring critical

---

## VERIFIED SOURCES

- [CyberNews - CloudFront outage analysis](https://cybernews.com/news/aws-cloudfront-outage-websites-5xx-errors/)
- [Data Center Dynamics - Major outage coverage](https://www.datacenterdynamics.com/en/news/major-aws-outage-brings-down-much-of-the-web/)
- [Charisma Magazine - Affected services reporting](https://mycharisma.com/news/aws-outage-disrupts-doordash-reddit-hulu-and-apple-pay-as-major-websites-go-down/)
- [Medium - Technical analysis](https://medium.com/the-tech-notes/the-aws-era-is-officially-dead-and-the-july-mega-outage-just-broke-the-cloud-a584bdb094bc)

---

## RECOMMENDATIONS

**Suggested additions:**
1. Highlight two separate incidents (not one)
2. Specific dates and durations
3. Clear examples of affected services
4. Cascade failure explanation (simplified)
5. Multi-cloud strategy context
6. AWS market dominance and concentration risk
7. Pattern of three incidents in three months

**Word count increase:** 398 → 500-550 words

