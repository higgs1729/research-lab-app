# R239 — fixed approximate-window screen

R236の凍結入力・窓・Studio FP32モデルをそのまま使った別目的の探索を一回行い、原CTで追試する暫定ROIを一件選んだ。合意した親座標は **`[4416,2048,384,256]`**（候補主域内`[64,384,384,256]`）。明るさだけでなく、下側の太い横接続と下降部分のまとまりを担当・主担当が独立に選んだ。インク、読字、紙層、新規性は未確認で、新文字0。R240は主担当が別起票するため、本件では追加CT/研究を開始しない。

R236の入力max1 DN差、確率対mean差0.0006942505、およびR237/R238の厳密入力未成立を保持した。本研究は「有限の原CT追試場所を選ぶ」という評価へ明示的に変更した別計画であり、旧不合格を後から合格にしていない。旧pair閾値と`passed=false`をそのまま観測保存し、finite/モデルhash/入力hash/正規化/CPU参照などの実装検査は停止条件として保持した。

## Results

| 項目 | 結果 |
| --- | --- |
| forward数 | 既知0343参照3 + publicφ1 + renderφ1 + 公開knownφ36 + 未知187 = 228/228 |
| model load / 計算時間 | 1回 / 54.301315秒 |
| CPU参照3点の最大差 | 9.238719940185547e-7（事前上限1e-4以内） |
| 小φ対 raw差 | max0.0028054118156433105 / mean0.0006942504648274431、旧gate false |
| 小φ対 raw8差 | max1 DN、1,689/9,216画素、mean0.1832682292 DN |
| 公開φ全体 vs 今回公開入力FP32 | raw差max0.0217790902 / mean0.0038173835、raw8 max6 / mean0.9741667 DN（記述のみ、新閾値なし） |
| 主担当float64別Hann再合成 | knownφ96,000画素 max差2.25842e-7、candidate655,360画素 max差2.22902e-7 |
| 主担当表示照合 | 10図の全元画素値一致、無リサンプル |
| 原CT追試合意ROI | parent XYWH `[4416,2048,384,256]`、暫定1件 |

公開knownφ320×300では、暗い内側を囲む粗い環状部と縦軸を今回も確認した。これは**公開原入力で既知の粗い形が出る推論実装の対照**であり、近似renderで全体φを再現した証明ではない。未知領域全体のrender正確性や紙層を、小φ対と既存幾何/CT照合から保証しない。

未知の下側には横方向につながる幅広い反応と下降部分があり、固定raw0..1でも見える。上下の端で切れ、輪郭はぼけている。CT max4面表示には繊維・割れ・点状反射があり、同一紙層やインクとの対応は未確定。担当は小さい左下ROI、主担当は同じ下側の広い帯を独立選択した後、主担当が小さいROIを次の有限確認へ採用した。元の所見は変更せず、合意は`joint-decision.json`に別保存した。

## Evidence

- `saved-pair-*`/`researcher-pair-visual-review.json`/`lead-pair-*.json`: R236保存対の全値・同表示・別目視。旧gate値と失敗を維持。
- `sources/v6-probability-f32.tif`/`public-probability-acquisition.json`: Drive原TIFF11,940,462 B。R234 ZIP manifestのfile SHA `1b4b432867fb1f0f5cba844371b76813b2c5b7ad0df7b3a5bb14ee9c717abb65`と全画素SHA一致。固定320×300以外の探索的な窓選択なし。
- `public-known-phi-display-contract.json`、担当/主担当の公開全体目視、`lead-public-reference-check.json`: 固定公開全体対照と96,000値/PNGの独立検証。
- `gpu-proposal.md`/`plan.json`/`cloud-plan.json`/`lead-cloud-clearance.json`: 別目的、固定228ケース、資源/料金/UTC境界と主担当承認。
- `r236-to-r239-diff.patch`/`bundle-change-report.json`/`offline-check.json`: gate観測化・finite停止、192 MiB実上限、R239所有prefix、空の最新Pod一覧を使う最小変更。archive25memberのうち20件はR236とSHA一致、5件はplan/契約参照/gpu_loop/manifest。
- `cloud-run/extracted/`: 全228patch、knownφ/未知mainのprobability/numerator/weight/mask、device正規化検査、重み取得原票、ログと実行結果。
- `lead_output_check.py`/`lead-output-check.json`: workerをimportしない主担当の全patch/正規化/CPU出力/別Hann照合。
- `lead_display_check.py`/`lead-display-output-check.json`: raw/固定scaled/CT/4quadrantの元値照合。主担当helper/processのruntime原票もmanifestのexternal referencesに保存する。
- `researcher-output-visual-review.json`/`lead-output-visual-review.json`/`joint-decision.json`: 独立原寸所見とその後の合意。両者の元ROIを保持。
- `resources.json`/`postrun-absence.json`/`lead_cloud_resource_check.py`/`lead-cloud-resource-check.json`: 一台の実行・削除・専用費用の未確定範囲。

## Native figures

- `review/public-known-phi-raw8-native.png` と `review/known_phi-probability-raw-native.png`: 同じ320×300 knownφ、固定raw0..1表示。
- `review/candidate-probability-raw-native.png`: 未知主域1024×640、固定raw0..1。
- `review/candidate-ct-native.png`: 同じ主域、CT u8 max indices6:10。
- `review/candidate-native-quadrant-{00,01,10,11}.png`: 原寸CT/raw/事前固定median..p99.5。追加の閾値・深さ・モデル・窓探索なし。

## Resources and closure

Secure A40一台 `uh56ny6t7mpdqx` / `r239-studio-31e322a51025b003`、実効$0.59/h、CA-MTL-1。実precreate14:25:25 UTC、絶対削除期限14:55:25 UTC、finallyの削除不在確認14:32:39 UTC。主担当14:33:13 UTCに専用GET404・name0・全Pod0、担当も14:33:27 UTCにGET404・name0を別読取確認した。自動再作成0。64 MiB物理予約と同一fileIDで12,753,670 BをSHA検証して回収した。

想定費$0.08–0.16、運用上限$0.35。precreateから不在確認まで434.444708秒×料金+20GB一時diskの**時間単価概算は約$0.07154**。専用明細は`records=[]`のため**実費pending**で、空の集計0や口座残高差を請求額と呼ばない。後日の明細確認は主担当が別追記記録として扱い、この凍結結果を変更しない。

CPU1/commit4 GiB、新規保存192 MiB上限、C空き2 GiB下限。モデルGPU最大allocated1,345,575,936 B/reserved1,556,086,784 B、Pod process peak RSS2,426,384,384 B。新CT0、新CPU model forward0、Cへのcheckpoint取得0、D操作/Git0、共有install/update/build変更0。Podだけ固定重み893,443,724 Bを一度取得した。親の独立照合後にmanifest/record案を凍結。根拠登録・外部公開/連絡/応募は本担当未実施。
