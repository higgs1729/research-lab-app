# R232 Studioの実GPU正規化とPHerc0343既知対照

Secure A40でモデルなしの正規化を実測し、全256種類のu8値のFP32ビットと固定96パッチのCUDA SHAが、丸めた逆数を掛ける算術と一致した。デバイスごとのSHAを照合する形に変更し、同じ台で96パッチの推論を完了した。保存CPU参照3件とGPUの最大絶対差は9.23872×10⁻⁷。既知字画の右側の囲い・曲がりと左側の主明部は再現された。右下の成分分離と左の細い終端は判別できなかった。新文字0。

## 正規化の実測と照合

- [一次・2026-11-15 JST] NVIDIA A40（SM 8.6）、PyTorch 2.13.0+cu130で、作者と同じ `float32 → clamp_(0,200) → div_(255)` をCUDA上で実行した。256種類のu8値を実際の入力形状に並べ、全FP32ビットを保存。直接除算のCPU参照と127種類でbit差があり、最大絶対差は5.960464477539063×10⁻⁸。PyTorchのCUDA実装はCPUスカラー除数の逆数を丸めて掛ける。全96パッチの実GPU SHAもこの式と完全一致し、パッチ0では137,435値にCPUとの差が出た。[正規化原票](cloud-run/extracted/normalization-probe.jsonl) · [パッチ0と全体の集計](normalization-summary.json) · [PyTorch v2.13.0 CUDA原文](https://github.com/pytorch/pytorch/blob/v2.13.0/aten/src/ATen/native/cuda/BinaryDivTrueKernel.cu#L32-L49)
- [一次・同日] 固定u8入力ファイル、パッチごとのraw SHAと座標、16層の+8..−7順、raw形状16×128×128とCUDA FP32形状1×1×16×128×128を照合した。モデルなしGPUプローブを重み取得より先に実行し、その期待・実測SHAに各forward直前の実SHAを完全一致させた。比較前の期待行と比較直前の実測行は96組を追記保存。CPT作者のcrop、CUDA正規化、モデルforward、出力のHann合成と既存CPU参照を維持。R231の例外直前におけるGPU側行は当時未保存で、今回の観測がその停止の説明を支持する。[固定計画](cloud-plan.json) · [R231からの差分](r231-diff.patch) · [オフライン検算](offline-check.json) · [forward直前原票](cloud-run/extracted/gpu/pre-forward.jsonl)

## 固定入力の出力

- [一次・同日] PHerc0343 main `[1344,1088,672,448]`、native 8.64 µm、128角入力・中央96・stride64、batch1・FP32/TF32 off。96 GPU forwardをモデルworker 27.280秒で完了。R229のCPUパッチ0/47/95との出力の最大絶対差は順に1.93715×10⁻⁷、9.23872×10⁻⁷、6.25849×10⁻⁷で、3件とも閾値1×10⁻⁴内だった。[worker原票](cloud-run/extracted/gpu/result.json) · [合成後スコア](cloud-run/extracted/gpu/probability.npy)
- [一次・同日、原寸目視] Studioの生階調で右側（箱9）の暗い中心を囲う太い明部と、左側（箱10）の主明部が受賞原図の同じ位置に出た。原図の右下に離れた明部はStudioでは輪に続き、左の二本の細い上向き終端も分離しない。固定のmedian→p99.5表示で暗い中心は見やすくなるが、字画の分離は確認できない。原寸比較は既知対照の部分再現に限る。[担当の原寸所見](visual-review.json) · [native比較](review/comparison-native.png) · [Atlas 256角比較](review/comparison-atlas-256.png) · [表示条件](comparison.json)
- [一次・同日、主担当の別検算] 全256ビット・96入力SHAを別のスカラーlookupで照合。全96パッチからfloat64 Hannで独立に再構成し、301,056画素の保存probabilityとの差は最大2.30870×10⁻⁷。native原寸とAtlas比較図を別の画素計算で再検算し、画像の階調差は0。主担当の別目視も粗い形状の再現と細部未分離を確認。[正規化の検算](lead-normalization-cloud.json) · [実出力の検算](lead-output-check.json) · [原寸と表示の検算](lead-visual-review.json)

## 資源と費用

手元は共有FIFOで300.294秒待ち、先行ジョブが空く前に自分の待機だけ終了した。実行したクラウドはCA-MTL-1・Secure A40一台、実効USD0.59/h、再作成0。作成前基準10:56:45 UTCからPID1確認まで186.014秒、入力転送54.549秒。重み893,443,724 BをPod内で一回取得しSHA照合した。追加CT取得・追加CPU forwardは0。結果archive 5,280,957 Bを12,582,912 Bの物理予約の同じファイルIDに保存し、SHA照合して111ファイルを展開した。[手元FIFO原票](local-probe-process.json) · [起動原票](cloud-run/launch-receipt.json) · [回収原票](cloud-run/capture.json) · [展開原票](extraction.json)

Pod `dwuiaamlk3334s` は絶対期限11:26:45 UTCより前の11:01:44.670 UTCに削除・不在確認。主担当の別API照会で個別GET 404、専用名0、全Pod0を確認した。API createdAtから不在まで297.648秒、計算と一時ディスクを含めた時刻見積はUSD0.04901。専用請求明細は11:04:58 UTCの追加照会で0行、実費は未確定。[削除](cloud-run/cleanup.json) · [主担当の照会](lead-cloud-resource-check.json) · [専用明細の追加照会](resource-billing-followup.json) · [資源集計](resources.json)
