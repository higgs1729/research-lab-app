# R116 crop引数検証の実装候補

現行renderer blob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` をC:へコピーした。`crop-guard.patch` は引数4値が全て0か、幅と高さがともに正かを通常renderの入力を開く前に検査する。`--help` と `--merge-tiff-parts` の分岐を先に通す。auto-cropとmanual指定の排他条件、cropとcanvasの交差計算は既存の位置にある。

`observation.patch` は別の観測ビルド向け。出力ディレクトリの準備を省き、実面のcrop選択を記録した時点でreturnする。元ソースと修正後ソースの両方に適用できる。製品候補の `crop-guard.patch` に観測用コードは含まれない。元ソースからの生成済み3版は `.work/r007-crop-input-guard01/sources` に保存した。

## 検証状況

元ソースのSHA-256とGit blobを照合し、3版を生成した。Windowsの `git apply --check` で製品差分と元版・修正版に対する観測差分の適用を確認した。Python 3で3スクリプトを構文検査し、`check_cli.py --help` が起動した。WSLで `Ubuntu` が `WSL_E_DISTRO_NOT_FOUND` を返したため、元rendererのhelp、3版のビルド、実面crop選択、変更後の早期拒否、既存動作とTIFFの比較は未実行。WSLの登録、修復、依存導入は行っていない。[環境原票](environment-stop.json)

## Ubuntuと既存依存が利用可能になったら

保存済みソースを使い、PowerShellから次を実行する。ビルドは1 CPU・AS 4 GiB・合計300秒、各CLI試験は30秒、小領域描画は120秒。依存物と対照をD:から読み、試験出力をC:に作る。各コマンドをネットワーク分離して実行する。

```powershell
wsl -d Ubuntu -- python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/r007/20261112-crop-input-guard01/run_trial.py run01
```

ハーネスは、元版のhelpを取得してから既存のR005単一TUコンパイル・リンクコマンドで製品候補と観測用2版をビルドする。不存在入力を渡して実CLIの終了コード・診断・出力の有無を検査する。観測版でheight欠落時と正常6ケースの選択を比べる。製品候補でPHerc0814の128×128を3層だけ描画し、既存のstack対照 `049.tif`〜`051.tif` と照合する。追加の短いmerge試験も行う。原票は `run01/`、生成物は `.work/r007-crop-input-guard01/run01`。失敗時は `stop.json` に段階を残す。C:の保存ソースが必要なら、元blobを照合して `prepare.py` で再生成できる。

データ不要の回帰チェック単体は `python3 -B check_cli.py /path/to/vc_render_tifxyz` で動かせる。実CLIを呼び、無効指定と既定・原点省略・負原点・auto・help・merge分岐を確認する。
