# Hecate既知対照の外部GPU見積もり

Secure RTX 4090を1台、既知のPHerc0343を1回処理する案。2026-11-14 07:56:50 UTCのカタログでCUDA 13.0以上の4090は5拠点で在庫あり、$0.89/時。比較したA5000は$0.27/時、該当在庫なし。実行案は4090のみ。最大$0.90/時と当日在庫を起動前に再照合し、割当実単価も読み返す。[取得結果](catalog-snapshot.json) [Runpodの料金表](https://www.runpod.io/pricing) [Runpod REST v2](https://api.runpod.io/v2/openapi.json)

| 区分 | 予算時間 | 4090の計算費 $0.89/時 |
| --- | ---: | ---: |
| 割当・イメージ起動 | 240秒 | $0.05933 |
| 保存入力の送信・固定重みの取得とSHA照合 | 180秒 | $0.04450 |
| 環境確認・ロード・最大81パッチの推論 | 600秒 | $0.14833 |
| 証拠回収 | 120秒 | $0.02967 |
| 削除・確認 | 60秒 | $0.01483 |
| **計算合計** | **1,200秒** | **$0.29667** |
| コンテナディスク20GB、$0.10/GB/月、30日換算 | 1,200秒 | $0.00093 |
| **合計、税別** | **1,200秒** | **$0.29759** |

単価が$0.90/時の場合は同じ時間で$0.30093。RunpodのPod通信は出入りとも$0。持続ディスク・ネットワークボリューム・公開ポートは0。既存残高で実行できることを確認する。1時間相当のクレジットは起動条件で、使用料は秒課金。税はクレジット購入時に支払方法・請求先で変わる。残高不足、自動入金の発動見込み、円換算・税を含む追加決済がある場合は起動を保留する。[Pod料金](https://docs.runpod.io/pods/pricing) [税](https://docs.runpod.io/accounts-billing/sales-tax)

起動・推論秒数は予算配分。Runpod公式PyTorch 2.13.0/CUDA 13.0/Ubuntu 24.04を固定。OCI configのビルド履歴で `/usr/local/bin/python` がPython 3.12のシンボリックリンクで、そのPythonにcu130のTorchを導入していることを確認した。圧縮レイヤー9.72 GBで、キャッシュがなければ240秒で起動できない場合がある。既存共有ツールに記録された別用途Secure 57台の起動中央値は229秒、最大761秒。入力tarは約3.52 MB。公開された同一固定重み522,576,086 Bを180秒の転送枠内で取得する。重みだけでも約2.9 MB/sが必要で、入力送信が先に時間を使う。GPUでの実測時間は未取得。[公式テンプレート](https://www.runpod.io/blog/rebuilding-pytorch-templates) [Docker Hubタグ](https://hub.docker.com/v2/repositories/runpod/pytorch/tags/2.1.0-cu1300-torch2130-ubuntu2404) [固定OCI config](originals/docker-config.json)

## 承認後の一回

1. [固定資産](fixed-assets.json)とローカル確認を読み返し、Consoleの対象、残高、自動入金条件を確認する。起動時は固有名と作成前UTC、作成前に同名が存在しないことをローカルに保存する。1回だけPOSTし、応答が途切れたら同名と作成時刻で照合して削除へ進む。既知IDがある場合は一致も確認する。割当が希望構成から外れても、同じ所有判定で削除する。作成は再送しない。A5000への切替は含めない。
2. 公開ポートなし。Runpod REST v2の認証付きexecを使い、固定tarを小分けで送る。入場は240秒。時計・Pod ID・自己GETを照合し、起動時のPod内期限が読める場合だけ転送する。25秒のexec応答期限はプロセス停止を意味しないため、モデル子プロセスは別の実時間期限で制御する。管理APIのexecが当該ホストで利用できなければ終了する。
3. 33×320²の保存入力、atlas XYWH [1376,1056,320,320]、評価 [1408,1088,256,256]。逆24→9、16×64²、stride 32、fp32/batch 1で公式predict一回。strict loadと全patchの入力SHA、座標、support、確率、時間を保存する。最初の3patchでR190 CPUとの差が1件でもMAE > 1e-4または最大差 > 1e-3なら4番の手前で止める。残り78枚の所要見通しが枠を超える場合も同じ箇所で止める。パッチ用CPU affinity 1、Torch allocator 4 GiB、RSSと空き容量を監視する。LinuxのRSS閾値は事後観測で、Windows Jobのメモリ制限とは異なる。別実行、warm-up、新CTは0。
4. 終了・例外・時間超過で実験専用PodをDELETEし、同一IDがGETで404またはTERMINATED、一覧から消失を確認する。確認が取れない場合は専用名・時刻を照合して別ブラウザのConsoleから削除する。実験後に同一Pod IDの請求明細を読み、実額と請求時間を記録する。明細反映待ちは資源を保持する理由にしない。成功時は保存確率と元のsupport・HannからCPUで再集約し、PNGと照合する。固定座標の公開予測、R175対照と比較し、主担当の独立目視で字画を判定する。主担当の既存参照4面比較では、公開Hecateの明暗は保存対照2種と大枠で対応した。この256²は既知字画の一部を含む。[主担当の原寸比較](lead-public-reference.png)

端末側の処理終了だけではPodを解放しない。PodのstopはGPUを解放するが持続ディスクは残り得る。今回は期限時にPodを削除する。端末や担当セッションの断線に備え、コンテナPID 1が作成要求前に決めた絶対UTCまで待ち、Runpodが注入するPod専用キーで自身のIDだけを削除する。端末側の既存アカウントキーはPodへ送らない。自己GETはDELETE権限を証明しない。Podが起動しない、期限処理が動かない、APIが不通、PodキーにDELETE権限がない場合は課金が続き得る。旧CLIの期限フラグも有効な課金制限に使えない。**20分を削除目標とし、US$0.50を承認枠として求める。いずれも運用上の管理で、事業者による強制上限はない。** [Pod環境変数](https://docs.runpod.io/pods/templates/environment-variables) [Pod管理](https://docs.runpod.io/pods/manage-pods) [現行CLI仕様](https://github.com/runpod/runpod-plugins-official/blob/main/plugins/runpod/skills/runpodctl/SKILL.md)

## 実行ファイル

- `python -B run_once.py --local-check` はローカルの資産SHA・tarのみを確認する。
- `python -B run_once.py --approved-run --output <未作成のローカルディレクトリ>` は承認後にリポジトリのWindows端末から一回だけ使用する。別ブラウザでもConsoleを開き、ログの専用名を控える。
- `python -B run_once.py --recover --output <同じディレクトリ>` は既存の専用Podの照合と削除だけを試みる。未確認時はConsoleで照合を継続する。
- [起動要求例](create-request.example.json)は期限と名前が例示値。[pod_boot.py](pod_boot.py)が期限削除、[pod_work.py](pod_work.py)が取得と別プロセスの期限、[run_known.py](run_known.py)が固定推論を担当する。[固定資産](fixed-assets.json)の公開参照画像はローカル比較用。結果tarに重み・入力・資格情報を含めない。

今回は資料取得とローカル準備まで。Pod作成・既存資源変更・支出・新CT・GPU処理・モデルforwardは0。起動、管理APIのexec転送、Pod専用キーによるDELETE、GPU速度は実機未確認。
