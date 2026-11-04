

#official given evals 

1. fuzzy nuemric -> correct number in answer?
1% tolerance - this is too loose a standard a number ideally should not devaite when being converted Pass if any of them is within 1% of the gold number. correct me if im wrong

2. exact match entity 
- reccomendation of winning company must be in the first sentence does not make sense what if the question is what are the two highest revenue companies?


3. llm judge 
    - split gold answer into individual facts chunks and compare with answer. answers score is percentage of gold answer match. passes at 80% and no contradiction

    - diff model family from answering model. 0 temp

4. human judges llm judge


#diagnostic metrics 

1. routing accuracy 
    - compare agent tool use to "required modalities"
    - missing source count as failure. extra source as over retrieval 

2. retrieval recall -> did the retrieved source find ans
    - recall@6 
    - either search on its own wihout llm(cheap) or during the full agent run 

3. grounding check 
    - catch made up citations 
    - check numbers come from where 
    - skip llm as faithfulness judge??

4. latency, cost, variance
    - p50 n p95 
    - token in and out and $ per question 
    - variance 

5. 









