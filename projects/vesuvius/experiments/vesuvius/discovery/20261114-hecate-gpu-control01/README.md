# 手元GPUの既知Hecate対照

2026-11-14 JST。既存CUDA環境はRTX 4060 Tiを認識した。GPU排他に一度並んだが、先行ジョブが続き、**120.034秒で入場待ちを終了した**。HecateのGPU子プロセスは起動せず、重みロード・forwardは0。既知字画、全81パッチの出力とCPU3パッチとの一致は未判定。[入場記録](entry-status.json) · [監視結果](supervisor-result.json)

## 根拠と再利用条件

- 既存ComfyUI埋込Python 3.13.14、Torch 2.13.0+cu130、CUDA 13.0、NumPy 2.5.2、ドライバ610.88。RTX 4060 Ti（compute capability 8.9、CUDA総量8,585,216,000 B）を確認した。環境確認はCUDA APIの認識までで、モデルforwardは使っていない。190のCPUは別のPython/Torch版。保存ソース、checkpoint、npy、公開参照、CPU3出力のSHAは一致した。[環境と資産](preflight.json) · [主担当の静的照合](lead-preflight.json)
- 15:57:36 JSTの入場直前はRAM空き10.7 GiB、VRAM使用2.55/8.0 GiB、実行一件・先待ち一件。FIFOで本研究を並べ、15:59:36.699 JSTに本研究のlauncherだけを終了した。本研究の待ち札とPIDは消え、先行ジョブと別の待ち札は残った。主担当も固定コード、未起動、終了と解放を別に確認した。[キューログ](exclusive.log) · [終了後の状態](post-admission-check.json) · [主担当の終了確認](lead-verified.json) · [主担当の解放確認](lead-release.json)
- `python -X utf8 -B supervise.py` は固定の `gpu.py exclusive` を呼ぶ。待ち120秒、子処理600秒、外側780秒、申告RAM/VRAM各4 GiB。子はJobの4 GiB制限、CPU1、CUDAのIEEE fp32・TF32無効を照合し、公式predictのreverse 24→9・64²/stride32・81パッチを使用する。3パッチのCPU整合（MAE ≤1e−4、最大差 ≤1e−3）と残り時間の判定は4番の前。この実行では入場前に止まったので、子側制限とCPU差の動作確認は未実施。[実行入口](supervise.py) · [子処理](run_gpu.py)
- 新しいCT、モデル、画像、依存の取得0 B。依存追加・共有環境変更・クラウド支出0。GPUモデル計算時間0。比較図は得られていない。

