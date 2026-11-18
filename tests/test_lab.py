import concurrent.futures
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from tests.support import ProjectDirectory
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "lab.py"
spec = importlib.util.spec_from_file_location("lab", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Lab = module.Lab
THREAD = "研究主担当-A"
OTHER = "研究主担当-B"


class LabTest(unittest.TestCase):
    def setUp(self):
        self.temp = ProjectDirectory()
        self.root = Path(self.temp.name)
        (self.root / "result.txt").write_text("measurement: 12 seconds", encoding="utf-8")
        self.lab = Lab(self.root)
        self.proposal = dict(problem="準備の重複 🔬", change="入力を再利用", benefit="準備時間を比較",
                             cost="CPU上での小変更", evidence=["result.txt"])

    def tearDown(self):
        self.lab.close()
        self.temp.cleanup()

    def test_prepared_and_paused_do_not_deliver(self):
        self.lab.propose(self.proposal)
        self.assertFalse(self.lab.delivery()["ready"])
        self.lab.activate(THREAD)
        self.assertTrue(self.lab.delivery()["ready"])
        self.lab.pause()
        self.assertFalse(self.lab.delivery()["ready"])

    def test_single_lead_and_explicit_pause_before_rebind(self):
        self.lab.activate(THREAD)
        self.lab.activate(THREAD)
        with self.assertRaises(ValueError):
            self.lab.activate(OTHER)
        with self.assertRaises(ValueError):
            self.lab.activate(THREAD, "other-host")
        self.lab.pause()
        self.lab.activate(OTHER)
        self.assertEqual(self.lab.status()["thread_id"], OTHER)

    def test_proposal_delivery_decision_outcome(self):
        identifier = self.lab.propose(self.proposal)["id"]
        self.lab.activate(THREAD)
        self.assertEqual(len(self.lab.delivery()["proposals"]), 1)
        self.lab.delivered(identifier, THREAD, "local")
        self.assertFalse(self.lab.delivery()["ready"])
        self.assertEqual(len(self.lab.proposals(pending=True)), 1)
        self.lab.decide(identifier, "accept", "小さい変更で検証できる")
        self.lab.outcome(identifier, "準備時間が12秒から4秒になった（合成テスト）")
        self.assertEqual(self.lab.proposals(pending=True), [])
        self.assertIn("4秒", self.lab.proposals()[0]["outcome"])

    def test_duplicate_and_changed_evidence(self):
        first = self.lab.propose(self.proposal)
        again = self.lab.propose(self.proposal)
        self.assertEqual(first["id"], again["id"])
        self.assertTrue(again["duplicate"])
        (self.root / "result.txt").write_text("measurement: 25 seconds", encoding="utf-8")
        changed = self.lab.propose(self.proposal)
        self.assertNotEqual(first["id"], changed["id"])

    def test_invalid_evidence_is_rejected(self):
        for evidence in ([], ["absent.txt"], [str(SCRIPT)], [23]):
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                self.lab.propose(dict(self.proposal, evidence=evidence))
        self.assertEqual(self.lab.proposals(), [])

    def test_stale_delivery_cannot_be_acknowledged(self):
        identifier = self.lab.propose(self.proposal)["id"]
        self.lab.activate(THREAD)
        with self.assertRaises(ValueError):
            self.lab.delivered(identifier, OTHER, "local")
        self.lab.pause()
        with self.assertRaises(ValueError):
            self.lab.delivered(identifier, THREAD, "local")
        self.assertIsNone(self.lab.proposals()[0]["delivered_at"])

    def test_failed_delivery_remains_available(self):
        self.lab.propose(self.proposal)
        self.lab.activate(THREAD)
        # No acknowledgement if the external send failed.
        self.assertEqual(self.lab.delivery(), self.lab.delivery())
        self.assertTrue(self.lab.delivery()["ready"])

    def test_rejected_and_deferred_are_not_renotified(self):
        self.lab.activate(THREAD)
        identifier = self.lab.propose(self.proposal)["id"]
        for decision in ("defer", "reject"):
            self.lab.decide(identifier, decision, "今回は優先しない")
            self.assertFalse(self.lab.delivery()["ready"])
        self.assertEqual(self.lab.propose(self.proposal)["decision"], "reject")
        with self.assertRaises(ValueError):
            self.lab.outcome(identifier, "not adopted")

    def test_concurrent_proposals_keep_one_copy(self):
        def submit(_):
            instance = Lab(self.root)
            try:
                return instance.propose(self.proposal)["id"]
            finally:
                instance.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            identifiers = list(pool.map(submit, range(8)))
        self.assertEqual(len(set(identifiers)), 1)

    def test_record_keeps_evidence_hash_and_cost(self):
        data = {"kind": "cost", "summary": "合成の費用記録", "evidence": ["result.txt"],
                "resources": {"cost": 0, "currency": "USD"}}
        self.lab.record(data)
        payload = self.lab.records()[0]["payload"]
        self.assertEqual(len(payload["evidence"][0]["sha256"]), 64)
        self.assertEqual(payload["resources"]["cost"], 0)

    def test_wait_reason_persists_and_resets_on_resume(self):
        self.lab.hold("次の対象を相談する")
        self.lab.close()
        self.lab = Lab(self.root)
        self.assertEqual(self.lab.status()["waiting_reason"], "次の対象を相談する")
        self.lab.activate(THREAD)
        self.assertIsNone(self.lab.status()["waiting_reason"])

    def test_invalid_record_leaves_no_record_or_event(self):
        for change in ({"evidence": []}, {"kind": "wrong"}, {"summary": " "}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.lab.record(dict(kind="experiment", summary="試験", evidence=["result.txt"]) | change)
        self.assertEqual(self.lab.records(), [])
        self.assertEqual(self.lab.events(), [])

    def test_parallel_activation_keeps_single_lead(self):
        def activate(identifier):
            instance = Lab(self.root)
            try:
                try:
                    instance.activate(identifier)
                    return True
                except ValueError:
                    return False
            finally:
                instance.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(activate, [THREAD, OTHER]))
        self.assertEqual(results.count(True), 1)
        self.assertEqual(len([e for e in self.lab.events() if e["action"] == "activate"]), 1)

    def test_cli_roundtrip_and_bad_input_exit(self):
        source = self.root / "proposal.json"
        source.write_text(json.dumps(self.proposal, ensure_ascii=False), encoding="utf-8-sig")
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        added = subprocess.run(command + ["propose", "--file", str(source)], capture_output=True,
                               encoding="utf-8", check=True)
        identifier = json.loads(added.stdout)["id"]
        inbox = subprocess.run(command + ["inbox"], capture_output=True, encoding="utf-8", check=True)
        self.assertEqual(json.loads(inbox.stdout)[0]["id"], identifier)
        failed = subprocess.run(command + ["activate", "--thread", " "], capture_output=True,
                                encoding="utf-8")
        self.assertEqual(failed.returncode, 2)
        self.assertEqual(self.lab.status()["phase"], "prepared")


if __name__ == "__main__":
    unittest.main()
