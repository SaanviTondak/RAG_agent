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
14. no llm as a grader - why 
    - in tool calling loop agent can already see what came back and search again 

15. why are we not using LangGraph 

16. no context compression - fireworks models have 128k ++ context window so 

17. One risk: developing with glm-5p3 all through Day 2–3 could unfairly favour it. If I tune prompts until it works, they may suit its quirks. To guard against that:

Keep prompts generic, with no model-specific tricks.
Run a second model occasionally during development to catch prompt bias early.