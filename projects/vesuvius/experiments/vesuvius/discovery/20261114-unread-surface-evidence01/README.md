# 未読面候補を先行surveyの所見と固定原図で確認

2026-11-14 JST。三面の公開カードから元CTへ戻して追試する字画・行の位置を選べなかった。一面の原寸予測追加取得と次のCT実験は見送った。担当と親が三枚を別目視した。インクの有無と候補外の面は未判定。 [事前選定](selection.json) · [担当目視](visual-review.json) · [親の別照合](lead-candidate-review.json)

## 候補と先行の紙面所見

現行First Letters規定の指定CTは0191 `20250821151635`、0257 `20250821151750`、0268 `20251110183117`。現行のWinners一覧にこの三巻のFirst Letters受賞を確認できなかった。公開一覧の確認範囲で、未公表の判読状況は不明。R195/R202で挙がった三つのatlas面は同じ巻の別seed。対応する先行survey行は `traced_ok=False, inked=False`、quick-lookの適格tile率0.033/0/0だった。作者のゲートはmedian crossness ≥0.31の512 px tileが40%以上。三行は測定値と通過しなかった記録があり、物理的な紙面帰属は未確定。R203で扱ったatlasの `sheet_fraction` とfallbackを順位には使っていない。 [公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [公式受賞一覧](https://scrollprize.org/winners) · [現行照合と保存一次HTML](lead-official-check.json) · [作者のゲート説明](../20261114-atlas-known-control01/survey-readme.md) · [固定survey原票](../20261114-unread-lead-reselection01/survey.csv)

| 固定候補 | 先行観測 | カードを原画で見た所見 |
| --- | --- | --- |
| PHerc0191 `p191_a`、XYZ 2301,3300,9499 | 5面中唯一のsheet gate通過・採点面。選ばれたforwardは強いtile 4対1/8、作者の側推定は外側。 | 左上の癒着した反応は暗い欠損に接し、右側には孤立点が散る。 [カード](originals/p191_a.jpg) |
| PHerc0257 `3549_4692_13210` | 作者のlead。forwardの強いtile 6対0/14、chain 1.962、暗部への重なり0.139。追試6面の推定側は内3・外3。比較する具体的な先行所見が最も多いが、作者は可読を報告していない。 | 上縁の連結塊、中央斜めの暗い境界の近くの粗い斑点、右下の短い反応から、独立した字画の輪郭と一定した間隔の行を指定できなかった。 [カード](originals/PHerc0257_3549_4692_13210.jpg) |
| PHerc0268 `9054_2867_6674` | 9面中唯一のsheet gate通過・採点面。reverseの強いtile 2対1/12。別のatlas面の低いcrossnessをこの面には適用しない。 | 上方の太い縦反応、広い斜めの割れに沿う点と短片。独立した字画列を追えなかった。 [カード](originals/PHerc0268_9054_2867_6674.jpg) |

## 追試を決められる範囲

固定surveyの各mesh metaは公式CTと同じ再構成IDの派生surface m7 L0を記録し、XYZ seed・bbox・tifxyz scale約0.05を持つ。固定木には各XYZ TIFFが各56,329 Bで公開される。mesh来歴は辿れるが、JPEG→未加工描画の座標対応、局所の同一物理紙面、訓練と全座標の非重複は未検証。固定surveyの公開木ではカード・採点・meshが確認でき、生成コードが読む連続予測はローカルwork出力。固定atlas `ac5ffd7098120368216948c4e06c494bf8e67178` の公開indexにこの三つと一致する固定面はなかった。別seedの予測の座標対応や物理的な重なりは未確認。 [固定meshメタと木の照合](source-check.json) · [固定atlas index](../20261113-next-target01/ink-atlas-index.json) · [作者の実行入口](../20261114-unread-lead-reselection01/survey-entry.py)

今回の目視は1773×786 RGBのJPEG三枚の両パネル全体。左はcrossnessに由来する彩色CT。右は作者が選んだ深さ順について、seed42/dense-nativeの正規化平均を緑の範囲に限定して重ねた加工表示。複数の連続予測を元の画素格子で比較した結果は無い。自動照合は九本文の実長・固定Git blob SHAと三JPEGの寸法、meta/CSV/カードの一致まで。 [表示コード](../20261114-pherc0846a-lead-audit01/report_card.py) · [取得前の一覧](acquisition-plan.json) · [照合原票](source-check.json)

## 取得量

カード三枚945,324 B、小メタ六本文4,698 B、保存本文計950,022 B、取得工程2.434秒。親の公式直接照会1応答は403で本文の保存0 B。現行web参照の正確な通信秒と転送量は未計測で、受賞・対象の原文はR202保存HTMLを参照。CPU1・commit4 GiBの取得工程は最大RSS36,855,808 B。新規原寸予測、元CTボクセル、XYZ TIFF、重み、モデル推論、GPU、課金、外部公開0。 [取得原票](acquisition.json) · [実行原票](acquisition-process.json)
