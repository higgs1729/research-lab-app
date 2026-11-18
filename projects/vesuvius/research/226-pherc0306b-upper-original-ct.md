Status: resolved
担当: 研究（r226_upper_original_ct）
Blocked by: 225

# PHerc0306B上方候補の曲線と隣接応答は、元CT上でどの紙面を辿っているか（2026-11-15）

## 依頼

本人は未読文字の発見を主目標に指定。225（record-6d649692af16）で、既知行と同じ条件の公開Reader/TRACE比較から、上方公開群一件を元CT追試へ保持した。親は担当所見を読む前に12原寸図で同じ群を選んだ。Readerは既知対照の粗い縦画・交差・輪を保ち、上方では左の曲がりと下辺が暗部を囲む形に接続し、隣の縦向き群も残る。ただしモデルによる誤った結合、共通CTの模様、紙層の切替は未排除。公開既出の形で、新文字も既読範囲も未認定である。

本件は、この固定候補を元CTへ正しく対応付け、字画状の部分と間の暗部がどの層・面に位置するか、同面の既知文字対照と比較して調べる。原CTからの局所断面や連続した法線方向の断面など、既存の道具を使い、候補の形を支える紙層を追えるかと、面が層間を切り替える具体的な証拠があるかを分けて残す。幾何の正確さだけでインクや文字を認定しない。曖昧だからインク無し、CT暗部に重なるから偽陽性、とは扱わない。R224の作者報告では暗部重なりの判別が弱く、180/214/216では既知箇所にも紙層帰属の曖昧さが残った。

候補は著者carrier半開XYXY [3424,3424,4160,3824]。R225/lead-visual-review.json と visual-review.json に形の位置、R224/coordinate-support.json と lead-grid-review.json に元CT XYZへの規約がある。volume20250521133212、mesh PHerc0306B_20250521133212_w074own_touchup_V5Rc。元frameは著者のraw pixel/20。現在rendererの半画素規約を流用しない。公開ct_surface_layer20.pngの値と正確に同じ再現条件を確定できた場合だけ比較し、層番号からoffset0などを推測しない。作者の表示・補間と別の生CT補間を混同しない。肯定対照は同面既知行の輪と近傍（225のknown t02、作者line1 pos8）。既知位置は元のletter_dimensionsと座標変換から固定する。

最初に対象・対照の少数の点と、候補内の連続性を判定できる固定断面を具体化する。225の図を基にした選定なので探索的であり盲検ではない。原CTのsource URL/level/metadata・dtype・圧縮・chunk、既存キャッシュ、必要key集合と追加実byte見積もりを確認し、plan.jsonへ固定して主担当に知らせる。元CT取得の目安上限256MiB（原CT見積もり確定後に報告）、C新規出力1GiB・空き10GiB、CPU1/commit4GiB、取得/計算各300秒を初期枠とする。数値上必要なら枠を勝手に広げず、何にどれだけ要るかを主担当へ。これは本人再承認ではなく、一件の資源設計の調整。0ドルのローカルCPUと公開データ取得だけ。新モデル推論・GPU・クラウド・自動全面補正・閾値や深さの総当たり・他面への探索・外部発信を含めない。

180/184/214/216の元CT断面・補間・限定取得、224の座標対応など既存実装を再利用し、独自の大きな基盤は作らない。既存表面/独立面の情報が小さく公開取得でき、同じ部位の層帰属を直接助けるなら参照できるが、名前や数値連続だけを独立紙面の証拠としない。物理紙面が確定しない場合も、今回の画像から分かった具体的な支持/矛盾/限界を記録し、225の候補を消す理由と未確定のまま残す理由を区別する。担当による一件の結果が出たら親が重要箇所を別目視・数値確認する。

出力はこの票へ追記。実験保存先 experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/ に計画・入力参照/ハッシュ・取得/計算ログ・座標と断面図・判断と資源・manifest・lab登録候補を置く。画像完成時には先に道筋とファイルを親へ送り、親所見を固めるまで担当の結論は別に保つ。既登録資料を変更しない。Dは読取のみ。次研究着手とlab登録は主担当、再委任なし。

gpt-6.1-sol / high を選択する。固定済み候補に既存の元CT取得・補間・断面手順を適用する依頼だが、別巻の座標・層・肯定対照を解釈して確かめる必要があるため。225完了・登録とinbox未決0を確認して逐次着手。

## 結論

[一次・2026-11-15] 左の曲がりと下辺は、元CTでmesh近傍の紙層状の明帯に沿う区間を持つ。上方の暗い内側と右隣への区間では帯が分岐・接近し、上方形状の全体を同じ物理紙層に割り当てられなかった。特定の位置で異なる紙層へ切り替わったという証拠も得られなかった。対照の既知輪でも輪縁は明帯の近く、輪内は暗部で、全経路の紙層帰属には曖昧さが残った。 [担当所見](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/visual-review.json) · [主担当の別目視](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/lead-visual-review.json)

[推論] 右隣まで同じ紙層を追う仮説は保留する。左側には局所的な紙層近傍の支持が残り、既知輪の比較から暗部や帯境界だけで除外する根拠は得られなかった。R225の公開既出候補一件は未確定の位置として保持する。Readerの結合が字画か、上方群に未読文字があるかは未確定。確定新文字0。 [左曲線](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-bend-normal-marked.png) · [上方横断](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-across-normal-marked.png) · [既知輪横断](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/known-across-normal-marked.png)

## 根拠・詳細

| 観測箇所 | 元CTとmeshの位置関係 |
| --- | --- |
| 上方の左曲線 U1/U2/U4 | [一次] 原軸断面では、三点が斜走する狭い帯かその境界の近くにある。法線断面の中央近くに追える明帯があるが、U1からU2の間は曲がりと隣接帯があり、中央を通る一本の連続性は確定しない。U2はd=−4で154 DN、d=0で88 DN。U4はd=0で144 DN、d=+4で42 DN。 [曲線断面](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-bend-normal-marked.png) · [U2原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/U2-orthogonal-marked.png) · [U4原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/U4-orthogonal-marked.png) |
| 上方の内側 U3と群間 U5 | [一次] U3は曲線内の低確率位置で、近接する斜走明帯と暗い隙間がある。U5では中央の小暗部が複数の近接帯に囲まれ、法線方向のd=−4/+4は106/143 DN、中央は70 DN。暗部が一枚の紙層を分断するかは不明。 [上方横断](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-across-normal-marked.png) · [U5原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/U5-orthogonal-marked.png) |
| 右隣 U6/U8/U7 | [一次] U6とU8は帯と空隙の境界付近。U7の中央はより明瞭な暗部にあり41 DN、d=+4に231 DNの明部がある。U8からU6/U7まで一条として追える帯は見えず、この範囲が一枚帰属の主な制約。 [隣接群断面](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-adjacent-normal-marked.png) · [U6原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/U6-orthogonal-marked.png) · [U7原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/U7-orthogonal-marked.png) |
| 作者既知の輪 K1–K4 | [一次] K1/K3/K4の輪縁は細帯または境界付近。輪内K2は43 DNでd=−4に132 DN。原軸と横断では近くに飽和状の明部があり、縦断でも中央の両側を通る帯が重なる。既知の字画配置は対照に使えるが、d=0が一条の明帯を通るという判定基準は得られない。 [既知位置図](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/known-locator.png) · [輪内原軸](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/K2-orthogonal-marked.png) · [輪の縦断](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/known-down-normal-marked.png) |

[一次] 候補のcarrier XYXYは [3424,3424,4160,3824)。既知は著者line 1 pos 8のο。著者主画像の箱 [4202,1778,261,296] から、R224で確認したfloat32軸・配置・上下反転を適用し、元carrierの画素中心範囲 x=4676.4443..4936.4443、y=2287.7407..2582.7407を得た。両者を著者のraw pixel/20規約でmesh XYZへ写像した。R225の既存の図を見て地点を選んだ探索的な比較。親は担当所見未閲覧で注釈図19枚を別目視し、同じ左側の部分支持、右側の帰属限界、層間切替の未立証を記録した。 [凍結計画](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/plan.json) · [独立計画照合](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/lead-plan-check.json) · [別目視](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/lead-visual-review.json)

[一次] 原CTは公式masked再構成L0のz/y/x、8 bit、無圧縮。原軸36面は整数DN。連続断面5本と位置図2枚は、meshの両接線から決めた局所法線に沿う診断用サンプリングを含み、すべて同じ0–255階調。最大の連続mesh座標間隔は1.035 voxel未満、最小の隣接法線内積は0.9994以上。CTで見える帯の途切れや分岐をモデルの結合・実際の層切替と同定する条件にはならない。METHODは中央名目層をlayer20と記述する。歴史的な描画実装との厳密一致が未確認のため、公開layer20 PNGとの画素比較は行っていない。 [表示仕様・断面一覧](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections-result.json) · [著者METHOD §2](../experiments/vesuvius/discovery/20261114-winning-method-gap01/originals/306b-method.md)

[一次] 主担当は元CT73キー・153,092,096 Bの全SHA256とS3 ETagのMD5、43 PNGの全417,780 DNを独立計算で照合し完全一致。XYZの最大絶対差は3.64×10⁻¹² voxel。HEAD/GETは204.34秒、描画処理は2.35秒、描画プロセスのピーク作業セット114,294,784 B。CPU1・プロセスcommit上限4 GiB、追加の基礎メタデータ3,281 B、D書き込み0、モデル推論0、GPU0、実費US$0。 [独立数値照合](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/lead-sample-check.json) · [資源](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/resources.json) · [manifest](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/record.json)

## 次に切り分ける一案

[推論] 著者が右端補正の判断に使った独立spiral-fitの同一巻回w074二面 `z8400`・`z8400o` を、まず固定した著者版の成果物一覧と構築スクリプトで探す。双方の同座標・同巻回・近傍支持が確かめられた場合は、U2側を起点に、U3–U5–U6を結ぶ今回の横断と二面の交点を比較する。とくに複数帯が接近するU5の前後で、二面が共に同じ帯を連続して辿るか、V5Rcの交点がその帯から離れるかを確認する。著者の右端補正で使った4 voxelはその既知部位の条件。今回の上方にその値をそのまま当てない。二面の配布と対象での両面被覆は未確認で、片方しか得られなければ独立二面での判定は保留する。 [著者の補正判断原票](../experiments/vesuvius/discovery/20261114-winning-method-gap01/originals/306b-surface-decision.json) · [対応する元CT横断](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/sections/upper-across-normal-marked.png)

## 取得の経路

- 公式S3のOME-Zarr v2の `.zgroup`、`.zattrs`、`0/.zarray` を取得し、元meshの補助m7 segmentationとは別のCTソースを固定。R224/R225の固定原票とR204のHEAD/GET、R214が借りたR204のCT補間・複写を再利用した。73キーすべてでHEADの本文長とETagを照合してからGET。 [取得原票](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/ct-acquisition.json) · [HTTPログ](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/ct-http.jsonl) · [入力参照とハッシュ](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/input-references.json)

## メモ

- 2026-11-15 [一次] 元CTは公式S3の `20250521133212-8.640um-1.2m-116keV-masked.zarr` L0。メタデータは ZYX、8-bit、無圧縮128³。既知輪の著者画像の箱をR224と同じfloat32リマップでcarrierへ戻した。R225図で探索的に上方8点と既知4点を選び、法線方向の連続断面5本、各点の原軸直交断面、2つのd=0位置図を [plan.json](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/plan.json) に固定。既存の適合CTキャッシュは確認できず、必要73キーで追加本文153,092,096 B。主担当も [独立計算](../experiments/vesuvius/discovery/20261115-pherc0306b-upper-original-ct01/lead-plan-check.json) で12点の位置と法線、全キーと417,780標本を照合した。照合後に元CT本文を取得。
