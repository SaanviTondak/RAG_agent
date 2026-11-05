# Hand-grading sheet: dev answers (20261104-2305_dev_glm-5p3)

Grade each answer in `eval/human_grades.json` as **pass**, **partial** or **fail**, with a short note when it isn't a clean pass.

- **pass**: you'd hand this to an analyst as correct, and it contains what the reference answer has (wording can differ; extra correct detail is fine).
- **partial**: mostly right but missing or getting wrong something the reference has.
- **fail**: wrong headline answer or figure, or missing most of the reference.

Grade against the reference answer, the way the hidden grader will. Don't look at any scorecard first.

---

## q_001 (tier 1, graded by `fuzzy_numeric`)

**Question:** What was Apple's total net revenue in fiscal year 2025?

**Reference answer:** $416.2 billion

**Agent answer:**

> Apple's total net revenue in fiscal year 2025 was **$416.2 billion**.
> 
> - This covers the fiscal year from September 29, 2024 through September 27, 2025 (Apple's fiscal year ends in late September).
> - The figure is net sales as reported on the consolidated income statement.
> 
> Sources: [SQL: income_statements]

---

## q_006 (tier 1, graded by `llm_judge`)

**Question:** What were the primary risk factors Apple disclosed related to its supply chain in its fiscal year 2025 10-K filing?

**Reference answer:** Apple disclosed risks including: reliance on single or limited sources for components; dependence on third-party manufacturers; supply chain disruptions from geopolitical tensions, natural disasters, and health emergencies; component supply constraints affecting product availability; and risks from concentration of manufacturing operations in specific regions.

**Agent answer:**

> Apple's FY2025 10-K (Item 1A, Risk Factors) discloses four primary supply-chain risk factors — dependence on outsourced manufacturing, single/limited-source component supply, trade restrictions and business interruptions, and inventory/purchase-commitment exposure — plus several related risks.
> 
> - **Dependence on outsourcing partners (p.10):** A significant majority of Apple's manufacturing is performed by outsourcing partners located primarily in China mainland, India, Japan, South Korea, Taiwan and Vietnam, with final assembly of substantially all hardware products by partners primarily in Asia and much of transportation/logistics management outsourced. This reduces Apple's direct control over production and distribution, can adversely affect cost, quality or quantity, leaves Apple responsible for warranty service on defects, and exposes it to supplier code-of-conduct violations. Changes or additions to the supply chain require considerable time and resources and carry regulatory and operational risks.
> 
> - **Obtaining components in sufficient quantities on commercially reasonable terms (p.10–11):** Certain components come from single or limited sources, and even multi-source components are subject to industrywide shortages and commodity price fluctuations — the filing cites past global semiconductor shortages. New products often use custom components available from only one source, with initial capacity constraints until supplier yields mature. Apple may be unable to extend or renew supply agreements, and suppliers may fail, consolidate, or shift to producing common components instead of Apple's custom ones.
> 
> - **Trade restrictions, tariffs and geopolitical disruption (p.8–9):** Restrictions on international trade (tariffs, import/export controls) can increase costs or limit availability of products, components, rare earths and other raw materials, and can force supplier changes, restructuring, or price increases. The filing specifically flags the new U.S. tariffs announced beginning in Q2 2025 on imports from China, India, Japan, South Korea, Taiwan, Vietnam and the EU, retaliatory measures by other countries, and the Section 232 investigation into semiconductor imports. It also notes global supply chains are highly concentrated and that escalating geopolitical tensions or conflict could cause significant disruptions.
> 
> - **Business interruptions (p.9):** Natural disasters (many supplier and contract-manufacturer operations are in earthquake-prone locations), fires, power shortages, industrial accidents, labor disputes, public health issues and similar events can make it difficult or impossible to manufacture and deliver products; because Apple relies on single or limited sources for many critical components, an interruption affecting those sources would exacerbate the consequences, and insurance may be insufficient.
> 
> - **Inventory write-downs and purchase-commitment risk (p.11):** Apple orders components and builds inventory in advance of product announcements, with manufacturing purchase obligations typically covering up to 150 days. Volatile, rapidly changing markets create the risk of forecasting incorrectly — ordering excess or insufficient components — and of not fully utilizing purchase commitments, requiring cancellation fee reserves.
> 
> - **Related risks:** design and manufacturing defects in third-party components (p.11); IT system failures or network disruptions that can impede manufacturing and shipping across the global supply chain (p.13); suppliers' exposure to ransomware and other malicious attacks that can disrupt operations (p.13–14); and adverse macroeconomic conditions that could cause financial instability or insolvency among suppliers, contract manufacturers and logistics providers (p.7–8).
> 
> Sources: [AAPL FY2025 10-K, p.7–14]

---

## q_008 (tier 1, graded by `fuzzy_numeric`)

**Question:** What percentage of Microsoft's total revenue came from the United States in fiscal year 2025?

**Reference answer:** 51.3%

**Agent answer:**

> In fiscal year 2025, 51.3% of Microsoft's total revenue came from the United States.
> 
> - U.S. revenue: $144.5 billion of $281.7 billion total revenue (FY2025, fiscal year ended June 30, 2025).
> - The remaining 48.7% ($137.2 billion) came from other countries.
> 
> Sources: [SQL: geographic_revenue, income_statements]

---

## q_011 (tier 2, graded by `exact_match_entity`)

**Question:** Which company had the fastest revenue growth rate between their two most recent fiscal years, and what was the growth rate?

**Reference answer:** Alphabet (GOOGL) had the fastest revenue growth between the two most recent fiscal years at about 15.1%.

**Agent answer:**

> Alphabet (GOOGL) had the fastest revenue growth between its two most recent fiscal years, at 15.1% (FY2024 → FY2025).
> 
> - **Alphabet:** $350.0 billion → $402.8 billion, +15.1%
> - **Microsoft:** $245.1 billion → $281.7 billion, +14.9% (a close second)
> - **Apple:** $391.0 billion → $416.2 billion, +6.4%
> 
> Note that the fiscal years cover different calendar months (Apple's ends late September, Microsoft's June 30, Alphabet's December 31), so the periods are not perfectly aligned.
> 
> Sources: [SQL: income_statements]

---

## q_012 (tier 2, graded by `llm_judge`)

**Question:** How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and does the 10-K filing explain why?

**Reference answer:** Apple's Greater China revenue decreased from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of approximately 3.8%. The FY2025 10-K states this was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Agent answer:**

> Apple's Greater China net sales fell from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of $2.6 billion (−3.8%, shown as (4)% in the 10-K), and yes, the FY2025 10-K explains the decrease.
> 
> - **FY2024 (ended September 28, 2024):** $66.95 billion; **FY2025 (ended September 27, 2025):** $64.38 billion — a decrease of $2.6 billion, or −3.8%.
> - **Why (per the 10-K, MD&A "Greater China"):** "Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
> - Greater China was the only one of Apple's five geographic reportable segments to decline in FY2025; every other region grew (Americas +7%, Europe +10%, Japan +15%, Rest of Asia Pacific +10%), while total net sales rose 6% to $416.2 billion.
> - This was the second consecutive annual decline for the segment, which had already fallen 8% in FY2024 from $72.56 billion in FY2023.
> 
> Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.48]

---

## q_014 (tier 2, graded by `llm_judge`)

**Question:** Microsoft restructured its segment reporting in August 2024. How are the three segments defined in the fiscal year 2025 10-K, and what was the revenue for each?

**Reference answer:** The three segments in the FY2025 10-K are: (1) Productivity and Business Processes ($120.8B) - includes Microsoft 365 Commercial/Consumer, LinkedIn, and Dynamics; (2) Intelligent Cloud ($106.3B) - includes Azure, SQL Server, Windows Server, GitHub, and enterprise services; (3) More Personal Computing ($54.6B) - includes Windows, Devices, Gaming, and Search/news advertising.

**Agent answer:**

> In its FY2025 10-K, Microsoft reports three segments — Productivity and Business Processes ($120.8 billion FY2025 revenue), Intelligent Cloud ($106.3 billion), and More Personal Computing ($54.6 billion) — which together sum to consolidated revenue of $281.7 billion. The August 2024 reorganization aligned segments with how Microsoft manages the business, most notably bringing the commercial components of Microsoft 365 together in Productivity and Business Processes, with prior-period segment information recast to match.
> 
> **Segment definitions and FY2025 revenue (fiscal year ended June 30, 2025):**
> 
> - **Productivity and Business Processes — $120.8 billion.** Products and services in Microsoft's portfolio of productivity, communication, and information services, spanning devices and platforms. It primarily comprises: Microsoft 365 Commercial products and cloud services (Microsoft 365 Commercial cloud — including Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot — plus Windows Commercial on-premises and Office licensed on-premises); Microsoft 365 Consumer products and cloud services; LinkedIn (Talent, Marketing, Premium Subscriptions, and Sales Solutions); and Dynamics products and cloud services (Dynamics 365 across ERP, CRM, Power Apps, and Power Automate, plus on-premises ERP/CRM).
> - **Intelligent Cloud — $106.3 billion.** Public, private, and hybrid server products and cloud services that power modern business and developers. It primarily comprises: Server products and cloud services (Azure and other cloud services — cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings — plus server products such as SQL Server, Windows Server, Visual Studio, System Center, and related CALs); and Enterprise and partner services (Enterprise Support Services, Industry Solutions, Nuance professional services, Microsoft Partner Network, and Learning Experience).
> - **More Personal Computing — $54.6 billion.** Products and services that put customers at the center of the experience with Microsoft's technology. It primarily comprises: Windows and Devices (Windows OEM licensing — Pro and non-Pro — plus Surface and PC accessories); Gaming (Xbox hardware and Xbox content and services, including first- and third-party content, Xbox Game Pass and other subscriptions, Xbox Cloud Gaming, and advertising); and Search and news advertising (Bing and Copilot, Microsoft News, Microsoft Edge, and third-party affiliates).
> 
> Note: the database's FY2024 segment figures (e.g., Productivity and Business Processes $106.8 billion) are on the recast basis used in the FY2025 10-K, so they differ from the FY2024 10-K's original segment presentation.
> 
> Sources: [SQL: segment_revenue], [SQL: income_statements], [MSFT FY2025 10-K, p.5], [MSFT FY2025 10-K, p.7], [MSFT FY2025 10-K, p.8], [MSFT FY2025 10-K, p.35]

---

## q_017 (tier 2, graded by `llm_judge`)

**Question:** According to Alphabet's 10-K filings, what are the key components of 'Google Services' revenue, and how did YouTube advertising revenue change between FY2024 and FY2025?

**Reference answer:** Google Services includes Google Search & other, YouTube ads, Google Network, and Google subscriptions/platforms/devices. YouTube advertising revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of approximately 11.7%.

**Agent answer:**

> Per Alphabet's FY2025 10-K, Google Services revenue consists of Google advertising plus Google subscriptions, platforms, and devices, and within that, YouTube ads revenue grew $4.2 billion (11.7%) from $36.1 billion in FY2024 to $40.4 billion in FY2025.
> 
> **Key components of Google Services revenue (FY2025 10-K, MD&A and Note 15):**
> - **Google advertising** ($294.7 billion in FY2025), made up of three components:
>   - Google Search & other — revenues on Google search properties (including traffic from search distribution partners) and other owned/operated properties like Gmail, Google Maps, and Google Play ($224.5 billion in FY2025)
>   - YouTube ads — revenues generated on YouTube properties ($40.4 billion in FY2025)
>   - Google Network — revenues on Google Network properties participating in AdMob, AdSense, and Google Ad Manager ($29.8 billion in FY2025)
> - **Google subscriptions, platforms, and devices** ($48.0 billion in FY2025) — fees for consumer subscription products (YouTube TV, YouTube Music and Premium, NFL Sunday Ticket, Google One), sale of apps and in-app purchases, and devices.
> 
> **YouTube ads change, FY2024 → FY2025:**
> - Revenue rose from $36,147 million to $40,367 million, an increase of $4.2 billion, or 11.7%.
> - The filing attributes the growth to direct response advertising products, followed by brand advertising products, both of which benefited from increased spending by advertisers.
> 
> Sources: [GOOGL FY2025 10-K, p.31], [GOOGL FY2025 10-K, p.35], [GOOGL FY2025 10-K, p.36], [GOOGL FY2025 10-K, p.87], [SQL: segment_revenue]

---

## q_018 (tier 2, graded by `exact_match_entity`)

**Question:** Which company has the highest current ratio (current assets / current liabilities) in their most recent fiscal year?

**Reference answer:** Alphabet (GOOGL) has the highest current ratio in the most recent fiscal year (about 2.01x).

**Agent answer:**

> Alphabet (GOOGL) has the highest current ratio in FY2025, at 2.01.
> 
> - **GOOGL:** $206.0 billion current assets / $102.7 billion current liabilities = **2.01**
> - **MSFT:** $191.1 billion current assets / $141.2 billion current liabilities = **1.35**
> - **AAPL:** $148.0 billion current assets / $165.6 billion current liabilities = **0.89**
> 
> Alphabet holds roughly twice its current liabilities in current assets, while Apple's ratio is below 1.0 — its current liabilities exceed current assets, consistent with Apple's lean working-capital management. Note that fiscal years differ: Apple's FY2025 ended in late September, Microsoft's on June 30, and Alphabet's on December 31, 2025.
> 
> Sources: [SQL: balance_sheets]

---

## q_022 (tier 3, graded by `llm_judge`)

**Question:** Across all three companies, which saw the largest absolute dollar increase in revenue between their two most recent fiscal years? Break down how much of that increase came from each business segment.

**Reference answer:** Alphabet had the largest absolute increase at approximately $52.8B ($350.0B to $402.8B). By operating segment, Google Services grew by $37.8B ($304.9B to $342.7B), Google Cloud grew by $15.5B ($43.2B to $58.7B), and Other Bets declined by $0.1B ($1.6B to $1.5B); a hedging reconciliation of approximately -$0.3B accounts for the difference between the segment subtotal and consolidated revenue. Microsoft increased by $36.6B and Apple by $25.1B.

**Agent answer:**

> Alphabet (GOOGL) saw the largest absolute revenue increase, with revenue rising $52.8 billion from $350.0 billion in FY2024 to $402.8 billion in FY2025 — ahead of Microsoft's +$36.6 billion and Apple's +$25.1 billion.
> 
> Breakdown of Alphabet's $52.8 billion increase by reportable segment (FY2024 → FY2025):
> - **Google Services: +$37.8 billion** ($304.9B → $342.7B), roughly 71.5% of the total increase — the dominant driver.
> - **Google Cloud: +$15.5 billion** ($43.2B → $58.7B), roughly 29.3% of the total increase.
> - **Other Bets: –$0.1 billion** ($1.6B → $1.5B), a slight decline.
> - **Hedging gains (losses): –$0.3 billion** ($0.2B → –$0.1B) — a reconciling item, not a segment, but it reduces the consolidated total.
> 
> These components sum exactly to the $52.8 billion consolidated increase. For comparison, Microsoft's +$36.6 billion came mostly from Intelligent Cloud (+$18.8B) and Productivity and Business Processes (+$14.0B, as restated in the FY2025 10-K), and Apple's +$25.1 billion came mostly from Services (+$13.0B) and iPhone (+$8.4B) — note Apple's figures here are its product/service categories, since its reportable segments are geographic.
> 
> Sources: [SQL: income_statements], [SQL: segment_revenue]

---

## q_025 (tier 3, graded by `llm_judge`)

**Question:** Apple's Services segment has been growing as a share of total revenue. Calculate the Services revenue growth rate for each of the last two years, compare it to iPhone revenue growth, and find what Apple's 10-K says about the strategic importance of Services.

**Reference answer:** Services growth: FY2023->FY2024: 12.9% ($85.2B to $96.2B), FY2024->FY2025: 13.5% ($96.2B to $109.2B). iPhone growth: FY2023->FY2024: 0.3%, FY2024->FY2025: 4.2%. Services is consistently growing much faster. The 10-K highlights Services as a key growth driver with higher margins, recurring revenue from subscriptions, App Store, Apple Music, iCloud, and advertising.

**Agent answer:**

> Services revenue grew 12.9% in FY2024 and 13.5% in FY2025, far outpacing iPhone growth of 0.3% and 4.2% in those years, lifting Services to 26.2% of Apple's total revenue in FY2025 (note: "Services" here is Apple's product/service category from the net-sales-by-category table; Apple's reportable segments are geographic).
> 
> - **Growth rates (calculated from database figures):** Services rose from $85.2 billion (FY2023) to $96.2 billion (FY2024, +12.9%) to $109.2 billion (FY2025, +13.5%); iPhone rose from $200.6 billion to $201.2 billion (+0.3%) to $209.6 billion (+4.2%). These match the 10-K's rounded changes (Services 13%/14%; iPhone —%/4%).
> - **Share of total revenue:** Services was 22.2% of total net sales in FY2023, 24.6% in FY2024, and 26.2% in FY2025 (total net sales $383.3B → $391.0B → $416.2B).
> - **What drove Services growth:** The FY2025 10-K (p.25) attributes the FY2025 increase "primarily due to higher net sales from advertising, the App Store and cloud services"; the FY2024 10-K (p.25) cites the same three drivers for FY2024. iPhone's FY2025 increase is attributed to higher net sales of Pro models.
> - **Strategic importance per the 10-K:** Apple frames Services as both a growth and margin engine. Services gross margin percentage was 75.4% in FY2025 (73.9% in FY2024, 70.8% in FY2023) versus 36.8% for Products in FY2025, and Services gross margin dollars grew from $71.1 billion to $82.3 billion in FY2025, helping lift total gross margin percentage from 46.2% to 46.9% (FY2025 10-K, p.25). In Item 1, Apple states it "is focused on expanding its market opportunities related to smartphones, personal computers, tablets, wearables and accessories, and services," lists "a strong third-party software and accessories ecosystem" among its principal competitive factors, and describes a broad services portfolio — App Store, subscription services (Apple Music, Apple TV, Apple Arcade, Apple Fitness+, Apple News+), AppleCare, cloud services, advertising, and payment services (Apple Card, Apple Pay) (FY2025 10-K, pp.4–5).
> 
> Could not be verified: the 10-K contains no explicit standalone "strategic importance of Services" narrative beyond the passages above (no dedicated Services strategy subsection was found in the sections read), and I did not review Item 1A Risk Factors or any paid-subscription/installed-base metrics, which may contain additional Services commentary.
> 
> Sources: [SQL: segment_revenue], [SQL: income_statements], [AAPL FY2025 10-K, pp.4–5], [AAPL FY2025 10-K, pp.24–25], [AAPL FY2024 10-K, p.25]

