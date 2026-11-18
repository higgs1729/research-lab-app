Status: resolved
担当: 検証

# R006: 是正した101層基準計時の独立検証

## 依頼

2026-11-12。研究111のrun02を、実装担当とは別の担当で検証する。対象は固定crop `(7356,2272,128,128)`、既定bicubic、101層、通常stackとmean積算0.5。今回の目的は、製品最適化へ進む判断に必要な基準計時の根拠を確かめること。新規ビルド・描画・ダウンロードや製品変更は行わない。

生ログから各プロセス・各パスのrequest壁、後続400幾何生成のthread CPU、キャッシュhitと呼出し数を独立に集計する。4タイルの重なる壁時間を加算して短縮量にしていないこと、同一Surface/Arrayの3パス、交互3プロセスずつ、CPU1とAS4GiB、全終了・回収を確認する。22.18〜24.97%の値がrequest壁を分母とする上限側の目安で、全体短縮率ではないことを判定する。

実際のmap・ELF・逆アセンブル・ローダー記録を照合し、O3 gridのpointとその中のHermite展開、O3 cache/Arrayの提供元を確認する。フルReleaseではない制限を記録する。通常stackと積算はoffset数が異なるのでモード間の時間差を高速化とは扱わない。

観測差分がサンプル演算・reducer・書出しを変えていないこと、実際のraster・中心・offset・キーが研究110の固定入力に対応することを確認する。計時TIFF 1,818枚の実ファイルをモード別の元対照202枚とハッシュ比較する。保存されたprotected前後を照合し、重要な入力・O3 object・ライブラリの現在SHAを再確認する。D:は既存入力の読み取り専用扱いとし、出力は新しいC:実験フォルダへ保存する。run01/run02原票は非変更。

実行環境はWSL distro名 `Ubuntu`。計時プログラムと出力は `C:/dev/kensyoukin/.work/r006-representative-baseline01/run02`、原票は `experiments/vesuvius/r006/20261112-representative-baseline01/run02`。D:からC:への出力先変更があるため、run01対run02の総時間差をリンク是正の性能効果として使わない。新規支出0円、CPU1、AS4GiB、検証スクリプトの実行上限120秒。追加subagentは禁止。

担当モデル/effortはSol/highを選ぶ。既存の原票と小領域の固定条件があり、独立集計・呼出し経路の確認にはコードの解釈が必要だが、新しい最適化設計は不要なため。検証結果と資源、失敗を本ファイルへ追記してresolvedにする。問題があれば原因・主張への影響を示し、別研究へ進まない。

## 結論（2026-11-12）

［一次］是正run02で、各タイルの初回を残した後続400回の幾何生成は、初回パスで **71.380〜78.520 ms** のthread CPUを使用した。各プロセスのrequest壁時間に対する比率は **22.178〜24.971%**、中央値 **24.494%**。同じArrayを使う後続6パスでは **33.470〜36.621%**。実ファイルから計時TIFF **1,818枚** と元対照 **202枚** を再ハッシュし、対応するモードと層ですべて一致した。実ELF・map・逆アセンブル・保存ローダー記録から、O3の点補間とその内部のHermiteインライン展開、O3のArray/cache提供元を確認した。[独立検証結果](../experiments/vesuvius/r006/20261112-representative-baseline-verification01/run-01/result.json)

［推論］固定した101層・bicubic・128×128の入力では、初回の全3プロセスが事前の約10%の実装検討基準を超えた。この比率は1 CPUで再生成を全て省いたときの、外側request壁時間に対する上限側の目安。再利用のコピー・割当・アクセスの負担や、書出しまで含めた製品の短縮率は変更前後の計時で評価する。実装採否は主担当の判断に委ねる。

## 生ログ・固定入力・画像

［一次］集計済みの `summary.json` を入力にせず、6本の生ログから各パスのrequest開始と終了を引き、幾何thread CPUは各requestのタイル別記録から取得した。各パスの最初の4タイル分を残し、残り100要求×4タイルのCPU時間を合計した。

| 積算プロセス | 初回の後続400回 幾何CPU ms | 初回request壁 ms | 初回比 | 後続1比 | 後続2比 |
|---|---:|---:|---:|---:|---:|
| 0 | 78.520 | 354.040 | 22.178% | 33.470% | 36.217% |
| 1 | 73.220 | 298.931 | 24.494% | 36.595% | 36.621% |
| 2 | 71.380 | 285.848 | 24.971% | 36.312% | 35.824% |

［一次］各パスでrequest区間は直列で、4タイルの区間はそれぞれrequest内に収まる。積算初回では、タイル壁の和と区間の和集合との差が115.472〜165.242 msあった。集計に使った壁時間は外側requestの和、幾何の分子はタイルを実行したスレッド自身のCPU時計。callerと補助workerの2スレッドはCPU 0の上で交代実行できる。`native.environment()` が起動元でCPU affinityとAS 4 GiBのhard/soft limitを設定し、子プロセスが継承する。各モード3本をstack、積算の交互に逐次実行し、開始・終了時刻、別PID、120秒以内、終了0・回収済みを6本すべてで確認した。プロセス票のRSS・CPU値はGNU time原票と一致した。[環境](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/environment.json) · [生ログ例](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/accum-0.log)

［一次］各プロセスの3パスでSurface/Arrayのアドレスは同じで、パス間の `Array::stats()` は連続していた。全パスで10種類のCTキーが出現。各requestの実キーは、そのoffset群に対する研究110のcoverageに含まれた。積算は各パスの101 request・101中心・404タイル幾何、stackは1 request・1中心・4タイル幾何。積算の各パスの `Array::chunk` は1,081回で、初回はディスク11〜12・メモリ1,069〜1,070ヒット、後続はディスク0・メモリ1,081ヒット。stackは20回で、初回はディスク11〜12・メモリ8〜9ヒット、後続はディスク0・メモリ20ヒット。ディスクヒットは取得したユニークキー数と区別した。OSのファイルキャッシュは制御されていない。[固定coverage](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/analysis01/ct-coverage.json)

［一次］保存幾何バイナリのSHA・raster・XYZ/法線16,384組の有限性、実requestのrasterと中心XYZを照合した。cropは `(7356,2272,128,128)`、既定bicubic、level 0・scale 1。中心XYZは約 `(3337.170410, 3020.873535, 2524.301514)`。stackは−50〜50の101 offsets、積算は各出力層に整数offsetとその+0.5を与える202 offsets。事前coverage、幾何判定、取得記録のSHAとローカルCT 10ファイル・メタデータ4ファイルの現在SHAを確認した。[固定幾何](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/analysis01/geometry-gate.json) · [CTの保存記録](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/fixture.json)

［一次］元ソースに保存された `grid.patch` と `vc_render_tifxyz.patch` を標準出力に適用し、O3オブジェクトのコンパイルに使ったソースとバイト一致した。差分は時計、タイルごとの記録、計測用の不足チェック、スレッド条件、Surface/Arrayの保持、3パスと出力先の切替を追加し、対象条件のサンプル演算、reducer、画像変換・TIFF書出しの処理を保っていた。タイマーと記録の負担は計測に含まれる。同モードのR005元対照各101枚と、6プロセス×3パス×101枚の実TIFFが一致した。未実装の幾何再利用については、内部のXYZ・法線・中心・valid/NaN・丸め前CT値の照合が別途必要。[grid差分](../experiments/vesuvius/r006/20261112-representative-baseline01/run01/grid.patch) · [renderer差分](../experiments/vesuvius/r006/20261112-representative-baseline01/run01/vc_render_tifxyz.patch)

## リンクと適用範囲

［一次］run02の保護対象395ファイルの保存前後SHAは一致。既存のO3オブジェクト6個、各TUのソース、CT、元対照、旧core・reader共有ライブラリ、run02の実バイナリ・reader・mapの現在SHAを再確認した。readerのmapとELF動的シンボルを照合すると、Surface版 `grid::sample` と `grid::point` は先頭側に移したO3 `grid-grid.cpp.o` が提供。Surfaceコールバック内の `resampleRows` から `point@plt` を呼び、保存されたローダー診断はrun02のreader内の同シンボルへ解決している。点補間本体の `vmulss` の `addr2line -i` で `hermite` から `point` へのインラインフレームを確認した。点補間本体の外部callは `sqrtf@plt` のみで、旧O0由来の独立 `hermite` シンボルはELFに残る。`Array::chunk`、`Array::read_layer_chunk`、`MemoryCache::get/put` はいずれも新readerのO3 `cache.cpp.o` へ解決した。ローダー診断の原票は `LD_BIND_NOW=1` の `--help` 起動で、描画時の経路は計時行・実バイナリと合わせて確認した。[リンクの独立照合](../experiments/vesuvius/r006/20261112-representative-baseline-verification01/run-01/result.json) · [ローダー原票](../experiments/vesuvius/r006/20261112-representative-baseline01/run02/bindings-timing.log)

［推論］platform I/Oの一部、元core、外部ライブラリなどを借りた混在ビルドなので、フルReleaseの時間は未測定。積算はstackの2倍のoffsetを評価するため、モード間の総時間差は幾何削減量に含めない。run01とrun02では出力先のドライブも違うため、総時間差からリンク是正による速度差を算定しない。

## 検証の資源

［一次］WSL Ubuntuでネットワーク隔離、CPU 0、AS 4 GiB、最大120秒の読取検証を1回実施。壁8.08秒、user/system CPU 1.02/0.59秒、最大RSS 111,352 KiB、終了0、追加費用0円。新規ビルド・描画・取得は行わなかった。D:は読取だけで、出力はC:の新規フォルダに保存した。事前参照で研究110のファイル名を一度取り違えたため、`rg --files` で実名を確認して読み直した。検証スクリプトは初回で完了した。[再検証手順](../experiments/vesuvius/r006/20261112-representative-baseline-verification01/README.md) · [資源原票](../experiments/vesuvius/r006/20261112-representative-baseline-verification01/run-01/time.txt) · [SHA-256](../experiments/vesuvius/r006/20261112-representative-baseline-verification01/run-01/SHA256SUMS)
