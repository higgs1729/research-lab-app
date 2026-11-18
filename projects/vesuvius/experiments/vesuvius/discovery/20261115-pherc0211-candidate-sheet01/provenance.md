# R240 fixed-ROI provenance check

2026-11-15、保存原文と固定revisionの原ファイルを確認した。候補はparent XYWH`[4416,2048,384,256]`のまま。CT断面や新モデル出力はまだ作っていない。

| 一次資料 | 直接確認できたこと | そこからは決められないこと |
| --- | --- | --- |
| v6 ZIP `mesh/parent/case.json`/`mesh/split.json` | 対象はmanual revision6、親canvas4600×6060。公開line2は親行2980:3580のcropとmaskで、候補の親行2048:2304とは非重複。split記録は親の確率mapのcrop/restrictionと記述する | 親crop外が未推論・未読・未提出だったとは言えない |
| v6 ZIP `mesh/parent/results.json` | 親面全体4600×6060を旧Studio checkpoint`ffffbf4f...dbd91145`で推論した履歴、6,663 tiles、stride64、normal_sign -1、確率SHA`0bf20b28...0f3e1`がある | 記録にある全親確率本文は今回未入手。R239のsoft-loss checkpoint`96b32628...e90`との同じ全親結果ではなく、候補個別の旧確率値や公開有無は未確認 |
| v6 ZIP `mesh/inference-record.json`/`mesh/reproduction.json` | 現在配布するline2の確率はGH200/bfloat16、soft-loss checkpoint96b326...、公開strip入力の再実行に由来する | これを親全体への同モデル推論の公開証明にはしない。historical parent resultsと現在のstrip reproductionを混同しない |
| v9 ZIP `mesh/case.json`/`mesh/normalized-tifxyz/meta.json` | 同じbaseline crop1711からの別手動revision9である。公開v9のZ範囲min7524.437、候補を覆うv6格子corner hullのZmax7461.280 | 異なるUVや最近傍XYZを同一紙へ接続できない。範囲外は同じ公開v9 mesh上ではない根拠に限定し、全既出作業との非重複・新規性を主張しない |
| 著者CPT READMEと`reference/crop1711-stock-vs-cpt.jpg` | 旧stitched crop1711をstock/CPTで比較した画像が既に公開されている。固定commit`2ac947c38589be6cfcc1b3b462e2431371a77043`から544,889 Bを取得しGit blob SHAと全SHAを確認 | JPEGは今回のmanual v6と同じ登録済みUV/XYZではない。候補の特定反応を画像内に一意対応できず、不一致を未公開の証明にしない |
| 公式受賞記事と元4図 | 受賞範囲外にも他者の公開反応があり、複数提出が重なる。記事はsegmentation skipや異なる紙からの文字列混在も述べる | 緑枠は既出作業全体の境界ではない。画像だけで候補へ登録できず、候補が既出文字と同じかは未解決 |

原文`orientation.json`はnormal_signを幾何から継承し、`physical_face_verified:false`を保持している。原CT断面で局所の帯状構造を追えたとしても、recto/versoやインクを直接確定するものではない。今回の観測は保存面が局所の連続した紙状構造の近くにあるか、層接触や裂け目で選択が曖昧になるかを確認する。

来歴の現判断は、**既往推論あり、記事の既出文字との一意対応は未解決、新規性は未確認**。候補を初の新文字と扱わない。著者の非公開作業は未確認のまま残す。画像の探索的な登録・別ROI選択・新surface作成はしない。

原文経路：

- R234 `sources/v6-line2-mesh.zip` / `sources/v9-mesh.zip` / `sources/drive-README.md` / `sources/cpt-README-fixed.md`を直接読取。今回の小原文抜粋は`./sources/mesh__*.json`（JSON丸ごと、値の編集なし）。
- [固定著者比較図](https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt/blob/2ac947c38589be6cfcc1b3b462e2431371a77043/studio-multiscroll-cpt-20261023/reference/crop1711-stock-vs-cpt.jpg)。GitHub連携で固定revisionのmetadataを確認し、binary非対応のため返されたraw URLから全544,889 Bを取得。`provenance-image-acquisition.json`にHTTP/size/SHA/Git blob整合を保存。
- [公式記事](https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211)の保存原HTMLはR229 `sources/award.html`、SHA45346fbb...f3ce。R234 `lead-article-images/`の元4図を実見。原文のUTF-8 visible textを`./sources/award-visible-text.txt`へ抽出し、元HTMLへのSHA参照は`source-provenance-inspection.json`に保存。
- 担当の画像所見は`researcher-provenance-visual-review.json`へ先に保存。旧R234の親記事所見を既に読んでいた事実を記載し、新しい独立blind reviewとは呼ばない。
