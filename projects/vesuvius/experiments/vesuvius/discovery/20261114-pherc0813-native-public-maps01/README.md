# PHerc0813 z12496_w020の公開予測と面座標

2026-11-14 JST。[一次・目視] 担当と主担当が二方向を原寸10枚で別々に確認した。幅の広い反応塊と短い弧・分岐が見える。forwardの概略 `XY=[512,660,640,870)` のY/T状と `[2080,690,2220,835)` の弧では輪郭や幅が続かず、reverseの `[1180,950,1390,1020)` は拡散した水平帯にとどまる。独立字画、字間と方向の揃う行、CTへ移すROIは選定せず、この一面で終了。座標は左上原点、ゼロ始まりの半開区間 `[x0,y0,x1,y1)`。 [全体図（1:4）](review01/overview.png) [原寸図と座標索引](review01/pixels.json) [主担当の別目視](lead-visual.json)

## 固定入力

| チームの層順 | 配布TIFF | 幅×高さ / dtype | バイト | LFS SHA-256 |
|---|---|---|---:|---|
| forward | [z12496_w020_reverse.tif](originals/z12496_w020_reverse.tif) | 2560×1120 / uint8 | 1,300,494 | `cbd3f4b32c4e8f0f45d4c1367e87ee5df4103c68b19e07f59da18d8a32b48d56` |
| reverse | [z12496_w020.tif](originals/z12496_w020.tif) | 2560×1120 / uint8 | 1,135,632 | `a87ad251b1e17ed416349c5a0c982bf591f8b737b4e91cf74a25ed4097ec5feb` |

[一次] 固定HF `dd968475bca14ccfbfd7b06cc6ba87723bb25642` とmesh `620769e2e1e70d1e61b588092229cb76d3af4804`。作者の工程は umbilicus＋lasagna の spiral fit → flatten → 一巻きごとのTIFXYZ。indexで繊維目視 `aprova`、1.73 cm²。公開予測は `vc_render_tifxyz` scale 1、L0、31層、step 1、法線反転なしで作り、seed43 step060000の層7:24を使用。順逆は作者の9月15日訂正を適用。作者自身の文字screenを通過した配布例はない。 [作者の方法](../20261114-unread-lead-reselection01/originals/pscamillo-mesh-method.md) [予測カード原文](../20261114-unread-lead-reselection01/originals/pscamillo-hf-readme.md) [固定取得原票](acquisition.json)

[一次・推論] 公式PHerc0813のscanは `20250720160015`、掲載volumeは `20250821151723`（9.362 µm、113 keV）。作者の生成法・公表の解像度と整合する。同面のmetaには使用volume URLやrenderer commitがなく、当時のコマンド原票と画素単位のCT一致は未確認。 [公式データ原文](../20261114-unread-lead-reselection01/originals/official-PHerc0813.html) [面メタデータ](originals/mesh/meta.json)

## 画素とXYZの検算

[一次・実測] XYZは128×56 float32、meta scaleは両軸0.05。保存rendererのscale 1・L0・crop/XY回転/反転なしの式では幅・高さを `round(grid_wh / scale)` とし、2560×1120になる。surface centerは (1280,560)、canvas左上は centerから `(W-1,H-1)/2` を引いてからscaleを掛ける。節点の連続座標は概ね `(u,v)=((x+0.5)*0.05,(y+0.5)*0.05)`。保存コードと同じfloat32丸めで、画素 (1850,550) の四節点の双線形位置は元ボクセルXYZ (3372.214947,3271.628152,12941.100107)。主担当が元XYZから別計算し、差は4.55×10⁻¹³ voxel。これは名目の座標式と実節点の検算で、当時のrendererの再実行や紙の物理表面の確認は未実施。 [rendererの原点とfull canvas式](../../r002/20261111-source-review/volume-cartographer__apps__src__vc_render_tifxyz.cpp) [QuadSurfaceの変換式](../../r003/20261111-source-review/volume-cartographer__core__src__QuadSurface.cpp) [プローブとbbox](review01/pixels.json) [主担当の別検算](lead-check.json)

[一次・実測] 有効節点5,138、四隅有効の四辺形4,946。四隅有効とした支持は1,978,400画素、bbox `[20,60,2520,1040)`。両予測の非ゼロマスクは同一の2,582,528画素で、支持域を全包含する。域外の604,128画素にも最大220の応答がある。非ゼロマスクは左上原点64×64の637ブロック（末端は画像境界で切り詰め）で完全再現し、うち93ブロックは四隅有効域と交差しない。原因は未確認。 [四隅有効域画像](review01/four-valid-nodes.png) [ブロックと値の原票](support-check.json)

## 原寸の再閲覧

各ファイルは上が公式forward、下がreverse。画像パネルは原TIFFと全値一致し、階調は0–255固定。個々の全画面を [forward](review01/forward.png) と [reverse](review01/reverse.png) で閲覧できる。

| y | x=0 | x=512 | x=1024 | x=1536 | x=2048 |
|---|---|---|---|---|---|
| 0 | [原寸](review01/native-tiles/x0000-y0000.png) | [原寸](review01/native-tiles/x0512-y0000.png) | [原寸](review01/native-tiles/x1024-y0000.png) | [原寸](review01/native-tiles/x1536-y0000.png) | [原寸](review01/native-tiles/x2048-y0000.png) |
| 560 | [原寸](review01/native-tiles/x0000-y0560.png) | [原寸](review01/native-tiles/x0512-y0560.png) | [原寸](review01/native-tiles/x1024-y0560.png) | [原寸](review01/native-tiles/x1536-y0560.png) | [原寸](review01/native-tiles/x2048-y0560.png) |

保存入力からの再実行はリポジトリルートで行い、新しい出力名を指定する。

```powershell
$r188 = 'experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01'
python -B tools/research/run_windows.py "$r188/review02-process.json" "$r188/review.py" "$r188/review02"
python -B tools/research/run_windows.py "$r188/support02-process.json" "$r188/check_support.py" "$r188/review02" "$r188/support02.json"
```

取得は固定GitHub contentsの応答でXYZの長さを先に照合し、公開Git blob/LFS SHAを検証した。受信2,531,901 B（XYZ 86,832 B、メタとファイル一覧8,943 B、予測2,436,126 B）、通信工程6.806秒。原寸生成・支持照合は合計8.954秒、1 CPU、数値スレッド1、commit 4 GiB上限。Windows入口で同階層 `common.py` と既存R186計画を解決した。LZW TIFFは既存Pillowで読んだ。CT取得・描画・新規推論・依存追加・ビルド・支出・外部公開0。 [取得前サイズ](acquisition-plan.json) [取得実行](acquisition-process.json) [原寸実行](review-process.json) [支持照合実行](support-process.json)
