Status: resolved
担当: 研究（R162担当 2026-11-13）
Blocked by: 161

# R009を通常のPython importで検証する最小経路はあるか

## 依頼

2026-11-13。三件の固定上流14d4e725での標準native構築・最小動作は研究160で成功し、研究161の追加公開候補も親別照合と登録まで完了した。公開更新は本人へ確認中だが、研究停止ではない。R009のPython入口は研究125で実拡張と実wrapperを検証した一方、sys.modulesへパッケージ探索だけを登録し、通常のvc_reader/__init__.pyとreader/__init__.pyを迂回していた。利用者が普通にimportして使う範囲への未確認点を埋める、小さい次の一件を計画する。

既存の固定14dソース、研究160の新nativeビルド、研究125の同一Ubuntu Python用ヘッダー/nanobind/NumPyと実拡張、既存のPython依存を読む。通常importに必要なモジュール・native targets・import時の処理を確認し、上流の既存CMake/pyprojectを使う経路を優先する。R125の古いネイティブ依存を新14dの型へ無根拠に混ぜない。通常パッケージ初期化を通すことと、wheelのビルド/インストール、完全な依存環境の新設は別の検証範囲として整理する。

この調査では読取と静的確認、既存ツール/インタープリタの版・依存一覧の確認まで。新規コンパイル、nativeや製品Python試験、依存導入、ネットワーク取得はしない。既存のソース・生成物・登録原票は不変、D:は読取専用。全体再ビルドを直ちに繰り返さず、必要な対象だけを通常ビルドできるか、既存生成物を読取で再利用できるかを確かめる。独自shimや偽のcallee、__init__を再び迂回する方法は目的に含めない。

返す内容は一案の具体的な固定入力/ソース/依存/ABI/コマンド、使える既存資産、足りない依存があれば公式入手先と量の見積もり、必要な作業容量/コンパイル・試験時間と停止条件。通常importから既存verify_python.pyを--writer/--extensionなしで動かすか、上流の該当pytestを普通に実行する最小計画を示す。小さく成立しない場合は、根拠と未充足を示し、大きい環境作りに広げない。

成果は本票と experiments/vesuvius/r009/20261113-normal-python-feasibility01/ の読取根拠・計画・lab候補。公開済みrepo、161候補、D:と全既存原票は変更しない。外部投稿/PR/応募/公開/課金/追加subagentなし。主担当が次の実行範囲を決める。今回モデルは gpt-6.1-sol / xhigh。通常パッケージ化とABIの新たな境界を判断する調査で、160を実装した担当が同じ構築資産を引き継ぐため。

## 結論（2026-11-13 JST）

[推論] 固定14d4e725のR009適用済み `vc_reader` を単体CMakeで構成し、標準 `_catalog` と `_reader` の2ターゲットだけを依存込みで構築すれば、通常の2段のパッケージ初期化から既存 `verify_python.py` を試せる見込み。R160のreader・Delta3DソースとR125の同一Ubuntu CPython用ヘッダー、nanobind 2.10.2、NumPy 2.2.6を使用し、新規取得は0 B。次の一案はCPU1・AS4 GiB・構成180秒・ビルド900秒・試験120秒・作業2 GiBを上限とする。ビルドは約4–8分、作業0.4–1 GiBの見積もり。構成、ビルド、通常import、製品試験はいずれも未実施。[固定コマンドと停止条件](../experiments/vesuvius/r009/20261113-normal-python-feasibility01/README.md)

## 根拠・詳細

[一次] `vc_reader/__init__.py` は `_catalog` を直接読み、`reader/__init__.py` の依存が `_reader` とNumPyを読む。C++側 `_reader` 初期化にも `_catalog` が必要。対象の通常importは `_thinning` と `_transforms` のPython拡張を要求しない。上流の単体CMakeは二対象を定義し、native thinningやcatalog等を標準ターゲットからリンクする。R160のVolume Cartographer親CMakeはreaderをPython OFFで組み込む。単体構成では `vc_reader_native` をソースから構築するため、旧R125 ELFやR160 nativeバイナリを差し替える作業は含めず、R160の固定ソースを再利用する。R125の旧 `_reader` ELFのRUNPATHはD:の旧nativeを指す。[ソース・ELF読取原票](../experiments/vesuvius/r009/20261113-normal-python-feasibility01/readback.txt)

[一次] `/usr/bin/python3` とR125ヘッダーは同じUbuntu `3.12.3-1ubuntu0.17` amd64、SOABI `cpython-312-x86_64-linux-gnu`。保存公式配布物3件のSHAを照合し、展開済みmultiarchヘッダーとNumPy実体を確認。固定 `verify_python.py` の `--writer`・`--extension` を省いた経路は `importlib.import_module('vc_reader.reader.writer')` を呼ぶ。新しいstageの二つの `__init__.py` はPythonのverboseログで、writer・拡張は既存JSON出力で確認できる。wheelやpytestランナーの動作は別の検証範囲。[ABI・依存・試験の原票](../experiments/vesuvius/r009/20261113-normal-python-feasibility01/readback.txt)

## 取得の経路

R160のWSL ext4作業先と登録資料、R125のC:既存配布物・展開済み依存、固定検査スクリプトを読取。ネットワーク取得、追加依存導入、追加クラウド支出は0。元の公式配布物のURLと容量はR125に記録済み。[取得原票](../experiments/vesuvius/r009/20261113-python-validation01/run01/downloads.json)

## メモ

- 2026-11-13、上流CMakeの標準ターゲット、通常importの依存閉包、現UbuntuのABIと配布物を照合。未確認のCMake構成とELF解決、通常初期化と保持回帰を次の1回にまとめた。[lab登録候補](../experiments/vesuvius/r009/20261113-normal-python-feasibility01/record.json)
