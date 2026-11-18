# PHerc0211 winner model: source/CPU control complete; GPU result not recovered

2026-11-15 JST、R229。今回の成果は固定ソース、入力契約、重み検証とCPU参照3件まで。既知字画の全主域再現、CPU–GPU一致、モデル間の可読性、GPU実forward数は未判定。**新文字0。** 主担当の指示により、この原票で本研究を閉じる。追加のモデル実行や別研究の起票はしていない。

## 確認できたもの

- [一次] 公式受賞発表HTML、Git `235e3be8a06749344862c89a1e52c81d90b15e0e`、release API、著者の学習記録、HFデータカード/Reader manifestを固定した。重みの公開は10月28日、本日は受賞発表。[source-study.md](source-study.md)
- [一次] 重み893,443,724 B、SHA `96b326286e38de99047f7cab36170c53749a18d5f43e5fde0c7c20f2980b0e90`、214テンソル、223,355,921パラメータを完全取得・SHA・strict loadで照合。seed42/dense-native/Reader V3やHecateとは異なるモデル/入力契約。性能優位を示す結果ではない。
- [一次] R222の同じPHerc0343既知主域 `[1344,1088,672,448]`、native8.64 µm、16層+8..−7、input128/core96/stride64/Hann、clip200/255を固定。入力bbox `[1264,1008,832,576]` は全て保存CT内。主担当は全7,667,712入力値、全面位相96coreと主域301,056画素の支持を独立照合した。[plan.json](plan.json)、[lead-plan-check.json](lead-plan-check.json)
- [一次] CPUは固定0/47/95の3パッチを一回ずつ、PyTorch2.14+cpu、FP32、CPU1/commit4 GiB、strict load一回で完了。監督73.801秒、最大RSS2,007,961,600 B、最低空きRAM6,969,958,400 B。参照確率は `cpu/p000.npy`, `p047.npy`, `p095.npy`。[patch-contract.json](patch-contract.json)、[cpu-process.json](cpu-process.json)

## 実行と未回収

1. 手元4060 TiはCPU参照後にFIFOを一度だけ試したが、8 GiB空きRAMの入場条件に届かず120.084秒で終了。手元GPU forward0、自launcher/待札解放済み。他用途cw11-stage等は停止していない。
2. A5000案は親の確認後の直前APIで在庫NONEとなりcreate前終了。A40への具体変更を親が許可し、科学15ファイル・lifecycle3ファイルの同一SHAを保ってGPU名とrate上限だけを変更した。
3. Secure A40 `fz22fx79xv6493`、専用名 `r229-studio-c12b34d2daf1796c` を一台作成。APIのcreatedAtは09:26:53.172 UTC、rate US$0.59/h。絶対削除期限09:56:52 UTC、startup240秒・モデル最大900秒。09:28:52.062にwatchdog markerが通過した。
4. 入力/workerを起動後、controllerは `collect()` へ進み、remote archiveをメモリ内へ読み切りSHAを照合した。**ローカル保存直前のC空き10 GiBチェックでAssertionErrorとなった。** `results.tar` はローカルに保存されず、job-result/worker log/画像/確率配列は未回収。GPU forwardは**最大計画96、実数不明**。失敗後のC空き観測10,565,263,360 Bは、失敗瞬間の値やarchive長ではない。[stderr原票](cloud-controller-stderr.txt)、[喪失記録](cloud-collection-failure.json)
5. outer finallyが09:30:03.778866 UTCに削除を確認。独立local watcher PID54716も終了。親が09:30:25にGET404・専用名0・全Pod0を別確認した。収集失敗時にも削除方針を維持し、再作成・モデルretryはしなかった。[cleanup](cloud-run-a40/cleanup.json)、[親の別照会](lead-cloud-resource-check-a40.json)

作成基準09:26:52からcleanupは191.779秒、実createdAtからは190.607秒。実createdAt基準の単価×時間は約US$0.03124、旧見積式の20GB一時disk分約US$0.000147を含めた**時刻見積約US$0.03139**。親のprecreate起点の時刻見積は約US$0.03158で、起点の違いとして区別する。Pod別明細は未反映で実費はnull。残高差や空のbilling totalsを「無料」とは扱わない。[resources.json](resources.json)

親はtracebackとcollectorの「全取得→SHA照合→空き条件→保存」の順序を独立確認した。ディスク満杯ではなく、約9.8 GiBの空きがあっても10 GiB条件で成果を保存しない回収設計が失敗した。空き容量低下の消費元は未特定。[親の失敗検証](lead-failure-review.json)

## 保存物と限界

- cache-release.jsonのとおり、未登録の公開重みキャッシュ一ファイルのみを親の許可で解放した。取得原票・header・CPU参照・閉じたlocal計画は残した。Podは同じ公開URLを一回直接fetchする設計であり、重みを入力tarへ含めない。
- `cloud-input-a40.tar.gz` は正確な入力・CPU参照・固定モデルコード・小依存wheel・workerを含む。推論値は変えていない。cloud版は同じ `studio_worker.gpu/patch/forward` をLinux path/runtime adapterで呼ぶ。[cloud-a40-amendment-check.json](cloud-a40-amendment-check.json)
- `lead_output_check.py` は親が用意した**未実行**の検算器。GPU数値検算済みとは数えない。最終原寸図・GPU score・visual verdictは存在しない。CPU参照3件だけから主域の字画再現を主張しない。
- 学習にはReader由来のPHerc0343Pがあり、今回のPHerc0343とscan keyは違うが、物理part関係/全ラベル座標重複は未検証。0211は訓練除外と作者は記すが、評価/モデル選択とラベル作成時のStudio系露出はある。既知対照も汎化性能評価とは呼ばない。
- stdout/stderrファイルは今回のtool console出力を分離して保存した転記で、元の行内容を保持（改行はLF）。API/runtime原票とは区別する。

[manifest.json](manifest.json) は現存ファイル、[record.json](record.json) は主担当が登録する候補。lab/recall登録、公開、応募送信は行っていない。
