"""API contract tests with a fake agent (no Fireworks calls, no cost).

  python -m unittest tests.test_server -v
"""

import json
import time
import unittest
from pathlib import Path
from unittest import mock

from fastapi.testclient import TestClient

from app import server
from app.llm import DeadlineExceeded, ProviderError

FIXTURE = json.loads((Path(__file__).parent / "fixtures" / "agent_result_q012.json").read_text())
QUESTION = {"question": FIXTURE["question"]}


def fake_run(question, history=None, on_step=None, **_):
    for step in FIXTURE["trace"]:
        if on_step:
            on_step(step)
    return FIXTURE


def failing(exc):
    def run(*_, **__):
        raise exc
    return run


def sse_events(text: str) -> list[tuple[str, dict]]:
    events = []
    for block in text.strip().split("\n\n"):
        lines = [l for l in block.splitlines() if not l.startswith(":")]
        if lines:
            event = next(l[7:] for l in lines if l.startswith("event: "))
            data = json.loads(next(l[6:] for l in lines if l.startswith("data: ")))
            events.append((event, data))
    return events


class ChatAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(server.app)
        cls.client.__enter__()  # runs the startup (index load)

    @classmethod
    def tearDownClass(cls):
        cls.client.__exit__(None, None, None)

    def post(self, run=fake_run, stream=False, **kw):
        headers = {"Accept": "text/event-stream"} if stream else {}
        with mock.patch.object(server.agent, "run", run):
            return self.client.post("/api/chat", json=kw or QUESTION, headers=headers)

    def test_json_has_answer_content_sources_steps_usage(self):
        r = self.post()
        self.assertEqual(r.status_code, 200)
        d = r.json()
        self.assertEqual(d["answer"], FIXTURE["answer"])
        self.assertEqual(d["content"], d["answer"])
        cites = [s["citation"] for s in d["sources"]]
        self.assertIn("AAPL FY2025 10-K, p.24", cites)
        self.assertIn("/pdfs/AAPL_FY2025_10-K.pdf#page=24", [s.get("url") for s in d["sources"]])
        self.assertTrue(any(s["type"] == "sql" for s in d["sources"]))
        self.assertTrue(d["steps"] and all(s["label"] for s in d["steps"]))
        self.assertGreater(d["usage"]["latency_s"], 0)

    def test_sse_events_in_order_and_answer_is_content_only(self):
        r = self.post(stream=True)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.headers["content-type"].startswith("text/event-stream"))
        events = sse_events(r.text)
        names = [e for e, _ in events]
        self.assertGreater(names.count("step"), 0)
        self.assertEqual(names[-3:], ["answer", "sources", "done"])
        self.assertEqual(events[-3][1], {"content": FIXTURE["answer"]})

    def test_stream_query_param(self):
        with mock.patch.object(server.agent, "run", fake_run):
            r = self.client.post("/api/chat?stream=true", json=QUESTION)
        self.assertIn("answer", [e for e, _ in sse_events(r.text)])

    def test_bad_requests_are_422(self):
        for body in ({}, {"question": ""}, {"question": "   "}, {"question": "x", "history": [{"role": "bot", "content": "y"}]}):
            with self.subTest(body=body):
                self.assertEqual(self.client.post("/api/chat", json=body).status_code, 422)

    def test_failures_get_honest_status_codes(self):
        for exc, status in ((ProviderError("down"), 502), (DeadlineExceeded("slow"), 504), (KeyError("bug"), 500)):
            with self.subTest(exc=type(exc).__name__):
                r = self.post(failing(exc))
                self.assertEqual(r.status_code, status)
                self.assertIn("error", r.json())
                self.assertNotIn("answer", r.json())

    def test_stream_failure_is_error_event(self):
        events = sse_events(self.post(failing(ProviderError("down")), stream=True).text)
        self.assertEqual(events[-1][0], "error")
        self.assertEqual(events[-1][1]["status"], 502)
        self.assertNotIn("answer", [e for e, _ in events])

    def test_hard_timeout_backstop(self):
        def slow(*_, **__):
            time.sleep(1.5)
            return FIXTURE
        with mock.patch.object(server, "HARD_TIMEOUT_S", 0.3):
            self.assertEqual(self.post(slow).status_code, 504)
            events = sse_events(self.post(slow, stream=True).text)
        self.assertEqual(events[-1], ("error", {"status": 504, "error": events[-1][1]["error"]}))

    def test_history_keeps_last_three_exchanges_without_sources_lines(self):
        seen = {}

        def capture(question, history=None, **_):
            seen["history"] = history
            return FIXTURE
        turns = []
        for i in range(5):
            turns += [{"role": "user", "content": f"q{i}"}, {"role": "assistant", "content": f"a{i}\n\nSources: [SQL: x]"}]
        self.post(capture, question="and Microsoft?", history=turns)
        self.assertEqual(len(seen["history"]), 6)
        self.assertEqual(seen["history"][0]["content"], "q2")
        self.assertNotIn("Sources", seen["history"][-1]["content"])

    def test_health_ui_and_pdfs(self):
        self.assertEqual(self.client.get("/api/health").json()["status"], "ok")
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("text/html", page.headers["content-type"])
        pdf = self.client.get("/pdfs/AAPL_FY2025_10-K.pdf")
        self.assertEqual(pdf.status_code, 200)
        self.assertEqual(pdf.headers["content-type"], "application/pdf")


if __name__ == "__main__":
    unittest.main()
