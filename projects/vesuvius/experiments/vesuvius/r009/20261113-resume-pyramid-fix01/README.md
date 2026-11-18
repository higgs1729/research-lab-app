# R009 Zarrピラミッド再開の確認

[研究121](../../../../research/121-r009-resume-pyramid-fix.md)の製品差分は `resume-pyramid.patch`。研究119に保存した元rendererを基点とし、既存 `createPyramidLevels` の階層計算を使う。通常実行と `--pre` は従来の3引数呼び出し。単一partで `--resume` とピラミッドが有効な場合だけ、保存済みL0に合わせて欠けた配列メタデータを作る。

PowerShellからWSL Ubuntuの既存環境で実行する。`run02` は両方で同じ未使用の識別子にする。ビルド・試験は同時に走らせない。`build.py` の前に新しいビルドディレクトリや依存導入は不要。

```powershell
$r009Trial = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-resume-pyramid-fix01'
wsl -d Ubuntu -- python3 -B "$r009Trial/build.py" run02
wsl -d Ubuntu -- python3 -B "$r009Trial/check.py" run02
```

- `build.py` はD:から元ソースと既存コンパイル設定を読み、C:でR009を適用する。R007とR009の両適用順も確認し、R009のみのrendererとpyramidの2翻訳単位をコンパイルする。既存ライブラリを再利用し、変更した2オブジェクトを実行ファイルに直接リンクする。コンパイラの依存ファイルとリンク済みシンボルを確認する。
- `check.py` は研究120とR115の対照およびR115の固定CTをハッシュ照合し、修正CLIを実行する。6レベルのshape、dtype、復号した全画素、OME属性を比較する。非既定設定の試験はL0をgzipレベル7・ドット区切り、L1を無圧縮・スラッシュ区切りに変え、L3には元のbloscを残す。3つの欠落レベルがL0の設定を継ぎ、既存の配列メタデータとL0の全ファイルのSHA-256・更新時刻が維持されるか確認する。
- ログ、実行条件、結果はこのディレクトリの `runNN`、コンパイラ依存ファイル、バイナリとZarr出力は `C:/dev/kensyoukin/.work/r009-resume-pyramid-fix01/runNN` に保存する。停止時は `build-stop.json` または `test-stop.json` と各プロセスのログを参照する。
- CPU 1、AS 4 GiB、core dump 0、`unshare -Urn`。ビルド300秒、試験120秒、C:作業128 MiB。固定入力、D:の元ソース・既存ライブラリおよび過去runは読み取りのみ。出力が既にある実行ラベルの再利用は拒む。

この差分は配列の初期化を修正する。L1以降の画素とrootのOME属性を再計算する既存処理は使い続ける。L0・既存下位レベルのshape、chunk shape、dtypeが今回の描画に合わないときはエラーを出す。

`resume-pyramid-python.patch` はネイティブ差分の後に適用する。既存Python関数 `create_pyramid_levels` に `preserve_existing=False` を加え、既定呼び出しは従来の動作。`preserve_existing=True` は作成済み配列を保持し、`overwrite` より優先される。適用とPython構文だけを確認するには、上の2コマンド後に `wsl -d Ubuntu -- python3 -B "$r009Trial/check_python_patch.py" run02` を実行する。このWSL環境ではnanobind・Python開発ヘッダー等が欠けており、バインディングのビルドと同梱pytestは未実行。
