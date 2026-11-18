# R005 標準CMakeで共有ライブラリと利用側を揃える試験

[研究159](../../../../research/159-r005-standard-cmake-build.md)の原票。`run.py` は上流CMake/Ninjaを起動し、条件と結果を保存する。CMakeListsやビルドグラフの書き換えは行わない。基点は保存済み `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5`。研究154の凍結製品パッチ2つを適用し、研究150の清書済み3ソースSHAと照合する。適用時の行末空白警告1件は凍結差分由来。

## 入口と記録

PowerShellから以下のWSLコマンドを使用する。タグは未使用のものを選ぶ。Linux側に作る専用作業ディレクトリは `start.json` に記録され、Ubuntuの `C:/WSL/Ubuntu/ext4.vhdx` 内にある。ビルド元・ビルド生成物・実行全出力はそこに保持する。C:の `experiments` には環境、構成、build、実行、照合の原票と最終XYZ TIFF・metaのコピーを置く。

```powershell
$entry = @'
set -eu
mount --make-rprivate /
mount --bind /mnt/d /mnt/d
mount -o remount,bind,ro /mnt/d
exec python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/r005/20261113-standard-cmake-build01/run.py run03
'@
wsl -d Ubuntu --exec unshare -Urnm bash -lc ($entry -replace "`r",'')
```

`unshare -Urnm` はユーザー・ネットワーク・mount名前空間を作る。D:を読み取り専用にする操作はその内側のみ。CPU affinity 1、OpenMPと数値ライブラリ1スレッド、AS4 GiB、core 0。構成600秒、ビルド2,400秒、第一面120秒をそれぞれ上限とし、作業6 GiBとホストC:空き10 GiBを監視する。各工程は `*-start.json` にPID/PGID、作業ディレクトリ、引数、時刻、ログ位置と上限を保存し、終了後は `*-process.json` にRSS・時間・ディスク観測と終了情報を保存する。既存出力には別タグを使う。`run01` はソース準備、`run02` が構成を起動した試行。

`run01` で `git archive <commit> <3 paths>` を実行すると、Git 2.43がpartial cloneの範囲外 `.github/CODEOWNERS` を要求して停止した。Git lazy fetch無効・ネット分離で、本文取得は起きていない。`run02` は同じ固定コミットの `git archive <commit>:<subtree>` を各3範囲に使い、必要範囲の本文だけで展開した。構成の実起動は `run02` の一回。

## 構築と照合

R003のGCC/G++/gfortran・QuickBuild O0・Ninjaを踏襲。`vc_obj2tifxyz` を標準ターゲットとして構成するため `VC_BUILD_APPS=ON` とし、ビルド対象は `flatboi vc_core vc_obj2tifxyz` の3件に限定。PaStiX/SPM・既存overlayを適用済みのlibigl・vc_delta3dはLinux作業先へコピー。生成物や古いCMakeCacheは再利用せず、libbacktraceは保存ローカルGit固定masterをfile URLに書き換え、上流ExternalProjectで通常のclone/build/installを行う。`configure-check.json` にreaderのヘッダーリンク、`make -j1`、ローカルmasterとbuild配下のパス、ターゲットを保存する。

構築後は共有 `libvc_core.so` のラスター定義と2利用側の同じライブラリへの解決、3翻訳単位のヘッダーを確認する。第一面の比較は既存Windowsの1CPU・4GiB runnerで行う。

```powershell
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$rel = '../20261113-standard-cmake-build01'
python -B "$r103/run_windows.py" "$rel/compare03-process.json" "$rel/compare.py" run03
```

既存R150の観測なし第一面と、172×683のXYZ三枚のSHA-256、全float32ビット、名目scaleを比較する。UUIDの差は別項目。固定main `14d4e725` 全体、旧バイナリへの新しい共有ライブラリの差し替え、OBJ生成、CT・推論は範囲外。

## 実測

採用原票は `run02/`、作業先は `/home/tomoy/r005-standard-cmake-run02-4lvsfbul`。構成77.208秒、標準3ターゲットの971ステップ686.787秒、別利用側のhelp 0.079秒、第一面26.793秒。ピークRSSはビルド1,672,716,288 B、第一面230,363,136 B。最終作業割当1,449,947,136 B、監視時点のC:空き最小45,294,411,776 B。全子プロセス回収、保護ファイルのSHA不変、外部取得・依存導入・追加クラウド支出0。[構成プロセス](run02/configure-process.json) · [ビルドプロセス](run02/build-process.json) · [作業最終状態](run02/final-state.json)

`run02/link-check.json` は実際の `.ninja_deps` で確認した同一ヘッダー、`nm` の共有ライブラリ定義、両利用側の `ldd`、新しいELFのSHAを含む。`run02/comparison.json` は3 TIFFのSHAと各117,476 float32画素すべて、名目scale一致を記録。metaの差はUUIDのみ。作業先のXYZ・metaと実験フォルダのコピーはそれぞれ同じSHAで、Linux側には他の生成ファイルも残してある。[リンク検査](run02/link-check.json) · [比較結果](run02/comparison.json)

主担当も別コードで実ソース3件、新ビルド4生成物、compile_commands、工程成功、Linux実出力と保存XYZ三枚のSHA・全float32ビット、名目scaleを照合した。[独立照合](lead-check.json) · [資源原票](lead-check-process.json)
