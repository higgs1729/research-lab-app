# Runpod起動確認のHTTP 404を切り分ける

[研究206](../../../../research/206-runpod-exec-diagnostic.md)。R205はPod詳細でRUNNINGになった後、起動確認のexecで404。本文を保存していなかったため原因は未確定。親が削除済みのR205専用IDを別確認したときは、404の構造化JSON `detail="Pod not found"` を得た。今回の実在Podに対する本文と区別する。 [R205](../20261114-pherc0846a-hecate-cloud-run01/README.md) · [比較原票](lead-deleted-exec-reference.json)

## R201からの変更

`diagnostic.py` が凍結R201の `run_once.py` を読み、起動確認関数だけを差し替える。作成・アップロード・科学worker・回収・finallyの専用Pod削除は同じコード。科学入力tarは5,079,040 B、SHA-256 `6386a46d938f1fce52e4bc50cdbf00d13e4190098d54ebe36e5bc93ed7a2b782` で一致。作成POSTの再送なし。 [診断コード](diagnostic.py) · [R201固定コード](../20261114-pherc0846a-hecate-cloud-plan01/run_once.py)

起動確認は全体240秒。同じPodの読み取り専用markerについて、409/503はRetry-Afterを考慮し、404は所有・構成を再確認して最大3回、最初の404から30秒まで調べる。401/403、Pod消失・構成不一致、markerの不正状態は停止。HTTP失敗は時刻・method・path・status・Retry-After・伏せ字済み本文を保存する。本文は最大2,048 Bを読み、指定JSONフィールドまたは定型短文を残す。作成や転送等の失敗本文は要求内容の反射を避けるため記録しない。markerは終了状態、自己GETステータス、期限、伏せ字済みstderrを保存。 [exec公式原文](originals/run-a-command-in-a-pod.md)

SSE起動ログは同一Pod・tail 12行、最大8 KiB、呼出元の待機上限2秒。コンテナ出力は既知watchdog行、システム出力は起動に関係する行に絞り、伏せ字を通す。取得不可でも本来の停止・削除を続ける。 [ログ公式原文](originals/stream-pod-logs.md) · [ローカル検証](local-verified-02.json)

起動直前に既存残高、auto-pay無効、既存台、Secure RTX4090在庫、単価≤US$0.90/時を再確認する。見積もりは20分でUS$0.29759（$0.89/時）、上限単価ならUS$0.30093、税別。絶対期限20分とUS$0.50は運用管理値。開始後は専用台の削除・GETと一覧・請求を確認する。 [固定価格根拠](../20261114-pherc0846a-hecate-cloud-plan01/README.md)

## 実行

2026-11-14 11:52:54 UTCの既存残高US$18.5034915884、auto-pay=false、他Pod 0、在庫HIGH、単価US$0.89/時。11:52:55 UTCに専用名 `r201-hecate-5d434966c490062d`、Pod ID `cdennye0tecc74` を単回POSTで作成した。EUR-IS-2、Secure RTX4090、実単価US$0.89/時、20GB、持続volume/公開ports 0、絶対期限12:12:55 UTC。 [入場](admission.json) · [作成](run01/launch-receipt.json)

GETはRUNNINGを返したが、read-only marker execは構造化HTTP 409で「Pod container is starting, retry shortly」、Retry-After 5秒を3回返した。同じIDで11:53:18.442 UTCにHTTP 200、markerの自己GET 200・ID・期限が一致。SSEからキャッシュ済みの固定イメージdigest、コンテナ開始、自己GET 200も確認した。今回は準備確認のexecに404が現れず、205の404原因は確定できない。 [起動時系列](run01/startup.jsonl)

同一固定入力33×384²の中央16層、順8→23・逆23→8、1ロード、CPU affinity 1、RTX 4090・CUDA 13.0・Torch 2.13.0+cu130、TF32/AMPなし、64²/stride32/batch1。固定重み522,576,086 Bの取得と照合5.863秒、ロード1.722秒、モデル工程16.571秒、peak GPU予約897,581,056 B、peak RSS 1,691,156,480 B。最初の3枚はMAE最大2.636×10⁻⁷・最大絶対差4.828×10⁻⁶でCPU比較を通り、残り239枚の見積13.227秒が残り595.796秒に収まった。順・逆各121枚を完走し、固定検証と主担当の独立検証で入力242件、確率991,232値、PNG294,912値を照合した。主担当の解析式と保存Hannの最大差は1.885×10⁻⁷。 [転送](transfer.json) · [実測](execution-result.json) · [先頭3枚](first-three.json) · [固定検証](verified-result.json) · [独立検証](lead-result-check.json)

## 原寸目視

順は暗い背景に離れた丸みのある反応、逆は中央左と右上の広い塊、右下の斜め帯が目立つ。一部はCTの繊維や割れ状部分と近い。担当と主担当は、全384²および主比較320²で、追試に値する一続きの字画や行の座標を選ばなかった。同近傍のR176ではseed42/dense-nativeも候補がなく、異なる格子・深さ窓でコントラストには差がある。この固定面・領域・窓の判定であり、物理的な紙面、訓練曝露、インクの有無は未確定。 [原寸320²](comparison-320.png) · [原寸384²](comparison-384.png) · [担当と主担当の目視](visual-review.json)

## 回収と削除

結果tar 4,833,280 Bを回収し、端末側finallyから11:55:04.217 UTCに専用台の削除を確認した。作成記録から129.217秒。担当の別GETで404・一覧全Pod 0、主担当も11:55:59 UTCに独立確認した。専用Podの自己DELETEを待たずに終了した。 [回収tar](run01/results.tar) · [削除原票](run01/cleanup.json) · [担当確認](post-delete-01.json) · [主担当確認](lead-deletion-check.json)

最終の12:01:00 UTCにGET 404、全Pod 0、auto-pay=false。作成前US$18.5034915884、削除5分経過後US$18.4730300208で、実測残高差は **US$0.0304615676**。初回照会の差US$0.0051652954から更新され、12:00:33と12:01:00で同額。対象Podの時間指定明細は0行で、課金秒数と計算・ディスクの内訳は未確認。R205のIDも作成前に再照会し、Pod別明細は未反映。 [最終請求照会](post-delete-final.json) · [課金サイクル後の照会](post-delete-cycle01.json) · [R205請求追補](prior-205-billing.json)
