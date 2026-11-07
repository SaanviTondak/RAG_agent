why not use determintisc router (eg jev)
many questions need both sources 
The words in a question don't reliably tell you the source. "How did YouTube ad revenue change?" sounds like a database question, but YouTube isn't in the database; it's only in the PDF tables.
No data to train/tune router 

Why the agent alone isn't quite enough either:

An LLM sometimes takes shortcuts. For q_012 ("did revenue change, and does the 10-K explain why?") it might get the numbers from SQL and then make up the "why" without ever searching the filings.
What I'd do: the agent does the routing, with deterministic checks around it. Rules make good checks, even though they make poor routers. I've added this to the plan:

A deterministic pre-pass (regex, no LLM). It pulls out company names and fiscal years ("Apple" → AAPL, "fiscal year 2025" → 2025) and passes them to the agent as filters. This is 100% reliable and makes PDF search much more precise.
A coverage check before the agent answers. If the question contains words like "why", "explain", "according to the 10-K", "risk" or "strategy", but the agent never searched the filings, the code sends it back once with "you haven't checked the filings yet". If the question asks for a number and there's no SQL or table evidence behind it, the agent gets a similar nudge to verify.
Let the eval decide. We measure routing accuracy: did the tools used match required_modalities? If the eval shows misroutes, we add more deterministic logic exactly where it fails.






1. tool calling agent rather than deterministic router 
    - queries may req both sources 
    - words in query may not reliably indicate source 
    - no data to tune router 

2. deterministic checks 
    - router agent may take shortcuts 
    - deterministic pre pass 
    - coverage check before agent answers 

3. inject schema into prompt 
    - model may guess wrong column names and write broken sql 
    - need exact string matches for sql 


4. small child chunks for search (500 character chunk), big parent chunks for readings 

5. how we converted pdf to md without breaking headings or tables 

6. hybrid search (need explanation)

7. force tool call on first turn 
    - make sure llm does not answer from its training memory and only from corpus 

8. temp 0 (always take most likely token no deviation in answers) and fixed seed 

9. can have one loop with parallel tool calls but not parallel runs
    - given multi step questions that are sequential -> parallel agents cant pass the results along 

10. simple conversation memory kept in ui (recent turns)
    - follow up questions work but api stays stateless
    - The API stays stateless. The grader sends its hidden questions one after another. If the server remembered question 3 while answering question 4, earlier answers could leak in and confuse it. Stateless means every question gets graded on its own.
    
    - but The UI keeps a little history. A human analyst will naturally ask follow-ups, so the chat page passes the last few turns along with each new question

11. gradio for ui 

12. no asking clarification questions (agent)
    - this will fail evals 
    - just state assumption and answer anyway 

13. no falling back to web search 
14. no llm as a relevance grader - why 
    - in tool calling loop agent can already see what came back and search again 

15. why are we not using LangGraph 

16. no context compression - fireworks models have 128k ++ context window so 

17. One risk: developing with glm-5p3 all through Day 2–3 could unfairly favour it. If I tune prompts until it works, they may suit its quirks. To guard against that:

Keep prompts generic, with no model-specific tricks.
Run a second model occasionally during development to catch prompt bias early.




#search decisions 

1. filter by company and year 
2. hybrid search to pick results 
    - top 30 chunks from bm25 + top 30 from embeddings -> merge using RRF -> reranker to rescored merged top 30 -> agent gets top 6 chunks 

3. keyword search -> lowercase, split on punctuation, keep numbers, no word stemming 

4. each result -> chunk id, citation, section label, chunk text, parent id 



#tools 


1. query_sql 
    - read only, errors go back to agent to fix query 
    - llms miscount zeros -> put commas in large numbers (40,000,000)

2. search_filings -> returns top 6 results 


3. read_section 
    - parent_id mode
    - ticker + fiscal_year + item mode 
        - capped at 40k characters (trade-off between answer completeness and cost/speed)

4. calculate 
    - takes several math expressions at once -> one call can do all comparisons -> saves agent turns 



#system prompt 

1. role, db schema, segment region and year coverage,
data caveats 
routing rules - The database is for the figures it holds.
The filings are for explanations, plus numbers the database doesn't have (YouTube, Search, Azure, capex…).
"Why" or "explain" questions need both.
If the two sources conflict, say so and prefer the newer filing.

math rule - all derived number must come from calc or sql 


2. answer 
    - first sentence is direct ans then explain 
    - sources 
    - assumptions if any stated


#agent 

1. budget 
    - max 8 tool calls and 10 llm turns (lets see eval distribution)

2. first turn must call tool 
3. pre pass hints 
4. coverage nudges (filing or number nudge if not done)

5. fallback when budget out -> final llm call w no tools to ans and say what missing 

6. context limits - need to justify 

7. output - ans, sources, trace, usage 