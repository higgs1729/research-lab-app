# PHerc0846A固定入力でdense-native step16000を比較

[研究172](../../../../research/172-pherc0846a-dense-native-comparison.md)の2026-11-14 JST原票。R171と同じ元CT描画、XY各 `[843,1355)` の512×512、9.362 µmを使用した。固定seed42とdense-nativeでは、同じ保存層順の予測に広い応答の共通部分があった。dense-nativeの両方向で字画や行を一意に指せず、文字候補・転写なし。元CT上の割れと応答の関係、物理紙面の対応、インクの有無は未判定。[比較図](comparison.png) · [集計](comparison.json)

## 配布物とソース

- [一次] HF固定rev `b894a0493ab2291cc8dc3247020c0d7cb0967a58` のカードはMIT。APIと著者VERIFYは `weights/dense_native_016000.safetensors` を272,767,904 B、SHA-256 `d3d95dc41dcb24ed76b84b5e12ca5dae25d7fb34edf1dfbb93e0186f91e6fc6d` と記録し、取得本文も一致。原計画256 MiBを4,332,448 B超えたので本文取得前に停止し、主担当が固定1件だけ272 MiBへ変更した。本文の取得上限180秒、実測10.467秒、HTTP 200。[固定モデルカード](https://huggingface.co/Nieuwlaar/ink9um-dense-native/blob/b894a0493ab2291cc8dc3247020c0d7cb0967a58/README.md) · [保存API](hf-model.json) · [著者VERIFY](weights-verify.md) · [取得開始](weight-start.json) · [取得結果](weight-result.json)
- [一次] 著者はvilla `3ea17f54a9b3d5fd1aaf73e1d2c8386dbaa9f30e` の `koine_machines.inference.infer` と `--overlap 0.5 --blend-mode hann --direction forward --no-compile` を指定。既存R133/171で使った `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` との差は対象ソース木内で学習ラベル前処理の1ファイルのみ。著者の3行レシピで裸のtensorに固定configとstep番号を付け、ローカルPTHを1件保存した。既存safetensors 0.8.0、CPU Torch 2.14.0+cpu、隔離Zarr 3.1.5を使用。CPU builderの学習パラメータは34,546,498、state_dict列挙は508テンソル・68,175,426要素で、配布全キー・形状・F32型と一致。CLIロードは3回とも不足0・過剰0。[著者再現手順](author-reproduce.md) · [固定config](author-config.json) · [ソース照合](source-check.json) · [無forward確認](preflight.json) · [全tensor照合](weight-header-check.json) · [PTH](package-result.json)
- [一次・推論] 著者configとR133参照configでモデル型、stem、対象head、入力チャネル、パッチ形状、正規化が一致。実行は同じ3D stem＋2D U-Net、同じ推論コード、別学習checkpointの比較。著者はKLAVISのdense-ex016重みを起点とし、追加した10件のPHerc0139 native 113 keV面に同面の公開78 keV教師マップを使ったと報告。公表config 8群と保存リストにPHerc0846A / 20250728152254の記載は見つからなかった。初期化checkpointの全入力と座標単位の重複は未検証。w035は公表configに明示され、工程対照として使った。[モデルカード原文](card.md) · [著者再現手順](author-reproduce.md) · [教師原票](author-teacher-sources.tsv) · [整列入力原票](author-aligned-sources.tsv)

## 入力と実行

保存R135 w035元CTの128×128×28から層6→22で1パッチを最初に実行。全16,384画素が有限・正重み、uint8で54–218の165階調があり工程対照を通過した。次にR171の保存512×512×33で中央17層8→24と24→8を各一回、49パッチずつ実行。保存チャンクとZarrメタデータを事前にSHA照合し、R171と同じXY・層番号を維持した。[入力契約](input-contract.json) · [対照](control/gate.json) · [forward](forward/execution.json) · [reverse](reverse/execution.json)

前処理は公式CLIのパッチ内robust-MAD（1–99百分位）、128²・stride64・Hann、batch1、workers0、CPU float32 sigmoid、TTA/compileなし。各画素の加重和と重みを保存し、除算・clipしたfloatと、公式TIFF/PNGのuint8値を全画素で照合した。著者の複数窓用シェルにある別出力の変換式 `(a-64)/128`、veto、コントラスト補正は適用していない。この実行の固定公式writerは `floor(255×clip(p,0,1))` を用いる。[公式CLI](https://github.com/ScrollPrize/villa/blob/47a9c37f6f8e99afdab47bb46ad425aa726f5dc0/ink-detection/koine_machines/inference/infer.py) · [推論ラッパー](infer_dense.py) · [比較コード](compare.py)

| 入力 | パッチ | 実測秒 | ピークRSS B | uint8範囲 |
|---|---:|---:|---:|---:|
| w035対照 | 1 | 7.626 | 831,217,664 | 54–218 |
| PHerc0846A 8→24 | 49 | 18.729 | 847,839,232 | 87–199 |
| PHerc0846A 24→8 | 49 | 18.154 | 832,610,304 | 92–201 |

CPU affinity 1、数値threads 1、Windows Job commit上限4 GiB、推論ごと120秒。R133のPython外部ソケット拒否とHF offlineを再利用した。元CTや深さ窓の追加、依存導入、ビルド、GPU、課金、公開はいずれも0件。公開文書・APIの保存本文は11件、合計85,257 B。取得本文と変換PTHを含む作業は約530 MiBで、C空き条件10 GiBと作業上限768 MiB内。クラウド追加支出0円、ローカル電力費は未計上。[取得ログ](metadata-acquisition.log) · [各工程の開始・制限](control-start.json) · [対照計測](control-process.json) · [forward計測](forward-process.json) · [reverse計測](reverse-process.json)

## 予測の位置と目視

両checkpointの同方向上位3%は各7,865画素。各float画像で第7,865位以上を採り、閾値に同値が複数あれば含める定義。実際の閾値同値は各1画素。順方向で1,471画素が重なり（Jaccard 0.1032）、主に右上の1,241画素。逆方向で1,448画素が重なり（0.1014）、主に左下の1,434画素。重なりの大半を含む象限はキャンバスX/Yの1099を境にした256×256区画。同方向の全float画素のPearson相関は順0.345、逆0.605。この無ラベルの切り出しにおける応答位置の記述で、精度や上流カードの別領域の数値とは対応づけていない。[集計原票](comparison.json)

原寸・固定0–255表示ではdense-nativeの両方向に広がりのある雲状・連結した応答が見える。順方向右上と逆方向左下に両checkpointの強い部分があるが、独立した字画の連なりや文字行は一意に追えない。親担当も結論文を読む前に単独PNGを原寸目視し、候補なしと判定した。別学習重みの反応が同じ場所に出ることはインクの同定に足りず、CTの暗部を割れ・紙面・インクへ帰属する根拠も今回の出力からは得られなかった。[原寸比較図](comparison.png) · [順方向PNG](forward/probability.png) · [逆方向PNG](reverse/probability.png)

## 再現と計測失敗

親担当の保存データ独立照合では、HF本文とPTHのSHA・同一入力/CLI条件、対照16,384画素と対象524,288画素のfloat→TIFF/PNG、およびR171と同じ重み和を確認した。0.569秒、製品・モデルの再起動0回。[親照合](lead-check.json) · [親計測](lead-process.json)

`weight_fetch.py` は同じ重みを持たない新しい出力先でのみ使用する。保存済み本文を再利用する場合は `weight-result.json` の長さ/SHAを照合する。R133/R135/R171を同じ相対配置で参照し、`preflight.py` と `prepare_weight.py` は既存 `experiments/vesuvius/r005/20261112-ct-render01/run_windows.py` に渡す。保存される条件を確認してから `run_stage.py control`、`forward`、`reverse` を逐次実行。既存出力がある場合は推論を再起動せず、同じデータから `compare.py` で検証できる。

取得用の最初のPowerShell起動はツールポリシーで実行前に拒否され、保存スクリプトのcurl起動1件が実際の取得。初回比較図と1回目の修正では下段ラベル等がCTパネル末尾113画素へ重なり、画素照合が停止した。両失敗の図、コード、原票を保存し、下段の余白拡大と文字描画後のパネル貼り付けで5パネルの全1,310,720画素を照合した。比較図の修正に伴う推論再起動は0回。[比較初回ログ](compare01-compare.log) · [比較2回目ログ](compare02-compare.log) · [比較完了ログ](compare.log)
