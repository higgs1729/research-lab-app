Status: resolved
担当: 検証

# R006: 幾何再利用のCPU試作を独立検証する

## 依頼

2026-11-12。研究113のCPU試作について、実装担当とは別に正しさと性能解釈を確認する。試作は非公開のPreparedSurface入口であり、公開可能な製品や11月応募への採用をこの検証だけで認定しない。

対象は `experiments/vesuvius/r006/20261112-geometry-reuse01`。製品差分と観測差分を分けて読む。固定Surface/Rasterと寿命、immutable入力、tile別の並行書込み、needNormals別キャッシュ、NaN中心、ゼロのみoffset、CTサンプリング・集約の演算順、CUDA付き要求の元経路を確認する。計時無効時のtrace負担が両経路で共通で、初回の準備・allocationをsampling区間に含めているか調べる。

保存生ログからoff/on各3プロセス×3パスを独立に集計する。主値は初回sampling中央値と各ペア、後続1/2、パス・プロセス全体、メモリ。cold/warmを混ぜた9パス中央値を主結果にはしない。研究111の細かい観測付き時間をbeforeとして使っていないこと、固定条件からの変更が無いこと、build失敗を含む資源上限を確認する。

実ファイルの幾何・法線・中心・offset・丸め前の集約画素・level記録とTIFFがoff/onおよび元対照と一致することを確認する。既存の合成チェックをCPU1/AS4GiBで一度だけ再実行し、退化法線でのゼロoffset、NaN中心、境界やpartial tile、flipの意味を保持しているか確認する。元の実験フォルダへ上書きしない。追加の大規模描画・ビルド・CT取得は行わない。O3提供元は新試作のmap/ELFと保存loaderから確認する。

現在の主張は初回サンプリングの約19.73%短縮、後続約25.56/32.21%短縮。全体プロセス中央値3.044→3.040秒で範囲が重なるため、実用全体時間の改善は未確認とする。各数字を独立に確かめ、未確認点・問題があれば具体的な根拠を残す。

新しい検証出力はC:、D:読み取りのみ。追加支出0円。検証実行CPU1/AS4GiB/120秒以内、追加subagent禁止。モデル/effortはSol/highを選ぶ。固定した比較と生ログがあり、主な仕事はコード解釈・独立計算で、新しい最適化設計は不要なため。依頼を残して結果と資源を追記しresolvedへ更新する。

## 結論（2026-11-12）

［一次］同一O3試作バイナリのoff/onを生ログから再集計した。準備と整数変換を含む初回サンプリングは中央値 **341.940 → 274.492 ms（19.725%短縮）**。初回の3組は8.189%、19.725%、15.500%短縮で、すべて非悪化だった。後続1と後続2の中央値はそれぞれ25.565%、32.211%短縮。元対照と計時TIFF 1,818枚・詳細観測TIFF 202枚がバイト一致した。［推論］固定入力でサンプリング中央値10%以上、初回各組非悪化、出力一致の試作基準を満たした。[独立集計](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/audit-03/measurements.json)

［一次］全プロセス壁は中央値 **3.044483 → 3.040329秒**。範囲はoff 3.038761〜3.093475秒、on 2.987584〜3.094510秒と重なり、初回パス全体の中央値は940.870 → 957.732 msだった。［推論］この観測では実用上の全体時間の改善は未確認。適用範囲は固定した128×128、既定bicubic、CPU・uint8・101層・mean積算0.5の試作。公開APIや応募採用の判定は別に必要。[各プロセス原票の独立集計](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/audit-03/measurements.json)

## 測定範囲と性能

［一次］実行引数を研究111 run02の固定条件と照合し、実行バイナリと出力先以外が同じと確認した。測定はoff→onの交互3組を1プロセスずつ実行し、各プロセスの3パスでSurface/Arrayのアドレスとcacheカウンタが連続した。性能計時6本は初回がメモリ1,069・ディスク12ヒット、後続はいずれもメモリ1,081・ディスク0。OSのファイルキャッシュは制御されていない。off/onの差は同じ試作バイナリでの切替で、研究111の細かい観測付き時間は比較式に使わなかった。全6本が120秒以内に正常終了して回収され、CPU 0・AS 4 GiBは起動元の設定から継承された。[実行順](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/measurement-order.json) · [環境](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/environment.json)

［一次］時間は3プロセスの中央値、単位はms。短縮率は各状態のoff/on中央値から計算した。TIFF壁は作成、書込、終了処理の合計。

| Array状態 | サンプリング off → on | 短縮 | TIFF off → on | パス全体 off → on |
|---|---:|---:|---:|---:|
| 初回 | 341.940 → 274.492 | 19.725% | 598.401 → 682.841 | 940.870 → 957.732 |
| 後続1 | 220.177 → 163.889 | 25.565% | 658.033 → 688.443 | 901.864 → 867.121 |
| 後続2 | 244.262 → 165.583 | 32.211% | 641.671 → 655.607 | 886.037 → 823.233 |

［一次］初回の組別サンプリングは294.204→270.110、341.940→274.492、359.420→303.708 ms。最大RSSはoff 94.422〜96.504 MiB（中央値96.383）、on 96.238〜96.711 MiB（中央値96.531）。初回と後続ではArrayの状態が違うため、両方を混ぜた9パス中央値は主判定に使っていない。[全反復と資源](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/audit-03/measurements.json)

［一次］`samplesStart` は積算分岐より前で、`PreparedSurface` の構築、中央取得、各タイルの遅延初期化と割当、全サンプル、`toImage`、分岐スコープ終了時のバッファ破棄までを囲む。共通のSurface/raster構築は区間外。詳細観測を無効にした両経路は同じ `is_open()` 判定を通り、tileのtraceポインタ判定は残るが、詳細用の割当・copy・出力は行わない。粗い計時とcache statsの読み取りは両経路で共通。観測上の短縮は幾何の再生成と反復バッファ割当の削減を含む。[共通計時差分](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/measurement.patch)

## 正しさと並行実行

［一次］元ソースに製品側の試作差分を適用した結果が保存された `product` ソースと一致し、そこに観測差分を適用すると実コンパイルソースに一致した。`PreparedSurface` は一つのrenderer出力タイルの積算分岐でだけ生存し、コピーした固定Rasterと読み取り専用のSurface参照を持つ。rendererがSurfaceとその頂点・有効マスクの所有元を保持する。その間、入力の書換えは見当たらない。`centre_` の `optional` は値の有限性と別に初期化済みを表し、法線を要求せず求めたNaN中心もそのまま保持する。`needNormals` ごとにXYZと法線のキャッシュを分けるため、退化法線を持つ点でゼロのみのoffset要求の有効性を保つ。[試作差分](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/reuse.patch) · [私用ヘッダー](../experiments/vesuvius/r006/20261112-geometry-reuse01/reuse_geometry.hpp)

［一次］キャッシュ外側のvectorは `parallel_for` より前にresizeする。既存ThreadPoolは各indexをatomicで一度ずつ割り当て、完了待ち後に戻る。workerは別々のタイル要素と観測用の別画素範囲に書き、後続requestは直列で再利用する。これは現在の呼出し側と不変入力の下での確認。同じ `PreparedSurface` への同時requestや、参照元頂点の並行更新を許す同期は持たない。計算済みバッファへの切替以降のCTの位置・補間・reducerの演算順は共通で、CUDA readerを持つlevelがあれば元の `grid::sample` へ戻す。CUDA実機経路の再実行は今回の範囲外。通常stack・compositeは従来の入口を通る。[試作差分](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/reuse.patch)

［一次］観測off/onの実ファイルを101要求すべてパースし、各48,000,452 BのSHA-256、raster、中心、offset、XYZ、法線、集約後の丸め前float値、levelを照合した。各フィールドがバイト一致。XYZ・法線・丸め前集約値の有限画素は各1,654,784、level 0も同数。全要求のXYZ/法線は研究110の保存幾何とも一致した。観測ログのタイル幾何生成は404→4回。元対照は整数TIFFを照合し、丸め前の値はoff/on観測間で照合した。計時1,818枚と詳細観測202枚は元R005の積算対照101枚に層ごとに一致した。[実traceのフィールド照合](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/audit-03/real_traces.json)

［一次］保存済み合成実行ファイルのSHAを照合したうえで、新しいC:作業先で一度実行した。法線退化と符号付きゼロのみのoffset、NaN中心と穴・境界、幅65のpartial tile、反転法線、有限中心を使う丸めの同一性を確認した。有限中心のケースでは原点基準のPoints経路と値が異なることもテストした。合成flipはSurface側の `flipNormals`。CLIのoffset符号反転は差分上で維持される。[合成テスト](../experiments/vesuvius/r006/20261112-geometry-reuse01/edge_cases.cpp) · [独立再実行ログ](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/edge-01/stdout.txt)

## リンクと資源

［一次］実mapとELF・保存loaderで、点補間と既存Surface、試作用 `PreparedSurface::sample` が現O3 `grid.o` に解決した。点補間の逆アセンブルと `addr2line -i` でHermiteのインライン展開を確認した。`Array::chunk`、`read_layer_chunk`、`MemoryCache::get/put` は借りたO3 `cache.cpp.o` が提供。旧coreなどの依存を借りた混在ビルド。保護対象399ファイルの前後SHAは一致し、実コンパイルソース、現ELF・リンクmap、合成バイナリ、借りたcacheオブジェクトを再ハッシュした。run01はソース生成アンカーで停止してコンパイル前。run02は合成リンクのlibcurl未指定で終了1となり、共有依存を追加して一度だけ再リンクした。失敗分を含む上限側のbuildは183.380秒、最大RSS約1.56 GiBで300秒以内。[現物リンクの照合](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/audit-03/build.json) · [元リンク失敗](../experiments/vesuvius/r006/20261112-geometry-reuse01/run02/link-edges.log)

［一次］独立検証はWSL Ubuntu、CPU 0・AS 4 GiB、ネットワーク隔離。監査成功34.55秒、合成再実行0.18秒。監査の最初の試行は非計時観測に性能計時と同一のディスクヒット数を要求して停止（4.53秒）。次はbuild上限側合計に再試行ラッパーの時間が入る点を厳密等号で誤って検査して停止（54.88秒）。原票に合わせて条件を補正した。検証全試行の計測壁合計94.14秒、最大RSS 107,892 KiB、追加費用0円。新規ビルド・CT取得・実データ描画は行っていない。[検証手順と失敗記録](../experiments/vesuvius/r006/20261112-geometry-reuse-verification01/README.md)
