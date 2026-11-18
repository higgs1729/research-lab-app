# R231 Studio既知対照のCA-MTL-1実行

Secure A40はCA-MTL-1で、作成前の基準時刻から200.888秒で起動した。固定入力の転送、重みの照合とモデル読み込みが成立し、最初のパッチの入力照合で停止した。GPU forwardは0。実行ログを12 MiBの物理予約から回収した。96パッチの結果と既知字画の評価は成立していない。新文字0。

## 実行と停止箇所

- [一次、2026-11-15 JST] R229のplan `d1a9774b…`、入力archive `499e33cc…` と全17メンバを照合した。CPU参照0/47/95、PHerc0343 main `[1344,1088,672,448]`、入力16層、128角入力・中央96・stride64、clip200/div255、sigmoid後Hann、FP32/batch1/TF32offを再利用した。追加のCPU forwardは0。[計画](cloud-plan.json) · [R230との差分](r230-diff.patch) · [配置・期限の検算](offline-placement-deadlines.json)
- [一次、同日] CA-MTL-1の在庫はLOW、Secure A40の表示と実効料金はUSD0.59/h、自動入金は無効。10:26:30 UTCを作成前の基準とし、10:36:30を起動期限、10:56:30を絶対期限とした。実際に作成した1台のイメージは10:28:46に展開中で、10:29:41に固定digestのpull完了、10:29:42にcontainer start、10:29:50.888にPID1 markerとself-GET 200を確認した。[直前照会](cloud-admission.json) · [展開ログ](startup-progress-probe/startup.jsonl) · [起動ログ](cloud-run/startup.jsonl)
- [一次、同日] 入力6,980,298 BのuploadとSHA照合がreadyから48.624秒で完了した。重み893,443,724 BはPodで一回取得して固定SHAと照合した。取得計測は3.722秒。GPU上で223,355,921パラメータを読み込み、状態テンソルを照合した。次に `studio_worker.py:104` の `row == contract['positions'][i]` で `AssertionError`。job終了コード1、保存されたpatch 0、GPU forward 0。回収したgpu/result.jsonは初期の `status: running` を記録しており、終了判定はjob-result.jsonとmodel.logによる。[実行原票](cloud-run/launch-receipt.json) · [取得結果](cloud-run/extracted/transfer.json) · [モデル情報](cloud-run/extracted/gpu/model.json) · [例外原票](cloud-run/extracted/model.log) · [終了原票](cloud-run/extracted/job-result.json)

## 正規化の切り分け

[一次、同日] 保存入力の全96パッチでraw SHAが一致し、FP32直接除算で全96件のCPU契約の正規化SHAを再現した。実行Podと同じPyTorch v2.13.0のCUDAソースでは、CPUスカラーを除数とする浮動小数点除算で、float32に丸めた逆数を掛ける。入力の同じ値へこの演算を適用すると全96パッチでSHAが変わった。パッチ0では262,144値のうち137,435値が変化し、最大絶対差は5.9604645e-8だった。[再計算と全96件の結果](pre-forward-normalization.json) · [照合コード](pre_forward_normalization.py) · [PyTorch v2.13.0 CUDAカーネル](https://github.com/pytorch/pytorch/blob/v2.13.0/aten/src/ATen/native/cuda/BinaryDivTrueKernel.cu#L32-L49)

[推論、同日] 正規化の演算経路で生じるbit差は、パッチ0での入力契約停止を説明する。例外前のGPU側rowと実SHAは保存されていない。R231内の追加GPU実行は0。

## 回収、削除、費用

作成前にWindowsの実割当12,582,912 Bと独立watcherのreadyを確認した。予約後のC空きは10,129,301,504 B。失敗時のarchive 3,841 Bを同じfile IDに書き、Pod提示・書込後の読戻し・展開前のSHAが一致した。archiveにjob-result、worker/model log、転送・依存・GPUモデル・開始・結果の8ファイルを保存した。Pod `54g607o5gbhsk1` は10:30:58.628 UTCに削除・不在確認。主担当の別API照会でもGET 404、専用名0、全Pod0。独立watcherは終了した。[予約・archive照合](cloud-run/capture.json) · [展開原票](extraction.json) · [削除原票](cloud-run/cleanup.json) · [主担当の照会](lead-cloud-resource-check.json)

APIのcreatedAtから不在確認までは267.454秒、20 GBの一時diskを含む時刻ベースの見積もりはUSD0.04404。専用請求照会は10:31と10:34 UTCの両方でHTTP 200・0行。実費は明細待ち。[資源・費用原票](resources.json) · [主担当の専用請求照会](lead-cloud-resource-check.json)
