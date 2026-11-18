# R237 PHerc0211 native TIF-band control

公開rendererのTIF-only経路は全幅6060×高さ128のbandを生成する。R236は横も128tileに分割しており、float32の座標原点の演算順が異なっていた。この分岐差を原文C++関数の小harnessで比較したが、公開入力のexact再現には到達しなかった。

| 対照 | 親XYWH | 全16層の値数 | tile差 | band差 | 最大差 |
| --- | --- | ---: | ---: | ---: | ---: |
| φ | 4768,3200,128,128 | 262144 | 843 | 824 | 1 DN |
| 結果前に選んだ別領域 | 4768,3328,64,64 | 65536 | 235 | 235 | 1 DN |

native tileφの入力/base/normalは凍結済みR236と全一致。native bandは両対照とも主担当の別NumPy介入と全値一致。残る差の原因は未同定。元imageの実行や作者のビルド設定一致を示す試験ではない。新文字、紙層、読字品質、未知モデル性能は未評価。

- `contract.json`: 実行前固定対照、深さ、既存CT5キー/公開input SHA、資源境界。
- `source-extraction.json`, `*.inc`, `native.cpp`: pinned revision `1e3f4c021f4e53bea3867772ed05f51a7e586a9c` の11関数と最小adapter。
- `build-settings.json`, `dependency-identities.json`: GCC13.3/OpenCV4.6、単一`-O2 -ffp-contract=off`設定。本体image実flagsは未確認。
- `tile-*`, `band-*`: uint8 plane0..15＝offset+8..−7、base/dirsはfloat32 C-order H×W×3。サイズはcontractを参照。
- `comparison.json`: 全値照合、R236再現、幾何とplane別差。
- `lead-source-branch-check.json`, `lead-numpy-band-check.json`, `lead-native-check.json`: 主担当の独立検証。最後の検証は原文11関数と全655360 native値を照合。
- `resources.json`: 凍結前スナップショット。最終保存量/ファイルSHAは`manifest.json`。

実行は既存WSL、CPU1/RLIMIT_AS4GiB、外部ネットワークなし（`unshare -Urn`）、build/run各120秒上限。Linux制限はWindows wrapperに依存しない。TMPDIR/TMP/TEMPを専用Cフォルダに置いた。build6.772秒/peakRSS208MB、tile2.627秒/23.7MB、band0.384秒/62.1MB。新規CT/remote取得、GPU、cloud支出、D操作、共有環境変更はすべて0。R236出力不変。

再実行する場合は本フォルダを上書きせず、新規フォルダで`prepare.py`→`run_linux.py build`→`tile`→`band`→`compare.py`を用いる。各スクリプトは保存済み資料を参照し、既存出力があれば拒否する。Windows準備/比較は`tools/research/run_windows.py`を使用。実際の初回準備にはCP932読取失敗があり、固定contract/gridを保持して`extract_sources.py`で回復したreceiptも残す。

親の確認後、同じ一介入の結果として研究を閉じる。追加compileやflag掃引、閾値緩和、未知forwardはしない。元CT描画の実flagsを知るにはpinned CMake等の別確認が必要。全OCIは2.764GB、本体build layerは1.608GBの圧縮metadataであり取得していない。
