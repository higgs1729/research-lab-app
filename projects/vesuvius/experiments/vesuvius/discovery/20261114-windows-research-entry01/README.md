# Windows研究入口のパス解決

2026-11-14 JST。日次監査 `audit-98f29f483bda` の採用項目。R170/R178/R180の同階層importと、R185のネスト出力でのR133参照を、次の実験から使える入口で確認した。

## 実測

- 旧runnerに別フォルダの小さなスクリプトを渡すと `ModuleNotFoundError` で終了1。新runnerでは同じファイルから同階層をimportし、終了0。対象の絶対 `argv[0]`、空白を含むファイルパスと引数、起動時CWDの維持、CPU 1個、数値ライブラリ用の5環境変数が `1`、commit上限4,294,967,296 Bを確認した。 [旧入口のstderr](run01/old-sibling.stderr.txt) [新入口の原票](run01/new-sibling.json)
- 対象の `RuntimeError` は終了1で例外型・文言を原票に残す。対象の `SystemExit(7)` はプロセス・原票とも終了7。作成済みの原票を再指定すると対象開始前に `FileExistsError` で終了1。同じ原票のSHA-256を前後で照合した。 [例外原票](run01/target-raise.json) [終了7原票](run01/target-exit.json) [上書き拒否のstderr](run01/duplicate-log.stderr.txt)
- R185の保存契約を新しい `run01/inference/original` にコピーし、R173を借りる実行入口の `--check` を2モデルで通した。両方でR173の実 `common.py`、R133の `run_local.py`、公式実装、保存済み依存先、元のZarrとチェックポイントを絶対パスで確認した。Zarrと重みはR185の実行原票と同じ位置だった。ネスト出力内に増えたものは契約コピーだけ。 [旧R185のstderr](../20261114-known-text-refinement-pilot01/model-run-failed-import/original-seed42-reverse.log) [seed42](run01/r173-seed42-reverse.stdout.txt) [dense-native](run01/r173-dense-reverse.stdout.txt)
- 主担当は別CWDから `../program/read_sibling.py` を渡し、同階層import、絶対 `argv[0]`、CWD維持、CPU 1個、各環境変数 `1`、4 GiBを確認した。 [主担当の検査](lead/verified.json)

検証7起動で10.287秒。比較元12ファイルのSHA-256は前後で一致した。新規CT取得・描画・モデルforward・ビルド・依存追加・クラウド費は0。実推論の動作は未検証。 [コマンドと比較元SHA-256](run01/verification.json)

## 次回の実行

Windows PowerShell。以下は `C:\dev\kensyoukin` からの実行例。新runnerの `log` と `script`、R173アダプタの `--entry`、`--output-dir`、`--r133` の相対パスはすべて起動時のCWD基準。対象へ渡す後続引数はそのまま渡る。新runnerは対象ファイルを絶対化し、その親を実行中の `sys.path` の先頭へ置く。

```powershell
$experiment = 'experiments/vesuvius/discovery/20261114-windows-research-entry01'
python -B "$experiment/verify.py" "$experiment/run02"
```

`verify.py` は存在しない結果ディレクトリを指定する。スクリプト一つを実行するときは `python -B tools/research/run_windows.py <新しい原票.json> <対象.py> [対象の引数]` を使う。原票の親ディレクトリは先に作る。開始時に原票を排他作成し、通常終了・Python例外時に同じ原票へ終了情報を記録する。強制終了では開始原票だけが残り得る。tracebackはstderrに流れるので必要なら新しいファイルに保存する。再試行時は新しい原票名と出力先を使う。

R173の資産位置だけを確認する例。`$output` は既存契約をコピーできる新しいディレクトリを指定する。

```powershell
$experiment = 'experiments/vesuvius/discovery/20261114-windows-research-entry01'
$output = "$experiment/preflight02/inference/original"
$r173 = 'experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/infer.py'
$r133 = 'experiments/vesuvius/r012/20261113-known-ink-inference01'
$contract = 'experiments/vesuvius/discovery/20261114-known-text-refinement-pilot01/inference/original/input-contract.json'
New-Item -ItemType Directory -Path $output -ErrorAction Stop | Out-Null
Copy-Item -LiteralPath $contract -Destination "$output/input-contract.json" -ErrorAction Stop
python -B tools/research/run_windows.py "$output/seed42-preflight-process.json" tools/research/infer_r173.py --entry $r173 --output-dir $output --r133 $r133 --tag seed42-reverse --check
```

`--check` はR173の `infer.py` と実 `common.py` を読み、入力・runner・重みなどの位置と既存の出力/一時ディレクトリがないことを確認する。R133の `run_local.py` は実行しない。実推論では同じ入口で新しい原票を指定し、`--check` を外す。保存契約内のZarrパスと保存メタデータ内の重みパスは既存R173が読む絶対パスを用いる。実推論時のハッシュ検査と保存は借用したR173側が担う。

アダプタは保存R173の `main(tag)` がグローバルの `HERE` を出力に、`R133` を借用runnerの場所に使うことを前提とする。実推論時だけ、`runpy` で得たその関数のグローバル辞書の2値を差し替え、`finally` で戻す。`sys.path` と `sys.modules['common']` も復元する。R133による環境変数・監査フックの設定はプロセス全体に及ぶため、このアダプタは専用のrunnerプロセスで一件ずつ使う。

[新runner](../../../../tools/research/run_windows.py) [R173アダプタ](../../../../tools/research/infer_r173.py) [研究票](../../../../research/187-windows-research-entry.md)
