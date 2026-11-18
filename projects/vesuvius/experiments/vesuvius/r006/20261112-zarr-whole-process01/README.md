# R115 通常のZarr出力でのプロセス全体比較

対象はPHerc0814の固定crop `(7356, 2272, 128, 128)`。bicubic・uint8・101層・step 1・mean積算0.5・scale 1・group 0で、通常の単一パスCLIに `--zarr-output` を渡した。CLI既定のBloscとpyramidを使い、L0〜L5を出力する。研究115の事前登録は `record-438b0050f39c`。

## 実行方法

WSL Ubuntuで、既存のR111/R113オブジェクト、ソース、原票とD:のfixtureが保存時の状態で必要。空きの実行名を指定する。保存済みの計測は `run01`。

```powershell
$trial = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r006/20261112-zarr-whole-process01'
wsl -d Ubuntu -- python3 -B "$trial/run_trial.py" run02
wsl -d Ubuntu -- taskset -c 0 prlimit --as=4294967296 -- unshare -Urn python3 -B "$trial/verify.py" run02
```

`run_trial.py` はR113の生成関数を使い、純試作ソースと `reuse.patch` を再計算して保存版との一致を検査する。R113の `build-settings.json` を今回のC:作業先へ差し替え、grid/rendererの2ファイルをO3でコンパイルし、readerとCLIを再リンクする。借りたR111のO3オブジェクト4点は保存SHAを照合する。readerのリンクではO3オブジェクトを先頭に置き、ビルド後にR113と同じ関数でmap・ELF・ローダーを検査する。

計時はCPU 0固定・AS 4 GiB・ネットワーク分離。ビルド全体300秒、各render 120秒を上限にする。20 MiBのCTチャンクとメタデータはD:でSHA-256を照合してC:へコピーし、全renderで共通の入力にする。offは `R113_REUSE_GEOMETRY` を除去、onは同変数に `1` を設定する。固定5組の各回で新規プロセス・新規Array・新規出力先を使う。OSキャッシュは制御していない。`/usr/bin/time` と単調時計で分離ラッパーを含む起動から回収までを記録した。

`verify.py` は1レベル1チャンクの固定出力を対象に、既存libbloscの `blosc_decompress_ctx` で60チャンク、既存libtiffの `TIFFReadEncodedTile` で対照101枚を復号する。各出力の全画素とL0対TIFFをバイト列で比較する。各レベルのメタデータ、チャンク座標、全ファイルと圧縮チャンクのSHA-256も保存する。

## 結果

プロセス壁時間の中央値はoff 1.539008秒、on 1.489310秒で3.23%短縮。組別の短縮率は順に70.17%、6.11%、9.96%、−7.52%、−13.22%。事前の10%かつ全組非悪化の条件は未達。初回offの5.600470秒も事前の順序どおり集計した。OSキャッシュや入出力待ちの寄与は未計測。

10出力すべてがL0〜L5の全画素、圧縮本文、全メタデータで一致した。各出力14ファイル・2,211,236 bytesで、L0はR005バイナリで生成した対照101 TIFFの復号値とも一致した。入力等399ファイルの保護SHAも前後で一致した。

ビルド206.486秒、10回の計測壁時間合計19.176秒、renderピークRSS 89,612,288 bytes、ビルドの個別プロセス最大RSS 1,674,366,976 bytes。全renderを終了コード0で回収した。新規CT取得0 bytes、追加クラウド支出0円。ローカル計算、電力とモデル利用の費用は未算定。

## 原票

- `run01/fixture.json` と `protected-{before,after}.json` はC:への複製と入力・既存ビルド等のSHAを記録する。
- `run01/build-{settings,result}.json`、`reuse.patch`、`link-gate.json`、`loader-resolution.json` と `point-disassembly.log` はビルドと実行時の解決を記録する。
- `run01/measurement-order.json`、`pair-*-process.json`、`pair-*-time.txt` とCLIログは固定順・引数・壁時間・user/sys CPU・ピークRSS・終了回収の原票。
- `run01/output-verification.json` は出力ファイル数とbytes、メタデータ・圧縮本文・復号値の照合を記録する。Zarr実出力とビルド生成物は `.work/r006-zarr-whole-process01/run01` に保存した。
- `run01/summary.json` は組ごとの比較、各モードの統計と閾値判定を記録する。
