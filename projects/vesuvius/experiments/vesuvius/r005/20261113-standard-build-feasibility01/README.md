# R005 標準CMakeビルドの成立性

[研究158](../../../../research/158-r005-standard-build-feasibility.md)の読取調査。対象は `UvGridRasterizer` を共有 `vc_core` に置き、同じヘッダーで利用側も作る構成。通常CMakeでの最初の確認は、保存済み `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5` を使う一件を提案する。

## 固定mainと使用可能な比較基点

| 範囲 | 14d4e725のパス数 | D: Gitで本文欠落 | 本文量 |
| --- | ---: | ---: | ---: |
| volume-cartographer | 1,114 | 80 | 3,206,734 B |
| vc_reader | 772 | 5 | 143,964 B |
| vc_object_store | 383 | 290 | 3,719,089 B |
| 3範囲合計 | 2,269 | 375 | 7,069,787 B |

D:のshallow・blob:none Gitに固定main `14d4e725df8b569e6fc8ceb3c04d130f705c1565` のcommit/treeがある。`ls-tree` とオフライン `rev-list --objects --missing=print` の積集合を取り、履歴にだけある不足を除いた。モノレポ全体では6,462パス中2,693欠落。C:の関連する既存部分Gitで一致した欠落blobは `vc_reader/README.md` 1件で、3範囲の残り374件・6,965,009 B。固定mainでは `vc_reader/CMakeLists.txt`、`vc_object_store/CMakeLists.txt`、`core/src/QuadSurfaceStore.cpp` 等が欠落する。量はR146に保存した非切詰めtreeの未圧縮本文で、HTTP応答やGit packの見積もりではない。必要になった時点で、D:を書き換えずC:に固定3範囲の不足本文を取り、blob IDを照合する。今回は取得を伴わない7ad02f4を使う。[パスとblob](git-inventory.log) · [本文集計](source-availability.json)

7ad02f4では3範囲全2,159パスが揃い、Git本文合計43,689,906 B。候補が変える3ファイル（flatboi、SurfaceMeshing実装・ヘッダー）と、上流ルート・flatboi・core・appsの4 CMakeListsは14d4e725と同じblob。両コミット間で `vc_obj2tifxyz.cpp`、reader/object store等に差がある。この一件の検証範囲は7ad02f4上の通常ビルドと、その基点の利用側ABIに限る。

## 一回の標準構築案

1. `C:/WSL/Ubuntu/ext4.vhdx` を使うUbuntuのLinux側に専用の新規ディレクトリを用意する。`git archive` で7ad02f4の3範囲をD:から読み、通常CMakeが参照する兄弟配置に展開する。D:のソース、生成物、Gitを読取のみとし、ソース展開は通信分離、lazy fetch無効。公開R005パッチ、R150製品パッチの順に適用し、変更3ファイルをR150 `source-sha256.json` と照合する。ビルド版識別はGitなしのCMake用 `VC_GIT_SHA1` と `VC_GIT_COMMIT_DATE=2026-11-11` を渡す。凍結差分のほかに上流ソースやCMakeへの変更は不要という案。
2. PaStiX v6.4.0（SPM/Morse込み）、既に上流overlayを適用済みのlibigl、vc_delta3dを各々 `.git` を除く新しいLinux作業コピーにし、`FETCHCONTENT_SOURCE_DIR_PASTIX`、`FETCHCONTENT_SOURCE_DIR_LIBIGL`、`FETCHCONTENT_SOURCE_DIR_VC_DELTA3D` を渡す。既存PaStiX本体とSPM CMakeListsはR003が前処理した版。通常CMakeが両ファイルに `file(WRITE)` するのでD:を直接指定できない。PaStiXのサブモジュール実体は同梱され、`.git` が無いとそのCMakeのGit更新分岐には入らない。libiglの上書き5ファイルはすべて上流overlayと同一。vc_delta3dのコード生成先は新規binary dir。
3. R003はsystem `libbacktrace.pc` を見つけず、`ExternalProject_Add` のGit取得へ進んだ。`FETCHCONTENT_FULLY_DISCONNECTED=ON` はこのExternalProjectを対象にしない。標準のExternalProjectを使い、プロセス内Gitの `url.file:///mnt/d/kensyoukin-work/r003-build/_deps/libbacktrace/src/libbacktrace_build.insteadOf=https://github.com/ianlancetaylor/libbacktrace.git` を `GIT_CONFIG_COUNT/KEY_0/VALUE_0` で指定し、`GIT_ALLOW_PROTOCOL=file` とネット名前空間で外部通信を遮断する。既存ローカルGitの `master` とHEADは同じ `0b9b49cf4a2c9229fc052d6716e1528b2f23e91a`。上流の処理が作るclone、autotools build、installは新規C側build配下。既存 `.a` やD側stampの転用は含めない。ローカルURLの供給が成立しなければログを保存して止める。
4. R003の `cmake -S <villa>/volume-cartographer -B <build> -G Ninja` を用い、GCC/G++/gfortran、`QuickBuild`、`VC_QUICKBUILD_OPT_LEVEL=0`、`BUILD_SHARED_LIBS=ON`、`VC_BUILD_FLATBOI=ON`、`VC_BUILD_APPS=ON` を指定。`VC_TESTING`、`FLATBOI_BUILD_SLIM_TESTS`、`VC_BUILD_FIBERLETS`、`VC_BUILD_PYTHON`、`VC_READER_ENABLE_CUDA`、`VC_OBJECT_STORE_BUILD_SERVER` はOFF。`FETCHCONTENT_FULLY_DISCONNECTED=ON` と上記3source overridesを使う。`VC_BUILD_APPS=ON` で `vc_obj2tifxyz` が現れる。必要なQt6・OpenGLWidgets・Boost program_optionsのCMakeパッケージは既存。アプリ全体は構成されるため、実際の構成依存が揃うかはconfigureで確認する。`reader/include/vc_reader/native` がコピーでなくLinuxのシンボリックリンクであることをconfigure後に確認する。旧D:のexFAT上ではコピー分岐で二重定義が起きた。
5. `cmake --build <build> --target flatboi vc_core vc_obj2tifxyz --parallel 1` を一回だけ実行する。GUIや `vc_cli_all` はビルド対象に加えない。新規CMakeが管理するreader・object store・inpaint・依存ライブラリを使い、R003の古いCMakeCache/生成物・R150のオブジェクトは持ち込まない。`libvc_core.so` が新メソッドを定義し、flatboiと `vc_obj2tifxyz` が同じ新しい共有ライブラリを解決することを `nm -C` と `ldd`、`compile_commands` で確かめる。D:の旧共有ライブラリを探索パスに入れない。旧版利用側へ新しい共有ライブラリだけを配布するABI互換性は、この試験で保証できない。

`UvGridRasterizer` を実体化する既存の直接呼出元は、旧ソースのflatboiと `vc_obj2tifxyz`。`vc_tifxyz2obj` は同ヘッダーの独立関数を、`vc_obj2tifxyz_legacy` は別クラス `StepUvRasterizer` を使用する。直接呼出元の全数は上記7ad02f4範囲で確認した。`VC_BUILD_APPS=OFF` の旧Ninjaに `vc_obj2tifxyz` ターゲットがないことも確認した。[標準ターゲット原票](targets.log)

次段で使用するコマンド案。作業ディレクトリはLinux側で新設し、下の構築部分はR150と同等のCPU・AS・core・子プロセス回収制限を適用する。例の `timeout` は各工程の時間上限。依存の `.git` と既存生成キャッシュを除くコピーには既存の `tar` を使う。

```bash
set -euo pipefail
trial=$(mktemp -d "$HOME/r005-standard-build.XXXXXX")
frozen=/mnt/d/kensyoukin-work/r003-villa
deps=/mnt/d/kensyoukin-work/r003-build/_deps
repo=/mnt/c/dev/kensyoukin
baseline=7ad02f4f6e306b744ef6d2742dfe31fd55713ee5
mkdir "$trial/villa" "$trial/tmp"
export GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0 GIT_ALLOW_PROTOCOL=file
unshare -Urn git -C "$frozen" archive "$baseline" volume-cartographer vc_reader vc_object_store \
  | tar -x -C "$trial/villa"
cd "$trial/villa"
git -c core.autocrlf=false apply "$repo/experiments/vesuvius/r005/20261113-upstream-preparation01/R005.patch"
git -c core.autocrlf=false apply "$repo/experiments/vesuvius/r005/20261113-grid-preserving-native01/grid-preserving-prototype.patch"
for name in pastix libigl vc_delta3d; do
  mkdir "$trial/$name"
  tar -C "$deps/$name-src" --exclude=.git --exclude=__pycache__ -cf - . | tar -x -C "$trial/$name"
done
export AGENTS_AGENT_MODE=1 CMAKE_BUILD_PARALLEL_LEVEL=1 OMP_NUM_THREADS=1 OMP_THREAD_LIMIT=1
export OPENBLAS_NUM_THREADS=1 PASTIX_NUM_THREADS=1 TMPDIR="$trial/tmp"
export GIT_CONFIG_COUNT=1
export GIT_CONFIG_KEY_0="url.file://$deps/libbacktrace/src/libbacktrace_build.insteadOf"
export GIT_CONFIG_VALUE_0=https://github.com/ianlancetaylor/libbacktrace.git
cpu=$(awk '/Cpus_allowed_list:/{split($2,a,/[-,]/); print a[1]}' /proc/self/status)
ulimit -v 4194304
ulimit -c 0
taskset -c "$cpu" unshare -Urn timeout 600 cmake -S "$trial/villa/volume-cartographer" -B "$trial/build" -G Ninja \
  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=gfortran \
  -DCMAKE_BUILD_TYPE=QuickBuild -DVC_QUICKBUILD_OPT_LEVEL=0 -DBUILD_SHARED_LIBS=ON \
  -DVC_BUILD_FLATBOI=ON -DVC_BUILD_APPS=ON -DVC_TESTING=OFF -DFLATBOI_BUILD_SLIM_TESTS=OFF \
  -DVC_BUILD_FIBERLETS=OFF -DVC_BUILD_PYTHON=OFF -DVC_READER_ENABLE_CUDA=OFF -DVC_OBJECT_STORE_BUILD_SERVER=OFF \
  -DVC_GIT_SHA1="$baseline" -DVC_GIT_COMMIT_DATE=2026-11-11 -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
  -DFETCHCONTENT_SOURCE_DIR_PASTIX="$trial/pastix" -DFETCHCONTENT_SOURCE_DIR_LIBIGL="$trial/libigl" \
  -DFETCHCONTENT_SOURCE_DIR_VC_DELTA3D="$trial/vc_delta3d"
test -L "$trial/build/reader/include/vc_reader/native"
taskset -c "$cpu" unshare -Urn timeout 2400 cmake --build "$trial/build" \
  --target flatboi vc_core vc_obj2tifxyz --parallel 1
```

## 容量・時間と最小照合

C:空き49,030,148,096 B（45.7 GiB）。3範囲の本文約43.7 MB、既存依存コピー約21.6 MB（PaStiX 13,177,162 B、libigl 6,895,863 B、delta3d 1,563,712 B）、ローカルlibbacktraceのソース・生成物と全ビルドを合わせた目安3 GiB。上限6 GiBを提案し、C:空き10 GiB以上を保つ。旧D: buildは2.1 GiB。今回は容量計測だけで、コピー・構成・ビルドは未実施。ローカルコピーのファイル割当、ext4 VHDの増加量、初回ビルドRSSは未実測。[依存、空き、ツール](dependencies.log) · [ローカルsource](offline-source.log)

旧R003はconfigure約232秒、部分ビルド385秒でexFATの問題、残りの成功ビルド1,201秒。今回のconfigureは1〜4分、初回ビルドは20〜35分を仮見積もりとする。1CPU affinity、AS 4 GiB、core 0、OpenMP/数値1スレッド、`CMAKE_BUILD_PARALLEL_LEVEL=1` と `--parallel 1`。上流libbacktraceの `make -j` は `ProcessorCount` を使うため、生成された値もconfigure後に確認する。configure 600秒、build 2,400秒、最小実行120秒を一回ずつの上限案とする。外部取得要求、D:向け書込み、ヘッダーリンク不成立、4 GiB到達、上限超過で記録を保存して終了する。既存D:ビルドの置換や大きな依存導入は今回の案に含めない。

最小実行は、新規標準flatboiでR150の第一面 `experiments/vesuvius/r003/20261111-input01`、`--keep=100.0`、5反復、`--pack-components-preserve-grid` を一回。入力4ファイルを保存manifestと照合する。R150観測なし `run02/first-preserve-product/output` の `[172,683]`、3枚のXYZ TIFFのSHA-256と全float32画素、`meta.json` の名目scaleを比較する。UUIDは新規生成。既存実行の所要は約24秒。別利用側は `vc_obj2tifxyz --help` と共有ライブラリ解決の確認までで、OBJの再生成やCT・推論は範囲外。新規ネットワーク取得・依存導入・有料計算・追加データは0の計画。
