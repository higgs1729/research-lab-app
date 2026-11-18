Status: resolved
担当: 研究（r232_normalization_control、2026-11-15）

# 232: CPU/GPUの正規化を正しく照合し、Studioの既知字画対照を評価できるか（2026-11-15）

## 依頼
- 問い: R231で止まった正規化照合について実GPUの値を直接確認し、元入力の同一性と数値精度を保って、固定した既知PHerc0343対照の可視評価まで完了できるか。
- 背景: R229でCPU参照3件完成、R230で結果領域の物理予約、R231でA40/CA-MTL-1の起動・strict読込・失敗回収を確認。R231のモデルforwardは0。CPU除算とCUDA逆数乗算の差は全96パッチで最大5.960464477539063e-8と独立再現されたが、実GPU値は未取得。原因を確かめずに全行一致条件だけを外してはならない。
- 欲しい形: 実GPUの正規化原票、元u8入力/座標/形状/深さ順の厳密照合、デバイス演算差の説明と狭い修正、既存CPU参照との出力差1e-4以内の検証、固定96パッチ結果の回収と既知字画の評価。元原票を保持し、失敗直前の入力/段階も保存する。既存モデルのGPU前処理を保持できる契約を第一候補とし、CPU前処理へ移す場合は科学条件の変更として明記する。
- 資源: モデルも重みも不要な小さな正規化プローブを先に検討する。共有FIFOと他作業を止めない規則を維持。小プローブは実作業に合う資源申告を根拠付きで選べるが共有の余裕・MemGuardを下げない。大モデルのRAM/VRAM条件は既存のまま。Cの小出力は64MiB以内・入場2GiB・有料実行前12MiB物理予約、D書込なし。新重み/CT取得を増やさない。
- 有料実行: Runpodの判断権は主担当に委任済み。再度の本人確認は不要。既知対照一台を必要と判断したら、具体的な変更と見積/絶対削除期限/専用名/回収/別削除確認を実行前に主担当へ提示する。既存R231の運用USD0.35/30分/CA-MTL-1/A40枠を上限候補とし、自動再作成しない。推論/評価結果が出るまで新研究へ移らない。
- やらないこと: 元の登録証拠の上書き、精度閾値やraw同一性の緩和、既知対照を新文字や未知汎化と呼ぶこと、候補ROIの探索や追加条件掃引、他GPUプロセスの停止、新しい外部公開。
- 完了後: 同じ研究票へ結論と根拠を追記し、実験原票/manifest/record候補を残す。主担当が別実装で数値と原寸図を確認する。段階ごとに進行を通知し、失敗時も科学評価と環境障害を分ける。

## 結論

実GPUの正規化を確認し、固定PHerc0343の96パッチを完走した。CPUの直接除算とCUDAの逆数乗算で最大5.9604645×10⁻⁸の丸め差があり、全96パッチでCPUとGPUのSHAが異なった。元入力を厳密照合したうえでCUDA固有の期待SHAを使う形へ修正した。保存CPU参照3件の出力との差は最大9.23872×10⁻⁷で、許容1×10⁻⁴に収まった。

既知字画の右の囲い・曲がりと左の主明部を原寸で確認した。右輪の下に離れた明部はStudioの太い反応に続き、左の細い二本の終端は分離しなかった。主担当の別目視も同じ判定。既知字画の粗い再現までで、可読性の向上は確認できなかった。新文字0。

## 根拠・詳細

- [一次・2026-11-15 JST] A40のPyTorch 2.13.0+cu130で、作者と同じGPU FP32 `clamp_(0,200).div_(255)` をモデル・重みなしで実行した。u8全256種類の実測bitと固定96件のGPU SHAは、丸めた逆数を掛けるCUDA式に完全一致。パッチ0では262,144値中137,435値のbitがCPUと異なった。主担当がPython `struct` による独立lookupと別のパッチ切り出しで再確認した。[実GPU原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/cloud-run/extracted/normalization-probe.jsonl) · [主担当の独立照合](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/lead-normalization-cloud.json) · [PyTorch v2.13.0 CUDA原文](https://github.com/pytorch/pytorch/blob/v2.13.0/aten/src/ATen/native/cuda/BinaryDivTrueKernel.cu#L32-L49)
- [一次・同日] 固定u8ファイルとraw SHA・座標・形状・16層+8..−7順を維持。モデルなしの実GPUゲートを重み取得より先に通し、各forward直前にも実SHA、形状、座標、raw SHAを照合して96組の原票を記録した。CPU参照0/47/95、GPUの算術・crop・forward・Hannを維持。R231そのものの停止直前実GPU行は未保存なので、今回の観測をR231の原因説明を支持する証拠とした。[実行差分](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/r231-diff.patch) · [forward直前原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/cloud-run/extracted/gpu/pre-forward.jsonl) · [照合集計](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/normalization-summary.json)
- [一次・同日] 既知主域 `[1344,1088,672,448]` を128角入力・中央96・stride64、batch1 FP32/TF32 offで一回実行。GPU workerは27.280秒、固定CPU参照0/47/95との出力最大絶対差は順に1.93715×10⁻⁷、9.23872×10⁻⁷、6.25849×10⁻⁷。主担当の別実装で96パッチをfloat64 Hannで再合成し、301,056画素で保存probabilityとの差は最大2.30870×10⁻⁷だった。[GPU出力原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/cloud-run/extracted/gpu/result.json) · [主担当の再構成](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/lead-output-check.json)
- [一次・同日] 生階調のStudioは、R222のReader V3より右側の暗い中心が明瞭に見える一方、原図より囲いが太く閉じ、下側もつながった。左の主明部と横帯は対応した。固定median→p99.5表示でも右下成分と左終端の分離は確認できなかった。主担当の別実装でも原寸とAtlasの図の画素差0。[native原寸比較](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/review/comparison-native.png) · [Atlas 256角比較](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/review/comparison-atlas-256.png) · [担当の目視原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/visual-review.json) · [主担当の原寸と画素照合](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/lead-visual-review.json)
- [一次・同日] 手元FIFOは300.294秒で入場前終了。CA-MTL-1のSecure A40一台を実効USD0.59/hで使用し、作成前から186.014秒で起動、12 MiB物理予約で5,280,957 B・111ファイルを回収した。Pod `dwuiaamlk3334s` は11:01:44.670 UTCに削除・不在確認。主担当の別API照会でGET 404・専用名0・全Pod0。API createdAt基準297.648秒、時刻見積USD0.04901。専用明細は照会時点で未反映。再作成・追加CT・追加CPU forwardは0。[回収原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/cloud-run/capture.json) · [資源原票](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/resources.json) · [主担当の削除照会](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/lead-cloud-resource-check.json)

[実験報告](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/README.md) · [Manifest](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/manifest.json) · [登録候補](../experiments/vesuvius/discovery/20261115-studio-device-normalization01/record.json)

## 取得の経路

R229の固定入力とCPU参照をR231の転送・回収・期限管理で再利用した。同一A40のモデルなしプローブで全u8のCUDA正規化をビット照合してから、同じ台で固定推論に進んだ。保存パッチの再合成と原寸表示を別実装で読み戻した。

## メモ

2026-11-15 19:54 JST。固定入力の全96件でCPU正規化SHAとR231のCUDA予測SHAを小さなu8 lookupで再現。固定13部品を保持し、科学workerのcrop・CUDA FP32 clamp/div・forward・CPU参照を変えずに、実測CUDA SHAとCPU契約を別々に照合する形で凍結した。クラウドは同じ台でモデルなしの正規化プローブを重み取得より先に実行し、通過時だけ既知対照へ進む。手元の先行プローブは共有FIFOへ投入済みで、他作業の終了を待っている。クラウド作成は0件、計画・差分・オフライン検算を主担当へ送った。

2026-11-15 19:56 JST。手元は共有FIFOで300.294秒待ち、入場前に終了。自launcher消滅・自分の待札0、他作業停止0。主担当が凍結版を別照合し、一台を実行可能とした。Runpodの作成前基準10:56:45 UTC、専用Pod `dwuiaamlk3334s`、絶対削除期限11:26:45 UTC。独立watcherを起動して、Cの結果領域12,582,912 Bを実割当で確保した。

2026-11-15 20:05 JST。実GPUプローブと固定96パッチを回収し、削除・不在を担当と主担当で確認。正規化・三つのCPU参照・合成と原寸図の独立照合が通り、既知字画の粗い再現と細部未分離を記録した。専用明細は11:04:58 UTCの照会でも0行。専用Podの時刻見積と請求未反映を分けて残した。
