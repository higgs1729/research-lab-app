Status: resolved
担当: 研究（r238_pherc0211_build_arithmetic / Astra xhigh / 2026-11-15）

# 238: 公開rendererのビルド設定に沿う演算で、残るCT入力差を説明できるか（2026-11-15）

## 依頼

- 問い: R237のnative小対照に残った最大1 DN差は、公開時rendererのビルド設定や積和演算の違いで説明できるか。説明に基づく有限のCPU介入で、公開入力と一致する局所経路を作れるか。
- 背景: R236は843/262144値の入力差を残し、後続GPU対照でもmean0.00069425>0.0005で停止。未知領域は未推論。R237では公開helperがTIF-only全幅bandであるのにR236が128列tileで原点を再設定していた分岐差を確認。原文関数11個を用いたGCC13.3/OpenCV4.6/-O2/-ffp-contract=offのharnessと別NumPy計算は完全一致したが、TIF bandのφ128²×16で824値、別対照64²×16で235値の1 DN差が残った。branch変更だけでは厳密再現は未成立。既知の作者GH200は推論の検証環境であり、CT描画ホストのCPU/arch/compilerを示すとは限らない。
- 最初の調査: 保存済みOCI configと固定revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c` のビルド原文から、対象rendererの最適化/CPU命令/浮動小数点設定を確認する。OCI historyではvc本体は `cmake -DVC_WITH_CUDA_SPARSE=off -DVC_USE_OPENMP=ON -GNinja /src && ninja` で、別のflatboi用Release設定を本体設定と混同しない。既存資料を優先し、足りなければ固定commitの小さい原文をCへHTTPS取得する。候補は例であり調べ方を限定しない。DのGitコマンドは禁止。
- 実験: 原文に根拠がある実行条件が一つ具体化できた場合だけ、既存R237のharness/描画位置を保持した一つの整合ビルド案を主担当へ返す。主担当確認後、同じφ/別対照と、結果を見る前に幾何と既存CTの支持から選ぶ新しい非重複の公開小領域を比較する。可能なら元のビルド設定に沿う単一介入だけで因果を切り分ける。根拠なしのcompiler flag、FMA挿入、深さ、補間方式の総当たりはしない。
- 欲しい成果: 元の設定として確認できたものと未確認のもの、前の設定との差、差を説明できた/できないという結果、再利用できるコードと入力契約。元container自体を実行していなければその旨を明記する。入力差の検査と文字の読める品質を混同しない。厳密一致に達しなくても既存の失敗を保持する。
- 制約: この研究一件のみ、再委任なし。GPU0・新規有料計算0・未知領域のモデル推論0。最初は新規保存64MiB以内・C空き2GiB下限・CPU1/既存Linux RLIMIT_AS4GiBとprocess-group deadline。新規CT本文の取得は初期計画に含めず、既存原票とファイルを読取再利用する。原文/ライブラリを得るための巨大image layer取得、共有install/update、D書込み、既存build変更は禁止。必要なら具体的な取得量を先に主担当へ返す。作業・compiler一時出力もC配下。
- 保存先: `experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/`。依頼は保持し、結論/根拠/経路/メモを同票に追記。R236/R237は凍結済みとして変更しない。主担当の別照合後にmanifest/recordを凍結。lab/recall登録と外部公開/連絡/応募は主担当側。

## 結論

**元CMakeから条件を具体化し、その条件に沿うGCCビルドを一組試したが、公開入力との完全一致には到達しなかった。** 本体既定Releaseの`-O3 -march=native`・LTOと、Slicingだけの`-ffast-math`を保持するため11原文関数を4つの翻訳単位へ分けた。旧flagsの分割基準はR237と全一致したが、整合設定では公開入力との差が全393,216値中1,256→1,371に増えた。いずれも最大1 DNである。

| 対照 | 親XYWH | 比較値数 | R237 flagsの分割基準 | 原文に沿う整合設定 |
| --- | --- | ---: | ---: | ---: |
| φ | 4768,3200,128,128 | 262,144 | 824差 | 881差 |
| R237の別対照 | 4768,3328,64,64 | 65,536 | 235差 | 254差 |
| 今回の新しい非重複対照 | 4832,3328,64,64 | 65,536 | 197差 | 236差 |

[一次計算、2026-11-15] ビルド条件を変えるとfloat32の座標・法線とCT出力が変わることは確認した。しかし複数の原文条件を一つの整合設定として変えたため、FMAだけを単独原因として分離した試験ではない。また元imageのbuild CPU/compiler/OpenCV版を同定していないので、元作者環境そのものを再現したとも言えない。入力経路は未成立として既存の失敗を保持し、追加flag/式の探索を行わない。[基準照合](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/baseline-check.json)・[整合設定照合](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/aligned-check.json)

GPU/新CT/有料計算/モデルforwardは0。未知ROI、読字品質、紙層の正しさ、インクや文字の有無は未評価。新文字0。

## 根拠・詳細

### 原文で確認できた条件と未確認の条件

- [一次取得、同日] 固定revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c` のroot/core/apps CMakeと6つのmodule、計9本文38,241 BをHTTPS取得し、URL/HTTP status/長さ/SHAを保存した。source候補`volume-cartographer/Dockerfile`は404で取得せず、その原票も残す。[取得原票1](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/first-http.json)・[2](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/second-http.json)・[3](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/third-http.json)
- [一次原文、同日] `VCCompilerFlags.cmake`はbuild type未指定時にReleaseを選び、x86系globalに`-std=c++23 -march=native -pipe`、Releaseに`-O3`とLTOを加える。`GCCToolchain.cmake`のLTOは`-flto=auto -ffunction-sections -fdata-sections`。`ReleaseUnsafe`にだけ定義されたglobal fast-math群は既定Releaseへは適用されない。[CompilerFlags原文](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/sources/volume-cartographer/cmake/VCCompilerFlags.cmake)・[GCC原文](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/sources/volume-cartographer/cmake/GCCToolchain.cmake)
- [一次原文、同日] `core/CMakeLists.txt`は`Slicing.cpp`のsource propertyだけに`-O3;-ffast-math`を追加する。`QuadSurface.cpp`や`Geometry.cpp`にはこのsource propertyは付かない。`vc_render_tifxyz`は`vc_core`へlinkする。[core原文](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/sources/volume-cartographer/core/CMakeLists.txt)・[apps原文](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/sources/volume-cartographer/apps/CMakeLists.txt)
- [一次、同日] 保存OCI historyの本体buildはbuild type/compilerを明示せず、`VC_USE_OPENMP=ON`でCMake/Ninjaを呼ぶ。flatboi用の別Release指定を本体へ流用していない。原文にはGCC/Clangの分岐があり、元imageで生成されたcompile_commandsやCPUを実物確認してはいない。今回のGCC branchは、既存GCC13.3に原文条件を適用する対照案である。
- [一次実測、同日] ローカルGCC13.3の`-march=native`はalderlakeに展開され、FMA/AVX2有効、AVX512F無効、`-ffp-contract`の既定はfastと表示された。作者のGH200という記述は推論検証環境の情報であり、CT描画環境と結び付けない。[compiler metadata](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/compiler-probe.json)

### 事前契約・実装・比較

[一次、同日] `proposal.json` SHA `d5f031b6704c22f2d9cd17712d75ec367e2dfe888a81b9ce9ada04b9b1d030f8` に旧2対照と新対照、+8..−7全16層、比較する全値を保存した。新対照はR237の別対照のすぐ右で、両旧ROIと非重複。mask全有効、保守的包絡の6CTキーがR235保存分に含まれ、全SHAが取得原票と一致する。主担当は原文9件・6CT・非重複を別確認して実行を承認した。[契約](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/proposal.json)・[主担当確認](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/lead-plan-clearance.json)

`Geometry`、`QuadSurface`、`Slicing`、`renderer`相当の4TUへ原文関数を分け、sampling loopだけをSlicingへ移した。class/file accessorはR237の最小adapterを保つ。native full-width bandの座標計算を保持してROIだけを標本化する。基準ビルドの旧2対照は入力・base XYZ・normalすべてR237と全一致したので、構成変更による数値差がないことを確認してから整合設定へ進んだ。[構成差分の記録](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/source-adaptation.json)

整合設定はglobal `-std=c++23 -O3 -DNDEBUG -march=native -flto=1 -ffunction-sections -fdata-sections -fopenmp`等、Slicingだけ`-O3 -ffast-math`追加とした。LTOのauto→1はCPU1維持のためで、debug用`-g3`/frame/unwind/type flagsは出力増大を避けて省略した。これらの差と全application依存を含まない点を契約に明記しており、作者binary同一性は主張しない。[基準の全command](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/build-baseline/settings.json)・[整合設定の全command](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/build-aligned/settings.json)

[一次計算、同日] 整合設定は基準に対しbase23,678成分、normal23,220成分、入力1,297値を変更した。base最大差0.001953125 voxel、normal最大差約1.19e−7。公開入力に対する旧誤差591値を解消する一方、706値に新差を生じた。元の残差が解決したとは扱わない。

[一次静的確認、同日] 生成binary内のFMA系命令は整合設定43箇所、基準0箇所だった。基準にも明示`std::fma`のlibm呼出しが残るので「基準はFMAを使わない」とは言わない。実際の命令が変わったことの補助証拠であり、公開入力の原因特定や単独FMA効果の証明ではない。[binary静的確認](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/binary-inspection.json)

### 資源と境界

[一次実測、同日] 基準build13.180秒/描画0.429秒、整合build29.266秒/描画1.446秒。native最大RSS297,037,824 B。Linux内でCPU affinity1とRLIMIT_AS4GiBを再確認し、各構成のcompile一式120秒、各run120秒のprocess-group deadlineを適用した。各processは`unshare -Urn`、TMPDIR/TMP/TEMPはC上専用tmp。全child回収済み、一時ファイル残存0。共有install/updateや既存build変更、D読取/書込/Gitはない。

独立検証前スナップショットは4,654,893 B、C空き8,670,654,464 B。保存見積16MiB/上限64MiB、C空き2GiB下限を守った。原文取得38,241 B以外の新規データ取得0、CT6キーは読取再利用、追加支出USD0。[資源記録](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/resources.json)

### 独立検証と主担当の終了判断

[一次・主担当、同日] 原文11関数、4TUのSHA、実compile flags（Slicingだけfast-math）、binary/object、両構成計786,432値と旧2baselineの全入力/幾何一致を別確認し、担当の全差分数と一致した。[主担当別照合](../experiments/vesuvius/discovery/20261115-pherc0211-render-build-arithmetic01/lead-output-check.json)

[判断・主担当、同日] R238の一介入を凍結し、この窓のbit-exact追究をここで閉じる。R236/R237/R238を後から合格へ変更しない。次に探索へ利用する可否は、既存1DN差とR236確率差の意味を明示し、目的と評価基準を具体化した別計画で判断する。今回の終了から閾値緩和や再GPUを自動実行しない。

## 取得の経路

元CMakeからinclude先を順に辿り、固定commitのraw URLで原文を保存した。必要なmoduleだけを読み、CMake自体のconfigureは実行しないため、FetchContent/Git/依存追加は発生していない。R237の原文関数/入力を直接読取して新Cフォルダへ接続し、同じ旧2対照のbit一致を入口gateにした。元巨大OCI layer、別compiler、別CPU命令設定の追加試行は行わない。

## 本人への質問

なし。主担当の別照合完了と凍結指示を受け、manifest/recordを保存する。登録/外部連絡/公開/応募はこの担当では行わない。

## メモ

- 2026-11-15 着手。R237は主担当の訂正後manifest `255ab4762bac83ed16a6ce029ef0b8ae7c6a4e616ef5162c0e50769f7118a491` で凍結済みとして参照し、変更しない。固定revision本体CMakeの原文を少量取得してflagsの根拠を先に確認する。開始C空き約8.59GiB。GPU/有料/未知forward/新CT/再委任なし。
- 固定commitの本体CMake9原文38,241 Bを取得。default Releaseはglobal `-O3 -march=native` とGCC LTO、Slicingだけsource property `-O3 -ffast-math`。ReleaseUnsafeの全体fast-mathとは区別した。Dockerfile候補一件404も原票保持。
- 主担当が `proposal.json` SHA `d5f031b6704c22f2d9cd17712d75ec367e2dfe888a81b9ce9ada04b9b1d030f8` を承認。Geometry/QuadSurface/Slicing/rendererの4TUへ分割し、まずR237と同じflags、次に原文に沿う一設定だけ。追加対照は親XYWH `[4832,3328,64,64]`、旧2対照と非重複、全16層65,536値。新対照を含む保守的支持6CTキーはR235保存分を使う。
- 分割baselineの旧2対照input/base/normalはR237と全一致。公開inputとの差はφ824・旧heldout235・新heldout197（全max1DN）。このgate確認後、整合設定一つのcompileへ進んだ。ローカル`-march=native`はalderlake、FMA/AVX2有効、AVX512F無効。元imageのbuild CPUと同一とは扱わない。
- 整合設定はφ881・旧対照254・新対照236差で、全max1DN。事前計画どおり追加flag/compileをせず停止した。生成binaryの静的命令確認だけを追加し、新しい数値runはない。主担当へ原票を渡して別照合待ち。
- 13:57UTC 主担当の全値/原文/flags別照合が完了。追加計算をせず凍結し、この窓のbit-exact追究を閉じる指示を受けた。未達の結果と未知ROI未評価を保持する。
