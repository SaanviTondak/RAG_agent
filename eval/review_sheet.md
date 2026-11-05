# Review sheet: gold facts and extra questions

Two jobs (steps 2b and 7b of plans/day3.md). Edit `eval/gold_facts.json` / `eval/extra_questions.json` directly, or write notes here and I'll apply them.

**For each fact list:** is every fact really required by the reference answer? Is anything split too finely (one figure becoming several facts) or missing? Once a list looks right, set `"reviewed": true` in `eval/gold_facts.json`.

**For each extra question:** is it clear and answerable from the data? Is the gold answer right and complete? Is the grader sensible?

## Part 1: dev fact lists (judge checklists)

### q_006: What were the primary risk factors Apple disclosed related to its supply chain in its fiscal year 2025 10-K filing?

**Reference:** Apple disclosed risks including: reliance on single or limited sources for components; dependence on third-party manufacturers; supply chain disruptions from geopolitical tensions, natural disasters, and health emergencies; component supply constraints affecting product availability; and risks from concentration of manufacturing operations in specific regions.

1. Apple disclosed reliance on single or limited sources for components as a supply chain risk factor.
2. Apple disclosed dependence on third-party manufacturers as a supply chain risk factor.
3. Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.
4. Apple disclosed supply chain disruptions from natural disasters as a risk factor.
5. Apple disclosed supply chain disruptions from health emergencies as a risk factor.
6. Apple disclosed component supply constraints affecting product availability as a risk factor.
7. Apple disclosed risks from concentration of manufacturing operations in specific regions as a supply chain risk factor.

### q_012: How did Apple's Greater China revenue change between fiscal year 2024 and fiscal year 2025, and does the 10-K filing explain why?

**Reference:** Apple's Greater China revenue decreased from $66.95 billion in FY2024 to $64.38 billion in FY2025, a decline of approximately 3.8%. The FY2025 10-K states this was primarily due to lower net sales of iPhone, partially offset by higher net sales of Mac.

1. Apple's Greater China revenue was $66.95 billion in FY2024
2. Apple's Greater China revenue was $64.38 billion in FY2025
3. Apple's Greater China revenue decreased from FY2024 to FY2025
4. The decline was approximately 3.8%
5. The FY2025 10-K states the decrease was primarily due to lower net sales of iPhone
6. The decrease was partially offset by higher net sales of Mac

### q_014: Microsoft restructured its segment reporting in August 2024. How are the three segments defined in the fiscal year 2025 10-K, and what was the revenue for each?

**Reference:** The three segments in the FY2025 10-K are: (1) Productivity and Business Processes ($120.8B) - includes Microsoft 365 Commercial/Consumer, LinkedIn, and Dynamics; (2) Intelligent Cloud ($106.3B) - includes Azure, SQL Server, Windows Server, GitHub, and enterprise services; (3) More Personal Computing ($54.6B) - includes Windows, Devices, Gaming, and Search/news advertising.

1. The FY2025 10-K has three segments.
2. One segment is Productivity and Business Processes.
3. Productivity and Business Processes revenue was $120.8B.
4. Productivity and Business Processes includes Microsoft 365 Commercial/Consumer.
5. Productivity and Business Processes includes LinkedIn.
6. Productivity and Business Processes includes Dynamics.
7. One segment is Intelligent Cloud.
8. Intelligent Cloud revenue was $106.3B.
9. Intelligent Cloud includes Azure.
10. Intelligent Cloud includes SQL Server.
11. Intelligent Cloud includes Windows Server.
12. Intelligent Cloud includes GitHub.
13. Intelligent Cloud includes enterprise services.
14. One segment is More Personal Computing.
15. More Personal Computing revenue was $54.6B.
16. More Personal Computing includes Windows.
17. More Personal Computing includes Devices.
18. More Personal Computing includes Gaming.
19. More Personal Computing includes Search/news advertising.

### q_017: According to Alphabet's 10-K filings, what are the key components of 'Google Services' revenue, and how did YouTube advertising revenue change between FY2024 and FY2025?

**Reference:** Google Services includes Google Search & other, YouTube ads, Google Network, and Google subscriptions/platforms/devices. YouTube advertising revenue grew from $36.1 billion in FY2024 to $40.4 billion in FY2025, an increase of approximately 11.7%.

1. Google Services includes Google Search & other
2. Google Services includes YouTube ads
3. Google Services includes Google Network
4. Google Services includes Google subscriptions/platforms/devices
5. YouTube advertising revenue was $36.1 billion in FY2024
6. YouTube advertising revenue was $40.4 billion in FY2025
7. YouTube advertising revenue increased by approximately 11.7% between FY2024 and FY2025

### q_022: Across all three companies, which saw the largest absolute dollar increase in revenue between their two most recent fiscal years? Break down how much of that increase came from each business segment.

**Reference:** Alphabet had the largest absolute increase at approximately $52.8B ($350.0B to $402.8B). By operating segment, Google Services grew by $37.8B ($304.9B to $342.7B), Google Cloud grew by $15.5B ($43.2B to $58.7B), and Other Bets declined by $0.1B ($1.6B to $1.5B); a hedging reconciliation of approximately -$0.3B accounts for the difference between the segment subtotal and consolidated revenue. Microsoft increased by $36.6B and Apple by $25.1B.

1. Alphabet had the largest absolute dollar increase in revenue among the three companies
2. Alphabet's revenue increased by approximately $52.8B, from $350.0B to $402.8B
3. Google Services grew by $37.8B, from $304.9B to $342.7B
4. Google Cloud grew by $15.5B, from $43.2B to $58.7B
5. Other Bets declined by $0.1B, from $1.6B to $1.5B
6. A hedging reconciliation of approximately -$0.3B accounts for the difference between the segment subtotal and consolidated revenue
7. Microsoft's revenue increased by $36.6B
8. Apple's revenue increased by $25.1B

### q_025: Apple's Services segment has been growing as a share of total revenue. Calculate the Services revenue growth rate for each of the last two years, compare it to iPhone revenue growth, and find what Apple's 10-K says about the strategic importance of Services.

**Reference:** Services growth: FY2023->FY2024: 12.9% ($85.2B to $96.2B), FY2024->FY2025: 13.5% ($96.2B to $109.2B). iPhone growth: FY2023->FY2024: 0.3%, FY2024->FY2025: 4.2%. Services is consistently growing much faster. The 10-K highlights Services as a key growth driver with higher margins, recurring revenue from subscriptions, App Store, Apple Music, iCloud, and advertising.

1. Services revenue grew 12.9% from FY2023 to FY2024 ($85.2B to $96.2B)
2. Services revenue grew 13.5% from FY2024 to FY2025 ($96.2B to $109.2B)
3. iPhone revenue grew 0.3% from FY2023 to FY2024
4. iPhone revenue grew 4.2% from FY2024 to FY2025
5. Services is consistently growing much faster than iPhone
6. The 10-K highlights Services as a key growth driver
7. The 10-K says Services has higher margins
8. The 10-K says Services has recurring revenue from subscriptions
9. The 10-K mentions App Store as part of Services
10. The 10-K mentions Apple Music as part of Services
11. The 10-K mentions iCloud as part of Services
12. The 10-K mentions advertising as part of Services

## Part 2: extra questions

Holdout questions (marked 🔒) are only run once, at the end.

### x_001 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** What was Microsoft's net income in fiscal year 2025?

**Gold:** $101.8 billion

- Numeric gold: `101832000000` (from SQL: `SELECT net_income FROM income_statements WHERE company_ticker='MSFT' AND fiscal_year=2025`)

### x_002 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** What was Alphabet's diluted earnings per share for fiscal year 2025?

**Gold:** $10.81

- Numeric gold: `10.81` (from SQL: `SELECT eps_diluted FROM income_statements WHERE company_ticker='GOOGL' AND fiscal_year=2025`)

### x_003 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** How much did Apple spend on research and development in fiscal year 2024?

**Gold:** $31.4 billion

- Numeric gold: `31370000000` (from SQL: `SELECT research_and_development FROM income_statements WHERE company_ticker='AAPL' AND fiscal_year=2024`)

### x_004 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** What were Microsoft's total assets at the end of fiscal year 2025?

**Gold:** $619.0 billion

- Numeric gold: `619003000000` (from SQL: `SELECT total_assets FROM balance_sheets WHERE company_ticker='MSFT' AND fiscal_year=2025`)

### x_005 🔒 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** What was Alphabet's operating income in fiscal year 2024?

**Gold:** $112.4 billion

- Numeric gold: `112390000000` (from SQL: `SELECT operating_income FROM income_statements WHERE company_ticker='GOOGL' AND fiscal_year=2024`)

### x_006 🔒 (lookup, tier 1, fuzzy_numeric, needs sql)

**Q:** What was Apple's gross margin percentage in fiscal year 2025?

**Gold:** 46.9%

- Numeric gold: `46.90516410716045` (from SQL: `SELECT 100.0 * gross_profit / revenue FROM income_statements WHERE company_ticker='AAPL' AND fiscal_year=2025`)

### x_007 (comparison, tier 2, exact_match_entity, needs sql)

**Q:** Which company had the highest operating margin in fiscal year 2025, and what was it?

**Gold:** Microsoft had the highest operating margin in FY2025 at about 45.6% (Alphabet 32.0%, Apple 32.0%).

- Numeric gold: `45.62195624085985` (from SQL: `SELECT 100.0 * operating_income / revenue FROM income_statements WHERE company_ticker='MSFT' AND fiscal_year=2025`)
- Gold entities: ['MSFT']

### x_008 (comparison, tier 2, exact_match_entity, needs sql)

**Q:** Which two companies had the highest total revenue in fiscal year 2025?

**Gold:** Apple ($416.2 billion) and Alphabet ($402.8 billion); Microsoft was third at $281.7 billion.

- Gold entities: ['AAPL', 'GOOGL']

### x_009 (comparison, tier 2, exact_match_entity, needs sql)

**Q:** Rank the three companies by research and development spending as a percentage of revenue in their most recent fiscal year.

**Gold:** Alphabet 15.2%, Microsoft 11.5%, Apple 8.3% (FY2025 R&D / revenue).

- Gold entities: ['GOOGL', 'MSFT', 'AAPL'] (order matters)

### x_010 🔒 (comparison, tier 2, fuzzy_numeric, needs sql)

**Q:** What was Microsoft's debt-to-equity ratio (total debt divided by stockholders' equity) at the end of fiscal year 2025?

**Gold:** About 0.13 ($43.2 billion of total debt / $343.5 billion of stockholders' equity).

- Numeric gold: `0.12562922332951942` (from SQL: `SELECT 1.0 * total_debt / stockholders_equity FROM balance_sheets WHERE company_ticker='MSFT' AND fiscal_year=2025`)

### x_011 (comparison, tier 2, fuzzy_numeric, needs sql)

**Q:** By what percentage did Alphabet's net income grow from fiscal year 2024 to fiscal year 2025?

**Gold:** About 32.0% ($100.1 billion to $132.2 billion).

- Numeric gold: `32.01422321660441` (from SQL: `SELECT 100.0 * (a.net_income - b.net_income) / b.net_income FROM income_statements a JOIN income_statements b ON b.company_ticker = a.company_ticker AND b.fiscal_year = 2024 WHERE a.company_ticker='GOOGL' AND a.fiscal_year=2025`)

### x_012 🔒 (comparison, tier 2, exact_match_entity, needs sql)

**Q:** Which company had the largest cash and cash equivalents balance at the end of its most recent fiscal year, and how much was it?

**Gold:** Apple, with $35.9 billion (Alphabet $30.7 billion, Microsoft $30.2 billion).

- Numeric gold: `35934000000` (from SQL: `SELECT cash_and_equivalents FROM balance_sheets WHERE company_ticker='AAPL' AND fiscal_year=2025`)
- Gold entities: ['AAPL']

### x_013 (comparison, tier 3, llm_judge, needs sql)

**Q:** For each company, what share of fiscal year 2025 revenue came from its largest geographic region, and which company's revenue was most concentrated in a single region?

**Gold:** Microsoft was the most concentrated: the United States was 51.3% of its FY2025 revenue. Alphabet's largest region, the United States, was 48.2% of revenue, and Apple's largest region, the Americas, was 42.9%.

- Facts:
  1. Microsoft's revenue was the most concentrated in a single region
  2. Microsoft's largest geographic region was the United States
  3. The United States accounted for 51.3% of Microsoft's FY2025 revenue
  4. Alphabet's largest geographic region was the United States
  5. The United States accounted for 48.2% of Alphabet's revenue
  6. Apple's largest geographic region was the Americas
  7. The Americas accounted for 42.9% of Apple's revenue

### x_014 (pdf_only, tier 1, llm_judge, needs pdf)

**Q:** What risks related to artificial intelligence does Microsoft disclose in its fiscal year 2025 10-K?

**Gold:** Microsoft's FY2025 10-K discloses AI risks including: intense and rapidly evolving competition in AI, including from open AI models; significant costs to build AI and cloud infrastructure that reduce operating margins; flawed algorithms, biased or inaccurate datasets, and harmful or inaccurate AI-generated content that could cause reputational or competitive harm or legal liability; misuse of its AI systems and services by users; emerging AI regulation such as the EU AI Act that could increase costs or restrict opportunity; and intellectual property claims arising from AI training and output.

- Gold pages: MSFT_FY2025_10-K p.17, MSFT_FY2025_10-K p.18, MSFT_FY2025_10-K p.22, MSFT_FY2025_10-K p.24, MSFT_FY2025_10-K p.26
- Facts:
  1. Microsoft's FY2025 10-K discloses intense and rapidly evolving competition in AI, including from open AI models.
  2. Microsoft's FY2025 10-K discloses significant costs to build AI and cloud infrastructure that reduce operating margins.
  3. Microsoft's FY2025 10-K discloses flawed algorithms, biased or inaccurate datasets, and harmful or inaccurate AI-generated content that could cause reputational or competitive harm or legal liability.
  4. Microsoft's FY2025 10-K discloses misuse of its AI systems and services by users.
  5. Microsoft's FY2025 10-K discloses emerging AI regulation such as the EU AI Act that could increase costs or restrict opportunity.
  6. Microsoft's FY2025 10-K discloses intellectual property claims arising from AI training and output.

### x_015 (pdf_only_figure, tier 1, fuzzy_numeric, needs pdf)

**Q:** What were Alphabet's capital expenditures in fiscal year 2025?

**Gold:** $91.4 billion, primarily reflecting investments in technical infrastructure.

- Numeric gold: `91400000000` (from the filing)
- Gold pages: GOOGL_FY2025_10-K p.35

### x_016 🔒 (pdf_only_figure, tier 1, fuzzy_numeric, needs pdf)

**Q:** According to Microsoft's fiscal year 2025 10-K, by how much did Azure and other cloud services revenue grow?

**Gold:** 34%

- Numeric gold: `34` (from the filing)
- Gold pages: MSFT_FY2025_10-K p.38

### x_017 (pdf_only_figure, tier 1, fuzzy_numeric, needs pdf)

**Q:** How much did Alphabet spend repurchasing its shares in fiscal year 2025?

**Gold:** $45.4 billion ($6.5 billion of Class A and $38.9 billion of Class C shares).

- Numeric gold: `45400000000` (from the filing)
- Gold pages: GOOGL_FY2025_10-K p.35

### x_018 🔒 (pdf_only, tier 2, llm_judge, needs pdf)

**Q:** What risks does Alphabet's fiscal year 2025 10-K describe about its dependence on advertising revenue?

**Gold:** Alphabet generated more than 70% of total revenues from online advertising in 2025. Risks: reduced advertiser spending, which tends to track economic conditions; advertisers and partners can terminate contracts at any time; AI is reshaping the advertising industry and Alphabet may not adapt to new ad formats effectively; changes to its own or other companies' advertising and data-privacy practices; and technologies that block ads or make personalized ads more difficult.

- Gold pages: GOOGL_FY2025_10-K p.9, GOOGL_FY2025_10-K p.10
- Facts:
  1. Alphabet generated more than 70% of total revenues from online advertising in 2025.
  2. Reduced advertiser spending is a risk, and advertiser spending tends to track economic conditions.
  3. Advertisers and partners can terminate contracts at any time.
  4. AI is reshaping the advertising industry and Alphabet may not adapt to new ad formats effectively.
  5. Changes to Alphabet's own or other companies' advertising and data-privacy practices are a risk.
  6. Technologies that block ads or make personalized ads more difficult are a risk.

### x_019 (pdf_only_figure, tier 1, fuzzy_numeric, needs pdf)

**Q:** What was Microsoft Cloud revenue in fiscal year 2025?

**Gold:** $168.9 billion, up 23%.

- Numeric gold: `168900000000` (from the filing)
- Gold pages: MSFT_FY2025_10-K p.33

### x_020 (sql_and_pdf, tier 2, llm_judge, needs sql+pdf)

**Q:** How did Microsoft's Intelligent Cloud revenue change from fiscal year 2024 to fiscal year 2025, and what does the 10-K say drove the change?

**Gold:** Intelligent Cloud revenue rose from $87.5 billion to $106.3 billion, an increase of about $18.8 billion or 21.5%. The FY2025 10-K attributes the growth to Azure: server products and cloud services revenue increased 23%, driven by Azure and other cloud services revenue growth of 34%.

- Gold pages: MSFT_FY2025_10-K p.38
- Facts:
  1. Intelligent Cloud revenue rose from fiscal year 2024 to fiscal year 2025.
  2. Intelligent Cloud revenue was $87.5 billion in fiscal year 2024.
  3. Intelligent Cloud revenue was $106.3 billion in fiscal year 2025.
  4. The increase was about $18.8 billion.
  5. The increase was 21.5%.
  6. The FY2025 10-K attributes the growth to Azure.
  7. Server products and cloud services revenue increased 23%.
  8. Azure and other cloud services revenue growth was 34%.

### x_021 (sql_and_pdf, tier 2, llm_judge, needs sql+pdf)

**Q:** How did Alphabet's Google Cloud revenue change between fiscal year 2024 and fiscal year 2025, and what does the 10-K say drove it?

**Gold:** Google Cloud revenue increased from $43.2 billion to $58.7 billion, up $15.5 billion or about 35.8%. The FY2025 10-K says the increase was primarily driven by growth in Google Cloud Platform, largely from infrastructure and platform services.

- Gold pages: GOOGL_FY2025_10-K p.37
- Facts:
  1. Google Cloud revenue was $43.2 billion in fiscal year 2024
  2. Google Cloud revenue was $58.7 billion in fiscal year 2025
  3. Google Cloud revenue increased by $15.5 billion between fiscal year 2024 and fiscal year 2025
  4. Google Cloud revenue increased by about 35.8% between fiscal year 2024 and fiscal year 2025
  5. The FY2025 10-K says the increase was primarily driven by growth in Google Cloud Platform
  6. The growth in Google Cloud Platform was largely from infrastructure and platform services

### x_022 (sql_and_pdf, tier 2, llm_judge, needs sql+pdf)

**Q:** How did Apple's Wearables, Home and Accessories revenue change from fiscal year 2024 to fiscal year 2025, and what reason does the 10-K give?

**Gold:** Wearables, Home and Accessories revenue fell from $37.0 billion to $35.7 billion, a decrease of about $1.3 billion or 3.6%. The FY2025 10-K says the decrease was primarily due to lower net sales of Accessories and Wearables.

- Gold pages: AAPL_FY2025_10-K p.25
- Facts:
  1. Wearables, Home and Accessories revenue decreased from fiscal year 2024 to fiscal year 2025.
  2. Wearables, Home and Accessories revenue was $37.0 billion in fiscal year 2024.
  3. Wearables, Home and Accessories revenue was $35.7 billion in fiscal year 2025.
  4. The revenue decrease was about $1.3 billion.
  5. The revenue decrease was 3.6%.
  6. The FY2025 10-K attributes the decrease primarily to lower net sales of Accessories.
  7. The FY2025 10-K attributes the decrease primarily to lower net sales of Wearables.

### x_023 🔒 (sql_and_pdf, tier 2, llm_judge, needs sql+pdf)

**Q:** How did Microsoft's More Personal Computing revenue change in fiscal year 2025, and what does the 10-K attribute the change to?

**Gold:** More Personal Computing revenue increased from $50.8 billion to $54.6 billion, up about $3.8 billion or 7.5%. The FY2025 10-K attributes the increase to Gaming (Xbox content and services, helped by the Activision Blizzard acquisition and Xbox Game Pass) and Search and news advertising (up 13%), with Windows and Devices up 2%.

- Gold pages: MSFT_FY2025_10-K p.38, MSFT_FY2025_10-K p.39
- Facts:
  1. More Personal Computing revenue increased from $50.8 billion to $54.6 billion
  2. The increase was about $3.8 billion
  3. The increase was 7.5%
  4. The FY2025 10-K attributes the increase to Gaming (Xbox content and services)
  5. Gaming was helped by the Activision Blizzard acquisition
  6. Gaming was helped by Xbox Game Pass
  7. The FY2025 10-K attributes the increase to Search and news advertising
  8. Search and news advertising was up 13%
  9. Windows and Devices was up 2%

### x_024 🔒 (sql_and_pdf, tier 3, llm_judge, needs sql+pdf)

**Q:** Apple's revenue from Japan grew in fiscal year 2025. By how much, and what does the 10-K say drove it?

**Gold:** Japan revenue rose from $25.1 billion in FY2024 to $28.7 billion in FY2025, an increase of about $3.7 billion or 14.6%. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone, Services and iPad.

- Gold pages: AAPL_FY2025_10-K p.24
- Facts:
  1. Japan revenue was $25.1 billion in FY2024
  2. Japan revenue was $28.7 billion in FY2025
  3. The increase was about $3.7 billion
  4. The increase was 14.6%
  5. The FY2025 10-K says the increase was primarily due to higher net sales of iPhone
  6. The FY2025 10-K says the increase was primarily due to higher net sales of Services
  7. The FY2025 10-K says the increase was primarily due to higher net sales of iPad

### x_025 (trap:apple_segments, tier 2, llm_judge, needs sql)

**Q:** What were Apple's reportable segments in fiscal year 2025, and how much revenue did each generate?

**Gold:** Apple's reportable segments are geographic: Americas $178.4 billion, Europe $111.0 billion, Greater China $64.4 billion, Japan $28.7 billion, and Rest of Asia Pacific $33.7 billion.

- Facts:
  1. Apple's reportable segments are geographic
  2. Americas generated $178.4 billion in revenue
  3. Europe generated $111.0 billion in revenue
  4. Greater China generated $64.4 billion in revenue
  5. Japan generated $28.7 billion in revenue
  6. Rest of Asia Pacific generated $33.7 billion in revenue

### x_026 🔒 (trap:alphabet_hedging, tier 2, fuzzy_numeric, needs sql)

**Q:** Which of Alphabet's business segments had the smallest revenue in fiscal year 2025, and how much was it?

**Gold:** Other Bets, with $1.5 billion.

- Numeric gold: `1537000000` (from SQL: `SELECT revenue FROM segment_revenue WHERE company_ticker='GOOGL' AND fiscal_year=2025 AND segment_name='Other Bets'`)

### x_027 (trap:missing_column, tier 2, fuzzy_numeric, needs sql)

**Q:** What was Alphabet's gross profit in fiscal year 2025?

**Gold:** $240.3 billion (revenue of $402.8 billion minus cost of revenues of $162.5 billion).

- Numeric gold: `240301000000` (from SQL: `SELECT revenue - cost_of_revenue FROM income_statements WHERE company_ticker='GOOGL' AND fiscal_year=2025`)

### x_028 (trap:fiscal_year_ends, tier 2, exact_match_entity, needs sql)

**Q:** Which company's fiscal year 2025 ended earliest, and what was its revenue for that year?

**Gold:** Microsoft, whose fiscal year 2025 ended June 30, 2025, with revenue of $281.7 billion.

- Numeric gold: `281724000000` (from SQL: `SELECT revenue FROM income_statements WHERE company_ticker='MSFT' AND fiscal_year=2025`)
- Gold entities: ['MSFT']

### x_029 (trap:msft_restatement, tier 3, llm_judge, needs sql+pdf)

**Q:** What was Microsoft's Intelligent Cloud revenue in fiscal year 2024?

**Gold:** $87.5 billion under the segment definitions restated in the FY2025 10-K. The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud, under the segment structure in place before the August 2024 reorganization.

- Gold pages: MSFT_FY2024_10-K p.43
- Facts:
  1. Microsoft's Intelligent Cloud revenue in fiscal year 2024 was $87.5 billion under the segment definitions restated in the FY2025 10-K.
  2. The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud.
  3. The $105.4 billion figure was reported under the segment structure in place before the August 2024 reorganization.

### x_030 (out_of_scope, tier 1, out_of_scope, needs nothing)

**Q:** What was Amazon's total revenue in fiscal year 2025?

**Gold:** Not available: the data covers only Apple, Microsoft and Alphabet.


### x_031 🔒 (out_of_scope, tier 1, out_of_scope, needs nothing)

**Q:** What was Apple's net income in fiscal year 2020?

**Gold:** Not available: the database covers FY2023-FY2025 and the filings are the FY2024 and FY2025 10-Ks.


### x_032 (out_of_scope, tier 1, out_of_scope, needs nothing)

**Q:** What is Microsoft's current stock price?

**Gold:** Not available: the data contains annual financials and 10-K filings, not market prices.

## Part 3: harder questions (added Day 4, all tune)

Written because the top three models all scored 32/32. Figures come from SQL (`gold_sql`) or were copied from the page text; facts are hand-written (`reviewed: false` in `eval/gold_facts.json`).

### x_033 (hard:multi_year_math, tier 3, exact_match_entity, needs sql)

**Q:** Which company had the highest compound annual growth rate in revenue from fiscal year 2023 to fiscal year 2025, and what was it?

**Gold:** Microsoft, at about 15.3% a year (Alphabet about 14.5%, Apple about 4.2%).

- Numeric gold: `15.300468973386483` (from SQL: `SELECT 100.0 * (power(1.0 * a.revenue / b.revenue, 0.5) - 1) FROM income_statements a JOIN income_statements b ON b.company_ticker = a.company_ticker AND b.fiscal_year = 2023 WHERE a.company_ticker='MSFT' AND a.fiscal_year=2025`)
- Gold entities: ['MSFT']

### x_034 (hard:margin_change, tier 3, exact_match_entity, needs sql)

**Q:** Which company's net profit margin improved the most, in percentage points, from fiscal year 2024 to fiscal year 2025?

**Gold:** Alphabet: its net margin rose about 4.2 percentage points, from 28.6% to 32.8% (Apple rose about 2.9 points, Microsoft about 0.2 points).

- Numeric gold: `4.206206154062542` (from SQL: `SELECT 100.0 * a.net_income / a.revenue - 100.0 * b.net_income / b.revenue FROM income_statements a JOIN income_statements b ON b.company_ticker = a.company_ticker AND b.fiscal_year = 2024 WHERE a.company_ticker='GOOGL' AND a.fiscal_year=2025`)
- Gold entities: ['GOOGL']

### x_035 (hard:older_filing_why, tier 3, llm_judge, needs sql+pdf)

**Q:** Apple's net income fell in fiscal year 2024 even though revenue grew. By how much did it fall, and what does the 10-K say caused it?

**Gold:** Net income fell from $97.0 billion in FY2023 to $93.7 billion in FY2024, a decrease of about $3.3 billion (3.4%), while revenue grew about 2.0%. The FY2024 10-K attributes the higher tax expense to a one-time income tax charge of $10.2 billion, net, related to the European Commission's State Aid Decision, which raised the effective tax rate to 24.1% from 14.7%.

- Gold pages: AAPL_FY2024_10-K p.27, AAPL_FY2024_10-K p.42
- Facts:
  1. Apple's net income was $97.0 billion in FY2023
  2. Apple's net income was $93.7 billion in FY2024
  3. Net income decreased by about $3.3 billion (about 3.4%)
  4. Revenue grew (about 2.0%) in FY2024
  5. The FY2024 10-K cites a one-time income tax charge of $10.2 billion, net
  6. The charge related to the European Commission's State Aid Decision
  7. The effective tax rate rose to 24.1% from 14.7%

### x_036 (hard:two_company_why, tier 3, llm_judge, needs sql+pdf)

**Q:** Microsoft and Alphabet both grew operating income in fiscal year 2025. By how much did each grow, and what does each company's 10-K say drove it?

**Gold:** Microsoft's operating income rose $19.1 billion (about 17.4%), from $109.4 billion to $128.5 billion; its 10-K says the growth came from all of its segments. Alphabet's rose $16.6 billion (about 14.8%), from $112.4 billion to $129.0 billion; its 10-K attributes the segment gains mainly to higher revenues: Google Services operating income rose $18.1 billion and Google Cloud $7.8 billion, partly offset by a $3.1 billion larger Other Bets loss and higher Alphabet-level AI research costs.

- Gold pages: MSFT_FY2025_10-K p.37, GOOGL_FY2025_10-K p.38, GOOGL_FY2025_10-K p.39
- Facts:
  1. Microsoft's operating income rose by $19.1 billion (about 17%)
  2. Microsoft's operating income was $109.4 billion in FY2024 and $128.5 billion in FY2025
  3. Microsoft's 10-K says the growth came from all (each) of its segments
  4. Alphabet's operating income rose by $16.6 billion (about 14.8%)
  5. Alphabet's operating income was $112.4 billion in FY2024 and $129.0 billion in FY2025
  6. Alphabet's 10-K attributes the segment operating income gains mainly to higher revenues
  7. Google Services operating income rose $18.1 billion
  8. Google Cloud operating income rose $7.8 billion
  9. A larger Other Bets loss (about $3.1 billion more) or higher Alphabet-level costs partly offset the gains

### x_037 (hard:definition_list, tier 2, llm_judge, needs pdf)

**Q:** How does Microsoft's fiscal year 2025 10-K define Microsoft Cloud revenue, and how much was it in each of the last three fiscal years?

**Gold:** Microsoft Cloud revenue includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365. It was $168.9 billion in FY2025, $137.7 billion in FY2024 and $111.6 billion in FY2023.

- Gold pages: MSFT_FY2025_10-K p.80, MSFT_FY2025_10-K p.33
- Facts:
  1. Microsoft Cloud revenue includes Microsoft 365 Commercial cloud
  2. Microsoft Cloud revenue includes Azure and other cloud services
  3. Microsoft Cloud revenue includes the commercial portion of LinkedIn
  4. Microsoft Cloud revenue includes Dynamics 365
  5. Microsoft Cloud revenue was $168.9 billion in FY2025
  6. Microsoft Cloud revenue was $137.7 billion in FY2024
  7. Microsoft Cloud revenue was $111.6 billion in FY2023

### x_038 (hard:two_filing_figures, tier 2, llm_judge, needs pdf)

**Q:** How much did Apple and Alphabet each spend on share repurchases in fiscal year 2025, and which spent more?

**Gold:** Apple spent more. Apple's cash flow statement shows $90.7 billion of repurchases of common stock in FY2025 (Note 10 reports 402 million shares repurchased for $89.3 billion; either figure is acceptable). Alphabet repurchased 240 million shares for $45.4 billion.

- Gold pages: AAPL_FY2025_10-K p.34, AAPL_FY2025_10-K p.45, GOOGL_FY2025_10-K p.42, GOOGL_FY2025_10-K p.80
- Facts:
  1. Apple spent more on share repurchases than Alphabet in FY2025
  2. Apple's FY2025 repurchases were about $90.7 billion (cash flow statement) or $89.3 billion (Note 10); either figure counts
  3. Alphabet's FY2025 repurchases were $45.4 billion

### x_039 (hard:share_change, tier 2, llm_judge, needs sql)

**Q:** What share of Alphabet's revenue came from Google Cloud in fiscal year 2025, and how did that share change from fiscal year 2024?

**Gold:** Google Cloud was about 14.6% of Alphabet's FY2025 revenue ($58.7 billion of $402.8 billion), up from about 12.4% in FY2024 ($43.2 billion of $350.0 billion), an increase of about 2.2 percentage points.

- Facts:
  1. Google Cloud was about 14.6% of Alphabet's FY2025 revenue
  2. Google Cloud revenue was $58.7 billion in FY2025
  3. Google Cloud was about 12.4% (12.3-12.4%) of Alphabet's FY2024 revenue
  4. The share increased by about 2.2 percentage points

### x_040 (hard:pdf_figure_plus_sql, tier 2, fuzzy_numeric, needs sql+pdf)

**Q:** What percentage of Microsoft's fiscal year 2025 revenue came from Microsoft Cloud?

**Gold:** About 60.0% ($168.9 billion of $281.7 billion).

- Numeric gold: `59.952293734293136` (from the filing)
- Gold pages: MSFT_FY2025_10-K p.33, MSFT_FY2025_10-K p.80
