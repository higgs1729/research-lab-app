Status: resolved
担当: 研究（R012インク推論独立検証、2026-11-13）
Blocked by: 133

# R012: 既知領域のCPUインク推論の入力・出力・集計を独立確認する（2026-11-13）

## 依頼

研究133で、取得済みw035公開画像128×128を固定の公式モデルへ一回だけ通した。既知訓練領域での工程確認であり、未知領域や文字判読の性能ではない。実装担当とは別に保存原票を調べ、入力の対応、固定checkpoint・公式ソースと環境、CPU実行、出力TIFFとラベル比較の数値を確認する。

対象は `research/133-r012-known-ink-inference.md` と `experiments/vesuvius/r012/20261113-known-ink-inference01/`。親がexperiment登録した後の元出力は凍結。入力は研究129の公開chunk全体で、元CT由来64×64の描画とは別物。公開XYZ/ラベルは研究127/130も参照できる。再取得・導入・モデルforward・推論の再実行は不要。保存ソースとログ、実データで確認する。

重要な判定は、(1) 公開のXY2176,1408から128×128、28層、選択層6〜22、監督域が元の保存ラベルと一致し推論前固定されていること、(2) checkpoint SHA、公式ソース固定版・必要な実行経路が保存物と合い、CPU1回というログと矛盾しないこと、(3) LZW uint8 TIFFの全画素から正6708/負4007/未監督5669とTP6678/FP415/FN30/TN3592、Dice/AUROC/APを独立再計算できること。作成担当の集計関数だけを呼ぶ確認にしない。同値の扱いとuint8量子化後128以上の閾値を保つ。

公式宣言のZarr2環境そのものではなく隔離Zarr3を使ったこと、単一patchの文脈・学習済み注釈であること、これは画像からインク候補を作る工程で文字転写ではないことを明記する。推論を再び走らせて同じ高い数値を確認する必要はない。原票の不一致があれば親へ返し、元資料は編集しない。

新規検証出力は `experiments/vesuvius/r012/20261113-known-ink-verification01/`。C:に保存、D:は読取だけ。有料計算・GPU・新規通信・ビルド・外部公開・追加subagentなし。一件逐次で、研究133の完了後に実行する。

今回のモデル/effortはgpt-6.1-sol / high。既存の独立ラベル復号・ハッシュ確認の手順があり、固定小出力の集計と主張範囲の確認を中心にするため。研究票に結論・コード・実行条件・未確認点を追記し、lab登録候補を親へ返す。

## 結論

[一次・独立検証] 研究133の保存原票は、w035の固定公開サーフェスを公式の固定インクモデルへローカルCPUで一回通し、対応する訓練用注釈と比較したという記録と一致した。LZW TIFFと元ラベルから、監督域10,715画素のAUROC 0.9976083893、AP 0.9985635439、保存値128以上のDice 0.9677559597を再計算した。対象は既知訓練領域の単一パッチ。画像からインク候補を出す工程が通ったことを示す。独立した文字転写、未知文字の発見、未知領域の汎化、元CT描画を入力にした推論は未評価。[独立結果](../experiments/vesuvius/r012/20261113-known-ink-verification01/result.json)

## 根拠・詳細

- [一次] **入力と注釈。** 保存原票の公開チャンクはL0 `0/0/11/17`、ZYX 28×128×128、無圧縮uint8、458,752 B。本文のMD5とETag、SHA-256を照合し、ローカル入力Zarr v2のデータと同一。原点は公開XY (2176,1408)、座標属性の9.362 µmスケールと移動量も一致する。左上64×64はR129の公開側と全値一致し、元CT由来の描画と画素値が異なる。20260918の元シャードをR130の独立CRC32C・Blosc復号で読み、同じ128×128の正6,708・負4,007・未監督5,669と、保存ラベル2配列を全数照合した。入力契約・ラベル・チャンクの保存更新時刻は17:26:13 JST、推論プロセス開始は17:31:56.837 JST。固定が先という判断は保存ファイル時刻と実行原票に基づく。[入力契約](../experiments/vesuvius/r012/20261113-known-ink-inference01/input-contract.json) · [公開チャンク取得原票](../experiments/vesuvius/r012/20261113-known-ct-control01/run01/http.jsonl)
- [一次] **固定モデルとソース。** 保存checkpointは138,360,039 B。HF `7109667e2607db1b90c37c8b09cb876ea7fe7bb1` のseed42 `step-075000.pth` で、公開LFS・HTTP原票・保存本文のSHA-256は `e635558ae6a1a807a7e5ec1e83adfd45bc3c0ac53883ea43f1d4e085d62a9cab`。ZIPメタデータを逆アセンブルして記録値を確認し、pickleを実行していない。保存ソース199ファイルはvillaの固定commit `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` のローカルGit blobと照合した。174ファイルはCRLFをLFに揃えるとGit blobに一致し、残り25は保存バイトのまま一致。R133の凍結マニフェスト649件は実ファイルのサイズとSHA-256が全て一致した。[checkpoint取得原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/checkpoint-http.jsonl) · [固定の公式CLI](https://github.com/ScrollPrize/villa/blob/47a9c37f6f8e99afdab47bb46ad425aa726f5dc0/ink-detection/koine_machines/inference/infer.py) · [ファイル照合](../experiments/vesuvius/r012/20261113-known-ink-verification01/result.json)
- [一次] **CPU実行と依存。** 保存CLIは層範囲を半開区間で取り、forwardで並べる。実行引数・ログ・無重み試験から28層のうち0始まりの6〜22、17×128×128、robust-MAD、単一パッチ・バッチ1、Hann、TTAなし、paddingなしを確認。ログにはモデル欠落／余分キー0、CPU、autocast・compile無効、占有スキャンL0へのfallback、選択パッチ1、確率TIFF出力1件があり、実行原票は終了0。無重み試験のforward実行フラグはfalse。壁時間4.406905秒、ピークRSS747,520,000 Bは元実行の記録。CPU版Torch 2.14.0+cpuと隔離パッケージZarr 3.1.5・numcodecs 0.16.5を使っており、固定ソース宣言はZarr 2.18.7・numcodecs 0.15.1。実データのZarr形式はv2。公式依存宣言と異なる組合せでの動作確認として扱う。[実行ログ](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01.stderr.log) · [実行原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01-process.json) · [依存宣言](../experiments/vesuvius/r012/20261113-known-ink-inference01/official-source/ink-detection/pyproject.toml)

### 保存TIFFからの独立集計

[一次] tifffileで単ページ・LZW・uint8・128×128を確認し、既存Pillowで全16,384画素を読んだ。保存値は53〜217。R133の集計関数は呼ばず、AUROCはソート済み負例への二分探索で厳密勝ち26,812,944組と同値3,456組を数え、同値は半分の重み。APは降順の同値を一群にして164群の再現率の増分で精度を加重した。正負の256値ヒストグラムも全数一致。二値化は監督域だけで保存uint8が128以上。公式コードは確率を[0,1]に制限し255を掛けてuint8に切り捨てるため、量子化前の0.5を二値閾値とする条件とは差がある。[独立集計コード](../experiments/vesuvius/r012/20261113-known-ink-verification01/verify.py) · [元の評価原票](../experiments/vesuvius/r012/20261113-known-ink-inference01/infer01/evaluation.json)

| 指標 | 独立再計算 |
|---|---:|
| TP / FP / FN / TN | 6,678 / 415 / 30 / 3,592 |
| Precision / Recall | 0.9414916114 / 0.9955277281 |
| Dice | 0.9677559597 |
| AUROC / AP | 0.9976083893 / 0.9985635439 |

既知インクの監督域に対する一致度であり、公開キャンバス全体を重なり付きで推論した場合には文脈が変わる。別の領域、checkpoint、閾値の探索は行っていない。

## 実行条件

2026-11-13 JST。Windows Python 3.14.6、既存NumPy、tifffile、Pillow、numcodecs、google-crc32c、ローカルGit objectを利用。検証本体0.526秒、追加通信0 B、有料計算0 USD。Git blobを最初に生バイトで比較したところCRLF差を検出し、改行変換だけを許して再確認した。元資料は読み取りのみ。モデルのロード、forward、推論の再実行、依存導入は実施していない。[検証コード](../experiments/vesuvius/r012/20261113-known-ink-verification01/verify.py) · [lab登録候補](../experiments/vesuvius/r012/20261113-known-ink-verification01/lab-record.json)

## メモ

- 公開チャンク、ラベルシャード、Git objectとcheckpoint、推論原票、TIFFを照合。研究133の主要数値に不一致なし。
