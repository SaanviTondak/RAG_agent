"""Eval plumbing without judge calls: alternative graders, failure causes, faithfulness evidence, editor section.

  python -m unittest tests.test_eval -v
"""

import unittest
from unittest import mock

from eval import failures, graders, robustness, run_eval

NUMERIC = {"id": "n", "evaluation": "fuzzy_numeric", "gold_answer": "$1.0 billion", "level": 1}
JUDGED = {"id": "j", "evaluation": "llm_judge", "gold_answer": " ".join(["word"] * 20), "level": 4}
ENTITY = {"id": "e", "evaluation": "exact_match_entity", "gold_answer": "Alphabet", "level": 2}


def facts(*verdicts):
    return {"facts": [{"verdict": v} for v in verdicts]}


def score(passed=True, sc=1.0, details=None, **kw):
    s = {"id": "j", "run": 0, "pass": passed, "score": sc, "reason": "r", "details": details or {}, "words": 100,
         "routing": {"ok": True, "missing": [], "extra": [], "used": []}, "recall": None,
         "grounding": {"ok": True, "ungrounded": []}, "lead": None, "faithfulness": None}
    return {**s, **kw}


class AlternativeGraders(unittest.TestCase):
    def test_strict_and_lenient(self):
        five = facts("covered", "covered", "covered", "covered", "missing")  # 80%: passes ours, fails strict
        self.assertFalse(robustness.strict(JUDGED, score(sc=0.8, details=five)))
        self.assertTrue(robustness.lenient(JUDGED, score(sc=0.8, details=five)))
        contradicted = facts("covered", "covered", "covered", "contradicted")
        self.assertFalse(robustness.lenient(JUDGED, score(False, 0.75, contradicted)))
        self.assertFalse(robustness.strict(NUMERIC, score(details={"first_sentence_pass": False})))
        self.assertFalse(robustness.strict(ENTITY, score(details={"string_check_ok": False})))


class NumericGrader(unittest.TestCase):
    """Regression cases from an outside review (Codex): wrong unit, reversed direction, wrong headline figure."""
    RAW = 416161000000

    def scan(self, answer, gold, unit):
        return graders.fuzzy_numeric(answer, gold, unit)["pass"]

    def test_units_and_direction(self):
        cases = [("Revenue was $416.2 billion.", self.RAW, "usd", True),
                 ("Revenue was $416.2 million.", self.RAW, "usd", False),
                 ("Revenue was $416,161 million.", self.RAW, "usd", True),
                 ("It was $416.2 million.", 416.2, "pct", False),
                 ("The share was 51.3%.", 51.3, "pct", True),
                 ("Services brought in $51.3 billion.", 51.3, "pct", False),
                 ("Revenue grew 15.1%.", 15.1, "pct", True),
                 ("Revenue grew -15.1%.", 15.1, "pct", False),
                 ("Revenue fell 15.1%.", 15.1, "pct", False),
                 ("Diluted EPS was $10.81.", 10.81, "plain", True),
                 ("Diluted EPS rose 10.81%.", 10.81, "plain", False),
                 ("The current ratio was 2.01.", 2.01, "plain", True),
                 ("Greater China fell 3.8%.", -3.8, "pct", True),
                 ("Greater China changed 3.8%.", -3.8, "pct", False)]
        for answer, gold, unit, want in cases:
            self.assertEqual(self.scan(answer, gold, unit), want, answer)

    def judged(self, answer, figure, negative=False, gold=RAW, unit="usd"):
        with mock.patch.object(graders, "judge_json", lambda *a, **k: ({"figure": figure, "negative": negative}, None)):
            return graders.fuzzy_numeric(answer, gold, unit, "q", "judge")

    def test_the_figure_given_as_the_answer_decides(self):
        wrong_headline = "Apple's revenue was $391.0 billion, up from $416.2 billion."
        g = self.judged(wrong_headline, "$391.0 billion")
        self.assertFalse(g["pass"])
        self.assertTrue(g["details"]["scan_pass"] and g["details"]["checks_disagree"])
        self.assertTrue(self.judged("Revenue was $416.2 billion, up from $391.0 billion.", "$416.2 billion")["pass"])
        self.assertFalse(self.judged("Revenue fell 15.1%.", "15.1%", negative=True, gold=15.1, unit="pct")["pass"])
        self.assertFalse(self.judged("No figure is available.", "")["pass"])

    def test_gold_units_are_read_from_the_gold_answer(self):
        self.assertEqual(graders.gold_unit({"gold_answer_numeric": self.RAW, "gold_answer": "$416.2 billion"}), "usd")
        self.assertEqual(graders.gold_unit({"gold_answer_numeric": 51.3, "gold_answer": "51.3%"}), "pct")
        self.assertEqual(graders.gold_unit({"gold_answer_numeric": 10.81, "gold_answer": "$10.81"}), "plain")


class EvidenceBookkeeping(unittest.TestCase):
    """Outside review (Codex): passages cut from a tool result were counted as seen; a citation range passed if any
    one of its pages had been seen."""

    def test_citation_range_needs_every_page(self):
        r = {"answer": "AAPL FY2025 10-K, pp.24-999; AAPL FY2025 10-K, p.24", "trace": [],
             "sources": [{"type": "section", "doc": "AAPL_FY2025_10-K", "page_start": 24, "page_end": 24}]}
        invalid = graders.citation_check(r)["invalid"]
        self.assertEqual(len(invalid), 1)
        self.assertTrue(invalid[0].startswith("AAPL FY2025 10-K, pp.24-999"))

    def test_search_records_only_passages_sent(self):
        from app import tools
        hit = {"id": "c", "parent_id": "p", "doc": "AAPL_FY2025_10-K", "page": 1, "ticker": "AAPL", "fiscal_year": 2025,
               "item": "1A", "item_title": "Risk Factors", "section": "s", "is_table": False, "score": 1.0,
               "text": "x" * 5000}
        index = mock.Mock()
        index.search.return_value = [dict(hit, id=f"c{i}", page=i) for i in range(1, 7)]
        with mock.patch.object(tools, "get_index", lambda: index):
            text, meta = tools.search_filings("q")
        self.assertLessEqual(len(text), tools.RESULT_CHARS)
        self.assertEqual(len(meta["hits"]), text.count("[") - text.count("[["))
        self.assertLess(len(meta["hits"]), 6)
        self.assertTrue(text.endswith("x"), "cut only between whole passages")


class FailureCauses(unittest.TestCase):
    trace = {"trace": []}

    def test_causes_in_order(self):
        cases = [
            (score(False, reason="grader error: x"), JUDGED, "grader error"),
            (score(False, routing={"ok": False, "missing": ["pdf"], "extra": [], "used": []}), JUDGED,
             "routing: never used pdf"),
            (score(False, recall={"hit": False, "recall": 0.0, "n_gold": 2}), JUDGED, "retrieval: no gold page"),
            (score(False, 0.5, facts("covered", "contradicted")), JUDGED, "wrong fact"),
            (score(False, 0.5, facts("covered", "missing"), recall={"hit": True, "recall": 0.5, "n_gold": 4}), JUDGED,
             "partial retrieval: 2 of 4"),
            (score(False, 0.5, facts("covered", "missing"), recall={"hit": True, "recall": 1.0, "n_gold": 1}), JUDGED,
             "omission: every gold page seen"),
            (score(False, 0.0, {"entity_ok": False}), ENTITY, "wrong company"),
            (score(False, 0.0, grounding={"ok": False, "ungrounded": ["3.4%"]}), NUMERIC, "calculation"),
        ]
        for s, q, want in cases:
            self.assertTrue(failures.suggest(q, s, self.trace).startswith(want), (want, failures.suggest(q, s, self.trace)))
        self.assertTrue(failures.suggest(JUDGED, score(False), {"trace": [{"type": "fallback"}]}).startswith("budget"))


class Faithfulness(unittest.TestCase):
    result = {"answer": "a", "trace": [{"type": "tool", "tool": "query_sql", "args": "{}", "result": "TOOL_OUTPUT",
                                        "meta": {}}]}

    def test_evidence_has_data_notes_history_and_tools(self):
        text, truncated = graders.evidence_text(self.result, [{"role": "user", "content": "earlier q"}])
        self.assertIn("Fiscal year ends", text)
        self.assertIn("Hedging gains", text)
        self.assertLess(text.index("earlier q"), text.index("TOOL_OUTPUT"))
        self.assertFalse(truncated)
        with mock.patch.object(graders, "FAITH_MAX_CHARS", 50):
            self.assertTrue(graders.evidence_text(self.result)[1])

    def test_grade_sums_judge_cost_and_can_skip_faithfulness(self):
        usage = {"prompt_tokens": 1, "completion_tokens": 1, "cached_tokens": 0, "cost_usd": 0.5}
        g = {"pass": True, "score": 1.0, "reason": "", "details": {}, "judge_usage": usage}
        with mock.patch.object(graders, "grade_answer", lambda *a: g), \
                mock.patch.object(graders, "lead_check", lambda *a: {"judge_usage": usage}), \
                mock.patch.object(graders, "faithfulness", lambda *a: {"judge_usage": usage, "ok": True}):
            q = {**JUDGED, "question": "q", "required_modalities": []}
            r = {**self.result, "sources": []}
            self.assertEqual(graders.grade(q, r, "m", {})["judge_usage"]["cost_usd"], 1.5)
            no_faith = graders.grade(q, r, "m", {}, faith=False)
        self.assertIsNone(no_faith["faithfulness"])
        self.assertEqual(no_faith["judge_usage"]["cost_usd"], 1.0)


class EditorSection(unittest.TestCase):
    def test_paired_counts(self):
        edit = {"type": "edit", "fallback": None}
        rows = [  # edited, draft passed, edit failed / edited, both passed / not edited (short)
            (JUDGED, score(False, 0.6, words=50, draft={"pass": True, "score": 1.0, "words": 120,
                                                       "faithfulness": None}), {"trace": [edit]}),
            (JUDGED, score(True, 1.0, words=60, draft={"pass": True, "score": 1.0, "words": 100,
                                                      "faithfulness": {"ok": False}}), {"trace": [edit]}),
            (NUMERIC, score(True), {"trace": []}),
        ]
        md = "\n".join(run_eval.editor_section(rows))
        self.assertIn("| Passed (all answers) | 3/3 | 2/3 |", md)
        self.assertIn("Draft passed, edited failed: j#0.", md)
        self.assertIn("| Edited answers with an unsupported or contradicted claim | 1/2 | 0/2 |", md)
        self.assertIn("Edited 2/3", md)
        self.assertEqual(run_eval.editor_section([(NUMERIC, score(), {"trace": []})]), [])


if __name__ == "__main__":
    unittest.main()
