Status: resolved
担当: 研究（r230_reserved_capture、gpt-6.1-sol/high、2026-11-15）
Blocked by: 229

# 230: 結果用領域を事前確保すれば、同じStudio既知対照を失わず回収できるか（2026-11-15）

## 依頼

主目標は新しい文字の発見、低支出の初受賞、再利用できる知識と道具。研究は逐次。R229をrecord-605dc4dacb3dへ登録し、全129ファイルを主担当が照合した。既知文字対照のソース・入力・CPU参照3件は成立したが、専用A40の出力archiveを全取得・SHA照合した後、保存前のC空き10GiB条件で停止して科学結果を失った。GPU実forward数とモデル成否は不明。台は約191秒で削除、主担当もGET404/専用名0/全Pod0を別確認。時刻見積USD0.03139、請求明細は未確定。C空き低下の消費元は未特定。同じcollectorのまま再計算しない。

本件は回収経路の限定修正と、R229と全く同じ一条件96パッチの既知対照一回。大きい研究基盤や別条件の探索は作らない。問いは、課金前に必要な出力領域を物理的に確保しておき、その後のC空き低下で取得済み結果を捨てず回収できるか、回収後にモデルの既知字画再現を評価できるか。研究票の依頼を保持し結論と根拠を追記する。

固定科学条件は `experiments/vesuvius/discovery/20261115-new-211-winner-model01/plan.json` SHA d1a9774b2ad3816ade4234c4449577e86f2bf49cd6d809915a1a1c1ebebc0312。保存CPU0/47/95、input16.npy、公式モデルソース、safetensors SHA96b32628を再利用し、CPU参照の再forwardをしない。PHerc0343の同じmain/support、16層+8..-7、128入力/中央96/stride64、clip200div255、sigmoid後Hann、96パッチ、FP32/batch1/TF32off、CPU-GPU tolerance1e-4。学習・元CT追加・再描画・深さ/向き/閾値探し・未知窓の実行・追加公開は含めない。条件を変えて見た目を救済しない。

既存R229 A40 archiveと科学worker、R217/219/229の期限/所有権/削除コードを借りる。重み893MBはPodへ固定公開URLから直接一回取得、ローカル再取得なし。原票は上書きせず、保存先は `experiments/vesuvius/discovery/20261115-studio-reserved-capture01/`。Dは読むだけ。

今回は主担当が、小さい回収用の新しいディスク契約を明示的に採用する。旧R229の10GiB条件を後から書き換えず、R230で新規ローカル書込を最大64MiBに制限し、起動前にはC空き2GiB以上と最大12MiBの結果領域を物理確保する。確保済み領域への回収は、新たな10GiB空き判定で捨てない。これは大きいCT/重み取得の条件変更ではなく、本件の小さい固定出力に限る。RAM/VRAMの入場・実行制限はそのまま維持。疎ファイルや圧縮による見かけだけの予約ではないこと、予約の所有権・上限と書込み後のarchive SHAを確認する。書込やfsync自体の実I/O障害まで成功を保証しない。既存ファイルへ書く最小変更を優先し、汎用キュー・新サービス・重い監視基盤へ広げない。

課金前に、C空きが後から旧10GiBを割った状態を模擬しても予約領域へ正しいarchiveを回収できることを確認する。実ディスクを埋める負荷試験はしない。上限超過やSHA不一致・予約欠損を正常結果と扱わないことも、同じ取得経路で小さく確認する。workerが失敗しても取得できたjob-result/logを保存し、台の削除を完遂する条件は維持。必要なテストを済ませたら繰り返さず、修正差分・原票・入力同一性を主担当へ渡す。主担当の別レビュー後に一台を起動する。

Runpod必要分の支出判断は本人から主担当へ委任済みで、本人への再承認は不要。候補はSecure A40一台、参考単価USD0.59/h・上限0.60/h、8〜20分の参考見積USD0.079〜0.197＋微小disk、最長1800秒・運用枠USD0.35（事業者の強制上限ではない）。即時の在庫・残高・自動入金無効・rateを確認し、変更が必要なら具体案を主担当へ返す。作成前からの絶対UTC期限、Pod PID1・outer finally・独立local監視、専用ID/名/作成時刻の照合、成功失敗とも削除と残存確認を保持。無断の機種切替や自動再試行をしない。主担当も最後に別API照会と専用明細を確認する。

回収後はR229で準備済みの主担当独立再構成器を流用できる形で、96patch・確率/分子/重み/mask・CPU比較原票を保存する。既存R222の同じCT/Reader/public比較を借り、原寸の固定raw表示と事前に決めた補助表示で既知の暗い囲い/曲がり、下側成分の分離、左細線終端を確認する。親へ先に画像パスを知らせ、親の別目視が済むまで自分の視覚結論は送らない。実行整合の対照であり、heldout性能・AP・新文字・第四応募項目の主張にしない。成功しても未読への次投入は別の研究を主担当が選ぶ。

重要結果には別の検証を残す。担当は今回はgpt-6.1-sol/highを明示的に選ぶ。原因箇所と借用する科学/資源管理手順が固定できているため、その解釈を伴う限定修正と再実行に適する。再委任なし、一件のみ。lab/recall登録は親が重複を確認して行うため担当は実行しない。外部メッセージ・公開・応募送信なし。最後にrecord候補/manifestと研究票を完成させる。

## 結論

結果領域の物理予約は、旧10 GiB条件を割った場合の回収に使えた。同じcollectorのオフライン試験で、模擬C空き3 GiBから失敗workerのarchiveを保存し、書込み後のSHAを確認した。Secure A40でも作成前に実割当12 MiBを確認したが、固定コンテナ画像の取得中に起動枠240秒に達して停止した。GPU forwardは0。本番archive回収と既知字画再現は未評価、新文字0。

## 根拠・詳細

- [一次、2026-11-15 JST] 旧collectorは模擬空き3 GiBで2チャンク取得後に停止した。新collectorは非疎・非圧縮・単一リンクのNTFSファイルに同じfile IDで書き、fsync、サイズと読戻しSHAを照合できた。超過サイズ・誤SHA・所有ID不一致・予約欠損を拒否し、終了コード3を含むjob-resultと2つのログを保存した。[試験](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/offline-collection-test.json) · [差分](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/collector.diff)
- [一次、同日] R229 A40 archiveのSHAと全17メンバを照合。固定plan、入力、CPU0/47/95を再利用し、再forwardは0。有償試行にも物理割当12,582,912 Bを確保し、予約後の実C空き10,407,673,856 Bとfile IDを記録した。親が同じ割当・IDを別確認した。[固定計画](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/cloud-plan.json) · [親の物理確認](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/lead-live-reservation-check.json)
- [一次、同日] EU-SE-1、Secure A40一台をUSD0.59/hで作成。起動確認execはHTTP409が36回、初期404が2回。10:02:06 UTCのproviderログに固定イメージを取得中とあり、既定の起動枠にPID1の確認が成立しなかった。入力転送・重み取得・モデル起動は0。再作成は0。[起動原票](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/cloud-run/startup.jsonl) · [providerログ](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/startup-probe/startup.jsonl)
- [一次、同日] Pod `1rznb9oa1abxn1` の削除を10:02:54.690520 UTCに確認し、親も別APIでGET404、専用名0、全Pod0を確認した。create前の独立local監視は終了後に残存せず、未使用予約を解放した。APIのcreatedAtから244.51752秒、旧20 GB disk式を含む時刻見積USD0.04026238。専用明細は空で実費未確定。[資源・費用](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/resources.json) · [親のAPI照会](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/lead-cloud-resource-check.json) · [予約解放](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/reservation-release.json)

[実験報告](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/README.md) · [manifest](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/manifest.json) · [登録候補](../experiments/vesuvius/discovery/20261115-studio-reserved-capture01/record.json)

## 取得の経路

R229の固定入力gzipを読み取り、R208/R206のreadinessとR229の束ね方・所有確認・削除を借りた。Windowsでは先にファイルを12 MiBへ設定して全域を書き、`GetFileInformationByHandleEx` の割当・属性とfile IDを確認した。読取専用の個別Podログで、RESTのRUNNING表示中もイメージ取得が続いていたことを確認した。

## メモ

2026-11-15。R229の登録・親のmanifest照合を前提に着手。R229 A40入力archiveをそのまま読取り、Runpod作成前にR230専用の物理予約と故障試験を確認する。

2026-11-15 18:58 JST。オフラインの同一exec収集経路で、C空きの模擬3 GiB時に旧版は全2チャンク取得後の10 GiB条件で停止。新版はWindows実割当12,582,912 B、非疎・非圧縮、単一リンク、同じfile IDへの書戻しとfsync・読戻しSHAを確認し、失敗workerのjob-result/logを回収した。上限超過、誤SHA、所有ID不一致、予約欠損を拒否した。R229 gzipのSHAと17件の全メンバを照合し、独立レビュー後にA40一台だけを起動した。作成前基準09:58:49 UTC、絶対削除10:28:49 UTC、Pod `1rznb9oa1abxn1`。実行前にCの空きは10 GiB未満、予約後10,407,673,856 B。別local監視が作成前にready。
