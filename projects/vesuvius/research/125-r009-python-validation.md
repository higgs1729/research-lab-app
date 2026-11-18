Status: resolved
担当: 研究・実装検証（2026-11-13、r009_resume_fix）
Blocked by: 124

# R009: Python別添の実バインディングを小さい隔離ビルドで検証できるか

## 依頼

2026-11-13（日本時間）。R009のC++/CLI修正は実行検証を進めたが、vc_reader/AGENTS.mdに従って用意したPython入口の別添は、適用・構文までで実ビルド/実行が未確認。公開候補をまとめる前に、この境界を低コストでどこまで埋められるか確認する。研究124完了後に着手する。

対象は `experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid-python.patch`。現行コードはnanobind >=2.10.2を使い、WSL UbuntuのPython3.12に開発ヘッダー・nanobind・NumPyがない。既存D:ネイティブライブラリとC:のR121 pyramid.oは利用できる。CMake/pyprojectと実コードを読み、全体再ビルドを避けて、実際の変更済みbindings.cppをビルド・ロードし、新引数の実動作を確認する最小経路を選ぶ。

可能なら実Python wrapperと追加pytestを使う。パッケージ全体のimportには未作成の_catalog等も必要となるので、対象の拡張と変更された実関数を隔離して確認する方法も認める。その場合は実関数・実native呼出しを用い、偽のcalleeや条件式の複製を成功根拠にしない。隔離した範囲と、未確認のパッケージ初期化/完全インストールを明記する。

小さいローカルZarrを使い、preserve_existing=Trueで既存の異なるcodec/separatorのarray metadataとデータを保持して欠落レベルを作ること、既定Falseの既存入口の契約を保持することを確認する。追加のCT描画・GPU・大きいデータは不要。失敗は原票を保存し、範囲内で小さく解決する。新しい環境のために実験条件・過去原票・登録済みパッチを書換えない。

新規に必要な小さいヘッダー/ビルド依存の取得は、公式の配布元から累計64MiB以内で認める。URL、版、SHAを残す。C:の隔離先に展開し、D:や復元WSLのシステム環境を変更しない。取得にはネットワークが必要だが、ビルドと試験はネットワーク分離する。既存バイナリ・ヘッダー・ABIの対応を先に確かめ、違うPython/OS用のヘッダーを流用しない。大きな全体ビルドや恒久的な依存導入へ広がるなら、必要な範囲を報告して止める。

上限はCPU1・AS4GiB・core0、コンパイル/リンク合計600秒、試験120秒、C:作業1GiB。追加クラウド見積0円、CT取得0。モデル/effortはgpt-6.1-sol / xhigh。既存ネイティブ資産を再利用したPython拡張の新しいビルド経路とABI・検証境界の判断を含むため。追加subagent・外部公開/送信は不可。準備と未完了点を早期にC:へ残し、依頼を保持して結論と原票・費用・限界を追記する。再利用用の実行手順とlab候補を返し、候補の採否は主担当が決める。

## 結論（2026-11-13 JST）

［一次・実行］パッチ済みの `bindings.cpp` から作った実nanobind `_reader` と、初期化に必要な実 `_catalog` をUbuntu CPython 3.12でロードし、パッチ済み `writer.py` を実行できた。`preserve_existing=True` ではgzip 7・スラッシュ区切りのL0と無圧縮・ドット区切りのL1について、全メタデータ・チャンクのSHA-256と更新時刻、復号画素17・9を保持し、L0のgzip 7・スラッシュ区切りでL2を作った。引数を省略した公開関数は既存のメタデータだけのL1をL0の設定で初期化し、L2も作った。既存4引数の拡張関数も成功した。[実行結果](../experiments/vesuvius/r009/20261113-python-validation01/run01/test03/checks.json)

［一次・実行］別添の `test_create_pyramid_levels_preserves_existing_arrays` はパッチ済みテストソースから元の `FunctionDef` を取り出し、実 `ZarrWriter`・`ZarrReader`・公開関数を渡して本体を通した。ソースとASTのSHA、実ロードした両拡張のSHAを保存した。隔離環境ではパッケージ探索パスを指定し、実関数・依存モジュール・実拡張を使った。`vc_reader` と `vc_reader.reader` の通常初期化、pytestランナー、完全インストール、wheel、他OS・他Python版は未検証。[実行条件](../experiments/vesuvius/r009/20261113-python-validation01/run01/test03/result.json) · [再試験手順](../experiments/vesuvius/r009/20261113-python-validation01/README.md)

## 固定mainへの適用

［一次・Git］固定main `0080fa393724575d4f19059d91402757f9351b28` のGit treeとD:の元ファイルを比較し、`bindings.cpp`、`writer.py`、`test_zarr_writer.py`、renderer、pyramid実装、ヘッダーの6点でblobが一致した。READMEのローカルblobは異なり、変更対象のcapability rowは同じだが、別添のhunk文脈に含まれる隣接行にD:側だけ `recoverDirectory` があった。元別添は固定mainでこのhunkだけ失敗した。[版照合](../experiments/vesuvius/r009/20261113-python-validation01/run01/source-provenance.json) · [初回の適用ログ](../experiments/vesuvius/r009/20261113-python-validation01/run01/fixed-main-apply.log)

［一次・Git］元patchを保存し、未変更の文脈1行だけを合わせた固定main版を別ファイルに作った。固定mainのC:コピーへR007→R121→R123→Python固定main版を順に `git apply --check`・適用できた。適用後のbindings、writer、テスト、ピラミッド実装・ヘッダーのSHA-256が実ビルド用ステージと一致した。[固定main版のPython差分](../experiments/vesuvius/r009/20261113-python-validation01/resume-pyramid-python-fixed-main.patch) · [適用証拠](../experiments/vesuvius/r009/20261113-python-validation01/run01/fixed-main-apply.json)

## ビルド経路・資源

［一次］実行中と同じUbuntu CPython `3.12.3-1ubuntu0.17` amd64の開発ヘッダー、nanobind `2.10.2`、NumPy `2.2.6` を公式配布物から取得しC:に展開した。実 `bindings.cpp` と `_reader` の初期化が必要とした実 `catalog_bindings.cpp`、nanobindのみをコンパイルし、R121 `pyramid.o` と既存D:のnative・thinning・catalog・sftpをリンクした。両拡張の実ロード、変更ヘッダーのコンパイル依存、ピラミッドの3シンボルを記録した。最初のコンパイル・ロードの停止票を保持し、multiarch includeの追加、既存thinningリンク追加、既存資産での `_catalog` 構築で解決した。[ABI原票](../experiments/vesuvius/r009/20261113-python-validation01/run01/abi-inputs.json) · [取得原票](../experiments/vesuvius/r009/20261113-python-validation01/run01/downloads.json) · [最終ビルド](../experiments/vesuvius/r009/20261113-python-validation01/run01/build04/result.json)

コンパイル・リンクを含む4回のCMakeビルドの壁時間合計344.444秒、最大RSS 3,201,736,704 bytes。試験3起動で壁時間合計4.835秒、成功回2.336秒、最大RSS 122,896,384 bytes。CPU 1、AS 4 GiB、core dump 0、ネットワーク分離。C:作業356,436,451 bytes。依存と配布メタデータ22,572,530 bytes。固定mainのREADME取得104,778 bytesと上限で止めた取得65,537 bytesを加えた本文受信量は22,742,845 bytes。D:とWSLのシステム環境は読み取りのみ。CT取得、全体再ビルド、追加クラウド支出はいずれも0。[lab登録候補](../experiments/vesuvius/r009/20261113-python-validation01/record.json)

## メモ

- 2026-11-13、WSL Ubuntu CPython 3.12.3の同版ヘッダー、nanobind 2.10.2、NumPy 2.2.6をC:へ隔離展開。ABI、取得URL・版・SHA、試験スクリプトを `experiments/vesuvius/r009/20261113-python-validation01/` に保存。
- `build01` は実 `bindings.cpp` のオブジェクト作成後、nanobind本体にUbuntu multiarchヘッダーが届かず停止。`build02` は対象includeだけを修正してリンクに成功し、`test01` でthinningの2シンボル不足を確認。`build03` は既存のthinning静的ライブラリを追加して再リンクし、`test02` で実 `_reader` 初期化に `_catalog` が必要と判明した。既存オブジェクトとライブラリを借りる `_catalog` 限定ビルドを継続。
- 固定mainのGit treeを基準にR007/R121/R123の適用成功。元Python差分はREADMEの隣接context一行が違うため停止。該当contextのみを合わせた `resume-pyramid-python-fixed-main.patch` で4差分が適用でき、Python実装と回帰テストは元差分を使ったビルド用C:ステージと同一。
- `build04` で既存 `_reader` のELFを再利用し、実 `_catalog` を追加。`test03` が終了0。再利用用 `verify.py` と実行手順、lab登録候補を保存。
