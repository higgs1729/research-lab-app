Status: resolved
担当: 研究

# R006: 11月まとめ応募に加える次の小改善は何か

## 依頼

2026-11-12。R005のflatboi成分配置は製品と限定CT比較の独立検証を完了し、第一項目として凍結した。本人の方針は、締切まで複数の小改善をまとめて一応募にすること。少ない支出で最初の受賞と再利用できる知識・道具を目指す。

次に扱う小改善の候補を最大3件へ絞り、最初に試す一件を提案する。現行の公式ソース・実利用のissue/PR・手元で実際に通したワークフローの根拠から、問題の実在、既存修正との重複、現在も使われる経路、必要な入力と小さい再現、期待する改善、手元CPUでの見込み/停止条件を整理する。事実と推論を分ける。既存の調査・ツールを先に参照し、同じ不採用候補やR005の終えた微調整を漫然と再開しない。

調査対象はVesuviusの解読に直接役立つツール改善。汎用の監査器/評価器だけを主成果にしない。公開情報の参照とローカルソースの読み取りを行い、実験・ビルド・大きなデータ取得・依存導入・有料計算・外部投稿は行わない。サブエージェントを追加しない。次の実験の採否は主担当が決める。

結果はこのファイルの依頼を保持して追記し、調査の入力・取得根拠は `experiments/vesuvius/r006/20261112-candidate-sources01` に保存する。既存の根拠を上書きしない。各候補を実装するのではなく、次の一件を判断できるところで調査を閉じる。

## 結果（2026-11-12）

**最初の一件は `vc_render_tifxyz --accum` の同一タイルでの幾何再利用。** 変更前の経路でXYZ・法線の補間回数と時間、CTサンプリング時間を一回測る。実用的なCPU時間の削減余地が出た場合に、同じサンプルと画像を保ったまま、層間でXYZ・法線を共有する小変更へ進む。

### 第一候補の根拠

- NerlnがPHerc0139 `20250108000004-w029_2025010827` の実CTを level 2・101層・2304×768画素のcropで描画し、`--slice-step 1 --accum 0.5` を mean、median、max で使用した。公開コマンド、照合用の対照、スコアがある。これは利用実績の根拠で、別の面でのインク判読向上や今回の高速化の根拠には使わない。公式Tutorial 5のS3描画とGUI Renderも同じCLIを利用する。公式例に `--accum` は含まれず、適用範囲は積算を選ぶ利用者に限る。[利用者の実行コマンド](https://github.com/nerln/vesuvius-compositor-sweep/blob/b0951fd0c63f1865fb202f3e1bd2945326fa0429/COMANDI.md#L6-L34) · [実行結果](https://github.com/nerln/vesuvius-compositor-sweep/blob/b0951fd0c63f1865fb202f3e1bd2945326fa0429/README.md) · [公式Tutorial 5](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/scrollprize.org/docs/07_tutorial5.md#L511-L544)
- `main` は `f0e441016900cb946bc3861025eca3a7cc2aae19`。`renderTiles` のCPU積算経路は一出力層ごとに同じ `surface` と `raster` で `sampleTile` を呼び、変えるのはサブステップのoffset列。`grid::sample(Surface, Raster, Request)` は毎回中央点を取り、読込タイルごとに同じ画素のXYZと法線を `resampleRect` で生成してCTをサンプルする。通常stackは全層を一度に渡す。全層を一枚にする composite も別の一回呼出しで、`alpha` と `beerlambert` はそちらに入る。[描画分岐](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L453-L477) · [CPUの幾何生成とサンプル](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/vc_reader/src/cpp/grid/grid.cpp#L379-L449) · [中央点とSurface経路](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/vc_reader/src/cpp/grid/grid.cpp#L507-L536)
- 同じ最適化のPRは検索範囲で見つからなかった。マージ済み #1528 は合成方式の修正、#1905 は必要チャンクの先読み。openの #2446 は `render_ink.py` の後処理RAM、#2449 と #2474 は法線・補間結果に触れる別変更。後二件の更新で既定描画が変わった場合はその時点のmainで基準を取り直す。[合成 #1528](https://github.com/ScrollPrize/villa/pull/1528) · [先読み #1905](https://github.com/ScrollPrize/villa/pull/1905) · [後処理 #2446](https://github.com/ScrollPrize/villa/pull/2446) · [法線 #2449](https://github.com/ScrollPrize/villa/pull/2449) · [窓境界 #2474](https://github.com/ScrollPrize/villa/pull/2474)

### 一回の測定案と停止条件

1. R005の `after-a` を使う。`render01/after-a/render-process.json` に実行引数がある。保存済み `D:/kensyoukin-work/r005-ct-render01/ct01.zarr`、同 `build02/vc_render_tifxyz`、`20261112-pack-native01/first-trace-on01/output` の面を再利用する。ROIは `(x,y,w,h)=(7388,2368,64,64)`、level 0、scale 1、線形、1スレッド。`build02/build-settings.json` のコンパイル・リンク条件を新しい隔離ディレクトリに転用できる。既存readerバイナリの再利用で、本体から測れるのは `sampleTile` 全体。幾何とCTの内訳が必要なら、同じ `grid.cpp` のCPU callbackとsampleループの境界に計時を入れた隔離計測で確認する。R005の幾何保存用環境変数を有効にすると追加補間と出力が入り、積算では同じ保存先を層ごとに上書きするので、計時には使わない。[実行条件](../experiments/vesuvius/r005/20261112-ct-render01/render01/after-a/render-process.json) · [隔離ビルド](../experiments/vesuvius/r005/20261112-ct-render01/build02/build-settings.json) · [既存計測差分](../experiments/vesuvius/r005/20261112-ct-render01/build02/observation.patch)
2. `--num-slices 3 --slice-step 1 --accum 0.5 --accum-type mean` の積算と、同じcrop・3層の通常stackを計測する。積算offsetは `[-1,-0.5,0,0.5,1,1.5]` voxel。範囲はR005の保存層−2〜+2に収まる。中間offsetが別の三線形近傍へ触れる可能性があるため、開始前に必要キーが取得済み10個に含まれるか照合し、未取得チャンクをfillとして使わない。通常stackと積算の経路判定に呼出し回数を用い、時間差の帰属は積算内の幾何、CT、書出しを別計時して判断する。1タイル3層では幾何生成3回と1回がコード上の予測。時間は事前ウォームアップ後の同条件反復で測る。[保存済みCTキー](../experiments/vesuvius/r005/20261112-ct-render01/ct01/fetch-result.json) · [凍結時の必要標本](../experiments/vesuvius/r005/20261112-ct-render01/freeze01/frozen-selection.json) · [offset生成](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L273-L288)
3. 再利用で除ける幾何時間 `(積算全層の幾何時間 - 一層相当)` が測定ばらつきに埋もれる、またはサンプリング段階の約1割に届かないなら、実装前に停止する。見込める場合は既存 `Surface::resample` と `sample(Points, Request)` から試す。Surface経路はraster中央を、Points経路はゼロをcenterに渡すため、結果の同一性は要検証。法線を要求する呼出しが零offsetだけの層の有効点判定に影響する場合もある。両経路でXYZ、法線が必要な層の方向、各層のvalid・NaN位置、丸め前のCT値、整数画素の同一性を確認する。線形の測定が有望でも、既定のbicubicを含めて同一性を確認してからCPUで採用を判断する。通常stack、合成、CUDAは既存経路を利用する案。公開APIで同一にならず、現行と同じcenter・有効判定・演算順を保つ差分が小さくまとまらない場合も停止する。[既存のSurface/Points API](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/vc_reader/include/vc_reader/grid.hpp#L93-L126) · [Pointsのcenter](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/vc_reader/src/cpp/grid/grid.cpp#L548-L558)

既存ROIは実CT20 MiBと実面を保持し、前回の隔離rendererビルドが約29.5秒・最大RSS 1.48 GiB、描画は最大7.15秒だった。今回の主な追加負担は計時版readerを必要とした場合のビルド。CPU一個・新規取得0・支出0の測定から始め、手元のbuildを借りられない場合や必要チャンクが不足する場合は投入を広げずに止める。期待する効果は積算描画のCPU時間の短縮。リモートの転送量やAUC改善は現時点で根拠がない。[前回の実測と独立検証](103-r005-ct-render-trial.md) · [独立検証](104-r005-ct-render-verification.md)

### 予備候補

**不完全な手動cropを、読込・出力の前にエラーにする。** 現行の4引数は既定0で `cw > 0 && ch > 0` のときだけ手動cropになる。例えば `--crop-width 64` を渡してheightを落としたCLIスクリプトは全キャンバス描画に進む。小さなROIを繰り返すCLI利用者が対象。実利用者のスクリプトは全4引数を渡しており、同じ引数落ちの外部報告は検索範囲で見つからなかった。GUIも有効なcropには全4引数を組み立てる。入力指定誤りのコストを止める小変更で、正常な描画の高速化は見込まない。R005の実面と同じ設定からheightだけを省いたケースを用い、変更前はgeometry-onlyの隔離計測で全キャンバス選択まで、変更後は入力オープン・チャンク要求・出力作成前の非ゼロ終了までを見る。正常な64×64と全引数省略の対照を残す。現行mainで早期拒否済み、既存呼出しが部分指定の仕様に依存、または不足の現れ方が再現しない場合は停止する。[crop分岐](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L1382-L1406) · [GUIの引数生成](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/volume-cartographer/apps/VC3D/CommandLineToolRunner.cpp#L397-L403) · [実利用者のCLI](https://github.com/nerln/vesuvius-compositor-sweep/blob/b0951fd0c63f1865fb202f3e1bd2945326fa0429/COMANDI.md#L6-L18)

#2478 は7公開面で1.2〜8.8 GBの概算を報告した提案。現在の `cachedOnly` はメモリ・ディスクcacheを読み、missingのキーを返す。無取得で純粋な要求量を出す経路や、圧縮後転送バイトの計測と同じ意味にはならない。見積で利用者がcropを選び直せるものの、見積単体では同じ描画の転送量も待ち時間も減らないため候補に加えなかった。#2482は報告者の公開面調査でmask利用が見つからず、期待仕様も未決。実利用側で既存解のある #2371/#2379、#2239/#2242、#2104/#2389・#2133、#1845/#1851 も見送った。[転送量の提案 #2478](https://github.com/ScrollPrize/villa/issues/2478) · [cache-onlyの契約](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/vc_reader/include/vc_reader/grid.hpp#L150-L189) · [mask仕様 #2482](https://github.com/ScrollPrize/villa/issues/2482) · [downloader #2379](https://github.com/ScrollPrize/villa/pull/2379) · [umbilicus #2242](https://github.com/ScrollPrize/villa/pull/2242) · [tracer #2389](https://github.com/ScrollPrize/villa/pull/2389) · [tracer #2133](https://github.com/ScrollPrize/villa/pull/2133) · [mesh選択 #1851](https://github.com/ScrollPrize/villa/pull/1851)

調査ではGitHub連携で検索・本文を確認し、`git ls-remote` でmainを再確認した。renderer、gridヘッダー・実装、点サンプラーの4ファイルは、ローカルの読み取り専用参照と現行mainのGit blobが一致した。原文18ファイル・取得URL・SHA-256・Git blob、限定検索の結果を保存した。今回はソース照合までで、描画・ビルド・計時・外部投稿は行っていない。[原文マニフェスト](../experiments/vesuvius/r006/20261112-candidate-sources01/sources.json) · [検索結果](../experiments/vesuvius/r006/20261112-candidate-sources01/search-results.json)
