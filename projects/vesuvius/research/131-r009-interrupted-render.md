Status: resolved
担当: 研究（R131担当 2026-11-13）
Blocked by: 130

# R009: 実際に中断したCT描画を再開すると正常出力へ戻るか（2026-11-13）

## 依頼

本人は公開済み三件の改善を深掘りして評価を高められるか相談し、その後リセットからの再開を指示した。R009は人工的に準備した途中状態からの再開を確認済みだが、実際の描画プロセスの中断は未確認。研究129/130で得たPHerc0139 w035の固定64×64×28層CT入力を使い、R007・R009を結合した既存の製品バイナリで、正常実行と実際に停止した出力からの再開を一件比較する。新しい応募項目を増やす目的ではなく、同じR009の実利用に近い根拠を補う問い。

研究130の完了後に着手する。入力の原票・基準画素は `experiments/vesuvius/r012/20261113-known-ct-control01/`、既存の結合版とビルド情報は `experiments/vesuvius/r009/20261113-pyramid-metadata01/` とC:の対応作業先。過去の正常出力と部分状態の検証は研究121〜125。これらは例として使える。固定の元CT・面を再取得せず、小領域のまま実行する。公開サーフェスとの完全一致や文字判読の証明にはしない。

欲しい判定は、実CT→Zarr出力を正常実行した対照と、実行中のプロセスを制御して強制終了し、保存された途中出力をそのまま `--resume` した結果との、実配列・全層画素・OME参照の一致。中断前に完成していたL0チャンクと配列メタデータの保持も調べる。正常対照を削って作った状態を、実際のプロセス中断と扱わない。root目録や下位ピラミッドの再計算は既存仕様と区別する。

既存のCLI・保存方式を確認し、少数チャンクの状態を確実に観測できる最小の方法を選ぶ。タイミングの成立・失敗も記録し、出力先と自分が起動したPID/プロセスグループだけを扱う。単なる経過時間で繰り返し乱打して成功例を選ばない。中断時のファイル存在・サイズ・ハッシュとどこまで書込みが完了したかを保ち、再開前の状態をコピーで保存する。SIGKILL等の試験上の停止を、実際の停電や全種のクラッシュ耐性に一般化しない。

画素やメタデータの不一致が出れば、まず既存出力と再開ロジックのどの段で起きたかを特定し、再現資料と最小の次案を返す。この票で配布パッチや公開repoを黙って改変しない。既存製品の修正が必要な場合は、主担当が次の一件として選ぶ。中断箇所を観測するために追加実装/ビルドが必要なら、既存能力で代替できない理由と最小案を先に親へ返す。

新規データ取得・モデル取得・推論・GPU・有料計算なし。ローカルCPU1、AS4GiB、個々のネイティブ処理300秒以内。新規作業量128MiB、正常対照と中断/再開を中心とする少数の実行に限定し、中断機構の試行は最大3回を初期上限とする。D:は読み取りだけ。新規出力は `experiments/vesuvius/r009/20261113-interrupted-render01/` とC:の独立作業先。凍結済み出力・配布候補は変更しない。外部連絡・公開・応募・追加subagentは禁止。

モデル/effortはgpt-6.1-sol / xhigh。既存の入力・修正版・比較手順を借りる一方、実中断を観測して部分保存と再開を区別する測定方法は未確立のため。依頼は凍結し、再現手順、終了状態、原票、費用、限界を追記して結果を親へ返す。重要な成功主張には別担当の検証を主担当が選ぶ。

## 結論

[一次・実行] PHerc0139 w035の64×64×28層の実CT描画を、既存のR007/R009結合版で二つの関数入口に停止した。異常終了後に残った実出力のコピーを `--resume` し、両方とも正常対照の14ファイルとSHA-256、L0〜L5の全層画素、OMEの実配列参照が一致した。L0チャンク完成後の状態では既存8ファイル、L0配列作成直後の状態では既存2ファイルを、再開用コピー上でSHA-256・mtime・inodeまで保持した。[実行結果](../experiments/vesuvius/r009/20261113-interrupted-render01/run05/result.json)

[一次・実行] L0配列作成直後の同じ停止出力を修正前版へ渡すと、L0チャンクを正常対照と同じ値で保存した後、欠けたL1配列を開けず終了1だった。結合版は欠けた下位配列を補って完走した。GDBの異常終了後に対象PIDとGDBの消失、および停止時のファイルが残ったことを確認した。製品プロセスのOS終了シグナルは確定できなかった。[修正前ログ](../experiments/vesuvius/r009/20261113-interrupted-render01/run05/old-resume.log) · [停止・再開の原票](../experiments/vesuvius/r009/20261113-interrupted-render01/README.md)

## 根拠・詳細

### 固定入力と停止方法

- [一次] 研究129の元CT 2チャンク、CTメタデータ、公開TIFXYZ全体をハッシュ照合し再利用。公開座標 `(x=2176,y=1408)` の64×64、28層、CT L0、scale 1、bicubic、三線形CT、flip-normals、9.362 µm。今回はZarrのみ、無圧縮uint8、ピラミッド有効。固定64×64ではL0全体が1チャンクになる。正常対照のL0は研究129の元CT描画出力と全値一致した。[入力とELFのハッシュ](../experiments/vesuvius/r009/20261113-interrupted-render01/run03/inputs.json) · [正常対照](../experiments/vesuvius/r009/20261113-interrupted-render01/run03/normal.json)
- [一次] 既存R123の結合ELFをGDBから自分の新規出力へ起動。non-PIEの関数入口でall-stopとし、停止中に対象PIDの実行ファイル、出力引数、`tracing stop`、namespace、バックトレース、ファイルを記録。L0完成後は `writePyramidLevel` 入口、下位配列作成前は通常描画の3引数 `createPyramidLevels` 入口で止めた。正常対照のファイルを削る操作は行わず、失敗試行を含め停止機構は3回で打ち切った。[L0完成後の停止原票](../experiments/vesuvius/r009/20261113-interrupted-render01/run02/after-l0-chunk-at-breakpoint.json) · [下位配列作成前の停止原票](../experiments/vesuvius/r009/20261113-interrupted-render01/run03/before-pyramid-arrays-at-breakpoint.json)

### 再開と保持

| 実出力の停止時点 | 再開前に実在したファイル | 結合版の再開 |
|---|---|---|
| L0完成後、下位画素計算前 | `.zgroup`、L0〜L5 `.zarray`、L0チャンク（114,688 B） | 8ファイル保持。L1〜L5のチャンクと `.zattrs` を作成。正常対照と一致 |
| L0配列作成後、下位配列作成前 | `.zgroup` とL0 `.zarray` | 2ファイル保持。L1〜L5配列、L0〜L5チャンクと `.zattrs` を作成。正常対照と一致 |

[一次・実測] 停止中のハッシュ・サイズ・mtime・inodeが異常終了後の元出力にそのまま残った。`copy2` でコピーした時点でDrvFsがmtimeの小数部を落とした。元出力と保存コピーはサイズ・SHA-256・配列内容で照合し、保持のmtime・inodeは再開用の同一コピーの前後で測った。rootのOME属性は両停止時に未作成で、再開後に生成した。下位画素の生成は既存のピラミッド処理。修正固有の差は、L0だけが初期化された状態から下位配列を作れたことにある。[元出力照合と再開結果](../experiments/vesuvius/r009/20261113-interrupted-render01/run05/result.json) · [修正前に残った配列](../experiments/vesuvius/r009/20261113-interrupted-render01/run05/old-after.json)

### 停止観測の範囲

[一次] 試行1はL0完成後のブレークポイントに達したが、GDB内の `/proc/1/ns/net` 読取権限エラーで停止原票を作れなかった。試行2は対象のnamespaceを起動元の値と比較し、対象PIDへ `os.kill` を発行後、GDBの `continue` が `Command aborted`。試行3は `signal SIGKILL` に切り替え、`/bin/true` では終了シグナルと回収を表示したが、製品は `Couldn't get registers: No such process`。停止時点のファイル記録とGDB回収、対象PID消失は試行2・3で確認した。`stop.py` の過去2版は別ファイルとして保存していない。停止の信号種別をOS終了状態で確認した製品試験、停電、チャンク途中書込み、複数タイル・partの挙動は未確認。[試行1](../experiments/vesuvius/r009/20261113-interrupted-render01/run01/after-l0-chunk-interrupt.log) · [試行2](../experiments/vesuvius/r009/20261113-interrupted-render01/run02/after-l0-chunk-interrupt.log) · [試行3](../experiments/vesuvius/r009/20261113-interrupted-render01/run03/before-pyramid-arrays-interrupt.log) · [再現手順](../experiments/vesuvius/r009/20261113-interrupted-render01/README.md)

## 資源

2026-11-13 JST。CPU affinity 1、OpenMPと数値スレッド上限1、AS 4 GiB、core dump 0、`unshare -Urn`、各300秒上限。既存の製品readerは補助スレッドを生成し、GDB停止中のinferiorは15スレッドと記録された。並列CPU利用はaffinityで1 CPUに固定。正常対照は0.527〜0.585秒、結合版再開2件0.423・0.472秒、修正前版0.321秒。正常3回・GDB停止3回・再開3回の計測壁時間20.69秒、最大RSS638,099,456 B（GDB込み）。C:の作業出力・原票は約1.5 MB。新規ビルド、データ取得、クラウド支出は0。別担当による確認は主担当へ引き継ぐ。[資源ログと再現手順](../experiments/vesuvius/r009/20261113-interrupted-render01/README.md) · [lab登録候補](../experiments/vesuvius/r009/20261113-interrupted-render01/record.json)

## メモ

- 既存R123結合ELFのSHA-256とネイティブ関数アドレスを確認した。既存GDBの関数入口停止を使い、L0画素完成後と、L0メタデータ完成後・下位配列作成前の2境界を調べる。出力チャンクや配列を人為的に削らない。
- GDBの3試行を保存した。試行2・3の停止原票に対応する実出力が残ったため、上限に達した後は停止試験を追加せず、保存コピーを再開した。初回コピー照合はDrvFsのmtime精度で停止し、`run04` に保存した。`run05` は元との内容同一性と、同一コピー上でのmtime保持を別々に照合した。
