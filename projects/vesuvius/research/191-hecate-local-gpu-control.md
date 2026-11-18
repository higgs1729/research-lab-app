Status: resolved
担当: 研究（R191担当、2026-11-14 JST）
Blocked by: 190

# 保存済みHecateと既存の手元GPU環境で既知対照を完走できるか（2026-11-14）

## 依頼

190はCPU1で3/81パッチを正常計算したが、残78が約60分となり900秒枠では停止した。重み・入力・最初の3確率・公式コードが保存済みで、GPU計算は未実施。今回は既存の手元CUDA環境を読み取りで確認し、可能なら同一の既知PHerc0343入力を一回のGPU処理で完走して字画比較を行う。CPU時間枠を延ばすだけの再試行はしない。追加クラウド支出0、クラウド自動振分けも使用しない。

親が確認した既存候補は C:/dev/ai-compute/local-image-gen/ComfyUI_windows_portable/python_embeded/python.exe（ファイル存在のみ）。C:/agents/tools/gpu.py の exclusive は手元GPU用の排他・入場・資源監視で、run はクラウド経路もあり使わない。共有Python/依存/ComfyUI設定は変更せず、既存環境に必要なTorch・NumPy等がなければ現状と不足を報告する。Py3.14専用の隔離Zarr等を別版Pythonへ混入させない。Hecateは190の保存npyを読むため新たなZarr利用は不要。

研究191の保存先 experiments/vesuvius/discovery/20261114-hecate-gpu-control01/。190/189/175は読み取り専用。新規の入力・重み・依存・CT取得は0、ディスク追加は32MiB以内。GPU型/ドライバ/実Torch・CUDA/NumPy/Python、既存コード・重み・npyのSHAを先に確定する。環境確認にはモデルforwardを使わない。

入力とモデルは190の固定条件をそのまま使う。33×320×320 uint8、atlas XYWH [1376,1056,320,320]、主比較 [1408,1088,256,256]、reverse24→9、16×64×64、stride32、81全パッチ、batch1、float32、uint8/255、Hann floor.001、round(255p)、逆順2Dのみ。保存ソース c232c18a1a86cfb91257a00db13288202bb8ae33732ba26f7291a9b8adb8da59 と重み809f4f10f7cb7afa19b4bee0f7d2ab31edd7e11b664f9f210cc9c17f22fcfe5dを変更せず公式predictを使う。CUDAでTF32を無効にしてCPU fp32との比較条件を残す。Hecate3D出力・新方向・新領域・bf16・パラメータ探索は含まない。

既存のGPU排他にメモリ4GiB・VRAM4GiBを申告し、余裕RAM4GiB/VRAM1GiBを維持する。CPU1/数値1thread、process commit4GiB、C空き10GiB以上。GPU待ちと実行を区別して記録し、入場を120秒を超えて待つ見通しなら今回は実行しない。ローカルモデル処理上限600秒、起動・解放を含む外側上限780秒。停止が必要ならこの研究が起動したプロセスだけを対象とし、他の作業や共有環境を変更しない。初めの3パッチも本番81の一部として保存し、残78の時間超過見込みで止める。

最初の3GPUパッチを190のCPU確率と同座標で比較し、各patchでMAE<=1e-4かつ最大差<=1e-3（0..1確率）を計算上の整合確認として使用する。この閾値は文字認識の正解率ではない。超過なら全体推論へ進まず条件差を記録する。同一パッチの再実行で救済しない。以降は全81の入力hash・位置・集約前確率・同期したCUDA計時を残す。CPU3件との重複はデバイス/実行環境の整合検証のためであり、CPU途中結果をGPU出力へ混ぜない。

主要な入口・環境・入場条件が揃った段階で親へ通知して別確認を受ける。親は新たなmodel forwardをせず、事前に固定済みの190/lead-input-expected.json、CPU3出力、GPU捕捉確率と最終全画素を独立集約・照合する。完走した場合のみ、公開Hecate同面と175 seed42/denseの共通256²を原寸・同0–255で並べ、親と担当で既知箱9/10部分の弧・輪・暗部の位置、融合/散乱を見る。公開予測との相関は再現性であり判読精度ではない。既知文字の新発見や訓練非重複は主張しない。

結果をこの票へ追記し、実測資源・取得0の根拠・入力/コード/出力・親別検証を保存、README/manifest/lab候補まで。lab登録は親。サブ委任なし。今回は gpt-6.1-sol / xhigh を選ぶ。初回の既存CUDA環境利用と排他・精度契約を接続し、CPUで得た根拠を捨てず一回のGPU既知対照へ進める課題のため。

## 結論

2026-11-14 JST。既存ComfyUI埋込Python 3.13.14のTorch 2.13.0+cu130はRTX 4060 Tiを認識した。固定入力・ソース・重み・公開参照・CPU3確率のSHAは一致。入場直前のRAM空きは10.7 GiB、VRAM使用2.55/8.0 GiB。手元GPU排他に一度並び、先行ジョブが続いたため、120.034秒で本研究の待ちを終了した。主担当は本研究のPID・待ち札が消え、既存ジョブと別の待ち札が残ったことを独立確認した。[環境原票](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/preflight.json) · [入場・停止](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/supervisor-result.json) · [主担当の解放確認](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/lead-release.json)

GPUモデルの子起動、重みロード、forwardは0。CUDA認識まで成立し、実モデルの完走・CPU3確率との一致・既知字画は未判定。新規取得・依存導入・共有環境変更・クラウド費0。固定の実行入口と照合を保存した。[実験報告](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/README.md) · [主担当の検証](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/lead-verified.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-hecate-gpu-control01/record.json)

## メモ

- 入場の事前照合には実機のCUDA認識だけを使った。埋込Pythonのscript親を明示し、既存排他と時間制限を一回だけ起動。再並びはしていない。
