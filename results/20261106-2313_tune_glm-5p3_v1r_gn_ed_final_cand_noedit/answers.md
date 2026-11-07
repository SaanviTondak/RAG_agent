# Answers: 20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand_noedit

47/47 passed. Failed answers first. Scorecard: [scorecard.md](scorecard.md).

## q_001#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Apple's total net revenue in fiscal year 2025?

**Gold:** $416.2 billion

**Grade:** answer's figure '$416.2 billion' matches 416161000000 (usd)

**Claims the tools did not back:** unsupported: The figure is total net sales.; unsupported: The product categories include Home and Accessories.

*1 tool calls, 3.2s, $0.0049*

**Answer:**

Apple's total net revenue in fiscal year 2025 was **$416.2 billion**.

- This covers the fiscal year from September 29, 2024 through September 27, 2025 (Apple's fiscal year ends in late September).
- The figure is total net sales as reported in the income statement, spanning all product categories (iPhone, Mac, iPad, Wearables, Home and Accessories) and Services.

Sources: [SQL: income_statements]

---

## q_006#0: PASS (llm_judge, level 1)

**Question:** What were the primary risk factors Apple disclosed related to its supply chain in its fiscal year 2025 10-K filing?

**Gold:** Apple disclosed risks including: reliance on single or limited sources for components; dependence on third-party manufacturers; supply chain disruptions from geopolitical tensions, natural disasters, and health emergencies; component supply constraints affecting product availability; and risks from concentration of manufacturing operations in specific regions.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*1 tool calls, 22.1s, $0.0247*

**Answer:**

Apple's FY2025 10-K (Item 1A, Risk Factors) discloses several primary supply chain risks, centered on its heavy reliance on outsourced, geographically concentrated manufacturing and single-source suppliers.

- **Dependence on outsourcing partners outside the U.S. (p.10):** A significant majority of Apple's manufacturing is performed by outsourcing partners located primarily in China mainland, India, Japan, South Korea, Taiwan and Vietnam, with final assembly of substantially all hardware products by partners primarily in Asia. Apple relies on single-source partners in the U.S., Asia and Europe for many components and has outsourced much of its transportation/logistics management, reducing direct control over production and distribution; it also generally remains responsible for warranty service despite defect-reimbursement provisions, and supplier code-of-conduct violations occur from time to time.

- **Obtaining components in sufficient quantities on commercially reasonable terms (p.10–11):** Because Apple sources certain components from single or limited sources, it faces significant supply and pricing risks, including industrywide shortages (e.g., past global semiconductor shortages), commodity price fluctuations, and capacity constraints on custom single-source components for new products. Suppliers may also fail, consolidate, or deprioritize Apple's custom components, and Apple may not secure alternative sources in a timely manner.

- **Trade restrictions, tariffs and geopolitical tensions (p.8):** Restrictions on international trade — such as tariffs and import/export controls — can increase costs or limit availability of products, components, rare earths and other raw materials, and can force Apple to change suppliers and restructure operations, which is expensive, time-consuming and disruptive. The filing specifically flags the new U.S. tariffs announced beginning in Q2 2025 on imports from China, India, Japan, South Korea, Taiwan, Vietnam and the EU, retaliatory measures by other countries, and the U.S. Commerce Department's Section 232 investigation into semiconductor imports; it notes such measures can be announced with little or no advance notice.

- **Business interruptions (p.8–9):** Natural disasters (many supplier and contract-manufacturer operations are in earthquake-prone locations), public health issues, industrial accidents at suppliers, labor disputes and other events can make it difficult or impossible to manufacture and deliver products. Because Apple relies on single or limited sources for many critical components, an interruption affecting those sources would exacerbate the consequences, and insurance coverage may be insufficient.

- **Inventory write-downs and purchase commitment risk (p.11):** Apple orders components and builds inventory ahead of announcements, with manufacturing purchase obligations typically covering up to 150 days of forecasted requirements; volatile markets create the risk of forecasting incorrectly and ordering excess or insufficient components, leading to write-downs and cancellation fee reserves.

- Related risks also touch the supply chain: design and manufacturing defects in third-party components (p.11), IT system failures that can impede manufacturing and shipping across the global supply chain (p.13), and reliance on global suppliers exposed to ransomware and other malicious attacks that can disrupt operations (p.13–14).

Sources: [AAPL FY2025 10-K, p.7–14]

---

## q_008#0: PASS (fuzzy_numeric, level 2)

**Question:** What percentage of Microsoft's total revenue came from the United States in fiscal year 2025?

**Gold:** 51.3%

**Grade:** answer's figure '51.3%' matches 51.3 (pct)

**Claims the tools did not back:** none

*2 tool calls, 10.1s, $0.0107*

**Answer:**

About 51.3% of Microsoft's total revenue in fiscal year 2025 came from the United States.

- U.S. revenue: $144.5 billion of $281.7 billion total revenue (FY2025, ended June 30, 2025).
- The remaining 48.7% ($137.2 billion) came from other countries.

Sources: [SQL: geographic_revenue, income_statements]

---

## q_011#0: PASS (exact_match_entity, level 2)

**Question:** Which company had the fastest revenue growth rate between their two most recent fiscal years, and what was the growth rate?

**Gold:** Alphabet (GOOGL) had the fastest revenue growth between the two most recent fiscal years at about 15.1%.

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%'

**Claims the tools did not back:** none

*2 tool calls, 5.8s, $0.0072*

**Answer:**

Alphabet (GOOGL) had the fastest revenue growth between its two most recent fiscal years, at 15.1% (FY2024 → FY2025).

- **Alphabet:** $350.0 billion → $402.8 billion, +15.1%
- **Microsoft:** $245.1 billion → $281.7 billion, +14.9% (a close second)
- **Apple:** $391.0 billion → $416.2 billion, +6.4%

Note that the fiscal years cover different calendar months (Apple's ends late September, Microsoft's June 30, Alphabet's December 31), so the periods are not perfectly aligned.

Sources: [SQL: income_statements]

---

## q_012#0: PASS (llm_judge, level 3)

**Question:** How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and does the 10-K filing explain why?

**Gold:** Apple's Greater China revenue decreased from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of approximately 3.8%. The FY2025 10-K states this was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** none

*3 tool calls, 11.6s, $0.0148*

**Answer:**

Apple's Greater China net sales fell from $66.95 billion in FY2024 to $64.38 billion in FY2025 — a decline of $2.6 billion, or 3.8% (shown as (4)% in the 10-K) — and yes, the FY2025 10-K explains the decrease.

- **FY2024 Greater China net sales:** $66,952 million; **FY2025:** $64,377 million (Apple's reportable segments are geographic).
- **Change:** –$2,575 million, or –3.8% year over year.
- **Why (per the 10-K):** "Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
- This was the second consecutive annual decline in the region (FY2023 was $72,559 million, down 8% in FY2024), even as Apple's total net sales grew 6% to $416.2 billion in FY2025.

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]

---

## q_014#0: PASS (llm_judge, level 3)

**Question:** Microsoft restructured its segment reporting in August 2024. How are the three segments defined in the fiscal year 2025 10-K, and what was the revenue for each?

**Gold:** The three segments in the FY2025 10-K are: (1) Productivity and Business Processes ($120.8B) - includes Microsoft 365 Commercial/Consumer, LinkedIn, and Dynamics; (2) Intelligent Cloud ($106.3B) - includes Azure, SQL Server, Windows Server, GitHub, and enterprise services; (3) More Personal Computing ($54.6B) - includes Windows, Devices, Gaming, and Search/news advertising.

**Grade:** 19/19 facts covered

**Claims the tools did not back:** none

*5 tool calls, 27.6s, $0.0295*

**Answer:**

In its FY2025 10-K (fiscal year ended June 30, 2025), Microsoft reports three segments — Productivity and Business Processes ($120.8 billion revenue), Intelligent Cloud ($106.3 billion), and More Personal Computing ($54.6 billion) — with the August 2024 changes most notably bringing the commercial components of Microsoft 365 together in the Productivity and Business Processes segment, and prior-period segment information recast to conform.

**Segment definitions and FY2025 revenue:**

- **Productivity and Business Processes — $120.8 billion** (up 13% from $106.8 billion in FY2024). Products and services in Microsoft's portfolio of productivity, communication, and information services, spanning a variety of devices and platforms. Primarily comprises: Microsoft 365 Commercial products and cloud services (Microsoft 365 Commercial cloud — including Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot — plus Windows Commercial on-premises and Office licensed on-premises); Microsoft 365 Consumer products and cloud services; LinkedIn (Talent, Marketing, Premium Subscriptions, and Sales Solutions); and Dynamics products and cloud services (Dynamics 365 across ERP, CRM, Power Apps, and Power Automate, plus on-premises ERP/CRM).

- **Intelligent Cloud — $106.3 billion** (up 21% from $87.5 billion in FY2024). Public, private, and hybrid server products and cloud services that power modern business and developers. Primarily comprises: server products and cloud services, including Azure and other cloud services (cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings, and other cloud services) and server products (SQL Server, Windows Server, Visual Studio, System Center, related Client Access Licenses, and other on-premises offerings); and Enterprise and partner services (Enterprise Support Services, Industry Solutions, Nuance professional services, Microsoft Partner Network, and Learning Experience).

- **More Personal Computing — $54.6 billion** (up 7% from $50.8 billion in FY2024). Products and services that put customers at the center of the experience with Microsoft's technology. Primarily comprises: Windows and Devices (Windows OEM licensing for Windows Pro and non-Pro, plus Surface and PC accessories); Gaming (Xbox hardware and Xbox content and services, including first- and third-party content, Xbox Game Pass and other subscriptions, Xbox Cloud Gaming, advertising, and other cloud services); and Search and news advertising (Bing and Copilot, Microsoft News, Microsoft Edge, and third-party affiliates).

The three segments sum to Microsoft's total FY2025 revenue of $281.7 billion. Note that these figures reflect the restated segment definitions; the FY2024 10-K reported segments under the old composition, so its segment figures differ.

Sources: [SQL: segment_revenue]; [MSFT FY2025 10-K, p.5]; [MSFT FY2025 10-K, p.8]; [MSFT FY2025 10-K, p.35]; [MSFT FY2025 10-K, p.37]; [MSFT FY2025 10-K, p.78]

---

## q_017#0: PASS (llm_judge, level 3)

**Question:** According to Alphabet's 10-K filings, what are the key components of 'Google Services' revenue, and how did YouTube advertising revenue change between FY2024 and FY2025?

**Gold:** Google Services includes Google Search & other, YouTube ads, Google Network, and Google subscriptions/platforms/devices. YouTube advertising revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of approximately 11.7%.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*4 tool calls, 18.4s, $0.0150*

**Answer:**

Per Alphabet's FY2025 10-K, Google Services revenue comprises **Google advertising** (Google Search & other, YouTube ads, and Google Network) plus **Google subscriptions, platforms, and devices**, and YouTube ads revenue grew $4.2 billion, from $36.1 billion in FY2024 to $40.4 billion in FY2025 (+11.7%).

**Components of Google Services revenue (FY2025 10-K, revenues by type):**
- **Google Search & other** — revenues on Google search properties (including traffic from search distribution partners using Google.com as default search) and other owned/operated properties like Gmail, Google Maps, and Google Play: $198.1 billion in FY2024 → $224.5 billion in FY2025.
- **YouTube ads** — revenues generated on YouTube properties: $36.1 billion → $40.4 billion.
- **Google Network** — revenues from properties participating in AdMob, AdSense, and Google Ad Manager: $30.4 billion → $29.8 billion.
- These three sum to **Google advertising**: $264.6 billion → $294.7 billion.
- **Google subscriptions, platforms, and devices** — consumer subscriptions (e.g., YouTube TV, YouTube Music and Premium, NFL Sunday Ticket, Google One), sale of apps and in-app purchases, and devices: $40.3 billion → $48.0 billion.
- Google Services total: $304.9 billion → $342.7 billion (+12.4%), consistent with the database's segment figures.

**YouTube ads change (FY2024 → FY2025):** increased $4.2 billion (from $36,147 million to $40,367 million, +11.7%). The filing attributes the growth to direct response advertising products, followed by brand advertising products, both of which benefited from increased spending by advertisers.

Sources: [GOOGL FY2025 10-K, p.35], [GOOGL FY2025 10-K, p.31], [GOOGL FY2025 10-K, p.36], [GOOGL FY2025 10-K, p.87], [SQL: segment_revenue]

---

## q_018#0: PASS (exact_match_entity, level 2)

**Question:** Which company has the highest current ratio (current assets / current liabilities) in their most recent fiscal year?

**Gold:** Alphabet (GOOGL) has the highest current ratio in the most recent fiscal year (about 2.01x).

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01'

**Claims the tools did not back:** none

*1 tool calls, 4.1s, $0.0035*

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

*3 tool calls, 20.1s, $0.0145*

**Answer:**

**Alphabet (GOOGL) saw the largest absolute revenue increase: +$52.8 billion (from $350.0 billion in FY2024 to $402.8 billion in FY2025)**, ahead of Microsoft (+$36.6 billion, $245.1B → $281.7B) and Apple (+$25.1 billion, $391.0B → $416.2B).

Breakdown of Alphabet's $52.8 billion increase by segment (FY2024 → FY2025):
- **Google Services: +$37.8 billion** ($304.9B → $342.7B) — the largest contributor, about 71.5% of the total increase.
- **Google Cloud: +$15.5 billion** ($43.2B → $58.7B) — about 29.3% of the total increase.
- **Other Bets: –$0.1 billion** ($1.6B → $1.5B) — a slight decline.
- **Hedging gains (losses): –$0.3 billion** ($0.2B → –$0.1B) — a reconciling item, not a segment; it slightly offset the segment gains.

The two segment increases plus these two small declines sum exactly to the $52.8 billion consolidated increase. Note that fiscal years differ: Alphabet's FY2025 ended December 31, 2025, while Apple's ended late September 2025 and Microsoft's June 30, 2025, so the periods cover different calendar months.

Sources:
- [SQL: income_statements]
- [SQL: segment_revenue]

---

## q_025#0: PASS (llm_judge, level 4)

**Question:** Apple's Services segment has been growing as a share of total revenue. Calculate the Services revenue growth rate for each of the last two years, compare it to iPhone revenue growth, and find what Apple's 10-K says about the strategic importance of Services.

**Gold:** Services growth: FY2023->FY2024: 12.9% ($85.2B to $96.2B), FY2024->FY2025: 13.5% ($96.2B to $109.2B). iPhone growth: FY2023->FY2024: 0.3%, FY2024->FY2025: 4.2%. Services is consistently growing much faster. The 10-K highlights Services as a key growth driver with higher margins, recurring revenue from subscriptions, App Store, Apple Music, iCloud, and advertising.

**Grade:** 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions

**Claims the tools did not back:** contradicted: Services is a growth driver across every geography; contradicted: Services gross margin percentage is rising primarily due to higher Services net sales and a different mix of services; contradicted: Services gross margin dollars are on roughly half the revenue of Products; unsupported: Services portfolio deepens engagement with the installed base of Apple devices

*7 tool calls, 34.6s, $0.0286*

**Answer:**

**Services grew 12.9% in FY2024 and 13.5% in FY2025, far outpacing iPhone growth of 0.3% and 4.2% in those years, lifting Services from 22.2% to 26.2% of total revenue over two years.** (Note: "Services" here is Apple's product/service revenue category, not a reportable segment — Apple's reportable segments are geographic.)

**Growth comparison (from the revenue-by-category data):**

| Category | FY2024 | FY2025 |
|---|---|---|
| Services | $96.2B (+12.9%) | $109.2B (+13.5%) |
| iPhone | $201.2B (+0.3%) | $209.6B (+4.2%) |

- Services revenue rose from $85.2B (FY2023) to $96.2B (FY2024) to $109.2B (FY2025), while iPhone was nearly flat at $200.6B → $201.2B → $209.6B. The 10-K's own table rounds these to 13%/14% for Services vs. "—%"/4% for iPhone.
- As a share of total net sales ($383.3B → $391.0B → $416.2B), Services climbed from 22.2% (FY2023) to 24.6% (FY2024) to 26.2% (FY2025) — Services drove most of Apple's total revenue growth.

**What the FY2025 10-K says about Services' strategic importance:**

- **Growth driver across every geography:** Services is cited as a primary driver of net sales increases in the Americas, Europe, Japan and Rest of Asia Pacific segments (Item 7, p.24), and MD&A attributes FY2025 Services growth "primarily due to higher net sales from advertising, the App Store and cloud services" (p.25).
- **Margin engine:** Services gross margin percentage was 75.4% in FY2025 (73.9% in FY2024, 70.8% in FY2023) versus 36.8% for Products — and it is rising "primarily due to higher Services net sales and a different mix of services." Services gross margin dollars ($82.3B) now approach three-quarters of Products' ($112.9B) on roughly half the revenue, and helped lift total gross margin from 44.1% to 46.9% over two years (p.25).
- **Ecosystem lock-in:** Item 1 (pp.4–5) frames Services as spanning advertising, AppleCare, cloud services ("store and keep customers' content up-to-date and available across multiple Apple devices"), the App Store and subscription content (Apple Arcade, Fitness+, Music, News+, TV+), and payment services (Apple Card, Apple Pay) — a portfolio that deepens engagement with the installed base of Apple devices.

Sources: [SQL: segment_revenue], [SQL: income_statements], [AAPL FY2025 10-K, p.24], [AAPL FY2025 10-K, p.25], [AAPL FY2025 10-K, pp.4-5]

---

## x_001#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Microsoft's net income in fiscal year 2025?

**Gold:** $101.8 billion

**Grade:** answer's figure '$101.8 billion' matches 101832000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 2.4s, $0.0024*

**Answer:**

Microsoft's net income in fiscal year 2025 (July 1, 2024 – June 30, 2025) was **$101.8 billion**.

- Net income: $101,832,000,000
- EPS (basic): $13.70; EPS (diluted): $13.64

Sources: [SQL: income_statements]

---

## x_002#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Alphabet's diluted earnings per share for fiscal year 2025?

**Gold:** $10.81

**Grade:** answer's figure '$10.81' matches 10.81 (plain)

**Claims the tools did not back:** unsupported: The EPS increase was driven by net income rising 32%.

*2 tool calls, 7.6s, $0.0107*

**Answer:**

Alphabet's diluted net income per share for fiscal year 2025 (year ended December 31, 2025) was **$10.81**.

- The figure is confirmed in both the financials database and the FY2025 10-K (income statement and Note 12, Net Income Per Share).
- It was computed under the two-class method: net income of $132,170 million divided by 12,230 million diluted weighted-average shares (12,116 million basic shares plus 114 million dilutive effect of RSUs and other contingently issuable shares).
- This was up $2.77 (34%) from $8.04 in FY2024, driven by net income rising 32% from $100,118 million to $132,170 million.
- By share class, diluted EPS was $10.82 for Class A, $10.81 for Class B, and $10.80 for Class C.

Sources: [SQL: income_statements]; [GOOGL FY2025 10-K, p.34]; [GOOGL FY2025 10-K, p.51]; [GOOGL FY2025 10-K, p.82]

---

## x_003#0: PASS (fuzzy_numeric, level 1)

**Question:** How much did Apple spend on research and development in fiscal year 2024?

**Gold:** $31.4 billion

**Grade:** answer's figure '$31.4 billion' matches 31370000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.7s, $0.0027*

**Answer:**

Apple spent **$31.4 billion** on research and development in fiscal year 2024 (the twelve months ended September 28, 2024).

- The exact figure was $31,370,000,000, as reported on Apple's FY2024 income statement.
- Apple's fiscal year 2024 ran from October 1, 2023 through September 28, 2024.

Sources: [SQL: income_statements]

---

## x_004#0: PASS (fuzzy_numeric, level 1)

**Question:** What were Microsoft's total assets at the end of fiscal year 2025?

**Gold:** $619.0 billion

**Grade:** answer's figure '$619.0 billion' matches 619003000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 2.0s, $0.0025*

**Answer:**

Microsoft's total assets at the end of fiscal year 2025 (June 30, 2025) were **$619.0 billion**.

- The figure is $619,003,000,000 as of the fiscal year-end balance sheet date of June 30, 2025.

Sources: [SQL: balance_sheets]

---

## x_007#0: PASS (exact_match_entity, level 2)

**Question:** Which company had the highest operating margin in fiscal year 2025, and what was it?

**Gold:** Microsoft had the highest operating margin in FY2025 at about 45.6% (Alphabet 32.0%, Apple 32.0%).

**Grade:** answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%'

**Claims the tools did not back:** none

*2 tool calls, 5.6s, $0.0046*

**Answer:**

Microsoft had the highest operating margin in FY2025, at 45.6% ($128.5 billion operating income on $281.7 billion of revenue).

- **MSFT: 45.6%** — operating income $128.5 billion / revenue $281.7 billion
- **GOOGL: 32.0%** — operating income $129.0 billion / revenue $402.8 billion
- **AAPL: 32.0%** — operating income $133.1 billion / revenue $416.2 billion

Note that the three fiscal years cover different calendar months (Microsoft's ended June 30, 2025; Apple's ended late September 2025; Alphabet's ended December 31, 2025), so this is a comparison of each company's own FY2025.

Sources: [SQL: income_statements]

---

## x_008#0: PASS (exact_match_entity, level 2)

**Question:** Which two companies had the highest total revenue in fiscal year 2025?

**Gold:** Apple ($416.2 billion) and Alphabet ($402.8 billion); Microsoft was third at $281.7 billion.

**Grade:** answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL'])

**Claims the tools did not back:** none

*1 tool calls, 3.3s, $0.0028*

**Answer:**

Apple and Alphabet had the highest total revenue in fiscal year 2025.

- **Apple (AAPL):** $416.2 billion — the highest of the three
- **Alphabet (GOOGL):** $402.8 billion — second highest
- Microsoft (MSFT) was third at $281.7 billion

Note that fiscal years differ: Apple's FY2025 ended in late September, Microsoft's on June 30, and Alphabet's on December 31, so the periods cover different calendar months.

Sources: [SQL: income_statements]

---

## x_009#0: PASS (exact_match_entity, level 2)

**Question:** Rank the three companies by research and development spending as a percentage of revenue in their most recent fiscal year.

**Gold:** Alphabet 15.2%, Microsoft 11.5%, Apple 8.3% (FY2025 R&D / revenue).

**Grade:** answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL'])

**Claims the tools did not back:** none

*2 tool calls, 4.8s, $0.0048*

**Answer:**

Alphabet spent the highest share of revenue on R&D in FY2025 (15.2%), followed by Microsoft (11.5%) and Apple (8.3%).

- **1. Alphabet (GOOGL): 15.2%** — $61.1 billion R&D on $402.8 billion revenue
- **2. Microsoft (MSFT): 11.5%** — $32.5 billion R&D on $281.7 billion revenue
- **3. Apple (AAPL): 8.3%** — $34.6 billion R&D on $416.2 billion revenue

Note that Apple's R&D dollars ($34.6 billion) exceed Microsoft's ($32.5 billion), but Apple's much larger revenue base puts it last on intensity. Also, fiscal years cover different calendar months (Apple's ends late September, Microsoft's June 30, Alphabet's December 31), so the periods are not perfectly aligned.

Sources: [SQL: income_statements]

---

## x_011#0: PASS (fuzzy_numeric, level 2)

**Question:** By what percentage did Alphabet's net income grow from fiscal year 2024 to fiscal year 2025?

**Gold:** About 32.0% ($100.1 billion to $132.2 billion).

**Grade:** answer's figure '32.0%' matches 32.01422321660441 (pct)

**Claims the tools did not back:** none

*2 tool calls, 5.8s, $0.0035*

**Answer:**

Alphabet's net income grew by **32.0%** from fiscal year 2024 to fiscal year 2025.

- FY2024 net income: $100.1 billion
- FY2025 net income: $132.2 billion
- Growth: ($132.17B − $100.118B) / $100.118B = 32.0%

Sources: [SQL: income_statements]

---

## x_013#0: PASS (llm_judge, level 4)

**Question:** For each company, what share of fiscal year 2025 revenue came from its largest geographic region, and which company's revenue was most concentrated in a single region?

**Gold:** Microsoft was the most concentrated: the United States was 51.3% of its FY2025 revenue. Alphabet's largest region, the United States, was 48.2% of revenue, and Apple's largest region, the Americas, was 42.9%.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** unsupported: Microsoft's concentration is structurally higher than peers that break out more regions.

*3 tool calls, 15.5s, $0.0129*

**Answer:**

Microsoft's revenue was the most concentrated in a single region in FY2025, with 51.3% of its $281.7 billion coming from the United States.

- **Apple (AAPL):** Largest region is the Americas at $178.4 billion, or 42.9% of $416.2 billion total revenue. (Apple's reportable segments are geographic; its other regions are Europe, Greater China, Japan, and Rest of Asia Pacific.)
- **Alphabet (GOOGL):** Largest region is the United States at $194.2 billion, or 48.2% of $402.8 billion total revenue (share computed against consolidated revenue, which includes a small negative hedging reconciling item of $127 million that is not a region).
- **Microsoft (MSFT):** Largest region is the United States at $144.5 billion, or 51.3% of $281.7 billion total revenue. Microsoft reports only two geographic buckets (United States and Other countries at $137.2 billion), so its concentration is structurally higher than peers that break out more regions.

Note that fiscal years differ: Apple's FY2025 ended late September 2025, Microsoft's ended June 30, 2025, and Alphabet's ended December 31, 2025.

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

## x_014#0: PASS (llm_judge, level 1)

**Question:** What risks related to artificial intelligence does Microsoft disclose in its fiscal year 2025 10-K?

**Gold:** Microsoft's FY2025 10-K discloses AI risks including: intense and rapidly evolving competition in AI, including from open AI models; significant costs to build AI and cloud infrastructure that reduce operating margins; flawed algorithms, biased or inaccurate datasets, and harmful or inaccurate AI-generated content that could cause reputational or competitive harm or legal liability; misuse of its AI systems and services by users; emerging AI regulation such as the EU AI Act that could increase costs or restrict opportunity; and intellectual property claims arising from AI training and output.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: Rivals offer open AI models at little or no cost.

*7 tool calls, 38.1s, $0.0418*

**Answer:**

Microsoft's FY2025 10-K (Item 1A, Risk Factors) discloses AI-related risks across nearly every risk category — competition, execution, misuse, security, infrastructure, legal/regulatory, and reputation. The main disclosures are:

- **Competition and execution (p.17):** AI is "a highly competitive and rapidly evolving market" with new competitors continually entering, including rivals offering open AI models at little or no cost. Microsoft bears "significant development and operational costs" to build AI models, services, platforms, and infrastructure, and its focus on cloud-based and AI services is "reducing operating margins"; it is uncertain whether these strategies will generate the revenue required to succeed, so revenue may not grow in line with the investments.

- **A dedicated AI risk factor — flaws, harmful content, and liability (p.23):** "Issues in the development, deployment, and use of AI may result in reputational or competitive harm or liability." AI algorithms or training methodologies may be flawed; datasets may be overbroad, insufficient, or contain biased or inaccurate information; AI-generated content may be offensive, illegal, inaccurate, or otherwise harmful. Human review may be required, including for "agentic AI systems that can take actions autonomously." Risks stem from intellectual property, data privacy, and other claims associated with AI training and outputs, compounded by an evolving regulatory landscape (including the EU) and rising global divergence in how to address ethical and societal impacts. AI developed by others, including strategic partner OpenAI, is also covered.

- **Misuse and abuse (pp.18, 22):** AI systems may be used in unintended or inappropriate ways, and users may engage in fraudulent or abusive activities through cloud and AI services (unauthorized account access, payment fraud, cryptocurrency mining, launching cyberattacks); detection efforts may not be effective, risking reputational damage. Users may also impersonate people or organizations "through the use of AI technologies" and spread misleading content on its platforms, and customers may deploy Microsoft's AI products in high-risk scenarios or use them inappropriately.

- **Security (pp.19–20):** Threat actors may use AI and machine learning as attack tools; increasing use of generative AI models in Microsoft's internal systems "may create new attack surfaces or methods for adversaries"; and features that rely on generative AI can be susceptible to security threats.

- **Infrastructure and supply constraints (p.23):** Datacenter demands "continue to increase" as AI features are incorporated into products; datacenters depend on permitted land, predictable energy, networking supplies, and servers including graphics processing units, whose cost or availability could be adversely affected. Limited suppliers for datacenter components, with competitors using the same suppliers amid "growing demand for AI services," could leave inadequate datacenter capacity.

- **Legal and regulatory exposure (pp.24–27):** Emerging AI legislation could increase costs or restrict opportunity — notably the EU AI Act, which "may increase costs or impact the provision or operation of our AI models and services in the European market" (regulatory areas include frontier model safety, transparency, and content provenance). Shifting U.S. AI export controls (e.g., the AI Diffusion Rule, recently rescinded but potentially replaced) could raise costs, create product-continuity uncertainty, and accelerate sovereignty initiatives abroad. Third parties assert copyright infringement and other claims "arising from AI training and output," which could force royalty-bearing licenses, product redesigns, or damages payments (including under customer indemnification commitments). Claims and lawsuits may also arise from AI services, and acquisitions/partnerships (e.g., the OpenAI partnership) depend partly on acquired companies meeting Microsoft's responsible AI policies.

- **Reputation (p.27):** Brand damage could result from public scrutiny of decisions regarding the development and deployment of AI and from "responsible AI failures."

Sources: [MSFT FY2025 10-K, Item 1A Risk Factors, pp.16–29]

---

## x_015#0: PASS (fuzzy_numeric, level 1)

**Question:** What were Alphabet's capital expenditures in fiscal year 2025?

**Gold:** $91.4 billion, primarily reflecting investments in technical infrastructure.

**Grade:** answer's figure '$91.4 billion' matches 91400000000 (usd)

**Claims the tools did not back:** none

*2 tool calls, 8.5s, $0.0096*

**Answer:**

Alphabet's capital expenditures in fiscal year 2025 (year ended December 31, 2025) were **$91.4 billion**, up 74.1% from $52.5 billion in FY2024.

- The FY2025 10-K states: "During the years ended December 31, 2024 and 2025, we spent $52.5 billion and $91.4 billion on capital expenditures, respectively."
- The consolidated statement of cash flows shows purchases of property and equipment of $91,447 million in 2025, versus $52,535 million in 2024.
- The spending consists primarily of technical infrastructure (servers and network equipment, data center land, and building construction and improvements) plus office facilities and ground-up development projects.
- The filing notes Alphabet expects to significantly increase its technical infrastructure investment in 2026 relative to 2025.

Sources: [GOOGL FY2025 10-K, p.41] (MD&A Capital Expenditures), [GOOGL FY2025 10-K, p.53] (Consolidated Statements of Cash Flows)

---

## x_017#0: PASS (fuzzy_numeric, level 1)

**Question:** How much did Alphabet spend repurchasing its shares in fiscal year 2025?

**Gold:** $45.4 billion ($6.5 billion of Class A and $38.9 billion of Class C shares).

**Grade:** answer's figure '$45.4 billion' matches 45400000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 7.5s, $0.0054*

**Answer:**

Alphabet spent **$45.4 billion** repurchasing its shares in fiscal year 2025 (year ended December 31, 2025).

- The company repurchased and subsequently retired 240 million shares in total: 37 million Class A shares for $6.5 billion and 203 million Class C shares for $38.9 billion.
- This was down from $62.0 billion in FY2024 (379 million shares) and $62.2 billion in FY2023 (528 million shares).
- The repurchases were made under board-authorized programs: $70.0 billion authorized in April 2024 plus an additional $70.0 billion authorized in April 2025, leaving $69.5 billion still available for repurchases as of December 31, 2025.

Sources: [GOOGL FY2025 10-K, p.42] (MD&A Share Repurchase Program), [GOOGL FY2025 10-K, p.80] (Note 11, Share Repurchases)

---

## x_019#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Microsoft Cloud revenue in fiscal year 2025?

**Gold:** $168.9 billion, up 23%.

**Grade:** answer's figure '$168.9 billion' matches 168900000000 (usd)

**Claims the tools did not back:** unsupported: The structured database only holds segment-level revenue (Productivity and Business Processes, Intelligent Cloud, More Personal Computing).

*1 tool calls, 10.1s, $0.0073*

**Answer:**

Microsoft Cloud revenue was **$168.9 billion in fiscal year 2025** (year ended June 30, 2025), up 23% from $137.7 billion in FY2024.

- Microsoft Cloud comprises Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365; these amounts are included within the Microsoft 365 Commercial products and cloud services, Server products and cloud services, LinkedIn, and Dynamics products and cloud services line items.
- For context, Microsoft Cloud was $111.6 billion in FY2023, so it grew from $111.6 billion → $137.7 billion → $168.9 billion over the last three fiscal years.
- Microsoft Cloud gross margin percentage decreased to 69% in FY2025, driven by the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure.
- This figure is disclosed in the 10-K filings rather than the structured database, which only holds segment-level revenue (Productivity and Business Processes, Intelligent Cloud, More Personal Computing).

Sources: [MSFT FY2025 10-K, p.33], [MSFT FY2025 10-K, p.80], [MSFT FY2025 10-K, p.37]

---

## x_020#0: PASS (llm_judge, level 3)

**Question:** How did Microsoft's Intelligent Cloud revenue change from fiscal year 2024 to fiscal year 2025, and what does the 10-K say drove the change?

**Gold:** Intelligent Cloud revenue rose from $87.5 billion to $106.3 billion, an increase of about $18.8 billion or 21.5%. The FY2025 10-K attributes the growth to Azure: server products and cloud services revenue increased 23%, driven by Azure and other cloud services revenue growth of 34%.

**Grade:** 8/8 facts covered

**Claims the tools did not back:** unsupported: Server products are on-premises.

*3 tool calls, 17.2s, $0.0175*

**Answer:**

Microsoft's Intelligent Cloud revenue rose from $87.5 billion in FY2024 to $106.3 billion in FY2025, an increase of $18.8 billion or 21.5% (the 10-K rounds this to "$18.8 billion or 21%").

- **FY2024 → FY2025:** $87,464 million → $106,265 million (database figures, which use the segment definitions as restated in the FY2025 10-K after the August 2024 reorganization; the FY2024 10-K's old-definition figures differ).
- **What drove it, per the FY2025 10-K (MD&A):** "Intelligent Cloud revenue increased driven by Azure." Within the segment:
  - Server products and cloud services revenue increased $18.6 billion or 23%, driven by Azure and other cloud services, which grew 34% "driven by demand for our portfolio of services."
  - Server products (on-premises) revenue decreased 3%, "driven by a decrease in transactional purchasing with continued customer shift to cloud offerings."
  - Enterprise and partner services revenue increased $166 million or 2%, driven by growth in Enterprise Support Services, offset in part by a decline in Industry Solutions.
- The filing also notes the segment's cost of revenue rose $10.6 billion or 36% driven by growth in Azure, and gross margin rose $8.2 billion or 14%, with gross margin percentage down due to scaling AI infrastructure, partly offset by efficiency gains in Azure.

Sources: [SQL: segment_revenue]; [MSFT FY2025 10-K, p.37]; [MSFT FY2025 10-K, p.38]

---

## x_021#0: PASS (llm_judge, level 3)

**Question:** How did Alphabet's Google Cloud revenue change between fiscal year 2024 and fiscal year 2025, and what does the 10-K say drove it?

**Gold:** Google Cloud revenue increased from $43.2 billion to $58.7 billion, up $15.5 billion or about 35.8%. The FY2025 10-K says the increase was primarily driven by growth in Google Cloud Platform, largely from infrastructure and platform services.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: The Executive Overview confirms the same driver.

*4 tool calls, 14.4s, $0.0158*

**Answer:**

Google Cloud revenue rose from $43.2 billion in FY2024 to $58.7 billion in FY2025, an increase of $15.5 billion, or 35.8% — and the 10-K attributes the growth primarily to Google Cloud Platform, largely from infrastructure and platform services.

- FY2024 Google Cloud revenue: $43,229 million; FY2025: $58,705 million (both per the database and the FY2025 10-K revenue table, which match).
- The FY2025 10-K MD&A states: "Google Cloud revenues increased $15.5 billion from 2024 to 2025, primarily driven by growth in Google Cloud Platform largely from infrastructure and platform services."
- The Executive Overview confirms the same driver, noting total revenues of $402.8 billion (+15%) were boosted in part by the $15.5 billion (36%) increase in Google Cloud revenues.
- Related context from the same filing: Google Cloud operating income increased $7.8 billion, driven by the revenue increase, partially offset by higher usage costs for technical infrastructure and employee compensation.

Sources: [SQL: segment_revenue]; [GOOGL FY2025 10-K, p.37]; [GOOGL FY2025 10-K, p.34]

---

## x_022#0: PASS (llm_judge, level 3)

**Question:** How did Apple's Wearables, Home and Accessories revenue change from fiscal year 2024 to fiscal year 2025, and what reason does the 10-K give?

**Gold:** Wearables, Home and Accessories revenue fell from $37.0 billion to $35.7 billion, a decrease of about $1.3 billion or 3.6%. The FY2025 10-K says the decrease was primarily due to lower net sales of Accessories and Wearables.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 13.7s, $0.0104*

**Answer:**

Apple's Wearables, Home and Accessories net sales fell from $37.0 billion in FY2024 to $35.7 billion in FY2025, a decline of $1.3 billion (−3.6%, shown as (4)% in the 10-K), which the 10-K attributes primarily to lower net sales of Accessories and Wearables.

- FY2024 net sales: $37,005 million; FY2025 net sales: $35,686 million (per the FY2025 10-K's Products and Services Performance table and Note 2 – Revenue).
- Change: −$1,319 million, or −3.6% ((35,686 − 37,005) / 37,005).
- Reason given in the FY2025 10-K MD&A: "Wearables, Home and Accessories net sales decreased during 2025 compared to 2024 primarily due to lower net sales of Accessories and Wearables."
- For context, this category includes smartwatches (Apple Watch), wireless headphones (AirPods, Beats), Apple Vision Pro, Apple TV, HomePod and accessories.

Sources: [SQL: segment_revenue]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.25]

---

## x_025#0: PASS (llm_judge, level 6)

**Question:** What were Apple's reportable segments in fiscal year 2025, and how much revenue did each generate?

**Gold:** Apple's reportable segments are geographic: Americas $178.4 billion, Europe $111.0 billion, Greater China $64.4 billion, Japan $28.7 billion, and Rest of Asia Pacific $33.7 billion.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** none

*2 tool calls, 16.1s, $0.0108*

**Answer:**

Apple's five reportable segments in fiscal 2025 are geographic — Americas, Europe, Greater China, Japan and Rest of Asia Pacific — and their net sales were $178.4 billion, $111.0 billion, $64.4 billion, $28.7 billion and $33.7 billion, respectively, out of $416.2 billion total net sales.

- **Americas** (North and South America): $178.4 billion — the largest segment, up 7% from $167.0 billion in FY2024.
- **Europe** (European countries plus India, the Middle East and Africa): $111.0 billion, up 10% from $101.3 billion.
- **Greater China** (China mainland, Hong Kong and Taiwan): $64.4 billion, down 4% from $67.0 billion.
- **Rest of Asia Pacific** (Australia, New Zealand and other Asian countries): $33.7 billion, up 10% from $30.7 billion.
- **Japan**: $28.7 billion, up 15% from $25.1 billion.
- Apple manages its business primarily on a geographic basis; although the segments sell similar hardware, software and services, each is managed separately to align with local customers, distribution partners and market dynamics. (Note: the database's `segment_revenue` table for Apple holds product/service categories like iPhone and Services, which are not its reportable segments — the figures above come from the geographic segment data, which matches Note 13 of the 10-K.)

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.5]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.48]

---

## x_027#0: PASS (fuzzy_numeric, level 6)

**Question:** What was Alphabet's gross profit in fiscal year 2025?

**Gold:** $240.3 billion (revenue of $402.8 billion minus cost of revenues of $162.5 billion).

**Grade:** answer's figure '$240.3 billion' matches 240301000000 (usd)

**Claims the tools did not back:** unsupported: Alphabet does not report a 'gross profit' line item in its income statement.

*3 tool calls, 15.1s, $0.0162*

**Answer:**

Alphabet's gross profit in fiscal year 2025 was **$240.3 billion** (revenues of $402.8 billion minus cost of revenues of $162.5 billion).

- Alphabet does not report a "gross profit" line item in its income statement, so this is derived as revenues ($402,836 million) less cost of revenues ($162,535 million) = $240,301 million.
- The FY2025 10-K confirms both inputs: revenues of $402.8 billion (up 15% year over year) and cost of revenues of $162.5 billion (up 11%, driven by traffic acquisition costs, content acquisition costs, and depreciation).
- This implies a gross margin of roughly 59.7% of revenues (cost of revenues was 40% of revenues per the 10-K).
- For comparison, FY2024 gross profit was $350,018M − $146,306M = $203.7 billion, so gross profit grew about 18% year over year.

Sources: [SQL: income_statements], [GOOGL FY2025 10-K, p.34], [GOOGL FY2025 10-K, p.37]

---

## x_028#0: PASS (exact_match_entity, level 6)

**Question:** Which company's fiscal year 2025 ended earliest, and what was its revenue for that year?

**Gold:** Microsoft, whose fiscal year 2025 ended June 30, 2025, with revenue of $281.7 billion.

**Grade:** answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion'

**Claims the tools did not back:** none

*2 tool calls, 6.2s, $0.0060*

**Answer:**

Microsoft's fiscal year 2025 ended earliest, closing on June 30, 2025, with revenue of $281.7 billion.

- The three FY2025 period-end dates: Microsoft on June 30, 2025; Apple on September 27, 2025; Alphabet on December 31, 2025.
- Microsoft's FY2025 revenue was $281,724,000,000 ($281.7 billion), per the income statements table.
- Note that these fiscal years cover different calendar months, so the companies' "FY2025" figures are not directly comparable periods.

Sources: [SQL: companies], [SQL: income_statements]

---

## x_029#0: PASS (llm_judge, level 6)

**Question:** What was Microsoft's Intelligent Cloud revenue in fiscal year 2024?

**Gold:** $87.5 billion under the segment definitions restated in the FY2025 10-K. The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud, under the segment structure in place before the August 2024 reorganization.

**Grade:** 3/3 facts covered

**Claims the tools did not back:** none

*3 tool calls, 25.5s, $0.0157*

**Answer:**

Microsoft's Intelligent Cloud segment revenue in fiscal year 2024 (ended June 30, 2024) was **$87.5 billion** under the current (recast) segment definitions, or $105.4 billion as originally reported in the FY2024 10-K.

- **As recast (current basis):** $87,464 million. In August 2024 Microsoft changed its segment composition — most notably moving the commercial components of Microsoft 365 into Productivity and Business Processes — and recast prior periods, so the FY2025 10-K (and the database) show FY2024 Intelligent Cloud revenue of $87.5 billion.
- **As originally reported:** $105,362 million in the FY2024 10-K, up 20% from $87,907 million in FY2023, driven primarily by Azure and other cloud services (which grew 30%).
- Under the recast definitions, Intelligent Cloud was Microsoft's second-largest segment in FY2024, behind Productivity and Business Processes ($106.8 billion) and ahead of More Personal Computing ($50.8 billion); total company revenue was $245.1 billion.

Sources: [SQL: segment_revenue], [MSFT FY2024 10-K, p.43], [MSFT FY2025 10-K, p.35], [MSFT FY2025 10-K, p.37]

---

## x_030#0: PASS (out_of_scope, level 0)

**Question:** What was Amazon's total revenue in fiscal year 2025?

**Gold:** Not available: the data covers only Apple, Microsoft and Alphabet.

**Grade:** The answer clearly states Amazon's FY2025 revenue is not in its data, explains its coverage is limited to Apple, Microsoft, and Alphabet, and offers no fabricated figure.

**Claims the tools did not back:** unsupported: Amazon is not in the accessible 10-K filings.; unsupported: The filings tool only indexes AAPL, MSFT, and GOOGL 10-Ks for FY2024 and FY2025.

*1 tool calls, 4.3s, $0.0028*

**Answer:**

Amazon's FY2025 total revenue is not available in my sources — I only cover Apple (AAPL), Microsoft (MSFT), and Alphabet (GOOGL), and Amazon (AMZN) is not in the financials database or the 10-K filings I can access.

- The database's `companies` table contains only those three companies, so there is no Amazon revenue data to query.
- The filings tool likewise only indexes AAPL, MSFT, and GOOGL 10-Ks for FY2024 and FY2025.

If you'd like, I can pull FY2025 total revenue for Apple, Microsoft, or Alphabet instead.

Sources: [SQL: companies]

---

## x_032#0: PASS (out_of_scope, level 0)

**Question:** What is Microsoft's current stock price?

**Gold:** Not available: the data contains annual financials and 10-K filings, not market prices.

**Grade:** The answer clearly states the current stock price is not available in its data and provides only related, sourced figures without fabricating a live quote.

**Claims the tools did not back:** none

*1 tool calls, 16.7s, $0.0128*

**Answer:**

I can't tell you Microsoft's current stock price — neither the financials database nor the FY2024/FY2025 10-K filings contains a live or per-share stock price quote, and I don't have access to market data.

The closest related figures available in the filings:

- **Aggregate market value of common stock held by non-affiliates:** $3.1 trillion as of December 31, 2024, based on the NASDAQ closing sale price (per the FY2025 10-K cover page). The FY2024 10-K reported $2.8 trillion as of December 31, 2023.
- **Shares outstanding:** 7,433,166,379 shares as of July 24, 2025 (FY2025 10-K cover page).
- **Trading venue:** Microsoft's common stock trades on the NASDAQ Stock Market under the symbol MSFT.
- The database does hold Microsoft's per-share earnings (e.g., diluted EPS), but not a share price.

For a real-time quote, you'd need a market data source (e.g., NASDAQ or a brokerage terminal), which is outside the tools I have here.

Sources: [MSFT FY2025 10-K, p.1], [MSFT FY2025 10-K, p.32], [MSFT FY2024 10-K, p.1]

---

## x_033#0: PASS (exact_match_entity, level 2)

**Question:** Which company had the highest compound annual growth rate in revenue from fiscal year 2023 to fiscal year 2025, and what was it?

**Gold:** Microsoft, at about 15.3% a year (Alphabet about 14.5%, Apple about 4.2%).

**Grade:** answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%'

**Claims the tools did not back:** none

*2 tool calls, 6.2s, $0.0049*

**Answer:**

Microsoft had the highest revenue CAGR from FY2023 to FY2025, at 15.3% (two-year compound annual growth rate).

- **MSFT: 15.3%** — revenue grew from $211.9 billion (FY2023) to $281.7 billion (FY2025)
- **GOOGL: 14.5%** — revenue grew from $307.4 billion (FY2023) to $402.8 billion (FY2025)
- **AAPL: 4.2%** — revenue grew from $383.3 billion (FY2023) to $416.2 billion (FY2025)

Note that the fiscal years cover different calendar months (Microsoft's ends June 30, Apple's in late September, Alphabet's December 31), so the periods are not perfectly aligned across companies.

Sources: [SQL: income_statements]

---

## x_034#0: PASS (exact_match_entity, level 2)

**Question:** Which company's net profit margin improved the most, in percentage points, from fiscal year 2024 to fiscal year 2025?

**Gold:** Alphabet: its net margin rose about 4.2 percentage points, from 28.6% to 32.8% (Apple rose about 2.9 points, Microsoft about 0.2 points).

**Grade:** answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.21 percentage points'

**Claims the tools did not back:** none

*2 tool calls, 6.6s, $0.0049*

**Answer:**

**Alphabet (GOOGL) improved the most**, with its net profit margin rising 4.21 percentage points, from 28.6% in FY2024 to 32.81% in FY2025.

- **GOOGL:** 28.6% → 32.81% (**+4.21 pp**); net income grew from $100.1 billion to $132.2 billion on revenue of $350.0 billion → $402.8 billion.
- **AAPL:** 23.97% → 26.92% (**+2.95 pp**); net income grew from $93.7 billion to $112.0 billion on revenue of $391.0 billion → $416.2 billion.
- **MSFT:** 35.96% → 36.15% (**+0.19 pp**); net income grew from $88.1 billion to $101.8 billion on revenue of $245.1 billion → $281.7 billion.

Note: the fiscal years cover different calendar months (Alphabet ends December 31, Apple late September, Microsoft June 30), so the periods are not perfectly aligned.

Sources: [SQL: income_statements]

---

## x_035#0: PASS (llm_judge, level 3)

**Question:** Apple's net income fell in fiscal year 2024 even though revenue grew. By how much did it fall, and what does the 10-K say caused it?

**Gold:** Net income fell from $97.0 billion in FY2023 to $93.7 billion in FY2024, a decrease of about $3.3 billion (3.4%), while revenue grew about 2.0%. The FY2024 10-K attributes the higher tax expense to a one-time income tax charge of $10.2 billion, net, related to the European Commission's State Aid Decision, which raised the effective tax rate to 24.1% from 14.7%.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** unsupported: Ireland granted Apple unlawful state aid via 1991 and 2007 tax opinions.

*4 tool calls, 22.7s, $0.0171*

**Answer:**

Apple's net income fell by **$3.3 billion** in FY2024 (from $97.0 billion to $93.7 billion, a 3.4% decline), even as revenue grew 2.0% to $391.0 billion — and the 10-K attributes the drop to a one-time income tax charge related to the European Commission State Aid Decision.

- **The numbers:** Net income fell from $96,995 million (FY2023) to $93,736 million (FY2024), a decline of $3,259 million (-3.4%), while revenue rose from $383,285 million to $391,035 million (+2.0%). Operating income actually *grew* 7.8% to $123,216 million, so the decline was entirely below the operating line.
- **The cause per the 10-K:** On September 10, 2024, the European Court of Justice set aside the 2020 General Court judgment and confirmed the Commission's 2016 State Aid Decision (that Ireland granted Apple unlawful state aid via 1991 and 2007 tax opinions). As a result, in Q4 2024 Apple recorded a **one-time income tax charge of $10.2 billion, net** — $15.8 billion payable to Ireland via release of escrow, partially offset by a $4.8 billion U.S. foreign tax credit and an $823 million decrease in unrecognized tax benefits.
- **Tax impact:** The provision for income taxes rose from $16,741 million to $29,749 million (+$13.0 billion), and the effective tax rate jumped from 14.7% to 24.1%. The MD&A states the 2024 effective tax rate was higher than 2023 "due primarily to a one-time income tax charge of $10.2 billion, net, related to the State Aid Decision," plus a higher effective tax rate on foreign earnings and lower tax benefits from share-based compensation.
- **Balance-sheet note:** As of September 28, 2024, Apple owed €14.2 billion ($15.8 billion) to Ireland, expected to be paid within 12 months, with the funds held in escrow and restricted from general use.

Sources: [SQL: income_statements], [AAPL FY2024 10-K, p.27], [AAPL FY2024 10-K, p.42]

---

## x_036#0: PASS (llm_judge, level 4)

**Question:** Microsoft and Alphabet both grew operating income in fiscal year 2025. By how much did each grow, and what does each company's 10-K say drove it?

**Gold:** Microsoft's operating income rose $19.1 billion (about 17.4%), from $109.4 billion to $128.5 billion; its 10-K says the growth came from all of its segments. Alphabet's rose $16.6 billion (about 14.8%), from $112.4 billion to $129.0 billion; its 10-K attributes the segment gains mainly to higher revenues: Google Services operating income rose $18.1 billion and Google Cloud $7.8 billion, partly offset by a $3.1 billion larger Other Bets loss and higher Alphabet-level AI research costs.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** unsupported: Expense growth lagging revenue growth is what carried Microsoft's operating income gain

*4 tool calls, 24.6s, $0.0221*

**Answer:**

Microsoft's operating income grew $19.1 billion (17.4%) in FY2025, from $109.4 billion to $128.5 billion, while Alphabet's grew $16.6 billion (14.8%), from $112.4 billion to $129.0 billion. (Note the fiscal years cover different months: Microsoft's FY2025 ended June 30, 2025; Alphabet's ended December 31, 2025.)

**Microsoft — what drove it (FY2025 10-K, MD&A):**
- Operating income "increased $19.1 billion or 17% with growth across each of our segments" — Intelligent Cloud, Productivity and Business Processes, and More Personal Computing.
- Revenue rose $36.6 billion or 15%: Intelligent Cloud driven by Azure (Azure and other cloud services revenue grew 34%), Productivity and Business Processes driven by Microsoft 365 Commercial cloud, and More Personal Computing driven by Gaming and Search and news advertising.
- Gross margin increased $22.9 billion or 13%, but gross margin percentage decreased slightly — Microsoft Cloud gross margin percentage fell to 69% "driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure."
- Operating expenses rose only $3.8 billion or 6%, driven by investments in cloud and AI engineering and Gaming (including the Activision Blizzard acquisition impact) — expense growth lagging revenue growth is what carried the operating income gain.

**Alphabet — what drove it (FY2025 10-K, MD&A and Note 15):**
- Google Services operating income increased $18.1 billion (to $139.4 billion), "primarily driven by an increase in revenues, partially offset by an increase in expenses related to legal and other matters, TAC, and content acquisition costs."
- Google Cloud operating income increased $7.8 billion (to $13.9 billion), "primarily driven by an increase in revenues, partially offset by increases in usage costs for technical infrastructure and employee compensation expenses."
- Revenue rose 15% to $402.8 billion, driven by Google Services (+$37.8 billion, +12%, led by Google Search & other +$26.4 billion) and Google Cloud (+$15.5 billion, +36%, largely from Google Cloud Platform infrastructure and platform services).
- Partially offsetting the segment gains: Other Bets' operating loss widened to $7.5 billion (from $4.4 billion) and Alphabet-level activities' loss widened to $16.8 billion (from $10.5 billion).

Sources: [SQL: income_statements]; [MSFT FY2025 10-K, p.37-38]; [GOOGL FY2025 10-K, p.34, 36-37, 39, 88]

---

## x_037#0: PASS (llm_judge, level 3)

**Question:** How does Microsoft's fiscal year 2025 10-K define Microsoft Cloud revenue, and how much was it in each of the last three fiscal years?

**Gold:** Microsoft Cloud revenue includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365. It was $168.9 billion in FY2025, $137.7 billion in FY2024 and $111.6 billion in FY2023.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 23.2s, $0.0201*

**Answer:**

Microsoft's FY2025 10-K defines Microsoft Cloud revenue as revenue from **Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365**, and reports it at **$168.9 billion in FY2025, $137.7 billion in FY2024, and $111.6 billion in FY2023**.

- **Definition** (Item 7, p.36 and Item 8, p.80): "Revenue from Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365." These amounts are included within the Microsoft 365 Commercial products and cloud services, Server products and cloud services, LinkedIn, and Dynamics products and cloud services lines in the product-and-service revenue table.
- **Amounts by year** (Item 8, p.80): $168.9 billion (FY2025), $137.7 billion (FY2024), $111.6 billion (FY2023) — growth of 22.7% in FY2025 and 23.4% in FY2024 (the filing rounds both to 23%).
- **Note on the prior filing**: the FY2024 10-K (p.92) defined Microsoft Cloud slightly differently (Azure and other cloud services, Office 365 Commercial, the commercial portion of LinkedIn, Dynamics 365, and other commercial cloud properties) and reported FY2024 as $137.4 billion. The FY2025 10-K's figures reflect the recast presentation, so the $137.7 billion FY2024 figure is the one to use.

Sources: [MSFT FY2025 10-K, p.80], [MSFT FY2025 10-K, p.36], [MSFT FY2025 10-K, p.33], [MSFT FY2024 10-K, p.92]

---

## x_038#0: PASS (llm_judge, level 4)

**Question:** How much did Apple and Alphabet each spend on share repurchases in fiscal year 2025, and which spent more?

**Gold:** Apple spent more. Apple's cash flow statement shows $90.7 billion of repurchases of common stock in FY2025 (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable). Alphabet repurchased 240 million shares for $45.4 billion.

**Grade:** 3/3 facts covered

**Claims the tools did not back:** unsupported: The difference between Apple's $89.3 billion repurchase note and $90.7 billion cash flow figure reflects settlement timing.

*4 tool calls, 33.1s, $0.0278*

**Answer:**

Apple spent more: Apple repurchased $89.3 billion of its common stock in fiscal 2025 (year ended September 27, 2025), versus Alphabet's $45.4 billion (year ended December 31, 2025) — a difference of $43.9 billion, with Apple spending about 1.97x as much.

- **Apple (FY2025):** Repurchased 402 million shares for $89.3 billion under its share repurchase programs (per the Share Repurchase Program note). The cash flow statement shows $90.7 billion of cash used for "Repurchases of common stock," the difference reflecting settlement timing. Apple exhausted the final $19.8 billion of its May 2024 $110 billion program in Q4 and announced a new $100 billion program in May 2025, of which only $221 million had been utilized by year-end.
- **Alphabet (FY2025):** Repurchased and retired 240 million shares for $45.4 billion — $6.5 billion of Class A shares (37 million shares) and $38.9 billion of Class C shares (203 million shares). Its board authorized $70.0 billion programs in both April 2024 and April 2025, leaving $69.5 billion available as of December 31, 2025.
- Note the fiscal years cover different calendar months (Apple's ended September 27, 2025; Alphabet's ended December 31, 2025).

Sources: [AAPL FY2025 10-K, p.45], [AAPL FY2025 10-K, p.33], [AAPL FY2025 10-K, p.21], [GOOGL FY2025 10-K, p.80], [GOOGL FY2025 10-K, p.42], [GOOGL FY2025 10-K, p.35]

---

## x_039#0: PASS (llm_judge, level 2)

**Question:** What share of Alphabet's revenue came from Google Cloud in fiscal year 2025, and how did that share change from fiscal year 2024?

**Gold:** Google Cloud was about 14.6% of Alphabet's FY2025 revenue ($58.7 billion of $402.8 billion), up from about 12.4% in FY2024 ($43.2 billion of $350.0 billion), an increase of about 2.2 percentage points.

**Grade:** 4/4 facts covered

**Claims the tools did not back:** none

*2 tool calls, 12.3s, $0.0083*

**Answer:**

Google Cloud contributed 14.6% of Alphabet's revenue in FY2025, up from 12.4% in FY2024 — an increase of about 2.2 percentage points.

- Google Cloud revenue: $58.7 billion in FY2025 vs. $43.2 billion in FY2024, growth of 35.8%.
- Total Alphabet revenue: $402.8 billion in FY2025 vs. $350.0 billion in FY2024, growth of 15.1%.
- Because Cloud grew more than twice as fast as the company overall, its share of consolidated revenue rose from 12.4% to 14.6%.

Sources: [SQL: segment_revenue], [SQL: income_statements]

---

## x_040#0: PASS (fuzzy_numeric, level 3)

**Question:** What percentage of Microsoft's fiscal year 2025 revenue came from Microsoft Cloud?

**Gold:** About 60.0% ($168.9 billion of $281.7 billion).

**Grade:** answer's figure '60.0%' matches 59.952293734293136 (pct)

**Claims the tools did not back:** unsupported: Microsoft Cloud is a supplemental revenue measure disclosed in the 10-K.

*3 tool calls, 13.6s, $0.0100*

**Answer:**

Microsoft Cloud accounted for approximately 60.0% of Microsoft's fiscal year 2025 total revenue ($168.9 billion of $281.7 billion).

- Microsoft Cloud revenue was $168.9 billion in FY2025, up 23% from $137.7 billion in FY2024, per the FY2025 10-K.
- Microsoft's total FY2025 revenue was $281.7 billion, so Microsoft Cloud represented 59.95% of total revenue.
- Microsoft Cloud includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365; these amounts are embedded within the Server products and cloud services, Microsoft 365 Commercial, LinkedIn, and Dynamics product lines rather than reported as a separate segment.
- Microsoft Cloud is not one of Microsoft's three reportable segments (Intelligent Cloud, Productivity and Business Processes, More Personal Computing) — it is a supplemental revenue measure disclosed in the 10-K.

Sources: [SQL: income_statements]; [MSFT FY2025 10-K, p.33]; [MSFT FY2025 10-K, p.80]

---

## x_041#0: PASS (llm_judge, level 5)

**Question:** Which company grew its operating income the fastest from fiscal year 2024 to fiscal year 2025, and what does that company's 10-K say drove the growth?

**Gold:** Microsoft, with operating income up about 17.4% (from $109.4 billion to $128.5 billion), ahead of Alphabet (about 14.8%) and Apple (about 8.0%). Its FY2025 10-K says operating income increased $19.1 billion or 17% with growth across each of its segments; gross margin increased $22.9 billion or 13%, also with growth across each segment.

**Grade:** 4/4 facts covered

**Claims the tools did not back:** none

*5 tool calls, 24.9s, $0.0255*

**Answer:**

**Microsoft grew operating income the fastest from FY2024 to FY2025, at 17.4%** (from $109.4 billion to $128.5 billion, up $19.1 billion), ahead of Alphabet at 14.8% ($112.4B → $129.0B) and Apple at 8.0% ($123.2B → $133.1B).

**Growth rates (FY2024 → FY2025 operating income):**
- Microsoft: +17.4% ($109,433M → $128,528M)
- Alphabet: +14.8% ($112,390M → $129,039M)
- Apple: +8.0% ($123,216M → $133,050M)

**What Microsoft's FY2025 10-K says drove the growth (MD&A, "Fiscal Year 2025 Compared with Fiscal Year 2024"):**
- Operating income increased $19.1 billion or 17% "with growth across each of our segments," on revenue up $36.6 billion or 15% — Intelligent Cloud driven by Azure, Productivity and Business Processes driven by Microsoft 365 Commercial cloud, and More Personal Computing driven by Gaming and Search and news advertising.
- Gross margin increased $22.9 billion or 13% with growth across each segment; Microsoft Cloud gross margin percentage declined to 69% due to scaling AI infrastructure, partly offset by efficiency gains in Azure.
- Operating expenses rose only $3.8 billion or 6% (investments in cloud and AI engineering and Gaming, including the Activision Blizzard acquisition), so revenue growth far outpaced expense growth.
- By segment (recast for the August 2024 segment reorganization): Productivity and Business Processes operating income +$10.1 billion or 17% (Microsoft 365 Commercial cloud); Intelligent Cloud +$6.8 billion or 18% (Azure, which grew 34%); More Personal Computing +$2.2 billion or 18% (Gaming and Search and news advertising).

Note: Microsoft's fiscal year ends June 30, while Apple's ends in late September and Alphabet's December 31, so the periods cover different calendar months.

Sources: [SQL: income_statements]; [MSFT FY2025 10-K, p.37]; [MSFT FY2025 10-K, p.38]; [MSFT FY2025 10-K, p.35]

---

## x_042#0: PASS (llm_judge, level 5)

**Question:** Which company spent the largest share of its revenue on research and development in fiscal year 2025, and what does its 10-K say about its investment in AI infrastructure?

**Gold:** Alphabet, at about 15.2% of revenue ($61.1 billion of $402.8 billion; Microsoft about 11.5%, Apple about 8.3%). Its FY2025 10-K says it continues to invest in capital expenditures to scale its technical infrastructure, in particular for AI; it invested heavily in 2025 ($91.4 billion of capital expenditures) and expects to significantly increase that investment in 2026 (servers, network equipment and data centers). It expects the costs of operating that infrastructure (depreciation, energy, equipment, network capacity) to increase significantly because AI requires more compute than its historical offerings.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 24.9s, $0.0186*

**Answer:**

**Alphabet (GOOGL) spent the largest share of its revenue on R&D in FY2025: 15.2% ($61.1 billion of $402.8 billion in revenue).**

**R&D as a share of revenue, FY2025:**
- Alphabet: 15.2% ($61.1B / $402.8B) — its 10-K reports R&D as 15% of revenues, up from 14% in 2024
- Microsoft: 11.5% ($32.5B / $281.7B)
- Apple: 8.3% ($34.6B / $416.2B)

(Note: fiscal years differ — Alphabet's FY2025 ended December 31, 2025; Microsoft's ended June 30, 2025; Apple's ended late September 2025.)

**What Alphabet's FY2025 10-K says about AI infrastructure investment:**
- **"Increased Investment in Technical Infrastructure" (MD&A trends):** Alphabet continues to invest in capital expenditures as it scales its technical infrastructure, "in particular for AI," to meet user and enterprise customer demand and to support internal research. It invested heavily in capex in 2025 and expects to **significantly increase** its investment in 2026 relative to 2025, including servers and network equipment and data centers.
- **Capital expenditures:** $91.4 billion in 2025, up from $52.5 billion in 2024, primarily reflecting investments in technical infrastructure (servers, network equipment, data center land, and building construction). Depreciation on property and equipment rose to $21.1 billion in 2025 from $15.3 billion in 2024.
- **Rising operating costs:** Costs of operating its technical infrastructure — depreciation, energy, equipment, and network capacity — are expected to significantly increase because developing and serving AI offerings requires more compute power than historical consumer and enterprise offerings; Alphabet expects to offset this partly through data center efficiencies, e.g., AI model design and its TPU- and GPU-based infrastructure.
- **Strategic framing (Item 1):** Alphabet describes its AI-optimized infrastructure as "a key differentiator" powering its own products (Search, YouTube) and Google Cloud, offering a range of AI accelerators including GPUs and its custom TPUs, such as Ironwood, its seventh-generation TPU.
- Relatedly, R&D expense itself rose $11.8 billion from 2024 to 2025, driven mainly by employee compensation (+$6.9B, including a Waymo valuation-based compensation charge) and depreciation (+$2.4B).

Sources: [SQL: income_statements], [GOOGL FY2025 10-K, p.30], [GOOGL FY2025 10-K, p.35], [GOOGL FY2025 10-K, p.37-38], [GOOGL FY2025 10-K, p.41], [GOOGL FY2025 10-K, p.5]

---

## x_043#0: PASS (llm_judge, level 5)

**Question:** Which of Apple's geographic segments performed worst in fiscal year 2025, and what reason does the 10-K give?

**Gold:** Greater China, the only region to decline: net sales fell about 3.8%, from $66.95 billion to $64.38 billion, while the Americas (+6.8%), Europe (+9.6%), Japan (+14.6%) and Rest of Asia Pacific (+9.9%) grew. The FY2025 10-K says the decrease was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Grade:** 5/5 facts covered

**Claims the tools did not back:** none

*4 tool calls, 18.6s, $0.0195*

**Answer:**

Greater China was Apple's worst-performing geographic segment in fiscal 2025 — the only one of its five reportable segments to decline, with net sales falling 3.8% to $64.4 billion from $67.0 billion in FY2024. The 10-K attributes the decline primarily to lower iPhone net sales, partially offset by higher Mac net sales.

- **Greater China:** $64.4 billion in FY2025 vs. $67.0 billion in FY2024, down $2.6 billion or 3.8% (the filing rounds this to (4)%). It was the second consecutive decline, following an (8)% drop in FY2024.
- **All other segments grew:** Americas +7% to $178.4 billion, Europe +10% to $111.0 billion, Japan +15% to $28.7 billion, and Rest of Asia Pacific +10% to $33.7 billion.
- **Reason per the 10-K (MD&A, Segment Operating Performance):** "Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
- Note: Apple's reportable segments are geographic (Americas, Europe, Greater China, Japan, Rest of Asia Pacific); the database's `segment_revenue` table for Apple instead holds product/service categories, so this answer uses the geographic segment data.

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]

---

## x_045#0: PASS (llm_judge, level 6)

**Question:** Do Alphabet's segment revenues in the database add up to its total revenue for fiscal year 2025? Explain any difference.

**Gold:** Not exactly. Google Services ($342.7 billion), Google Cloud ($58.7 billion) and Other Bets ($1.5 billion) sum to about $403.0 billion, about $127 million more than total revenue of $402.8 billion. The difference is a $127 million hedging loss, a reconciling item rather than a segment; segments plus hedging equal consolidated revenue.

**Grade:** 5/5 facts covered

**Claims the tools did not back:** none

*5 tool calls, 24.6s, $0.0219*

**Answer:**

No — the three reportable segments alone sum to $403.0 billion, which is $127 million more than Alphabet's FY2025 total revenue of $402.8 billion; the difference is exactly offset by a "Hedging gains (losses)" reconciling item of –$127 million, so the segments plus that item add up precisely.

- Segment revenues in the database (FY2025): Google Services $342.7 billion, Google Cloud $58.7 billion, Other Bets $1.5 billion — sum $403.0 billion.
- Total revenue per the income statement: $402.8 billion, leaving a $127 million gap.
- The database also contains a "Hedging gains (losses)" row of –$127 million. This is not a segment — it is a reconciling item. Adding it gives $402.8 billion, matching total revenue exactly.
- The FY2025 10-K (Note 15, p.88) confirms this structure: Alphabet reports three segments (Google Services, Google Cloud, Other Bets) and states that "hedging gains (losses) related to revenue are not allocated to our segments." The same note's table shows the identical figures, with hedging losses of $(127) million bridging the segments to total revenues of $402,836 million.
- The hedging item reflects Alphabet's foreign currency cash flow hedges: per Note 7 (p.67), Alphabet designates foreign currency forwards and options as cash flow hedges of forecasted revenue transactions denominated in non-US-dollar currencies, and those hedge results are reclassified into revenue when the hedged revenue is recognized.

Sources: [SQL: segment_revenue], [SQL: income_statements], [GOOGL FY2025 10-K, p.88], [GOOGL FY2025 10-K, p.67]

---

## x_047#0: PASS (llm_judge, level 4)

**Question:** How do Microsoft's and Alphabet's fiscal year 2025 10-Ks describe the effect of AI infrastructure on their costs and margins?

**Gold:** Microsoft says scaling its AI infrastructure lowered gross margin percentages: Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure, and operating expenses rose on investments in cloud and AI engineering. Alphabet says it is significantly increasing investment in technical infrastructure, in particular for AI, and that the costs of operating it (depreciation, energy, equipment and network capacity) are expected to increase significantly because AI offerings require more compute; Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure.

**Grade:** 6/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering

**Claims the tools did not back:** unsupported: Alphabet frames AI infrastructure with expected downward pressure on operating margin.

*3 tool calls, 39.2s, $0.0271*

**Answer:**

Both FY2025 10-Ks describe AI infrastructure as a meaningful driver of rising costs and margin pressure: Microsoft quantifies it as a slight decline in gross margin percentage (Microsoft Cloud gross margin fell to 69%), while Alphabet frames it as significantly increasing technical-infrastructure costs (depreciation, energy, equipment, network capacity) with expected downward pressure on operating margin. Note the fiscal years differ: Microsoft's FY2025 ended June 30, 2025; Alphabet's ended December 31, 2025.

**Microsoft (FY2025 10-K)**
- Cost of revenue increased $13.7 billion or 19%, driven by growth in Microsoft Cloud; gross margin dollars grew $22.9 billion or 13%, but gross margin percentage decreased slightly, driven by Intelligent Cloud (p.37).
- Microsoft Cloud gross margin percentage decreased to 69%, "driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure" (p.37).
- By segment: Intelligent Cloud cost of revenue rose $10.6 billion or 36% on Azure growth, with gross margin percentage down from scaling AI infrastructure, partly offset by Azure efficiency gains (p.38); Productivity and Business Processes gross margin percentage decreased slightly primarily from scaling AI infrastructure, offset by Microsoft 365 Commercial cloud efficiencies (p.38).
- Forward-looking: "The investments we are making in cloud and AI infrastructure and devices will continue to increase our operating costs and may decrease our operating margins," with datacenters dependent on land, energy, networking supplies, and servers including GPUs (p.34). The Risk Factors add that Microsoft is "incurring significant costs to build and maintain infrastructure to support cloud-based and AI services, reducing operating margins" (p.17).

**Alphabet (FY2025 10-K)**
- In its "Increased Investment in Technical Infrastructure" trend discussion, Alphabet says the costs of operating its technical infrastructure — depreciation, energy, equipment, and network capacity — "are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings," while it expects to keep driving data-center efficiencies through AI model design and its TPU/GPU-based infrastructure (p.30).
- Realized in FY2025: cost of revenues increased $16.2 billion to $162.5 billion (+11%), with the other cost of revenues increase driven primarily by content acquisition costs (largely YouTube), depreciation expense, and other technical infrastructure operations costs (pp.34, 37); operating expenses rose 22% to $111.3 billion, also driven in part by depreciation (p.34).
- Google Cloud operating income increased $7.8 billion, "primarily driven by an increase in revenues, partially offset by increases in usage costs for technical infrastructure" (p.39).
- Margin framing: Alphabet warns it "may experience downward pressure on our operating margin" from a higher level of investment in technical infrastructure (Risk Factors, p.12), and that AI offerings "may monetize differently than our historical consumer and enterprise offerings which could affect revenue growth rates and margin trends" (p.30).

**Common thread:** both companies tie rising costs to AI compute (datacenters, servers, GPUs/TPUs), both cite offsetting efficiency efforts, and both flag margin pressure — Microsoft reports it as already realized in gross margin percentage (slightly), while Alphabet presents it largely as expected/forward-looking pressure on operating margin.

Sources: [MSFT FY2025 10-K, p.17], [MSFT FY2025 10-K, p.34], [MSFT FY2025 10-K, p.37], [MSFT FY2025 10-K, p.38], [GOOGL FY2025 10-K, p.12], [GOOGL FY2025 10-K, p.30], [GOOGL FY2025 10-K, p.34], [GOOGL FY2025 10-K, p.37], [GOOGL FY2025 10-K, p.39]

---

## x_048#0: PASS (llm_judge, level 4)

**Question:** Which company had the highest capital expenditures in fiscal year 2025, and which had the highest capital expenditures relative to revenue?

**Gold:** Alphabet spent the most in dollars: $91.4 billion of purchases of property and equipment (Microsoft $64.6 billion, Apple $12.7 billion). Relative to revenue, Microsoft was narrowly highest at about 22.9% ($64.6 billion of $281.7 billion), just ahead of Alphabet at about 22.7% ($91.4 billion of $402.8 billion); Apple was about 3.1%.

**Grade:** 5/5 facts covered

**Claims the tools did not back:** unsupported: Apple's low capex is consistent with its asset-lighter hardware model.

*5 tool calls, 17.2s, $0.0198*

**Answer:**

**Alphabet had the highest capital expenditures in FY2025 ($91.4 billion), while Microsoft had the highest capex relative to revenue (22.9% of revenue, just ahead of Alphabet's 22.7%).**

- **Alphabet (GOOGL):** $91.4 billion in purchases of property and equipment (FY ended Dec 31, 2025), driven primarily by investments in technical infrastructure — servers, network equipment, and data centers. That equals 22.7% of its $402.8 billion revenue.
- **Microsoft (MSFT):** $64.6 billion in additions to property and equipment (FY ended June 30, 2025), up $20.1 billion year-over-year, supporting cloud and AI infrastructure. That equals 22.9% of its $281.7 billion revenue — the highest intensity of the three.
- **Apple (AAPL):** $12.7 billion in payments for acquisition of property, plant and equipment (FY ended Sept 27, 2025), only 3.1% of its $416.2 billion revenue — far below the other two, consistent with its asset-lighter hardware model.

Note that the three fiscal years cover different calendar months (Microsoft's ended June 30, 2025; Apple's September 27, 2025; Alphabet's December 31, 2025), so the comparison is not on identical calendar periods.

Sources:
- [GOOGL FY2025 10-K, p.53] (cash flow statement) and [GOOGL FY2025 10-K, p.41] (MD&A capital expenditures)
- [MSFT FY2025 10-K, p.50] (cash flow statement)
- [AAPL FY2025 10-K, p.33] (cash flow statement)
- [SQL: income_statements] (FY2025 revenue for all three companies)

---

## x_049#0: PASS (llm_judge, level 7)

**Question:** Which other region grew the fastest, and why?

*Follow-up to:* How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and why?

**Gold:** Japan grew fastest: net sales rose about 14.6%, from $25.1 billion to $28.7 billion. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** none

*4 tool calls, 13.7s, $0.0145*

**Answer:**

Japan grew the fastest, with net sales up 14.6% (the 10-K rounds to 15%), from $25.05 billion in FY2024 to $28.70 billion in FY2025. The FY2025 10-K attributes this primarily to higher net sales of iPhone, Services and iPad.

- Growth by region (FY2024 → FY2025): Japan 14.6%; Rest of Asia Pacific 9.9%; Europe 9.6%; Americas 6.8%; Greater China declined 3.8%.
- Japan's increase was driven by iPhone, Services and iPad — the only region where iPad was cited as a driver.

Sources: [SQL: geographic_revenue], [AAPL FY2025 10-K, p.24]

---

