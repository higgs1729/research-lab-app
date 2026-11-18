# R003: 公開入力を固定し、変更前のCPUビルドを開始

2026-11-11 19:56 JST、heartbeat時間枠996885。開始時に主担当running・未決監査提案0件・重複実験プロセスなしを確認。R001は保留、R002は既存修正と重複するため不採用のまま。今回の研究はR003だけ。

## 投入判断

[一次資料確認](30-r003-flatboi-source-review.md)に基づき、`flatboi` の初期UVの単位問題を現行コードの実行で確かめる。原因の仮説と18件・20件の比較は既存issue #2500の作者alpaltianによる成果。こちらの新規発見として扱わない。修正PRの重複は確認した検索範囲では見つからず、現行mainの問題箇所も変わっていなかった。

まず変更前を実データで実行する。その後、初期UVの単位修正を小さい差分で試し、出力に残る領域と伸びを同条件で比較する。stride倍で全ての独立成分の重なりが防げると仮定しない。粗格子化そのものによる小成分の欠落、UV liftの無効点は別の限界として残る。

## 今回実行したこと

- コミット `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5` を `D:/kensyoukin-work/r003-villa` に固定。`volume-cartographer`・`vc_reader`・`vc_object_store` だけをsparse checkout。19:53の `git status --porcelain` は空で、上流コードは未変更。
- 既存WSL Ubuntuの公式 `install_build_deps.sh minimal-build` を実行し、終了コード0。事前見積もりは326MB取得・導入量の合計上限1.56GB。apt更新後の実ログは20更新・362新規、339MB取得・追加ディスク1564MB（ほかにsoftware-propertiesの2更新、44.4KBとapt一覧12.3MB）。有料計算を使っていない。Windows C:の空きは11.40GBから8.65GBへ変わったが、WSL仮想ディスク等も含むため全差分をパッケージ実占有量とみなさない。
- issueの主再現面 `PHerc0814/segments/20250929040153-auto_grown_20250929040153260/mesh/intermediate/tifxyz_original/` の4ファイルを取得。計1,110,638 bytes、サイズとETagを保存済み一覧と照合、SHA-256を記録。入力は変更しない。
- GUI・CUDA・Python binding・object-store serverを無効にしたflatboi構成で、CMake設定が231.658秒で成功。上流CIの構成を基に、手元のGCC 13 / gfortran、QuickBuild O0を使用。CIのClang/Flangと同一環境ではない。性能評価用のビルドではない。

## 現在の実行

19:56時点でコンパイル中。1並列、CPU affinity 0、OMP/OpenBLAS/PaStiX各1スレッド。`flatboi` と既存の `check_slim_assembly` が対象。ビルドディレクトリは `D:/kensyoukin-work/r003-build`。設定は通ったが、バイナリ完成・テスト成功・実データ再現・修正効果はまだ未確認。

起動コマンド（実行済み。稼働中に重ねて実行しない）:

```powershell
wsl.exe --exec python3 /mnt/c/dev/kensyoukin/experiments/vesuvius/r003/20261111-build-planning/run_native.py build01
```

- 実行セッションID: `24860`、WSLのrunner PID: `277`（再利用され得るため、番号だけで生存や対象を判断しない）。
- 現在状態: [state.json](../experiments/vesuvius/r003/20261111-build01/state.json)。これは実行中に更新される。19:56の固定証拠は [snapshot01](../experiments/vesuvius/r003/20261111-build-planning/progress-snapshot01.json)。
- ログ: [設定](../experiments/vesuvius/r003/20261111-build01/configure.log)、[コンパイル](../experiments/vesuvius/r003/20261111-build01/build.log)。後者は実行中に追記される。
- 設定600秒・ビルド1800秒の上限。超えればプロセスグループを停止し、状態を失敗として保存する。自動で再実行しない。最初のビルドでは完了時間を未実測なので、この時点を投入の見直し点にする。

次のheartbeatでは、まずこの実行の状態と実プロセスを確認する。completeならバイナリのハッシュとassemblyテストのログを確認し、上記公開入力の `--keep=1.5`、50反復、symmetric_dirichletの変更前実行へ進む。failedなら原因を確認し、環境修正に費やす時間と再利用価値を再判断する。runningなら重複起動しない。

## 保存物と資源

- [実験計画](../experiments/vesuvius/r003/20261111-build-planning/plan.json)
- [固定checkoutのスクリプト](../experiments/vesuvius/r003/20261111-build-planning/prepare_workspace.py)と[ログ](../experiments/vesuvius/r003/20261111-build-planning/checkout.log)
- [公式依存導入のログ](../experiments/vesuvius/r003/20261111-build-planning/install01.log)
- [CPUビルドの実行・停止・記録スクリプト](../experiments/vesuvius/r003/20261111-build-planning/run_native.py)
- [入力取得スクリプト](../experiments/vesuvius/r003/20261111-build-planning/download_input.py)、[入力manifest](../experiments/vesuvius/r003/20261111-input01/manifest.json)

有料計算の新規調達0 USD。LLM利用・ローカル電力は金額換算していない。実データの取得量は上記1,110,638 bytesで、依存ソースのGit取得・apt取得・資料調査はこれに含まない。大きい作業物はD:へ分離した。上流のAGENTS.md、CONTRIBUTING.md、SCROLL_ANATOMY.mdとvc_readerのcapability mapを読了。提出物はまだなく、人が実行・レビューしたという主張もしていない。
