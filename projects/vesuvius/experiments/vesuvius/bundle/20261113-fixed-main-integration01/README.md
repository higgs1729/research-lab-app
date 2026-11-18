# 固定main上のR005・R007・R009統合試験

[研究160](../../../../research/160-bundle-fixed-main-integration.md)の原票。上流基点は `14d4e725df8b569e6fc8ceb3c04d130f705c1565`。`volume-cartographer`、`vc_reader`、`vc_object_store` の固定本文を用い、他のモノレポ領域は試験に含めない。

## 固定本文とパッチ

研究158の不足一覧と、研究146が保存したGitHubの固定treeを照合した。C:側の研究146 indexにある `vc_reader/README.md` はローカルで再利用。残る374件だけを `raw.githubusercontent.com/ScrollPrize/villa/<固定commit>/<path>` から、圧縮なしのHTTPSで逐次取得した。最初は252 Bの1件で検証した。URL・HTTP応答・サイズ・Git blob IDとSHA-256は `fetch-plan.json` と `fetch-*.jsonl`。本文6,965,009 B、HTTP応答ヘッダーと要求側の保守的余裕込み7,824,340 B。TLS/TCPレベルのバイトは個別計測していない。受信本文の上限、HTTP計上上限は32 MiB。

`stage.py` は、ネットワーク分離後にD:の固定Git treeと保存treeを再照合し、ローカルGit 1,894、ローカルC: index 1、取得本文374の計2,269ファイルを別のLinux作業先に展開する。各ファイルは長さ・Git blob ID・SHA-256・modeを記録する。パッチは凍結済みR005二段、R009、R007の順に適用する。変更10ファイルの固定元blob、適用順、途中/最終SHAは `run01/patch-result.json`。R005製品3ファイルはR150、R009単体7ファイルはR146、R007とR009適用後rendererはR123の実コンパイル元 `66d96d1e…` と一致する。

## 通常構築と最小実行

取得後の作業はUbuntuの `C:/WSL/Ubuntu/ext4.vhdx` 内に分離する。R159のCMake実引数、プロセス計測、readerヘッダー検査、共有ライブラリ検査を再利用。上流CMake/Ninjaへ `flatboi vc_core vc_obj2tifxyz vc_render_tifxyz` を指定する。PaStiX/SPM、libigl、vc_delta3dの保存ソースから別の作業コピーを作る。libbacktraceは上流ExternalProjectを使い、既存D: Gitのmaster `0b9b49cf…` をローカルfile URLで提供。D:はプロセス専用mount名前空間で読み取り専用にする。ネットワーク分離、1CPU、OpenMPと数値ライブラリ1スレッド、AS4 GiB、core 0。作業6 GiB、ホストC:空き10 GiBを監視する。

PowerShellで `C:/dev/kensyoukin` を起点とし、取得済み `blobs` がある状態で別の実行タグを指定する。以下は再構築する場合の入口。

```powershell
$entry = @'
set -eu
mount --make-rprivate /
mount --bind /mnt/d /mnt/d
mount -o remount,bind,ro /mnt/d
exec python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/bundle/20261113-fixed-main-integration01/integrate.py run02
'@
wsl -d Ubuntu --exec unshare -Urnm bash -lc ($entry -replace "`r",'')
```

構成600秒、ビルド2,400秒、R005第一面120秒、R007の保存CLI試験120秒、R009は通常・初回resume・L0-only resume各60秒。各工程の `*-start.json` と `*-process.json` にPID/PGID、開始時刻、引数、期限、作業先、計測と終了状態を保存する。比較は `compare.py <実行タグ>` をR103の既存Windowsランナー経由で起動する。研究157の保存R009幾何・読取条件と15ファイル検査を借りる。L0-only状態は今回の正常対照から `.zgroup` とL0のみをコピーして作り、停止試験は行わない。全6レベルの値、OME、全ファイル、既存L0ファイルの内容・mtime・inodeを照合する。

## 実測結果

Linux作業先 `/home/tomoy/bundle-fixed-main-run01-pywin6ml`。`run01` で構成75.785秒・RSS52,809,728 B、ビルド993ステップ653.284秒・RSS1,672,572,928 B。4標準ターゲットは終了0。初回の計測側 `ldd` 判定が、`build/bin/../core` と `../reader` の表記を許容せず停止した。`run01/failure.json` と `launch01.log` を保存し、実体を `Path.resolve()` で検査して、同じ生成物の未起動試験のみ `integrate.py continue run01 run01-smokes` で続行した。構成・ビルドは各一回。再開前後で新生成物SHAは一致した。[ビルド原票](run01/build-process.json) · [rendererリンク](run01-smokes/renderer-link-check.json)

- R005第一面24.089秒。172×683のXYZ三枚はR150・R159とSHAおよび各117,476 float32ビット一致。名目scale一致、meta差はUUID。 [比較](run01-smokes/comparison.json)
- R007保存CLI回帰18件を0.376秒で完了。早期拒否9件、正当cropの入力open到達5件。 [比較](run01-smokes/r007-comparison.json)
- R009通常0.172秒、空出力先への初回resume 0.176秒、L0-onlyからのresume 0.179秒。通常はR157と一致し、2種類の再開は新通常と全15ファイル・全6論理階層・OME一致。L0-onlyの既存4ファイルでSHA、mtime_ns、inodeを保持。 [比較](run01-smokes/r009-comparison.json)

主担当が独立コードで固定ツリー2,269本文とmode、保存とLinux側のXYZ、R007 JSONL、R009の生チャンク別復号とL0-only保持を照合した。最終作業割当1,627,389,952 B、C:空き43,591,737,344 B。依存インストール・クラウド支出0。GUI、全アプリ、通常Python初期化とwheelは未検証。[独立照合](lead-check.json) · [作業最終状態](run01-smokes/final-state.json)
