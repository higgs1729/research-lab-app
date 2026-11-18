# R006 CPU積算描画の変更前測定

2026-11-12。依頼と判断は [研究108](../../../../research/108-r006-accum-baseline.md)。計時対象はPHerc0814のR005 after-a、crop (7388, 2368, 64, 64)、group 0、scale 1、表面linear・CT三線形、3層、slice step 1、TIFF。積算は `--accum 0.5 --accum-type mean`。

## 再実行

Windows PowerShellから実行する。元のWSL Ubuntu 24.04、R003のソース・共有ライブラリ・コンパイルDB、R005のローカルCT・面・ネイティブ描画ハーネスを借りる。新しいラベルを使うと別の記録と出力ができる。

```powershell
$trialPath = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r006/20261112-accum-baseline01'
wsl -d Ubuntu -- unshare -Urn python3 -B "$trialPath/coverage.py"
wsl -d Ubuntu -- python3 -B "$trialPath/baseline.py" run02
wsl -d Ubuntu -- unshare -Urn python3 -B "$trialPath/summarize.py" "$trialPath/run02"
```

`baseline.py` は描画前に同じcoverage検査を実行する。バイナリ・オブジェクト・TIFFは `D:/kensyoukin-work/r006-accum-baseline01/<label>`、引数・差分・前後の入力ハッシュ・出力ハッシュ・生ログはこのフォルダの `<label>`。元バイナリの両モードを各1回照合し、計時4条件を各1回ウォームアップしてから各5回測る。反復ごとに条件の順を反転する。毎回新しいプロセスと出力先を使う。OS側のキャッシュは消去していない。Arrayのデコード済みチャンクを入れるメモリキャッシュは毎プロセス新規。

## 計時の境界

| 名前 | 範囲 |
|---|---|
| host | 各CPU Surfaceサンプラー呼出しのrequest検査、中心、タイル、CT、結果組立。3回または1回の和 |
| centre | 各requestのraster中央1点のXYZ。法線の要求なし |
| geometry | CPUタイルの `points` callbackがXYZ・法線を生成。バッファ確保はhostのみ |
| CT | タイル画素ループ全体。offset、有限判定、三線形、必要なチャンクの取得、積算reducer、格納を含む |
| chunk | CT中の `Array::chunk` 呼出し。初回のファイル取得と後続のメモリキャッシュ参照を別に集計 |
| TIFF | writerのsetup、tile write、finish/closeの和。永続ストレージへのflush完了時刻は測定外 |
| プロセス | GNU timeを介した起動から終了まで。最大RSSとuser/system CPUも取得 |

readerの境界は単調壁時計と同じスレッドのCPU時計、TIFFは壁時計。計時点で時計を読む負担がある。特に `Array::chunk` の時計読み取りと計測用の不足検査はCTループ内に入る。readerのログは計時終了後のスレッドローカルオブジェクト破棄時に出す。タイルは各requestで1個なのでArrayの数値ループは呼出し側で同期実行し、ログ上の二つのthread IDも一致する。OpenMP/OpenCVを1スレッドに固定し、Arrayの補助プールにはR005と同じ1 workerを指定した。このROIでは補助workerにタイルが渡らない。

## 保存した記録

- [事前coverage](coverage.json)と[最初の検査失敗](coverage-first-attempt.log)。中心の有限性を要求した初回assertは試験側の誤りで、描画前にコードのNaN fallbackに合わせて修正した。保存幾何の中心は法線を要求した結果、実サンプラーの中心は法線を要求しないため、後者もログでNaNと確認した。
- [全反復の集計と各requestの数値](run01/summary.json)、[O3積算の生ログ例](run01/O3-accum-1.log)、[同モード対照のTIFFハッシュ](run01/control-outputs.json)。タイミング付き24描画はすべて、同じモードの対照TIFF 3枚とバイト一致した。
- [grid差分](run01/grid.patch)、[renderer差分](run01/vc_render_tifxyz.patch)、[O0コマンド](run01/build-O0.json)、[O3コマンド](run01/build-O3.json)、[依存TUの設定](run01/dependency-compile-settings.json)、[O0バイナリSHA-256](run01/binary-O0.json)、[O3バイナリSHA-256](run01/binary-O3.json)。
- [環境と資源制限](run01/environment.json)、[保護対象の開始前ハッシュ](run01/protected-before.json)、[終了後ハッシュ](run01/protected-after.json)、[O3コンパイル警告](run01/compile-grid-O3.log)。GCC 13は汎用の `ElementType::load` について `-Wstringop-overflow` を出した。今回の `|u1` は `visit_load` が直接 `uint8_t` を読む分岐を使う。

O3は `grid.cpp` 一個の差し替え。XYZ・法線補間、level map、三線形点サンプラー、タイルループは同TUとそこから展開されるヘッダーにある。O0/O3とも `-ffp-contract=off` を維持した。Arrayのヘッダー定義はgridコンパイルで最適化され得る一方、元共有ライブラリ側で解決される依存、外部cache/open/store/TIFF TU、rendererは既存O0。実行ファイル側のSurface版 `grid::sample` シンボルと、各requestの計時行・オフセット・回数により差し替えの通過を確認した。フルReleaseの計測値はここには含まれない。
