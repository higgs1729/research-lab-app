# PHerc0125 5409_5288_14587 の公開原寸比較

2026-11-14 JST。固定atlasのPHerc0125一面で、元CTを追加取得して追試する字画・行の領域を選べなかった。中央CTと中心窓の七モデル両順で、孤立した反応、繊維・割れの近傍、画像の有効領域の縁を確認した。判断はこの一面の中心窓に限る。[全モデル全体図](review01/overview.png) · [担当目視](visual-review.json) · [主担当目視](lead-checked.json) · [主担当の独立照合](lead-checked.json)

## 選んだ面

PHerc0800 R137–143、PHerc1218 R165–167、PHerc0846A R169–176、PHerc1545 R177–178、PHerc0813別来歴の `z12496_w020` R188、PHerc0846B `2768_2813_9748` R192は今回の再取得対象から外した。固定atlasのPHerc0813 `2999_3156_5096` はR188の面とは別。PHerc0343は既知対照、PHerc0306BはFirst Letters受賞済み。固定indexで一巻一公開面かつ既精査巻と重ならない0125、0191、0257を比較した。[固定atlas一覧](../20261113-next-target01/ink-atlas-index.json) · [公式受賞発表一覧](https://scrollprize.org/winners)

| 固定面 | 公式の対象CT再構成 | 作者のsheet mask比率 | 中心両順がALIVEの組 | CT・中心予測の本文 |
| --- | --- | ---: | ---: | ---: |
| **PHerc0125 5409_5288_14587** | `20250821151825` | 86.3% | 7/7 | 20,770,643 B |
| PHerc0191 2707_2976_13281 | `20250821151635` | 15.9% | 7/7 | 18,929,783 B |
| PHerc0257 3904_6108_9436 | `20250821151750` | 16.3% | 6/7（Hecate逆順はDEGENERATE） | 19,197,793 B |

三面は同じ9.362 µm CT、2184²の9.6 µm canvas、描画チャンク欠落0。PHerc0125はatlas作者の `crossness >= 0.31` のマスクで紙面構造を比較できる範囲が広く、七モデルの中心両順が揃うため、原寸を受信する前に選んだ。マスク比率は作者の紙面判定の代理値。明度やモデルの一致は字画の認定に使っていない。公式First Letters規定本文の三つのvolume IDを、既存保存本文と現行公式ページで照合した。保存したData Browser HTMLはJS表示の殻で、scan・volume詳細は公式の表示本文と固定metaを参照した。[選定原票](selection.json) · [保存した規定原文](../20261113-next-target01/prizes.html) · [現行First Letters規定](https://scrollprize.org/prizes#first-letters-prizes) · [0125公式](https://scrollprize.org/data_browser/PHerc0125) · [0191公式](https://scrollprize.org/data_browser/PHerc0191) · [0257公式](https://scrollprize.org/data_browser/PHerc0257)

## 原寸で確認した形

座標は公開canvasの左上原点、ゼロ始まりの概略半開矩形 `[x0,y0,x1,y1)`。担当は全モデルの1:8全体図、CT/Hecate/Reader V3の原寸16図と他モデルの要所12図を確認した。主担当はCT原図、Hecate逆原図、全体図、原寸6図の5領域を別に確認した。原寸データと両者の画素照合は全15画像の全面を覆う。

| 概略位置 | 同じ画素位置の観察 |
| --- | --- |
| `[870,780,1092,950)` | Hecate順とReader両版の順、d9v2順の一部に明るい塊が重なる。CTの斜めの割れ・繊維の近傍で、分離した輪郭と字間は見いだせない。 [Hecate・Reader V3](review01/native-tiles/x0546-y0546-g1.png) · [Reader V2・d9v2](review01/native-tiles/x0546-y0546-g3.png) |
| `[1270,1092,1638,1638)` | CTで裂けと異なる向きの繊維が交わる。予測の点や太い曲がりはモデル・向きで位置と輪郭が変わり、繰り返しのある行を選べない。 [Hecate・Reader V3](review01/native-tiles/x1092-y1092-g1.png) · [dense・seed42](review01/native-tiles/x1092-y1092-g2.png) |
| `[49,1650,145,2116)` | seed42/43の両順の強い縦帯はCT有効域の左端に沿う。 [seed42](review01/native-tiles/x0000-y1638-g2.png) · [seed43](review01/native-tiles/x0000-y1638-g4.png) |
| `[1260,1870,1540,2050)` | Hecate逆の角張った塊と近くの丸い塊が散在し、Readerとdenseでは同じ字画の輪郭が続かない。CTには複数の裂けと繊維束が見える。 [Hecate・Reader V3](review01/native-tiles/x1092-y1638-g1.png) · [dense・seed42](review01/native-tiles/x1092-y1638-g2.png) · [Reader V2・d9v2](review01/native-tiles/x1092-y1638-g3.png) |

## 入力と再現

固定atlas `ac5ffd7098120368216948c4e06c494bf8e67178` の `ct_mid.png` と `maps/<model>/c+0_s1_{forward,reverse}.png`。すべて2184×2184の単チャンネルuint8で、固定木のバイト数とLFS SHAに一致。原寸は0–255を維持し、タイル546²を16位置、4組（CT＋Hecate/Reader V3、CT＋dense/seed42、CT＋Reader V2/d9v2、CT＋seed43）に分けた。保存画像から読み戻し、288パネルで85,857,408値が元PNGと一致した。CTの複数組表示を除く固有の元画素値は71,547,840。全体図だけ1:8面積平均。座標・各図SHA・各パネル原点は索引に記録した。[固定画像取得計画](acquisition-plan.json) · [全タイル索引](review01/pixels.json)

面は固定survey `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の `results/meshes/PHerc0125_5409_5288_14587`。公式scan `20250720091415`、ESRF 113 keV、volume `20250821151825`。固定metaのCTは同再構成のmasked Zarr L0。描画scale .975、box `[0,2184,0,2184]`、65層、step 1.025元ボクセル。中央CTの描画bbox `[49,49,2116,2116)` は4,272,489画素、内部の8値が0なので非ゼロは4,272,481画素。主担当の初回照合でこの差を同一視した仮定を修正し、全画素を再照合した。両方向はatlasの層順で、筆記面の確定はしていない。七モデルの当該巻学習曝露はmetaで `unknown`。XYZを受信しておらず、2D画素から元CT座標への厳密な写像は未検証。[面メタ](candidates/PHerc0125-meta.json) · [固定atlasカード](../20261113-next-target01/ink-atlas.md) · [独立照合原票](lead-checked.json)

```powershell
$r195 = 'experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01'
python -B tools/research/run_windows.py "$r195/review02-process.json" "$r195/prepare_view.py" "$r195/review02"
```

候補メタ192,253 B、選定面のPNG 20,770,643 B、計20,962,896 B、通信工程34.878秒。描画・照合4.731秒、CPU1、commit上限4 GiB、最大RSS112,594,944 B。新規CTボクセル、重み、推論、GPU、有料計算、外部公開0。[候補の取得原票](candidate-acquisition.json) · [画像の取得原票](image-acquisition.json) · [処理原票](analysis-process.json)
