"""Research status, evidence records and audit inbox. Standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
from datetime import datetime, timezone
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1] / "projects" / "default"


def now():
    return datetime.now(timezone.utc).isoformat()


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


class Lab:
    def __init__(self, root: Path):
        self.root = root.resolve()
        runtime = self.root / "runtime"
        runtime.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(runtime / "lab.sqlite3", timeout=15)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS control (
                id INTEGER PRIMARY KEY CHECK(id=1), phase TEXT NOT NULL,
                thread_id TEXT, host_id TEXT NOT NULL DEFAULT 'local', waiting_reason TEXT);
            INSERT OR IGNORE INTO control(id, phase) VALUES(1, 'prepared');
            CREATE TABLE IF NOT EXISTS records (
                id TEXT PRIMARY KEY, kind TEXT NOT NULL, created TEXT NOT NULL,
                payload TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS proposals (
                id TEXT PRIMARY KEY, created TEXT NOT NULL,
                fingerprint TEXT NOT NULL UNIQUE, payload TEXT NOT NULL,
                decision TEXT NOT NULL DEFAULT 'pending', reason TEXT,
                delivered_to TEXT, delivered_at TEXT, outcome TEXT);
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY, created TEXT NOT NULL,
                action TEXT NOT NULL, payload TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS heartbeat_ticks (
                thread TEXT NOT NULL, host TEXT NOT NULL, slot INTEGER NOT NULL,
                PRIMARY KEY(thread,host,slot));
        """)
        # Existing CLI databases can also be opened by this application.
        columns = {row[1] for row in self.db.execute("PRAGMA table_info(control)")}
        if "waiting_reason" not in columns:
            self.db.execute("ALTER TABLE control ADD COLUMN waiting_reason TEXT")

    def close(self):
        self.db.close()

    def event(self, action, payload):
        self.db.execute("INSERT INTO events(created,action,payload) VALUES(?,?,?)",
                        (now(), action, encode(payload)))

    def status(self):
        state = dict(self.db.execute("SELECT * FROM control WHERE id=1").fetchone())
        state.pop("id")
        state["pending_proposals"] = self.db.execute(
            "SELECT COUNT(*) FROM proposals WHERE decision='pending'").fetchone()[0]
        state["record_count"] = self.db.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        return state

    def activate(self, thread, host="local"):
        self.require({"thread": thread, "host": host}, ("thread", "host"))
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            current = self.status()
            if current["phase"] == "running" and (
                current["thread_id"] != thread or current["host_id"] != host
            ):
                raise ValueError("別の主担当が稼働中です。主担当や環境を変更する前に一時停止してください。")
            self.db.execute("UPDATE control SET phase='running',thread_id=?,host_id=?,waiting_reason=NULL WHERE id=1",
                            (thread, host))
            self.event("activate", {"thread_id": thread, "host_id": host})
        return self.status()

    def pause(self):
        with self.db:
            self.db.execute("UPDATE control SET phase='paused',waiting_reason=NULL WHERE id=1")
            self.event("pause", {})
        return self.status()

    def hold(self, reason):
        self.require({"reason": reason}, ("reason",))
        with self.db:
            self.db.execute("UPDATE control SET phase='waiting',waiting_reason=? WHERE id=1", (reason,))
            self.event("hold", {"reason": reason})
        return self.status()

    @staticmethod
    def require(data, fields):
        if not isinstance(data, dict):
            raise ValueError("入力はJSONオブジェクトにしてください。")
        for key in fields:
            if not isinstance(data.get(key), str) or not data[key].strip():
                raise ValueError(f"空でない文字列を入力してください: {key}")

    def evidence(self, data):
        refs = data.get("evidence")
        if not isinstance(refs, list) or not refs:
            raise ValueError("根拠（evidence）にはプロジェクト内のファイルを1件以上指定してください。")
        result = []
        for ref in refs:
            if not isinstance(ref, str):
                raise ValueError("根拠のパスは文字列で指定してください。")
            path = (self.root / ref).resolve()
            if not path.is_relative_to(self.root) or not path.is_file():
                raise ValueError(f"プロジェクト内のファイルが見つかりません: {ref}")
            # Hash incrementally; evidence may include large experiment outputs.
            with path.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            result.append({"path": path.relative_to(self.root).as_posix(), "sha256": digest})
        return sorted(result, key=lambda item: item["path"])

    def record(self, data):
        self.require(data, ("kind", "summary"))
        if data["kind"] not in ("experiment", "verification", "decision", "cost", "audit"):
            raise ValueError("記録の種類が不正です。")
        if data.get("claim_status", "observed") not in ("hypothesis", "observed", "verified"):
            raise ValueError("主張の状態が不正です。")
        payload = dict(data, evidence=self.evidence(data))
        identifier = "record-" + uuid4().hex[:12]
        with self.db:
            self.db.execute("INSERT INTO records VALUES(?,?,?,?)",
                            (identifier, data["kind"], now(), encode(payload)))
            self.event("record", {"id": identifier, "kind": data["kind"], "summary": data["summary"]})
        return {"id": identifier, **payload}

    def propose(self, data):
        self.require(data, ("problem", "change", "benefit", "cost"))
        payload = {key: data[key] for key in ("problem", "change", "benefit", "cost")}
        payload["evidence"] = self.evidence(data)
        fingerprint = hashlib.sha256(encode(payload).encode()).hexdigest()
        identifier = "audit-" + uuid4().hex[:12]
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO proposals(id,created,fingerprint,payload) VALUES(?,?,?,?)",
                            (identifier, now(), fingerprint, encode(payload)))
            row = self.db.execute("SELECT * FROM proposals WHERE fingerprint=?", (fingerprint,)).fetchone()
            if row["id"] == identifier:
                self.event("propose", {"id": identifier, "problem": data["problem"]})
        return {"id": row["id"], "duplicate": row["id"] != identifier,
                "decision": row["decision"]}

    @staticmethod
    def unpack(row):
        item = dict(row)
        item["payload"] = json.loads(item["payload"])
        item.pop("fingerprint", None)
        return item

    def proposals(self, pending=False):
        sql = "SELECT * FROM proposals"
        if pending:
            sql += " WHERE decision='pending'"
        return [self.unpack(row) for row in self.db.execute(sql + " ORDER BY created,id")]

    def delivery(self):
        state = self.status()
        target = {"threadId": state["thread_id"], "hostId": state["host_id"]}
        if state["phase"] != "running":
            return {"ready": False, "reason": state["phase"], "proposals": []}
        proposals = [p for p in self.proposals(pending=True)
                     if p["delivered_to"] != encode(target)]
        return {"ready": bool(proposals), "target": target, "proposals": proposals}

    def delivered(self, identifier, thread, host):
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            state = self.status()
            if state["phase"] != "running" or (state["thread_id"], state["host_id"]) != (thread, host):
                raise ValueError("受領先と現在の主担当・環境が一致しないか、稼働中ではありません。最新に更新してください。")
            cursor = self.db.execute(
                "UPDATE proposals SET delivered_to=?,delivered_at=? WHERE id=? AND decision='pending'",
                (encode({"threadId": thread, "hostId": host}), now(), identifier))
            if cursor.rowcount != 1:
                raise ValueError("未判断の提案が見つかりません。")
            self.event("delivered", {"id": identifier, "thread": thread, "host": host})
        return {"id": identifier, "delivered": True}

    def decide(self, identifier, decision, reason):
        self.require({"reason": reason}, ("reason",))
        if decision not in ("accept", "defer", "reject"):
            raise ValueError("採否は採用・保留・不採用から選び、理由を入力してください。")
        with self.db:
            cursor = self.db.execute("UPDATE proposals SET decision=?,reason=? WHERE id=?",
                                     (decision, reason, identifier))
            if cursor.rowcount != 1:
                raise ValueError("提案が見つかりません。")
            self.event("decision", {"id": identifier, "decision": decision, "reason": reason})
        return {"id": identifier, "decision": decision}

    def outcome(self, identifier, result):
        self.require({"result": result}, ("result",))
        with self.db:
            cursor = self.db.execute("UPDATE proposals SET outcome=? WHERE id=? AND decision='accept'",
                                     (result, identifier))
            if cursor.rowcount != 1:
                raise ValueError("採用された提案が見つかりません。結果は採用した提案に記入してください。")
            self.event("outcome", {"id": identifier, "outcome": result})
        return {"id": identifier, "outcome": result}

    def records(self):
        return [self.unpack(row) for row in self.db.execute("SELECT * FROM records ORDER BY created,id")]

    def events(self):
        return [self.unpack(row) for row in self.db.execute("SELECT * FROM events ORDER BY id")]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Project root; tests use an isolated directory")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "pause", "inbox", "history", "delivery", "records", "events"):
        sub.add_parser(name)
    active = sub.add_parser("activate", help="Register a lead (any nonempty ID); does not launch research")
    active.add_argument("--thread", required=True)
    active.add_argument("--host", default="local")
    hold = sub.add_parser("hold", help="Suppress heartbeat while waiting for a human decision")
    hold.add_argument("--reason", required=True)
    for name in ("record", "propose"):
        sub.add_parser(name).add_argument("--file", type=Path, required=True)
    delivered = sub.add_parser("delivered", help="Acknowledge only after confirmed delivery to the registered lead")
    delivered.add_argument("id")
    delivered.add_argument("--thread", required=True)
    delivered.add_argument("--host", default="local")
    decision = sub.add_parser("decide")
    decision.add_argument("id")
    decision.add_argument("decision", choices=("accept", "defer", "reject"))
    decision.add_argument("--reason", required=True)
    outcome = sub.add_parser("outcome")
    outcome.add_argument("id")
    outcome.add_argument("--result", required=True)
    args = parser.parse_args(argv)
    lab = Lab(args.root)
    try:
        if args.command in ("status", "pause", "delivery", "records", "events"):
            result = getattr(lab, args.command)()
        elif args.command == "activate":
            result = lab.activate(args.thread, args.host)
        elif args.command == "hold":
            result = lab.hold(args.reason)
        elif args.command in ("record", "propose"):
            result = getattr(lab, args.command)(json.loads(args.file.read_text(encoding="utf-8-sig")))
        elif args.command in ("inbox", "history"):
            result = lab.proposals(pending=args.command == "inbox")
        elif args.command == "delivered":
            result = lab.delivered(args.id, args.thread, args.host)
        elif args.command == "decide":
            result = lab.decide(args.id, args.decision, args.reason)
        else:
            result = lab.outcome(args.id, args.result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    finally:
        lab.close()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main())
