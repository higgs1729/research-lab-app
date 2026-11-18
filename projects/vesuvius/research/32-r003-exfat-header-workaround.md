# R003: exFAT上のヘッダーコピーを切り分け、変更前ビルドを再開

2026-11-11 20:16 JST、heartbeat時間枠996886。未決監査提案0件。前回のビルドは385.175秒で終了コード1、重複する研究プロセスなしだった。本人判断待ちはない。研究対象はR003のまま。

## 原因と限定した回避

`vc_reader_catalog` の `disk_budget.cpp` で `vcr::Lru`、`ElementType`、`Auth` などの二重定義が発生した。固定ソースの `vc_reader/cmake/NativeTargets.cmake` は公開ヘッダーの場所を `src/cpp` へのsymlinkにする設計で、作れなければコピーする。D:はexFATで、今回の生成先はリンクでなく通常のディレクトリと別ファイルになっていた。コピーと原本のSHA-256は一致しており、古い生成内容が混ざった問題ではない。

同じ `lru.hpp` を原本パスと公開ヘッダーパスでincludeする最小コンパイルを保存した。コピー経由では `redefinition of default argument` で失敗（3.14秒）、公開側を原本へのincludeにするだけで成功（0.79秒）。コンパイラや上流のヘッダー本文は変えていない。

この結果に基づき、**ビルドディレクトリ内の生成ヘッダー201個だけ**を原本へのincludeに置き換えた。変更前に全ファイルを原本とバイト比較し、元のSHA-256と参照ヘッダーのSHA-256を保存した。研究対象の上流ソースは変更していない。停止した `disk_budget.cpp.o` を同じビルドツリーで再コンパイルして終了コード0を確認した。

これは今回のexFAT環境に対するローカルの回避処理。flatboiの初期UV問題の修正ではなく、上流の修正PRも作成していない。CMakeを再設定するとコピーへ戻る可能性があるため、再開時には設定処理を繰り返さず、生成ヘッダーの状態も記録した。

## 現在の実行と次の確認

`20261111-build02` の変更前ビルドが稼働中。前回成功した部分を再利用して残り166ステップを処理し、20:16時点では19ステップまで進んだ。flatboi本体の翻訳単位のコンパイルと既存 `test_slim_assembly` は通っているが、リンクと全体の完了はまだ未確認。assemblyの出力は36 systems、input_rejections 14、comparison_rejections 15、matrix_max_scaled_error 0、rhs_max_scaled_error 3.4879728367302089e-06、lifecycle_max_absolute_error 0。合成入力の既存検査であり、R003の実データ上の重なりを測った結果ではない。

実行コマンド（稼働中に重ねて実行しない）:

```powershell
wsl.exe --exec python3 /mnt/c/dev/kensyoukin/experiments/vesuvius/r003/20261111-header-debug/resume_native.py
```

- 実行セッション `40586`、WSL runner PID `275`。番号だけで判断せず、[現在状態](../experiments/vesuvius/r003/20261111-build02/state.json)と実プロセスのコマンドを照合する。
- 1並列、CPU affinity 0。各プロセスのアドレス空間上限4GiB、ビルド全体30分でプロセスグループを停止。コンパイラ一時ファイルもD:に指定。
- 既存assemblyターゲットは上流CMake側でPaStiX等を2スレッドに上書きして実行する。親のCPU affinityは1 CPUのまま。性能測定ではない。
- C:の空きは確認時2.69GB、物理メモリの空きは約7.43GiBだった。空き容量の変化全体を今回の処理に帰属できていない。C:へビルドを移さず、D:の既存成果を再利用する。

次のheartbeatはbuild01ではなくbuild02を確認する。completeならバイナリのハッシュとログを保存し、固定済みの公開入力を `--keep=1.5`、50反復、symmetric_dirichletで実行する。failedなら原因と資源を見直す。runningなら重複起動しない。現時点で実データ再現や修正効果の主張はしない。

## 根拠

- [元の失敗状態](../experiments/vesuvius/r003/20261111-build01/state.json)、[失敗ログ](../experiments/vesuvius/r003/20261111-build01/build.log)
- [最小プローブ](../experiments/vesuvius/r003/20261111-header-debug/probe.py)、[結果](../experiments/vesuvius/r003/20261111-header-debug/result.json)、[失敗メッセージ](../experiments/vesuvius/r003/20261111-header-debug/copied.log)
- [生成物だけを変更するスクリプト](../experiments/vesuvius/r003/20261111-header-debug/forward_generated_headers.py)、[201ファイルの記録](../experiments/vesuvius/r003/20261111-header-debug/forwarders-manifest.json)、[元の失敗対象の再コンパイル](../experiments/vesuvius/r003/20261111-header-debug/disk-budget-retry.log)
- [20:16の固定スナップショット](../experiments/vesuvius/r003/20261111-header-debug/progress-snapshot02.json)、[assembly検査結果](../experiments/vesuvius/r003/20261111-header-debug/slim-assembly-result.json)、[制限付き再開スクリプト](../experiments/vesuvius/r003/20261111-header-debug/resume_native.py)

有料計算の新規調達0 USD。このheartbeatで追加パッケージや実データは取得していない。LLM利用とローカル電力は金額換算していない。
