# R238 — source-based renderer build arithmetic

固定revisionのCMake9原文38,241 Bから、既定Releaseの`-O3 -march=native`/GCC LTOと、Slicing.cppだけの`-ffast-math`を確認した。一つの整合設定を既存GCC13.3で試したが、公開入力とのexact一致には達しなかった。

| 対照 | 親XYWH | 全値数 | 分割baselineの差 | 整合設定の差 |
| --- | --- | ---: | ---: | ---: |
| φ | 4768,3200,128,128 | 262144 | 824 | 881 |
| R237 heldout | 4768,3328,64,64 | 65536 | 235 | 254 |
| 新heldout | 4832,3328,64,64 | 65536 | 197 | 236 |

全最大1 DN。baseline旧2対照はR237のinput/base/normalと全一致。整合設定では合計1,297入力値が変わり、旧誤差591を解消する一方706に新差が出た。source由来の複数flagsを一組として変えたので、FMA単独の因果には分解しない。

- `proposal.json`/`lead-plan-clearance.json`: 実行前の3ROI・全16層(+8..−7)・全比較値・既存CT6キー・資源境界と主担当確認。
- `sources/`, `*-http.json`: pinned revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c` の原文と取得原票。root/core/appsのCMake、CompilerFlags/GCC/LLVM等。Dockerfile候補1件404も保持。
- `common.hpp`, `geometry.cpp`, `quad.cpp`, `slicing.cpp`, `renderer.cpp`: R237の11関数を原文所属に沿う4TUへ分離。`source-adaptation.json`に保持点とadapter変更を記録。
- `build-baseline/`, `build-aligned/`: compiler全command、object/binary、資源/停止ログ。baseline旧2対照bit一致gate後にalignedを実行。
- `baseline/`, `aligned/`: band全幅位相を保持した局所描画。plane0..15がoffset+8..−7、u8 C-order H×W。base/dirsはfloat32 H×W×3、XYZ順。
- `baseline-check.json`, `aligned-check.json`: 全値とplane別比較、XYZ/normal、修正/新差の数。
- `compiler-probe.json`, `binary-inspection.json`: ローカルnative targetはalderlake、FMA/AVX2有効。整合binaryにFMA系43命令箇所。基準の明示std::fma/libm経路をFMAなしとは扱わない。
- `resources.json`: 凍結前の資源スナップショット。最終保存量とSHAは親の別照合後のmanifestに記載する。
- `lead-output-check.json`: 主担当が原文11関数、4TU/実flags、全786432値、旧2baselineの入力/幾何全一致を別確認。担当数値と一致。

alignedはglobal`-O3 -march=native -flto=1 -fopenmp`等、**Slicingだけfast-math**。原文の`-flto=auto`を1workerへ制限し、debug用metadata flagsは省略した。元CT描画のCPU/compiler/OpenCV版、実image binaryは未確認であり、作者環境そのものの再現と呼ばない。既知GH200は推論検証環境の記述。

CPU1/Linux RLIMIT_AS4GiB、各build一式/各run120秒上限、ネットワーク分離、C専用TMP/TMPDIR/TEMP。基準build13.180秒/run0.429秒、整合build29.266秒/run1.446秒、native最大RSS297MB。新CT/モデル/GPU/cloud支出、D操作、共有環境変更は0。R236/R237は不変。追加flags/compile/深さ/閾値の救済探索なし。

再実行は新規フォルダで行う。`prepare_plan.py`は固定入力/関数を接続し、`run_linux.py build baseline`→`run baseline`→`compare.py baseline`の旧2対照gate後に、`build aligned`→`run aligned`→`compare.py aligned`を実行する。元実行は親の`lead-plan-clearance.json`を検査している。固定済み出力の上書きは拒否する。

入力の完全一致は未成立。未知ROI、読字品質、紙層、インク不存在は未評価、新文字0。

主担当は別照合後にこの一介入の凍結と、この窓のbit-exact追究終了を決定した。既存1DN差/R236確率差を含む探索利用の可否は、目的と評価基準を具体化した別計画で判断する。R236/R237/R238を合格に書き換えず、閾値緩和や再GPUへ自動で進まない。
