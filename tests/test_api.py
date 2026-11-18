import json
from pathlib import Path
from tests.support import ProjectDirectory
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from app import ResearchServer


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.temp = ProjectDirectory()
        self.root = Path(self.temp.name)
        (self.root / "根拠.txt").write_text("符号つき面積: 0.5 🔬", encoding="utf-8")
        self.server = ResearchServer(("127.0.0.1", 0), self.root)
        self.thread = threading.Thread(target=self.server.serve_forever, kwargs={"poll_interval": 0.01})
        self.thread.start()
        self.base = self.server.origin
        self.proposal = {"problem": "反転数だけでは不十分", "change": "重なりも検査", "benefit": "比較の信頼性",
                         "cost": "小さなCPU計算", "evidence": ["根拠.txt"]}

    def tearDown(self):
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()
        self.temp.cleanup()

    def request(self, path, data=None, headers=None, raw=None):
        actual_headers = {"Content-Type": "application/json", "X-Lab-Token": self.server.token}
        actual_headers.update(headers or {})
        body = raw if raw is not None else (json.dumps(data, ensure_ascii=False).encode() if data is not None else None)
        request = Request(self.base + path, data=body, headers=actual_headers)
        try:
            response = urlopen(request, timeout=5)
        except HTTPError as exc:
            response = exc
        with response:
            text = response.read().decode()
            result = json.loads(text) if response.headers.get_content_type() == "application/json" else text
            return response.status, result

    def ok(self, path, data=None):
        code, result = self.request(path, data)
        self.assertEqual(code, 200, result)
        return result

    def activate(self):
        return self.ok("/api/activate", {"thread_id": "研究班-A", "host_id": "local"})

    def test_page_state_and_files(self):
        code, html = self.request("/")
        self.assertEqual(code, 200)
        self.assertIn("研究記録", html)
        self.assertIn(self.server.token, html)
        self.assertNotIn("__TOKEN__", html)
        self.assertNotIn("https://", html)
        state = self.ok("/api/state")
        self.assertEqual(state["status"]["phase"], "prepared")
        self.assertEqual(state["files"], ["根拠.txt"])
        self.assertEqual(self.ok("/api/files"), state["files"])
        self.assertEqual(self.ok("/api/events"), [])

    def test_state_transitions_and_lead_conflict(self):
        self.activate()
        code, result = self.request("/api/activate", {"thread_id": "another"})
        self.assertEqual(code, 400)
        self.assertIn("error", result)
        self.assertEqual(self.ok("/api/hold", {"reason": "研究対象の変更を相談"})["waiting_reason"], "研究対象の変更を相談")
        self.assertEqual(self.ok("/api/status")["phase"], "waiting")
        self.assertEqual(self.ok("/api/pause", {})["phase"], "paused")
        state = self.ok("/api/activate", {"thread_id": "another"})
        self.assertIsNone(state["waiting_reason"])
        self.assertEqual(state["thread_id"], "another")

    def test_record_evidence_and_events(self):
        r = self.ok("/api/record", {"kind": "verification", "summary": "最小例のみ確認", "claim_status": "verified",
                                     "evidence": ["根拠.txt"], "resources": {"cost": 0, "currency": "JPY"}})
        self.assertEqual(len(r["evidence"][0]["sha256"]), 64)
        records = self.ok("/api/records")
        self.assertEqual(records[0]["payload"]["evidence"], r["evidence"])
        self.assertEqual(self.ok("/api/events")[0]["action"], "record")
        from urllib.parse import quote
        current = self.ok("/api/evidence?path=" + quote("根拠.txt"))
        self.assertEqual(current["sha256"], r["evidence"][0]["sha256"])
        self.assertIn("0.5", current["text"])
        (self.root / "根拠.txt").write_text("changed", encoding="utf-8")
        self.assertNotEqual(self.ok("/api/evidence?path=" + quote("根拠.txt"))["sha256"], r["evidence"][0]["sha256"])

    def test_proposal_delivery_decision_outcome(self):
        identifier = self.ok("/api/propose", self.proposal)["id"]
        repeated = self.ok("/api/propose", self.proposal)
        self.assertTrue(repeated["duplicate"])
        self.assertEqual(identifier, repeated["id"])
        self.assertEqual(len(self.ok("/api/inbox")), 1)
        self.assertFalse(self.ok("/api/delivery")["ready"])
        self.activate()
        self.assertTrue(self.ok("/api/delivery")["ready"])
        self.assertEqual(self.request("/api/delivered", {"id": identifier, "thread_id": "wrong", "host_id": "local"})[0], 400)
        self.ok("/api/delivered", {"id": identifier, "thread_id": "研究班-A", "host_id": "local"})
        self.assertFalse(self.ok("/api/delivery")["ready"])
        self.assertEqual(len(self.ok("/api/inbox")), 1)  # Delivery is separate from decision.
        self.assertEqual(self.request("/api/outcome", {"id": identifier, "result": "too early"})[0], 400)
        for decision in ("defer", "reject", "accept"):
            self.ok("/api/decide", {"id": identifier, "decision": decision, "reason": "比較条件を確認"})
            self.assertEqual(self.ok("/api/inbox"), [])
        self.ok("/api/outcome", {"id": identifier, "result": "周辺面との交差も検査できた"})
        self.assertIn("交差", self.ok("/api/history")[0]["outcome"])
        actions = [e["action"] for e in self.ok("/api/events")]
        self.assertEqual(actions.count("propose"), 1)
        self.assertIn("outcome", actions)

    def test_heartbeat_busy_input_wait_target_reservation_and_pause(self):
        self.activate()
        snapshot = {"thread_id": "研究班-A", "host_id": "local", "idle": False, "needs_input": False}
        self.assertEqual(self.ok("/api/heartbeat", snapshot)["reason"], "not_idle")
        snapshot["idle"] = True
        self.assertEqual(self.ok("/api/heartbeat", dict(snapshot, needs_input=True))["reason"], "needs_input_or_unknown")
        self.assertEqual(self.ok("/api/heartbeat", dict(snapshot, thread_id="wrong"))["reason"], "wrong_target")
        result = self.ok("/api/heartbeat", snapshot)
        self.assertTrue(result["ready"])
        self.assertFalse(result["sent"])
        self.assertEqual(result["reason"], "reserved")
        self.assertEqual(self.ok("/api/heartbeat", snapshot)["reason"], "already_attempted")
        self.ok("/api/hold", {"reason": "本人判断"})
        self.assertEqual(self.ok("/api/heartbeat", snapshot)["reason"], "waiting")
        self.ok("/api/pause", {})
        self.assertEqual(self.ok("/api/heartbeat", snapshot)["reason"], "paused")

    def test_validation_errors_do_not_mutate_records_or_proposals(self):
        cases = [
            ("/api/record", {"kind": "experiment", "summary": "missing evidence"}),
            ("/api/record", {"kind": "invalid", "summary": "invalid", "evidence": ["根拠.txt"]}),
            ("/api/record", {"kind": "experiment", "summary": "invalid", "claim_status": "made_up", "evidence": ["根拠.txt"]}),
            ("/api/propose", dict(self.proposal, evidence=["../outside.txt"])),
            ("/api/propose", dict(self.proposal, evidence=[str(Path(__file__).resolve())])),
            ("/api/propose", dict(self.proposal, evidence=[])),
            ("/api/propose", dict(self.proposal, cost=" ")),
            ("/api/activate", {"thread_id": " "}),
            ("/api/activate", {"thread_id": 123}),
            ("/api/hold", {"reason": None}),
            ("/api/decide", {"id": "none", "decision": "accept", "reason": " "}),
            ("/api/outcome", {"id": "none", "result": " "}),
            ("/api/heartbeat", {"thread_id": "A", "host_id": "local", "idle": "false", "needs_input": False}),
        ]
        for path, data in cases:
            with self.subTest(path=path, data=data):
                code, result = self.request(path, data)
                self.assertEqual(code, 400)
                self.assertIn("error", result)
        self.assertEqual(self.ok("/api/records"), [])
        self.assertEqual(self.ok("/api/history"), [])
        self.assertEqual(self.ok("/api/status")["phase"], "prepared")

    def test_bad_json_routes_and_local_request_guards(self):
        for raw in (b"{bad", b"[]", b"null", b'{"value":NaN}', b"\xff"):
            with self.subTest(raw=raw):
                self.assertEqual(self.request("/api/propose", raw=raw)[0], 400)
        self.assertEqual(self.request("/api/pause", {}, headers={"X-Lab-Token": "wrong"})[0], 403)
        self.assertEqual(self.request("/api/pause", {}, headers={"Origin": "https://other.invalid"})[0], 403)
        self.assertEqual(self.request("/api/pause", {}, headers={"Host": "other.invalid"})[0], 403)
        self.assertEqual(self.request("/api/status", headers={"Host": "other.invalid"})[0], 403)
        self.assertEqual(self.request("/api/pause", {}, headers={"Content-Type": "text/plain"})[0], 400)
        self.assertEqual(self.request("/api/missing")[0], 404)
        self.assertEqual(self.request("/api/missing", {})[0], 404)
        self.assertEqual(self.request("/api/evidence?path=runtime/lab.sqlite3")[0], 400)
        self.assertEqual(self.request("/../../app.py")[0], 404)
        self.assertEqual(self.ok("/api/status")["phase"], "prepared")

    def test_image_evidence_and_missing_file(self):
        png = b"\x89PNG\r\n\x1a\n" + b"\0" * 16
        (self.root / "図.png").write_bytes(png)
        evidence = self.ok("/api/evidence?path=%E5%9B%B3.png")
        self.assertTrue(evidence["image"])
        self.assertEqual(evidence["text"], "")
        request = Request(self.base + "/api/raw?path=%E5%9B%B3.png")
        with urlopen(request, timeout=5) as response:
            self.assertEqual(response.headers.get_content_type(), "image/png")
            self.assertEqual(response.read(), png)
        code, result = self.request("/api/raw?path=%E6%A0%B9%E6%8B%A0.txt")
        self.assertEqual(code, 400)
        self.assertIn("画像", result["error"])
        code, result = self.request("/api/evidence?path=gone.md")
        self.assertEqual(code, 400)
        self.assertIn("同梱していません", result["error"])
        code, result = self.request("/api/raw?path=runtime/lab.sqlite3")
        self.assertEqual(code, 400)
        self.assertNotIn("同梱していません", result["error"])


if __name__ == "__main__":
    unittest.main()
