# PHerc0846AのRunpod一回実験

[研究205](../../../../research/205-pherc0846a-runpod-hecate.md)（2026-11-14 JST）。Runpod Secure RTX 4090を専用で一台作成。管理APIで起動確認のコマンドを送るとHTTP 404になり、入力転送前に終了した。推論・GPU/CPU比較・完成PNGの回収は未実施。PHerc0846Aの字画・行の有無は未判定。 [実行ログ](launcher.log) · [固定実行案](../20261114-pherc0846a-hecate-cloud-plan01/README.md)

| UTC（2026-11-14） | 実測 |
| --- | --- |
| 11:33:50.227 | 残高US$18.5044861634、auto-pay無効、既存Pod 0、Secure 4090在庫HIGH・候補5拠点、表示単価US$0.89/時 |
| 11:34:02 | 単回作成要求、専用名 `r201-hecate-3c44b0a6d15cf04c`、ID `pqgmm8obc1rojl` |
| 11:34:12.605 | 固定controllerの削除完了確認。記録した作成秒から10.605秒 |
| 11:34:37.661 | 担当の別API照会で同ID 404・専用名の一覧一致0 |
| 11:54:02 | 作成前に設定した絶対削除期限 |

作成前にR201 manifest全30件のSHAを照合した。コードの変更0、Pod作成POST一回、再作成0。作成応答で専用IDを取得し、構成照合を通過。固定コードがGETでRUNNINGを確認した後、watchdog markerを読む `POST /v2/pods/{id}/exec` が404。エラー本文は固定controllerが保存しないため、実行ホスト・権限・サービスのどこで拒否されたかは確定できない。watchdogの自己GET／自己削除の成立は未確認。端末側finallyの削除を確認し、回収用tarは生成されなかった。 [事前確認](admission.json) · [作成原票](run01/launch-receipt.json) · [削除原票](run01/cleanup.json) · [削除後照合](post-delete-01.json) · [Runpod REST仕様](https://api.runpod.io/v2/openapi.json)

同じAPIキーで `GET /v2/account` は200、`GET /v2/organization` は404。現行REST仕様は非所属のとき404を返すと記載。作成・詳細・execの各要求に `X-Team-Id` は送っていない。REST仕様ではexecが呼出元自身のアカウントに限定され、コンテナ準備待ちは409、ホスト側のexec未対応等は503。今回の404を準備待ちと同一視できる資料はなく、エラー本文が未保存のため原因は不明。 [所属照会](identity-scope.json) · [Runpod REST仕様](https://api.runpod.io/v2/openapi.json)

11:34:37 UTC、11:35:26 UTC、11:37:02 UTCのPod ID指定請求照会はHTTP 200、対象明細0行、残高は作成前と同額。Runpodの課金サイクル5分を超えた11:39:23 UTCに残高がUS$18.5034915884へ減り、11:42:37 UTCも同額。既存残高の実測減少は **US$0.000994575**。11:39:56 UTCの対象指定・無指定のPod請求および時間別全利用明細はすべて0行。公開Consoleと同じGPU請求の読み取りも、対象時間帯の行は得られなかった。Pod別内訳・課金秒は未確定。GraphQLの型照会はHTTP 400で終了し、Consoleに公開されているクエリを一度使用した。 [5分後](post-delete-window-02.json) · [複数経路照合](billing-crosscheck-01.json) · [Console請求照会](console-gpu-billing.json) · [最終請求照会](post-delete-window-final.json) · [Runpod課金仕様](https://docs.runpod.io/accounts-billing/billing)

最終照会時にも全Pod 0、専用ID GET 404。主担当も別に一覧全件と専用IDの消失を確認した。自動入金は引き続きfalse。専用Podの終了と請求反映の確認はこの研究内で行った。 [主担当の削除確認](lead-deletion-check.json)
