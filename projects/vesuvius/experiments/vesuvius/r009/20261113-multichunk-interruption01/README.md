# R009 二つのL0チャンクでの停止・再開

固定PHerc0139 w035と9.362 µmのCTレベル0を使った。crop XYWHは (2239, 1343, 1, 129)、28層、step 1、scale 1、bicubic、flip normals。出力はZarr v2無圧縮uint8のみ。研究156が固定した既存2キーとR123結合ELF、入力13件をSHA-256照合した。 [固定候補](../20261113-multichunk-feasibility01/candidate03.json) · [入力原票](run01/inputs.json)

保存出力は C:/dev/kensyoukin/.work/r009-multichunk-interruption01/run01/ の normal.zarr、stopped.zarr、resumed.zarr。stopped.zarr は実際に止まった現物。コピーだけを再開した。照合・再集計に使うときは、この3本を読み取り専用として扱う。

| 起動 | 終了値 | 壁時間 |
| --- | ---: | ---: |
| 正常 | 0 | 0.573秒 |
| GDB停止 | 1 | 6.029秒 |
| 保存コピーから再開 | 0 | 0.370秒 |

GDBは0x62afeeで停止し、AL=1、対象ELFと全引数、PID、tracing stop、別のネット名前空間を確認した。第1チャンク、.zgroup、L0〜L5の.zarrayの8ファイルだけが存在し、各ファイルのSHAとサイズは正常対照と一致。第2キー、下位画素、root .zattrs、一時ファイルはなかった。R131の停止スクリプトを呼ぶとGDBはレジスタ取得エラーで終了した。対象とGDBのPIDの消失、および停止出力のハッシュ・mtime・inodeの保持を確認。OS終了シグナルは未確定。 [停止原票](run01/at-breakpoint.json) · [レジスタと引数](run01/return-register.json) · [終了原票](run01/stopped.json)

再開コピーの前後で既存8件のサイズ・SHA・mtime_ns・inodeを保持。第2キーが新設され、正常対照と全15ファイルのサイズ・SHA、全6レベルの論理uint8値、実配列メタとOMEが一致した。L0のshapeは[28,129,1]、chunksは[28,128,1]。第2キーは28個の非ゼロ論理値と3,556 Bのゼロpadding。 [再開前](run01/before-resume.json) · [再開後](run01/after-resume.json) · [結果](run01/result.json)

## 実行条件

以下は実施コマンド。run01は凍結済み。別の実行が必要になった場合は未使用のタグを使う。

~~~powershell
wsl -d Ubuntu --exec python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-multichunk-interruption01/run.py run01
~~~

R131の引数生成・制約・停止スクリプトと既存boundedランナーを再利用した。CPU affinity 1、数値スレッド上限1、AS 4 GiB、core 0、unshare -Urn。各最大60秒、合計180秒。正常・停止・再開は各1回。初回はラッパーが既存モジュールのimportで止まり、プロセス起動前に修正した。 [環境](run01/environment.json) · [初回のimport停止](preflight-import.log)

下位配列のメタデータは停止時に存在した。旧版にも既存L0のスキップがあるため、今回の結果は二つのL0ブロックでの保持と完走の確認。停電、書きかけのチャンク、複数partや同時書込みは未試験。
