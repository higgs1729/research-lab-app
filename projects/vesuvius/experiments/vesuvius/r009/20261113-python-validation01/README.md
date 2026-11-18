# R009 Pythonバインディングの実行確認

[研究125](../../../../research/125-r009-python-validation.md)の再試験用。`verify.py` は小さいローカルZarr v2を作り、既存L0/L1のファイルSHA-256、更新時刻、復号画素と、新規L2のshape、chunk shape、dtype、圧縮、区切りを照合する。`preserve_existing` を省略した公開関数と、既存4引数の `_reader.create_pyramid_levels` も呼ぶ。

通常のパッケージを導入できる環境では、パッチ済み `vc_reader` を使うPythonでこのスクリプトを直接実行する。

```sh
python -B verify.py
```

既存ビルドの拡張だけを使う場合は、実際のソースツリーの `writer.py` と、そのPython用にビルドした `_reader` 拡張を渡す。実 `_catalog` 拡張は `_reader` と同じディレクトリに置ける。`--work` は新規ディレクトリ。`--upstream-test` を付けると、指定したパッチ済みテストファイルから追加回帰テストの `FunctionDef` を取り出し、同じASTの本体を実 `ZarrWriter`、`ZarrReader`、`create_pyramid_levels` で実行する。

```sh
python -B verify.py \
  --writer /path/to/vc_reader/src/vc_reader/reader/writer.py \
  --extension /path/to/_reader.cpython-312-x86_64-linux-gnu.so \
  --upstream-test /path/to/vc_reader/tests/test_zarr_writer.py \
  --work /path/to/new-output
```

隔離実行ではパッケージの検索パスだけを登録し、実 `writer.py` とその依存Pythonモジュール、実nanobind拡張 `_reader` と `_catalog` をロードする。`vc_reader` と `vc_reader.reader` の `__init__.py` は実行範囲外。pytestランナー、全テスト、wheel、通常のパッケージ初期化はこの研究の対象外。

## このWSL環境での再ビルド

PowerShellで実行する。`run02` は未使用のラベルを使う。今回の増分ビルドは `run01/build04`。再実行には修正済みの隔離CMake設定を使うため `build01` から実行できる。

```powershell
$r009Python = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-python-validation01'
wsl -d Ubuntu -- python3 -B "$r009Python/prepare.py" run02
wsl -d Ubuntu -- python3 -B "$r009Python/build.py" run02 build01
wsl -d Ubuntu -- python3 -B "$r009Python/run_test.py" run02 build01 test01
wsl -d Ubuntu -- python3 -B "$r009Python/check_fixed_main.py" run02
```

`prepare.py` はUbuntuの実行中のCPythonと同版の開発ヘッダー、nanobind、NumPyだけを公式配布元から取得し、C:の `.work/r009-python-validation01/runNN` に展開する。`build.py` はR121で固定したpatchを適用した `bindings.cpp`、初期化に必要な `catalog_bindings.cpp`、nanobindをコンパイルし、既存R121 `pyramid.o` とD:のnative、thinning、catalog、sftpライブラリをリンクする。build/testはCPU 1、AS 4 GiB、core dump 0、`unshare -Urn`。プロセスと出力の原票をこのディレクトリの `runNN` に保存する。

`resume-pyramid-python-fixed-main.patch` は公開候補のPython差分。研究121で保存したPython差分から、README hunkの隣接する未変更文脈だけを固定main `0080fa393724575d4f19059d91402757f9351b28` に合わせた。固定mainの元ファイルでR007→R121→R123→このPython差分の順に `git apply --check` と適用を確認した。実行に使ったbindings、writer、テスト、ピラミッドヘッダー・実装と適用後のSHA-256が一致する。
