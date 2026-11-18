Status: resolved
担当: 研究（R133担当 2026-11-13）
Blocked by: 132

# R012: 既知領域を公式のインク推論まで低支出で通せるか（2026-11-13）

## 依頼

研究129/130で既知PHerc0139 w035の元CT描画と公開サーフェスを区別した基準入力ができ、研究131/132でその入力を使ったR009実停止・再開の深掘りを終えた。次は一連の工程確認をインク検出まで進められるかを一件調べる。本人の「既存三件の深掘り、文字解読を目標にする方針の相談」「リセットしました 再開」を受けた既存の低支出研究の範囲であり、未知文字発見やFirst Lettersへの大方針が本人決定済みとは扱わない。

既存能力を借りる有力候補は研究127で確保した公式 `scrollprize/ink_9um` のモデルと、model cardが指定するvillaの `koine_machines.inference.infer`。まず実コードの固定版、チェックポイントと前処理・層・画素サイズの契約、既存ローカルの依存とCPU実行経路を確かめる。独自モデル・学習器・別推論器を作ることは目的にしない。D:の保存repoや取得済み原文を再利用し、必要な公式の固定ソースだけ小さく取得してよい。

モデル候補は保存資料のHF commit `7109667e2607db1b90c37c8b09cb876ea7fe7bb1`、`hybrid_3d2d-seed42/step-075000.pth`（138,360,039 B、LFS SHA-256 e635558ae6a1a807a7e5ec1e83adfd45bc3c0ac53883ea43f1d4e085d62a9cab）。この一個を事前固定し、結果を見てcheckpointやseedを選び替えない。公式コードと整合しない場合は理由を返し、無断のモデル探索で埋めない。

入力は取得済み公開サーフェスL0チャンク `0/0/11/17` の28×128×128を使うことを第一候補とする。研究129の64×64はその左上四分の一であり、128×128の文脈は同じ保存チャンクにある。CT由来の64×64を、黙って拡大やゼロ埋めして同じ入力とみなさない。公開XY (2176,1408) からの128×128全体は既知の訓練用注釈に対応し、評価対象・監督域・前処理・層の選び方・境界を推論前に固定する。公式の必要文脈がこれを超えるなら、追加取得や便宜的paddingをする前に条件を親へ返す。

欲しい結果は、公式の固定モデルと処理を使ってこの既知領域から1回の推論を実行できるか、入力に対応した確率画像とラベル比較、時間・メモリ・追加転送量・再利用手順。注釈は訓練由来なので成績を汎化性能、独立な文字転写、未知文字の発見とは扱わない。任意の閾値や前処理を探索して成績を上げず、公式既定値か事前固定条件を使う。元CT描画との入力差の影響評価は今回へ広げない。

実行前に依存・入力契約・費用を短く親へ報告する。既存環境で成立すれば、公式ソース取得合計5MiBと上記モデル1個の取得・ローカルCPU推論1回へ進んでよい。ネットワーク元URL・応答・サイズ・ハッシュを保存する。新しい依存導入が要る場合は不足と最小の導入容量・時間を返し、親が選ぶ。モデルの取得前でもCPU経路がない、文脈/登録が不成立、資源が過大と分かったらそこで具体的な次案を返す。

GPU・クラウド・有料計算・学習・fine-tuningは実行しない。有料の必要性が出れば実験ごとの見積もりと本人承認が別途必要。ローカルCPU1、最初の推論300秒・実メモリ4GiBを目安とし、実行可能な制限方法を記録する。C:の新規作業容量1GiB以内を初期上限。D:は読み取りのみ。新しい原票は `experiments/vesuvius/r012/20261113-known-ink-inference01/`。公開repo・凍結資料の改変、外部連絡、応募、追加subagentをしない。研究132の完了後に逐次着手する。

モデル/effortはgpt-6.1-sol / xhigh。公式のモデルと既知入力を借りるが、この環境で初めて前処理・深さ・CPU推論を一つの経路へ合わせる必要があるため。依頼は凍結し、前提が不足した場合も原票と最小の次案を残す。成功主張の別担当検証は主担当が選ぶ。

## 結論

[一次・実行] PHerc0139 w035の既知128×128領域で、公式の固定モデルをローカルCPUで1回実行し、128×128のuint8確率TIFFを得た。固定checkpointを公式CLIでロードし、欠落キー・余分なキーはともに0。既存Windows CPU Torch 2.14.0と、隔離したZarr 3.1.5等を使った。計測壁時間4.407秒、最大RSS747,520,000 B。クラウド支出0円。[実行ログ](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01.stderr.log) · [確率TIFF](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/probability.tif)

[一次・実測] 事前固定の監督域10,715画素ではAUROC 0.997608、average precision 0.998564。保存値128以上でDice 0.967756。対象はモデルの訓練に使われたw035の一領域で、ラベル一致はこの工程の動作を示す。未知領域の汎化、独立転写、文字の判読は今回の測定範囲外。[数値](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/evaluation.json) · [公開面・出力・注釈の比較図](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/comparison.png)

## 根拠・詳細

### 公式処理と入力の固定

- [一次] HF model cardが指定するvilla `merge-ink-pipelines` のtipを照会し、`47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` の既存D: Git objectから `koine_machines.inference.infer` と構築・正規化の公式コードをC:へ抽出。実行ファイルを改変せずに呼んだ。現在の公式チュートリアルが示す後継の `vesuvius.ink_detection.inference.infer` とは入口が異なる。checkpointはHF commit `7109667e2607db1b90c37c8b09cb876ea7fe7bb1` の `hybrid_3d2d-seed42/step-075000.pth`。公開LFS SHA-256と取得本文が一致した。ZIPの `data.pkl` を実行せずに調べ、追加backboneの指定と外部URL文字列がないことを確認した。[公式モデルカード](https://huggingface.co/scrollprize/ink_9um/tree/7109667e2607db1b90c37c8b09cb876ea7fe7bb1) · [固定の公式CLI](https://github.com/ScrollPrize/villa/blob/47a9c37f6f8e99afdab47bb46ad425aa726f5dc0/ink-detection/koine_machines/inference/infer.py) · [checkpoint原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/checkpoint-http.jsonl)
- [一次] 研究129で取得した公開L0 `0/0/11/17` の28×128×128、458,752 Bを、そのままローカルZarr v2の1チャンクへ配置。公開座標はXY `(2176,1408)`、左上64×64は研究129の公開対照と全値一致した。20260918の保存ラベルと同じXYで、正6,708・負4,007・未監督5,669を推論前に固定。モデルへの入力は公開サーフェス。研究129の元CT由来の64×64との入力差は今回比較していない。[入力・評価範囲の固定](../experiments/vesuvius/r012/20261113-known-ink-inference01/input-contract.json)
- [一次・実行] 公式は17×128×128のpatchを使い、元28層から中心 `28//2−17//2=6` を起点に0始まりで層6〜22をforwardに渡す。ローダーは1パッチ、バッチ1、ワーカー0、Hann、overlap 0.5、TTAなし、入力paddingなし。公式robust-MADは1・99パーセンタイルでクリップし、中央値とMADで正規化する。無重み試験で全入力458,752値と正規化テンソルを照合し、公式builderをCPU上に構築、LZWの確率画像形式を読戻した。推論ではcheckpointの `model` を使用。低解像度の占有確認は公式fallbackでL0に対して行い、占有率100%で1パッチが選ばれた。公開キャンバス全体を重なり付きで推論する場合は、パッチ境界の文脈が変わる。[無重み確認](../experiments/vesuvius/r012/20261113-known-ink-inference01/smoke03/result.json) · [実行条件](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/execution.json)

### 依存・取得・費用

[一次] 既存CPython 3.14.6にCPU Torch 2.14.0+cpu、torchvision 0.29.0、timm 1.0.30、NumPy 2.5.2があった。公式CLIは最初にzarr未導入で停止し、公式宣言のNumCodecs 0.15.1にはWindows CPython 3.14のwheelがない。親の選択で、公式PyPIの `zarr 3.1.5`、`numcodecs 0.16.5`、`donfig 0.8.1.post1`、`imagecodecs 2026.3.6`、`pynrrd 1.1.3` の5輪をC:専用targetに展開し、既存 `google-crc32c 1.9.0` を再利用した。グローバル環境の該当パッケージは導入前後とも未検出。公式の宣言環境を厳密に再現した試験とは条件が異なる。この組み合わせで公式CLIのZarr v2・LZWの経路が動いた。[依存メタデータ](../experiments/vesuvius/r012/20261113-known-ink-inference01/dependency-metadata/choices.json) · [取得原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/wheel-http.jsonl) · [隔離target](../experiments/vesuvius/r012/20261113-known-ink-inference01/target-install.json)

2026-11-13 JST。新規転送はwheel 20,325,570 B、依存・索引メタデータ1,100,370 B、checkpoint 138,360,039 B。計159,785,979 B（152.38 MiB）。新規CT・公開画像・公式ソース本文のダウンロードは0 B。C:新規作業は約213 MB、隔離targetは49,950,545 B。CPU affinity 1、Torch intra/inter-op 1、Zarr concurrency 1、Windows Jobの4 GiB commit上限、300秒の親プロセス監視。HF offlineとPythonの外部ソケット監査を有効化し、Windows asyncio用の内部ループバックのみ通した。GPU・新規Torch・ソースビルド・学習・有料計算は行っていない。[計測原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01-process.json) · [再現手順](../experiments/vesuvius/r012/20261113-known-ink-inference01/README.md) · [lab登録候補](../experiments/vesuvius/r012/20261113-known-ink-inference01/record.json)

### ラベル比較

| 項目 | 事前固定の監督域 |
|---|---:|
| 保存確率値の全範囲 | 53〜217 / 255 |
| AUROC / average precision | 0.997608 / 0.998564 |
| 保存値128以上のTP / FP / FN / TN | 6,678 / 415 / 30 / 3,592 |
| Precision / recall / Dice | 0.941492 / 0.995528 / 0.967756 |

公式TIFFは `p×255` のuint8切り捨てなので、保存値128以上は量子化前の0.5と厳密に同じ閾値ではない。AUROCは同値を半分として扱い、APも同値を同じ順位にまとめた。未監督5,669画素は比較から外した。公開チュートリアルに載る画像はstep-020000であり、今回のstep-075000の出力値と照合していない。[集計方法と全ヒストグラム](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/evaluation.json) · [公式チュートリアル](https://scrollprize.org/tutorial5)

## メモ

- 研究132完了を確認。HF card指定branchをremote照合し、同一commit 47a9c37f6f8e99afdab47bb46ad425aa726f5dc0 のD:の既存Git objectから、C:へ原文を抽出した。公開0/0/11/17を128×128のZarr v2として固定し、研究129の左上64×64と一致を確認。監督域は正6708・負4007、未監督5669。
- 公式CLIのhelpが既存Windows CPU環境でzarr未導入により終了。公式宣言のZarr2/NumCodecs 0.15.1を既存CPython 3.14向けwheelだけで揃えられない。既存CPU torchと公式ソースを維持したZarr3パッケージの互換性検証案を親へ通知。重み未取得。
- 親が採用した5 wheelをハッシュ照合して専用targetへ展開。無重み試験1は外部通信防止のラッパーがWindows asyncioの内部socket pairを遮断したため停止。内部ループバックを許容後、試験2はラッパーが公式 `iter_blocks` へ必須引数を渡しておらず停止。呼び出しを修正して試験3が完走した。公式ソース・依存版・入力条件は試行間で固定。
- 無重み試験の成立後に指定checkpoint一つを取得し、公式CPU推論を一回だけ実行。保存TIFFの評価を実施し、独立確認を親へ引き継いだ。
