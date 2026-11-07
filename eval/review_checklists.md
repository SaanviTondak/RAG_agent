# Review: 15 unreviewed judge checklists

These checklists decide pass/fail for 15 questions (3 of them holdout: x_044, x_046, x_050). About 20 minutes. For each one, check:
1. Is every fact true? The most relevant sentences from the gold pages are below. Already verified mechanically
   (2026-11-06): every number in these checklists is either found on a gold page (automatic match) or matches a SQL query on the
   database (the 15 that are database figures or calculations: x_035, x_039, x_041, x_045, x_050). So the
   numbers are right; your job is mainly the judgment calls in 2 and 3.
2. Is every fact really needed to answer the question, and is anything important missing?
3. Is anything split so finely that one slip fails two facts?

Mark each `OK` or write the change next to it. I'll apply the edits and set `reviewed: true`.

## x_035 (tune, level 3, llm_judge)

**Q:** Apple's net income fell in fiscal year 2024 even though revenue grew. By how much did it fall, and what does the 10-K say caused it?

**Gold answer:** Net income fell from $97.0 billion in FY2023 to $93.7 billion in FY2024, a decrease of about $3.3 billion (3.4%), while revenue grew about 2.0%. The FY2024 10-K attributes the higher tax expense to a one-time income tax charge of $10.2 billion, net, related to the European Commission's State Aid Decision, which raised the effective tax rate to 24.1% from 14.7%.

**Checklist:**

1. Apple's net income was $97.0 billion in FY2023  — OK / change:
2. Apple's net income was $93.7 billion in FY2024  — OK / change:
3. Net income decreased by about $3.3 billion (about 3.4%)  — OK / change:
4. Revenue grew (about 2.0%) in FY2024  — OK / change:
5. The FY2024 10-K cites a one-time income tax charge of $10.2 billion, net  — OK / change:
6. The charge related to the European Commission's State Aid Decision  — OK / change:
7. The effective tax rate rose to 24.1% from 14.7%  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2024 10-K, p.27*
  - The Company’s effective tax rate for 2024 was higher than the statutory federal income tax rate due primarily to a one-time income tax charge of $10.2 billion, net, related to the State Aid Decision (refer to Note 7, “Income Taxes” in the Notes to Consolidated Financial Statements in Part II, Item 8 of this Form 10-K) and state income taxes, partially offset by a lower effective tax rate on foreign earnings, the impact of the U.S.
  - The Company’s effective tax rate for 2024 was higher compared to 2023 due primarily to a one-time income tax charge of $10.2 billion, net, related to the State Aid Decision, a higher effective tax rate on foreign earnings and lower tax benefits from sharebased compensation.
  - Provision for income taxes, effective tax rate and statutory federal income tax rate for 2024, 2023 and 2022 were as follows (dollars in millions):
  - |Effective tax rate|24.1%|14.7%|16.2 %|
- *AAPL FY2024 10-K, p.42*
  - As a result, during the fourth quarter of 2024 the Company recorded a one-time income tax charge of $10.2 billion, net, which represents $15.8 billion payable to Ireland via release of the escrow, partially offset by a U.S.
  - The Company and Ireland appealed the State Aid Decision to the General Court of the Court of Justice of the European Union (the “General Court”).
  - On September 25, 2020, the Commission appealed the General Court’s decision to the European Court of Justice (the “ECJ”) and a hearing was held on May 23, 2023.
  - On September 10, 2024, the ECJ announced that it had set aside the 2020 judgment of the General Court and confirmed the Commission’s 2016 State Aid Decision.

## x_036 (tune, level 4, llm_judge)

**Q:** Microsoft and Alphabet both grew operating income in fiscal year 2025. By how much did each grow, and what does each company's 10-K say drove it?

**Gold answer:** Microsoft's operating income rose $19.1 billion (about 17.4%), from $109.4 billion to $128.5 billion; its 10-K says the growth came from all of its segments. Alphabet's rose $16.6 billion (about 14.8%), from $112.4 billion to $129.0 billion; its 10-K attributes the segment gains mainly to higher revenues: Google Services operating income rose $18.1 billion and Google Cloud $7.8 billion, partly offset by a $3.1 billion larger Other Bets loss and higher Alphabet-level AI research costs.

**Checklist:**

1. Microsoft's operating income rose by $19.1 billion (about 17%)  — OK / change:
2. Microsoft's operating income was $109.4 billion in FY2024 and $128.5 billion in FY2025  — OK / change:
3. Microsoft's 10-K says the growth came from all (each) of its segments  — OK / change:
4. Alphabet's operating income rose by $16.6 billion (about 14.8%)  — OK / change:
5. Alphabet's operating income was $112.4 billion in FY2024 and $129.0 billion in FY2025  — OK / change:
6. Alphabet's 10-K attributes the segment operating income gains mainly to higher revenues  — OK / change:
7. Google Services operating income rose $18.1 billion  — OK / change:
8. Google Cloud operating income rose $7.8 billion  — OK / change:
9. A larger Other Bets loss (about $3.1 billion more) or higher Alphabet-level costs partly offset the gains  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *MSFT FY2025 10-K, p.37*
  - Operating income increased $19.1 billion or 17% with growth across each of our segments.
  - - Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure.
  - Revenue increased $36.6 billion or 15% with growth across each of our segments.
  - Cost of revenue increased $13.7 billion or 19% driven by growth in Microsoft Cloud.
- *GOOGL FY2025 10-K, p.38*
  - We report our segment results as Google Services, Google Cloud, and Other Bets.
  - The following table presents segment operating income (loss) (in millions).
  - > (1) Alphabet-level activities primarily reflect expenses related to our shared AI research and development.
  - |Research and development expenses as a percentage of revenues|14%|15 %|
- *GOOGL FY2025 10-K, p.39*
  - Google Services operating income increased $18.1 billion from 2024 to 2025.
  - The increase in operating income was primarily driven by an increase in revenues, partially offset by an increase in expenses related to legal and other matters, TAC, and content acquisition costs.
  - Google Cloud operating income increased $7.8 billion from 2024 to 2025.
  - Other Bets operating loss increased $3.1 billion from 2024 to 2025.

## x_037 (tune, level 3, llm_judge)

**Q:** How does Microsoft's fiscal year 2025 10-K define Microsoft Cloud revenue, and how much was it in each of the last three fiscal years?

**Gold answer:** Microsoft Cloud revenue includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365. It was $168.9 billion in FY2025, $137.7 billion in FY2024 and $111.6 billion in FY2023.

**Checklist:**

1. Microsoft Cloud revenue includes Microsoft 365 Commercial cloud  — OK / change:
2. Microsoft Cloud revenue includes Azure and other cloud services  — OK / change:
3. Microsoft Cloud revenue includes the commercial portion of LinkedIn  — OK / change:
4. Microsoft Cloud revenue includes Dynamics 365  — OK / change:
5. Microsoft Cloud revenue was $168.9 billion in FY2025  — OK / change:
6. Microsoft Cloud revenue was $137.7 billion in FY2024  — OK / change:
7. Microsoft Cloud revenue was $111.6 billion in FY2023  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *MSFT FY2025 10-K, p.80*
  - Our Microsoft Cloud revenue, which includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365, was $168.9 billion, $137.7 billion, and $111.6 billion in fiscal years 2025, 2024, and 2023, respectively.
  - These amounts are included in Microsoft 365 Commercial products and cloud services, Server products and cloud services, LinkedIn, and Dynamics products and cloud services in the table above.
  - |Microsoft 365 Commercial products and cloud services| **87,767**|76,969| 66,949|
  - |Microsoft 365 Consumer products and cloud services| **7,404 **| 6,648| 6,417|
- *MSFT FY2025 10-K, p.33*
  - - Microsoft 365 Commercial products and cloud services revenue increased 14% driven by Microsoft 365 Commercial cloud revenue growth of 15%.
  - We generate revenue by offering a wide range of cloud-based solutions, content, and other services to people and businesses; licensing and supporting an array of software products; delivering relevant online advertising to a global audience; and designing and selling devices.
  - - Microsoft Cloud revenue increased 23% to $168.9 billion.
  - Our most significant expenses are related to compensating employees; supporting and investing in our cloud-based services, including datacenter operations; designing, manufacturing, marketing, and selling our other products and services; and income taxes.

## x_038 (tune, level 4, llm_judge)

**Q:** How much did Apple and Alphabet each spend on share repurchases in fiscal year 2025, and which spent more?

**Gold answer:** Apple spent more. Apple's cash flow statement shows $90.7 billion of repurchases of common stock in FY2025 (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable). Alphabet repurchased 240 million shares for $45.4 billion.

**Checklist:**

1. Apple spent more on share repurchases than Alphabet in FY2025  — OK / change:
2. Apple's FY2025 repurchases were about $90.7 billion (cash flow statement) or $89.3 billion (Note 10); either figure counts  — OK / change:
3. Alphabet's FY2025 repurchases were $45.4 billion  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2025 10-K, p.34*
  - |Repurchases of common stock|(90,711)|(94,949)|(77,550)|
  - |Supplemental cash flow disclosure:||||
  - |Cash, cash equivalents, and restricted cash and cash equivalents, beginning balances|$ 29,943|$ 30,737|$ 24,977|
  - |Adjustments to reconcile net income to cash generated by operating activities:||||
- *AAPL FY2025 10-K, p.45*
  - During 2025, the Company repurchased 402 million shares of its common stock for $89.3 billion.
  - The following table shows the changes in shares of common stock for 2025, 2024 and 2023 (in thousands):
  - |Common stock repurchased|(401,672)|(499,372)|(471,419)|
  - |Common stock issued, net of shares withheld for employee taxes|58,146|66,097|78,055|
- *GOOGL FY2025 10-K, p.42*
  - During 2025, we repurchased and subsequently retired 240 million shares for $45.4 billion.
  - During the year ended December 31, 2025, total cash dividends were $4.8 billion for Class A, $703 million for Class B, and $4.5 billion for Class C shares, respectively.
  - - **November 2025** : We issued $500 million of US dollar-denominated floating-rate senior unsecured notes and $17.0 billion of US dollar-denominated fixed-rate senior unsecured notes with a weighted-average coupon rate of 4.92% and a weighted-average maturity of approximately 20 years.
  - As of December 31, 2025, we had senior unsecured notes outstanding with a total carrying value of $48.5 billion, of which $2.0 billion was short-term.
- *GOOGL FY2025 10-K, p.80*
  - During the year ended December 31, 2025, total cash dividends were $4.8 billion for Class A, $703 million for Class B, and $4.5 billion for Class C shares, respectively.
  - Shares of Class B common stock may be converted at any time at the option of the stockholder and automatically convert upon sale or transfer to Class A common stock.
  - Our Board of Directors has authorized three classes of stock, Class A and Class B common stock, and Class C capital stock.
  - The rights of the holders of each class of our common and capital stock are identical, except with respect to voting.

## x_039 (tune, level 2, llm_judge)

**Q:** What share of Alphabet's revenue came from Google Cloud in fiscal year 2025, and how did that share change from fiscal year 2024?

**Gold answer:** Google Cloud was about 14.6% of Alphabet's FY2025 revenue ($58.7 billion of $402.8 billion), up from about 12.4% in FY2024 ($43.2 billion of $350.0 billion), an increase of about 2.2 percentage points.

**Checklist:**

1. Google Cloud was about 14.6% of Alphabet's FY2025 revenue  — OK / change:
2. Google Cloud revenue was $58.7 billion in FY2025  — OK / change:
3. Google Cloud was about 12.4% (12.3-12.4%) of Alphabet's FY2024 revenue  — OK / change:
4. The share increased by about 2.2 percentage points  — OK / change:

**Source sentences (gold pages, most relevant first):**


## x_041 (tune, level 5, llm_judge)

**Q:** Which company grew its operating income the fastest from fiscal year 2024 to fiscal year 2025, and what does that company's 10-K say drove the growth?

**Gold answer:** Microsoft, with operating income up about 17.4% (from $109.4 billion to $128.5 billion), ahead of Alphabet (about 14.8%) and Apple (about 8.0%). Its FY2025 10-K says operating income increased $19.1 billion or 17% with growth across each of its segments; gross margin increased $22.9 billion or 13%, also with growth across each segment.

**Checklist:**

1. Microsoft had the fastest operating income growth  — OK / change:
2. Microsoft's operating income grew about 17.4% (17%), from $109.4 billion to $128.5 billion  — OK / change:
3. Alphabet's operating income grew about 14.8% and Apple's about 8.0%  — OK / change:
4. The 10-K says the growth came from (growth across) each of Microsoft's segments  — OK / change:
5. Gross margin increased $22.9 billion (about 13%)  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *MSFT FY2025 10-K, p.37*
  - Gross margin increased $22.9 billion or 13% with growth across each of our segments.
  - Operating income increased $19.1 billion or 17% with growth across each of our segments.
  - Revenue increased $36.6 billion or 15% with growth across each of our segments.
  - Cost of revenue increased $13.7 billion or 19% driven by growth in Microsoft Cloud.

## x_042 (tune, level 5, llm_judge)

**Q:** Which company spent the largest share of its revenue on research and development in fiscal year 2025, and what does its 10-K say about its investment in AI infrastructure?

**Gold answer:** Alphabet, at about 15.2% of revenue ($61.1 billion of $402.8 billion; Microsoft about 11.5%, Apple about 8.3%). Its FY2025 10-K says it continues to invest in capital expenditures to scale its technical infrastructure, in particular for AI; it invested heavily in 2025 ($91.4 billion of capital expenditures) and expects to significantly increase that investment in 2026 (servers, network equipment and data centers). It expects the costs of operating that infrastructure (depreciation, energy, equipment, network capacity) to increase significantly because AI requires more compute than its historical offerings.

**Checklist:**

1. Alphabet spent the largest share of revenue on R&D  — OK / change:
2. Alphabet's R&D was about 15.2% of revenue  — OK / change:
3. Microsoft's R&D share was about 11.5% and Apple's about 8.3%  — OK / change:
4. The 10-K says Alphabet continues to invest in technical infrastructure, in particular for AI  — OK / change:
5. The 10-K says Alphabet invested heavily in capital expenditures in 2025 (about $91.4 billion)  — OK / change:
6. Alphabet expects to significantly increase its technical infrastructure investment in 2026  — OK / change:
7. The costs of operating the infrastructure (depreciation, energy, equipment, network capacity) are expected to increase significantly because AI needs more compute  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *GOOGL FY2025 10-K, p.30*
  - The costs associated with operating our technical infrastructure - depreciation, energy, equipment, and network capacity - are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings.
  - We invested heavily in capital expenditures in 2025 and in 2026, we expect to significantly increase  , relative to 2025, our in  vestment in our technical infrastructure, including servers and network equipment, and data centers.
  - **_Increased Investment in Technical Infrastructure:_** We continue to invest in capital expenditures as we scale our technical infrastructure, in particular for AI, to meet the demand of our users and enterprise customers and to support research internally.
  - While our technical infrastructure costs increase, we expect to continue to drive efficiencies in our data centers, for example, through the design of our AI models and our TPU and GPU-based technical infrastructure.
- *GOOGL FY2025 10-K, p.35*
  - tax law enacted on July 4, 2025, allow, among other things, for immediate expensing of domestic research and experimentation costs and accelerated depreciation on eligible capital expenditures, the effects of which are included in operating cash flows for the year ended December 31, 2025.
  - - Capital expenditures, which primarily reflected investments in technical infrastructure, were $91.4 billion for the year ended December 31, 2025.
  - - In 2025, we entered into definitive agreements to acquire Wiz, a leading cloud security platform, for $32.0 billion, and Intersect, a provider of data center and energy infrastructure solutions, for $4.8 billion in cash plus the assumption of debt.
  - - Cost of revenues was $162.5 billion, an increase of 11% y  ear over year, primarily driven by increases in TAC, content acquisition costs, and depreciation expense.

## x_043 (tune, level 5, llm_judge)

**Q:** Which of Apple's geographic segments performed worst in fiscal year 2025, and what reason does the 10-K give?

**Gold answer:** Greater China, the only region to decline: net sales fell about 3.8%, from $66.95 billion to $64.38 billion, while the Americas (+6.8%), Europe (+9.6%), Japan (+14.6%) and Rest of Asia Pacific (+9.9%) grew. The FY2025 10-K says the decrease was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

**Checklist:**

1. Greater China performed worst (the only region to decline)  — OK / change:
2. Greater China net sales fell about 3.8%, from $66.95 billion to $64.38 billion  — OK / change:
3. Apple's other regions grew in FY2025  — OK / change:
4. The 10-K says the decrease was primarily due to lower net sales of iPhone  — OK / change:
5. The decrease was partially offset by higher net sales of Mac  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2025 10-K, p.24*
  - Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.
  - Rest of Asia Pacific net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and Mac.
  - Europe net sales increased during 2025 compared to 2024 primarily due to higher net sales of Services, iPhone and Mac.
  - Americas net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone and Services.

## x_044 (holdout, level 5, llm_judge)

**Q:** How much did the company with the lowest current ratio in fiscal year 2025 spend on share repurchases that year?

**Gold answer:** Apple had the lowest current ratio (about 0.89). It spent $90.7 billion on repurchases of common stock in FY2025 according to its cash flow statement (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable).

**Checklist:**

1. Apple had the lowest current ratio in FY2025 (about 0.89)  — OK / change:
2. Apple's FY2025 share repurchases were about $90.7 billion (cash flow statement) or $89.3 billion (Note 10); either figure counts  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2025 10-K, p.34*
  - |Repurchases of common stock|(90,711)|(94,949)|(77,550)|
  - |Supplemental cash flow disclosure:||||
  - |Cash, cash equivalents, and restricted cash and cash equivalents, beginning balances|$ 29,943|$ 30,737|$ 24,977|
  - |Adjustments to reconcile net income to cash generated by operating activities:||||
- *AAPL FY2025 10-K, p.45*
  - During 2025, the Company repurchased 402 million shares of its common stock for $89.3 billion.
  - The following table shows the changes in shares of common stock for 2025, 2024 and 2023 (in thousands):
  - |Common stock repurchased|(401,672)|(499,372)|(471,419)|
  - |Common stock issued, net of shares withheld for employee taxes|58,146|66,097|78,055|

## x_045 (tune, level 6, llm_judge)

**Q:** Do Alphabet's segment revenues in the database add up to its total revenue for fiscal year 2025? Explain any difference.

**Gold answer:** Not exactly. Google Services ($342.7 billion), Google Cloud ($58.7 billion) and Other Bets ($1.5 billion) sum to about $403.0 billion, about $127 million more than total revenue of $402.8 billion. The difference is a $127 million hedging loss, a reconciling item rather than a segment; segments plus hedging equal consolidated revenue.

**Checklist:**

1. The segment revenues do not add up exactly to total revenue  — OK / change:
2. Google Services, Google Cloud and Other Bets sum to about $403.0 billion  — OK / change:
3. Alphabet's total revenue was $402.8 billion  — OK / change:
4. The difference is about $127 million  — OK / change:
5. The difference is hedging gains (losses), a reconciling item that is not a segment  — OK / change:

**Source sentences (gold pages, most relevant first):**


## x_046 (holdout, level 6, llm_judge)

**Q:** Apple's fiscal year 2025 10-K reports that Greater China net sales decreased 4%. Do the figures in the database agree?

**Gold answer:** Yes. The database shows Greater China revenue of $66.95 billion in FY2024 and $64.38 billion in FY2025, a decline of about 3.8%, which rounds to the 10-K's 4%; the dollar figures match the 10-K's segment table ($66,952 million and $64,377 million).

**Checklist:**

1. Yes, the database agrees with the 10-K  — OK / change:
2. Greater China revenue was $66.95 billion in FY2024 and $64.38 billion in FY2025  — OK / change:
3. The decline is about 3.8%, which rounds to 4%  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2025 10-K, p.24*
  - |Greater China|64,377|(4)%|66,952|(8)%|72,559|
  - The following table shows net sales by reportable segment for 2025, 2024 and 2023 (dollars in millions):
  - Greater China net sales decreased during 2025 compared to 2024 primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.
  - The following table shows net sales by category for 2025, 2024 and 2023 (dollars in millions):

## x_047 (tune, level 4, llm_judge)

**Q:** How do Microsoft's and Alphabet's fiscal year 2025 10-Ks describe the effect of AI infrastructure on their costs and margins?

**Gold answer:** Microsoft says scaling its AI infrastructure lowered gross margin percentages: Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling AI infrastructure, offset in part by efficiency gains in Azure, and operating expenses rose on investments in cloud and AI engineering. Alphabet says it is significantly increasing investment in technical infrastructure, in particular for AI, and that the costs of operating it (depreciation, energy, equipment and network capacity) are expected to increase significantly because AI offerings require more compute; Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure.

**Checklist:**

1. Microsoft says scaling its AI infrastructure lowered its gross margin percentage  — OK / change:
2. Microsoft Cloud gross margin percentage decreased to 69%  — OK / change:
3. Microsoft's margin pressure was offset in part by efficiency gains in Azure  — OK / change:
4. Microsoft's operating expenses rose on investments in cloud and AI engineering  — OK / change:
5. Alphabet expects the costs of operating its technical infrastructure (depreciation, energy, equipment, network capacity) to increase significantly  — OK / change:
6. Alphabet attributes the rising costs to AI requiring more compute than its historical offerings  — OK / change:
7. Alphabet expects to significantly increase its investment in technical infrastructure in 2026  — OK / change:
8. Google Cloud's operating income gains were partly offset by higher usage costs for technical infrastructure  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *MSFT FY2025 10-K, p.37*
  - - Microsoft Cloud gross margin percentage decreased to 69% driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure.
  - - Gross margin percentage decreased slightly driven by Intelligent Cloud, offset in part by More Personal Computing.
  - Operating expenses increased $3.8 billion or 6% driven by investments in cloud and AI engineering and Gaming, including the impact of the Activision Blizzard acquisition.
  - |**(In millions, except percentages and per share amounts)**|**2025**|**2024**|**Percentage** **Change**|
- *MSFT FY2025 10-K, p.38*
  - Gross margin percentage decreased slightly primarily driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Microsoft 365 Commercial cloud.
  - Gross margin percentage decreased driven by the impact of scaling our AI infrastructure, offset in part by efficiency gains in Azure.
  - - Operating expenses increased $1.5 billion or 7% driven by investments in cloud and AI engineering.
  - - Operating expenses increased $1.1 billion or 4% driven by investments in cloud and AI engineering and commercial sales.
- *GOOGL FY2025 10-K, p.30*
  - The costs associated with operating our technical infrastructure - depreciation, energy, equipment, and network capacity - are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings.
  - We invested heavily in capital expenditures in 2025 and in 2026, we expect to significantly increase  , relative to 2025, our in  vestment in our technical infrastructure, including servers and network equipment, and data centers.
  - While our technical infrastructure costs increase, we expect to continue to drive efficiencies in our data centers, for example, through the design of our AI models and our TPU and GPU-based technical infrastructure.
  - As we continue to incorporate AI into our products and services, such as with AI Overviews and AI Mode in Search, and with enterprise AI solutions on our Google Cloud Platform, we may monetize differently than our historical consumer and enterprise offerings which could affect revenue growth rates and margin trends.
- *GOOGL FY2025 10-K, p.39*
  - The increase in operating income was primarily driven by an increase in revenues, partially offset by increases in usage costs for technical infrastructure and employee compensation expenses.
  - The increase in operating income was primarily driven by an increase in revenues, partially offset by an increase in expenses related to legal and other matters, TAC, and content acquisition costs.
  - Google Cloud operating income increased $7.8 billion from 2024 to 2025.
  - The increase in operating loss was primarily driven by an increase in employee compensation expenses largely due to an increase in a valuation-based compensation charge related to Waymo.

## x_048 (tune, level 4, llm_judge)

**Q:** Which company had the highest capital expenditures in fiscal year 2025, and which had the highest capital expenditures relative to revenue?

**Gold answer:** Alphabet spent the most in dollars: $91.4 billion of purchases of property and equipment (Microsoft $64.6 billion, Apple $12.7 billion). Relative to revenue, Microsoft was narrowly highest at about 22.9% ($64.6 billion of $281.7 billion), just ahead of Alphabet at about 22.7% ($91.4 billion of $402.8 billion); Apple was about 3.1%.

**Checklist:**

1. Alphabet had the highest capital expenditures in dollars  — OK / change:
2. Alphabet's FY2025 capital expenditures were about $91.4 billion  — OK / change:
3. Microsoft's FY2025 capital expenditures were about $64.6 billion  — OK / change:
4. Apple's FY2025 capital expenditures were about $12.7 billion  — OK / change:
5. Microsoft had the highest capital expenditures relative to revenue (about 22.9%)  — OK / change:
6. Alphabet's capital expenditures were about 22.7% of revenue  — OK / change:
7. Apple's capital expenditures were about 3.1% of revenue  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *GOOGL FY2025 10-K, p.53*
  - |Purchases of property and equipment|(32,251)|(52,535)|(91,447)|
  - |Purchases of property and equipment included in accrued liabilities and||||
  - |Depreciation of property and equipment|11,946|15,311|21,136|
  - |Accrued revenue share|482|1,059|899|
- *MSFT FY2025 10-K, p.50*
  - |Additions to property and equipment| **(64,551)**|(44,477)| (28,107)|
  - | Unearned revenue|**5,438**|5,348| 5,535|
  - |Acquisition of companies, net of cash acquired and divestitures, and purchases of intangible and other assets|**(5,978)**|(69,132)| (1,670)|
  - |Purchases of investments| **(29,775)**|(17,732)| (37,651)|
- *AAPL FY2025 10-K, p.34*
  - |Payments for acquisition of property, plant and equipment|(12,715)|(9,447)|(10,959)|
  - |Purchases of marketable securities|(24,407)|(48,656)|(29,513)|

## x_049 (tune, level 7, llm_judge)

**Q:** Which other region grew the fastest, and why?

*(follow-up; earlier turn: How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and why?)*

**Gold answer:** Japan grew fastest: net sales rose about 14.6%, from $25.1 billion to $28.7 billion. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

**Checklist:**

1. Japan grew the fastest  — OK / change:
2. Japan's net sales grew about 14.6%  — OK / change:
3. Japan's net sales rose from $25.1 billion to $28.7 billion  — OK / change:
4. The 10-K attributes the increase primarily to higher net sales of iPhone  — OK / change:
5. The 10-K attributes the increase to higher net sales of Services  — OK / change:
6. The 10-K attributes the increase to higher net sales of iPad  — OK / change:

**Source sentences (gold pages, most relevant first):**

- *AAPL FY2025 10-K, p.24*
  - Japan net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and iPad.
  - Europe net sales increased during 2025 compared to 2024 primarily due to higher net sales of Services, iPhone and Mac.
  - Rest of Asia Pacific net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone, Services and Mac.
  - Americas net sales increased during 2025 compared to 2024 primarily due to higher net sales of iPhone and Services.

## x_050 (holdout, level 7, llm_judge)

**Q:** How much of that came from the United States, and how did that share change from the year before?

*(follow-up; earlier turn: What was Microsoft's total revenue in fiscal year 2025?)*

**Gold answer:** $144.5 billion, or about 51.3% of FY2025 revenue, came from the United States, up from about 50.9% ($124.7 billion of $245.1 billion) in FY2024, an increase of about 0.4 percentage points.

**Checklist:**

1. About $144.5 billion of FY2025 revenue came from the United States  — OK / change:
2. The United States was about 51.3% of FY2025 revenue  — OK / change:
3. The United States was about 50.9% of FY2024 revenue  — OK / change:
4. The United States share rose by about 0.4 percentage points  — OK / change:

**Source sentences (gold pages, most relevant first):**



## Decisions (Saanvi, 2026-11-06)
Judged from each question's wording, not from which facts the agent tends to miss.
- **x_048:** dropped facts 4 and 7 (Apple's capex and capex share): not asked; a correct answer without Apple covered 5/7 = 71% and failed.
- **x_041:** dropped fact 5 (gross margin +$22.9B): it does not answer what drove operating income. Fact 3 (runners-up) kept: it is the evidence for "fastest".
- **x_035:** fact 4 "Revenue grew (about 2.0%)" -> "Revenue grew": the question itself says revenue grew.
- **x_047:** dropped fact 7 (2026 investment plans): about investment, not costs or margins. Facts 2 and 3 kept separate.
- **x_042:** fact 3 (other companies' R&D shares) kept: it is the evidence for "largest share".
- All other lists (x_036, x_037, x_038, x_039, x_043, x_044, x_045, x_046, x_049, x_050) OK as written. All 31 checklists are now human-reviewed.
