# w035の実CT描画の停止と再開

[研究131](../../../../research/131-r009-interrupted-render.md)の原票。既存R123結合版ELF、研究129のCT・完全な公開TIFXYZ・64×64×28の設定を再利用した。Zarrのみ、無圧縮uint8、ピラミッド有効。正常対照、停止出力、再開出力は `C:/dev/kensyoukin/.work/r009-interrupted-render01/`。その中の `run02/after-l0-chunk.zarr` と `run03/before-pyramid-arrays.zarr` が、実レンダラの停止で残った元出力。比較に使ったコピーは `run05/` に保存した。

| 元出力 | GDB停止位置 | 実際に保存済み | 再開結果 |
|---|---|---|---|
| run02 | `writePyramidLevel` の最初の入口 | `.zgroup`、L0〜L5 `.zarray`、完成済みL0チャンク | 8ファイル保持、正常対照の14ファイルと一致 |
| run03 | 3引数 `createPyramidLevels` の入口 | `.zgroup` とL0 `.zarray` | 2ファイル保持、正常対照の14ファイルと一致 |
| run03の別コピー、修正前版 | 同上 | 同上 | L0画素完成後、L1配列を開けず終了1 |

## 保存済みの実停止状態から再開を確認

PowerShellからWSL Ubuntuを実行する。`run06` は未使用のタグにする。下のコマンドは `run02` と `run03` の停止原票・元出力を読み、ハッシュ等を照合して新しいコピーから再開する。GDBの起動や新たな停止は生じない。

```powershell
$r131 = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-interrupted-render01'
wsl -d Ubuntu --exec python3 -B "$r131/run.py" run06 recover
```

`run05/*-origin.json` に元出力の停止時点のSHA-256、時刻、inode、対象PID、GDB終了状態。`run05/*-before-resume.json` と `*-after.json` は再開用の同一コピーの前後。コピー時にDrvFsのmtime精度が秒へ落ちたため、元出力とコピーの同一性にはサイズ・SHA-256、再開時の保持には同一コピー上のmtime・inodeも使う。比較対照は `run02/normal.json` と `run03/normal.json`。`run05/result.json` は全レベルの復号画素ハッシュとOME参照。L0の画素ハッシュは研究129のCT由来出力と一致した。

## 停止の観測と限界

GDBは新規出力に起動した既存ELFだけを追跡した。固定ELFの `nm -C` と `readelf` でnon-PIEの関数入口を求め、all-stopのブレークポイントに到達した時点で `/proc` の実行ファイル・出力引数・PID・namespaceとファイルの状態を確認した。`run.py <未使用タグ> after-l0-chunk` または `before-pyramid-arrays` がその入口。今回の3回の上限を使い切ったため、保存結果の照合は上の `recover` を使う。

1. `run01` はL0完成後の関数入口に到達した。観測スクリプトが `/proc/1/ns/net` の権限エラーで終了した。これを使った再開比較は行っていない。
2. `run02` は比較するnamespaceを起動元自身の値へ変更した。L0完成後の停止原票を保存し、対象PIDへの `os.kill(pid, SIGKILL)` の次のGDB `continue` が `Command aborted` を返した。
3. `run03` はGDBの `signal SIGKILL` に変更した。`/bin/true` ではシグナル終了と回収を表示した。複数スレッドの製品inferiorでは停止原票の保存後、GDBが `Couldn't get registers: No such process` と終了した。

各試行の `*-interrupt.log`、`*-interrupt-process.json`、取得できた `*-at-breakpoint.json` を保存した。`stop.py` は試行間で更新し、1・2回目の各版は別ファイルとして保存していない。2・3回目はブレークポイント時のファイルが元出力にそのまま残り、記録された対象PIDとGDB PIDの消失を確認した。OSの終了シグナルを明示的に採取できたのは `/bin/true` の事前試験。製品は関数入口で実停止し、GDBが異常終了した後の出力から再開した範囲の比較になる。停電、チャンク書込中の停止、複数タイルや複数partでの再開はこの入力では未測定。
