# PHerc0846B 2768_2813_9748 の原寸比較

2026-11-14 JST。[一次・目視] 固定atlasのPHerc0846B一面で、元CTに戻す字画や行の候補を選べなかった。担当は原寸16図を、主担当は全体図、両順のHecate原図と原寸4図を別々に目視した。主担当は全7枚の固定SHA、原寸112パネルの33,388,992画素も別計算で照合した。CT追加、深さ探索、モデル再実行は0。判定範囲はこの一面の中心窓。 [全体図](review01/overview.png) [原寸の座標索引](review01/pixels.json) [主担当の目視](lead-visual.json) [主担当の数値照合](lead-checked.json)

## 形を確認した位置

座標は左上原点、ゼロ始まり。矩形は概略の半開区間 `[x0,y0,x1,y1)`。

| 位置 | 同じ画素の観察 |
|---|---|
| `[1092,1450,1950,1610)` | Reader V3両順の長い横帯は、CT中央層の裂けや層境界と位置・曲がりが重なる。字間や反復する輪郭は見えなかった。 [中央](review01/native-tiles/x1092-y1092.png) [右](review01/native-tiles/x1638-y1092.png) |
| `[325,640,570,820)` | Reader V3の斜めの広い反応はCTの曲がる繊維・空隙に沿い、先端と幅がぼける。 [左上寄り](review01/native-tiles/x0000-y0546.png) |
| `[220,1860,330,1970)` | Hecate forwardの強い二塊は輪郭が不規則で孤立する。Reader V3とseed42で対応する字画形を選べなかった。 [左下](review01/native-tiles/x0000-y1638.png) |
| CT表示範囲の外周 | seed42両順の強い帯は外周に沿って長く続き、内側にはぼけた塊が散在する。 [右下](review01/native-tiles/x1638-y1638.png) |

## 入力・来歴

- [一次] SharpMeow/first-letters-ink-atlas固定版 `ac5ffd7098120368216948c4e06c494bf8e67178`。`kbh-PHerc0846B_2768_2813_9748` の `ct_mid.png` と `maps/{hecate-9.6,reader-v3,ink_9um-s42}/c+0_s1_{forward,reverse}.png` だけを取得した。seed42はstep 75,000。方向はatlasが格納した層順。三モデルの訓練曝露はこの面のmetaでいずれも `unknown`。 [固定atlasカード](../20261113-next-target01/ink-atlas.md) [面メタ](surface-meta.json)
- [一次] 固定metaの `mesh.base` はsurvey `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の `results/meshes/PHerc0846B_2768_2813_9748`、CTは `20250804142305` のL0。公式Data Browserはscan `20250719185515`、volume `20250804142305`、9.362 µm、113 keVを記載。R186が見た `3962,4983,7051` は別面。 [atlas index](../20261113-next-target01/ink-atlas-index.json) [公式Data Browser](../20261114-unread-lead-reselection01/originals/official-PHerc0846B.html) [R186別面](../20261114-unread-lead-reselection01/PHerc0846B_3962_4983_7051-meta.json)
- [一次・実測] 全七PNGは2184×2184単チャンネルuint8。atlasのcanvasは9.6 µm/px、render scale 0.975、boxは `[0,2184,0,2184]`、65層（法線方向の間隔1.025元ボクセル）。`ct_mid` の非ゼロ範囲は `[49,49,2116,2116)` の4,272,489画素で、公表rendered_pxと同数。Hecateの非ゼロbboxは同じ範囲。Reader V3とseed42は全画面非ゼロなので、非ゼロ値で紙面の有効域を作れない。候補未選定のためXYZを追加取得せず、atlas画素からCTボクセルへの写像は未検証。 [寸法と画素原票](review01/pixels.json)

## 原寸図と再実行

各図の左上はCT中央層。モデル列はHecate、Reader V3、seed42の順で、上がforward、下がreverse。各パネルは元画像と同じ0–255値を546×546で切り出した。全体図のみ7分の1の面積平均。

| y / x | 0 | 546 | 1092 | 1638 |
|---|---|---|---|---|
| 0 | [原寸](review01/native-tiles/x0000-y0000.png) | [原寸](review01/native-tiles/x0546-y0000.png) | [原寸](review01/native-tiles/x1092-y0000.png) | [原寸](review01/native-tiles/x1638-y0000.png) |
| 546 | [原寸](review01/native-tiles/x0000-y0546.png) | [原寸](review01/native-tiles/x0546-y0546.png) | [原寸](review01/native-tiles/x1092-y0546.png) | [原寸](review01/native-tiles/x1638-y0546.png) |
| 1092 | [原寸](review01/native-tiles/x0000-y1092.png) | [原寸](review01/native-tiles/x0546-y1092.png) | [原寸](review01/native-tiles/x1092-y1092.png) | [原寸](review01/native-tiles/x1638-y1092.png) |
| 1638 | [原寸](review01/native-tiles/x0000-y1638.png) | [原寸](review01/native-tiles/x0546-y1638.png) | [原寸](review01/native-tiles/x1092-y1638.png) | [原寸](review01/native-tiles/x1638-y1638.png) |

```powershell
$r192 = 'experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01'
python -B tools/research/run_windows.py "$r192/analysis02-process.json" "$r192/prepare_view.py" "$r192/review02"
```

Windowsの入口で同階層の取得設定と保存入力を解決した。メタ40,854 B、七PNG 8,115,339 B、計8,156,193 Bを取得し、通信工程15.006秒。固定木の長さとLFS SHAを本文取得前に保存し、全件一致。図生成・全112パネルの値検査は8.544秒、CPU1、数値ライブラリ1スレッド、commit上限4 GiB、最大RSS 91,545,600 B。XYZ・新規CTボクセル・レンダー・モデル/GPU実行・追加依存・有料計算0。 [取得前計画](acquisition-plan.json) [取得原票](acquisition.json) [処理原票](analysis-process.json)
