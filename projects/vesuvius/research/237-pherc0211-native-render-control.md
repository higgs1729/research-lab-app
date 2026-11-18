Status: resolved
担当: 研究（r237_pherc0211_native_render / Astra xhigh / 2026-11-15）

# 237: PHerc0211の局所入力を、公開時のネイティブ描画と同じ演算で作れるか（2026-11-15）

## 依頼

- 問い: R236の公開φ入力と局所移植入力に残る最大1 DN差を、公開時のnative rendererに基づく有限の介入で説明・解消し、親面の別領域を評価するための入力経路を確立できるか。
- 背景: R236は入力の厳密比較が843/262,144値で不一致。その失敗を保持した別の近似入力計画でも、同一GPUの確率差mean0.0006942505が事前基準0.0005を超え、3既知参照+2対比較の5forwardで停止した。未知187/既知φ面36は未実行で、候補の有無は未評価。閾値不通過と実際の読字品質の悪化は同じではなく、後者は未評価。専用台xpbuoy304rmuazはGET404/name0まで確認済み。R236を後から合格へ書き換えない。
- 狙い: Python近似の閾値を緩めるのでなく、公開時の演算経路の具体的な違いを一つ検証する。既存のrenderer・ビルド・保存ソース・CTを短く確認し、借りる/小さくつなぐ方法を優先する。全面CT取得や汎用rendererの再実装へ広げない。材料の例はR236の`lead-renderer-oci/`、revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c`、保存済みv6公開入力、R235のφCT、既存WSLのツールである。調べ方はこれらに限定しない。
- 欲しいもの: 相違を生む演算や実行経路の根拠、少量で実行できる具体案、実行コードと条件・出力の照合。小さい既知対照だけで検証し、R236と同じφに加え、結果を見る前に選んだ別の公開input小領域でも確かめる。追加対照は保存済みCTの範囲で成立するものを優先し、位置/深さ/比較する全値を先に固定する。一つの対照一致から親全面・実紙面・新文字を断定しない。
- 最初に、既存実行物/ソースの利用候補、局所タイルでも全親canvas・tile位相を保てるか、必要保存量/資源を整理して主担当へ返す。根拠のある小さいCPU試験は続けてよい。新規有料計算、コンテナ全layerや大量依存の取得、未知候補の推論はこの票ではまだ実行しない。必要なら具体的なサイズ・費用を見積もる。閾値/モデル/深さの救済探索はしない。
- 制約: 研究はこの一件のみ、再委任なし。GPU0、追加クラウド費0、CPU1、既存hard commit4GiB。Linux実行ならWindowsラッパーだけでLinuxのRAM上限が担保されると扱わず、既存のLinux制限経路を確認する。初期新規保存64MiB以内、C空き2GiB下限。大きなcompile/cache/依存が必要なら先に量を返す。Dは直接のファイル読取のみ、**DでGitコマンドを一切実行しない**（partial cloneの過去検索でlazy fetch/maintenanceを発生させたR236主担当の事例あり）。新規出力はC。共有環境のinstall/update/削除や既存ビルドの変更はしない。
- 保存先: `experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/`。依頼部は保持し、結論・根拠・経路・メモを同票へ追記する。モデル出力の読字評価は本票の目的ではない。主担当が別検証してからmanifest/recordを凍結。lab/recall登録・外部公開/連絡/応募は主担当側で扱う。

## 結論

**公開のTIF-only経路とR236の局所描画に、横方向の原点を作る演算順の違いがあることを確認した。しかし、その一か所をnative原文関数で揃えても公開入力との完全一致は得られず、親面の別領域を厳密再現する入力経路は未成立のまま、この有限試験を終了する。**

[一次、2026-11-15] 作者の再現コードは `--tif-output` のみを指定する。固定rendererは横6060画素×高さ128のbandを一回の`gen`で作る。一方R236は横も128画素ごとに`gen`相当の座標原点を作り直していた。全canvasの中心が同じでも、float32での `origin + dx * scale` の演算順が変わる。[親の原文別確認](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/lead-source-branch-check.json)

| 事前固定対照 | 比較値数 | native旧tile対照の差 | native TIF band介入の差 | 最大絶対差 |
| --- | ---: | ---: | ---: | ---: |
| R236と同じφ：親XYWH `[4768,3200,128,128]` | 262,144 | 843 | 824 | 1 DN |
| 別領域：親XYWH `[4768,3328,64,64]` | 65,536 | 235 | 235 | 1 DN |

[一次計算、同日] native tileのφ入力・base XYZ・normalはR236保存配列と全一致した。native bandの両対照は、主担当が別に行った「NumPyの横原点だけをbandへ変える計算」と全値一致した。したがって、**今回の固定ビルド条件では**R236のNumPy移植と原文C++の算術は一致する。残る1,059/327,680値の差をPython言語自体、FMA、CPU architectureのいずれかに断定する根拠はない。[担当比較](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/comparison.json)・[主担当の全native照合](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/lead-native-check.json)

元renderer/containerそのものを実行した試験ではない。読字品質、親全面、正しい紙層、未知領域のインクや文字は未評価。R236の当初の失敗と未知forward未実行を保持する。追加モデルforward0、CT取得0、有料計算0、新文字0。

## 根拠・詳細

### 実行契約と保持した演算

- [一次、同日] `contract.json` SHA `3c785547faa7a76d2a34c8eb677b2f9d4d5dc59c872ccb9bfcd53e29b94fdf70` をnative実行前に保存。φと重ならない追加対照は次のY bandに置き、深さは両方+8..−7の16層、比較は全値。公開maskは全有効。CT支持の確認には座標の±1voxelを含む保守的包絡を使い、R235既存CT5キーに含まれることを確認した。公開inputのSHAもR236の固定値と一致。[実行契約](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/contract.json)
- [一次原文、同日] pinned revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c` から、warp4関数、`internal_loc`、`grid_normal_int`、`normalizeNormals`、`computeCanvasOrigin`、`validMask`、`QuadSurface::gen`、`sampleTrilinear` の11関数を抽出。改行を統一し、`sampleTrilinear` のinline macroだけを除いた。元関数本文は親が別照合した。[抽出箇所とSHA](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/source-extraction.json)
- [一次実装、同日] 最小のclassフィールドとconstructor、検証済みraw gridを読む入口、欠損を例外にするCT accessorだけを接続した。source loader、Zarr cache、TIFF writer、CLI全体は借りていない。native側で全幅6060×128の幾何を作ってから固定ROIを取り出し、CTはROI内だけを標本化した。親全面のCTは取得せず、元bandの横位相とY128位相を保持する。[実行コード](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/native.cpp)
- [一次実測、同日] φのbandとtileはbaseの3,198/49,152成分で異なり、最大0.001953125 voxel、normalは全一致。出力175値が変わり、公開対照との差は843→824となった。追加対照はtileとbandのbase/normal/全出力が一致した。小領域の位置により、この分岐差の影響が出ない場合もある。

### ビルドと資源の限界

[一次実測、同日] 既存Ubuntu WSLのGCC13.3.0、OpenCV4.6.0、`-std=c++17 -O2 -ffp-contract=off -I/usr/include/opencv4 -lopencv_core` を一組だけ使用。これは今回の対照用設定であり、作者imageの設定とは主張しない。CPU affinity1・Linux `RLIMIT_AS=(4GiB,4GiB)` を実測し、既存`native.py`のdeadline/process-group停止を再利用した。ビルド/各実行上限120秒、`unshare -Urn`でネットワークなし、TMPDIR/TMP/TEMPはC上の専用`tmp`。[ビルド条件](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/build-settings.json)・[依存の版/SHA](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/dependency-identities.json)

- build 6.772秒・peakRSS208,175,104 B、tile 2.627秒・23,666,688 B、band 0.384秒・62,128,128 B。全childは終了回収済み、一時ファイル残存0。Windows準備/比較も既存hard process commit4GiB・CPU1で実行。
- 研究フォルダは独立検証を含む凍結前スナップショットで2,971,242 B、C空き4,414,902,272 B。最終値はmanifestに保存。初期64MiB枠・実行見積10MiB内、C空き2GiB下限を維持。[資源スナップショット](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/resources.json)
- 保存OCIの全layer圧縮量は2,764,426,945 B。本体buildに対応するlayerは1,608,134,412 Bで、全取得は実施しなかった。config historyにある本体buildは `cmake -DVC_WITH_CUDA_SPARSE=off -DVC_USE_OPENMP=ON -GNinja /src && ninja`。flatboiに別記されたRelease flagsを本体へ転用しない。実最適化設定はpinned repositoryのCMake等に依存し未確認。GH200は公開推論の検証環境で、元CT描画ホストのarch/compilerを示す根拠ではない。

### 独立検証と終了判断

[一次・主担当、同日] source branchを保存ZIPのhelperとrenderer原文から確認した後、native結果を読む前にNumPyの横originだけを変更して両対照を計算した。その後、原文11fragment・include/build hash、tile/band計655,360入力値、φtileの全XYZ/normal、両bandと別NumPyの全値を照合した。[別NumPy計算](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/lead-numpy-band-check.json)・[native別検証](../experiments/vesuvius/discovery/20261115-pherc0211-native-render-control01/lead-native-check.json)

[判断] sourceに基づく一つの介入の効果を確認したため本票をresolvedとする。strict入力経路の成功を意味しない。追加compile、flag/式の掃引、閾値緩和、未知候補の推論は行わない。次の投入を選ぶなら、pinned CMake等から本体の実flagsを先に特定するか、別の既存公開入力を使うかを主担当が判断する。実作者binaryを取る案は上記layer量と依存の未確認を踏まえ、別途見積が必要。

## 取得の経路

R234 ZIPの親tifxyz/公開mask、R236の保存公開inputと旧renderer原文、R235のCTを直接読取した。新規remote取得0、D読取/書込/Git実行0。初回準備はWindows既定CP932でUTF-8 C++原文を読んだ時点で停止したため、既に保存した契約/gridは保持し、UTF-8指定の抽出専用入口で続行した。失敗receiptも保存。共有install/updateや既存buildの変更なし。

## 本人への質問

なし。主担当の別検証完了後の指示で本票・README・manifest・登録候補recordを凍結する。lab/recall登録、外部連絡、公開、応募はこの担当では行わない。

## メモ

- 2026-11-15 着手。共通CONTEXT/instruction-triage、AGENTS、system/lead、研究スキル、README、研究体制設計とR235/R236を確認した。R236出力は読取だけとし、Git・lab・recall・GPU・追加クラウドの実行なし。C空きは開始時約5.13GiB。
- 保存済みOCI receiptは全layer圧縮量2,764,426,945 B。初期64MiB枠で全部取得する候補は除外する。既存Linux制限の実装は `experiments/vesuvius/r005/20261112-ct-render01/native.py` の `environment`（CPU affinity一個・RLIMIT_AS 4GiB）と `bounded`（process group kill付きdeadline）で確認。既存native binaryは新しいrenderer経路のため、そのまま旧版再現とは扱わない。
- 13:36UTC native実行前にφ128²と追加64²、+8..−7の全16層、全値exact比較を固定。準備末尾のcodepage失敗を回復し、原文11関数の隔離harnessを一回compileした。共有ビルドは変更しない。
- TIF-only分岐は全幅band、R236は横128tileと判明。親も分岐を独立確認し、同じ固定対照で横originだけの別NumPy計算を行った。
- nativeはtile→bandの二回で終了。φ843→824差、追加235→235差、全max1DN。exact経路未成立として親へ報告し、追加compileなしで閉じる判断を受けた。
- 13:41UTC 主担当は全native出力と原文を別確認し、manifest/record凍結へ進むよう指示した。R236成果物は不変、モデルforward追加0、未知ROI評価なし。
