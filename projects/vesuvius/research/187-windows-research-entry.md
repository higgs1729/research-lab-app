Status: resolved
担当: 研究（R187、2026-11-14）
Blocked by: 186

# 別フォルダの研究で再発した入口のパス解決を直す（2026-11-14）

## 依頼

日次監査audit-98f29f483bdaを採用済み。R170/R178/R180では共通Windows runpy入口から対象スクリプトの同階層モジュールを読めず停止、R185ではネストした出力先から資産R133を誤解決してforward前に停止した。次のWindows入口再利用前に、登録済み原本を保持した新しい再利用入口へ小さく修正する。

共通資源制限は experiments/vesuvius/r005/20261112-ct-render01/run_windows.py を借りられる。新しい入口は対象scriptの絶対位置を一度解決し、その親がスクリプト実行中のimport探索先になるようにする。CPU1、commit4GiB、数値ライブラリ1threadと開始/終了/例外時の原票を保つ。相対パスの基準を明記し、出力先を資産位置の基点にしない。登録済み旧runnerや既存実験ソースは編集しない。例として tools/research/ 以下に置くが、必要以上の設定体系や一般フレームワークは作らない。

推論入口については、R173 infer.pyを借りたR185 model.pyの失敗と修正を確認し、出力先とR133等の保存資産を別に明示して解決する次回用の入口/アダプタを残す。本番と同じ入口で、モデルを動かす前に同階層importと借用runner/資産の場所を確認できること。借用関数のglobalsを外から書き換える手法を使うなら狭い範囲に閉じ、前提と戻し処理を示す。

確認は実際の失敗に対応する小さい二例で足りる：別フォルダのスクリプトが同階層moduleを読む例、R185同様のネスト出力から実在するR133等を同じ絶対位置へ解決する例。エラー時のログ/終了コードと既存出力を上書きしない性質も入口として必要な範囲を確認する。新たなCT取得・描画・モデルforward・build・依存追加・有料計算なし。成功済み実験は一切再実行しない。

実測の証拠、再利用コマンド、失敗時の扱い、比較元SHA、新しいcode/検証/manifest/lab候補を experiments/vesuvius/discovery/20261114-windows-research-entry01/ に保存し、研究票へ結論を追記する。親が主要差分と別入口一例を確認してから確定。監査outcomeとlab登録は親。C新規出力、D読取のみ。サブ委任なし。

今回はgpt-6.1-sol / high。反復例と修正方針は確定しており、既存資源制限と資産配置を解釈して小さく移植する作業のため。186完了後に逐次着手。

## 結論

2026-11-14 JST。[一次] 新Windows入口で別フォルダの同階層importが通り、起動時CWD、CPU1、commit 4 GiB、数値ライブラリ用の1thread環境を保持した。R173アダプタは、ネスト出力でR133の借用runner、保存Zarr、seed42とdense-nativeの重みをR185の実行原票と同じ位置へ解決した。実モデルforwardは未実施。 [実験報告](../experiments/vesuvius/discovery/20261114-windows-research-entry01/README.md)

## 根拠・詳細

[一次] 旧入口の同階層importは終了1、新入口は終了0。`RuntimeError` で終了1、`SystemExit(7)` で終了7となり、原票のコードと一致した。既存原票は開始前の排他作成で保護し、再指定後のSHA-256も一致した。主担当は別CWDから別の相対スクリプトを渡し、同階層importと資源設定を確認した。比較元12ファイルのSHA-256は検証前後で一致。担当の7起動は10.287秒で、クラウド費は0円。 [検証原票](../experiments/vesuvius/discovery/20261114-windows-research-entry01/run01/verification.json) [主担当検証](../experiments/vesuvius/discovery/20261114-windows-research-entry01/lead/verified.json)

## 取得の経路

[一次] 旧入口のWindows Job Object設定を新runnerから借用した。R173アダプタは実 `common.py` を読み、R173の入口、実験出力とR133資産のパスを引数で受け取る。相対CLIパスは起動時CWD基準。次の実験では事前に同じ入口を `--check` で動かして資産の位置を確認できる。 [新runner](../tools/research/run_windows.py) [R173アダプタ](../tools/research/infer_r173.py) [再利用コマンド](../experiments/vesuvius/discovery/20261114-windows-research-entry01/README.md)

## メモ

2026-11-14 JST。[一次] R005のWindows runnerは別ディレクトリのファイル実行前に対象の親をimport探索先へ足していない。R185の失敗ログは差し替えた出力 `HERE` の上位からR133を探したことを示す。登録済みファイルを読み取り、資源制限を借りる実行入口と、出力・R173・R133を独立して受け取るアダプタの実装に着手した。

主担当の差分読解と別CWD試験の完了後に確定。lab登録候補とmanifestを保存した。
