import sys
from pathlib import Path
from tests.support import ProjectDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from lab import Lab
from heartbeat import tick

THREAD = "研究主担当-A"


class AtomicFake:
    def __init__(self, actual="idle"):
        self.actual = actual
        self.calls = 0
        self.sent = 0

    def wake_if_idle(self, control, prompt, key):
        self.calls += 1
        if self.actual != "idle":
            return "busy"
        self.sent += 1
        return "sent"


class HeartbeatTest(unittest.TestCase):
    def setUp(self):
        self.tmp = ProjectDirectory()
        self.lab = Lab(Path(self.tmp.name))
        self.lab.activate(THREAD)
        self.snapshot = dict(thread_id=THREAD, host_id="local", observed_at=3600,
                             status="idle", needs_input=False)

    def tearDown(self):
        self.lab.close()
        self.tmp.cleanup()

    def test_idle_once_per_slot(self):
        backend = AtomicFake()
        self.assertTrue(tick(self.lab, self.snapshot, backend, 3600)["sent"])
        self.assertFalse(tick(self.lab, self.snapshot, backend, 3601)["sent"])
        self.assertEqual(backend.sent, 1)

    def test_busy_does_not_call_sender(self):
        backend = AtomicFake()
        for status in ("active", "running", "unknown", "needsInput"):
            result = tick(self.lab, dict(self.snapshot, status=status), backend, 3600)
            self.assertFalse(result["sent"])
        self.assertEqual(backend.calls, 0)

    def test_stale_wrong_target_and_input_wait_skip(self):
        backend = AtomicFake()
        for changes in ({"observed_at": 3500}, {"thread_id": "other"},
                        {"needs_input": True}, {"needs_input": None}):
            self.assertFalse(tick(self.lab, dict(self.snapshot, **changes), backend, 3600)["sent"])
        self.assertEqual(backend.calls, 0)

    def test_race_discarded_and_not_queued(self):
        backend = AtomicFake("running")
        self.assertEqual(tick(self.lab, self.snapshot, backend, 3600)["reason"], "busy")
        backend.actual = "idle"
        self.assertFalse(tick(self.lab, self.snapshot, backend, 3601)["sent"])
        self.assertEqual(backend.sent, 0)

    def test_reservation_and_pause(self):
        reserved = tick(self.lab, self.snapshot, timestamp=3600)
        self.assertTrue(reserved["ready"])
        self.assertEqual(reserved["target"]["threadId"], THREAD)
        self.assertFalse(tick(self.lab, self.snapshot, timestamp=3601).get("ready", False))
        self.lab.pause()
        backend = AtomicFake()
        self.assertEqual(tick(self.lab, self.snapshot, backend, 3600)["reason"], "paused")
        self.assertEqual(backend.calls, 0)

    def test_freshness_boundaries_and_slot_transition(self):
        for observed in (None, True, float("nan"), float("inf"), 3601, 3539.9):
            with self.subTest(observed=observed):
                result = tick(self.lab, dict(self.snapshot, observed_at=observed), timestamp=3600)
                self.assertEqual(result["reason"], "stale_or_unknown")
        self.assertTrue(tick(self.lab, dict(self.snapshot, observed_at=3540), timestamp=3600)["ready"])
        self.assertTrue(tick(self.lab, dict(self.snapshot, observed_at=5400), timestamp=5400)["ready"])

    def test_failed_transport_is_not_replayed(self):
        class Failure:
            def wake_if_idle(self, *args):
                raise OSError("delivery unknown")
        with self.assertRaises(OSError):
            tick(self.lab, self.snapshot, Failure(), 3600)
        self.assertEqual(tick(self.lab, self.snapshot, timestamp=3601)["reason"], "already_attempted")
        self.assertEqual(self.lab.events()[-1]["payload"]["reason"], "already_attempted")

    def test_concurrent_ticks_and_restart_reserve_once(self):
        import concurrent.futures
        def attempt(_):
            lab = Lab(self.lab.root)
            try:
                return tick(lab, self.snapshot, timestamp=3600)
            finally:
                lab.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(attempt, range(8)))
        self.assertEqual(sum(r.get("ready", False) for r in results), 1)
        self.lab.close()
        self.lab = Lab(self.tmp.path)
        self.assertEqual(tick(self.lab, self.snapshot, timestamp=3601)["reason"], "already_attempted")

    def test_prepared_waiting_and_invalid_snapshot(self):
        self.lab.hold("本人判断")
        self.assertEqual(tick(self.lab, self.snapshot, timestamp=3600)["reason"], "waiting")
        self.lab.db.execute("UPDATE control SET phase='prepared' WHERE id=1")
        self.lab.db.commit()
        self.assertEqual(tick(self.lab, self.snapshot, timestamp=3600)["reason"], "prepared")
        for snapshot in (None, []):
            with self.assertRaises(ValueError):
                tick(self.lab, snapshot, timestamp=3600)


if __name__ == "__main__":
    unittest.main()
