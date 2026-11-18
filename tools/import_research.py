"""実運用した研究体制(kensyoukin)の記録を、提出用の研究プロジェクトへ写す。

    python tools/import_research.py --source C:/dev/kensyoukin --dest projects/vesuvius

記録・監査提案・イベントは全件を写す。根拠ファイルは容量を抑えるため、
1 ファイル --max-file 以下のものを優先度順に、合計 --budget までだけ写す。
写さなかった根拠も記録には残り、画面では「同梱していない」と表示される。
提出物を作るときに 1 回だけ使う道具で、アプリの動作には要らない。
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.lab import Lab  # noqa: E402

# 研究の中身が分かりやすいものから先に入れる
PRIORITY = {".md": 0, ".png": 1, ".jpg": 1, ".jpeg": 1, ".json": 2, ".txt": 3, ".py": 4,
            ".patch": 4, ".csv": 5, ".log": 6, ".jsonl": 6}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--dest", type=Path, required=True)
    ap.add_argument("--max-file", type=int, default=200_000)
    ap.add_argument("--budget", type=int, default=12_000_000)
    a = ap.parse_args()
    src, dest = a.source.resolve(), a.dest.resolve()
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"写し先が空ではありません: {dest}")
    old = sqlite3.connect(src / "runtime" / "lab.sqlite3")
    old.row_factory = sqlite3.Row
    records = [dict(r) for r in old.execute("SELECT * FROM records ORDER BY created,id")]
    proposals = [dict(r) for r in old.execute("SELECT * FROM proposals ORDER BY created,id")]
    events = [dict(r) for r in old.execute("SELECT * FROM events ORDER BY id")]
    control = dict(old.execute("SELECT * FROM control WHERE id=1").fetchone())

    paths = set()
    for row in records + proposals:
        paths.update(e["path"] for e in json.loads(row["payload"]).get("evidence", []))
    candidates = []
    for rel in paths:
        f = src / rel
        if f.is_file() and f.stat().st_size <= a.max_file:
            candidates.append((PRIORITY.get(f.suffix.lower(), 9), f.stat().st_size, rel))
    used, copied = 0, 0
    for _, size, rel in sorted(candidates):
        if used + size > a.budget:
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src / rel, target)
        used += size
        copied += 1

    lab = Lab(dest)
    with lab.db:
        lab.db.executemany("INSERT INTO records VALUES(:id,:kind,:created,:payload)", records)
        lab.db.executemany(
            "INSERT INTO proposals(id,created,fingerprint,payload,decision,reason,delivered_to,delivered_at,outcome)"
            " VALUES(:id,:created,:fingerprint,:payload,:decision,:reason,:delivered_to,:delivered_at,:outcome)",
            proposals)
        lab.db.executemany("INSERT INTO events(id,created,action,payload) VALUES(:id,:created,:action,:payload)",
                           events)
        lab.db.execute("UPDATE control SET phase=?,thread_id=?,host_id=? WHERE id=1",
                       (control["phase"], control["thread_id"], control["host_id"]))
    lab.close()
    (dest / "PROJECT.txt").write_text(
        "Vesuvius Challenge の研究で実際に使った記録(2026-11-11〜)。\n"
        f"記録 {len(records)} 件・監査提案 {len(proposals)} 件・イベント {len(events)} 件。\n"
        f"根拠ファイルは {len(paths)} 個のうち {copied} 個({used / 1e6:.1f} MB)だけを同梱。\n",
        encoding="utf-8")
    print(json.dumps({"records": len(records), "proposals": len(proposals), "events": len(events),
                      "evidence_total": len(paths), "evidence_copied": copied, "bytes": used},
                     ensure_ascii=False))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
