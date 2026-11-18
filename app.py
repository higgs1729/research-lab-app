"""Local research notebook server. Python 3.11+, standard library only."""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import secrets
import sqlite3
import sys
import time
from urllib.parse import parse_qs, urlsplit
import webbrowser

from tools.lab import Lab, ROOT
from tools.heartbeat import tick

APP_DIR = Path(__file__).resolve().parent
MAX_BODY = 1_048_576
IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
               ".gif": "image/gif", ".webp": "image/webp"}


def project_files(root):
    """Offer regular project files, excluding runtime and hidden directories/links."""
    result = []
    for folder, directories, files in os.walk(root, followlinks=False):
        directories[:] = sorted(d for d in directories if not d.startswith(".")
                                and d not in ("runtime", "__pycache__")
                                and not (Path(folder) / d).is_symlink())
        for name in sorted(files):
            path = Path(folder) / name
            if not name.startswith(".") and not path.is_symlink() and path.is_file():
                if path.resolve().is_relative_to(root):
                    result.append(path.relative_to(root).as_posix())
    return sorted(result)


class ResearchServer(ThreadingHTTPServer):
    # Join handlers on close, so every SQLite connection is closed before exit.
    daemon_threads = False

    def __init__(self, address, root):
        self.root = Path(root).resolve()
        # Initialize schema before accepting concurrent requests.
        lab = Lab(self.root)
        lab.close()
        self.token = secrets.token_urlsafe(32)
        super().__init__(address, ResearchHandler)

    @property
    def origin(self):
        return f"http://127.0.0.1:{self.server_port}"


class ResearchHandler(BaseHTTPRequestHandler):
    server_version = "ResearchLab/1.0"

    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, fmt, *args):
        # Request bodies (research notes) are never written to logs.
        pass

    def send_content(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'nonce-" +
                         self.server.token + "'; style-src 'unsafe-inline'; object-src 'none'; "
                         "base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
        self.end_headers()
        self.wfile.write(body)

    def json_response(self, status, value):
        self.send_content(status, json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8"),
                          "application/json; charset=utf-8")

    def valid_host(self):
        return self.headers.get("Host") == f"127.0.0.1:{self.server.server_port}"

    @staticmethod
    def offered(lab, url):
        """画面に出してよい根拠ファイルの相対パスを返す。runtime/ の DB などは出さない。"""
        ref = parse_qs(url.query).get("path", [""])[0]
        if ref not in project_files(lab.root):
            if ref and not (lab.root / ref).exists():
                raise ValueError("この根拠ファイルは提出物に同梱していません(容量を抑えるため、"
                                 "大きいファイルは省いています)。記録とハッシュは残っています。")
            raise ValueError("プロジェクト内の選択可能な根拠ファイルを指定してください。")
        return ref

    def do_GET(self):
        if not self.valid_host():
            self.json_response(403, {"error": "起動時に表示された 127.0.0.1 のURLで開いてください。"})
            return
        url = urlsplit(self.path)
        if url.path == "/":
            html = (APP_DIR / "static" / "index.html").read_text(encoding="utf-8")
            self.send_content(200, html.replace("__TOKEN__", self.server.token).encode("utf-8"),
                              "text/html; charset=utf-8")
            return
        if url.path == "/favicon.ico":
            self.send_content(204, b"", "image/x-icon")
            return
        lab = Lab(self.server.root)
        try:
            if url.path == "/api/state":
                value = {"project": str(lab.root), "status": lab.status(),
                         "records": lab.records(), "proposals": lab.proposals(),
                         "events": lab.events(), "files": project_files(lab.root)}
            elif url.path == "/api/files":
                value = project_files(lab.root)
            elif url.path == "/api/status":
                value = lab.status()
            elif url.path == "/api/records":
                value = lab.records()
            elif url.path in ("/api/inbox", "/api/history"):
                value = lab.proposals(pending=url.path == "/api/inbox")
            elif url.path == "/api/events":
                value = lab.events()
            elif url.path == "/api/delivery":
                value = lab.delivery()
            elif url.path == "/api/evidence":
                ref = self.offered(lab, url)
                path = (lab.root / ref).resolve()
                hashes = lab.evidence({"evidence": [ref]})
                image = path.suffix.lower() in IMAGE_TYPES
                content = b""
                if not image:
                    with path.open("rb") as stream:
                        content = stream.read(65537)
                value = {**hashes[0], "image": image,
                         "text": content[:65536].decode("utf-8", errors="replace"),
                         "truncated": len(content) > 65536}
            elif url.path == "/api/raw":
                # 画像の根拠だけを、そのまま返す(画面で縮小表示・拡大表示するため)
                ref = self.offered(lab, url)
                path = (lab.root / ref).resolve()
                kind = IMAGE_TYPES.get(path.suffix.lower())
                if kind is None:
                    raise ValueError("画像ファイルだけを表示できます。")
                self.send_content(200, path.read_bytes(), kind)
                return
            else:
                self.json_response(404, {"error": "エンドポイントがありません。"})
                return
            self.json_response(200, value)
        except (ValueError, OSError, sqlite3.Error) as exc:
            self.json_response(400, {"error": str(exc)})
        finally:
            lab.close()

    def do_POST(self):
        if (not self.valid_host() or self.headers.get("X-Lab-Token") != self.server.token
                or self.headers.get("Origin") not in (None, self.server.origin)):
            self.json_response(403, {"error": "操作元を確認できません。画面を再読み込みしてください。"})
            return
        lab = None
        try:
            if self.headers.get_content_type() != "application/json":
                raise ValueError("Content-Type は application/json にしてください。")
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_BODY:
                raise ValueError("入力は1バイト以上1 MiB以下のJSONにしてください。")
            body = self.rfile.read(length)
            data = json.loads(body.decode("utf-8"), parse_constant=self.reject_constant)
            Lab.require(data, ())
            lab = Lab(self.server.root)
            route = urlsplit(self.path).path
            if route == "/api/activate":
                value = lab.activate(data.get("thread_id"), data.get("host_id", "local"))
            elif route == "/api/pause":
                value = lab.pause()
            elif route == "/api/hold":
                value = lab.hold(data.get("reason"))
            elif route in ("/api/record", "/api/propose"):
                value = getattr(lab, route.rsplit("/", 1)[1])(data)
            elif route == "/api/decide":
                Lab.require(data, ("id", "decision", "reason"))
                value = lab.decide(data["id"], data["decision"], data["reason"])
            elif route == "/api/outcome":
                Lab.require(data, ("id", "result"))
                value = lab.outcome(data["id"], data["result"])
            elif route == "/api/delivered":
                Lab.require(data, ("id", "thread_id", "host_id"))
                value = lab.delivered(data["id"], data["thread_id"], data["host_id"])
            elif route == "/api/heartbeat":
                # Explicit target fields let the core detect a stale screen/rebound lead.
                Lab.require(data, ("thread_id", "host_id"))
                if type(data.get("idle")) is not bool or type(data.get("needs_input")) is not bool:
                    raise ValueError("待機中・入力待ちのチェック状態を送ってください。")
                snapshot = {"thread_id": data["thread_id"], "host_id": data["host_id"],
                            "observed_at": time.time(), "status": "idle" if data["idle"] else "active",
                            "needs_input": data["needs_input"]}
                value = tick(lab, snapshot)
            else:
                self.json_response(404, {"error": "エンドポイントがありません。"})
                return
            self.json_response(200, value)
        except (ValueError, OSError, sqlite3.Error, UnicodeError) as exc:
            self.json_response(400, {"error": str(exc)})
        finally:
            if lab:
                lab.close()

    @staticmethod
    def reject_constant(value):
        raise ValueError(f"JSONの数値が不正です: {value}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="研究プロジェクトのフォルダ")
    parser.add_argument("--demo", action="store_true", help="巻物平坦化の教材デモを作成して開く")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--port", type=int, default=8780, help="0なら空いているポートを使用")
    parser.add_argument("--research", action="store_true",
                        help="実際の研究記録(projects/vesuvius)を開く")
    args = parser.parse_args(argv)
    if args.research and (args.demo or args.root):
        parser.error("--research は --demo / --root と同時に使えません")
    if args.research:
        root = APP_DIR / "projects" / "vesuvius"
        if not (root / "runtime" / "lab.sqlite3").is_file():
            parser.exit(2, f"研究記録が見つかりません: {root}\n")
    else:
        root = args.root or (APP_DIR / "projects" / "demo" if args.demo else ROOT)
    try:
        if args.demo:
            from seed_demo import seed_demo
            seed_demo(root)
        try:
            server = ResearchServer(("127.0.0.1", args.port), root)
        except OSError:
            if args.port == 0:
                raise
            # 既定ポートが他のアプリに使われていても起動できるよう、空きポートへ切り替える
            print(f"ポート {args.port} は使えないため、空いているポートで起動します", flush=True)
            server = ResearchServer(("127.0.0.1", 0), root)
    except (ValueError, OSError, sqlite3.Error) as exc:
        parser.exit(2, f"起動できません: {exc}\n")
    print(f"Research Lab: {server.origin}\nプロジェクト: {server.root}\n終了: Ctrl+C", flush=True)
    if not args.no_browser:
        try:
            webbrowser.open(server.origin)
        except webbrowser.Error as exc:
            print(f"ブラウザを開けません。上記URLを開いてください: {exc}", flush=True)
    try:
        server.serve_forever(poll_interval=0.2)
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main())
