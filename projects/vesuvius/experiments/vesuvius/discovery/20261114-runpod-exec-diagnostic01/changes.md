# R201との実行差分

R201の凍結コントローラを同一ファイルから読込み、次の二点を追加した。

- `DiagnosticApi` は同じ管理REST要求に、伏せ字・上限付きのエラー観測と期限付きSSE取得を追加する。継承した `exec` の本番呼出しは再送しない。
- `wait_armed` は固定Podの所有・構成を照合し、marker読取だけを期限内で再試行する。新しいコードは `diagnostic.py` に全て保存した。

R201の `run`、`cleanup`、`upload`、`launch_work`、`collect`、`make_bundle`、`create_request`、PID 1、転送worker、推論、ローカル再集約をそのまま参照する。固定科学入力tarのバイト列SHAはR201と一致。R205の課金確認コードも読取用途で参照し、新しい原票だけに保存する。
