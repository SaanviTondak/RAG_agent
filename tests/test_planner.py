"""Planner: the gate, plan parsing, and how the agent uses a plan (fake model, no Fireworks calls).

  python -m unittest tests.test_planner -v
"""

import json
import unittest
from types import SimpleNamespace
from unittest import mock

from app import agent, planner
from app.llm import ProviderError
from eval.run_eval import load_set

# Hand labels on the tuning questions: multi-part = two or more distinct asks, or a step that needs another step's
# result. Holdout questions are deliberately not used (an earlier version tuned the gate on them too; the planner
# is off by default, so no headline result depended on it).
MULTI = {"q_011", "q_012", "q_014", "q_017", "q_022", "q_025", "x_007", "x_013", "x_020", "x_021", "x_022",
         "x_025", "x_028", "x_033", "x_035", "x_036", "x_037", "x_038", "x_039", "x_041",
         "x_042", "x_043", "x_045", "x_047", "x_048", "x_049"}


def response(content="", tool_calls=None):
    msg = SimpleNamespace(content=content, tool_calls=tool_calls)
    return SimpleNamespace(choices=[SimpleNamespace(message=msg, finish_reason="stop")], usage=None)


PLAN_JSON = json.dumps({"sub_questions": [
    {"ask": "Find the company with the highest R&D share", "source": "database", "depends_on": []},
    {"ask": "What its 10-K says about AI investment", "source": "filings", "depends_on": [1]},
    {"ask": "", "source": "x"}, {"ask": "Bad deps", "source": "weird", "depends_on": [9, "a"]}]})


class Gate(unittest.TestCase):
    def test_gate_against_hand_labels(self):
        qs = load_set("tune")
        planned = {q["id"] for q in qs if planner.needs_plan(q["question"])}
        self.assertGreaterEqual(len(planned & MULTI) / len(MULTI), 0.9, "recall")
        self.assertGreaterEqual(len(planned & MULTI) / max(len(planned), 1), 0.9, "precision")

    def test_simple_lookups_are_not_planned(self):
        for q in ("What was Apple's total net revenue in fiscal year 2025?",
                  "How much did Alphabet spend repurchasing its shares in fiscal year 2025?",
                  "What risks does Alphabet's fiscal year 2025 10-K describe about its dependence on advertising revenue?"):
            self.assertFalse(planner.needs_plan(q), q)

    def test_dependent_and_multi_company_questions_are_planned(self):
        for q in ("How much did the company with the lowest current ratio spend on buybacks?",
                  "How do Microsoft's and Alphabet's 10-Ks describe AI costs?",
                  "Apple's revenue from Japan grew. By how much, and what drove it?"):
            self.assertTrue(planner.needs_plan(q), q)


class Planning(unittest.TestCase):
    def test_plan_parsing_cleans_steps(self):
        with mock.patch.object(planner, "chat", lambda **kw: response(PLAN_JSON)):
            steps, _ = planner.make_plan("q", "m")
        self.assertEqual([s["source"] for s in steps], ["database", "filings", "both"])
        self.assertEqual(steps[1]["depends_on"], [1])
        self.assertEqual(steps[2]["depends_on"], [])
        self.assertEqual(planner.required_sources(steps), {"database", "filings"})

    def test_bad_plan_json_gives_no_plan(self):
        with mock.patch.object(planner, "chat", lambda **kw: response("not json")):
            self.assertIsNone(planner.make_plan("q", "m")[0])

    def run_agent(self, question, plan_fn, chat_fn):
        with mock.patch.object(agent, "make_plan", plan_fn), mock.patch.object(agent, "chat", chat_fn), \
                mock.patch.object(agent, "_save_trace", lambda r: None):
            return agent.run(question, planner="auto", grounding_nudge=False)

    def test_plan_is_shown_injected_and_drives_the_routing_check(self):
        seen = []

        def chat(**kw):
            seen.append([dict(m) for m in kw["messages"]])
            return response("Alphabet, at 15.2%.")
        steps = [{"ask": "Find the company", "source": "database", "depends_on": []},
                 {"ask": "Read its 10-K on AI", "source": "filings", "depends_on": [1]}]
        q = "Which company spent the most on R&D relative to revenue, and how is it investing in AI?"
        r = self.run_agent(q, lambda *a, **k: (steps, None), chat)
        self.assertEqual(r["trace"][0]["type"], "plan")
        self.assertIn("1. Find the company (database)", seen[0][-1]["content"])
        nudges = [s["text"] for s in r["trace"] if s["type"] == "nudge"]
        self.assertTrue(any("searched the 10-Ks" in n for n in nudges), "plan needs filings, none searched")

    def test_simple_question_skips_planning(self):
        called = []
        r = self.run_agent("What was Apple's total net revenue in fiscal year 2025?",
                           lambda *a, **k: called.append(1) or (None, None), lambda **kw: response("$416.2 billion."))
        self.assertEqual(called, [])
        self.assertIsNone(r["plan"])

    def test_planner_failure_falls_back_to_no_plan(self):
        def boom(*a, **k):
            raise ProviderError("down")
        r = self.run_agent("Which company grew fastest, and why?", boom, lambda **kw: response("Microsoft."))
        self.assertIsNone(r["plan"])
        self.assertEqual(r["answer"], "Microsoft.")


if __name__ == "__main__":
    unittest.main()
