Status: resolved
担当: 研究（R205担当、2026-11-14 JST）
Blocked by: 204

# 承認済みRunpod一回実験でPHerc0846AのHecate両順を完走できるか（2026-11-14）

## 依頼

研究201の具体的計画を一回実行する。本人は約US$0.30・運用枠US$0.50案への返答で「Runpodは必要ならその分自由に使っていいです 台の管理はしっかりしてね」と指示した。Runpodの必要分は主担当判断で利用することをAGENTS/README/system lead/heartbeatへ反映済み。本人のGoogleログインとブックマーク追加も完了との報告があり、TASK-61は終了済み。支出の再確認は求めない。

主担当は既存APIキーの正規の読み取りで、残高US$18.5044861634、自動入金false、台0、RTX4090 Secure US$0.89/時・在庫HIGHを確認済み。根拠は `runtime/runpod-20261114-authorization.json`、`runtime/runpod-20261114-billing-verified.json`、`runtime/runpod-20261114-current-resources.json`。Console公開JSから確認したmyselfの課金fieldをAPIで読めるので、認証や支出承認待ちへ戻らない。現在値は起動直前に再確認する。

計画と固定実行コードは `experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-plan01/`。201の凍結ファイルは変更しない。単価≤US$0.90/時、4090 Secure一台、固定OCI、期限20分、持続volume/公開portsなし、作成POST一回。起動前から専用名・実ID・開始時刻・期限・単価を保存する。成功・失敗・例外の全経路で今回の専用Podを削除し、APIで404/TERMINATEDと一覧からの消失を別確認する。既存Podや別仕事には触れない。起動失敗やGPU整合失敗の場合は自動再作成せず、証拠と費用を保存してから主担当が次を判断する。

現在のBilling条件を再確認したうえで、固定 `run_once.py --approved-run --existing-credits-checked --output <新しいrun01>` を一度実行する。既存API認証を使い、キー・メール・認証本文を出力へ含めない。処理開始時に専用名・ID・期限を主担当へ速やかに知らせる。起動や終了を他のheartbeatへ任せず、この研究内で最後まで管理する。

科学条件は201のまま。R199の固定384²・16層、順8→23／逆23→8、64²/stride32/batch1/fp32、1ロード最大242patch。先頭3patchはCPU参照のMAE≤1e-4/max≤1e-3、残時間予測・メモリ条件を満たす場合だけ続行する。結果tar・環境・全入力SHA・全patch確率・PNG・同じ環境のCPU Hannを回収。固定verify_resultで再集約を検算し、親もHannの数式を含め別確認する。新CT/学習/条件変更/二台目なし。完成画像は外部公開せず、既存CTと原寸で追試すべき字画/行の有無を判断する。

費用は実測のPod billing行を確認し、反映待ちでも台の削除確認は先に完了する。運用枠US$0.50や20分は事業者の強制上限ではない。台の削除が確認できなければ他研究へ進まず、専用原票を使ってrecover/API照合・Console確認を続け、本人へ実際の状況を伝える。

保存先 `experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/`、実行出力はその `run01/`。この票に結論・科学結果の範囲・起動削除・実費・失敗を追記し、README/manifest/record候補を残す。親の独立確認後に登録。再委任・別研究並列なし。

今回は **gpt-6.1-sol / xhigh** を選ぶ。固定計画の初の実GPU・外部API実行で、失敗時の資源回収とGPU/CPU数値差を判定する必要があるため。

## メモ

事前にR201 manifest全30件のSHAと、11:33:50 UTC時点で既存残高US$18.5044861634、自動入金false、既存Pod 0、Secure RTX 4090 US$0.89/時・在庫HIGHを確認した。11:34:02 UTCに単回作成、専用名 `r201-hecate-3c44b0a6d15cf04c`、ID `pqgmm8obc1rojl`、削除期限11:54:02 UTC。RUNNINGを見て呼んだ起動確認の管理execがHTTP 404で停止し、finallyで11:34:12.605 UTCに削除確認。11:34:37 UTCの別照合でもID 404・名前一覧0。初回請求照会では残高・明細に変化がなかった。入力送信・モデル処理・再作成0。 [入場](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/admission.json) · [起動原票](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/run01/launch-receipt.json) · [削除原票](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/run01/cleanup.json) · [独立照会](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/post-delete-01.json)

## 結論

[一次・実測] 一台を作成したが、管理execの起動確認HTTP 404により入力転送前に停止した。固定コードは再作成せず、同じIDの削除と一覧からの消失を約10.6秒で確認。担当と主担当も削除後のGET 404・全Pod 0を別確認した。入力転送、重み取得、モデルforward、完成PNGは0。PHerc0846Aの字画とGPU/CPU整合は未判定。 [実行ログ](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/launcher.log) · [主担当の削除確認](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/lead-deletion-check.json)

[一次・実測] 11:39:23 UTCに残高がUS$18.5044861634からUS$18.5034915884へ減り、差 **US$0.000994575**。11:42:37 UTCにも同じ残高、対象ID GET 404、全Pod 0。対象PodのREST明細とConsoleの同時間GPU明細は取得時点で0行で、GPU・ディスクの内訳と課金秒は未確認。残高差は実測のアカウント値として記録した。追加入金はなし。 [最終請求照会](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/post-delete-window-final.json) · [Console請求照会](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/console-gpu-billing.json)

## 根拠・詳細

Runpod APIはPod詳細をRUNNINGで返した後、watchdog markerの確認execで404を返した。固定controllerがエラー本文を保持しないため原因は未確定。現在の公式仕様はコンテナ準備待ちに409、exec未対応・一時利用不能に503を記載する。同じAPIキーの所属照会はaccount 200、organization 404で、組織指定のヘッダーは未送信。起動確認の失敗をHecateやGPUの不良と扱う根拠はない。 [所属確認](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/identity-scope.json) · [Runpodのexec仕様](https://docs.runpod.io/api-reference-v2/pods/run-a-command-in-a-pod)

固定R201のmanifest全30件を照合して同コードを一回実行。20分とUS$0.50は管理値として使用した。固定コード、入力、重みを変更せず、別Pod・新CT・GPU推論・公開は0。 [実験README](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-cloud-run01/record.json)
