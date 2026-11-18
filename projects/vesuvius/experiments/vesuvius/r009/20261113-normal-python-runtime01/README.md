# R009の通常Python初期化とローカルZarr保持試験

[研究163](../../../../research/163-r009-normal-python-runtime.md)の原票。固定ソース、依存、標準CMake引数と停止条件は[研究162の計画](../20261113-normal-python-feasibility01/README.md)。

## 実行条件

R160固定14d4e725にR009適用済みの `vc_reader` と保存Delta3Dソースを、C:上のUbuntu ext4へコピーした。固定readerの全本文SHAとファイルmode、Delta3Dコピー、R125のCPython ABI・配布物3件のSHAを照合した。Ubuntu CPython 3.12.3-1ubuntu0.17 amd64、nanobind 2.10.2、NumPy 2.2.6、CMake 3.28.3、Ninja 1.11.1、GCC/G++ 13.3.0。製品ソースやCMakeへの追加差分はない。[準備原票](run02/prepared.json)

`run.py` はR159の `measured` で工程を起動する。上流単体CMakeのCPU Debug O0で `_catalog` と `_reader` を明示して、その依存を一緒に構築する。stageはコピーした実PythonパッケージとCMakeが直接出力する二拡張・native共有ライブラリからなる。R125から借りるのは開発ヘッダー・nanobind・NumPyで、旧nativeをロードする経路は使わない。ネットワーク・mountの分離、D:のread-only bind、1 CPU、数値/OpenMP 1スレッド、AS 4 GiB、core 0、作業2 GiB、ホストC:空き10 GiB。構成180秒、ビルド900秒、試験120秒で、各工程のPID/PGID、絶対期限、引数、ログを保存する。[資源条件](run02/environment.json) · [構成原票](run02/configure-start.json) · [ビルド原票](run02/build-start.json)

親が再現の範囲を決めた後、PowerShellの `C:/dev/kensyoukin` から未使用ラベルを指定できる。`run01` は事前確認の停止票、`run02` は今回の製品工程に対応する。

```powershell
$trial = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-normal-python-runtime01'
wsl -d Ubuntu --exec unshare -Urnm bash "$trial/launch.sh" run03
```

`run01` の事前確認ではR125のdpkg原票と比較する際、計測側で全パッケージ名へ `:amd64` を付けたため停止した。R125と同じ標準出力を使う計測変更後に別ラベルで起動した。`run01` のconfigure、build、製品試験はいずれも0回。[初回停止](run01/failure.json) · [初回ログ](launch01.log)

## 結果

`run02` で固定reader全772本文/modeとDelta3D 137本文コピーを確認した。構成、ビルド、通常import試験を各1回起動し、すべて終了0。ビルドは83ステップ。標準 `_catalog` と `_reader` の `PyInit_*`、`.cpython-312-x86_64-linux-gnu.so` の拡張名、`_reader` が今回stage内に新規構築した `libvc_reader_native.so` に解決することを確認した。[構成後照合](run02/configure-check.json) · [ビルドログ](run02/build.log) · [ELF照合](run02/link-check.json)

凍結 `verify_python.py` を `-B -S -v` で実行した。`-S` はPythonのsite初期化を省く。`--writer` と `--extension` は渡していない。`verify.log` 188/240行と241/478行にstageの `vc_reader/__init__.py` と `vc_reader/reader/__init__.py` のソースロードとimport完了がある。JSONは `import_isolated=false`、実writerと拡張2件のパス・SHA、NumPy 2.2.6を記録する。[試験引数](run02/verify-start.json) · [importログ](run02/verify.log) · [結果](run02/result.json)

- `preserve_existing=True` でL0のgzip 7・スラッシュ区切り、L1の無圧縮・ドット区切りを維持した。既存7ファイルのSHA-256とmtime、L0全64画素の17とL1全16画素の9が一致した。欠けたL2をshape/chunks `(1,2,2)`、gzip 7・スラッシュ区切りで作った。
- 既定引数ではL0のファイルSHA・mtimeを保ち、メタデータだけのL1をL0の設定で作り直してL2を作った。従来の4引数 `_reader.create_pyramid_levels` も通過した。
- `test_create_pyramid_levels_preserves_existing_arrays` のAST関数本体を実APIで実行した。試験はローカルの小さい3 fixtureに限定し、全pytest・wheel構築や導入・他Python/OSは未検証。[結果](run02/result.json)

終了0の試験後、計測側がCPython `-v` のソース行に引用符が付くと仮定して検査を停止した。元ログは引用符なしで両初期化の行を含む。停止票を保存し、`finish-saved run02` で同じログ・JSON・生成物を読み直した。製品3工程は再起動せず、実Linux fixture全22ファイルを `run02/fixtures/` に保存してSHAとmtimeを記録した。[後処理停止](run02/failure.json) · [保存照合](run02/verify-check.json) · [完了票](run02/complete.json)

| 工程 | 壁時間（秒） | 最大RSS（B） |
| --- | ---: | ---: |
| configure | 16.290 | 28,467,200 |
| build | 762.035 | 3,201,777,664 |
| verify | 2.180 | 122,052,608 |

ビルドは約12分42秒で、R162の目安4〜8分を超え、900秒以内で完了した。最終作業割当363,208,704 B、ホストC:空き42,636,468,224 B。新規取得・依存導入・追加クラウド支出0。電力・モデル費は未算定。[構成プロセス](run02/configure-process.json) · [ビルドプロセス](run02/build-process.json) · [試験プロセス](run02/verify-process.json)

主担当が別の静的検査で両初期化の実ログ・固定SHA、実writerと拡張2件のSHA、保持7ファイルのLinux SHA・mtime、新規メタデータ、保存22ファイルの集合と本文を確認した。標準ライブラリで全80画素を直接復号して17/9を照合した。照合0.615秒、最大RSS62,783,488 B、製品再起動0。[独立検査コード](lead_check.py) · [独立照合結果](lead-check.json) · [lab登録候補](record.json)
