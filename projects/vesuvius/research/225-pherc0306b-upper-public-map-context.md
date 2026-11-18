Status: resolved
担当: 研究（r225_upper_public_map / gpt-6.1-sol / high / 2026-11-15）
Blocked by: 224

# PHerc0306Bの既知行と上方の公開応答を同条件で比較すると、原CTで追う価値のある形が残るか（2026-11-15）

## 依頼

本人の目標は新しい文字の発見。公開済み改善三件は一つの11月応募へまとめる。224は0306Bの既知行に隣接する上方応答を選び、TRACEと別系列のReader V3公開生予測を同じ面・幅で比較する案を固定した。本件はその一件を実施し、既知対照で感度を確かめた上で、原CTや独立面を追加調査するに値する具体的な候補が残るか判断する。新しい文字、未読、受賞可能性は未認定。上方応答は既に作者公開画像にあり、再表示したことだけでは前進と数えない。

凍結済み計画は experiments/vesuvius/discovery/20261115-discovery-next-intervention01/next-plan.json、SHA256 6e9f4eccf7de9c5e3b14e071f938bd6fc6a4bddae8de0946ffaeb0f775b90c4d。224票、lead-upper-visual-review.json、lead-grid-review.json、lead-plan-check.json、provenance-and-novelty.jsonも必要箇所を参照する。次案の対象・二帯・モデル・表示範囲・判断条件を変えずに実施する。実装方法は既存道具から選ぶ。TRACE/Reader V3の二NPYと派生CT表面PNGだけ新規取得171424048 B、全SHA確認、モデル推論・GPU・新生CTボクセル・有料計算・外部公開/投稿/応募は0。作者meshのpixel/20規約を用い、R222 rendererの半画素規約を混ぜない。

取得期限300秒、計算CPU1/commit4GiB/300秒、C作業1GiB・空き10GiBを計画値として保つ。Dは読取のみ。既存入力を再利用し、登録済み原票は変えない。依存追加や大きな追加取得が必要なら実行前に主担当へ理由を伝える。

原native整数cropを一度flipUDし、raw0..1表示と二帯和集合のモデルごとmedian→p99.9を共通適用した補助表示を残す。NaN、有限ゼロ、CT>0、数値幾何支持を区別する。4416幅の全景は位置確認用、128px重複を持つ幅1152以下の原寸tileを全幅に漏れなく作り、原寸で比較する。二帯の全幅末尾を取りこぼさない。既知と試験の具体的な形・対応・相違を示す。画素一致やCT暗部との重なりだけを採否基準にしない。Reader既知対照が不成立なら上方を陰性と断定せず、固定比較での追加投資根拠なしとする。既存TRACEの形だけを理由に保持しない。

画像ができたら主担当へ一覧とnative表示規約を送る。主担当は重要な既知対照と上方群を、担当判定文を読む前に別目視する。結果はこの票に追記して完成し、experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/ に入力参照、コード、取得/計算ログ、固定表示と所見、実費0の根拠、manifestとlab登録候補を置く。次候補の開始とlab登録は主担当。再委任なし、一件ずつ。

モデルはgpt-6.1-sol、effortはhigh。224で対象・座標・表示・判定が固定済みで、既存の公開予測の取得/描画手順を解釈して実施する依頼のため。新しい探索方針やインフラを作る依頼ではない。224完了・登録とinbox未決0を確認して着手。

## 結論

**公開済みの上方応答群から、原CTまたは独立面で紙層を確かめる候補を1件保持した。** 既知行の粗い縦画・交差・下側の横画と右側の輪はReader V3でも同位置に残った。上方ではReaderが、TRACEで分かれて見える左側の曲がりと下側の応答をより連続した弧と下辺でつなぐ。右隣の応答にも大まかな配置の対応がある。raw0..1と固定補助階調の両方で確認した。局所追試用の目安はraw半開XYXY `[3424,3424,4160,3824]`。確定新文字は0、物理紙層と既読範囲は未確定。 [比較画像・根拠一覧](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/README.md)

## 根拠・詳細

| 比較 | 所見 |
|---|---|
| 既知帯 t01 | [一次・原寸目視] 縦の細長い応答、その右の交差と下方の太い横応答の相対位置をReaderでも確認した。Readerでは分かれて見える箇所が太くつながり、細い終端を再現したとは言えない。 |
| 既知帯 t02 | [一次・原寸目視] 作者line 1位置8の箱に対応する右寄りの輪と暗い内側は同位置。ReaderはTRACEより輪郭を太く描き、左側の横応答へ強くつながる。粗い構造と配置の肯定対照として成立。 |
| 上方 t00/t01 | [一次・原寸目視] t01局所x0–335、表示y330–575付近で、TRACEは左の曲がった縦部分と短い下側の応答。Readerは左上から下辺までより連続し、暗い内側に回り込む。右端は弱く分かれる。隣のx400–680、y220–570近辺では下部二箇所と右の立ち上がりの粗い位置が対応し、強さとつながり方には差がある。 |
| 上方の残り | [一次・原寸目視] t01下側の三つの孤立ピーク、t02–t03をまたぐ下寄りの太い応答、末尾t04の縦長の塊には追える連続形を選ばず、追加ROIは0。 |

[推論] Readerの接続が字画か、モデルによる結合や共通CTに由来するかはこの比較から判定できない。派生CTには交差する繊維と暗い隙間がある。採否は既知対照と粗い形の配置に基づけ、CT暗部との重なりや画素単位の一致を条件にしなかった。原CT追試では候補と同面既知点の紙層支持を照合し、紙層帰属と字画の証拠を別に評価する。公開済みの形であり、R224の公開tracingに重ならないことから他提出の既読範囲は確定しない。 [担当所見](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/visual-review.json) · [R224来歴](../experiments/vesuvius/discovery/20261115-discovery-next-intervention01/provenance-and-novelty.json)

主担当は担当所見を読む前に12原寸図の別目視を固定し、同じ一群を保持した。主担当の応答中心の見積もり `[3424,3460,4116,3752]` は担当が選んだ少し広い位置目安に収まる。担当も共有前に画像を見て判断したが、担当所見JSONを書き出す前に主担当の要約を受信した。主担当はさらに取得原票3件の全SHA・shape・dtypeと階調限界を別計算し、原寸の予測・CT 50図の計56,770,560画素を照合した。 [主担当別目視](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/lead-visual-review.json) · [入力照合](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/lead-input-check.json) · [表示照合](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/lead-panel-check.json)

## 取得の経路

2026-11-15に固定HFからNPY各76,244,128 Bと派生CT PNG 18,935,792 Bを全取得。3本文計171,424,048 B、12.751秒、全SHA一致。4900×7780、NPYはC順float16。作者の20 raw px/grid規約で有限正XYZの4頂点支持は各帯5,087,232/5,087,232。CT>0は既知5,087,214、上方5,087,207。両モデルとも二帯にNaN・有限ゼロ0、補助階調の標本数は各10,174,421。共通median→p99.9はTRACE 0.2098388671875→0.775390625、Reader 0.275146484375→0.81103515625。画像は整数crop後に一度flipUDし、幅4416全体を高さ1152の原寸5タイルでカバー。最後の320px幅まで保存し、隣接は128px重複。全景は1/4の位置図。 [取得ログ](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/acquisition.json) · [全表示](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/display-manifest.json)

生成処理2.870秒、CPU affinity 1コア／process commit上限4 GiB、ピークworking set 274,370,560 B。C作業1 GiB・空き10 GiBの範囲、D書込0。推論、GPU、原CTボクセル、有料計算、外部投稿は0。 [計算ログ](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/render-process.json) · [資源記録](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/resources.json) · [manifest](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-public-map01/record.json)

## メモ

- 2026-11-15：共通指示、researchスキル、224票・固定計画SHA、224登録 record-dfd4b7b2783a、監査inbox未決0を確認して着手。
- 同日：固定3資産を取得、同面二帯を作成して判定前に主担当へ表示一覧を送付。双方の目視と主担当の原票・表示照合を保存。登録・次の着手は主担当。
