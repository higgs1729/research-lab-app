# PHerc0175B 3024_3577_11121 の公開中心予測

2026-11-14 JST。[一次・目視] 中央CT画像と七モデルの中心窓両順から、元CTへ戻す字画や行のROIを選べなかった。面内の強い反応は広がった塊や裂け・繊維に沿う短い反応で、字画の区切りと間隔が続く箇所は確認できなかった。この一面の中心窓で終了。 [全体図](review01/overview.png) [担当目視原票](visual-review.json)

## 一面の選定

固定atlas indexで各巻最初の一面を事前に代表とした。下の三代表はすべて9.6 µm/px、2016×2016、rendered_px 3,640,464、欠損chunk 0、中央CTと七モデル両順あり。公式First Letters規定の指定volumeは各metaのCT L0参照と一致し、当日保存した公式Winnersページに三巻の受賞記載を確認できなかった。 [候補選定原票](selection.json) [公式規定](candidates/official-prizes.html) [公式Winners](candidates/official-winners.html)

| 代表 | 指定volume | `face_check.mask` | `sheet_fraction` | livenessあり |
|---|---|---|---:|---:|
| PHerc0175B `3024_3577_11121` | `20250521125822` | `ct > 0 (sheet mask under 5 %)` | 1.000 | 7 |
| PHerc0268 `2704_5907_7421` | `20251110183117` | `sheet (crossness >= 0.31)` | 0.069 | 7 |
| PHerc0483A `3155_3610_11128` | `20250521140913` | `sheet (crossness >= 0.31)` | 0.172 | 6 |

原寸取得前の選定では `sheet_fraction` を同じマスクの割合と誤読し、値1.000と全七モデルのlivenessでPHerc0175Bを選んだ。主担当の確認で、0175Bのmetaは `ct > 0` への切り替えを記載していた。値1.000は切り替え後の割合と考えられるが、算出コードは未確認。三面の紙面品質はこの値で比較できない。原寸CTには層の折れ・空隙・裂けが複数見えた。選定当時の判断は原票に残し、今回の観察は取得済みの一面に限定した。 [選定原票](selection.json) [0175B meta](candidates/PHerc0175B-meta.json) [0268 meta](candidates/PHerc0268-meta.json) [0483A meta](candidates/PHerc0483A-meta.json)

## 原寸で見た形

- 右上Hecateには複数の明るい塊がある。幅・境界が不規則で、近傍の斜め繊維と独立した字画の輪郭を選べなかった。 [右上](review01/native-tiles/x1512-y0000-g1.png)
- 中央右寄りのHecate短線・Readerの広い反応は、CTの長い斜め空隙と曲がった層に隣接する。中央下のd9v2の細い暗線もCTの層構造に沿う。 [斜め空隙](review01/native-tiles/x1512-y0504-g1.png) [d9v2](review01/native-tiles/x1008-y1008-g3.png)
- seed42とseed43には表示範囲の縁に沿う強い帯があり、内側の弧や塊は境界がぼける。 [seed42左縁](review01/native-tiles/x0000-y1008-g2.png) [seed43右縁](review01/native-tiles/x1512-y0504-g4.png)

担当は全15画像の全体図、CT・Hecate・Reader V3の原寸全16図と他モデルの原寸9図を目視した。主担当は全体図と六つの位置の原寸図で全七モデルの一部を別目視し、同じく追試ROIを選ばなかった。原寸64図は座標を16分割し、各区画にモデル4組を用意した。各原寸パネルは504×504、座標は左上ゼロ始まりで半開区間。全体図のみ同じ1:8面積平均。 [原寸索引](review01/pixels.json) [主担当の目視・別検算](lead-checked.json)

## 入力と再利用

[一次] 固定atlas `ac5ffd7098120368216948c4e06c494bf8e67178`。CT中央PNGとHecate 9.6、Reader V3、seed42、dense-native、Reader v2、d9v2、seed43の `c+0_s1` 両順の計15枚。すべて単チャンネルuint8。全64図288パネル計73,156,608値（CTの重複パネル込み）が元PNGと一致し、主担当も全値を別照合した。 [長さ・LFS SHA](acquisition-plan.json) [画素原票](review01/pixels.json) [主担当の別検算](lead-checked.json)

面metaは固定survey `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の `results/meshes/PHerc0175B_3024_3577_11121` とL0のCTを参照。公式Data Browserはscan `20250510115222`、volume `20250521125822`、8.64 µm、116 keV。atlasはscale 0.9、9.6 µm/px、全canvas、65層。公表の描画3,640,464画素に対して中央CT PNG非ゼロは3,640,421画素で、bbox `[45,45,1953,1953)` 内の43画素も値0。三代表とも七モデルの訓練曝露はmetaで `unknown`。元meshのXYZや2D→元CT写像、完全な先行判読との重複は未確認。 [面meta](candidates/PHerc0175B-meta.json) [公式Data Browser](candidates/PHerc0175B-official.html)

R195の取得・パネル生成・全値比較を再利用した。比較対象、現行公式二ページの保存、2016²面の504²分割を変更した。保存済み入力から再実行する場合はリポジトリルートで新しい出力名を使う。

```powershell
$r202 = 'experiments/vesuvius/discovery/20261114-next-atlas-surface01'
python -B tools/research/run_windows.py "$r202/analysis02-process.json" "$r202/prepare_view.py" "$r202/review02"
```

公式原文・小メタ424,677 Bと画像16,558,105 B、計16,982,782 B、通信30.348秒。図生成と照合15.675秒、CPU1、数値スレッド1、commit上限4 GiB、最大RSS 101,322,752 B。新CTボクセル、XYZ、重み、推論、GPU、ビルド、課金、外部公開0。 [公式・候補取得](candidate-acquisition.json) [画像取得](image-acquisition.json) [分析実行](analysis-process.json)
