# R006の101層代表計測に向けた入力確認

[研究110](../../../../research/110-r006-representative-feasibility.md)の固定入力を使った。取得したのは幾何だけで、TIFF出力は0枚。CTの強度と性能は測定範囲外。

## 再実行

```powershell
$trialPath = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r006/20261112-representative-feasibility01'
wsl -d Ubuntu -- python3 -B "$trialPath/feasibility.py" run02
wsl -d Ubuntu -- python3 -B "$trialPath/analyse.py" run02
wsl -d Ubuntu -- python3 -B "$trialPath/build_plan.py" run02
```

最後のコマンドは `geometry-gate.json` と `ct-coverage.json` が両方合格のときに使う。どのコマンドも研究108とR005の計測・タイムアウト処理を借りている。子プロセスはネットワーク隔離、CPU 0、4 GiBのアドレス空間制限。新ラベルは隔離作業先と結果フォルダの両方に使われる。

- [ビルド引数](run01/build-settings.json)と[観測差分](run01/observation.patch)。R005の観測用ソースから上限判定を128×128へ広げた。観測差分に残る単一タイルのコメントはR005時点の説明。Surfaceの幾何取得は `Surface::resample`、将来のCTサンプラーのタイル数は別経路の `sampleTiles` の64×64分割から求めた。
- [メタデータのみの入力](run01/geometry-settings.json)、[実行引数と資源](run01/geometry-process.json)、[rendererログ](run01/geometry.log)、[保存XYZ・法線](run01/geometry.bin)。CTコンテナは4メタデータファイルだけを置き、geometry-only分岐で終了した。
- [有効画素・連結・元成分の確認](run01/analysis01/geometry-gate.json)と[全202オフセットのCTキー、追加8 URLとバイト見積](run01/analysis01/ct-coverage.json)。保存されたR005のraster owner、元メッシュの成分、float32のraster座標から、各bicubic四隅と4×4の微分支持の由来を確認した。元成分と画素の4近傍連結を確認したもので、パピルス紙面との対応や判読性は評価していない。
- [build案の原引数と予定argv](run01/build-plan01/build-plan.json)、[開始前の保護対象SHA-256](run01/protected-before.json)、[終了後SHA-256](run01/protected-after.json)。予定argvには将来の計時用renderer/gridソースと出力の仮パスが入る。実行には次回計測の決定と計時パッチが必要。

## 次の一回で測る場合

現行rendererのビルド引数と、Ninjaの `-t commands` が返すreaderのリンク引数を借りる。予定はrenderer 1 TUとreader 5 TUのO3化、reader共有libとrendererの再リンク。readerは `grid/grid.cpp`、`cache.cpp`、`zarr/open.cpp`、`display/display.cpp`、`sources/image_write.cpp`。元のオブジェクトとアーカイブを入力に借り、同じSONAMEを持つ別共有libを新ディレクトリに出す。readerとrendererのリンク対象を固定し、loaderとリンクマップで新共有libの使用と弱い `Array::chunk`、`MemoryCache::get` 等の提供元を確かめる。ヘッダー内のArray・LRU・RAWファイル取得はgrid等からも展開される。外部cache prefill TUは弱い定義を提供し得るため対象へ含めた。生チャンクI/Oのplatform、Zarrメタデータの一部、core、外部ライブラリは元のビルドを借りる。全体のRelease性能はこの構成でも未測定。

次回の見積はローカルCPUと既存ライブラリで追加支出0円、CT本文16 MiB、ビルド全体300秒以内、各計測プロセス120秒以内、AS4 GiB。読込チャンクを全て保持する場合は20 MiB、通常stackのfloatサンプル配列は約6.31 MiB。計時版のピークRSSと予定6 TUのビルド時間は未測定。比較できる実績は今回のrenderer O0コンパイル34.84秒・最大RSS約1.48 GiBと、研究108のgrid O3コンパイル33.45秒・約1.23 GiB。予定上限を超えたビルドや実行は止める。

取得を決めた場合は既存CTとは別のローカルZarrを組み立て、必要10キーのサイズとハッシュを確認してからネットワーク隔離で描画する。CTを読む最初のpassと、同じArray/MemoryCacheを保った後続passを対にする。初回を測るプロセスはモードごとに新設する。OSのファイルキャッシュの状態は別扱い。各passの前後で `Array::stats()` のmemory hits、disk hits、corrupt等を取得し、全チャンクが非nullであることと事前の実ファイル検査で欠損fillを防ぐ。後続を温まった測定と扱う条件は、対象キーを保持し、後続のdisk hitsが0であること。

一つの128×128出力タイルはCPU grid内で四つの64×64タイルに分かれる。研究108の単一タイル共有記録をそのまま使うと複数workerの同時更新になるため、各requestでタイル別の記録をあらかじめ確保し、タイルindexごとの境界とthread IDを計り、`parallel_for` から戻って集計する。CPU一個へ固定してもcallerと補助workerが交代して走り得る。タイルのCPU時間合計、壁時間区間、requestの外側で測る壁時間、TIFFとプロセスを別々に保存する。重なるタイル壁時間を合算して、削減される経過時間として扱わない。
