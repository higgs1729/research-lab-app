Status: resolved
担当: 研究（R201担当、2026-11-14 JST）
Blocked by: 200

# 未読PHerc0846AのHecate二方向試験を外部GPU一台で行う具体案（2026-11-14）

## 依頼

研究199/200の入力とモデルは正常だが、混雑する手元CPUの所要予測が75分/100分枠を超えて最初3枚で停止した。完成画像がなく、字画は未判定。200の三確率は199と全ビット一致。2026-11-14 19:30JSTの手元GPUは別用途cw-stage-07が約51分保持し、その後にも既存待ち札があった。新しいCPU再試行や時間枠の再拡大は選ばず、この固定一領域・一モデルを外部GPUで完走する費用と実行案を用意する。これは実行前の準備であり、**有料計算は未承認、Pod作成・変更・課金は行わない**。

今回判定したいことは、199の保存入力でHecateの順/逆に追試する字画/行候補が現れるか。対象と入力は研究199のまま、XYWH[896,896,384,384]、内部[928,928,320,320]、中央16層[8:24]、forward8→23/reverse23→8、64²/stride32/batch1/fp32、各121枚計242。別入力/深さ/閾値、学習、新CT、別モデル、公開/応募/外部連絡は含めない。モデルは一度だけロード。最初の順方向3枚を本番に含め、保存CPU3確率とのMAE<=1e-4/max<=1e-3を満たすことを第4枚前に確認する。GPU未実測なので一致や完走は事前に保証しない。TF32/自動混合精度を使わない。全実入力/確率/座標/時間と両完成PNGを回収できるようにする。

不要となった研究194の既知対照実験を復活させない。194の固定Runpodイメージ、期限削除・所有判定・回収・ローカル検証の仕組みは再利用し、今回の入力/242枚/二方向/CPU参照に必要な部分だけ変え、全差分を残す。Pod一台・一回、希望構成はSecure RTX4090、開始から削除目標20分、計算工程600秒、概算約US$0.30・承認枠US$0.50税別を出発点とし、現在の公式料金・カタログ・在庫・固定イメージがこの案に合うか確認する。古い194の金額やコードを検証なしに転用しない。条件が合わなければ作成せず、その不足を報告する。

既存残高のみで実行、自動入金や追加決済が必要なら開始しない方針。本人承認前は残高/課金設定を変更しない。資格情報を資料・ログへ含めない。作成POSTは再送せず、応答不明の場合は専用名・時刻で照合して回収する。期限時はstopでなく専用Pod削除、API失敗時の回収手段と請求確認を記す。事業者の強制金額上限がない点と、端末/Pod双方の期限処理でも障害時に超過し得る点を明記する。原票194は変更しない。

成果は experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/ の見積もり・固定資産・実行前検証・実行案・短い承認文。ローカルでは構文/資産/tar/変更箇所を確認し、モデルforwardやPod作成は0。親が案と変更を独立に確認してから、本人へこの一実験の支出承認を求める。新規依存の導入、別研究/再委任はしない。

研究票へ準備範囲と実機未検証点を記録し、manifest/record候補まで。担当は **gpt-6.1-sol / xhigh**。既存の未実機確認のクラウド実行案を未知面二方向へ変えるため、停止・回収と数値同等性の条件を含む不確実性がある。主担当は数値契約とコード差分の別検証を担当する。

## 結論

PHerc0846Aの固定384²を、Runpod Secure RTX 4090一台で順・逆各121パッチを一回実行する案を用意した。2026-11-14 10:35:42 UTCの公式カタログでCUDA 13.0以上の在庫は4拠点、単価US$0.89/時。20分、20GB、通信費込みの税別見積もりは **US$0.29759**。作成直前の単価上限をUS$0.90/時、本人に求める運用上の承認枠をUS$0.50税別とする。追加決済が必要な場合は開始しない。実機の速度と数値一致は未測定。今回のPod作成・GPU・モデルforward・支出は0。 [見積もりと実行案](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/README.md) · [公式カタログ原票](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/catalog-snapshot.json)

## 根拠・詳細

- [一次] 公式料金原文は計算・コンテナディスクの秒課金、通信費0、1時間相当の起動クレジットを記載。Docker Hubの現行タグはR194と同じamd64 digestでactive。20分の内訳は起動240秒、入力と重み転送180秒、推論600秒、回収120秒、削除確認60秒。 [一次原文の取得記録](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/sources.json)
- [一次・ローカル確認] 入力tarは5,079,040 B。199/200の先頭3 CPU確率は同一で、各GPUパッチのMAE≤1e-4・最大差≤1e-3を第4パッチ前に求める。残239パッチの時間予測もこの時点で判定。合成242パッチで両PNGの回収と再集約294,912画素、作成応答喪失時にPOST一回と専用Podだけの削除を確認した。 [固定資産](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/fixed-assets.json) · [R194からの差分](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/r194-code.diff) · [ローカル確認](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/local-verified.json)
- [推論] 端末finallyとPod内絶対期限の自己DELETEを併用する。自己GETは自己DELETEの許可を確定しない。起動不全やAPI障害時はConsoleで専用名・作成時刻・IDを照合し削除する。20分とUS$0.50はいずれも強制上限ではない。 [停止・回収](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/README.md)
- [一次] 主担当の読み取り専用API照会で既存残高を確認した。Consoleの自動入金設定確認はログインの本人確認で止まり、追加決済が起きないことは未確認。承認後に必要な本人確認は手作業キュー agents:TASK-61 に登録。設定変更と課金は0。 [残高照会記録](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/lead-account-check.json)
- [一次] 主担当が全242入力契約、CPU確率3件、tar内9本文、OCI hash chainと現行タグ、単価と20分の算術を独立照合し、差分を確認した。 [独立照合](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/lead-review.json)

## 取得の経路

未認証の公式カタログGETは401。既存資格情報を出力せず、公式REST v2の同一GETで4090の一行のみを保存した。公開料金ページはPythonの標準User-Agentで403となり、curlで本文を取得した。管理・課金・環境変数の原文、現行REST schema、Dockerタグを保存。イメージレイヤーやモデルの追加取得は0。

## 本人への質問

主担当がこの一実験の承認を求める。自動入金の条件確認を終えてから起動可否を判断する。 [承認文案](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/approval-draft.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/record.json)

## メモ

公式カタログと料金仕様を保存し、R194の専用Pod管理をR199の固定入力・二方向へ移した。2026-11-14 JSTのローカル模擬検証では、実機、課金、推論の起動は0。
