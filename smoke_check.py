"""Launch the real application, check JSON endpoints, then stop its process."""
from __future__ import annotations

import json
from pathlib import Path
import queue
import re
import socket
import subprocess
import sys
import threading
from urllib.error import HTTPError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen
from uuid import uuid4

APP_DIR = Path(__file__).resolve().parent


def main():
    project = APP_DIR / "runtime" / "smoke-projects" / uuid4().hex
    command = [sys.executable, str(APP_DIR / "app.py"), "--demo", "--no-browser",
               "--root", str(project), "--port", "0"]
    checks = []
    process = subprocess.Popen(command, cwd=APP_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, encoding="utf-8")
    base = None
    failure = None
    try:
        lines = queue.Queue()
        threading.Thread(target=lambda: lines.put(process.stdout.readline()), daemon=True).start()
        startup = lines.get(timeout=15)
        match = re.search(r"http://127\.0\.0\.1:\d+", startup)
        if not match:
            raise RuntimeError("Server did not report its local URL: " + startup)
        base = match.group()
        with urlopen(base, timeout=5) as response:
            page = response.read().decode("utf-8")
        token = re.search(r'name="lab-token" content="([^"]+)"', page).group(1)

        def request(path, data=None, expected=200):
            body = None if data is None else json.dumps(data, ensure_ascii=False).encode("utf-8")
            req = Request(base + path, data=body, headers={"Content-Type": "application/json", "X-Lab-Token": token})
            try:
                response = urlopen(req, timeout=10)
            except HTTPError as exc:
                response = exc
            with response:
                value = json.load(response)
                if response.status != expected:
                    raise AssertionError((path, response.status, value))
            checks.append({"path": path, "method": "GET" if data is None else "POST", "status": expected})
            return value

        state = request("/api/state")
        assert state["status"]["record_count"] == 4
        assert len(state["proposals"]) == 4
        assert len(request("/api/files")) == 5
        for path in ("/api/status", "/api/records", "/api/history", "/api/events"):
            request(path)
        ref = state["records"][0]["payload"]["evidence"][0]
        assert request("/api/evidence?path=" + quote(ref["path"]))["sha256"] == ref["sha256"]
        proposal = request("/api/inbox")[0]
        submission = dict(proposal["payload"], evidence=[r["path"] for r in proposal["payload"]["evidence"]])
        assert request("/api/propose", submission)["duplicate"]
        request("/api/record", {"kind": "verification", "summary": "HTTP疎通で根拠のハッシュを確認",
                                "claim_status": "verified", "evidence": [ref["path"]]})
        request("/api/activate", {"thread_id": "conflicting-lead"}, expected=400)
        target = request("/api/delivery")["target"]
        request("/api/delivered", {"id": proposal["id"], "thread_id": "wrong", "host_id": "local"}, expected=400)
        request("/api/delivered", {"id": proposal["id"], "thread_id": target["threadId"], "host_id": target["hostId"]})
        request("/api/decide", {"id": proposal["id"], "decision": "accept", "reason": "HTTP疎通確認のため"})
        request("/api/outcome", {"id": proposal["id"], "result": "APIから採用後の結果を保存できた"})
        assert not request("/api/inbox")
        snapshot = {"thread_id": target["threadId"], "host_id": target["hostId"], "idle": False, "needs_input": False}
        assert request("/api/heartbeat", snapshot)["reason"] == "not_idle"
        snapshot["idle"] = True
        assert request("/api/heartbeat", snapshot)["ready"]
        assert request("/api/heartbeat", snapshot)["reason"] == "already_attempted"
        request("/api/hold", {"reason": "HTTP確認用の判断待ち"})
        assert request("/api/heartbeat", snapshot)["reason"] == "waiting"
        request("/api/pause", {})
        assert request("/api/heartbeat", snapshot)["reason"] == "paused"
        assert request("/api/status")["record_count"] == 5
    except Exception as exc:
        failure = f"{type(exc).__name__}: {exc}"
    finally:
        process.terminate()
        try:
            remaining, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            remaining, stderr = process.communicate(timeout=5)
        port_closed = True
        if base:
            try:
                with socket.create_connection(("127.0.0.1", urlsplit(base).port), timeout=1):
                    port_closed = False
            except OSError:
                pass
        report = {"status": "passed" if not failure and port_closed else "failed",
                  "python": sys.version.split()[0], "command": command, "project": str(project),
                  "checks": checks, "server_stopped": process.poll() is not None,
                  "port_closed": port_closed, "error": failure, "stderr": stderr}
        output = APP_DIR / "verification-output" / "smoke.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
