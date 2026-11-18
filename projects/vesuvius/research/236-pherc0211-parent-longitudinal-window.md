Status: resolved
担当: 研究（r236_pherc0211_parent_window / Astra xhigh / 2026-11-15）

# 236: PHerc0211の公開親面にある別の長手方向窓から、追試する字画を得られるか（2026-11-15）

## 依頼

- 問い: PHerc0211の受賞者が公開しているv6親面のうち、受賞行の中央寄りと連続する長手方向の別窓を使い、新しく評価する一窓から追試する字画/文字行を選べるか。手作業で新しい面を作る前に、既存の大きな親面の支持を使う介入である。
- 背景: R235はrecord-d17a739e0aa5へ登録済み。既知φ付近の紙層状帯は比較的見やすかったが、v9二行目右端の先は圧着/分岐が密で同じ一枚を選べず、その右端の局所CT診断と延長案を終了した。R228の0306B局所CT、R233の0800モデル比較も閉じた。そこへ戻らない。新文字0、公開改善三件、11月まとめ応募方針は維持。
- 材料の例: R234保存 `sources/v6-line2-mesh.zip` の `mesh/parent/normalized-tifxyz/` は230×303ノード・scale0.05で、公開単行の切出し2980:3580より広い。bbox Zは5224–9718。R234のv9三行面、公式記事の別提出図も先行範囲の手掛かり。v6のsplit.jsonは大きいseams配列を含むので、全体を出力せず必要な欄だけ読む。親面が存在することは正しい紙層の証明ではない。splitには親の予測を切り出した旨があり、未公開の先行作業も否定できない。公表図の緑枠外を未読と断定しない。
- 初期成果: 既知φの親面内位置、公開v6単行/v9三行との物理対応と範囲、親面の長手方向に選ぶ有限の一窓と既知対照を具体化する。右端の潰れを避け、中央寄りで既存面に支持のある区間を優先する。面の作成時の来歴と法線/解像度/表示方向を確認し、モデル出力を見る前に選択を固定する。先行公開図との重なりや新規性が不明ならそのまま不明と記す。
- 最初は保存資料と少量の原文/metadataだけで進め、主担当へ入力・位置・必要CTキー・取得量・再描画方法・対照・モデルforward数・出力量・費用見積を返す。初期新規保存64MiB以下、GPU0/料金0、D読取のみ、C空き2GiB以上。全親面を丸ごと再描画/ダウンロードする計画を無条件に走らせない。既存の局所CT/入力作成/モデル実行経路を先に確認し、同種の基盤を作り直さない。
- 入力の整合: 作者は正確なv6単行再現に親面全体の描画後crop+maskが必要と記している。独自の局所描画をそのまま厳密再現と呼ばない。公開の実入力や既知対照を利用し、選ぶ方式の座標/half-pixel/法線/深さ/量子化/支持を確かめる。例: 既知φの原CT36MiBはR235から再利用でき、公開v6入力ファイルは約58.18MB。必要量を確認してから取得を計画する。未知窓の入力を作るためだけに既知モデルの成立を何度も調べ直さない。
- 継続実行: 初期計画を主担当が確認したら、この同じ研究票内で入力取得・検証・固定一窓のStudio推論・原寸評価まで進めてよい。CPU1/既存hardcommit4GiBを基本とし、具体的保存枠は見積後に決める。有料実行が必要ならRunpod一台、見積・実費・所有権/絶対削除期限/回収予約/別削除照会までを具体化して親へ返す。本人はRunpod利用判断を主担当へ委任済みで本人への再承認要求はしない。計画前に台を作らない。
- 結果の扱い: この一窓から明確な追試先が得られなければ、同じ窓の深さ/モデル/閾値を増やして救済しない。反応が出ても公開既出との関係・紙層・別検証を経るまで新文字0。既知対照は入力/観測の確認で、独立の未知性能評価と混同しない。改善三件への自動加算も行わない。
- 保存先: `experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/`。取得原票・固定版・入力/計算/図/所見/費用を本票へ追記する。大きな配列や全manifestをtool出力へ出さない。初期計画と途中の実行結果を親へ共有し、主担当が数値と原寸を別確認した後に最終manifest/recordを凍結。再委任・lab/recall登録・外部公開/連絡/応募は主担当側で判断するので、この担当は行わない。

## 結論

**長手方向の固定一窓を用意したが、既知φの入力対照gateが不通過となり、未知窓の推論前に終了した。** 原寸の未知確率像は存在せず、字画/文字行の選定は未評価。ROI0・インクなし・候補面の不成立とは判定しない。新文字0、公開改善三件・11月まとめ応募方針を維持する。

公開v6入力と局所描画は固定262,144値中843値に最大1 DN差があり、当初の厳密再現に失敗した。主担当はこの失敗を保持したまま近似局所描画の探索へ計画を変更し、同一GPU/FP32モデルによる公開φ入力対局所入力の確率差を事前gateにした。実測absmax0.0028054118は上限0.005以内だが、meanabs0.0006942505が上限0.0005を超えたため予定どおり停止した。この差の読字/精度への科学的影響は別問題で未評価である。

実行は既存0343参照3＋pairedφ2の**計5 forward**。既知φ36・未知187は実行しなかった。閾値変更・再GPU・追加深さ/モデルの救済はしていない。結果を回収して専用Podを13:19:15.617UTCに削除し、担当・主担当ともGET404/name0を確認した。作成から196.932秒、時刻による費用見積US$0.03242694。専用請求明細の扱いは末尾の費用記録を参照する。[GPU原票](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/cloud-run/extracted/gpu/result.json)・[親の別検算](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/lead-output-check.json)・[資源記録](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/resources.json)

## 根拠・詳細

### 固定窓と未確定な先行範囲

v6親面の主域XYWH `[4352,1664,1024,640]` を、モデル出力を見る前に選んだ。既知φと同じUV列付近を小さいv/Zへ進む窓で、R235で閉じた右端を延長しない。主域のグリッド包絡はXYZ `[3048.6494,3437.7861,6800.9561]`–`[3922.9971,3874.3901,7476.7588]`。v9公開三行面の最小Z7524.437より小さいが、未読・未公開・新規領域とは断定しない。

- [一次・保存公開資料、2026-11-15] v6親面は230×303ノード・scale0.05、全canvas6060×4600。手修正2026-10-26のrev6、v9は2026-10-28の別手修正rev9であり、同一画素の単純平行移動ではない。v6単行は親Y2980:3580をcrop+mask。split原文は親の予測を切り出したと明記しており、親全体の先行推論を否定できない。[小メタ抽出](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/source-inspection.json)
- [一次計算、同日] 既知φのv9ノードr45,c240、XYZ `[3516.6299,3347.9063,8367.5996]` に最も近いv6親ノードはr163,c241（11.9284 voxel）。隣接quadのbilinear最近点は親UV `[4827.2391,3269.3417]`、距離1.59596 voxel。これは表面座標の近さであり同じ紙層の独立証明ではない。親の別Gauss–Newton確認ではXYZ差約5.16e-7 voxel。[幾何計画](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/geometry-plan.json)・[親の別検算](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/lead-geometry-check.json)
- [一次計算、同日] 未知主域の全親格子で寄与するStudio patchは187、入力支持XYWH `[4272,1584,1152,768]`。さらに二ノード拡張した支持は2816/2816ノードが有効。主域の全node包絡に±10 voxelを足してもv9最小Zから37.678 voxel離れる。面の連続UV支持を使うだけで、紙層の正しさは未検証。別提出図にはXYZ登録がなく重複は不明。
- [一次HEAD、同日] 保守的CT集合は142 chunk、全てHTTP200・各2,097,152 B、合計297,795,584 B（284 MiB）。2node拡張の各cell bbox±10 voxelによるsuperset。実際の描画8角支持がこの集合内であることをGET前に確認し、無断拡大しない。[HEAD原票](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/ct-head-plan.json)。旧`geometry-plan.json`の既知域全体CT見積168新chunkは探索時の上限で、初期計画には採用していない。
- [一次原文・主担当の取得、同日] 作者のpinned OCI renderer revisionは `1e3f4c021f4e53bea3867772ed05f51a7e586a9c`。現ローカルrendererとは異なる。旧版はsource-gridの中央差normalをnearest warpし、座標はbilinear、normalを再正規化する。CT位置はfloat32、uint8化は丸めではなく切捨て。[固定原文](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/lead-renderer-oci/source-extraction.json)。D側gitは親側調査中にpartial cloneのlazy fetchが判明したため以後禁止し、必要旧原文はCへHTTPS保存する。

### 実施した入力対照と当初の計画

公開v6 NPYは58,176,128 B、uint8 `[16,600,6060]`、SHA `b639ef3d91e21768a5c601cc8f0f36d7483cc3fd089b53f6ddf5c91511b30d9e`。親XYWH `[4768,3200,128,128]`＝公開strip `[4768,220,128,128]` の全16層を比較する。maskの16,384画素は全有効。必要9chunk/18MiBはR235既存CTに全て含まれ、新しいCT取得・複写は不要。

親canvas中心・128tile位相・half-pixel・旧nearest normal・offset+8..−7・切捨てを保存原文から局所移植する。CLI cropまたは単行meshの描画を厳密再現と呼ばない。固定262,144値が全一致した場合だけこのcropのexactを認め、差が出ればplane別不一致数・最大/平均DN差と原因を親へ返し、未知CT/GPUへ自動で進めない。一crop一致から親全面一致や正しい紙層を主張しない。

未知一窓が入力gateを通れば、CUDA FP32/同じStudioで未知187＋公開strip格子の既知φ36＋既存CPU参照のGPU確認3＝226 forwardを一回だけ行う案。既知φ主域はstrip `[4704,140,320,300]`、支持 `[4656,48,448,448]`。親格子とcrop格子の位相差、作者GH200/BF16との差があるので公開予測とのbit同一性は主張しない。追加深さ・逆順・別モデルなし。

### 資源案

当初の資源案は初期保存64 MiB内、CPU1/commit4 GiB、C空き2 GiB下限、D読取のみ。実行段階は新規保存上限768 MiB、予想450〜600 MiB、回収用64 MiBを事前に物理予約する案とした。Runpodは既存R233 controller/capture/deadlineを再利用し、Secure A40一台・再作成0・30分絶対削除期限、事前料金照会≤US$0.60/h、見積US$0.079〜0.159・運用上限US$0.35。実際の起動・削除は下記の実行結果に記録した。

### 実行結果と別検証

- [一次実測、2026-11-15] 103CT chunk/216,006,656 B（206 MiB）を225.68秒で取得。固定samplingの全14,155,776点・8cornerが103keys内で、親の別列挙と一致。候補input uint8[16,768,1152]を28.84秒で作り、SHA `27af8b21cee6e1abfd11e221075dc81cd1f1d0ac37aeb7d0045cd54fba23480c`、全zero画素0。主担当の独立float64原CT標本102,432値は差379・最大1 DN。[担当入力契約](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/candidate-input-contract.json)・[独立入力検算](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/lead-candidate-input-check.json)
- [一次実測、同日] 公開φpair262,144値と既知φ用448²×16入力3,211,264値は公開NPYと全一致。未知入力は近似renderとして固定し、主担当が全候補画素のfinite、normal node、座標（別float64と最大0.001221 voxel差）を確認。CT主域655,360画素もindices6:10 maxと一致した。紙層の正しさを認定する検査ではない。
- [一次実測、同日] 同じCUDA環境で全256値・全228予定patchの正規化SHAを照合し、その後5件だけmodel forwardを実行。既存CPU出力との最大差は1.94e−7、9.24e−7、6.26e−7。pairedφ出力は全finite、max0.0028054118・mean0.0006942505でmean gate不通過。主担当が5件の入力/正規化/出力と差分を別計算し一致した。未知canvas0・原寸未知評価なし。[対照gate](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/cloud-run/extracted/gpu/paired-phi-gate.json)・[主担当確認](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/lead-output-check.json)
- [一次運用、同日] 最初の起動試行は既存台1件でcreate前停止した。共通名簿で動画生成用 `agents-edo1116` と確認後、主担当がその正確なid/nameのみ許容する別controller/planを承認。既存台には操作せず、研究用 `xpbuoy304rmuaz` を一台だけ作成。64 MiB物理予約へ204,063 Bの結果archiveを同一fileID/SHAで保存し、367,922 Bを展開した。実作成13:15:58.685UTC、削除/不在13:19:15.617UTC、絶対期限13:45:57UTC内。最終allPods1は残した別用途台であり研究用残存ではない。請求は研究用idに限定し、口座差額を費用にしない。

### 次に考えられる有限の介入（未調査・未実行）

[推論、同日] 公開v6入力をそのまま利用できるのは600行の単行内であり、今回の候補を覆わない。公開v9入力も公開三行面の範囲である。別課題にするなら、**元の固定rendererのnative C++算術を使い、全親canvas/128tile位相を保持した小さなtile集合だけを標本化する入口**を検討できる。既存入口だけで可能か、小さなtile選択変更が必要かは未確認。最初に同じφでraw入力一致を判定する介入で、今回の閾値緩和ではない。compilerの積和融合、native math、843個の1 DN差の発生箇所は未同定。全親面のCT取得・全面描画を無条件に認める提案でもない。

## 取得の経路

R234 ZIPを直接読んで小メタと再現コードだけ抽出。splitの巨大seams配列は長さと選択列の値だけを記録した。初期は142個の公開S3 CTオブジェクトをHEADのみ確認し、承認後に実支持103件だけ全取得した。公開v6入力も正規公開Drive URLから全取得し、作者の全ファイルSHAを確認した。元の保存証跡は変更せず原票を別ファイルへ作成。未知モデル出力は生成していない。

## 本人への質問

なし。入力対照からの継続判断は主担当の研究権限内。Runpodの本人への再承認要求はしない。

## メモ

- 2026-11-15 着手。共通前提、AGENTS、lead、研究スキル、README、R234/R235/R233保存資料を確認。recallはfindのみ、登録なし。開始C空き8,071,458,816 B。
- 初期geometryはモデル出力取得前に固定。主担当の別計算でφ対応・主域非重複・187patch支持が一致した。初期計画保存時の新規出力総量568,634 B。主担当が追加した旧renderer原文を含む。
- 主担当へ公開入力取得と既存φ128²比較の条件を送付。入力GET、未知CT GET、GPUは未実施。最終manifestはまだ作成しない。
- 主担当の `lead-control-plan-approval.json` により公開input＋既存φ対照だけ承認。4.82秒で58,176,128 Bを全取得し、公開SHA・uint8 shape[16,600,6060]一致。`public-input-acquisition.json` に原票保存。
- 初回局所portは固定262,144値中843値が異なり、最大1 DN・平均絶対差0.00321579 DN。`control_compare.py` と `control-comparison.json`、差分/XYZ/normal配列を保存。比較3.76秒、追加CT0、GPU0、料金0、新規保存60,211,407 B。0 DN gate不通過として未知CT/GPUを停止した。差はfloat32演算/コンパイラの積和融合等の可能性があるが未同定で、主担当へ報告済み。主担当の別float64実装は1088値で最大1 DN差を確認したが、これはexact gateを緩めるものではない。
- 主担当は厳密再現の失敗を保持し、近似局所描画の探索へ目的を限定する新計画を判断した。`plan-v3.json` SHA `5e03444aad724d1629e6290644ee33d25c93c7094c3645a7a383f5092574ee43`。公開φ入力と局所render入力の同一GPU/FP32二forwardで、central96確率のabsmax≤0.005、meanabs≤0.0005、NaNなしを事前gateとする。順序は既存0343参照3→pairedφ2→gate→既知φ36→未知187、総228。gate不通過なら未知を実行しない。初回843差を事後に合格とは扱わない。
- 全14,155,776点・113,246,208 cornerを担当と親が別列挙し、必要unionは103keys/206MiBで初期142HEADの部分集合と一致。`lead-input-execution-approval.json`を受け、103件216,006,656Bを225.68秒で全取得、HEAD/GET ETag・MD5・SHA一致。上限を768MiBへ拡張し、Cfree2GiB・D読取のみを維持。
- 固定render式SHA `eb863455b8a107cb566079fd8e71e5e5cf351225cc420833185d69ed81f02279`で候補input16を28.84秒生成。uint8[16,768,1152]、14,155,904B、SHA `27af8b21cee6e1abfd11e221075dc81cd1f1d0ac37aeb7d0045cd54fba23480c`、全zero画素0。主担当の事前66×97格子×16層102,432値照合はmax1DN、差379値。公開pair262,144値とknownφ3,211,264値は原入力と全一致。CT主域PNG1024×640はindices6:10 maxの全655,360値一致、主担当のモデル前目視で明らかな空白/破損なし。紙層やインクの認定ではない。
- R233から一回のGPU経路・制御・回収・削除を移植。`cloud-plan.json` SHA `f1d415d58cf74d247e5228c3433ba236f240fce138aedbfed165eb695ca1b801`、archive21,536,052B、結果配列予定18,202,880B。offlineは228patch入力全SHA・5gateケース・archive全member・保存予算を確認。Podはまだ作成せず、主担当へ13:12UTCまでのprecreate/最遅13:42UTC削除のレビューを依頼した。科学計画 `plan.json` SHA `840f8a340e366982e1d89b14b99bc8dd51c542bdfffc6ed01c003e46f3d38d5e`。
- 主担当は25archive members・20controller SHA・228全patch・実行順/gate・回収/削除を別確認し、`lead-cloud-clearance.json`で一台実行を承認。13:08UTCにliveadmissionを行ったが、既存台1件によりcreate前停止。R236の台0、GPU0、追加料金0、launch receipt/物理予約なし、controller終了。既存台は `x7bt3pjbb741n0` / `agents-edo1116` / created2026-11-15T12:52:44.344Zで、識別metadataだけ読取し触れていない。`admission-existing-pods-readonly.json`・`precreate-stop.json`に記録。主担当から新規createやadmission規則変更を待つよう指示を受け、パッケージを保持して所有確認待ち。
- 別用途台の所有確認後、限定coexist版を別名に保存。cloud-plan-coexist SHA `c4676e6d7cf1405d77e83f3812bdcf36de76a292c9743ac6d5af833e7d931e3a`、科学archive SHA `df612995037c88d8d9f4f5cc8667b7e91ab211fdb97c3a7c7e8304201cbcaff6` は不変。旧admission失敗/計画/clearanceは保持。新承認はprecreate≤13:22UTC・削除≤13:52UTC、コードもUTCを検査。
- 許容既存台の再照会とliveadmission後、研究用 `xpbuoy304rmuaz` / `r236-studio-26992626130f3add` を一台だけ作成。precreate13:15:57UTC、実作成13:15:58.685UTC、固定削除期限13:45:57UTC。known3+paired2でmean gate停止、model worker5.86468秒、回収後13:19:15.617UTC削除。親の全5出力/LUT/SHA/差分検算と別削除照会を受領し、入力gate不通過として本票を閉じる。
- 13:26:26UTCの専用id請求再照会でもrecords0で、実費未確定。時刻見積US$0.03242694を実請求と区別する。GET404/name0/allPods1を再確認。口座残高差は別用途台を含み得るので使用しない。[請求追照会](../experiments/vesuvius/discovery/20261115-pherc0211-parent-window01/resource-billing-followup.json)。主担当の指示により、別検証コード/原票も含めたmanifestと登録候補recordを凍結する。lab/recall登録・公開・応募は行わない。
