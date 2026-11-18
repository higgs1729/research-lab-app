Status: resolved
担当: 研究

# R006: 101層・bicubicの変更前計時

## 依頼

2026-11-12。検証109の非代表的な分母という指摘と、準備110の入力ゲート通過を受け、次の一件を代表条件の変更前計時とする。最適化製品の実装は今回行わない。対象は110で速度を見る前に固定したPHerc0814 `first-trace-on01/output`、crop `(7356,2272,128,128)`、既定bicubic、level 0、scale 1、101層・step 1。通常stackと `--accum 0.5 --accum-type mean` を測る。全画素が元メッシュ成分0に属する有効な一領域で、64×64の読込タイルは4個。実紙面対応・判読性をこの試験で主張しない。

## 資源と取得

既存R005/R006のbounded runner、幾何・coverage、compile/link原票を再利用する。記録は `experiments/vesuvius/r006/20261112-representative-baseline01`、実行は `D:/kensyoukin-work/r006-representative-baseline01`。旧ソース・ビルド・CT・成果物は非変更。新規CTは110 `run01/analysis01/ct-coverage.json` に列挙した公開S3の8キーだけ、正常取得本文合計16 MiB。保存済み2キーとメタデータを隔離Zarrへコピーし、取得時刻、URL、byte、SHA、失敗を保存する。取得は全体120秒以内、再試行は各キー一度まで、失敗した本文も含めた転送を記録する。未取得やサイズ不一致はfillで進めず停止する。

費用見積は追加のクラウド計算支出 **0円**、新規CT **16 MiB**、隔離CT本文合計20 MiB。GPU・有料基盤・新規依存を使わない。CPU一個、AS4 GiB、最適化ビルド全体300秒、各計測プロセス120秒。6 TU（renderer、reader grid/cache/open/display/image_write）のO3案を借りる。フルReleaseではない残存O0依存と実際のsymbol解決を記録する。上限内で用意できなければ勝手に大規模ビルドへ変えず結果を返す。

## 測定と同一性

- 二モードそれぞれ独立プロセスを3回。各プロセスは同じSurface/Arrayを保持して初回1回と後続2回を描画する。モード順は交互にし、計測のために反復数を増やさない。初回はArray新規、OSキャッシュは制御外。後続は同じArrayに対する実測とし、`Array::stats()` 差分でhit/missの状態を確認する。
- 計時のための変更は観測・同一条件の繰返し・出力先の切替のみ。元のサンプル、演算順、reducer、書出しを保つ。同一プロセスの後続ごとに別出力を作る。保存幾何と実際のraster/中心/offsetを確認し、必要CTキーの事前coverageと実取得を照合する。
- 4タイルの計時はindexごとに独立した記録へ書き、join後に集約する。callerとhelper workerが共に実行できるので、旧1タイル用の共有可変計時状態を流用しない。CPU affinity 1でもタイル壁時間の単純和を短縮量にしない。タイルの開始終了、thread ID、thread CPU、外側request wallを区別する。ログ出力は測定範囲外へまとめる。
- 原R005のrendererで各モードを1回ずつ描画し対照を得る。全計時出力の101 TIFFがモード別の対照と一致することを確認する。これは基準計時の観測が画像を変えていないことの確認で、未実装の再利用案の検証ではない。
- 通常stackは101 offsets、積算は202 offsetsなので二モードの総時間差を幾何削減量として扱わない。積算は404 tile geometry callsと101 centre calls、stackは4と1をコード上の予測として実測する。

## 判定

主判定は、積算の各独立プロセスの初回描画で、各タイルの最初の幾何生成を残して除ける後続100回×4タイルのthread CPU合計が、外側CPUサンプリングrequest wall合計の約10%以上で、反復のばらつきに埋もれないか。同一CPUに固定した幾何計算量の目安であり、実際の壁時間短縮率と呼ばない。後続2回の値、初回CT取得・cache利用、書出し、全プロセス時間を別に提示する。再利用時のcopy/追加allocationの負担を無視した上限側の見積である。

基準を満たさなければこの候補の実装へ進まず、今回の代表的な小領域での負の結果として閉じる。満たした場合も実装採否は主担当が決め、後続の変更前後の実時間比較とXYZ/法線/中心/valid/NaN/丸め前CT/整数画素の一致、独立検証が必要。今回の条件をさらに微調整して閾値を越えるまで試さない。

担当はSol/xhighを選ぶ。既存ハーネスの単純な再実行より、4タイルの並行記録・Array生存期間・最適化依存のlink解決を正しく保つ必要があるため。追加subagentは禁止。依頼を残して結果を本ファイルへ追記し、Statusをresolvedにする。

## 結論（2026-11-12）

［一次］リンク順を是正した計時版で、積算の初回3本は固定基準の約10%をすべて超えた。各タイルの最初の幾何生成を残した後続400回は **71.38〜78.52 ms** のスレッドCPUを使い、外側のCPUサンプリングrequest壁時間の **22.18〜24.97%** を占めた。比率の中央値は24.49%。全18パスのTIFF 1,818枚はモード別に元R005の対照とバイト一致した。[run02生データ集計](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/summary.json) · [元対照のハッシュ](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/control-outputs.json)

| 積算の独立プロセス | 初回の後続400回 幾何CPU ms | 初回のrequest壁 ms | 初回比 | 後続1比 | 後続2比 |
|---|---:|---:|---:|---:|---:|
| 0 | 78.520 | 354.040 | 22.178% | 33.470% | 36.217% |
| 1 | 73.220 | 298.931 | 24.494% | 36.595% | 36.621% |
| 2 | 71.380 | 285.848 | 24.971% | 36.312% | 35.824% |

［推論］同じ1 CPUで再生成を省く場合の上限側の目安として、初回3本の観測ばらつきの範囲でも基準を上回った。再利用時のcopy・追加allocationを含む壁時間差と、実装後の内部幾何・丸め前CTの一致は別に検証する。ここでの判定範囲は固定の128×128・101層・ローカルCT。実装採否は主担当が独立検証を受けて判断する。

## 是正後の計時と根拠

［一次］run02では、既存の6 O3オブジェクトを再コンパイルせず、readerの5オブジェクトをリンク入力の先頭へ移した。逆アセンブルで、O3の `resampleRows` がO3 `grid::point` を呼び、その本体にHermite演算が展開されていることを確認した。ローダーはこの `point` とArray/cacheの主要関数を新readerに解決し、後者の提供元はO3 `cache.cpp.o` だった。platform I/Oの一部は旧O0オブジェクト、coreや外部ライブラリは元のビルドを使用した。[リンク・コンパイル引数](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/build-settings.json) · [幾何の実呼出し](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/geometry-link.json) · [Array/cacheのリンクマップ](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/link-map-selection.json) · [ローダー記録](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/loader-resolution.json)

［一次］全パスのraster・中心XYZ・offset・チャンクキーが固定入力と事前coverageに対応した。積算は202 offsets、タイル幾何404回・中心101回。通常stackは101 offsets、タイル幾何4回・中心1回。両モードは別のプロセスで3回ずつ、順序は交互。各プロセスの3パスで同一Surface/Arrayを保持した。積算の初回は11〜12ディスクヒット・1,069〜1,070メモリヒット、後続は全パス0ディスクヒット・1,081メモリヒット。stackは初回11〜12ディスクヒット・8〜9メモリヒット、後続は0ディスクヒット・20メモリヒット。ディスクヒットには同一キーの並行取得が含まれ得る。全パスで10種類の実キーを確認した。OSのファイルキャッシュ状態は制御外。[生ログ例](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/accum-0.log) · [キャッシュ・呼出し集計](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/summary.json)

各段階の3プロセスの中央値。単位はms。CT CPUはチャンク取得を含む。TIFF壁はセットアップ、タイル書込、完了処理の合計。

| モード・パス | request壁 | 幾何CPU | CT CPU | うちArray取得CPU | TIFF壁 | パス全体壁 |
|---|---:|---:|---:|---:|---:|---:|
| stack 初回 | 98.775 | 0.731 | 58.384 | 16.856 | 403.132 | 514.880 |
| stack 後続1 | 43.431 | 0.680 | 40.794 | 0.042 | 405.597 | 460.527 |
| stack 後続2 | 43.102 | 0.684 | 40.458 | 0.036 | 417.017 | 472.091 |
| 積算 初回 | 298.931 | 73.873 | 144.933 | 20.839 | 520.786 | 834.346 |
| 積算 後続1 | 195.607 | 71.718 | 118.930 | 0.909 | 466.904 | 675.532 |
| 積算 後続2 | 193.691 | 70.828 | 118.101 | 0.912 | 412.032 | 618.769 |

［一次］描画プロセス全体の壁はstack 1.735〜1.835秒、積算3.089〜3.737秒。4タイルでは呼出し側と補助workerが交代して実行し、計測区間の重なりを生ログと集計に保存した。積算初回のタイル壁の重複は115.47〜165.24 ms。主判定の分子にはタイルのスレッドCPU時間だけを使い、モード間の総時間差は算入していない。[全実行の計時・資源](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/summary.json)

［一次］D:の復帰後、旧CT、6オブジェクト、元対照202枚を再ハッシュし、D:を既存入力の読み取りに限定した。run02の新バイナリ・TIFF・一時ファイルはC:へ出力した。保護対象395ファイルの前後SHA-256は一致。再リンク全体21.302秒、最大RSS 525.68 MiB。描画6プロセスの壁合計15.612秒、最大RSS 96.83 MiB。CPU 0、AS 4 GiB、各描画120秒上限。初回の新規取得は16 MiB、再計時では転送0バイト、追加支出は全体で0円。C:出力へ移したため、run01とrun02のTIFF・プロセス壁時間の差はリンク是正の効果の算定から除外した。[復帰時の判断と照合](../experiments/vesuvius/20261112-storage-restored01/source-check-and-decision.json) · [run02入力の照合](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/reuse-input.json) · [run02資源集計](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/summary.json)

## 初回ビルドの診断（2026-11-12）

［一次］予定の6 TUはGCC 13でO3コンパイルできた。初回の混在ビルドは、積算の後続400回の幾何で1.519〜1.659秒のスレッドCPU、hostサンプリングrequest壁比87.10〜88.12%を記録した。全18計時パスのTIFF 1,818枚は元R005のモード別対照と一致した。[run01集計](../experiments/vesuvius/r006/20261112-representative-baseline01/run01/summary.json)

［一次］リンクマップでは `grid-grid.cpp.o` のO3 `grid::point` が破棄され、先に現れる旧 `projection/mask.cpp.o` のO0 `grid::point` とHermite関数が採用された。逆アセンブルと `addr2line -i` は、O3のSurfaceコールバックに展開された `resampleRows` が `point@plt` を呼び、選ばれたO0 `point` が `hermite@plt` を呼ぶことを示した。ローダーは両シンボルを新しい共有lib内の旧オブジェクト由来のアドレスに解決した。Array/cacheの主要関数は新しいO3 `cache.cpp.o` だった。87〜88%はこの混在ビルドの診断値として保存した。[幾何の実呼出しとO0原票](../experiments/vesuvius/r006/20261112-representative-baseline01/run01/geometry-link.json) · [Array/cacheのリンクマップ](../experiments/vesuvius/r006/20261112-representative-baseline01/run01/link-map-selection.json)

主担当がO0の提供元を独立に確認し、同じ6 TUの既存オブジェクトを使い、readerのリンク順でO3オブジェクトを前に移す隔離run02を承認した。上限は再リンク全体60秒。入力・計時・出力照合の条件を固定し、元の対照TIFFとCTを再ハッシュして使用する。[是正の決定記録](../experiments/vesuvius/r006/20261112-representative-link-correction/record.json)

## メモ

- 2026-11-12。固定した8 URLは各1回の取得で成功。旧CTの2キーと4メタデータを照合して隔離Zarrへコピーした。
- 2026-11-12。予定の6 TUをO3で隔離ビルドした。対照と計時版のreader解決を分けて確認し、stack・積算を交互に各3プロセスで実行した。
- 2026-11-12。再リンクハーネスの最初の起動では、研究108の同名集計モジュールが先に解決され、作業先を作る前に停止した。importの順序を修正して起動した。[起動エラー](../experiments/vesuvius/r006/20261112-representative-baseline01/relink-startup.log)
- 2026-11-12 17:22 JST。修正後は作業先の作成時にWSLで `Errno 22` が出た。WindowsからD:が見えず、WSLの `/mnt/d` にも元の作業先がなかった。Disk 1のI/O再試行とUASPリセットが同時期に記録されていた。この起動はrun02の再リンク・描画を始める前に止まり、D:の復帰まで中断した。run01の実行票21件は終了と回収済みを確認した。[エラー原票](../experiments/vesuvius/r006/20261112-representative-baseline01/relink-drive-unavailable.log) · [ホストのディスク状態](../experiments/vesuvius/r006/20261112-representative-baseline01/relink-drive-unavailable.json) · [中断時のC:側の根拠とプロセス票](../experiments/vesuvius/r006/20261112-representative-baseline01/c-drive-manifest.json)
- 2026-11-12 21:42 JST。D:復帰後の照合では、最初の確認で6つのコンパイル単位名をファイルパスとして扱った。コンパイル引数の `-c` から実ソース6件を取り直し、先に照合済みの308実パスと合わせて不一致0を確認した。D:はボリューム警告が残るため読み取りに限定し、C:の隔離先でrun02を実行した。[復帰時の照合補正と判断](../experiments/vesuvius/20261112-storage-restored01/source-check-and-decision.json)
