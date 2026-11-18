# PHerc0813 z14304_w100の公開原寸

2026-11-15 JST。[一次・目視] 担当と主担当はseed43 step060000の両層順を別々に原寸で確認し、元CTへ進めるROIをともに0件とした。開いた輪状の反応、鉤、太い屈曲、境界で反復する筋を認めた。屈曲の両端と線幅を明瞭には追えず、反対順で大きく形が変わる例があった。単独の字画を採ることも許容し、数値ゲートや行の有無を選定条件に使わなかった。今回の判断範囲はこの面のseed43両順。物理紙層、中央CTでの対応、別checkpointの反応、巻全体のインクは未検証。 [担当の観察](visual-review.json) · [主担当の別観察](lead-visual-review.json)

## 気になった形の原寸

各図は上から公開forward、reverse、別表示の作者マスク。座標は左上を原点とした半開区間 `[x0,y0,x1,y1)`。マスクの重ね合わせに使った左上位置は記述上の仮定。

| canvas範囲 | 観察 | 作者マスク内 | 原寸 |
|---|---|---:|---|
| `[9148,988,9385,1220)` | forwardの暗い中心を明部が囲むが、左下が開き、下端の明部が横に拡散する。reverseでは明部の位置がずれる。 | 54,984 / 54,984 | [図](review01/observations/01.png) |
| `[3950,1030,4290,1260)` | forwardの鉤。下側が太い斜帯とつながり、別々の終端を拾えない。reverseでは上方の斜帯が目立つ。 | 59,500 / 78,200 | [図](review01/observations/02.png) |
| `[4350,610,4560,810)` | forwardの屈曲は横向きの部分が減衰し、縦側が太く広がる。上に別の長い帯が通る。 | 42,000 / 42,000 | [図](review01/observations/03.png) |
| `[6230,1538,6510,1750)` | forwardの太い鉤とreverseの下部の弧は、まとまり方が異なる。 | 36,680 / 59,360 | [図](review01/observations/04.png) |
| `[8160,508,8670,650)` | 上の直線状境界に沿う準周期的な筋。双方にあり、今回の位置合わせでは全域が採点マスク外。 | 0 / 72,420 | [図](review01/observations/05.png) |

[各図の位置と画素範囲](review01/observations/coordinates.json)

## 入力の来歴

[一次] Carson Rodrigues, *Eligible scroll atlas renders*（2026, Hugging Face, CC BY-NC 4.0）を使用。固定rev `33b4fc81f13a32332b179bf8c34f42ec3cfe7589`。作者はpscamilloのmesh `0c966f8f11f92cffb09dbc6320a706161405ad0b` を `VC3D-4b3c728` の `vc_render_tifxyz` でscale 1・L0・31層・step 1・`--flip-normals` としてレンダーしたと記す。当atlasのforwardは接尾辞なし、reverseは `_reverse`。R188で用いた別配布の方向表示と異なる。推論原票は元surface 31×1860×12340、pad後31×1920×12352、overlap 0.5、Hann blend、batch 16、両層順。歴史的な実行コマンドの完全な再現、元CTとの直接の画素照合は未実施。作者マスクは採点用の侵食済み占有域。atlas manifestの `valid_px` 8,530,433、目視 `aprova`、ink_pass_v1/v2ともfalseは作者の別集計であり、今回の画像判断に使う閾値ではない。 [固定公開カード](https://huggingface.co/datasets/rodriguescarson/eligible-scroll-atlas-renders/blob/33b4fc81f13a32332b179bf8c34f42ec3cfe7589/README.md) · [保存カード](originals/atlas-card.md) · [推論原票](originals/infer.json) · [R220保存manifest](../20261115-next-contiguous-unread-window01/atlas-manifest.csv)

[一次・実測] meshのgridは617×93、XYZはfloat32、scaleは0.05。元の有効XYZ節点のZ範囲は14304.8311–15103.3818、R188 `z12496_w020` は12498.8682–13292.8643。公表節点の座標箱はZで1,011.9668 voxel離隔する。巻紙の物理層の帰属は未確認。固定atlas treeに別配布の中央CT画像はなく、対応する380,538,880 Bのsurface tarは取得していない。 [固定mesh tree](originals/render-mesh-tree.json) · [XYZ照合](mesh-overlap.json) · [atlas面tree](originals/atlas-segment-tree.json)

[一次] 同日の公式規定ではPHerc0813の再構成 `20250821151723` がFirst Letters対象。公式データはscan `20250720160015`、9.362 µm、113 keV、公式セグメント掲載0。公式Winners本文で当該巻は見当たらなかった。未公表の審査・読解は確認範囲外。 [公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [Winners](https://scrollprize.org/winners) · [公式データ](https://scrollprize.org/data_browser/PHerc0813) · [確認原票](lead-current-official-check.json)

## 画像と再閲覧

| 役割 | 型と寸法 | バイト数 | 原図 |
|---|---|---:|---|
| seed43 forward | 12352×1920、uint8、LZW TIFF | 7,559,153 | [TIFF](originals/PHerc0813-z14304_w100-20250821151723-ink9um-s43_060k.tif) |
| seed43 reverse | 12352×1920、uint8、LZW TIFF | 7,510,193 | [TIFF](originals/PHerc0813-z14304_w100-20250821151723-ink9um-s43_060k_reverse.tif) |
| 作者マスク | 12340×1860、uint8二値、deflate TIFF | 36,601 | [TIFF](originals/valid_mask.tif) |

PNGの画像領域は原TIFFの0–255を1:1でコピーし、回転・強調・マスク処理を加えていない。両方向の予測非ゼロ域は同一の13,721,600画素。作者マスクは9,008,610画素で、記述上の左上位置合わせでは非ゼロ予測4,712,990画素がマスク外。うち26,880画素は元surface矩形の外側。全景のみ8×8の面積平均で縮小した。原寸は上forward、下reverse、各中心タイルに上下左右32pxまでの周辺を加えた。両方向が全ゼロの15枚も索引に残した。主担当は両方向の中心領域47,431,680値、周辺込み57,098,240表示値を別途照合し、中心領域が全画素を各1回覆うことを確認した。 [全体・1:8](review01/overview.png) · [全原寸forward](review01/forward.png) · [全原寸reverse](review01/reverse.png) · [マスクのみ](review01/author-mask.png) · [座標索引](review01/pixels.json) · [主担当の表示照合](lead-panel-check.json)

| 中心y / x | 0 | 960 | 1920 | 2880 | 3840 | 4800 | 5760 | 6720 | 7680 | 8640 | 9600 | 10560 | 11520 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | [0](review01/native/x00000-y0000.png) | [960](review01/native/x00960-y0000.png) | [1920](review01/native/x01920-y0000.png) | [2880](review01/native/x02880-y0000.png) | [3840](review01/native/x03840-y0000.png) | [4800](review01/native/x04800-y0000.png) | [5760](review01/native/x05760-y0000.png) | [6720](review01/native/x06720-y0000.png) | [7680](review01/native/x07680-y0000.png) | [8640](review01/native/x08640-y0000.png) | [9600](review01/native/x09600-y0000.png) | [10560](review01/native/x10560-y0000.png) | [11520](review01/native/x11520-y0000.png) |
| 432 | [0](review01/native/x00000-y0432.png) | [960](review01/native/x00960-y0432.png) | [1920](review01/native/x01920-y0432.png) | [2880](review01/native/x02880-y0432.png) | [3840](review01/native/x03840-y0432.png) | [4800](review01/native/x04800-y0432.png) | [5760](review01/native/x05760-y0432.png) | [6720](review01/native/x06720-y0432.png) | [7680](review01/native/x07680-y0432.png) | [8640](review01/native/x08640-y0432.png) | [9600](review01/native/x09600-y0432.png) | [10560](review01/native/x10560-y0432.png) | [11520](review01/native/x11520-y0432.png) |
| 864 | [0](review01/native/x00000-y0864.png) | [960](review01/native/x00960-y0864.png) | [1920](review01/native/x01920-y0864.png) | [2880](review01/native/x02880-y0864.png) | [3840](review01/native/x03840-y0864.png) | [4800](review01/native/x04800-y0864.png) | [5760](review01/native/x05760-y0864.png) | [6720](review01/native/x06720-y0864.png) | [7680](review01/native/x07680-y0864.png) | [8640](review01/native/x08640-y0864.png) | [9600](review01/native/x09600-y0864.png) | [10560](review01/native/x10560-y0864.png) | [11520](review01/native/x11520-y0864.png) |
| 1296 | [0](review01/native/x00000-y1296.png) | [960](review01/native/x00960-y1296.png) | [1920](review01/native/x01920-y1296.png) | [2880](review01/native/x02880-y1296.png) | [3840](review01/native/x03840-y1296.png) | [4800](review01/native/x04800-y1296.png) | [5760](review01/native/x05760-y1296.png) | [6720](review01/native/x06720-y1296.png) | [7680](review01/native/x07680-y1296.png) | [8640](review01/native/x08640-y1296.png) | [9600](review01/native/x09600-y1296.png) | [10560](review01/native/x10560-y1296.png) | [11520](review01/native/x11520-y1296.png) |
| 1728 | [0](review01/native/x00000-y1728.png) | [960](review01/native/x00960-y1728.png) | [1920](review01/native/x01920-y1728.png) | [2880](review01/native/x02880-y1728.png) | [3840](review01/native/x03840-y1728.png) | [4800](review01/native/x04800-y1728.png) | [5760](review01/native/x05760-y1728.png) | [6720](review01/native/x06720-y1728.png) | [7680](review01/native/x07680-y1728.png) | [8640](review01/native/x08640-y1728.png) | [9600](review01/native/x09600-y1728.png) | [10560](review01/native/x10560-y1728.png) | [11520](review01/native/x11520-y1728.png) |

リポジトリルートから別の出力名で原寸表示を再作成できる。

```powershell
$r221 = 'experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01'
python -B tools/research/run_windows.py "$r221/review02-process.json" "$r221/review.py" review02
```

保存したHTTP本体は合計16,080,613 B。LFS SHA-256とGit blob SHA-1を固定のtreeと照合した。主担当も入力16ファイルを別検算した。初回の主担当source照合はマスクもpadded寸法と仮定したため失敗し、再実行で元寸法を保持して左上に配した比較へ訂正した。画像取得・表示はWindowsの既存ランナーでCPU 1、commit上限4 GiB。元三次元CT・surface tar・追加モデル推論・GPU・有料計算・外部送信は各0。ローカル電力費は未計測。 [取得計画](acquisition-plan.json) · [取得原票](acquisition.json) · [主担当の初回原票](lead-source-process.json) · [訂正後の照合](lead-source-check.json) · [資源](resources.json) · [ファイル照合表](manifest.json)
