Status: resolved
担当: 研究

# R006: 101層・標準補間の計測を小さく準備できるか

## 依頼

2026-11-12。研究108の3層の計時は検証109で確認したが、初回チャンク取得が支配的で、公開実利用101層の投資判断へ外挿できないことも確認した。製品実装には進まない。次の一件は、既定bicubic・101層・step 1・accum 0.5・複数64×64読込タイルを含む代表入力の測定が、低い追加資源で可能かの準備に限定する。好都合な速度が出るまで条件を変える試験にはしない。

既存R005/R006のrenderer、grid TU差替え、resource-bounded runner、CTメタデータ/チャンクを借りる。CPU一個、追加費用0円、新規CT取得なし、GPUなし。元ソース・共有lib・build・過去成果物は変更しない。新フォルダ `experiments/vesuvius/r006/20261112-representative-feasibility01` と `D:/kensyoukin-work/r006-representative-feasibility01` を使う。幾何取得に必要なら、既存R005の観測用rendererの64×64制限を新しい隔離版で128×128へ広げる最小変更を認める。CTを読まないgeometry-only経路を用い、製品最適化や計時は行わない。ビルド300秒/回、幾何・軽い解析120秒/回、AS4 GiB。失敗も保持する。

### 選択する入力と判定

- R005と同じPHerc0814 `first-trace-on01/output`、level 0、scale 1。先に速度・CT強度を見ずに、cropを `(7356,2272,128,128)` に固定する。旧after-aのX中心7420を保ち、旧ROIで有効な上32行の側へ拡張する。旧after-aはy=2368..2399で全64列が有効、y=2400..2431は全列が無効だったため、y=2400を下端として上へ128画素を取る。
- 既定bicubicでXYZ/法線の実幾何、valid密度、中心のXYZと法線有無、4読込タイルを確認する。有効画素が90%未満、連続した一成分の領域として不適切なら、その事実を報告して停止する。都合のよい別cropを探索しない。
- 実際の101層・2 substepsのoffsetは `-50,-49.5,...,50,50.5` を想定し、生成コードと照合する。三線形8近傍と丸め余裕の必要CTキー・既存10キーとの差・追加転送byteの見積を出す。正確な列挙が資源上限内で難しい場合、安全側の連続線分包絡から上限を出し、その意味を区別する。欠損CTの値をfillとして使う描画は実行しない。
- 想定追加取得が64チャンク（128 MiB、無圧縮2 MiB/個）を超えるなら低費用の入力準備としては停止する。超えない場合も今回は取得しない。URL/キー/byteの根拠と次実験の0円見積・時間/RAM上限を提示する。見積のために有料基盤を起動しない。
- 既存compile_commandsから関連renderer/readerの最適化に必要なTU、元ビルドを汚さず借りられる範囲・ビルド負担を短く調べる。代表計測では一つのArrayを生かした初回/後続を分け、各タイルのスレッド・hit/miss・CPU/壁計時を混同しない設計を示す。全体の巨大再ビルド、依存導入、未見積の範囲拡大はしない。

次の代表計測の採否と実行は主担当が決める。この依頼では性能結果や画像の改善は主張しない。本人の11月まとめ応募の採用項目は引き続きR005一件で、R006は研究中。監査inboxは0件を確認した。

## 結論（2026-11-12）

［一次］固定した128×128・既定bicubicの範囲は **16,384/16,384画素（100%）** でXYZ・法線が有効。元の成分0に属する一つの4近傍連結領域で、描画時に使う四つの64×64読込タイルは各4,096有効画素。101層・step 1・accum 0.5の全202オフセットを覆うCTは10チャンク。既存10チャンクのうち使えるのは2チャンクで、**追加8チャンク、16,777,216バイト（16 MiB）** の見積。64チャンクの上限内で、代表計測の入力条件を満たした。今回は幾何取得だけを実施した。[幾何の判定](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/analysis01/geometry-gate.json) · [キー・URL・バイト見積](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/analysis01/ct-coverage.json)

## 根拠・詳細

- ［一次］crop `(7356,2272,128,128)`、PHerc0814 `first-trace-on01/output`、level 0、scale 1を固定。raster中央のXYZは (3337.170410, 3020.873535, 2524.301514)、法線は (−0.915415, 0.390335, 0.098258)。保存時に法線を要求して有効だったため、`point` が法線分岐前に書くXYZは法線を要求しない `centreOf` でも同じになる。R005のownerと元メッシュの成分から、全有効画素の四隅および最大4×4のbicubic微分支持の有効点を成分0と照合した。ここで確認した連続性は保存rasterと元メッシュに対するもので、紙面との対応や判読性は未評価。[生の幾何](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/geometry.bin) · [解析コード](../experiments/vesuvius/r006/20261112-representative-feasibility01/analyse.py)
- ［一次］rendererのsubstepは `[0, 0.5]`、101層の基底は −50から50の整数。合わせて −50〜50.5の0.5刻み、202オフセット。保存XYZ・法線と有限な中心を使ってfloat32のoffset加算・identity level mapを再現し、3,309,568サンプルの三線形8近傍（重複込み26,476,544近傍）を離散列挙した。±0.001 voxelのhaloも同じ10キーに収まった。既存の `0/19/23/25` と `0/19/23/26` を再利用でき、ローカル10ファイルは受取記録のSHA-256と全件一致。追加8キーのURLは同じ取得記録のルートから組み立てた。型は無圧縮 `|u1`、128³で2 MiB/キー。URLの今回の応答は未確認。[offset別のcoverageと追加URL](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/analysis01/ct-coverage.json)
- ［一次］R005の観測rendererの上限を別コピーで128×128に広げ、metadata-only Zarrの4ファイルを元CTメタデータとハッシュ照合して、geometry-only分岐で終了した。CT本文・TIFF出力はいずれも0、追加支出0円。隔離したコンパイル34.84秒、リンク3.75秒、幾何0.627秒、離散列挙を含む解析8.75秒、ビルド依存調査3.30秒。壁合計51.27秒、user/system CPU 24.72/3.16秒、最大RSS約1.48 GiB。記録した57保護ファイルの前後SHA-256は一致した。[実行と資源の記録](../experiments/vesuvius/r006/20261112-representative-feasibility01/README.md)

## 次の代表計測の条件

［推論］元のcompile DBとNinjaの読取専用リンク照会から、renderer 1 TUとreader 5 TU（`grid.cpp`、`cache.cpp`、`zarr/open.cpp`、`display.cpp`、`sources/image_write.cpp`）をO3にして新しいreaderとrendererへリンクする案を組めた。リンク入力48点は実ファイルを確認した。XYZ・法線・CT補間に加え、Array・MemoryCache・RAWローカル取得の主要処理はヘッダーから展開される。借りたO0オブジェクトとの弱いシンボルの解決はリンクマップとloaderで確認する。platform I/O、coreや一部依存はO0のまま残るため、フルReleaseの代用範囲は限定的。6 TUの最適化ビルドは未実行で、既測の単体コンパイルはrenderer O0の34.84秒とgrid O3の33.45秒。次の見積はローカルで0円、CT本文16 MiB、ビルド全体300秒・各計測120秒・AS4 GiBを上限とする。[実行前のビルド案](../experiments/vesuvius/r006/20261112-representative-feasibility01/run01/build-plan01/build-plan.json)

［推論］計時する場合は、必要10チャンクを隔離Zarrでサイズ・ハッシュ確認し、欠損をエラーにする。各モードで新しいArrayによる初回と、同じArrayを保持した後続を測る。`Array::stats()` のmemory hits・disk hits等の差分を取り、後続のdisk hitsが0か確かめる。CPU一個でも `parallel_for` のcallerと補助workerが交代し、壁時間区間は重なり得る。単一タイル用の共有計時状態は流用せず、タイルindexごとの境界・thread ID・CPU時間を保存し、join後に集約する。タイルCPU時間の合計とrequest外側の壁時間を別々に報告する。今回の入力準備から短縮率や画像改善は判定しない。[計測設計と再実行手順](../experiments/vesuvius/r006/20261112-representative-feasibility01/README.md)
