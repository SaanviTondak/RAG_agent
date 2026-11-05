"""Fill gold_answer_numeric for extra questions from their gold_sql, and check the files are consistent.

  python -m eval.make_gold

Numeric gold is computed by SQL (never by hand or by the agent) and stored at full precision; the
grader's rounding rule handles the comparison. Also checks: every gold page exists in the index,
every entity question has gold_entities, and the written gold answer contains the computed figure.
"""

import json
import sqlite3

from app.config import DB_PATH
from eval.graders import _chunk_pages, fuzzy_numeric
from eval.run_eval import EVAL_DIR

PATH = EVAL_DIR / "extra_questions.json"
METHODS = {"fuzzy_numeric", "exact_match_entity", "llm_judge", "out_of_scope"}


def main() -> None:
    questions = json.loads(PATH.read_text())
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    pages = {(cid.split("#")[0], p) for cid, (start, end) in _chunk_pages().items() for p in range(start, end + 1)}
    problems = []
    for q in questions:
        if q.get("gold_sql"):
            rows = con.execute(q["gold_sql"]).fetchall()
            if len(rows) != 1 or rows[0][0] is None:
                problems.append(f"{q['id']}: gold_sql returned {rows}")
                continue
            q["gold_answer_numeric"] = rows[0][0]
        q.setdefault("gold_answer_numeric", None)
        g = q["gold_answer_numeric"]
        if q["evaluation"] not in METHODS:
            problems.append(f"{q['id']}: unknown evaluation {q['evaluation']}")
        if q["evaluation"] == "fuzzy_numeric" and g is None:
            problems.append(f"{q['id']}: fuzzy_numeric needs a numeric gold")
        if q["evaluation"] == "exact_match_entity" and not q.get("gold_entities"):
            problems.append(f"{q['id']}: exact_match_entity needs gold_entities")
        if g is not None and not fuzzy_numeric(q["gold_answer"], g)["pass"]:
            problems.append(f"{q['id']}: gold_answer text {q['gold_answer']!r} doesn't contain {g}")
        for gp in q.get("gold_pages", []):
            if (gp["doc"], gp["page"]) not in pages:
                problems.append(f"{q['id']}: gold page {gp} not in the index")
        print(f"{q['id']} [{q['split']:7}] {q['evaluation']:18} gold={g!s:>16}  {q['gold_answer'][:70]}")
    PATH.write_text("[\n" + ",\n".join("  " + json.dumps(q, ensure_ascii=False) for q in questions) + "\n]\n")
    splits = {s: sum(q["split"] == s for q in questions) for s in ("tune", "holdout")}
    print(f"\n{len(questions)} questions: {splits}")
    print("\n".join(["Problems:", *problems]) if problems else "No problems found.")


if __name__ == "__main__":
    main()
