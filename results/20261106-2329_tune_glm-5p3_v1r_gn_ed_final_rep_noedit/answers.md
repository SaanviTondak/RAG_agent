# Answers: 20261106-2329_tune_glm-5p3_v1r_gn_ed_final_rep_noedit

25/26 passed. Failed answers first. Scorecard: [scorecard.md](scorecard.md).

## x_047#1: FAIL (llm_judge, level 4)

**Question:** How do Microsoft's and Alphabet's fiscal year 2025 10-Ks describe the effect of AI infrastructure on their costs and margins?

**Gold:** Microsoft says scaling its AI infrastructure lowered gross margin percentages: Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure, and operating expenses rose on investments in cloud and AI engineering. Alphabet says it is significantly increasing investment in technical infrastructure, in particular for AI, and that the costs of operating it (depreciation, energy, equipment and network capacity) are expected to increase significantly because AI offerings require more compute; Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure.

**Grade:** 5/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure

**Claims the tools did not back:** unsupported: Both companies' operating margins were roughly flat in FY2025.

*4 tool calls, 39.7s, $0.0407*

**Answer:**

Both 10-Ks describe AI infrastructure as a significant driver of rising costs and margin pressure, but each pairs that with offsetting efficiencies — Microsoft says scaling AI infrastructure "may decrease our operating margins" and cut its gross margin percentage, while Alphabet says technical-infrastructure costs "are expected to significantly increase" and create "downward pressure" on operating margin, though both companies' operating margins were roughly flat in FY2025.

**Microsoft (FY2025 10-K, fiscal year ended June 30, 2025)**
- MD&A outlook (p.34): "The investments we are making in cloud and AI infrastructure and devices will continue to increase our operating costs and may decrease our operating margins," noting datacenter expansion depends on land, energy, networking supplies, and servers including GPUs.
- FY2025 vs. FY2024 results (p.37): Cost of revenue increased $13.7 billion or 19% driven by growth in Microsoft Cloud; gross margin percentage decreased slightly, driven by Intelligent Cloud. Microsoft Cloud gross margin percentage fell to 69%, "driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure."
- Intelligent Cloud detail (p.38): segment cost of revenue rose $10.6 billion or 36% driven by Azure, with gross margin percentage decreased by AI infrastructure scaling, offset in part by Azure efficiency gains.
- Risk Factors (p.17): "We are incurring significant costs to build and maintain infrastructure to support cloud-based and AI services, reducing operating margins."
- Actuals (database): gross margin slipped from 69.8% to 68.8%, while operating margin rose from 44.6% to 45.6% on revenue growth of 15%.

**Alphabet (FY2025 10-K, fiscal year ended December 31, 2025)**
- MD&A "Trends in Our Business and Financial Effect" (p.30): Alphabet continues to invest in capital expenditures to scale technical infrastructure "in particular for AI," expects to significantly increase that investment in 2026 (servers, network equipment, data centers), and states that infrastructure operating costs — "depreciation, energy, equipment, and network capacity — are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings." It expects to keep driving datacenter efficiencies, e.g., through AI model design and its TPU/GPU-based infrastructure.
- Cost of revenues (p.37): increased $16.2 billion from 2024 to 2025, with the $11.2 billion rise in other cost of revenues driven primarily by content acquisition costs (largely YouTube), depreciation expense, and other technical infrastructure operations costs; cost of revenues fell from 42% to 40% of revenues.
- Risk Factors (p.12): flags "downward pressure on our operating margin" from a higher level of investment in technical infrastructure, and cautions it "may not be able to continue to drive efficiencies at the rate we have in the past."
- Actuals (database): operating margin was essentially unchanged at 32.1% in FY2024 vs. 32.0% in FY2025, as 15% revenue growth outpaced the 11% rise in cost of revenues.

In short, Microsoft frames AI infrastructure as already compressing gross margin (Microsoft Cloud down to 69%) while operating margin still expanded, whereas Alphabet frames it as a forward-looking cost escalation (especially depreciation and energy) that pressures margins but was absorbed in FY2025 by revenue growth and datacenter efficiencies.

Sources: [MSFT FY2025 10-K, p.34], [MSFT FY2025 10-K, p.37], [MSFT FY2025 10-K, p.38], [MSFT FY2025 10-K, p.17], [GOOGL FY2025 10-K, p.30], [GOOGL FY2025 10-K, p.37], [GOOGL FY2025 10-K, p.34], [GOOGL FY2025 10-K, p.12], [SQL: income_statements]

---

## q_001#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Apple's total net revenue in fiscal year 2025?

**Gold:** $416.2 billion

**Grade:** answer's figure '$416.2 billion' matches 416161000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.3s, $0.0048*

**Answer:**

Apple's total net revenue in fiscal year 2025 was **$416.2 billion**.

- This covers the fiscal year from September 29, 2024 through September 27, 2025 (Apple's fiscal year ends in late September).

Sources: [SQL: income_statements]

---

## q_001#1: PASS (fuzzy_numeric, level 1)

**Question:** What was Apple's total net revenue in fiscal year 2025?

**Gold:** $416.2 billion

**Grade:** answer's figure '$416.2 billion' matches 416161000000 (usd)

**Claims the tools did not back:** unsupported: The figure is total net sales.; unsupported: The figure comprises both products and services.

*1 tool calls, 2.3s, $0.0022*

**Answer:**

Apple's total net revenue in fiscal year 2025 was **$416.2 billion**.

- This covers the fiscal year from September 29, 2024 through September 27, 2025 (Apple's fiscal year ends in late September).
- The figure is total net sales, comprising both products and services.

Sources: [SQL: income_statements]

---

## q_006#0: PASS (llm_judge, level 1)

**Question:** What were the primary risk factors Apple disclosed related to its supply chain in its fiscal year 2025 10-K filing?

**Gold:** Apple disclosed risks including: reliance on single or limited sources for components; dependence on third-party manufacturers; supply chain disruptions from geopolitical tensions, natural disasters, and health emergencies; component supply constraints affecting product availability; and risks from concentration of manufacturing operations in specific regions.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** unsupported: The filing discloses five primary supply chain-related risks.

*1 tool calls, 26.4s, $0.0179*

**Answer:**

Apple's FY2025 10-K (Item 1A, Risk Factors) discloses five primary supply chain–related risks: dependence on outsourced manufacturing concentrated in Asia, single/limited-source component supply, trade restrictions and new U.S. tariffs, business interruptions, and inventory/purchase-commitment exposure.

- **Dependence on outsourcing partners (p.10):** A significant majority of Apple's manufacturing is performed by outsourcing partners located primarily in China mainland, India, Japan, South Korea, Taiwan and Vietnam (plus U.S.-based sourcing). Apple relies on single-source partners in the U.S., Asia and Europe for many components and on partners primarily in Asia for final assembly of substantially all of its hardware products, and has outsourced much of its transportation and logistics. This reduces direct control over production and distribution, has at times adversely affected cost, quality or quantity, leaves Apple responsible for warranty service on defects, and exposes it to supplier code-of-conduct violations.

- **Obtaining components in sufficient quantities on commercially reasonable terms (pp.10–11):** Because Apple sources certain components from single or limited sources, it faces significant supply and pricing risks, including industrywide shortages and commodity price fluctuations (citing past global semiconductor shortages). New products often use custom components available from only one source, with initial capacity constraints until supplier yields mature; suppliers may fail, consolidate, or shift to common components, and Apple may not be able to renew supply agreements on similar terms or find alternative sources.

- **Trade restrictions, tariffs and geopolitical tensions (p.8):** Restrictions on international trade — tariffs and controls on imports/exports of goods, technology or data — can increase the cost or limit the availability of products, components, rare earths and other raw materials, and can force supplier changes that are expensive, time-consuming and disruptive. The filing specifically flags the new U.S. Tariffs announced beginning in Q2 2025 on imports from China, India, Japan, South Korea, Taiwan, Vietnam and the EU, threatened reciprocal/retaliatory measures, and a Section 232 investigation into semiconductor imports. It also notes global supply chains are highly concentrated and that escalating geopolitical tensions or conflict could cause significant disruptions.

- **Business interruptions (pp.8–9):** Political events, conflict, terrorism, natural disasters, public health issues and industrial accidents can make it difficult or impossible to manufacture and deliver products and create delays and inefficiencies in the supply and manufacturing chain. Many of Apple's and its suppliers' operations are in earthquake-prone locations, and because Apple relies on single or limited sources for many critical components, an interruption affecting those sources would exacerbate the consequences; insurance coverage may be insufficient.

- **Inventory write-downs and purchase-commitment risk (p.11):** Apple orders components and builds inventory in advance of product announcements, with manufacturing purchase obligations typically covering up to 150 days. Volatile, rapidly changing markets create the risk of forecasting incorrectly — ordering excess or insufficient components — leading to inventory write-downs, impairments of capital assets held at suppliers' facilities and inventory prepayments, and purchase-commitment cancellation fee reserves.

- Related disclosures: Apple also notes its global supply chain depends on complex IT systems whose failure could impede manufacturing and shipping (p.13), and that its global suppliers are exposed to ransomware and other malicious attacks that can disrupt business operations (pp.13–14).

Sources: [AAPL FY2025 10-K, p.8], [AAPL FY2025 10-K, p.9], [AAPL FY2025 10-K, p.10], [AAPL FY2025 10-K, p.11], [AAPL FY2025 10-K, p.13]

---

## q_006#1: PASS (llm_judge, level 1)

**Question:** What were the primary risk factors Apple disclosed related to its supply chain in its fiscal year 2025 10-K filing?

**Gold:** Apple disclosed risks including: reliance on single or limited sources for components; dependence on third-party manufacturers; supply chain disruptions from geopolitical tensions, natural disasters, and health emergencies; component supply constraints affecting product availability; and risks from concentration of manufacturing operations in specific regions.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** unsupported: Apple's FY2025 10-K Item 1A discloses five primary supply chain risk factors: dependence on outsourced manufacturing concentrated in Asia, single/limited-source component supply, tariffs and trade restrictions, business interruptions, and inventory write-down/purchase commitment exposure.

*1 tool calls, 24.1s, $0.0164*

**Answer:**

Apple's FY2025 10-K (Item 1A) discloses five primary supply chain risk factors: dependence on outsourced manufacturing concentrated in Asia, single/limited-source component supply, tariffs and trade restrictions, business interruptions, and inventory write-down/purchase commitment exposure.

- **Dependence on outsourcing partners (p.10):** A significant majority of Apple's manufacturing is performed by outsourcing partners located primarily in China mainland, India, Japan, South Korea, Taiwan and Vietnam (plus U.S. partners). Apple relies on single-source partners in the U.S., Asia and Europe for many components, and on partners primarily in Asia for final assembly of substantially all hardware products. It has also outsourced much of its transportation and logistics management. These arrangements reduce Apple's direct control over production and distribution, can affect cost, quality or quantity, and Apple remains responsible for warranty service despite defect-reimbursement provisions. Supplier code of conduct violations occur from time to time.

- **Component availability and pricing (pp.10–11):** Because Apple obtains certain components from single or limited sources, it faces significant supply and pricing risks, including industrywide shortages and commodity price fluctuations — the filing cites past global semiconductor shortages. New products often use custom components available from only one source, with initial capacity constraints until supplier yields mature. Suppliers may fail, consolidate, or shift to common components, and Apple may not be able to renew supply agreements on similar terms or find alternative sources.

- **Trade restrictions and tariffs (p.8):** Restrictions on international trade (tariffs and import/export controls on goods, technology or data) can increase the cost or limit the availability of products, components, rare earths and other raw materials, and can force supplier changes that are expensive, time-consuming and disruptive. Beginning in Q2 2025, new U.S. tariffs were announced on imports from China, India, Japan, South Korea, Taiwan, Vietnam and the EU, with several countries imposing or threatening reciprocal tariffs; the U.S. Department of Commerce also initiated a Section 232 investigation into semiconductor imports. The filing notes global supply chains are highly concentrated and that escalating geopolitical tensions or conflict could cause significant disruptions.

- **Business interruptions (pp.8–9):** Apple's and its suppliers' operations are in locations prone to earthquakes and other natural disasters (intensified by climate change), plus fires, power shortages, industrial accidents, terrorist attacks, ransomware, labor disputes and public health issues. Because Apple relies on single or limited sources for many critical components, an interruption affecting those sources would exacerbate the consequences; recovery can require substantial time and expenditures, and insurance may be insufficient.

- **Inventory write-downs and purchase commitments (p.11):** Apple orders components and builds inventory in advance of product announcements, with manufacturing purchase obligations typically covering up to 150 days. Volatile markets and rapid technology/price changes create the risk of forecasting incorrectly — ordering excess or insufficient components — and of not fully utilizing purchase commitments, requiring cancellation fee reserves.

- Related risks also touch the supply chain: design and manufacturing defects in components purchased from third parties (p.11), and IT system failures or ransomware attacks on Apple or its global suppliers that can impede manufacturing and shipping (p.13).

Sources: [AAPL FY2025 10-K, p.8], [AAPL FY2025 10-K, p.9], [AAPL FY2025 10-K, p.10], [AAPL FY2025 10-K, p.11], [AAPL FY2025 10-K, p.13]

---

## q_008#0: PASS (fuzzy_numeric, level 2)

**Question:** What percentage of Microsoft's total revenue came from the United States in fiscal year 2025?

**Gold:** 51.3%

**Grade:** answer's figure '51.3%' matches 51.3 (pct)

**Claims the tools did not back:** none

*4 tool calls, 6.6s, $0.0064*

**Answer:**

About 51.3% of Microsoft's total revenue in fiscal year 2025 came from the United States.

- U.S. revenue: $144.5 billion of $281.7 billion total revenue (FY2025, ended June 30, 2025).
- The remainder, $137.2 billion, came from other countries, or 48.7% of total revenue.

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

## q_008#1: PASS (fuzzy_numeric, level 2)

**Question:** What percentage of Microsoft's total revenue came from the United States in fiscal year 2025?

**Gold:** 51.3%

**Grade:** answer's figure '51.3%' matches 51.3 (pct)

**Claims the tools did not back:** none

*4 tool calls, 5.9s, $0.0063*

**Answer:**

About 51.3% of Microsoft's total FY2025 revenue came from the United States.

- U.S. revenue: $144.5 billion of $281.7 billion total revenue (fiscal year ended June 30, 2025).
- The remaining $137.2 billion, or 48.7%, came from other countries.

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

## q_011#0: PASS (exact_match_entity, level 2)

**Question:** Which company had the fastest revenue growth rate between their two most recent fiscal years, and what was the growth rate?

**Gold:** Alphabet (GOOGL) had the fastest revenue growth between the two most recent fiscal years at about 15.1%.

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%'

**Claims the tools did not back:** none

*2 tool calls, 6.6s, $0.0071*

**Answer:**

Alphabet (GOOGL) had the fastest revenue growth between its two most recent fiscal years, at 15.1% (FY2024 → FY2025).

- **Alphabet:** $350.0 billion → $402.8 billion, +15.1%
- **Microsoft:** $245.1 billion → $281.7 billion, +14.9% (a close second)
- **Apple:** $391.0 billion → $416.2 billion, +6.4%

Note that the fiscal years cover different calendar months (Apple's ends late September, Microsoft's June 30, Alphabet's December 31), so the periods are not perfectly aligned.

Sources: [SQL: income_statements]

---

## q_011#1: PASS (exact_match_entity, level 2)

**Question:** Which company had the fastest revenue growth rate between their two most recent fiscal years, and what was the growth rate?

**Gold:** Alphabet (GOOGL) had the fastest revenue growth between the two most recent fiscal years at about 15.1%.

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%'

**Claims the tools did not back:** none

*2 tool calls, 7.3s, $0.0076*

**Answer:**

Alphabet (GOOGL) had the fastest revenue growth between its two most recent fiscal years, at 15.1% (FY2024 → FY2025).

- **Alphabet:** revenue grew from $350.0 billion to $402.8 billion, a 15.1% increase — the fastest of the three.
- **Microsoft:** revenue grew from $245.1 billion to $281.7 billion, a 14.9% increase — a close second.
- **Apple:** revenue grew from $391.0 billion to $416.2 billion, a 6.4% increase — the slowest of the three.

Note that fiscal years cover different calendar months: Apple's FY2025 ended in late September 2025, Microsoft's on June 30, 2025, and Alphabet's on December 31, 2025.

Sources: [SQL: income_statements]

---

## q_012#0: PASS (llm_judge, level 3)

**Question:** How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and does the 10-K filing explain why?

**Gold:** Apple's Greater China revenue decreased from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of approximately 3.8%. The FY2025 10-K states this was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: This is consistent with the iPhone-driven decline.

*3 tool calls, 13.4s, $0.0184*

**Answer:**

Apple's Greater China net sales fell from $66.95 billion in FY2024 to $64.38 billion in FY2025 — a decline of $2.6 billion, or 3.8% (shown as (4)% in the 10-K) — and yes, the FY2025 10-K explains the decrease.

- **FY2024 (ended September 28, 2024):** $66,952 million in Greater China net sales.
- **FY2025 (ended September 27, 2025):** $64,377 million, a decrease of $2,575 million (-3.8%).
- **Why (per the 10-K, MD&A – Segment Operating Performance):** "Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
- The filing also notes (Note 2 – Revenue) that in Greater China, iPhone revenue represented a moderately higher proportion of net sales than in other segments, which is consistent with the iPhone-driven decline.
- Note: Greater China is one of Apple's five geographic reportable segments (Americas, Europe, Greater China, Japan, Rest of Asia Pacific); the figures above are segment net sales, not product-category revenue.

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.37]

---

## q_012#1: PASS (llm_judge, level 3)

**Question:** How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and does the 10-K filing explain why?

**Gold:** Apple's Greater China revenue decreased from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of approximately 3.8%. The FY2025 10-K states this was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: The iPhone decline weighed more heavily in Greater China.

*3 tool calls, 15.0s, $0.0139*

**Answer:**

Apple's Greater China net sales fell from $66.95 billion in FY2024 to $64.38 billion in FY2025 — a decline of $2.6 billion, or 3.8% (shown as (4)% in the 10-K) — and yes, the FY2025 10-K explains the decrease.

- **FY2024 (ended Sept 28, 2024):** $66,952 million; **FY2025 (ended Sept 27, 2025):** $64,377 million, per the database and the 10-K's segment table (Greater China is one of Apple's five reportable geographic segments).
- **Why (per the 10-K, MD&A "Greater China"):** "Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
- **Context:** Note 2 (Revenue) adds that in Greater China, iPhone revenue represented a moderately higher proportion of net sales than in other segments, so the iPhone decline weighed more heavily there. This was the second consecutive annual decline (Greater China was down 8% in FY2024 from $72,559 million in FY2023), even as Apple's total net sales grew 6% to $416.2 billion in FY2025.

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.37]; [AAPL FY2025 10-K, p.48]

---

## q_014#0: PASS (llm_judge, level 3)

**Question:** Microsoft restructured its segment reporting in August 2024. How are the three segments defined in the fiscal year 2025 10-K, and what was the revenue for each?

**Gold:** The three segments in the FY2025 10-K are: (1) Productivity and Business Processes ($120.8B) - includes Microsoft 365 Commercial/Consumer, LinkedIn, and Dynamics; (2) Intelligent Cloud ($106.3B) - includes Azure, SQL Server, Windows Server, GitHub, and enterprise services; (3) More Personal Computing ($54.6B) - includes Windows, Devices, Gaming, and Search/news advertising.

**Grade:** 19/19 facts covered

**Claims the tools did not back:** none

*5 tool calls, 29.9s, $0.0317*

**Answer:**

In its FY2025 10-K, Microsoft reports three segments — Productivity and Business Processes, Intelligent Cloud, and More Personal Computing — with FY2025 revenue of $120.8 billion, $106.3 billion, and $54.6 billion, respectively (total $281.7 billion). The August 2024 changes "align our segments with how we currently manage our business, most notably bringing the commercial components of Microsoft 365 together in the Productivity and Business Processes segment," and prior-period segment information has been recast to conform.

**Segment definitions and FY2025 revenue (per the FY2025 10-K, with figures matching the database):**

- **Productivity and Business Processes — $120.8 billion** (FY2024 recast: $106.8 billion, +13%): products and services in the portfolio of productivity, communication, and information services. Comprises Microsoft 365 Commercial products and cloud services (Microsoft 365 Commercial cloud — including Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot — plus Windows Commercial on-premises and Office licensed on-premises); Microsoft 365 Consumer products and cloud services; LinkedIn; and Dynamics products and cloud services (Dynamics 365 and on-premises ERP/CRM).
- **Intelligent Cloud — $106.3 billion** (FY2024 recast: $87.5 billion, +21%): public, private, and hybrid server products and cloud services that power modern business and developers. Comprises server products and cloud services (Azure and other cloud services — cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings — plus SQL Server, Windows Server, Visual Studio, System Center, and related CALs) and Enterprise and partner services (Enterprise Support Services, Industry Solutions, Nuance professional services, Microsoft Partner Network, Learning Experience).
- **More Personal Computing — $54.6 billion** (FY2024 recast: $50.8 billion, +7%): products and services that put customers at the center of the experience with Microsoft's technology. Comprises Windows and Devices (Windows OEM licensing, Surface and PC accessories); Gaming (Xbox hardware and Xbox content and services, including Xbox Game Pass and other subscriptions and Xbox Cloud Gaming); and Search and news advertising (Bing and Copilot, Microsoft News, Microsoft Edge, and third-party affiliates).

Note: because of the recast, these FY2024 comparatives differ from the segment figures Microsoft originally reported in its FY2024 10-K under the old segment definitions; the database and FY2025 10-K both use the new (restated) definitions.

Sources: [SQL: segment_revenue], [MSFT FY2025 10-K, p.5], [MSFT FY2025 10-K, p.7], [MSFT FY2025 10-K, p.8], [MSFT FY2025 10-K, p.35], [MSFT FY2025 10-K, p.37]

---

## q_014#1: PASS (llm_judge, level 3)

**Question:** Microsoft restructured its segment reporting in August 2024. How are the three segments defined in the fiscal year 2025 10-K, and what was the revenue for each?

**Gold:** The three segments in the FY2025 10-K are: (1) Productivity and Business Processes ($120.8B) - includes Microsoft 365 Commercial/Consumer, LinkedIn, and Dynamics; (2) Intelligent Cloud ($106.3B) - includes Azure, SQL Server, Windows Server, GitHub, and enterprise services; (3) More Personal Computing ($54.6B) - includes Windows, Devices, Gaming, and Search/news advertising.

**Grade:** 19/19 facts covered

**Claims the tools did not back:** none

*6 tool calls, 39.1s, $0.0362*

**Answer:**

In its FY2025 10-K, Microsoft reports three segments — Productivity and Business Processes, Intelligent Cloud, and More Personal Computing — with FY2025 revenue of $120.8 billion, $106.3 billion, and $54.6 billion, respectively (totaling the $281.7 billion consolidated revenue). The August 2024 changes most notably brought the commercial components of Microsoft 365 together in the Productivity and Business Processes segment, and prior-period segment information was recast to conform.

**Segment definitions (FY2025 10-K, Item 1):**

- **Productivity and Business Processes — $120.8 billion (FY2025).** Products and services in Microsoft's portfolio of productivity, communication, and information services, spanning a variety of devices and platforms. It comprises: (1) Microsoft 365 Commercial products and cloud services — Microsoft 365 Commercial cloud (Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot) plus Microsoft 365 Commercial products (Windows Commercial on-premises and Office licensed on-premises); (2) Microsoft 365 Consumer products and cloud services (Microsoft 365 Consumer subscriptions, Office licensed on-premises, and other consumer services); (3) LinkedIn (Talent Solutions, Marketing Solutions, Premium Subscriptions, Sales Solutions); and (4) Dynamics products and cloud services (Dynamics 365 across ERP, CRM, Power Apps, and Power Automate, plus on-premises ERP and CRM applications).

- **Intelligent Cloud — $106.3 billion (FY2025).** Public, private, and hybrid server products and cloud services that power modern business and developers. It comprises: (1) Server products and cloud services — Azure and other cloud services (cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings, and other cloud services) plus server products (SQL Server, Windows Server, Visual Studio, System Center, related Client Access Licenses, and other on-premises offerings); and (2) Enterprise and partner services (Enterprise Support Services, Industry Solutions, Nuance professional services, Microsoft Partner Network, and Learning Experience).

- **More Personal Computing — $54.6 billion (FY2025).** Products and services that put customers at the center of the experience with Microsoft's technology. It comprises: (1) Windows and Devices — Windows OEM licensing (Windows Pro and non-Pro licenses sold through the OEM channel) and Devices (Surface and PC accessories); (2) Gaming — Xbox hardware and Xbox content and services (first- and third-party content including games and in-game content, Xbox Game Pass and other subscriptions, Xbox Cloud Gaming, advertising, and other cloud services); and (3) Search and news advertising — Bing and Copilot, Microsoft News, Microsoft Edge, and third-party affiliates.

**Notes on the restatement:** Beginning in FY2025, the information the chief operating decision maker reviews reflects the new segment composition; the recast primarily affected Note 8 (Goodwill), Note 12 (Unearned Revenue), and Note 18 (Segment Information and Geographic Data). On the recast basis, FY2024 segment revenue was $106.8 billion (Productivity and Business Processes), $87.5 billion (Intelligent Cloud), and $50.8 billion (More Personal Computing), summing to the $245.1 billion FY2024 consolidated total. These recast figures differ from the segment amounts originally reported in the FY2024 10-K under the old definitions.

Sources: [SQL: segment_revenue], [SQL: income_statements], [MSFT FY2025 10-K, p.5], [MSFT FY2025 10-K, p.8], [MSFT FY2025 10-K, p.35], [MSFT FY2025 10-K, p.51], [MSFT FY2025 10-K, p.78]

---

## q_017#0: PASS (llm_judge, level 3)

**Question:** According to Alphabet's 10-K filings, what are the key components of 'Google Services' revenue, and how did YouTube advertising revenue change between FY2024 and FY2025?

**Gold:** Google Services includes Google Search & other, YouTube ads, Google Network, and Google subscriptions/platforms/devices. YouTube advertising revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of approximately 11.7%.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*4 tool calls, 16.7s, $0.0180*

**Answer:**

Per Alphabet's FY2025 10-K, Google Services revenue comprises **Google advertising** (Google Search & other, YouTube ads, and Google Network) plus **Google subscriptions, platforms, and devices**, and YouTube ads revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of $4.2 billion (+11.7%).

**Key components of Google Services revenue (FY2025, per the 10-K revenue table):**
- **Google Search & other** — $224.5 billion: revenues from Google search properties (including traffic from search distribution partners using Google.com as default search) and other owned/operated properties like Gmail, Google Maps, and Google Play.
- **YouTube ads** — $40.4 billion: revenues generated on YouTube properties.
- **Google Network** — $29.8 billion: revenues from Google Network properties participating in AdMob, AdSense, and Google Ad Manager.
- These three make up **Google advertising** at $294.7 billion.
- **Google subscriptions, platforms, and devices** — $48.0 billion: consumer subscription products (e.g., YouTube TV, YouTube Music and Premium, NFL Sunday Ticket, Google One), sale of apps and in-app purchases, and devices.
- **Google Services total** — $342.7 billion in FY2025, up from $304.9 billion in FY2024 (matching the database's segment figures).

**YouTube ads change (FY2024 → FY2025):**
- Revenue rose from $36,147 million to $40,367 million — an increase of $4,220 million, or 11.7%.
- The filing attributes the growth to **direct response advertising products, followed by brand advertising products**, both of which benefited from increased spending by advertisers.

Sources: [GOOGL FY2025 10-K, p.35], [GOOGL FY2025 10-K, p.36], [GOOGL FY2025 10-K, p.31], [GOOGL FY2025 10-K, p.87], [SQL: segment_revenue]

---

## q_017#1: PASS (llm_judge, level 3)

**Question:** According to Alphabet's 10-K filings, what are the key components of 'Google Services' revenue, and how did YouTube advertising revenue change between FY2024 and FY2025?

**Gold:** Google Services includes Google Search & other, YouTube ads, Google Network, and Google subscriptions/platforms/devices. YouTube advertising revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of approximately 11.7%.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*4 tool calls, 16.6s, $0.0175*

**Answer:**

Per Alphabet's FY2025 10-K, Google Services revenue has two key components — Google advertising (Google Search & other, YouTube ads, and Google Network) and Google subscriptions, platforms, and devices — and YouTube ads revenue grew $4.2 billion, from $36.1 billion in FY2024 to $40.4 billion in FY2025 (+11.7%).

**Key components of Google Services revenue (FY2025 10-K, revenues by type):**
- **Google advertising — $294.7 billion in FY2025** (vs. $264.6 billion in FY2024), comprising:
  - Google Search & other: $224.5 billion (revenues on Google search properties, including traffic from search distribution partners, plus other owned/operated properties like Gmail, Google Maps, and Google Play)
  - YouTube ads: $40.4 billion (revenues generated on YouTube properties)
  - Google Network: $29.8 billion (revenues on Google Network properties participating in AdMob, AdSense, and Google Ad Manager)
- **Google subscriptions, platforms, and devices — $48.0 billion in FY2025** (vs. $40.3 billion in FY2024): consumer subscription products (e.g., YouTube TV, YouTube Music and Premium, NFL Sunday Ticket, Google One), sale of apps and in-app purchases, and devices.
- These sum to Google Services total revenue of $342.7 billion in FY2025, up from $304.9 billion in FY2024 (consistent with the database's segment figures).

**YouTube ads change (FY2024 → FY2025):**
- Increased $4.2 billion, from $36,147 million to $40,367 million, a growth rate of 11.7%.
- The filing attributes the growth to direct response advertising products, followed by brand advertising products, both of which benefited from increased spending by advertisers.

Sources: [GOOGL FY2025 10-K, p.35], [GOOGL FY2025 10-K, p.31], [GOOGL FY2025 10-K, p.36], [GOOGL FY2025 10-K, p.87], [SQL: segment_revenue]

---

## q_018#0: PASS (exact_match_entity, level 2)

**Question:** Which company has the highest current ratio (current assets / current liabilities) in their most recent fiscal year?

**Gold:** Alphabet (GOOGL) has the highest current ratio in the most recent fiscal year (about 2.01x).

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01'

**Claims the tools did not back:** none

*1 tool calls, 3.0s, $0.0030*

**Answer:**

Alphabet (GOOGL) has the highest current ratio in FY2025, at 2.01.

- **GOOGL:** $206.0 billion current assets / $102.7 billion current liabilities = **2.01**
- **MSFT:** $191.1 billion / $141.2 billion = **1.35**
- **AAPL:** $148.0 billion / $165.6 billion = **0.89** (Apple is the only one of the three with current liabilities exceeding current assets)

Note: fiscal years differ — Apple's FY2025 ended late September 2025, Microsoft's June 30, 2025, and Alphabet's December 31, 2025.

Sources: [SQL: balance_sheets]

---

## q_018#1: PASS (exact_match_entity, level 2)

**Question:** Which company has the highest current ratio (current assets / current liabilities) in their most recent fiscal year?

**Gold:** Alphabet (GOOGL) has the highest current ratio in the most recent fiscal year (about 2.01x).

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01'

**Claims the tools did not back:** none

*1 tool calls, 3.6s, $0.0032*

**Answer:**

Alphabet (GOOGL) has the highest current ratio in FY2025, at 2.01.

- **GOOGL** (FY ended Dec 31, 2025): $206.0 billion current assets / $102.7 billion current liabilities = **2.01**
- **MSFT** (FY ended Jun 30, 2025): $191.1 billion / $141.2 billion = **1.35**
- **AAPL** (FY ended Sep 27, 2025): $148.0 billion / $165.6 billion = **0.89** — the only one below 1.0, meaning current liabilities exceed current assets

Note the fiscal years end in different months (June for Microsoft, September for Apple, December for Alphabet), so the ratios are measured at different points in calendar 2025.

Sources: [SQL: balance_sheets]

---

## q_022#0: PASS (llm_judge, level 4)

**Question:** Across all three companies, which saw the largest absolute dollar increase in revenue between their two most recent fiscal years? Break down how much of that increase came from each business segment.

**Gold:** Alphabet had the largest absolute increase at approximately $52.8B ($350.0B to $402.8B). By operating segment, Google Services grew by $37.8B ($304.9B to $342.7B), Google Cloud grew by $15.5B ($43.2B to $58.7B), and Other Bets declined by $0.1B ($1.6B to $1.5B); a hedging reconciliation of approximately -$0.3B accounts for the difference between the segment subtotal and consolidated revenue. Microsoft increased by $36.6B and Apple by $25.1B.

**Grade:** 8/8 facts covered

**Claims the tools did not back:** none

*3 tool calls, 18.3s, $0.0137*

**Answer:**

**Alphabet (GOOGL) saw the largest absolute revenue increase: $52.8 billion (from $350.0 billion in FY2024 to $402.8 billion in FY2025), ahead of Microsoft's $36.6 billion and Apple's $25.1 billion.**

Company-level comparison (FY2024 → FY2025):
- **GOOGL:** $350.0B → $402.8B, **+$52.8B**
- **MSFT:** $245.1B → $281.7B, **+$36.6B**
- **AAPL:** $391.0B → $416.2B, **+$25.1B**

Segment breakdown of Alphabet's $52.8 billion increase:
- **Google Services: +$37.8 billion** ($304.9B → $342.7B) — about 71.5% of the total increase
- **Google Cloud: +$15.5 billion** ($43.2B → $58.7B) — about 29.3% of the total increase
- **Other Bets: –$0.1 billion** ($1.6B → $1.5B) — a slight decline
- **Hedging gains (losses): –$0.3 billion** ($0.2B → –$0.1B) — a reconciling item, not a segment, but it reduces the consolidated total

These components sum exactly to the $52.8 billion consolidated increase. Note that fiscal years differ: Alphabet's FY2025 ended December 31, 2025, Microsoft's June 30, 2025, and Apple's late September 2025, so the periods cover different calendar months.

Sources: [SQL: income_statements], [SQL: segment_revenue]

---

## q_022#1: PASS (llm_judge, level 4)

**Question:** Across all three companies, which saw the largest absolute dollar increase in revenue between their two most recent fiscal years? Break down how much of that increase came from each business segment.

**Gold:** Alphabet had the largest absolute increase at approximately $52.8B ($350.0B to $402.8B). By operating segment, Google Services grew by $37.8B ($304.9B to $342.7B), Google Cloud grew by $15.5B ($43.2B to $58.7B), and Other Bets declined by $0.1B ($1.6B to $1.5B); a hedging reconciliation of approximately -$0.3B accounts for the difference between the segment subtotal and consolidated revenue. Microsoft increased by $36.6B and Apple by $25.1B.

**Grade:** 8/8 facts covered

**Claims the tools did not back:** none

*3 tool calls, 26.1s, $0.0209*

**Answer:**

**Alphabet (GOOGL) saw the largest absolute revenue increase: +$52.8 billion, from $350.0 billion in FY2024 to $402.8 billion in FY2025** — ahead of Microsoft (+$36.6 billion, $245.1B → $281.7B) and Apple (+$25.1 billion, $391.0B → $416.2B).

How Alphabet's $52.8 billion increase breaks down by segment:
- **Google Services: +$37.8 billion** ($304.9B → $342.7B), about 71.5% of the total increase — the dominant driver.
- **Google Cloud: +$15.5 billion** ($43.2B → $58.7B), about 29.3% of the increase.
- **Other Bets: –$0.1 billion** ($1.6B → $1.5B), a small drag.
- **Hedging gains (losses): –$0.3 billion** ($0.2B → –$0.1B) — this is a reconciling item, not a segment; segments plus hedging sum to consolidated revenue.

Notes: Alphabet's fiscal year ends December 31, while Apple's ends late September and Microsoft's June 30, so the periods cover different calendar months. Microsoft's segment figures above reflect the segment definitions restated in its FY2025 10-K (August 2024 reorganization).

Sources: [SQL: income_statements], [SQL: segment_revenue]

---

## q_025#0: PASS (llm_judge, level 4)

**Question:** Apple's Services segment has been growing as a share of total revenue. Calculate the Services revenue growth rate for each of the last two years, compare it to iPhone revenue growth, and find what Apple's 10-K says about the strategic importance of Services.

**Gold:** Services growth: FY2023->FY2024: 12.9% ($85.2B to $96.2B), FY2024->FY2025: 13.5% ($96.2B to $109.2B). iPhone growth: FY2023->FY2024: 0.3%, FY2024->FY2025: 4.2%. Services is consistently growing much faster. The 10-K highlights Services as a key growth driver with higher margins, recurring revenue from subscriptions, App Store, Apple Music, iCloud, and advertising.

**Grade:** 10/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions

**Claims the tools did not back:** unsupported: Profitability underscores the strategic weight of Services.

*8 tool calls, 44.6s, $0.0447*

**Answer:**

Apple's Services revenue grew 12.9% in FY2024 and 13.5% in FY2025, far outpacing iPhone growth of 0.3% and 4.2% in those years, lifting Services to 26.2% of total revenue in FY2025.

- **Growth comparison (note: "Services" and "iPhone" are Apple's product/service categories, not its reportable segments, which are geographic):** Services rose from $85.2 billion (FY2023) to $96.2 billion (FY2024, +12.9%) to $109.2 billion (FY2025, +13.5%), while iPhone went from $200.6 billion to $201.2 billion (+0.3%) to $209.6 billion (+4.2%). Services outgrew iPhone in both years.
- **Rising share of revenue:** Services climbed from 22.2% of total net sales in FY2023 to 24.6% in FY2024 and 26.2% in FY2025 (total net sales $383.3 billion → $391.0 billion → $416.2 billion).
- **What the 10-K says about Services' strategic role:** In Item 1, Apple describes itself as selling "a variety of related services" — advertising, AppleCare, cloud services, digital content (the App Store plus subscriptions such as Apple Arcade, Fitness+, Music, News+ and TV), and payment services (Apple Card, Apple Pay) — and states it "is focused on expanding its market opportunities related to smartphones, personal computers, tablets, wearables and accessories, and services." It emphasizes that it "designs and develops nearly the entire solution for its products, including the hardware, operating system, numerous software applications and related services," positioning services as integral to its integrated offering.
- **Profitability underscores the strategic weight:** Per the MD&A, Services gross margin was 75.4% in FY2025 (up from 73.9% in FY2024 and 70.8% in FY2023) versus 36.8% for Products, with Services gross margin of $82.3 billion in FY2025; the FY2025 increase was driven primarily by higher net sales from advertising, the App Store and cloud services (iPhone's increase was driven by Pro models). The 10-K also notes Services net sales include amortization of deferred value of services bundled in certain product prices.

Not verified: the FY2024 10-K's own commentary on the FY2023→FY2024 Services drivers (the FY2025 10-K explains only the FY2025 vs. FY2024 change), and Apple makes no single explicit "strategic importance of Services" declaration — the framing above is drawn from the Business, Competition and MD&A sections cited.

Sources: [SQL: segment_revenue], [SQL: income_statements], [AAPL FY2025 10-K, p.4-5], [AAPL FY2025 10-K, p.24-25]

---

## q_025#1: PASS (llm_judge, level 4)

**Question:** Apple's Services segment has been growing as a share of total revenue. Calculate the Services revenue growth rate for each of the last two years, compare it to iPhone revenue growth, and find what Apple's 10-K says about the strategic importance of Services.

**Gold:** Services growth: FY2023->FY2024: 12.9% ($85.2B to $96.2B), FY2024->FY2025: 13.5% ($96.2B to $109.2B). iPhone growth: FY2023->FY2024: 0.3%, FY2024->FY2025: 4.2%. Services is consistently growing much faster. The 10-K highlights Services as a key growth driver with higher margins, recurring revenue from subscriptions, App Store, Apple Music, iCloud, and advertising.

**Grade:** 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions

**Claims the tools did not back:** unsupported: Services is margin accretive.; unsupported: Services is a growing, higher-margin complement to hardware.; unsupported: Services deepen customer lock-in across the installed base.

*7 tool calls, 36.4s, $0.0277*

**Answer:**

Apple's Services category grew 12.9% in FY2024 and 13.5% in FY2025 — far outpacing iPhone, which grew just 0.3% and 4.2% in those years — lifting Services from 22.2% to 26.2% of total net sales over two years. (Note: Apple's reportable segments are geographic; "Services" and "iPhone" here are the product/service categories in the 10-K's net-sales-by-category table.)

**Growth rates (fiscal years ending late September)**

| Category | FY2024 | FY2025 |
|---|---|---|
| Services | $96.2B, +12.9% (10-K: 13%) | $109.2B, +13.5% (10-K: 14%) |
| iPhone | $201.2B, +0.3% (10-K: ~0%) | $209.6B, +4.2% (10-K: 4%) |

- Services grew roughly 43x faster than iPhone in FY2024 ($96.2B vs. $85.2B prior year, vs. iPhone's $201.2B vs. $200.6B) and about 3x faster in FY2025.
- As a share of total net sales ($416.2B in FY2025), Services rose from 22.2% (FY2023) to 24.6% (FY2024) to 26.2% (FY2025), while iPhone still accounted for 50.4% of FY2025 revenue.

**What the 10-K says about Services' strategic importance**

- **Growth drivers (MD&A, FY2025 10-K):** Services net sales increased in 2025 "primarily due to higher net sales from advertising, the App Store and cloud services" — the same drivers cited for 2024 vs. 2023 in the FY2024 10-K.
- **Margin accretive:** Services gross margin increased in both 2025 and 2024, with the gross margin percentage rising "primarily due to a different mix of services" — i.e., Services is a growing, higher-margin complement to hardware.
- **Ecosystem breadth (Item 1, Business):** Apple describes a broad services portfolio built around its devices — advertising platforms, AppleCare support, cloud services that keep content synced "across multiple Apple devices," the App Store, subscription content (Apple Music, Apple TV, Apple Arcade, Apple Fitness+, Apple News+), and payment services (Apple Card, Apple Pay).
- **Competitive positioning:** In its Competition discussion, Apple lists "a strong third-party software and accessories ecosystem" and service features/quality among its principal competitive factors, underscoring that services deepen customer lock-in across the installed base.

Sources: [SQL: segment_revenue], [SQL: income_statements], [AAPL FY2025 10-K, p.24-25], [AAPL FY2025 10-K, p.4-5], [AAPL FY2024 10-K, p.25]

---

## x_014#0: PASS (llm_judge, level 1)

**Question:** What risks related to artificial intelligence does Microsoft disclose in its fiscal year 2025 10-K?

**Gold:** Microsoft's FY2025 10-K discloses AI risks including: intense and rapidly evolving competition in AI, including from open AI models; significant costs to build AI and cloud infrastructure that reduce operating margins; flawed algorithms, biased or inaccurate datasets, and harmful or inaccurate AI-generated content that could cause reputational or competitive harm or legal liability; misuse of its AI systems and services by users; emerging AI regulation such as the EU AI Act that could increase costs or restrict opportunity; and intellectual property claims arising from AI training and output.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: Some competitors distribute open AI models at little or no cost.

*7 tool calls, 39.2s, $0.0372*

**Answer:**

Microsoft's FY2025 10-K discloses AI-related risks throughout Item 1A, headlined by a dedicated risk factor — "Issues in the development, deployment, and use of AI may result in reputational or competitive harm or liability" — plus AI-specific competition, execution, misuse, security, infrastructure, and regulatory risks.

- **Development and deployment flaws (dedicated AI risk factor, p.23):** AI algorithms or training methodologies may be flawed; datasets may be overbroad, insufficient, or contain biased or inaccurate information; AI-generated content may be offensive, illegal, inaccurate, or otherwise harmful. Ineffective AI practices by Microsoft or others (including strategic partner OpenAI) could cause incidents that impair acceptance of AI solutions or harm individuals, customers, or society. Human review may be required, including for agentic AI systems that act autonomously. Risks stem from intellectual property, data privacy, and other claims associated with AI training and outputs, compounded by an evolving regulatory landscape (including new EU laws), ethical issues with broad societal impacts, and rising global divergence in how to address them. AI solutions with unintended consequences, or contrary to Microsoft's responsible AI policies, could hurt its reputation, competitive position, and results.

- **Competition and execution (p.17):** AI is "a highly competitive and rapidly evolving market" with new competitors continually entering; Microsoft bears significant development and operational costs to build AI models, services, platforms, and infrastructure, and some competitors distribute open AI models at little or no cost. Its focus on cloud-based and AI services presents execution risks — significant infrastructure costs are reducing operating margins, and it is uncertain whether strategies will attract users or generate revenue in line with these investments.

- **Misuse and abuse (p.18, p.22):** AI systems may be used in unintended or inappropriate ways, and users may engage in fraudulent or abusive activities through cloud and AI services (unauthorized account access, payment fraud, cryptocurrency mining, launching cyberattacks); detection efforts may not be effective, risking reputational damage. Users may also impersonate people or organizations through AI technologies, and customers may deploy Microsoft's AI products in high-risk scenarios or use them inappropriately.

- **Security (p.19–20):** Threat actors may use AI and machine learning in attacks; increasing use of generative AI models in Microsoft's internal systems may create new attack surfaces or methods for adversaries; and features that rely on generative AI can be susceptible to security threats.

- **Infrastructure and supply (p.23–24):** Datacenter demands continue to increase as AI features are incorporated into services, and datacenters depend on permitted land, predictable energy, networking supplies, and servers including graphics processing units. There are limited suppliers for certain datacenter components, and capacity may be constrained as competitors use the same suppliers amid growing demand for AI services; shortages could leave inadequate datacenter capacity to support AI product delivery and development.

- **Legal, regulatory, and litigation (p.24–27):** Emerging AI legislation and regulation could increase costs or restrict opportunity — e.g., the EU AI Act may increase costs or impact provision/operation of AI models and services in Europe, with regulatory focus on model/system development and deployment, frontier model safety, transparency, and content provenance. Shifting U.S. AI export controls (the AI Diffusion Rule and potential replacement rulemakings) could raise costs, create continuity uncertainty, and accelerate sovereignty initiatives abroad. Claims and lawsuits may arise from AI services, and third parties may assert copyright infringement and other claims arising from AI training and output. Public scrutiny of AI development and deployment decisions and responsible AI failures could also damage Microsoft's reputation and brands (p.27).

Sources: [MSFT FY2025 10-K, p.17], [MSFT FY2025 10-K, p.18], [MSFT FY2025 10-K, p.19], [MSFT FY2025 10-K, p.20], [MSFT FY2025 10-K, p.22], [MSFT FY2025 10-K, p.23], [MSFT FY2025 10-K, p.24], [MSFT FY2025 10-K, p.25], [MSFT FY2025 10-K, p.26], [MSFT FY2025 10-K, p.27]

---

## x_014#1: PASS (llm_judge, level 1)

**Question:** What risks related to artificial intelligence does Microsoft disclose in its fiscal year 2025 10-K?

**Gold:** Microsoft's FY2025 10-K discloses AI risks including: intense and rapidly evolving competition in AI, including from open AI models; significant costs to build AI and cloud infrastructure that reduce operating margins; flawed algorithms, biased or inaccurate datasets, and harmful or inaccurate AI-generated content that could cause reputational or competitive harm or legal liability; misuse of its AI systems and services by users; emerging AI regulation such as the EU AI Act that could increase costs or restrict opportunity; and intellectual property claims arising from AI training and output.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: Competitors also use open AI models at little cost.

*7 tool calls, 31.7s, $0.0312*

**Answer:**

Microsoft's FY2025 10-K discloses AI-related risks across nearly every category of its Item 1A Risk Factors — competition, execution and investment, misuse, security, liability, infrastructure/supply, regulation, litigation, and reputation. The main disclosures are:

- **Competition and execution (p.17):** AI is "a highly competitive and rapidly evolving market" with new entrants; Microsoft bears significant development and operational costs to build AI models, services, platforms, and infrastructure, and must respond to technological change, regulation, and public scrutiny. Competitors also use open AI models at little cost. A dedicated risk factor states that its "focus on cloud-based and AI services presents execution and competitive risks" — heavy infrastructure spending is reducing operating margins, and it is uncertain whether AI strategies will attract users or generate revenue in line with those investments.

- **Investment and partnership risk (p.18):** Investments in AI-based products and services are speculative and may not achieve expected returns or historical margins. The acquisitions/alliances risk factor cites the OpenAI strategic partnership and notes that realizing benefits from such arrangements depends partly on meeting standards for responsible AI.

- **Misuse and abuse (p.18, p.22):** AI systems may be used in unintended or inappropriate ways, and users may commit fraud or abuse (unauthorized account access, payment fraud, cryptocurrency mining, launching cyberattacks) through cloud and AI services; detection efforts may fail, causing reputational damage. Platform-abuse risks include impersonation "through the use of AI technologies" and misleading content.

- **AI development, deployment, and liability (p.22–23):** A dedicated risk factor warns that flawed AI algorithms or training methodologies, overbroad/insufficient/biased datasets, and offensive, illegal, inaccurate, or harmful AI-generated content could cause harm and impair acceptance of AI solutions; human review may be needed, including for agentic AI systems that act autonomously. These risks may create legal liability, regulatory action, and brand/reputational/competitive harm, stemming from intellectual property, data privacy, and other claims tied to AI training and outputs, compounded by an evolving regulatory landscape (including the EU) and global divergence on ethical and societal issues. Customers may also deploy Microsoft's AI products in high-risk scenarios or use them inappropriately (p.22).

- **Security (p.19–20):** Threat actors may use AI and machine learning in attacks; increasing internal use of generative AI "may create new attack surfaces or methods for adversaries"; and features relying on generative AI can be susceptible to security threats.

- **Infrastructure and supply (p.23–24):** Datacenter demands are rising as AI features are incorporated into services, and datacenters depend on land, energy, networking supplies, and servers including GPUs — costs and availability of which could be adversely affected. Limited suppliers for datacenter components, with competitors drawing on the same suppliers amid growing AI demand, could leave inadequate capacity to support AI services.

- **Regulation, trade, litigation, and reputation (p.24–27):** Emerging AI legislation — notably the EU AI Act — could increase costs or restrict AI models and services, with regulatory focus on model development/deployment, frontier model safety, transparency, and content provenance. Shifting U.S. AI export controls (e.g., the rescinded AI Diffusion Rule and potential replacement rulemakings) could raise costs, create continuity uncertainty, and accelerate sovereignty initiatives abroad. Lawsuits may arise from AI services, and IP infringement claims specifically "arising from AI training and output" are cited. Finally, public scrutiny of AI development and deployment decisions, and responsible AI failures, could damage Microsoft's reputation and brands.

Sources: [MSFT FY2025 10-K, p.17], [MSFT FY2025 10-K, p.18], [MSFT FY2025 10-K, p.19], [MSFT FY2025 10-K, p.20], [MSFT FY2025 10-K, p.22], [MSFT FY2025 10-K, p.23], [MSFT FY2025 10-K, p.24], [MSFT FY2025 10-K, p.25], [MSFT FY2025 10-K, p.26], [MSFT FY2025 10-K, p.27]

---

## x_036#0: PASS (llm_judge, level 4)

**Question:** Microsoft and Alphabet both grew operating income in fiscal year 2025. By how much did each grow, and what does each company's 10-K say drove it?

**Gold:** Microsoft's operating income rose $19.1 billion (about 17.4%), from $109.4 billion to $128.5 billion; its 10-K says the growth came from all of its segments. Alphabet's rose $16.6 billion (about 14.8%), from $112.4 billion to $129.0 billion; its 10-K attributes the segment gains mainly to higher revenues: Google Services operating income rose $18.1 billion and Google Cloud $7.8 billion, partly offset by a $3.1 billion larger Other Bets loss and higher Alphabet-level AI research costs.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** unsupported: Microsoft 10-K attributes operating income growth primarily to revenue growth.

*5 tool calls, 29.1s, $0.0248*

**Answer:**

Microsoft's operating income grew $19.1 billion (+17.4%) and Alphabet's grew $16.6 billion (+14.8%) in FY2025, with both 10-Ks attributing the growth primarily to revenue growth — Microsoft's across all three segments, Alphabet's led by Google Services and Google Cloud.

**Microsoft (FY2025 ended June 30, 2025):** operating income rose from $109.4 billion to $128.5 billion, +$19.1 billion or 17.4% (the 10-K rounds to 17%).
- The 10-K says operating income "increased $19.1 billion or 17% with growth across each of our segments," on revenue up $36.6 billion or 15% — Intelligent Cloud driven by Azure, Productivity and Business Processes driven by Microsoft 365 Commercial cloud, and More Personal Computing driven by Gaming and Search and news advertising.
- By segment: Productivity and Business Processes operating income +$10.1 billion (17%), Intelligent Cloud +$6.8 billion (18%), More Personal Computing +$2.2 billion (18%).
- Gross margin increased $22.9 billion or 13%, while operating expenses rose only $3.8 billion or 6% (investments in cloud and AI engineering and Gaming, including the Activision Blizzard acquisition impact) — so revenue growth outpaced expense growth. Gross margin percentage declined slightly from scaling AI infrastructure, offset in part by efficiency gains in Azure.

**Alphabet (FY2025 ended December 31, 2025):** operating income rose from $112.4 billion to $129.0 billion, +$16.6 billion or 14.8%.
- Google Services operating income increased $18.1 billion, "primarily driven by an increase in revenues" (Google Services revenues +$37.8 billion or 12%), partially offset by higher expenses for legal and other matters, TAC, and content acquisition costs.
- Google Cloud operating income increased $7.8 billion, primarily driven by revenue growth (Google Cloud revenues +$15.5 billion or 36%), partially offset by usage costs for technical infrastructure and employee compensation.
- Other Bets partially offset the gains: its operating loss widened by $3.1 billion, driven by employee compensation expenses, largely a valuation-based compensation charge related to Waymo.

Note the fiscal years cover different calendar months (Microsoft's ended June 30, 2025; Alphabet's ended December 31, 2025), so the periods aren't directly comparable.

Sources:
- [SQL: income_statements]
- [MSFT FY2025 10-K, p.37-38]
- [GOOGL FY2025 10-K, p.34, p.39]

---

## x_036#1: PASS (llm_judge, level 4)

**Question:** Microsoft and Alphabet both grew operating income in fiscal year 2025. By how much did each grow, and what does each company's 10-K say drove it?

**Gold:** Microsoft's operating income rose $19.1 billion (about 17.4%), from $109.4 billion to $128.5 billion; its 10-K says the growth came from all of its segments. Alphabet's rose $16.6 billion (about 14.8%), from $112.4 billion to $129.0 billion; its 10-K attributes the segment gains mainly to higher revenues: Google Services operating income rose $18.1 billion and Google Cloud $7.8 billion, partly offset by a $3.1 billion larger Other Bets loss and higher Alphabet-level AI research costs.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** none

*6 tool calls, 30.8s, $0.0272*

**Answer:**

Microsoft's operating income grew by $19.1 billion (+17.4%, from $109.4 billion to $128.5 billion) and Alphabet's grew by $16.6 billion (+14.8%, from $112.4 billion to $129.0 billion) in their respective fiscal 2025 years.

**Microsoft (FY2025, ended June 30, 2025)**
- Operating income rose from $109,433 million to $128,528 million, an increase of $19,095 million; the 10-K states "Operating income increased $19.1 billion or 17% with growth across each of our segments."
- The driver was broad revenue growth: revenue increased $36.6 billion or 15%, with Intelligent Cloud driven by Azure, Productivity and Business Processes driven by Microsoft 365 Commercial cloud, and More Personal Computing driven by Gaming and Search and news advertising.
- Gross margin increased $22.9 billion or 13%, though gross margin percentage decreased slightly as Microsoft Cloud gross margin percentage fell to 69% from the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure.
- Operating expenses rose only $3.8 billion or 6% (investments in cloud and AI engineering and Gaming, including Activision Blizzard), so revenue growth outpaced expense growth.

**Alphabet (FY2025, ended December 31, 2025)**
- Operating income rose from $112,390 million to $129,039 million, an increase of $16,649 million.
- Google Services operating income increased $18.1 billion, "primarily driven by an increase in revenues, partially offset by an increase in expenses related to legal and other matters, TAC, and content acquisition costs."
- Google Cloud operating income increased $7.8 billion, "primarily driven by an increase in revenues, partially offset by increases in usage costs for technical infrastructure and employee compensation expenses."
- These gains were partially offset by Other Bets, whose operating loss widened by $3.1 billion, driven by higher employee compensation expenses largely from a valuation-based compensation charge related to Waymo.

Note the fiscal calendars differ: Microsoft's FY2025 covers July 2024–June 2025, while Alphabet's covers calendar 2025.

Sources: [SQL: income_statements], [MSFT FY2025 10-K, p.37], [GOOGL FY2025 10-K, p.39]

---

## x_047#0: PASS (llm_judge, level 4)

**Question:** How do Microsoft's and Alphabet's fiscal year 2025 10-Ks describe the effect of AI infrastructure on their costs and margins?

**Gold:** Microsoft says scaling its AI infrastructure lowered gross margin percentages: Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure, and operating expenses rose on investments in cloud and AI engineering. Alphabet says it is significantly increasing investment in technical infrastructure, in particular for AI, and that the costs of operating it (depreciation, energy, equipment and network capacity) are expected to increase significantly because AI offerings require more compute; Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure.

**Grade:** 6/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering

**Claims the tools did not back:** none

*7 tool calls, 49.2s, $0.0485*

**Answer:**

Both companies' FY2025 10-Ks describe AI infrastructure spending as a significant and growing cost driver that pressures margins — Microsoft says it is already reducing gross margin percentage, while Alphabet says the biggest cost increases are still ahead — and both pair that pressure with expected efficiency offsets. (Note the fiscal years differ: Microsoft's FY2025 ended June 30, 2025; Alphabet's ended December 31, 2025.)

**Microsoft (FY2025 10-K)**
- MD&A states flatly: "The investments we are making in cloud and AI infrastructure and devices will continue to increase our operating costs and may decrease our operating margins," noting datacenter expansion depends on land, energy, networking supplies, and servers including GPUs (p.34). The Risk Factors section repeats that it is "incurring significant costs to build and maintain infrastructure to support cloud-based and AI services, reducing operating margins" (p.17).
- The realized effect in FY2025: cost of revenue rose $13.7 billion or 19% (to $87.8 billion, +18.5% per the database), driven by growth in Microsoft Cloud, and gross margin percentage "decreased slightly" driven by Intelligent Cloud — Microsoft Cloud gross margin percentage fell to 69% "driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure" (p.37). Within Intelligent Cloud, cost of revenue rose $10.6 billion or 36% on Azure growth, with gross margin percentage down for the same AI-infrastructure reason (p.38).
- Supporting figures: depreciation expense jumped to $22.0 billion in FY2025 from $15.2 billion in FY2024, and Microsoft had committed $32.1 billion for construction primarily related to datacenters as of June 30, 2025 (p.65). Despite the gross margin pressure (68.8% vs. 69.8% per the database), operating margin actually edged up to 45.6% from 44.6%.

**Alphabet (FY2025 10-K)**
- The MD&A "Trends" section is the centerpiece: Alphabet invested heavily in capex in 2025 ($91.4 billion vs. $52.5 billion in 2024) and expects to "significantly increase" investment in 2026 for servers, network equipment, and data centers. It warns that technical infrastructure operating costs — "depreciation, energy, equipment, and network capacity — are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings," while it expects to keep driving datacenter efficiencies through AI model design and its TPU/GPU-based infrastructure (pp.30, 41).
- The realized FY2025 effect: cost of revenues rose $16.2 billion (+11.1% to $162.5 billion per the database), with the "other cost of revenues" portion up $11.2 billion primarily due to content acquisition costs (largely YouTube), depreciation expense, and other technical infrastructure operations costs (p.37); the Executive Overview likewise cites TAC, content acquisition costs, and depreciation as the drivers (p.34). Depreciation on property and equipment rose to $21.1 billion from $15.3 billion (p.41).
- Margin framing is more forward-looking: the Risk Factors section says Alphabet "may experience downward pressure on our operating margin" from the higher level of investment in technical infrastructure, among other factors (p.12). In FY2025 itself, cost of revenues grew slower than revenue (11% vs. 15%), so cost of revenues as a share of revenue improved to 40.3% from 41.8% and operating margin was roughly flat at 32.0% vs. 32.1%. Google Cloud's operating income rose $7.8 billion, with revenue growth partially offset by increases in usage costs for technical infrastructure (p.39).

**Common thread:** both filings attribute rising cost of revenue/depreciation to the AI buildout, both explicitly flag margin pressure (Microsoft as a current gross-margin drag, Alphabet as an expected 2026 cost acceleration and margin risk), and both counterbalance it with efficiency claims — Microsoft's "efficiency gains in Azure" and Alphabet's datacenter/model-design and custom TPU efficiencies.

Sources: [MSFT FY2025 10-K, pp.17, 34, 37, 38, 44, 65]; [GOOGL FY2025 10-K, pp.12, 30, 34, 37, 39, 41]; [SQL: income_statements]

---

