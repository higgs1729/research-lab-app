from pathlib import Path
from tests.support import ProjectDirectory
import unittest

from seed_demo import measurements, seed_demo
from tools.lab import Lab


class DemoTest(unittest.TestCase):
    def test_numeric_example(self):
        result = measurements()
        self.assertEqual(result["before"]["signed_areas"], [0.5, -0.5])
        self.assertEqual(result["after"]["signed_areas"], [0.5, 0.5])
        self.assertEqual(result["before"]["inverted"], 1)
        self.assertEqual(result["after"]["inverted"], 0)
        self.assertEqual(result["after"]["degenerate"], 0)
        self.assertTrue(result["fixed_vertices_unchanged"])

    def test_seed_idempotent_and_evidence_portable(self):
        with ProjectDirectory() as folder:
            root = seed_demo(Path(folder))
            lab = Lab(root)
            try:
                self.assertEqual(lab.status()["phase"], "running")
                self.assertEqual(len(lab.records()), 4)
                self.assertEqual(len(lab.proposals()), 4)
                self.assertEqual(len(lab.proposals(pending=True)), 1)
                self.assertEqual({p["decision"] for p in lab.proposals()}, {"pending", "accept", "defer", "reject"})
                before = lab.records()
                seed_demo(root)
                self.assertEqual(before, lab.records())
                for row in lab.records() + lab.proposals():
                    refs = row["payload"]["evidence"]
                    self.assertEqual(lab.evidence({"evidence": [r["path"] for r in refs]}), refs)
                    for ref in refs:
                        self.assertFalse(Path(ref["path"]).is_absolute())
            finally:
                lab.close()

    def test_seed_does_not_overwrite_existing_project(self):
        with ProjectDirectory() as folder:
            root = Path(folder)
            (root / "mine.txt").write_text("keep", encoding="utf-8")
            with self.assertRaises(ValueError):
                seed_demo(root)
            self.assertEqual((root / "mine.txt").read_text(encoding="utf-8"), "keep")
            self.assertFalse((root / "runtime").exists())


if __name__ == "__main__":
    unittest.main()
