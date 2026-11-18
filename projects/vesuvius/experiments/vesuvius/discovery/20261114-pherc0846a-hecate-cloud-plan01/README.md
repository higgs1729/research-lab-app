# PHerc0846AのHecate二方向試験の見積もり

Runpod Secure RTX 4090を1台、固定384²の順・逆各121パッチに一回だけ使う案。2026-11-14 10:35:42 UTCの公式カタログは **US$0.89/時**。CUDA 13.0以上の4拠点に割当候補があり、EU-RO-1はHIGH、EUR-IS-1/2・US-IL-1はLOW。起動前に再取得し、在庫と **$0.90/時以下** を確かめる。割当後も実単価と構成を読み返す。 [公式カタログ取得原票](catalog-snapshot.json) · [公開料金表](https://www.runpod.io/pricing)

| 工程 | 予算時間 | 計算費 |
| --- | ---: | ---: |
| 割当・コンテナ起動 | 240秒 | $0.05933 |
| 固定入力送信・固定重み取得と照合 | 180秒 | $0.04450 |
| 環境確認・1ロード・最大242パッチ | 600秒 | $0.14833 |
| 結果回収 | 120秒 | $0.02967 |
| 専用Pod削除・確認 | 60秒 | $0.01483 |
| **GPU計算計** | **20分** | **$0.29667** |
| 20GBコンテナディスク・$0.10/GB/月・30日換算 | 20分 | $0.00093 |
| **20分の概算・税別** | | **$0.29759** |

単価が$0.90/時なら20分で$0.30093。通信料は$0、持続ディスク・ネットワークボリュームは0。秒課金で、起動には構成の1時間相当の既存クレジットが必要。作成直前に同じアカウントのBillingで残高、自動入金の発動条件と既存消費を確認し、追加決済が必要または判断できない場合は保留する。承認枠の案は **US$0.50税別**、専用Pod削除の目標は作成要求前から20分。いずれも運用上の管理値で、事業者の強制上限は確認できない。 [Pod料金の保存原文](originals/pods-pricing.md) · [Runpod課金仕様](https://docs.runpod.io/accounts-billing/billing)

主担当の読み取り専用照会で既存残高を確認した。自動入金の設定確認はConsoleログインの本人確認で止まった。追加決済が発生しない条件は未確認で、実行用フラグ `--existing-credits-checked` をまだ付けられない。承認後に必要な本人確認は agents:TASK-61。 [残高照会記録](lead-account-check.json)

## 起動と判定

1. 本人がこの一実験を承認し、現在の在庫・単価・既存残高が条件に合う場合、Windows端末で `python -B run_once.py --approved-run --existing-credits-checked --output <未作成のローカルディレクトリ>` を一回実行する。作成前に固有名が空いていることを確認し、名前と作成時刻を保存してから作成POSTを一回送る。作成応答が不明なら同じPOSTを送らず、固有名・作成窓・得られた場合はPod IDから専用Podを照合して削除する。
2. R194と同じ固定OCI digestのRunpod PyTorch 2.13.0/CUDA 13.0/Ubuntu 24.04。現在のDocker Hubタグも同じdigestでactive。R194の保存configでは `/usr/local/bin/python` とcu130 Torchの組み合わせを確認した。管理APIのexecを使用し、公開ポートなし。Pod自身の期限・ID・自己GETの一致後に転送する。固定入力tar 5,079,040 Bを36 execで転送・照合し、Podが配布元の固定重み522,576,086 Bを180秒の同じ転送枠内で取得する。冷状態のイメージは圧縮9.72 GBで起動240秒を超え得る。 [固定資産](fixed-assets.json) · [現行Dockerタグ](originals/docker-tag.json) · [R194固定OCI config](../20261114-hecate-cloud-estimate01/originals/docker-config.json)
3. R199保存CTのXYWH [896,896,384,384]、内部[928,928,320,320]。中央16層 [8:24]、順8→23・逆23→8、公式predict（3D入力から2D出力）、FP32、64²/stride32/batch1、TF32・AMPなし。1ロード、同一の121位置×2。先頭の順方向3パッチは本番に含め、199/200でバイト一致したCPU確率との全値MAE≤1e-4、最大差≤1e-3を各パッチで要求する。比較不合格、残239パッチの時間予測が残枠超過、メモリ下限・上限違反で停止。新CT、条件変更、別Pod、再実行は含まない。 [実行コード](run_pilot.py) · [全変更差分](r194-code.diff)
4. 全実入力の座標・支持・raw/正規化SHA、保存確率、パッチ時間と両PNGを回収する。ローカルの `python -B verify_result.py <results.tar>` はモデルを呼ばず、CT支持・環境と同じCPU Hann・保存確率からPNG全294,912画素を照合する。完成時は担当と主担当が原寸CT・両PNGを別々に見て、追試する字画や行を座標で指せるか判断する。R176との比較は同じ近傍の別格子で行う。
5. 成功、失敗、時間超過で今回の専用PodをDELETEし、同一IDの404またはTERMINATEDと一覧からの消失を確認する。確認不能なら同じ原票で `--recover --output <同じディレクトリ>` を使用する。API障害時は専用名・作成時刻・既知IDをConsoleで照合して削除する。削除後にBillingまたは `GET /v2/billing/pods?podId=<ID>` で実額を確認し、反映待ちの間もPodは削除した状態にする。stopでは持続ディスクが残り得る。 [Pod管理](https://docs.runpod.io/pods/manage-pods) · [Runpod REST仕様](originals/openapi.json)

端末のfinallyとPod PID 1の絶対UTC自己DELETEを併用する。Podは事業者が注入する専用キーで自身だけを対象にする。自己GETの成功からDELETE権限は分からない。端末停止、コンテナ起動不全、API障害、Pod専用キーの権限不足では20分や$0.50を超え得る。 [Pod環境変数](https://docs.runpod.io/pods/templates/environment-variables)

## 実行前確認

現行の作成・exec要求schema、固定入力、CPU参照、重みSHA、入力tarをローカルで照合した。合成の242パッチ・両PNGを実際の回収コードで取り込み、PNG全画素を照合した。作成応答を失う模擬APIではPOST一回で所有の一台だけを削除した。主担当も全入力・CPU参照・tar本文・イメージ・価格を独立確認した。クラウドの起動、execの転送時間、Pod専用キーのDELETE、実GPUの数値一致と速度は未検証。Pod作成、課金、GPU、モデルforwardは0。 [ローカル確認](local-verified.json) · [主担当の独立照合](lead-review.json) · [一次取得ログ](sources.json) · [起動要求例](create-request.example.json) · [承認文案](approval-draft.md)
