Status: resolved
担当: 研究（R163担当 2026-11-13）
Blocked by: 162

# R009の通常パッケージ初期化と保持試験を標準二対象ビルドで通す

## 依頼

2026-11-13。主担当は研究162の一案を採用する。固定14d4e725にR009を適用した研究160のreaderソース、同版Delta3D、研究125に残る実行中Ubuntu CPython 3.12.3-1ubuntu0.17用ヘッダー/nanobind2.10.2/NumPy2.2.6を使い、上流vc_reader単体CMakeの_catalogと_readerを通常構築する。偽パッケージ登録で__init__を省略した125の範囲から、実際の二つの__init__を通す範囲へ進める。

具体条件・入力・コマンドは experiments/vesuvius/r009/20261113-normal-python-feasibility01/README.md。C上WSL ext4の新規作業先へソース/通常Pythonパッケージをコピーし、標準CMakeのlibrary outputをstage/vc_readerへ揃える。既存160/125のソース・生成物・登録物・161の凍結候補を変更しない。D:は専用mount名前空間でread-only、ネットワーク分離。CMake/製品ソースへ新しい修正を足さず、既存計測ランナーと標準機能を使う。

開始前に版/ソース/ヘッダー・配布物/SOABIを照合。configure一回180秒、build一回900秒、通常importと試験一回120秒。CPU一個、数値/OpenMP一スレッド、AS4GiB、core0。新作業2GiB以内、C:空き10GiB以上。PID/PGID、引数、時刻、ログと期限を開始時に保存して重複起動を防ぐ。想定外の取得、欠けた依存、ソース変更が必要な問題、時間/容量/メモリ超過があれば原票を残して止める。追加ダウンロード・依存導入・有料計算なし。見込みは4–8分/0.4–1GiB。

構成後に二target・コンパイル元と実ヘッダー・書込先を確認してbuildへ進む。二拡張のSOABI、同時に作った新native共有ライブラリへの解決をnm/readelf/ldd等で確認する。R125の旧nativeや別Python用のバイナリを混ぜない。lddの表記はPath.resolveで実体を比較する。構築完了後、既存の公開verify_python.pyをwriter/extension引数なしで起動し、通常importのコード経路を使う。

Python -Sはsiteだけの省略と明記し、-vログでstageのvc_reader/__init__.pyとreader/__init__.pyが実行されることを確認。reportのimport_isolated=false、実writer/両拡張のパスとSHA、NumPy版を記録する。小さいZarrのpreserve_existing=TrueでL0/L1のSHA・mtime・画素17/9保持とL2生成、既定入口と既存4引数native呼出しを既存チェックに従って確認する。指定上流テスト関数のAST本体の実行も同じ一回に含めるが、pytestランナー全体やwheel導入と呼ばない。

本票と experiments/vesuvius/r009/20261113-normal-python-runtime01/ に入力/構成/構築/実行の原票・独立確認しやすい出力と保存fixture・費用・lab候補を残す。主担当が別照合・採否・登録する。新CT、GPU、データ取得、モデル、公開/応募/PR/外部メッセージ/subagentなし。161の公開更新確認は別に保留中で、今回はその候補を書き換えない。

今回の委任モデルは gpt-6.1-sol / xhigh。計画は得たが標準Python拡張構築と初期化の初回実行を含み、版/ABIと資源境界を扱うため。同じ162担当へ引き継ぎ、研究を一件ずつ進める。

## 結論（2026-11-13 JST）

[一次・実行] 固定14d4e725にR009を適用したreaderの標準CMake `_catalog` と `_reader` が同じUbuntu CPython 3.12用に構築できた。両拡張の初期化シンボルと、`_reader` の新native共有ライブラリへの解決を確認。実 `vc_reader/__init__.py` と `vc_reader/reader/__init__.py` を通常importして、凍結 `verify_python.py` が一回で終了0。`--writer` と `--extension` は省き、`-S` でsite初期化だけを省いた。結果は `import_isolated=false`、実writerと拡張2件、NumPy 2.2.6を記録した。[ELF照合](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/link-check.json) · [通常import照合](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/verify-check.json)

[一次・実行] Trueで既存L0/L1全7ファイルのSHA-256・mtime、復号画素17/9を保持し、shape/chunks `(1,2,2)` のL2をgzip 7・スラッシュ区切りで生成した。既定ではL1のメタデータをL0設定で再初期化し、従来の4引数native呼出しも成功。上流の指定回帰関数のAST本体を実APIで実行した。全pytest、wheel構築・導入、他Python/OSは未検証。[保持・既定・4引数の結果](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/result.json)

[一次・独立照合] 主担当が両初期化の実ログ・固定SHA、実拡張とwriterのSHA、Linuxの既存7ファイルのSHA・mtime、保存22ファイルの集合と本文、新階層メタデータを確認した。標準ライブラリでgzipと無圧縮の全80画素を直接復号し、17/9と一致した。別照合0.615秒、最大RSS62,783,488 B、製品再起動0。[独立照合](../experiments/vesuvius/r009/20261113-normal-python-runtime01/lead-check.json)

## 根拠・詳細

[一次] 固定reader 772本文のSHA・mode、Delta3D 137本文コピー、R125の同版開発ヘッダー・保存配布物3件・SOABIを照合。新C/ext4上の構成16.290秒、ビルド762.035秒、試験2.180秒。最大RSS 3,201,777,664 B。ビルド時間は162の4〜8分見積もりを超え、承認上限900秒内。最終作業割当363,208,704 B、C:空き42,636,468,224 B。新規取得・追加依存導入・追加クラウド支出0。D:は専用mountで読取、各工程はネットワーク分離・CPU1・AS4 GiB。[入力・手順・実測](../experiments/vesuvius/r009/20261113-normal-python-runtime01/README.md)

## 取得の経路

研究160の固定ソース・Delta3D、R125で公式配布元から保存した同版Pythonヘッダーとnanobind・NumPyを使用。製品ソースとCMakeに今回の追加変更はない。[入力SHAと版](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/prepared.json)

## メモ

- `run01` は事前確認のdpkg表示書式で停止。元票の標準出力ではlibpythonだけに `:amd64` が付き、計測側で全件へ付けた表示と一致しなかった。製品工程の起動は0回。R125と同じ `dpkg-query -W` の出力を比較する計測変更後、別 `run02` を開始した。[停止原票](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run01/failure.json)
- `run02` の作業先は `/home/tomoy/r009-normal-python-run02-678qsuuz`、runner PID 1637。構成PID/PGID 1647が16.290秒で終了0。コンパイル元・ヘッダー・出力先を照合後、ビルドPID/PGID 1817を開始。各工程の開始・期限・引数・ログを原票に保存。[構成照合](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/configure-check.json) · [ビルド開始](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/build-start.json)
- 試験PID/PGID 2305は終了0。計測側が `-v` のパスに引用符を想定したため後処理が停止した。実ログを照合し、同じ製品実行の出力だけを読み直して両初期化を確認し、fixture 22件を保存した。構成・ビルド・製品試験の再起動は0回。[初回後処理停止](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/failure.json) · [完了票](../experiments/vesuvius/r009/20261113-normal-python-runtime01/run02/complete.json)
- 原票と主担当の照合を保存し、lab登録候補を作成した。[lab登録候補](../experiments/vesuvius/r009/20261113-normal-python-runtime01/record.json)
