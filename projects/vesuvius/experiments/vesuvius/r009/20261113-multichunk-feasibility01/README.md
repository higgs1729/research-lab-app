# R009 複数L0チャンクの実中断試験案

[研究156](../../../../research/156-r009-multichunk-resume-feasibility.md)の保存物調査。ネイティブ実行と停止は次の試験。固定入力はR129/131のPHerc0139 w035と9.362 µm CTレベル0。試験には [R123の結合ビルド原票](../20261113-pyramid-metadata01/run01/build-settings.json) のC:製品ELFを使う。バイナリと入力13件はR131のSHA-256に一致した。

## 固定する一件

R131正常対照の引数を借り、`--crop-x 2239 --crop-y 1343 --crop-width 1 --crop-height 129` と新規出力先にする。Zarr v2のみ、無圧縮uint8、`--pyramid true`、28層、scale 1、step 1、group 0、bicubic、`--flip-normals`、9.362 µm、cache 1 GiB。TIFF・複数part・回転・合成は使わない。通常・停止・再開で同じ描画引数を使用し、再開コピーだけ `--resume` を追加する。[R131の引数原票](../20261113-interrupted-render01/run02/normal-process.json)

保存 `--help` と実ソースでは、チャンクのXYを設定するCLIがない。L0の `chunks0` は `[baseZ,min(128,H),min(128,W)]`。Z全層を一緒に書くため、XY面積最小の二タイルは1×129。出力shape ZYXは `[28,129,1]`、chunksは `[28,128,1]`。L0の `0/0/0/0` は128行、`0/0/1/0` は実データ1行。後者も本体は各層128行分で、残りは0埋め。L1〜L5の高さは65、33、17、9、5で、幅1と28層を維持する。OMEルートの独自 `chunk_size` と実配列 `.zarray` の `chunks` は別項目として比較する。

`check_saved.py` は保存TIFXYZから、実装が使う格子の列111・行67〜73と、Hermite中心差分が使う40頂点を特定した。すべて有効。位置多項式をBezier制御点の凸包で囲い、単位法線の各座標について ±13.5 voxel、算術余裕1 voxel、三線形の上側コーナーを加えた。ZYXの保守的範囲は `[3987,3362,4164]`〜`[4157,3423,4205]`、必要CTキーは `0/31/26/32` と `0/32/26/32` のみ。4 MiBの両キーは保存済み。重複するR129の `(x=2239,y=1408..1471)` では同じfloat32格子で、第1タイル63画素・1,764標本、第2タイル1画素・28標本が保存実値で非ゼロ。新規65画素のネイティブ法線や、タイルごとにCT内部原点が変わったときの丸め前値・uint8同一性は未確認。全体の両実キーを正常対照で確認する。[候補とCT範囲](candidate03.json)

## 実停止と合否

1. 新しいC:作業先で正常対照を1回だけ作る。終了0、L0の2ファイルが実在し各3,584 B、実領域に非ゼロ値、末尾の余白0、OMEがL0〜L5実配列を参照することを確認。入力/ELFのSHA-256が異なる場合と両キーが揃わない場合は先へ進まない。
2. 同じ引数で空の別出力をGDB all-stopから1回起動。ELFハッシュを照合し、x86-64 non-PIEのuint8 `renderTiles` の `writeChunkSkipEmpty` 呼出直後 `0x62afee` にブレークポイントを置く。最初の到達でPC、backtrace、`$al == 1`、inferiorのPID・exe・出力引数・tracing stop・起動元と異なるネット名前空間を保存する。出力は `.zgroup`、L0〜L5 `.zarray`、対照とSHA/長さが同じ第1キーだけ。第2キー、L1〜L5の実チャンク、ルート `.zattrs`、一時ファイルがないことも確認する。この集合と一致した時点で自分が起動したinferiorを終了させ、終了原票・PID消失・回収と残存出力の一致を記録する。GDBの例外とOS終了状態を分け、観測できた範囲で記述する。通常完走後のファイル削除は使わない。[固定ELFの停止位置](elf-inspection.log)
3. 停止原票と現物を照合し、新しいC:コピーに `--resume` を付けて1回だけ再開する。成功判定の一つは、同一コピー上で第1キーのSHA・mtime_ns・inodeを保ち、第2キーを新しく保存すること。必要に応じて再開のuint8 `chunkExists` 戻り `0x62b746` の真/偽やL0 writer呼出1回を観測できる。通常の比較では、既存L0が保持された根拠に前後のファイル情報を使う。[再開分岐](resume-branch.log)
4. 別の成功判定として、正常対照と再開後のファイルパス/長さ/SHA、全6解像度の全uint8値・shape・実chunks・codec/fillとOMEのaxes/変換/参照を比較する。L0の再構成時は第2チャンクの末尾パディングを論理配列から除き、パディング自体も別検査する。コピー元とコピー先のmtime差は書換えと扱わず、同じコピーの再開前後で測る。

通常はL0を作り、下位配列メタデータを初期化し、L0タイルを書き、最後に下位画素とルート属性を書く。Zarrのみのresumeは既存L0キーの存在を見てタイルをスキップし、欠けたタイルを描く。ローカルwriterは一時ファイルから最終名に置換する。既定Fastはfsyncを要求しない。第1キーの発行後を測る今回の案では、下位配列メタデータがすでにある。旧ELFにも `chunkExists` 呼出があり、この案は複数L0の保持・完走同等性を評価する。R009修正固有の救済、書込み途中の破損、停電、同時書込み、複数partは範囲外。[旧ELFの静的記録](old-elf-inspection.log)

## 上限と資料

R131正常描画0.527秒・約66 MiB、停止6.151秒・約606 MiBが目安。候補はL0の3,612値とパディング込み出力ペイロード10,780 Bの見込み。次の実験の予算案はCPU affinity 1・OpenMP/数値1スレッド・AS 4 GiB・core 0、`unshare -Urn`、各60秒・3プロセス累計180秒、C:作業128 MiB、停止試行1回。全体タイムアウト時は自分が起動した対象・GDBの回収を確認して終了する。既存ファイルは読取のみ。新規取得・ビルド・クラウド費用は0の計画。

今回の調査は固定済みの1候補の解析とバイナリの静的検査。`candidate.json` は0.01 voxel余裕の初回、`candidate02.json` は1 voxel余裕での二回目。初回・二回目の解析で左上の混合微分の添字を読み違えた。`points.hpp` に沿って各隅自身の混合微分で修正した採用原票が `candidate03.json` で、数値は二回目と一致した。Windows PowerShellから以下で解析だけを再実行できる。再実行は未使用の出力名にする。

```powershell
$runner = 'experiments/vesuvius/r005/20261112-ct-render01/run_windows.py'
$rel = '../../r009/20261113-multichunk-feasibility01'
python -B $runner "$rel/check04-process.json" "$rel/check_saved.py" candidate04.json
```
