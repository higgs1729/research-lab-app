"""Reserve a heartbeat after a fresh idle check. A check/send race is accepted."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time
import sys
import math
if __package__:
    from .lab import Lab, ROOT
else:
    from lab import Lab, ROOT

PROMPT = ("研究のheartbeatです。現在の方針、実行中の仕事、結果、監査の受信箱を確認し、"
          "必要な次の研究を一件ずつ進めてください。本人の判断待ちは維持し、"
          "実行中の仕事を重複起動しないでください。")


def eligible(control, snapshot, timestamp):
    if control["phase"] != "running":
        return control["phase"]
    if snapshot.get("thread_id") != control["thread_id"] or snapshot.get("host_id") != control["host_id"]:
        return "wrong_target"
    observed = snapshot.get("observed_at")
    if isinstance(observed, bool) or not isinstance(observed, (float, int)) or not 0 <= timestamp - observed <= 60:
        return "stale_or_unknown"
    if snapshot.get("status") != "idle":
        return "not_idle"
    # A terminal turn status is necessary, but user/approval waits must also be ruled out.
    if snapshot.get("needs_input") is not False:
        return "needs_input_or_unknown"
    return None


def tick(lab, snapshot, transport=None, timestamp=None):
    timestamp = time.time() if timestamp is None else timestamp
    if not isinstance(snapshot, dict):
        raise ValueError("Snapshot must be a JSON object")
    if isinstance(timestamp, bool) or not isinstance(timestamp, (float, int)) or not math.isfinite(timestamp) or timestamp < 0:
        raise ValueError("Timestamp must be a finite nonnegative number")
    with lab.db:
        lab.db.execute("BEGIN IMMEDIATE")
        control = lab.status()
        reason = eligible(control, snapshot, timestamp)
        if reason:
            lab.event("heartbeat", {"sent": False, "reason": reason})
            return {"sent": False, "reason": reason}
        lab.db.execute("""CREATE TABLE IF NOT EXISTS heartbeat_ticks (
            thread TEXT NOT NULL, host TEXT NOT NULL, slot INTEGER NOT NULL,
            PRIMARY KEY(thread,host,slot))""")
        slot = int(timestamp // 1800)
        cur = lab.db.execute("INSERT OR IGNORE INTO heartbeat_ticks VALUES(?,?,?)",
                             (control["thread_id"], control["host_id"], slot))
        if not cur.rowcount:
            lab.event("heartbeat", {"sent": False, "reason": "already_attempted"})
            return {"sent": False, "reason": "already_attempted"}
        lab.event("heartbeat", {"sent": False, "reason": "reserved", "slot": slot,
                                "thread": control["thread_id"], "host": control["host_id"]})
    # Persist the attempt before transport: an ambiguous failure is never replayed this slot.
    key = f"{control['host_id']}:{control['thread_id']}:{slot}"
    if transport is None:
        return {"sent": False, "ready": True, "reason": "reserved", "key": key,
                "target": {"threadId": control["thread_id"], "hostId": control["host_id"]},
                "prompt": PROMPT}
    result = transport.wake_if_idle(control, PROMPT, key)
    if result not in ("sent", "busy", "paused", "needs_input"):
        raise ValueError("Unknown delivery result; do not retry this tick")
    return {"sent": result == "sent", "reason": result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--snapshot", type=Path, help="Fresh normalized app state; reserves this tick")
    args = parser.parse_args()
    lab = None
    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8-sig")) if args.snapshot else {}
        lab = Lab(args.root)
        print(json.dumps(tick(lab, snapshot), ensure_ascii=False))
        return 0
    except (ValueError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    finally:
        if lab:
            lab.close()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main())
