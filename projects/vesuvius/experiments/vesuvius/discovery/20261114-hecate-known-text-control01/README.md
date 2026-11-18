# PHerc0343既知面のHecate 9.6 µm試験

2026-11-14 JST。**CPU1の900秒枠では完走が見込めず、3/81パッチで停止した。** 公式checkpointのstrict loadと、固定既知CTを使う最初の3回のforwardは成立した。評価域全体の出力が無いため、既知字画の維持と固定atlasへの再現性は未判定。未完の集約を原寸予測として表示していない。[計時判断](first-three.json) · [実行結果](execution-result.json) · [外部監視](supervisor-result.json)

## 固定条件と結果

- R175の33×384² uint8から全層320²を切り出した。atlas XYWH [1376,1056,320,320]、主比較 [1408,1088,256,256]、raw SHA-256 `81085d69df18eea1da683e23396fe120aabf90ad7877d9bd43d17aa5e98b12d9`。親が9登録チャンクから別に切り出した期待値と一致した。モデル入力は深さ24→9、64²/stride32、uint8/255、CPU fp32 batch1。XY間隔9.600000254 µm、Z9.599039497 µm。[実入力契約](input-contract.json) · [親の起動前照合](lead-preflight.json) · [公式固定コード](../20261114-alternative-ink-model-selection01/originals/hecate.py)
- Hecateの固定重み522,576,086 Bと同面のatlas reverse 2,114,372 Bを一件ずつ取得し、長さ・SHAを照合。本文合計524,690,458 B、取得工程32.496秒。新規CT・依存・GPU・ビルド・追加クラウド支出0。準備初回は共有CRC32Cのパス未設定で終了し、R133と同じパス設定で準備のみ再実行した。[取得原票](acquisition.json) · [初回準備原票](prepare-process.json) · [準備結果](prepare02-process.json)
- strict load 16.920秒、130,413,270パラメータ。forward 49.236 / 44.817 / 46.188秒。パッチ境界で測った後二つの間隔の大きい方46.232秒から、残り78の予測は3,606.064秒。残枠715.990秒で4番のforward前に停止した。監視186.832秒、実行入口184.106秒、peak RSS 1,283,719,168 B。CPU affinity 1、Windows Jobのprocess commit上限4 GiB、数値1thread、実行準備時の物理空き8,780,054,528 B、C空き30,994,837,504 B。壁時間900秒による強制終了には達していない。[ロード](load.json) · [実測パッチ](patches.jsonl) · [実行資源](infer-process.json)
- 捕捉は作者コードを変更せず、hookでraw/正規化入力のSHA、位置と、マスク・Hann前のfloat32 sigmoidを保存した。3パッチのatlas開始は (1376,1056)、(1408,1056)、(1440,1056)。主比較で触れたのは上側32行の一部で、全面81パッチの支持は揃わない。Windowsの中断時に残った公式memmapは分子が完了3件、分母が4件目の加算後。最終PNG・同座標比較図・認識指標は作成していない。[捕捉コード](run_hecate.py) · [資源監視](supervise.py)
- 主担当はforward前に固定した独立入力のSHAに3件すべてが一致し、保存確率3×4,096値が有限でファイルのraw hashと一致すること、起動コードが固定版と一致し、終了が規定の見積停止であることを別に確認した。[主担当の別検算](lead-verified.json)

## 実行入口

`acquire.py` は189の固定URLを二件だけ取得。準備は `python -B ../../../../tools/research/run_windows.py prepare02-process.json run_hecate.py prepare`、単回起動は `python -B supervise.py`。既存成果物は読み取り専用。保存済みの計算を再実行せずに検証できるよう、位置・入力hash・予測確率・途中集約を保持した。今のCPU枠で同条件を救済再実行する根拠は得られなかった。

