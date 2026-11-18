# R005 整数格子保持後のCT画素比較

[研究152](../../../../research/152-r005-grid-preserving-ct-boundary.md)の原票。R103の固定元領域とR150の観測なしTIFXYZを、同じR103観測rendererのlinear CPU経路で比較した。元面53045と63364を含む64×64、深さ −2、−1、0、+1、+2 voxelを用いた。

| 領域 | crop XYWH | 格子X移動 |
| --- | --- | ---: |
| R103の元領域 | 7428, 2378, 64, 64 | 0 |
| 格子保持・成分0 | 7388, 2378, 64, 64 | −2 |
| 格子保持・成分2 | 8608, 2378, 64, 64 | +59 |

元の中心座標を `float32(格子幅 / 2 / scale)` で求め、キャンバス原点と切り出し位置から実座標を再構成した。移動先は元のdouble格子原点に整数移動を加えた位置に最も近い出力画素を採用した。元ROIの同じ画素オフセットを照合する。選定はCT読込前の `plan01/` にあり、元面ID、成分、各画素の実float32格子位置と4支持点のXYZ・元面・成分を保存した。`source_grids()` はR150の観測なしTIFXYZ三枚を観測ありTIFFとハッシュ照合し、後者の元面IDを使った。

`vc_render_tifxyz.cpp` の `renderSurface` は、レベル0の等倍XYZ・頂点の有効性と法線チャンネルなしの頂点を `vc_reader` へ渡す。`grid.cpp` の `resampleRows` は各画素のdouble格子座標をfloat32に渡す。`points.hpp` の `point()` はこのlinear経路で、4点から両線形補間と局所接線の外積による法線を計算する。描画の5層は `buildOffsetList` の順、レベル0等倍、符号付き法線沿い。実標本のXYZはネイティブ観測XYZと法線に層オフセットを適用して再構成した。元と移動先のネイティブ丸め前値はそのまま比較し、出力TIFFは保存float32値を偶数丸めした結果に照合した。

## 再現

PowerShellで `C:/dev/kensyoukin` を開く。以下は新しいタグを使い、凍結原票を読み取り専用で使用する。WSLではR103の `bounded` と実行引数を借り、ネットワーク分離・1CPU・AS 4 GiB・core 0を適用する。Windows側は同研究の既存1CPU・4GiB制限ランナーを使う。

```powershell
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$r152 = '../20261113-grid-preserving-ct01'
$entry = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r005/20261113-grid-preserving-ct01/renderer.py'
python -B "$r103/run_windows.py" "$r152/plan02-process.json" "$r152/compare.py" plan plan02
wsl -d Ubuntu --exec python3 -B $entry geometry geometry02 plan02
python -B "$r103/run_windows.py" "$r152/coverage02-process.json" "$r152/compare.py" coverage coverage02 plan02 geometry02
wsl -d Ubuntu --exec python3 -B $entry render render02 plan02 coverage02
python -B "$r103/run_windows.py" "$r152/compare03-process.json" "$r152/compare.py" compare compare03 plan02 coverage02 render02
```

`geometry01/` はCT値なしの既存ネイティブ曲面XYZ/法線。`coverage01/coverage.json` は描画前の全8コーナーと ±0.001 voxelの保守的ハローの必要キーと、既存10チャンクのSHA-256。`render01/` はその検査後に実行した二つのネイティブfloat32・TIFF・観測XYZ/法線。`compare02/` は対応マスクに基づく層別・ビット単位の一致と元混合帯の測定、`sample-arrays.npz` はXYZ・法線・層XYZ・float32/uint8の検査用配列。最初の `compare01` を保持し、二度目は元対照の凍結SHA照合と混合帯の輝度範囲を加えた。再描画は行わなかった。

元の純粋支持2,816画素の5層、計14,080標本は全ビット一致した。元の混合支持1,280画素は移動先の両領域で無効。元は全5層の混合帯が非ゼロで、輝度最小値は層順に12、9、17、18、12、最大値はいずれも255。元の混合標本に移動先で対応する物理点は定義できない。元のダブル精度格子原点との微小残差はこの窓のfloat32化で消えた。別の窓・bicubic・紙面対応と判読は未検証。追加取得とビルドは0。ネイティブ実測1.816秒、Windows集計3.002秒。
