"""Answer editor and the "Plan first" switch, with a fake model (no Fireworks calls).

  python -m unittest tests.test_editor -v
"""

import json
import time
import unittest
from types import SimpleNamespace
from unittest import mock

from fastapi.testclient import TestClient

from app import agent, editor, server
from app.evidence import step_view
from app.llm import DeadlineExceeded, ProviderError

QUESTION = "Which risks does Apple's fiscal year 2025 10-K disclose about its supply chain?"
SOURCES = "Sources: [AAPL FY2025 10-K, p.10]"
DRAFT = ("Apple discloses several supply-chain risks, including single-source suppliers and concentration of "
         "manufacturing in Asia. " + "The 10-K explains at length how each of these could materially adversely affect "
         "the business, results of operations and financial condition. " * 8 + "Revenue was $416.2 billion.\n\n"
         + SOURCES)
SHORT = "Apple discloses supply-chain risks: single-source suppliers and manufacturing concentrated in Asia."


def response(content="", tool_calls=None):
    msg = SimpleNamespace(content=content, tool_calls=tool_calls)
    return SimpleNamespace(choices=[SimpleNamespace(message=msg, finish_reason="stop")], usage=None)


def edited(answer):
    return lambda **kw: response(json.dumps({"points": ["single-source suppliers"], "answer": answer}))


def raising(exc):
    def chat(**kw):
        raise exc
    return chat


class Editor(unittest.TestCase):
    def run_edit(self, chat_fn, draft=DRAFT, deadline=None):
        with mock.patch.object(editor, "chat", chat_fn):
            return editor.edit(QUESTION, draft, "m", deadline)

    def test_short_draft_is_not_sent(self):
        calls = []
        self.assertIsNone(self.run_edit(lambda **kw: calls.append(1), draft=SHORT))
        self.assertEqual(calls, [])

    def test_edit_is_used_and_keeps_the_sources_line(self):
        r = self.run_edit(edited(SHORT))
        self.assertIsNone(r["fallback"])
        self.assertEqual(r["answer"], SHORT + "\n\n" + SOURCES)

    def test_checks_keep_the_draft(self):
        cases = {"new numbers": SHORT + " Revenue was $500.0 billion.",
                 "not shorter": DRAFT.replace("\n\n" + SOURCES, " Extra words here."),
                 "empty": ""}
        for reason, answer in cases.items():
            r = self.run_edit(edited(answer))
            self.assertTrue(r["fallback"].startswith(reason), (reason, r["fallback"]))
            self.assertEqual(r["answer"], DRAFT)

    def test_the_company_the_answer_leads_with_must_stay_first(self):
        unnamed = "Which company discloses the most supply-chain risks?"
        no_company = "Several supply-chain risks are disclosed: single-source suppliers."
        self.assertTrue(editor.guard(unnamed, DRAFT, no_company)[1].startswith("first sentence lost"))
        self.assertIsNone(editor.guard(QUESTION, DRAFT, no_company)[1], "fine when the question names Apple")

    def test_bad_json_keeps_the_draft(self):
        r = self.run_edit(lambda **kw: response("not json"))
        self.assertEqual((r["fallback"], r["answer"]), ("empty", DRAFT))

    def test_timeout_or_provider_failure_keeps_the_draft(self):
        for exc in (DeadlineExceeded("late"), ProviderError("down")):
            r = self.run_edit(raising(exc))
            self.assertEqual((r["fallback"], r["answer"]), (type(exc).__name__, DRAFT))

    def test_no_call_when_the_time_budget_is_nearly_used(self):
        calls = []
        r = self.run_edit(lambda **kw: calls.append(1), deadline=time.time() + 2)
        self.assertEqual((r["fallback"], calls), ("no time left", []))


class AgentWithEditor(unittest.TestCase):
    def run_agent(self, edit_chat, **kw):
        with mock.patch.object(agent, "chat", lambda **k: response(DRAFT)), mock.patch.object(editor, "chat", edit_chat), \
                mock.patch.object(agent, "_save_trace", lambda r: None), mock.patch.object(agent, "TOOL_CUTOFF_S", 0):
            return agent.run(QUESTION, grounding_nudge=False, planner="off", editor=True, **kw)

    def test_edited_answer_is_returned_and_the_draft_kept(self):
        r = self.run_agent(edited(SHORT))
        self.assertEqual(r["answer"], SHORT + "\n\n" + SOURCES)
        self.assertEqual(r["draft"], DRAFT)
        step = next(s for s in r["trace"] if s["type"] == "edit")
        self.assertEqual(step_view(step)["label"], "Tightening the answer")

    def test_failed_edit_returns_the_draft_and_shows_no_step(self):
        r = self.run_agent(raising(ProviderError("down")))
        self.assertEqual((r["answer"], r["draft"]), (DRAFT, None))
        step = next(s for s in r["trace"] if s["type"] == "edit")
        self.assertIsNone(step_view(step))


class PlanFirst(unittest.TestCase):
    def test_planner_on_plans_even_a_simple_question(self):
        called = []
        with mock.patch.object(agent, "make_plan", lambda *a, **k: called.append(1) or (None, None)), \
                mock.patch.object(agent, "chat", lambda **kw: response("$416.2 billion.")), \
                mock.patch.object(agent, "_save_trace", lambda r: None):
            agent.run("What was Apple's total net revenue in fiscal year 2025?", planner="on", grounding_nudge=False,
                      editor=False)
        self.assertEqual(called, [1])

    def test_request_plan_field_sets_the_planner(self):
        seen = []

        def fake_run(question, history=None, on_step=None, **kw):
            seen.append(kw.get("planner"))
            return {"answer": "x", "sources": [], "trace": [], "model": "m",
                    "usage": {"latency_ms": 1, "llm_calls": 1, "tool_calls": 0, "prompt_tokens": 0,
                              "completion_tokens": 0, "cost_usd": 0}}
        with mock.patch.object(server.agent, "run", fake_run), mock.patch.object(server, "get_index"):
            client = TestClient(server.app)
            for body in ({"question": "q", "plan": True}, {"question": "q", "plan": False}, {"question": "q"}):
                self.assertEqual(client.post("/api/chat", json=body).status_code, 200)
            client.post("/api/chat?stream=true", json={"question": "q", "plan": True})
        self.assertEqual(seen, ["on", "off", None, "on"])


if __name__ == "__main__":
    unittest.main()
