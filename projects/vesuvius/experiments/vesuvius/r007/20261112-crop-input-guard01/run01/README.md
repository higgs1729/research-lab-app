# R116 ネイティブ試験結果

2026-11-13 JST。Ubuntu復元確認後、準備済みの [ハーネス](../run_trial.py) をそのまま `run01` として実行した。検証対象は現行rendererのblob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` に [crop-guard.patch](../crop-guard.patch) を適用した版。`baseline-observe` と `guard-observe` には [observation.patch](../observation.patch) を適用し、出力ディレクトリ作成を抑止してcrop選択時点で停止させた。

| 実面での指定 | 旧版 `(x, y, 幅, 高さ)` | 修正版 `(x, y, 幅, 高さ)` |
|---|---|---|
| 完全指定 | `(7356, 2272, 128, 128)` | 同じ |
| 全省略 | `(0, 0, 13600, 3440)` | 同じ |
| 全0 | `(0, 0, 13600, 3440)` | 同じ |
| 正の幅と高さ、原点省略 | `(0, 0, 128, 128)` | 同じ |
| 原点 `(-16, -8)`、幅と高さ128 | `(0, 0, 112, 120)` | 同じ |
| auto-crop | `(19, 19, 13561, 3401)` | 同じ |
| 完全指定から高さだけ削除 | `(0, 0, 13600, 3440)` | 早期拒否 |

旧版の高さ欠落は46,784,000画素／層を選び、完全指定は16,384画素／層を選んだ。修正版の高さ欠落は不存在のvolume・segmentationを使って別途確認した。8件の無効Zarr指定と1件の無効TIFF指定は、crop診断・終了コード1・画像出力なし。正常5件の不存在入力はvolumeエラーに到達した。help、既存のpart-idとsegmentationのエラー、空merge、2 partの実TIFF mergeも確認した。[選択原票](crop-selection.json) · [早期拒否ログ](cli-missing-height.log) · [mergeログ](merge.log)

修正版の通常CLIで、保存済みCTのPHerc0814の128×128を3層だけ実描画した。`00.tif`〜`02.tif` は既存stack対照 `049.tif`〜`051.tif` と全ファイルのSHA-256が一致し、既存Pillowでも復号後のuint8画素が一致した。merge出力 `00.tif` も中央対照 `050.tif` と同じSHA-256と復号画素だった。[TIFF原票](summary.json)

CPU0固定・AS 4 GiB、全コマンドはネットワーク分離。ビルド124.694秒、ビルド最大RSS 1,583,865,856 bytes。18 CLI試験の最大壁時間0.247秒、13観測の最大0.581秒、3層描画0.532秒・最大RSS 78,790,656 bytes。全40プロセスを回収し、期待した終了コードを照合した。追加のCT取得とクラウド支出は0。ローカル電力・モデル利用費は未算定。全面は観測時の選択寸法だけを示す。転送量、料金、描画時間の節減は計測していない。[ビルド原票](build-result.json) · [実描画プロセス](small-render-process.json)

## 独立検証の入口

1. [固定blobの照合](../../20261112-crop-preflight01/source-match.json)、[製品差分](../crop-guard.patch)、[観測差分](../observation.patch) を読む。製品版のguardがmerge分岐後、volume・store・segmentの読み込み前にあること、観測版が画像作成・サンプリング前にreturnすることを確認する。
2. `baseline-observe-missing-height.log` と `baseline-observe-complete.log` の `R116 selected` 行、正常6組の同じ行、`cli-missing-height-process.json` と `.log` を突き合わせる。必要なら保存バイナリ `baseline-observe` でのみ高さ欠落を再現し、観測ログを使う。保存作業先は `C:/dev/kensyoukin/.work/r007-crop-input-guard01/run01`。
3. 回帰試験を短く再実行する場合は、下のコマンドで保存済み `guard` を使う。`TMPDIR` はC:の既存作業先を指定する。実画像の確認は `summary.json` の出力と対照を別のTIFFデコーダで読み、3層を比較する。全工程を再実行する場合は [準備時の手順](../README.md) の実行名を未使用の名前にする。

```powershell
$r116 = '/mnt/c/dev/kensyoukin'
$r116Work = "$r116/.work/r007-crop-input-guard01/run01"
wsl -d Ubuntu -- taskset -c 0 prlimit --as=4294967296 -- unshare -Urn env "TMPDIR=$r116Work" python3 -B "$r116/experiments/vesuvius/r007/20261112-crop-input-guard01/check_cli.py" "$r116Work/guard"
```
