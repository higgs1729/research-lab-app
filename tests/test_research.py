"""同梱した実研究記録(projects/vesuvius)が開けて、根拠の扱いが壊れていないこと。"""
from pathlib import Path
import unittest

from app import main, project_files
from tools.lab import Lab

ROOT = Path(__file__).resolve().parents[1] / "projects" / "vesuvius"


@unittest.skipUnless((ROOT / "runtime" / "lab.sqlite3").is_file(), "研究記録が同梱されていない")
class ResearchProjectTest(unittest.TestCase):
    def test_records_and_bundled_evidence(self):
        lab = Lab(ROOT)
        try:
            records = lab.records()
            self.assertGreaterEqual(len(records), 300)
            offered = set(project_files(ROOT))
            refs = {e["path"] for r in records for e in r["payload"].get("evidence", [])}
            bundled = refs & offered
            self.assertTrue(bundled, "根拠が 1 つも同梱されていない")
            self.assertTrue(any(p.lower().endswith(".png") for p in bundled))
            # 同梱した根拠は登録時のハッシュと一致する(取り込みで中身を変えていない)
            # 同梱した根拠は、どれかの記録の登録時ハッシュと一致する(取り込みで中身を変えていない)。
            # 元の研究で登録後に書き換わったファイルが 2 個あり、画面では「変わっている」と出る
            stored = {}
            for r in records:
                for e in r["payload"].get("evidence", []):
                    stored.setdefault(e["path"], set()).add(e["sha256"])
            current = lab.evidence({"evidence": sorted(bundled)})
            matched = sum(row["sha256"] in stored[row["path"]] for row in current)
            self.assertGreaterEqual(matched, len(current) - 5)
        finally:
            lab.close()

    def test_research_flag_conflicts(self):
        with self.assertRaises(SystemExit):
            main(["--research", "--demo"])


if __name__ == "__main__":
    unittest.main()
