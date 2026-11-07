"""Time-budget behaviour with a fake model (no Fireworks calls).

  python -m unittest tests.test_budget -v
"""

import time
import unittest
from types import SimpleNamespace
from unittest import mock

from app import agent, llm


def fake_response(content="The answer.", tool_calls=None):
    msg = SimpleNamespace(content=content, tool_calls=tool_calls)
    return SimpleNamespace(choices=[SimpleNamespace(message=msg, finish_reason="stop")], usage=None)


class TimeBudget(unittest.TestCase):
    def test_missing_key_is_reported_when_a_model_is_called(self):
        with mock.patch.object(llm, "FIREWORKS_API_KEY", ""), self.assertRaises(llm.MissingKeyError):
            llm._retry(lambda: None)

    def test_expired_deadline_raises_before_calling(self):
        calls = []
        with mock.patch.object(llm, "FIREWORKS_API_KEY", "test"), self.assertRaises(llm.DeadlineExceeded):
            llm._retry(lambda: calls.append(1), deadline=time.time() - 1)
        self.assertEqual(calls, [])

    def test_past_tool_cutoff_answers_from_evidence_without_tools(self):
        seen = []

        def chat(**kw):
            seen.append(kw["tool_choice"])
            return fake_response()
        with mock.patch.object(agent, "chat", chat), mock.patch.object(agent, "TOOL_CUTOFF_S", 0), \
                mock.patch.object(agent, "_save_trace", lambda r: None):
            r = agent.run("What was Apple's revenue in fiscal year 2025?")
        self.assertEqual(seen, ["none"])  # straight to the fallback call, tools not offered
        self.assertIn("fallback", [s["type"] for s in r["trace"]])
        self.assertEqual(r["usage"]["tool_calls"], 0)


if __name__ == "__main__":
    unittest.main()
