# R009通常Python importの最小構築案

[研究162](../../../../research/162-r009-normal-python-feasibility.md)の読取調査。2026-11-13 JST。通常の `vc_reader.reader.writer` import に要る拡張は `_catalog` と `_reader`、外部PythonパッケージはNumPy。固定14d4e725の上流 `vc_reader/CMakeLists.txt` で、この二つを明示的にビルドする一案を選んだ。通常importとローカルZarrの保持・既定動作を次の一回で測る。以下の構成・ビルド・試験コマンドは未実行。[読取原票](readback.txt)

## 入力とABI

- R160の実ソース `/home/tomoy/bundle-fixed-main-run01-pywin6ml/villa/vc_reader`。基点 `14d4e725df8b569e6fc8ceb3c04d130f705c1565`、R009適用済み。`bindings.cpp`、`zarr_write.hpp`、`pyramid.cpp`、`writer.py`、`test_zarr_writer.py` の実体SHA-256がR160の変更後票と一致。二つの `__init__.py` も保存ソースから使う。[R160パッチ票](../../bundle/20261113-fixed-main-integration01/run01/patch-result.json)
- R160の同階層 `vc_delta3d`。R158で保存Gitの `45339743b450ff707d21fb742dc1b3b2bf99306d` を確認し、R160で `.git` を除いて作ったソースコピー。上流のローカルFetchContent overrideに渡す。CMake 3.28.3、Ninja 1.11.1、GCC/G++ 13.3.0、Threads、nlohmann_json、CURL、zlib、SQLite、libtiff、libpng、libjpeg、blosc、zstd、lz4は現Ubuntuの既存資産。[依存の固定点](../../r005/20261113-standard-build-feasibility01/dependencies.log) · [R160構築記録](../../bundle/20261113-fixed-main-integration01/README.md)
- `/usr/bin/python3` はUbuntu CPython 3.12.3 amd64、Debian版 `3.12.3-1ubuntu0.17`、SOABI `cpython-312-x86_64-linux-gnu`。R125の `.work/r009-python-validation01/run01` に同版の開発ヘッダー、nanobind 2.10.2とNumPy 2.2.6が展開済み。保存した公式配布物3件のSHA-256を再照合した。合わせて22,457,878 Bの既存配布物を使うので、追加取得は0 B。ヘッダーの `pyconfig.h` がmultiarch側を参照するため、CMakeの `Python_INCLUDE_DIR` とC++フラグの `-isystem` を両方渡す。[R125 ABI票](../20261113-python-validation01/run01/abi-inputs.json) · [Ubuntu/PyPI配布票](../20261113-python-validation01/run01/downloads.json)
- R160親CMakeの `volume-cartographer/cmake/ObjectStore.cmake` が `VC_READER_BUILD_PYTHON OFF` でreaderを組み込む。R160には共有nativeと静的catalog/sftp/thinningがある。単体 `NativeReader.cmake` は自分で `vc_reader_native` を宣言する。既存の `vc_readerConfig.cmake` も未インストールのビルド位置にあり、隣のインストール用 `vc_readerTargets.cmake` を前提にする。そこで既存バイナリは規模の見積根拠に使い、次の試験は二拡張とその依存を同じ固定ソースから一緒に構築する。R125の `_reader` ELFには旧D: nativeへのRUNPATHがある。[読取原票](readback.txt)

`src/vc_reader/__init__.py` は `_catalog` を直接importする。`reader/__init__.py` が読むwriter、reader、cacheなどで `_reader` とNumPyをロードする。`src/cpp/sources/bindings.hpp` も `_reader` の初期化中に `_catalog` をimportする。`_thinning` と `_transforms` のPython拡張は対象入口の依存閉包に現れず、native thinningは通常のCMake依存で入る。`pyproject.toml` の `scikit-build-core` はwheel工程のビルド依存。今回の次試験では上流CMakeが出す拡張を固定ソースの通常パッケージと同じディレクトリに置き、wheelの構築・導入は別の検証範囲になる。[読取原票](readback.txt)

## 次の一回

親が実行を選んだ場合、Ubuntuの `unshare -Urnm` 内で進める。R160と同じ専用mount名前空間でD:をread-onlyにし、C:上のWSL ext4に `mktemp` の別先を取る。R160の計測と同様に各工程の引数、PID/PGID、時刻、上限、ログ、終了状態を保存し、ホストC:空きと作業量を監視する。下記はその名前空間内の工程コマンド。外部パッケージ探索に影響する既存 `LD_LIBRARY_PATH` 等は解除する。各製品工程は1 CPU、AS 4 GiB、core 0。例のCPU 0は実行時の許容CPU集合から選ぶ。[既存実行管理](../../bundle/20261113-fixed-main-integration01/README.md)

```bash
set -euo pipefail
fixed=/home/tomoy/bundle-fixed-main-run01-pywin6ml
repo=/mnt/c/dev/kensyoukin
deps="$repo/.work/r009-python-validation01/run01"
pinc="$deps/python-dev/usr/include"
verify="$repo/deliverables/vesuvius/november-workflow-improvements-20261113/zarr-output-recovery/verify_python.py"
work=$(mktemp -d /home/tomoy/r009-normal-python-XXXXXX)
build="$work/build"
stage="$build/stage"
mkdir -p "$stage" "$work/tmp"
cp -a "$fixed/villa/vc_reader" "$work/source"
cp -a "$fixed/vc_delta3d" "$work/vc_delta3d"
cp -a "$work/source/src/vc_reader" "$stage/vc_reader"
unset LD_LIBRARY_PATH LD_PRELOAD PYTHONHOME
export TMPDIR="$work/tmp" PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 OMP_THREAD_LIMIT=1 MKL_NUM_THREADS=1 CUDA_VISIBLE_DEVICES=
ulimit -v 4194304
ulimit -c 0

PYTHONPATH="$deps/site" timeout -k 10s 180s taskset -c 0 cmake \
  -S "$work/source" -B "$build" -G Ninja \
  -DCMAKE_C_COMPILER=/usr/bin/gcc -DCMAKE_CXX_COMPILER=/usr/bin/g++ \
  -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_FLAGS_DEBUG=-O0 -DCMAKE_CXX_FLAGS_DEBUG=-O0 \
  "-DCMAKE_CXX_FLAGS=-isystem $pinc" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
  "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=$stage/vc_reader" -DCMAKE_BUILD_RPATH_USE_ORIGIN=ON \
  -DVC_READER_BUILD_PYTHON=ON -DVC_READER_BUILD_READER=ON -DVC_READER_SHARED_READER=ON \
  -DVC_READER_ENABLE_CUDA=OFF -DVC_READER_BUILD_NATIVE_TESTS=OFF -DVC_READER_BUILD_C_API=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_vc_delta3d=ON -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
  "-DFETCHCONTENT_SOURCE_DIR_VC_DELTA3D=$work/vc_delta3d" \
  -DPython_EXECUTABLE=/usr/bin/python3 "-DPython_INCLUDE_DIR=$pinc/python3.12" \
  "-Dnanobind_DIR=$deps/site/nanobind/cmake"

# この時点で compile_commands.json と Ninja の対象を照合する。
timeout -k 10s 900s taskset -c 0 cmake --build "$build" --target _catalog _reader --parallel 1

# この時点で両拡張のSOABIと readelf / ldd の解決先を照合する。
PYTHONPATH="$stage:$deps/site" timeout -k 10s 120s taskset -c 0 /usr/bin/python3 -B -S -v "$verify" \
  --upstream-test "$work/source/tests/test_zarr_writer.py" \
  --work "$work/fixtures" --report "$work/result.json" \
  >"$work/verify.stdout" 2>"$work/import.log"
```

起動前にソースSHAとR125のヘッダー・配布物・SOABIを照合。構成後は `compile_commands.json` が新作業コピーの `bindings.cpp`、`catalog_bindings.cpp`、`pyramid.cpp` とR125の開発ヘッダーを参照することを確認する。`ninja -t query _catalog` と `ninja -t query _reader` で対象を確認。ビルド後は拡張2件が `.cpython-312-x86_64-linux-gnu.so` であること、`ldd` で欠落がなく `_reader` の `libvc_reader_native.so` が今回のstage実体へ解決することを確認する。相対成分のあるldd表記は `realpath` で比較する。

合格条件は、`import.log` でstageの `vc_reader/__init__.py` と `vc_reader/reader/__init__.py` のロードが追え、`result.json` が `import_isolated: false`、stage内の実writerと両拡張の実パス・SHA-256、NumPy 2.2.6を示し、試験が終了0になること。Trueで既存L0/L1のSHA、mtime、画素17/9を保持しL2を作る。既定呼出しは従来のメタデータ初期化を再現し、既存4引数native呼出しも通る。`--upstream-test` は上流テストの指定関数本体を実関数で再実行する。`-S` はPythonのsite初期化を省く指定で、パッケージの二つの `__init__.py` は通常のimportにより実行される。[既存検査](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/zarr-output-recovery/verify_python.py)

## 見積と停止条件

R160のNinjaログでreader配下200.773秒、Delta3D 29.917秒のコマンド時間を確認。R125のbindings初回（後続nanobindで停止）は119.687秒・最大RSS 3,201,736,704 B、catalog増分48.378秒、成功試験2.336秒。次の構成は数十秒、二対象ビルドは約4–8分、試験は数秒、作業は0.4–1 GiBを見込む。今回の構成・RSSの実測値は未確認。特に上流のコンパイルフラグと固定14dでの `bindings.cpp` のAS4 GiB内の成立は次の実測で判定する。各工程1回、構成180秒、ビルド900秒、試験120秒。作業2 GiBとホストC:空き10 GiBを停止条件とする。調査時のC:空き43,546,841,088 B。[読取原票](readback.txt) · [R125実測](../../../../research/125-r009-python-validation.md)

固定ソース・ABI・依存の欠落、想定外の取得や別native実体への解決、時間・容量・AS上限、構成・ビルド・試験の異常があれば、該当工程の原票を保持して終了する。次の試験の見積は新規取得0 B、追加クラウド費0円。
