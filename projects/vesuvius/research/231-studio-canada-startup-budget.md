Status: resolved
担当: 研究（r231_canada_control、gpt-6.1-sol/high、2026-11-15）
Blocked by: 230

# 231: 起動先と時間配分を固定して、Studio既知対照を回収・評価できるか（2026-11-15）

## 依頼

主目標は新しい文字の発見、低支出の初受賞、再利用できる知識と道具。研究は逐次。R230をrecord-b8be51a51151へ登録し、主担当が全28ファイルを照合した。Cの結果ファイル12MiB事前物理確保は模擬3GiB条件でも取得物を保持し、本番でも親別照合が通った。ただしEU-SE-1のA40はproviderのimage取得が240秒起動枠に収まらず、入力転送・forward0で削除した。費用時刻見積USD0.04026、明細未確定。R229は同じ固定image/A40でCA-MTL-1の起動markerが約120秒で成立し、後段collectへ到達した（結果自体は旧C条件で失った）。地域名から次も同じhost/キャッシュに当たるとは断定しない。

本件では次の一台の起動配置をCA-MTL-1に限定し、起動待ちを600秒まで割り当て、固定96パッチの科学結果を回収して評価する。同じ240秒の試行を繰り返さない。これは新しいモデル条件の探索ではなく、保存済み対照を完遂する運用上の限定変更。C保存契約はR230のまま、archive/科学ソース/CPU参照/モデル重み/前処理/表示評価もR229/230のまま。学習・新CT・面生成・深さ/向き/閾値の変更・追加未知窓を含めない。

保存先は `experiments/vesuvius/discovery/20261115-studio-canada-control01/`。参照元はR229のplan.json SHA d1a9774b2ad3816ade4234c4449577e86f2bf49cd6d809915a1a1c1ebebc0312、cloud-input-a40.tar.gz SHA499e33cc48383a9d88cdeeab70aa5618f0fc29f7563c51d90af52a929eb2115a、R230のcapture.py/collector/deadline管理。旧原票は不変、新しい出力のみ。科学17メンバは同一byteを使い、CPU参照を再forwardしない。重み893MBはPodへ直接一回取得、ローカルに再取得しない。

変更する実行契約は、CA-MTL-1限定、起動最大600秒、転送最大480秒かつ作成前基準から1080秒まで、モデル最大900秒かつ同1620秒まで、回収最大120秒かつ同1740秒まで、削除のため残り60秒、作成前から絶対1800秒である。最長起動の場合はモデルに最大540秒が残るが、実行時間がその枠で足りない場合は実測の見込み停止に従い、品質条件は緩めない。絶対期限を起動完了時にリセットしない。想定時間を実績として報告しない。旧起動240秒は短時間試行に使ってきた設定であり、今回のimage取得未了という実測に基づく新しい有限試験と記録する。

Secure A40一台、参考単価USD0.59/h・上限0.60/h、参考8〜20分USD0.079〜0.197＋小さいdisk、絶対30分上限の見積約USD0.3014以内、運用枠USD0.35（事業者の強制上限ではない）。本人はRunpod必要分の判断を主担当へ委任済み。直前に残高・自動入金無効・CA-MTL-1在庫/rateを確認し、条件未達なら作成しない。自動再作成・別地域/別GPUへの自動変更はしない。必要な別案は具体的根拠を親へ返す。

R230の物理予約・C空き2GiB/新書込64MiB/出力12MiB上限、GPU/RAM条件、専用Pod ID/名/createdAt照合、Pod PID1とouter finallyと独立local絶対監視、成功失敗時の削除と残存確認を保持。独立監視がreadyであることを作成前に確認する。すでに通ったR230回収テスト全体を繰り返さず、変えた配置/期限式を小さいオフライン検算で確認する。600秒起動時を含め絶対上限に収まること、選択された地域がCA-MTL-1のみであること、入力同一性を確認して差分/計画を親へ渡す。親の別レビュー後に一台を起動する。

起動中のprovider read-only logは有限採取し、段階の進展と実測を保存する。推論済みと推測しない。回収・削除を優先し、job-result/ログとgpu/以下の96patch、probability/numerator/weight/nonzero/resultを回収する。本件でも実行失敗なら原票で閉じ、同じ条件の自動retryをしない。親が別API照会で削除と専用明細を確認する。口座残高差を他用途と区別できない各Pod実費に配賦しない。

科学結果が成立したら、R229/230で準備した親独立再構成器に渡せるパスを先に知らせる。既知PHerc0343の同じmain [1344,1088,672,448]、CPU3参照、固定raw表示と事前補助表示で、既知の暗い囲い/曲がり、下側成分の分離、左細線終端を既存R222比較と見比べる。画像は一回最大4枚までにし、一度見た所見をメモし不必要に再読しない。親の別目視まで担当の視覚結論は送らない。既知実行対照でありheldout性能/AP/新文字/第四応募項目とは扱わない。実験後の未知投入は親が次の研究で選ぶ。

今回の担当はgpt-6.1-sol/highを明示的に選ぶ。原因・既存手順が固定できた狭い配置/時間配分変更と、既存数値検証・図作成の解釈を伴う実行のため。再委任せず本票一件のみ。研究票を完成し、重要所見と条件/費用/原票/manifest/record候補を残す。lab/recallは親が担当。公開・外部メッセージ・応募送信はしない。

## 結論

CA-MTL-1のSecure A40は200.888秒で起動し、固定入力と重みの照合、モデル読み込みまで進んだ。GPU forwardの直前に、最初のパッチの入力照合で停止した。失敗ログは物理予約から回収できた。GPU forwardは0で、96パッチの結果と既知字画は未評価、新文字0。

## 根拠・詳細

- [一次、2026-11-15 JST] 固定plan、6,980,298 Bのarchive、全17メンバ、保存CPU参照3件は同一。CA-MTL-1専用指定と、起動600秒の場合でも転送・モデル・回収・削除が作成前基準の1080/1620/1740/1800秒に収まることを検算した。固定モデルの第3patch予測は実際のモデル期限にも照合する設定。今回第3patchまで進むことはなかった。[計画](../experiments/vesuvius/discovery/20261115-studio-canada-control01/cloud-plan.json) · [オフラインの期限検算](../experiments/vesuvius/discovery/20261115-studio-canada-control01/offline-placement-deadlines.json)
- [一次、同日] Secure A40一台USD0.59/h。10:29:41 UTCに固定イメージ取得完了、10:29:50.888 UTCにPID1 marker確認。入力転送はreadyから48.624秒、重み893,443,724 BはPodで一回取得してSHAを照合。モデル読み込み後、`studio_worker.py:104` の `row == contract['positions'][i]` で例外が発生し、workerは終了コード1だった。[起動原票](../experiments/vesuvius/discovery/20261115-studio-canada-control01/cloud-run/startup.jsonl) · [例外ログ](../experiments/vesuvius/discovery/20261115-studio-canada-control01/cloud-run/extracted/model.log) · [終了原票](../experiments/vesuvius/discovery/20261115-studio-canada-control01/cloud-run/extracted/job-result.json)
- [一次、同日] 直接FP32除算で全96件のraw・正規化SHAをオフライン再現した。PyTorch v2.13.0 CUDAのCPUスカラー除算を模したFP32逆数乗算は全96件で異なるSHAになり、パッチ0では137,435値、最大絶対差5.9604645e-8だった。[推論、同日] この演算差が今回の停止を説明する。停止直前のGPU側rowは保存されていない。[照合原票](../experiments/vesuvius/discovery/20261115-studio-canada-control01/pre-forward-normalization.json) · [PyTorchの固定版原文](https://github.com/pytorch/pytorch/blob/v2.13.0/aten/src/ATen/native/cuda/BinaryDivTrueKernel.cu#L32-L49)
- [一次、同日] 結果用の実割当12 MiBの同じfile IDから、3,841 Bの失敗archiveと8ファイルをSHA照合して回収した。Pod `54g607o5gbhsk1` は10:30:58.628 UTCに削除・不在確認。主担当の別API照会でもGET 404、専用名0、全Pod0。APIのcreatedAtから267.454秒、時刻見積USD0.04404。10:31と10:34 UTCの専用明細に行がなく、実費未確定。再作成0。[回収原票](../experiments/vesuvius/discovery/20261115-studio-canada-control01/cloud-run/capture.json) · [展開原票](../experiments/vesuvius/discovery/20261115-studio-canada-control01/extraction.json) · [資源と費用](../experiments/vesuvius/discovery/20261115-studio-canada-control01/resources.json) · [主担当の別照会](../experiments/vesuvius/discovery/20261115-studio-canada-control01/lead-cloud-resource-check.json)

[実験報告](../experiments/vesuvius/discovery/20261115-studio-canada-control01/README.md) · [manifest](../experiments/vesuvius/discovery/20261115-studio-canada-control01/manifest.json) · [登録候補](../experiments/vesuvius/discovery/20261115-studio-canada-control01/record.json)

## 取得の経路

R230のcollectorと独立監視、R229の固定科学archiveを再利用した。providerの個別read-onlyログでイメージの展開からpull完了を追い、PID1の実応答で起動を確定した。停止後に固定入力のパッチ領域を読み、NumPyで二つのFP32演算を比較した。

## メモ

2026-11-15。R230の登録と親の28ファイル照合を前提に着手。R229とR230の原票を読み取り、CA-MTL-1と作成前基準の時間配分を専用フォルダで検算する。

2026-11-15。固定plan、gzip、全17メンバおよび予約・展開・図作成コードが先行実行と同一。CA-MTL-1以外を除外し、境界600秒の起動締切と最長時の1080/1620/1740/1800秒をオフラインで検算した。固定workerの予測はplan上の900秒を参照するため、割当が短い場合も期限内完遂の見込みを判定できるよう、指定Pod内の第3patch予測を実際のモデル期限に照合する処理をコントローラへ追加した。残520秒で見込み525秒の模擬では、正しい親PIDに結びついたworkerへの一度だけの停止要求を確認。先のfreeze原票は専用フォルダの `pre-forecast-review/` に保存し、更新版の別レビューを親へ依頼した。

2026-11-15 19:26 JST。親の別レビュー後、直前のAPIでCA-MTL-1のSecure A40在庫LOW、USD0.59/h、自動入金無効、残高USD17.1254108349、作成前の全Pod0を確認。独立監視がreadyになってから1台だけを作成した。Pod `54g607o5gbhsk1`、作成前基準10:26:30 UTC、起動期限10:36:30 UTC、絶対削除期限10:56:30 UTC。結果用の実割当12,582,912 B、予約後C空き10,129,301,504 B。

2026-11-15 19:31 JST。入力照合の失敗後、8ファイルを回収してから台の削除と残存なしを確認。画像と独立再構成への入力は生成されなかった。今回のGPU実行はこの1台で終了。
