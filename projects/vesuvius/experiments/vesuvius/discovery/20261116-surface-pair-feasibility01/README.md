# PHerc. 0211 の手直し前後の面を使った対照

2026-11-16 JST。公開資料の範囲では、受賞者の手直し後の面と同じ既知文字領域を覆う、手直し前の固定面を特定できなかった。受賞者図の緑枠と公開 v9 は画像上で対応し、既存の小さな φ が対照位置として残る。手直し前に必要な面の ID と来歴の手掛かりは得られたので、その座標ファイルと同じ巻き・紙面上の対応が提示されたときに再開できる。

## 受賞者図と後面

- [一次] 公式発表では、Priyank Aranke が全高の VC spiral fit、隣接 winding の接合、VC3D Manual での手作業、DinoVol を使った行方向の延長を経て描画した。受賞者の色付き図 fig01（1863×407）の緑枠に11字を報告する。続く黄色図 fig02（2048×523）は Vincent Lemonnier の honorable mention。R244 が確認した既出応答の掲載先は fig02 で、受賞者のモデルや面版の帰属までは扱わない。原図4枚の出典と SHA は保存済み。 [公式発表](https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211) · [原図取得記録](../20261115-pherc0211-adjacent-context01/lead-article-images/acquisition.json) · [R244](../../../../research/244-pherc0211-public-figure-verification.md)
- [一次] v6 親 `PHerc0211-crop1711-manual-20261026-1237-legacyuv20-v6` と v9 `PHerc0211-crop1711-lines123-manual-20261028-1316-legacyuv20-v9` は同じ原 CT `20250821151803`、9.362 µm/voxel、同じ `baseline_source_id` の **`PHerc0211-spiral-stitch-rev01-crop-20261022-1711`** を記録する。それぞれ別の手直し済みスナップショットで `registration_ancestors` は空。Orientation は frozen stitched crop 1711 の `original` から global `normal_sign=-1` を引き継ぎ、遡った参照名は m35000 combined-flatten window の w028/w029。定めた近傍点での法線一致と物理的な面の表裏の確認は別で、両方とも `physical_face_verified=false`。ZIP にある格子/OBJ/NPZ と SHA は配布の手直し後のもの。v9 の `source-tifxyz` も manual snapshot SHA に一致する。 [v6 親 case](../20261116-pherc0211-added-context-coverage01/sources/v6/mesh__parent__case.json) · [v9 case](../20261116-pherc0211-added-context-coverage01/sources/v9/mesh__case.json) · [v9 orientation](../20261116-pherc0211-added-context-coverage01/sources/v9/mesh__orientation.json) · [v9 ZIP](https://drive.google.com/file/d/1aQhMxc3A5wYOBtHGy9fiJaGUyNwDzLmu/view) · [v6 ZIP](https://drive.google.com/file/d/1CGqmGKvKznjKCXw1xmo_OPclnLn681D3/view)
- [一次計算・推論] fig01 の転写と緑線を含まない3ブロックを、保存 ZIP の無着色 `mesh/raw-ct.png` とスケール .285–.325 で高域グレースケール相関した。v9 は左/中/右で相関 **.789 / .727 / .687**、同じ縮尺で離れた次点は ≤.079。3点とも同じ縮尺 .306 と変換 `uv_v9 ≈ xy_fig01 / .306 + (-68.63,699.35)` に落ちる。v6-line2 は .107 / .425 / .058 で変換も一致しない。対応図でも中央と右の縦割れの配置が揃う。fig01 の緑線の着色ピクセル外接箱 `[284,8,1543,152]` は v9 上でおよそ XYXY `[859,725,4974,1197)`。**既存 v9 φ の XYWH `[4640,780,320,300]` はこの箱の内側**。縮小・着色済み図から得た近似であり、図の原寸 crop 履歴・確率の画素同一性・前面の紙層対応は未証明。 [対応図](winner-panel-v9-ct.png) · [相関と原バイト SHA](figure-registration.json) · [座標とマスク](coordinate-evidence.json) · [既存 v9 φ 計画](../20261115-pherc0211-adjacent-context01/candidate-plan.json)

## 前面の探索範囲

| 一次資料 | 調べた範囲と結果 |
| --- | --- |
| [著者 Drive](https://drive.google.com/drive/folders/1bvKolL_TIE3k5Ixi1qlOiAmofQ6r2ocH) | R241 保存目録の直下22＋下位8フォルダ44件。現行の座標は2本の manual ZIP と対応 tifxyz フォルダ。v6 ZIP 内の親全体は手直し後で line2 描画の親。前面 ID の XYZ は見当たらない。 [目録](../20261116-pherc0211-parent-probability-source01/sources/drive-inventory.json) · [原 README](../20261116-pherc0211-parent-probability-source01/sources/drive-README-raw.md) |
| Drive の旧 P737 成長面および manual v3 | `P737m01st3-grown` は穴埋め・縁切り・接合を著者が記し、`manual_ct_extension=true`。v9 の φ の有効 cell 四隅の Y 上限3410.28と、grown のメタ bbox の Y 下限4309.42は899.14 voxel離れる。概算緑枠の Y 上限4260.81とも48.61 voxel離れる。P737 manual v3 は緑枠の外接箱と交差するが φ の箱とは Y で650.48 voxel離れる。旧版ごとのモデルも Studio epoch9 / Thin15 と異なる。 [grown の原文](originals/archive-grown-README.md) · [manual v3 の原文](originals/archive-p737-manual-README.md) · [比較](coordinate-evidence.json) |
| Drive の旧 3305 / [著者 Expanded9 データ](https://huggingface.co/datasets/paranke/vesuvius-expanded9-training-data/tree/fabf840229a4e0f0dac314de70aff360843961d3/submission/PHerc0211-3305-r002-c01/geometry) | v9 φ と外接箱は交差する。Drive の方法書は手作業による点追加を明記し、HF にある `source-tifxyz` 自体も `manual_ct_extension=true`。HF の input record が参照する親面パスは著者環境内。これらから crop1711 の前面と同一とは確認できない。 [方法書](originals/archive-3305-README.txt) · [メタ](originals/expanded9-3305-source-meta.json) · [input record](originals/expanded9-3305-input.json) |
| [著者コード](https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt)・[VC3D Manual](https://github.com/priyankaranke/vc3d-manual) | R241 保存の3 tree、crop1711 の比較 JPEG と実行スクリプトを再点検。DinoVol Original / Rev1 の比較と著者環境内パスが残る。Original という表示から元 spiral fit の XYZ 配布を導けない。公開訓練2データ目録の PHerc0211 形状は Expanded9 の旧 3305。旧報告が指した grow/render/inference repo の匿名 API は各404で公開資料として確認できない。 [固定脚本](../20261116-pherc0211-parent-probability-source01/sources/github-publish_crop1711.sh) · [GitHub 目録](../20261116-pherc0211-parent-probability-source01/sources/github-inventory.json) · [取得原票](followup-acquisitions.jsonl) |
| [公式 Data Browser](https://scrollprize.org/data_browser/PHerc0211)・S3・[spiral dataset](https://dl.ash2txt.org/datasets/spiral_datasets/PHerc0211/20250821151803/) | Browser は segment 0。S3 の当該巻の階層は photos / volumes / representations（predictions・umbilicus）。predictions の surfaces / lasagna は体積予測。spiral dataset にある tracks は fit の入力。固定巻き面の座標配布はこれらの目録で確認できない。 [S3 原目録](originals/s3-root.xml) · [spiral 目録](originals/spiral-dataset-index.html) |
| [公式 Winners](https://scrollprize.org/winners) 経由の [Bryant Le の先行報告](https://github.com/bnleft/first-light-pherc0211/tree/728a27234f50d239c6c83934dad6952b48b94b76) | 独立した fit の公開記録は z10000–11000、w010–065。v9 全体の Z 上限9312.36、v6 親全体の9718.02より上。現行固定 tree 96件・releases 0 に描画画像・設定・ログはあるが 3D 面ファイルを確認できない。 [固定 README](originals/first-light-README.md) · [tree](originals/first-light-tree.json) |
| [gmDevi の独立 fit](https://github.com/gmDevi/vc-windows-tools/tree/420608850f5f126524e7a06ef3a8c85ba31d7f6c)・[eligible-scroll-spiral-fits](https://huggingface.co/datasets/rodriguescarson/eligible-scroll-spiral-fits/tree/63c641ba1dc794073208c24f7f88fa59c4f77621) | gmDevi の3バッチは先行探索で位置が一致する面の入手先を確定できない。第2帯 z13500–15000 は Z 非重複。固定 tree 3,265件・releases 0 で当該巻は画像/集計。HF の固定目録4,337件ではメッシュは PHerc0191 と PHerc0826。 [報告](originals/gmdevi-REPORT.md) · [索引](originals/gmdevi-run-index.md) · [HF 目録](originals/eligible-fits-inventory.json) |

[推論] 上記の範囲で前面の公開配布を確認できなかった。巻きモデル・tracks・体積予測・手直し済み面・画像だけでは今回の対を成立させられない。BBox の分離は記録された座標範囲で支持を除くために用い、交差は紙面の一致と見なさない。

## 既往実験と面版

| 研究 | 実際に使った面と今回の関係 |
| --- | --- |
| R229–232 | PHerc0211 受賞モデルを導入。既知の固定入力による検証先は PHerc0343。R230/231 はその回収・起動・正規化の過程。 |
| R233 | PHerc0800 の固定 auto_grown 面。PHerc0211 との面だけの比較には巻・場所が異なる。 |
| R234–235 | v9 の二行目右端と小 φ。公開 v9 像、格子点と元 CT の局所診断。R235 は新しい描画入力の対照を実行していない。 |
| R236–238 | v6 手直し後の親格子で単行を作る公式描画と局所描画の比較。最大1 DNと R236 の確率 gate 不合格は同じ後面の描画経路差。 |
| R239 | 公開 v6-line2 φ（strip `[4704,140,320,300]`、親 `[4704,3120,320,300]`）の既知像は公開入力由来。未知候補は同 v6 親の近似描画。 |
| R240–242 | v6 親の固定候補と φ の局所 CT 診断、旧 epoch9 全親確率の来歴、同じ近似 renderer/soft-loss による候補周囲。旧全親確率と現在配布の soft-loss 単行画像は別。 |
| R243 | v6 親追加域から v9 への一括同紙対応は未確定。追加保存画像の局所の近さを、前面対や共通 UV の証明に使わない。 |
| R244 | v6 親由来の反応との比較先は公式 fig02。既出反応と判断済みで、モデル・面版や紙層の帰属は未確定。 |

## 条件付き比較

[推論] 再開の条件は、手直し直前の crop1711 の元 XYZ（理想は接合後・初回手直し前。生の winding しかなければ、その共通部分だけを使い比較の意味を限定する）、固定版/SHA、元巻き番号、v9 と同じ CT 基準での紙面対応。そのときだけ既存 v9 φ `[4640,780,320,300]` の一領域を試す。下記は設計で、実行判断は別途。

1. 比較の推論出力を開く前に、紙面側を対応づける。元巻き・接合の来歴、既知 φ の横につながる反応と縦軸を覆う領域の複数の CT 断面・局所アンカー、近い別巻き候補と法線方向を確認する。既存の対応が定まらない、同じ巻きで広がりを確保できない、正負の面向きを一つに選べない、数字の近さだけで別の紙を排除できない場合は停止。前後でグリッドが違えば CT を参照して対応を確認し、既存の UV を共通の native ピッチ 9.362 µm の座標へ一意に対応づける。局所編集、深さ最適化、インクを見て位置を調整する処理は比較条件に入れない。
2. 唯一の介入は共通チャートに対する面の XYZ と、同じ演算で得る局所法線。共通のCT L0、renderer の版・実行環境・格子処理・補間・丸め・端処理と共通有効画素を固定する。31層を1 voxel 刻みで描画し、実体に対する層順を統一してゼロ面に対し `+8,+7,…,-7` の16枚を取る。実体の側と結び付けてから、必要ならメッシュのパラメータ向きの違いを一つの global sign で補う。両条件を同じ soft-loss EMA（SHA `96b326286e38de99047f7cab36170c53749a18d5f43e5fde0c7c20f2980b0e90`）、FP32、TF32 off、同じ正規化 `clip(DN,0,200)/255`、同じ128入力/central96/stride64 Hann、同じ表示で実行する。正規化演算・crop origin・padding・mask を共有し、対象字画を欠損や padding が切る場合は停止。
3. 追加量の上限案は片面6×6パッチ、両面72 forward。共通 ROI を原点に出力タイル始点を各軸 `-32,32,96,160,224,288` に固定すれば、16 px の入力余白込みで448×448の1 canvas/面。両面の31層 uint8 は12,443,648 B、16層入力は6,422,528 B、72件の central96 raw float32 は2,654,208 B。旧保存CTキーを再利用し、両面を含むサンプル hull のキー集合を出してから通信量を見積もる。追加 CT が必要なら当案の上限は8キー（2 MiB/キー、16 MiB）とする。超過ならこの案を停止し、別の投入判断へ戻す。上限は比較の前提を変える根拠に使わない。
4. 固定の参照は fig01 緑枠の右側、v9 公開 float32 確率と同じ座標の v9 CT。二者が同じ原寸濃淡と対応 CT を見て、左側の曲がりから中央・右へ伸びる反応と中央から下がる軸の保持、途切れ、共通範囲外を個別に記録する。まず共通 renderer の後面で主形状が再現することを陽性対照にする。再現しなければ面効果は未判定で終了。再現した場合だけ前面の原寸を比較し、前後とも同じ重なりで形の保持を判定する。旧公開確率との画素一致は要求せず、層順・モデル・表示条件は判定前に固定する。得られる結論は、この既知 φ の形がこの2面でどれだけ保たれたかまで。混在する接合・手直し・成長の内訳や他巻の律速はこの比較から決まらない。 [v9 公開確率の原寸表示](v9-phi-public-raw8-native.png) · [v9 公開 CT の原寸表示](v9-phi-public-ct-native.png)

主担当は原 ZIP の XYZ 全78,561値と図変換を別計算し、φ の支持 bbox の包含、P737 両版との Y 方向非交差、図の割れ線の対応を確認した。座標表の cell 集合は格子境界側を広めに含む保守的な包絡。 [独立照合](lead-check.json)

取得原票に保存した公開目録・テキスト・JSON の本文は **2,027,363 B**、最大単体833,292 B。外部目録の入口確認にも同じ小資料を読み、原票の量は総 HTTP 転送量を表さない。元CT voxel、モデル、ZIP 本体の再取得、forward、GPU、ビルド、有料計算、外部連絡は0。新規保存は C、D への操作は0。数値処理は既存 Windows runner の CPU1/commit4GiB。R234/R241/R243 の保存原文、v6/v9 ZIP、fig01 を再利用した。 [原票1](acquisitions.jsonl) · [原票2](followup-acquisitions.jsonl) · [相関の実行](figure-process.json) · [座標の実行](coverage-process.json)
