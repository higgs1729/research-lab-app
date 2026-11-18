# R009 ピラミッド無効時のOME参照修正

[製品差分](pyramid-metadata.patch)は、既存 `omeMultiscales` に渡す追加レベル数を `--pyramid` に合わせる。通常の単一part出力と `--pre` の両方から同じフラグを渡す。レベル生成や描画の計算は既存処理を使う。固定rendererに差分単独で適用でき、R007とR121の後に適用した場合も結合ソースが同一になる。[適用とビルド原票](run01/build-settings.json)

| 条件 | OMEのdatasets | 配列メタデータ | チャンク・画素 |
|---|---|---|---|
| R121保存出力、`--pyramid false` | L0〜L5 | L0 | L0は既存対照と一致 |
| 結合版、`--pyramid false` | L0 | L0 | L0は既存対照と一致 |
| 結合版、`--pre --num-parts 2 --pyramid false` | L0 | L0 | 仕様どおりチャンク未作成 |
| 結合版、既定の通常出力 | L0〜L5 | L0〜L5 | R120/R115の14ファイル・全レベル画素と一致 |
| 結合版、既定の初回 `--resume` | L0〜L5 | L0〜L5 | 同じ対照14ファイル・全レベル画素と一致 |

無効時の出力は通常4ファイル、`--pre` 3ファイル。通常と `--pre` のroot属性は、既定出力からdatasetsのL1〜L5を除いた内容と一致した。L0の `.zarray` は全条件で同一。R007のデータ不要CLI回帰18件も通過した。R121の保存出力、固定CT、R120/R115対照、借りた `pyramid.o`、元ソースを再照合した。[修正前の参照](run01/old-pyramid-disabled.json) · [試験結果](run01/result.json)

## 再現と独立確認

Ubuntu WSLの既存環境を使い、保存済みR121の `pyramid.o`・変更ヘッダー、R120/R115の対照と固定CT、R007の差分・CLI回帰を参照する。空いている実行名で起動する。`run01` は実行済み。

```powershell
wsl -d Ubuntu -- python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-pyramid-metadata01/run_trial.py run02
```

1. 既存の3差分を固定ソースに適用し、独立したメタデータ差分を最初に適用した場合と最終ソースが一致することを確認する。R121の `pyramid.o` のSHA-256と変更ヘッダーを照合し、rendererだけをコンパイルする。依存ファイルとELFのピラミッドシンボルも確認する。
2. 保存済み出力を読むだけで確認する場合は、`old-pyramid-disabled.json` と `result.json` のrootを開き、実際の `.zattrs` のdatasetsと `0/.zarray`〜`5/.zarray` の存在を照合する。`disabled-pre.zarr` は配列のメタデータまでを比較する。
3. `normal.zarr` と `fresh-resume.zarr` はR120 `normal-manifest.json` とファイル別SHAを比較する。`disabled-normal.zarr` はL0のBloscチャンクを復号し、同じ対照のL0と比較する。crop回帰は `crop-*-process.json` とログを参照する。

実行ログとJSONは `runNN/`、バイナリ・依存ファイル・Zarr出力は `C:/dev/kensyoukin/.work/r009-pyramid-metadata01/runNN` に保存する。ビルドは113.286秒・最大RSS 1,585,221,632 bytes、ネイティブ試験は110.074秒・最大RSS 96,710,656 bytes、C:作業量22,710,582 bytes。CPU 0固定、AS 4 GiB、core dump 0、ネットワーク分離。試験22件すべてを回収し、停止票は発生しなかった。追加CT取得・クラウド支出はゼロ。ローカル電力とモデル利用費は未算定。Pythonバインディングの実ビルドは本試験の対象外。[ビルド結果](run01/build-result.json) · [試験条件](run01/environment.json)
