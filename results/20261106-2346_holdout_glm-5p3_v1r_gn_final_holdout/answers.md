# Answers: 20261106-2346_holdout_glm-5p3_v1r_gn_final_holdout

39/39 passed. Failed answers first. Scorecard: [scorecard.md](scorecard.md).

## x_005#0: PASS (fuzzy_numeric, level 1)

**Question:** What was Alphabet's operating income in fiscal year 2024?

**Gold:** $112.4 billion

**Grade:** answer's figure '$112.4 billion' matches 112390000000 (usd)

**Claims the tools did not back:** none

*2 tool calls, 9.0s, $0.0070*

**Answer:**

Alphabet's operating income (income from operations) in fiscal year 2024 was **$112.4 billion** ($112,390 million), on revenues of $350.0 billion.

- This was up 33% from $84,293 million in FY2023, with operating margin expanding from 27% to 32%, per the FY2024 10-K's Executive Overview.
- By segment (FY2024 10-K, Note 15): Google Services $121,263 million, Google Cloud $6,112 million, Other Bets $(4,444) million, and Alphabet-level activities $(10,541) million, summing to the $112,390 million total.
- Alphabet's fiscal year 2024 covered January 1 – December 31, 2024.

Sources: [SQL: income_statements]; [GOOGL FY2024 10-K, p.37]; [GOOGL FY2024 10-K, p.54]; [GOOGL FY2024 10-K, p.90]

---

## x_005#1: PASS (fuzzy_numeric, level 1)

**Question:** What was Alphabet's operating income in fiscal year 2024?

**Gold:** $112.4 billion

**Grade:** answer's figure '$112.4 billion' matches 112390000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.2s, $0.0046*

**Answer:**

Alphabet's operating income in fiscal year 2024 was **$112.4 billion** (on revenue of $350.0 billion, for the year ended December 31, 2024).

Sources: [SQL: income_statements]

---

## x_005#2: PASS (fuzzy_numeric, level 1)

**Question:** What was Alphabet's operating income in fiscal year 2024?

**Gold:** $112.4 billion

**Grade:** answer's figure '$112.4 billion' matches 112390000000 (usd)

**Claims the tools did not back:** none

*2 tool calls, 8.1s, $0.0076*

**Answer:**

Alphabet's operating income in fiscal year 2024 (January 1 – December 31, 2024) was **$112.4 billion**.

- This was earned on revenue of $350.0 billion, an operating margin of 32.1% (computed as 112,390 / 350,018).

Sources: [SQL: income_statements]

---

## x_006#0: PASS (fuzzy_numeric, level 2)

**Question:** What was Apple's gross margin percentage in fiscal year 2025?

**Gold:** 46.9%

**Grade:** answer's figure '46.9%' matches 46.90516410716045 (pct)

**Claims the tools did not back:** none

*2 tool calls, 4.7s, $0.0032*

**Answer:**

Apple's gross margin percentage in fiscal year 2025 was **46.9%**.

- Revenue: $416.2 billion
- Cost of revenue: $221.0 billion
- Gross profit: $195.2 billion
- Gross margin = $195.2 billion ÷ $416.2 billion = 46.9%

Sources: [SQL: income_statements]

---

## x_006#1: PASS (fuzzy_numeric, level 2)

**Question:** What was Apple's gross margin percentage in fiscal year 2025?

**Gold:** 46.9%

**Grade:** answer's figure '46.9%' matches 46.90516410716045 (pct)

**Claims the tools did not back:** none

*2 tool calls, 3.8s, $0.0033*

**Answer:**

Apple's gross margin percentage in fiscal year 2025 was **46.9%**.

- Gross profit: $195.2 billion
- Total net sales (revenue): $416.2 billion
- Gross margin = $195.2B ÷ $416.2B = 46.9%

Sources: [SQL: income_statements]

---

## x_006#2: PASS (fuzzy_numeric, level 2)

**Question:** What was Apple's gross margin percentage in fiscal year 2025?

**Gold:** 46.9%

**Grade:** answer's figure '46.9%' matches 46.90516410716045 (pct)

**Claims the tools did not back:** none

*2 tool calls, 5.1s, $0.0060*

**Answer:**

Apple's gross margin percentage in fiscal year 2025 was **46.9%**.

- Revenue: $416.2 billion
- Cost of revenue: $221.0 billion
- Gross profit: $195.2 billion
- Gross margin = $195.2 billion ÷ $416.2 billion = 46.9%

Sources: [SQL: income_statements]

---

## x_010#0: PASS (fuzzy_numeric, level 2)

**Question:** What was Microsoft's debt-to-equity ratio (total debt divided by stockholders' equity) at the end of fiscal year 2025?

**Gold:** About 0.13 ($43.2 billion of total debt / $343.5 billion of stockholders' equity).

**Grade:** answer's figure '0.13' matches 0.12562922332951942 (plain)

**Claims the tools did not back:** unsupported: Microsoft carries a very low level of debt relative to its equity base.

*2 tool calls, 3.3s, $0.0042*

**Answer:**

Microsoft's debt-to-equity ratio at the end of fiscal year 2025 (June 30, 2025) was **0.13** (0.1256).

- Total debt: $43.2 billion ($43,151 million)
- Stockholders' equity: $343.5 billion ($343,479 million)
- Ratio: $43,151M ÷ $343,479M = 0.13

This indicates Microsoft carries a very low level of debt relative to its equity base.

Sources: [SQL: balance_sheets]

---

## x_010#1: PASS (fuzzy_numeric, level 2)

**Question:** What was Microsoft's debt-to-equity ratio (total debt divided by stockholders' equity) at the end of fiscal year 2025?

**Gold:** About 0.13 ($43.2 billion of total debt / $343.5 billion of stockholders' equity).

**Grade:** answer's figure '0.13' matches 0.12562922332951942 (plain)

**Claims the tools did not back:** unsupported: Microsoft carries relatively little debt relative to its equity base.

*2 tool calls, 3.5s, $0.0032*

**Answer:**

Microsoft's debt-to-equity ratio at the end of fiscal year 2025 (June 30, 2025) was **0.13** (0.1256).

- Total debt: $43.2 billion ($43,151 million)
- Stockholders' equity: $343.5 billion ($343,479 million)
- Ratio: $43.2B ÷ $343.5B = 0.13

This indicates Microsoft carries relatively little debt relative to its equity base.

Sources: [SQL: balance_sheets]

---

## x_010#2: PASS (fuzzy_numeric, level 2)

**Question:** What was Microsoft's debt-to-equity ratio (total debt divided by stockholders' equity) at the end of fiscal year 2025?

**Gold:** About 0.13 ($43.2 billion of total debt / $343.5 billion of stockholders' equity).

**Grade:** answer's figure '0.13' matches 0.12562922332951942 (plain)

**Claims the tools did not back:** none

*2 tool calls, 3.0s, $0.0033*

**Answer:**

Microsoft's debt-to-equity ratio at the end of fiscal year 2025 (June 30, 2025) was **0.13** (0.1256).

- Total debt: $43.2 billion ($43,151 million)
- Stockholders' equity: $343.5 billion ($343,479 million)
- Ratio: $43,151M ÷ $343,479M = 0.1256, i.e. roughly $0.13 of debt for every $1 of equity

Sources: [SQL: balance_sheets]

---

## x_012#0: PASS (exact_match_entity, level 2)

**Question:** Which company had the largest cash and cash equivalents balance at the end of its most recent fiscal year, and how much was it?

**Gold:** Apple, with $35.9 billion (Alphabet $30.7 billion, Microsoft $30.2 billion).

**Grade:** answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion'

**Claims the tools did not back:** none

*1 tool calls, 3.4s, $0.0032*

**Answer:**

Apple had the largest cash and cash equivalents balance at the end of FY2025, at $35.9 billion (as of September 27, 2025).

- **AAPL:** $35.9 billion (period ended 2025-09-27)
- **GOOGL:** $30.7 billion (period ended 2025-12-31)
- **MSFT:** $30.2 billion (period ended 2025-06-30)

Note that the three companies' fiscal years end in different months (Apple in late September, Microsoft in June, Alphabet in December), so these balances are as of different dates within calendar 2025.

Sources: [SQL: balance_sheets]

---

## x_012#1: PASS (exact_match_entity, level 2)

**Question:** Which company had the largest cash and cash equivalents balance at the end of its most recent fiscal year, and how much was it?

**Gold:** Apple, with $35.9 billion (Alphabet $30.7 billion, Microsoft $30.2 billion).

**Grade:** answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion'

**Claims the tools did not back:** none

*1 tool calls, 3.1s, $0.0027*

**Answer:**

Apple had the largest cash and cash equivalents balance at the end of FY2025, at $35.9 billion (period ended September 27, 2025).

- **AAPL:** $35.9 billion (FY2025 ended September 27, 2025)
- **GOOGL:** $30.7 billion (FY2025 ended December 31, 2025)
- **MSFT:** $30.2 billion (FY2025 ended June 30, 2025)

Note that the three fiscal years end in different months, so these balances are as of different dates. This comparison covers cash and cash equivalents only, not total cash plus marketable securities.

Sources: [SQL: balance_sheets]

---

## x_012#2: PASS (exact_match_entity, level 2)

**Question:** Which company had the largest cash and cash equivalents balance at the end of its most recent fiscal year, and how much was it?

**Gold:** Apple, with $35.9 billion (Alphabet $30.7 billion, Microsoft $30.2 billion).

**Grade:** answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion'

**Claims the tools did not back:** none

*1 tool calls, 2.9s, $0.0027*

**Answer:**

Apple had the largest cash and cash equivalents balance at the end of FY2025, at $35.9 billion (period ended September 27, 2025).

- **AAPL:** $35.9 billion (FY2025 ended September 27, 2025)
- **GOOGL:** $30.7 billion (FY2025 ended December 31, 2025)
- **MSFT:** $30.2 billion (FY2025 ended June 30, 2025)

Note that the three companies' fiscal years end in different months, so these balances are as of different dates within calendar 2025.

Sources: [SQL: balance_sheets]

---

## x_016#0: PASS (fuzzy_numeric, level 1)

**Question:** According to Microsoft's fiscal year 2025 10-K, by how much did Azure and other cloud services revenue grow?

**Gold:** 34%

**Grade:** answer's figure '34%' matches 34 (pct)

**Claims the tools did not back:** unsupported: The 10-K discloses Azure growth only as a percentage, not a dollar amount.

*1 tool calls, 6.7s, $0.0080*

**Answer:**

According to Microsoft's FY2025 10-K, Azure and other cloud services revenue grew **34%** in fiscal year 2025 compared with fiscal year 2024.

- The MD&A states: "Azure and other cloud services revenue grew 34% driven by demand for our portfolio of services" (p.38), and the Overview section repeats the 34% growth figure (p.34).
- This growth drove Server products and cloud services revenue up $18.6 billion, or 23%, within the Intelligent Cloud segment (p.38).
- The 10-K discloses Azure growth only as a percentage, not a dollar amount; Intelligent Cloud segment revenue overall rose from $87.5 billion to $106.3 billion, up 21% (p.37).

Sources: [MSFT FY2025 10-K, p.38], [MSFT FY2025 10-K, p.34], [MSFT FY2025 10-K, p.37]

---

## x_016#1: PASS (fuzzy_numeric, level 1)

**Question:** According to Microsoft's fiscal year 2025 10-K, by how much did Azure and other cloud services revenue grow?

**Gold:** 34%

**Grade:** answer's figure '34%' matches 34 (pct)

**Claims the tools did not back:** unsupported: The 10-K reports Azure growth only as a percentage, not a dollar amount.; unsupported: The 34% figure is the extent of the disclosed Azure growth.

*1 tool calls, 6.2s, $0.0053*

**Answer:**

According to Microsoft's FY2025 10-K, Azure and other cloud services revenue grew **34%** in fiscal year 2025 compared with fiscal year 2024.

- The filing states: "Azure and other cloud services revenue grew 34% driven by demand for our portfolio of services" (Item 7, MD&A, discussion of Server products and cloud services).
- This growth drove Server products and cloud services revenue up $18.6 billion or 23%, within the Intelligent Cloud segment, whose revenue increased $18.8 billion or 21% to $106.3 billion.
- The 10-K reports Azure growth only as a percentage, not a dollar amount, so the 34% figure is the extent of the disclosed growth.
- Note: Microsoft's fiscal year 2025 ended June 30, 2025.

Sources: [MSFT FY2025 10-K, p.38]

---

## x_016#2: PASS (fuzzy_numeric, level 1)

**Question:** According to Microsoft's fiscal year 2025 10-K, by how much did Azure and other cloud services revenue grow?

**Gold:** 34%

**Grade:** answer's figure '34%' matches 34 (pct)

**Claims the tools did not back:** unsupported: The 10-K reports Azure growth only as a percentage (34%), not as a dollar amount.; contradicted: Server products and cloud services revenue itself is not separately broken out in the filing's revenue tables.

*1 tool calls, 7.2s, $0.0055*

**Answer:**

Azure and other cloud services revenue grew **34%** in fiscal year 2025, driven by demand for Microsoft's portfolio of services.

- This growth is disclosed in the MD&A (Item 7) discussion of the Intelligent Cloud segment, where server products and cloud services revenue increased $18.6 billion or 23%, driven by Azure and other cloud services.
- The 10-K reports Azure growth only as a percentage (34%), not as a dollar amount; Azure and other cloud services revenue is a component of server products and cloud services revenue, which itself is not separately broken out in the filing's revenue tables.
- The filing defines the metric as revenue from Azure and other cloud services, including cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings, and other cloud services.
- Related context: Microsoft Cloud revenue (which includes Azure and other cloud services) was $168.9 billion in FY2025, up from $137.7 billion in FY2024.

Sources: [MSFT FY2025 10-K, p.38], [MSFT FY2025 10-K, p.34], [MSFT FY2025 10-K, p.36], [MSFT FY2025 10-K, p.80]

---

## x_018#0: PASS (llm_judge, level 1)

**Question:** What risks does Alphabet's fiscal year 2025 10-K describe about its dependence on advertising revenue?

**Gold:** Alphabet generated more than 70% of total revenues from online advertising in 2025. Risks: reduced advertiser spending, which tends to track economic conditions; advertisers and partners can terminate contracts at any time; AI is reshaping the advertising industry and Alphabet may not adapt to new ad formats effectively; changes to its own or other companies' advertising and data-privacy practices; and technologies that block ads or make personalized ads more difficult.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** none

*5 tool calls, 32.8s, $0.0511*

**Answer:**

Verified against the FY2025 financial tables: Google advertising revenues were $294.7 billion of Alphabet's $402.8 billion total revenues in 2025 — 73.2% of the total — consistent with the 10-K's statement that it generated "more than 70% of total revenues from online advertising in 2025." With that confirmed, here are the risks the FY2025 10-K (Item 1A, p.10) describes about Alphabet's dependence on advertising revenue:

- **Revenue concentration**: More than 70% of total revenues came from online advertising in 2025 ($294.7 billion of $402.8 billion, per the disaggregated revenue table), so the business is heavily exposed to anything that weakens that revenue stream.
- **Partner attrition**: Many advertisers, companies that distribute its products and services, digital publishers, and content providers can terminate their contracts at any time, and may not continue doing business with Alphabet if it does not create more value (more users or customers, new sales leads, increased brand awareness, or more effective monetization) than their available alternatives.
- **AI-driven shifts in advertising**: Alphabet believes AI is quickly reshaping the advertising industry, including how ads are delivered online, and there is no assurance it will adapt effectively and competitively to this shift or that its new and evolving advertising formats, strategies, and offerings will be successful.
- **Advertising policy and data privacy changes**: Changes to Alphabet's own advertising policies and data privacy practices — and to other companies' practices — have in the past, and may in the future, affect the advertising services it is able to provide.
- **Ad-blocking and anti-personalization technologies**: Technologies have been developed that make personalized ads more difficult or block the display of ads altogether, and some providers of online services have integrated technologies that could impair the availability and functionality of third-party digital advertising.
- **Macroeconomic cyclicality**: Advertiser expenditures tend to correlate with overall economic conditions; adverse macroeconomic conditions have affected, and may in the future affect, demand for advertising, causing fluctuations in advertiser spending that could harm financial condition and operating results.

Relatedly, the separate risk factor on revenue growth (p.12) lists "deceleration or declines in advertiser spending" among the factors that could cause Alphabet's revenue growth rate to decline over time.

Sources: [GOOGL FY2025 10-K, p.10], [GOOGL FY2025 10-K, p.12], [GOOGL FY2025 10-K, p.61], [SQL: segment_revenue], [SQL: income_statements]

---

## x_018#1: PASS (llm_judge, level 1)

**Question:** What risks does Alphabet's fiscal year 2025 10-K describe about its dependence on advertising revenue?

**Gold:** Alphabet generated more than 70% of total revenues from online advertising in 2025. Risks: reduced advertiser spending, which tends to track economic conditions; advertisers and partners can terminate contracts at any time; AI is reshaping the advertising industry and Alphabet may not adapt to new ad formats effectively; changes to its own or other companies' advertising and data-privacy practices; and technologies that block ads or make personalized ads more difficult.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** none

*4 tool calls, 29.4s, $0.0352*

**Answer:**

Verified: Alphabet's FY2025 10-K discloses that it generated **more than 70% of total revenues from online advertising in 2025**, and the financial tables confirm this — Google advertising revenues were $294.7 billion out of total revenues of $402.8 billion, or 73.2% of consolidated revenue (Google Search & other $224.5 billion, YouTube ads $40.4 billion, Google Network $29.8 billion).

The risks the FY2025 10-K (Item 1A, p.10) describes about this advertising dependence are:

- **Concentration of revenue:** more than 70% of 2025 total revenues came from online advertising, so the business is highly exposed to anything that reduces ad demand or effectiveness.
- **Partner/contract risk:** advertisers, companies that distribute its products, digital publishers, and content providers can terminate their contracts at any time, and may not continue doing business with Alphabet if it does not create more value (users, sales leads, brand awareness, more effective monetization) than their available alternatives.
- **AI-driven shifts in advertising:** Alphabet believes AI is quickly reshaping the advertising industry, including how ads are delivered online, and there is no assurance it will adapt effectively and competitively to new and evolving advertising formats, strategies, and offerings.
- **Advertising policy and data privacy changes:** changes to Alphabet's own advertising policies and data privacy practices — and to other companies' practices — have in the past, and may in the future, affect the advertising services it is able to provide.
- **Ad-blocking and personalization-impairing technologies:** technologies have been developed that make personalized ads more difficult or block ad display altogether, and some online service providers have integrated technologies that could impair the availability and functionality of third-party digital advertising.
- **Macroeconomic cyclicality:** advertiser expenditures tend to correlate with overall economic conditions; adverse macroeconomic conditions have affected, and may in the future affect, demand for advertising, causing fluctuations in advertiser spending.

A related risk factor (p.12) reinforces this dependence: among the factors that could cause Alphabet's revenue growth rate to decline over time, it lists "deceleration or declines in advertiser spending," along with changes in customer usage and demand, competition, and pricing decreases.

Sources: [GOOGL FY2025 10-K, p.10], [GOOGL FY2025 10-K, p.12], [GOOGL FY2025 10-K, p.35], [SQL: segment_revenue], [SQL: income_statements]

---

## x_018#2: PASS (llm_judge, level 1)

**Question:** What risks does Alphabet's fiscal year 2025 10-K describe about its dependence on advertising revenue?

**Gold:** Alphabet generated more than 70% of total revenues from online advertising in 2025. Risks: reduced advertiser spending, which tends to track economic conditions; advertisers and partners can terminate contracts at any time; AI is reshaping the advertising industry and Alphabet may not adapt to new ad formats effectively; changes to its own or other companies' advertising and data-privacy practices; and technologies that block ads or make personalized ads more difficult.

**Grade:** 6/6 facts covered

**Claims the tools did not back:** unsupported: Related risks elsewhere in Item 1A reinforce the advertising dependence.

*6 tool calls, 39.0s, $0.0539*

**Answer:**

Alphabet's FY2025 10-K (Item 1A, Risk Factors) devotes a dedicated risk factor to its advertising dependence, disclosing that more than 70% of total revenues came from online advertising in 2025 — a figure the financial tables confirm: Google advertising revenues were $294.7 billion of $402.8 billion total revenues in FY2025, or 73.2% (vs. 75.6% in FY2024). The specific risks disclosed (p.10) are:

- **Partner loss / no long-term commitments:** Many advertisers, companies that distribute Alphabet's products, digital publishers, and content providers can terminate their contracts at any time, and may not continue doing business with Alphabet if it does not create more value (users, sales leads, brand awareness, more effective monetization) than their available alternatives.
- **AI-driven shifts in advertising:** Alphabet believes AI is quickly reshaping the advertising industry, including how ads are delivered online, and there is no assurance it will adapt effectively and competitively to this shift or that new and evolving advertising formats, strategies, and offerings will be successful.
- **Privacy and policy changes:** Changes to Alphabet's own advertising policies and data privacy practices — and to other companies' practices — have in the past, and may in the future, affect the advertising services Alphabet is able to provide.
- **Ad-blocking and personalization-blocking technologies:** Technologies have been developed that make personalized ads more difficult or block the display of ads altogether, and some online service providers have integrated technologies that could impair the availability and functionality of third-party digital advertising.
- **Macroeconomic sensitivity:** Advertiser expenditures tend to correlate with overall economic conditions; adverse macroeconomic conditions have affected, and may in the future affect, demand for advertising, causing fluctuations in advertiser spending that could harm Alphabet's financial condition and operating results.

Related risks elsewhere in Item 1A reinforce this dependence: the revenue-growth risk factor lists "deceleration or declines in advertiser spending" among factors that could slow revenue growth (p.12), and the privacy/data-protection risk factor (GDPR, the EU Digital Markets Act, and similar regimes) warns that adverse rulings, legislation, or regulation could force changes in how Alphabet provides services — including DMA requirements that search engines share anonymized data with rival companies (pp.21–22).

Sources: [GOOGL FY2025 10-K, p.10], [GOOGL FY2025 10-K, p.12], [GOOGL FY2025 10-K, pp.21–22], [GOOGL FY2025 10-K, p.35], [SQL: segment_revenue], [SQL: income_statements]

---

## x_023#0: PASS (llm_judge, level 3)

**Question:** How did Microsoft's More Personal Computing revenue change in fiscal year 2025, and what does the 10-K attribute the change to?

**Gold:** More Personal Computing revenue increased from $50.8 billion to $54.6 billion, up about $3.8 billion or 7.5%. The FY2025 10-K attributes the increase to Gaming (Xbox content and services, helped by the Activision Blizzard acquisition and Xbox Game Pass) and Search and news advertising (up 13%), with Windows and Devices up 2%.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** none

*3 tool calls, 10.3s, $0.0094*

**Answer:**

Microsoft's More Personal Computing revenue rose $3.8 billion, or 7.5% (the 10-K rounds to 7%), from $50.8 billion in FY2024 to $54.6 billion in FY2025, and the 10-K attributes the increase primarily to Gaming and Search and news advertising.

- **Gaming: +$2.0 billion, +9%.** Xbox content and services revenue grew 16%, driven by the impact of the Activision Blizzard acquisition and Xbox Game Pass, partially offset by Xbox hardware revenue declining 25% on lower console volumes.
- **Search and news advertising: +$1.6 billion, +13%.** Excluding traffic acquisition costs, revenue grew 20%, driven by higher search volume and higher revenue per search.
- **Windows and Devices: +$288 million, +2%.** Windows OEM and Devices revenue grew 3%, driven by Windows OEM growth, offset in part by a decline in Devices.
- Segment operating income also rose $2.2 billion, or 18%, to $14.2 billion, with gross margin up $3.5 billion (13%) on improvement across all businesses.
- Note: these figures use the segment definitions as restated in the FY2025 10-K (following the August 2024 reorganization); the FY2024 10-K's segment figures under the old definitions differ.

Sources: [SQL: segment_revenue], [MSFT FY2025 10-K, p.37], [MSFT FY2025 10-K, p.38]

---

## x_023#1: PASS (llm_judge, level 3)

**Question:** How did Microsoft's More Personal Computing revenue change in fiscal year 2025, and what does the 10-K attribute the change to?

**Gold:** More Personal Computing revenue increased from $50.8 billion to $54.6 billion, up about $3.8 billion or 7.5%. The FY2025 10-K attributes the increase to Gaming (Xbox content and services, helped by the Activision Blizzard acquisition and Xbox Game Pass) and Search and news advertising (up 13%), with Windows and Devices up 2%.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** none

*3 tool calls, 11.5s, $0.0097*

**Answer:**

Microsoft's More Personal Computing revenue rose $3.8 billion, from $50.8 billion in FY2024 to $54.6 billion in FY2025 (a 7.5% increase, which the 10-K rounds to 7%), and the 10-K attributes the growth primarily to Gaming and Search and news advertising.

- **Gaming: +$2.0 billion (+9%)** — driven by Xbox content and services, which grew 16% on the impact of the Activision Blizzard acquisition and Xbox Game Pass, partially offset by Xbox hardware declining 25% on lower console volumes.
- **Search and news advertising: +$1.6 billion (+13%)** — revenue excluding traffic acquisition costs grew 20%, driven by higher search volume and higher revenue per search.
- **Windows and Devices: +$288 million (+2%)** — Windows OEM and Devices revenue grew 3% on Windows OEM growth, partially offset by a decline in Devices.
- Segment operating income also rose $2.2 billion (18%) to $14.2 billion, with gross margin up $3.5 billion (13%) on improvement across all businesses.
- Note: these figures use the segment definitions as restated in the FY2025 10-K (following the August 2024 reorganization); the FY2024 10-K reported the segment under the old definitions.

Sources: [SQL: segment_revenue], [MSFT FY2025 10-K, p.37], [MSFT FY2025 10-K, p.38]

---

## x_023#2: PASS (llm_judge, level 3)

**Question:** How did Microsoft's More Personal Computing revenue change in fiscal year 2025, and what does the 10-K attribute the change to?

**Gold:** More Personal Computing revenue increased from $50.8 billion to $54.6 billion, up about $3.8 billion or 7.5%. The FY2025 10-K attributes the increase to Gaming (Xbox content and services, helped by the Activision Blizzard acquisition and Xbox Game Pass) and Search and news advertising (up 13%), with Windows and Devices up 2%.

**Grade:** 9/9 facts covered

**Claims the tools did not back:** none

*3 tool calls, 15.5s, $0.0110*

**Answer:**

Microsoft's More Personal Computing revenue increased $3.8 billion, or 7.5%, in fiscal year 2025 — from $50.8 billion in FY2024 to $54.6 billion in FY2025 — and the 10-K attributes the increase primarily to Gaming and Search and news advertising.

- **Gaming** was the largest driver: revenue increased $2.0 billion, or 9%, driven by Xbox content and services (up 16% on the impact of the Activision Blizzard acquisition and Xbox Game Pass), offset in part by a 25% decline in Xbox hardware on lower console volumes.
- **Search and news advertising** revenue increased $1.6 billion, or 13%; excluding traffic acquisition costs it rose 20%, driven by higher search volume and higher revenue per search.
- **Windows and Devices** was roughly flat: revenue increased $288 million, or 2%, with Windows OEM and Devices up 3% on Windows OEM growth, offset in part by a decline in Devices.
- Segment operating income also rose $2.2 billion, or 18%, to $14.2 billion.
- Note: these figures use the segment definitions as restated in the FY2025 10-K (following the August 2024 reorganization); the FY2024 10-K reported segments under the old definitions, so its FY2024 comparatives differ.

Sources: [SQL: segment_revenue], [MSFT FY2025 10-K, p.37], [MSFT FY2025 10-K, p.38]

---

## x_024#0: PASS (llm_judge, level 3)

**Question:** Apple's revenue from Japan grew in fiscal year 2025. By how much, and what does the 10-K say drove it?

**Gold:** Japan revenue rose from $25.1 billion in FY2024 to $28.7 billion in FY2025, an increase of about $3.7 billion or 14.6%. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 8.1s, $0.0077*

**Answer:**

Apple's Japan net sales grew by $3.7 billion in FY2025 (from $25.1 billion to $28.7 billion), a 14.6% increase (shown as 15% in the 10-K), driven primarily by higher net sales of iPhone, Services and iPad.

- FY2024 Japan net sales: $25.1 billion; FY2025: $28.7 billion — an increase of $3.651 billion, or 14.6%.
- The FY2025 10-K (MD&A, Segment Operating Performance) states: "Japan net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and iPad."
- Japan was Apple's fastest-growing reportable segment in FY2025 (Americas +7%, Europe +10%, Greater China −4%, Rest of Asia Pacific +10%).
- Note: Apple's reportable segments are geographic; the Japan figures here are from the geographic segment disclosure.

Sources:
- [SQL: geographic_revenue]
- [AAPL FY2025 10-K, p.24]

---

## x_024#1: PASS (llm_judge, level 3)

**Question:** Apple's revenue from Japan grew in fiscal year 2025. By how much, and what does the 10-K say drove it?

**Gold:** Japan revenue rose from $25.1 billion in FY2024 to $28.7 billion in FY2025, an increase of about $3.7 billion or 14.6%. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 7.4s, $0.0080*

**Answer:**

Apple's Japan net sales grew by $3.7 billion (from $25.1 billion in FY2024 to $28.7 billion in FY2025), a 14.6% increase (shown as 15% in the 10-K), driven primarily by higher net sales of iPhone, Services and iPad.

- FY2024 Japan net sales: $25.1 billion (fiscal year ended September 28, 2024); FY2025: $28.7 billion (ended September 27, 2025) — a $3.7 billion increase.
- The FY2025 10-K (MD&A, Segment Operating Performance) states: "Japan net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and iPad."
- Note: Japan is one of Apple's reportable geographic segments (Apple's reportable segments are geographic, not product categories).

Sources:
- [SQL: geographic_revenue]
- [AAPL FY2025 10-K, p.24]

---

## x_024#2: PASS (llm_judge, level 3)

**Question:** Apple's revenue from Japan grew in fiscal year 2025. By how much, and what does the 10-K say drove it?

**Gold:** Japan revenue rose from $25.1 billion in FY2024 to $28.7 billion in FY2025, an increase of about $3.7 billion or 14.6%. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

**Grade:** 7/7 facts covered

**Claims the tools did not back:** none

*3 tool calls, 13.5s, $0.0080*

**Answer:**

Apple's Japan net sales grew by $3.7 billion in fiscal 2025 (from $25.1 billion to $28.7 billion), a 14.6% increase (shown as 15% in the 10-K), driven primarily by higher net sales of iPhone, Services and iPad.

- Japan net sales rose from $25,052 million in FY2024 to $28,703 million in FY2025, an increase of $3,651 million (+14.6%).
- The FY2025 10-K (MD&A, Segment Operating Performance) states: "Japan net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and iPad."
- Japan was Apple's fastest-growing reportable segment in FY2025 (15% vs. 10% for Europe and Rest of Asia Pacific, 7% for Americas, and a 4% decline in Greater China).
- Note: Apple's reportable segments are geographic; the figures above are from the Japan geographic segment.

Sources:
- [SQL: geographic_revenue]
- [AAPL FY2025 10-K, p.24]

---

## x_026#0: PASS (fuzzy_numeric, level 6)

**Question:** Which of Alphabet's business segments had the smallest revenue in fiscal year 2025, and how much was it?

**Gold:** Other Bets, with $1.5 billion.

**Grade:** answer's figure '$1.5 billion' matches 1537000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.5s, $0.0053*

**Answer:**

Alphabet's smallest reportable segment in FY2025 was **Other Bets**, with revenue of **$1.5 billion** ($1,537 million).

- The "Hedging gains (losses)" row (–$127 million) is a reconciling item, not a segment, so it is excluded from the ranking.
- For context, the other segments were far larger: Google Services at $342.7 billion and Google Cloud at $58.7 billion.

Sources: [SQL: segment_revenue]

---

## x_026#1: PASS (fuzzy_numeric, level 6)

**Question:** Which of Alphabet's business segments had the smallest revenue in fiscal year 2025, and how much was it?

**Gold:** Other Bets, with $1.5 billion.

**Grade:** answer's figure '$1.5 billion' matches 1537000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.5s, $0.0029*

**Answer:**

Alphabet's smallest business segment in FY2025 was **Other Bets**, with revenue of **$1.5 billion** ($1,537 million).

- Segment ranking for FY2025 (excluding the "Hedging gains (losses)" reconciling item, which is not a segment):
  - Google Services: $342.7 billion
  - Google Cloud: $58.7 billion
  - Other Bets: $1.5 billion
- The "Hedging gains (losses)" line of –$127 million is a reconciling item rather than a business segment, so it is excluded from the ranking.

Sources: [SQL: segment_revenue]

---

## x_026#2: PASS (fuzzy_numeric, level 6)

**Question:** Which of Alphabet's business segments had the smallest revenue in fiscal year 2025, and how much was it?

**Gold:** Other Bets, with $1.5 billion.

**Grade:** answer's figure '$1.5 billion' matches 1537000000 (usd)

**Claims the tools did not back:** none

*1 tool calls, 3.2s, $0.0025*

**Answer:**

Alphabet's smallest business segment in FY2025 was **Other Bets**, with revenue of **$1.5 billion** ($1,537 million).

- The "Hedging gains (losses)" row (–$127 million) is a reconciling item, not a business segment, so it is excluded from the ranking.
- The other segments were far larger: Google Services at $342.7 billion and Google Cloud at $58.7 billion.

Sources: [SQL: segment_revenue]

---

## x_031#0: PASS (out_of_scope, level 0)

**Question:** What was Apple's net income in fiscal year 2020?

**Gold:** Not available: the database covers FY2023-FY2025 and the filings are the FY2024 and FY2025 10-Ks.

**Grade:** The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related available data without fabricating a figure.

**Claims the tools did not back:** unsupported: Fiscal 2020 ended September 26, 2020

*2 tool calls, 11.2s, $0.0096*

**Answer:**

Apple's fiscal year 2020 net income is not available in my sources, so I can't provide that figure.

- The financial database only contains Apple income statement data for fiscal years 2023–2025 (net income of $97.0 billion, $93.7 billion, and $112.0 billion, respectively).
- The filings I have access to are Apple's FY2024 and FY2025 Form 10-Ks. Their income statements cover at most three years each: the FY2024 10-K shows FY2022–FY2024, and the FY2025 10-K shows FY2023–FY2025. Neither reaches back to fiscal 2020 (the year ended September 26, 2020).
- The earliest figure available is FY2022 net income of $99.8 billion, per the FY2024 10-K's consolidated statements of operations.

Sources: [SQL: income_statements], [AAPL FY2024 10-K, p.31], [AAPL FY2025 10-K, p.30]

---

## x_031#1: PASS (out_of_scope, level 0)

**Question:** What was Apple's net income in fiscal year 2020?

**Gold:** Not available: the database covers FY2023-FY2025 and the filings are the FY2024 and FY2025 10-Ks.

**Grade:** The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related, sourced figures without fabricating the requested number.

**Claims the tools did not back:** unsupported: Apple's fiscal year 2020 ended September 26, 2020.

*2 tool calls, 9.1s, $0.0084*

**Answer:**

Apple's fiscal year 2020 net income is not available in my sources, so I can't provide that figure.

- The financial database contains Apple's income statements only for fiscal years 2023–2025 (net income of $97.0 billion, $93.7 billion, and $112.0 billion, respectively).
- The filings I have access to are Apple's FY2024 and FY2025 Form 10-Ks, whose income statements cover fiscal years 2022–2025 at the earliest — the FY2024 10-K's earliest comparative year is FY2022 (net income $99.8 billion), and the FY2025 10-K's earliest is FY2023.
- Neither source reaches back to fiscal 2020 (the year ended September 26, 2020), so I can't state that number from these materials.

Sources: [SQL: income_statements]; [AAPL FY2024 10-K, p.31]; [AAPL FY2025 10-K, p.30]

---

## x_031#2: PASS (out_of_scope, level 0)

**Question:** What was Apple's net income in fiscal year 2020?

**Gold:** Not available: the database covers FY2023-FY2025 and the filings are the FY2024 and FY2025 10-Ks.

**Grade:** The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related, correctly-scoped data without fabricating a figure.

**Claims the tools did not back:** contradicted: The only FY2020-related data in the filings is the stock performance graph.

*2 tool calls, 9.9s, $0.0079*

**Answer:**

Apple's fiscal year 2020 net income is not available in my sources, so I can't give you that figure.

- The financials database only contains Apple income statement data for fiscal years 2023–2025 (net income of $97.0 billion, $93.7 billion, and $112.0 billion, respectively).
- The FY2024 10-K's consolidated statements of operations go back only to fiscal 2022 (net income of $99.8 billion), and the FY2025 10-K goes back only to fiscal 2023 — neither filing's income statement includes fiscal 2020.
- The only FY2020-related data in the filings is the stock performance graph (Apple's cumulative return of $207 per $100 invested as of September 2020), which does not include net income.

Sources: [SQL: income_statements], [AAPL FY2024 10-K, p.30], [AAPL FY2025 10-K, p.30]

---

## x_044#0: PASS (llm_judge, level 5)

**Question:** How much did the company with the lowest current ratio in fiscal year 2025 spend on share repurchases that year?

**Gold:** Apple had the lowest current ratio (about 0.89). It spent $90.7 billion on repurchases of common stock in FY2025 according to its cash flow statement (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable).

**Grade:** 2/2 facts covered

**Claims the tools did not back:** unsupported: The difference between the $90.1B and $89.3B figures is due to settlement timing.

*2 tool calls, 12.0s, $0.0144*

**Answer:**

Apple — the company with the lowest FY2025 current ratio — spent **$89.3 billion** on share repurchases in fiscal 2025.

- **Current ratio ranking (FY2025):** Apple 0.89 ($148.0B current assets ÷ $165.6B current liabilities), Microsoft 1.35, Alphabet 2.01 — so Apple is the lowest.
- **Repurchase amount:** Apple's FY2025 10-K states it repurchased 402 million shares of common stock for $89.3 billion during 2025 (MD&A and the Share Repurchase Program note both cite this figure).
- **Program context:** Apple completed the final $19.8 billion of its May 2024 $110 billion program in Q4 FY2025, and announced a new $100 billion program on May 1, 2025, of which only $221 million had been utilized by fiscal year-end (September 27, 2025).
- Note: the statement of shareholders' equity shows $90.1 billion charged to accumulated deficit for common stock repurchased, a slightly higher figure than the $89.3 billion repurchase spend due to settlement timing; the $89.3 billion is the amount the filing reports as repurchased during the year.

Sources:
- [SQL: balance_sheets]
- [AAPL FY2025 10-K, p.27]
- [AAPL FY2025 10-K, p.45]
- [AAPL FY2025 10-K, p.21]

---

## x_044#1: PASS (llm_judge, level 5)

**Question:** How much did the company with the lowest current ratio in fiscal year 2025 spend on share repurchases that year?

**Gold:** Apple had the lowest current ratio (about 0.89). It spent $90.7 billion on repurchases of common stock in FY2025 according to its cash flow statement (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable).

**Grade:** 2/2 facts covered

**Claims the tools did not back:** unsupported: The difference is due to accounting presentation.

*2 tool calls, 11.1s, $0.0089*

**Answer:**

Apple — the company with the lowest FY2025 current ratio (0.89) — spent **$89.3 billion** on share repurchases in fiscal 2025.

- **Current ratios (FY2025):** Apple 0.89 ($148.0B current assets / $165.6B current liabilities), Microsoft 1.35, Alphabet 2.01 — Apple is the only one below 1.0.
- **Repurchase amount:** Apple's FY2025 10-K states it repurchased 402 million shares of common stock for $89.3 billion during 2025 (MD&A and the Share Repurchase Program note both cite this figure).
- **Program context:** Apple completed the final $19.8 billion of its May 2024 $110 billion program in Q4 FY2025 and announced a new $100 billion program on May 1, 2025, of which only $221 million had been utilized by fiscal year-end (September 27, 2025).
- Note: the shareholders' equity statement shows $90.1 billion charged to accumulated deficit for common stock repurchased, a slightly higher figure than the $89.3 billion repurchase-program spend due to accounting presentation; the repurchase amount itself is $89.3 billion.

Sources: [SQL: balance_sheets]; [AAPL FY2025 10-K, p.27]; [AAPL FY2025 10-K, p.45]; [AAPL FY2025 10-K, p.21]

---

## x_044#2: PASS (llm_judge, level 5)

**Question:** How much did the company with the lowest current ratio in fiscal year 2025 spend on share repurchases that year?

**Gold:** Apple had the lowest current ratio (about 0.89). It spent $90.7 billion on repurchases of common stock in FY2025 according to its cash flow statement (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable).

**Grade:** 2/2 facts covered

**Claims the tools did not back:** none

*2 tool calls, 9.4s, $0.0074*

**Answer:**

Apple, the company with the lowest FY2025 current ratio (0.89), spent **$89.3 billion** on share repurchases in fiscal 2025.

- **Current ratios (FY2025):** Apple 0.89 ($148.0B current assets ÷ $165.6B current liabilities), Microsoft 1.35, Alphabet 2.01 — Apple's is the lowest, the only one below 1.0.
- **Repurchases:** Apple's FY2025 10-K states it repurchased 402 million shares of common stock for $89.3 billion during 2025, under its May 2024 program (up to $110 billion, fully utilized in Q4 2025) and a new May 2025 program of up to $100 billion.
- For context, Apple also paid $15.4 billion in dividends and dividend equivalents that year.

Sources: [SQL: balance_sheets]; [AAPL FY2025 10-K, p.27]; [AAPL FY2025 10-K, p.45]

---

## x_046#0: PASS (llm_judge, level 6)

**Question:** Apple's fiscal year 2025 10-K reports that Greater China net sales decreased 4%. Do the figures in the database agree?

**Gold:** Yes. The database shows Greater China revenue of $66.95 billion in FY2024 and $64.38 billion in FY2025, a decline of about 3.8%, which rounds to the 10-K's 4%; the dollar figures match the 10-K's segment table ($66,952 million and $64,377 million).

**Grade:** 3/3 facts covered

**Claims the tools did not back:** none

*3 tool calls, 8.9s, $0.0096*

**Answer:**

Yes — the database agrees with the 10-K. Greater China net sales fell from $66,952 million in FY2024 to $64,377 million in FY2025, a decline of $2,575 million, or 3.8%, which rounds to the 4% decrease Apple reports.

- The database's Greater China figures ($66,952 million for FY2024 and $64,377 million for FY2025) exactly match the segment net sales table in the FY2025 10-K's MD&A (p.24) and Note 13 (p.48).
- The filing attributes the decrease primarily to lower iPhone net sales, partially offset by higher Mac net sales.
- For context, this was the second consecutive annual decline: Greater China net sales had already fallen 8% in FY2024 from $72,559 million in FY2023.

Sources: [SQL: geographic_revenue]; [AAPL FY2025 10-K, p.24]; [AAPL FY2025 10-K, p.48]

---

## x_046#1: PASS (llm_judge, level 6)

**Question:** Apple's fiscal year 2025 10-K reports that Greater China net sales decreased 4%. Do the figures in the database agree?

**Gold:** Yes. The database shows Greater China revenue of $66.95 billion in FY2024 and $64.38 billion in FY2025, a decline of about 3.8%, which rounds to the 10-K's 4%; the dollar figures match the 10-K's segment table ($66,952 million and $64,377 million).

**Grade:** 3/3 facts covered

**Claims the tools did not back:** none

*3 tool calls, 11.7s, $0.0105*

**Answer:**

Yes — the database agrees with the 10-K. Greater China net sales fell from $66,952 million in FY2024 to $64,377 million in FY2025, a decline of $2,575 million or 3.8%, which the 10-K rounds to a 4% decrease.

- The FY2025 10-K's MD&A segment table (p.24) shows Greater China net sales of $64,377 million in 2025 vs. $66,952 million in 2024, marked "(4)%" — identical to the database's geographic_revenue figures for both years.
- The exact change is −3.8% (−$2.58 billion), which Apple rounds to 4% in the filing.
- The 10-K explains the decrease was "primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac."
- Note: Apple's reportable segments are geographic; Greater China is one of five (Americas, Europe, Greater China, Japan, Rest of Asia Pacific), and it was the only one to decline in FY2025.

Sources: [SQL: geographic_revenue], [AAPL FY2025 10-K, p.24]

---

## x_046#2: PASS (llm_judge, level 6)

**Question:** Apple's fiscal year 2025 10-K reports that Greater China net sales decreased 4%. Do the figures in the database agree?

**Gold:** Yes. The database shows Greater China revenue of $66.95 billion in FY2024 and $64.38 billion in FY2025, a decline of about 3.8%, which rounds to the 10-K's 4%; the dollar figures match the 10-K's segment table ($66,952 million and $64,377 million).

**Grade:** 3/3 facts covered

**Claims the tools did not back:** none

*3 tool calls, 12.7s, $0.0111*

**Answer:**

Yes — the database agrees exactly with the 10-K. Greater China net sales fell from $66,952 million in FY2024 to $64,377 million in FY2025, a decline of 3.8%, which the 10-K's MD&A table reports as "(4)%."

- The FY2025 10-K's segment table (Item 7, p.24) shows Greater China net sales of $64,377 million in 2025 vs. $66,952 million in 2024, a (4)% change — identical to the database's geographic_revenue figures for the periods ended 2025-09-27 and 2024-09-28.
- The precise change is −$2,575 million, or −3.8% (the filing rounds to the nearest whole percent).
- Note 13 (Item 8, p.48) confirms the same figures, with China net sales of $64,377 million (2025) and $66,952 million (2024).
- The filing attributes the decrease primarily to lower net sales of iPhone, partially offset by higher net sales of Mac.

Sources: [SQL: geographic_revenue], [AAPL FY2025 10-K, p.24], [AAPL FY2025 10-K, p.48]

---

## x_050#0: PASS (llm_judge, level 7)

**Question:** How much of that came from the United States, and how did that share change from the year before?

*Follow-up to:* What was Microsoft's total revenue in fiscal year 2025?

**Gold:** $144.5 billion, or about 51.3% of FY2025 revenue, came from the United States, up from about 50.9% ($124.7 billion of $245.1 billion) in FY2024, an increase of about 0.4 percentage points.

**Grade:** 4/4 facts covered

**Claims the tools did not back:** none

*4 tool calls, 10.8s, $0.0112*

**Answer:**

Microsoft's U.S. revenue in FY2025 was $144.5 billion, or 51.3% of total revenue — up from 50.9% in FY2024, an increase of about 0.4 percentage points.

- FY2025: U.S. revenue $144.5 billion out of $281.7 billion total (51.3%); "Other countries" contributed the remaining $137.2 billion.
- FY2024: U.S. revenue $124.7 billion out of $245.1 billion total (50.9%).
- U.S. revenue grew 15.9% year over year, slightly outpacing total revenue growth of 14.9%, which nudged the U.S. share up.

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

## x_050#1: PASS (llm_judge, level 7)

**Question:** How much of that came from the United States, and how did that share change from the year before?

*Follow-up to:* What was Microsoft's total revenue in fiscal year 2025?

**Gold:** $144.5 billion, or about 51.3% of FY2025 revenue, came from the United States, up from about 50.9% ($124.7 billion of $245.1 billion) in FY2024, an increase of about 0.4 percentage points.

**Grade:** 4/4 facts covered

**Claims the tools did not back:** none

*2 tool calls, 6.9s, $0.0079*

**Answer:**

Microsoft's U.S. revenue in FY2025 was $144.5 billion, or 51.3% of total revenue — up from 50.9% in FY2024, an increase of about 0.4 percentage points.

- FY2025: U.S. revenue $144.5 billion out of $281.7 billion total (51.3%)
- FY2024: U.S. revenue $124.7 billion out of $245.1 billion total (50.9%)
- U.S. revenue grew faster than total revenue, so the U.S. share of revenue rose slightly year over year.

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

## x_050#2: PASS (llm_judge, level 7)

**Question:** How much of that came from the United States, and how did that share change from the year before?

*Follow-up to:* What was Microsoft's total revenue in fiscal year 2025?

**Gold:** $144.5 billion, or about 51.3% of FY2025 revenue, came from the United States, up from about 50.9% ($124.7 billion of $245.1 billion) in FY2024, an increase of about 0.4 percentage points.

**Grade:** 4/4 facts covered

**Claims the tools did not back:** none

*3 tool calls, 9.2s, $0.0073*

**Answer:**

Microsoft's U.S. revenue in FY2025 was $144.5 billion, or 51.3% of total revenue — up about 0.4 percentage points from 50.9% in FY2024.

- FY2025: U.S. revenue $144.5 billion out of $281.7 billion total (51.3%)
- FY2024: U.S. revenue $124.7 billion out of $245.1 billion total (50.9%)
- The share rose because U.S. revenue grew 15.9% year over year, slightly faster than total revenue growth of 14.9%

Sources: [SQL: geographic_revenue], [SQL: income_statements]

---

