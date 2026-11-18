Status: resolved
担当: 研究（R115 Sol/high）

# R006: 通常のZarr出力で処理全体を比較する

## 依頼

2026-11-12。研究113・114で形状再利用のCPU試作は画素を変えず初回サンプリングを約19.73%短縮したが、TIFF出力を含むプロセス全体は改善未確認だった。次の一件は実利用例が使うZarr出力の通常CLIで、処理全体のoff/onを比較する。試作の採用や公開は未決。

利用例の根拠は[固定版の実行コマンド](https://github.com/nerln/vesuvius-compositor-sweep/blob/b0951fd0c63f1865fb202f3e1bd2945326fa0429/COMANDI.md)。PHerc0139で `--zarr-output`、101層、step1、accum0.5、mean等を使用し、pyramidやcompressorは指定していない。2026-11-12に原文を再確認した。今回も既定bloscとpyramid L0〜L5を有効にする。入力は固定済みの別巻物PHerc0814・128×128・既定bicubic・101層・uint8・mean積算0.5のままで、外部利用者の大きいROIの性能を代表すると主張しない。

## 実装と資源

R113のアルゴリズムを変えず、観測差分を除いた試作ソースから通常の単一パスCLIをビルドする。pixel trace、内部タイマ、3パス反復を除き、off/onを同じバイナリの試作環境変数で切り替える。private PreparedSurfaceのままでよい。製品公開用APIやPython/CUDA機能の設計へ広げない。既存のO3依存オブジェクトとリンク原票を借り、変更grid/rendererのみコンパイルする。実O3 point/Array-cacheの解決を測定前に確認する。

追加支出0円、CT取得0。固定CT20MiBを保存SHAを照合してC:専用fixtureへコピーし、すべてのoff/onで同じC:入力とC:出力を使う。D:は依存物の読み取りのみ。元ソース・ビルド・試作113・原票は非変更。CPU1、AS4GiB、今回ビルド全体300秒、各描画120秒。新規依存導入、GPU、大きい環境再構築はしない。

## 固定比較と判定

通常CLIの完全な起動から終了までを各5回。組の順序は `(off,on),(on,off),(off,on),(on,off),(off,on)` と事前固定する。全出力先を新しくし、キャッシュを制御したと偽らない。各プロセスはArray新規、OS cacheは制御外。TIFF同時出力、resume、pre、pyramid省略、圧縮形式の変更はしない。プロセス壁・user/sys CPU・peak RSS・終了回収、出力ファイル数/bytesを保存する。113の時間と直接比較せず、この一件内のoff/onだけを比較する。

off/onのL0〜L5のshape、dtype、chunk配列と画素を確認する。圧縮本文が一致すればその事実も残し、L0を既存R005対照101 TIFFとデコード後に照合する。既存ライブラリのデコーダを借り、新しいZarr実装は作らない。実行引数や出力先など意図的なメタデータ差分と画素を区別する。

処理全体で中央値10%以上短縮し、5組すべてで悪化せず、出力同一なら、この固定小領域の通常Zarr処理で実用効果ありと判断する。閾値未達、方向が不安定、全体差が観測ばらつきに埋もれる場合は、この試作の全体実用性は未確認としてR006を保留する。圧縮やROI・回数を変えて好結果を探さない。どちらも再利用コード・正負の知見を残し、別の課題へ移る判断材料にする。採用主張には別担当での原票検証が必要。

モデル/effortはSol/highを選ぶ。アルゴリズムと正しさの基準は既にあり、既存ビルド・通常CLI・比較条件を解釈して実行する作業が中心で、新しい最適化設計は不要なため。追加subagent禁止。依頼を残し、失敗を含めた結果・資源・限界を追記してresolvedへ更新する。

## 結論

2026-11-12 [一次・固定比較]。通常Zarr CLIのプロセス壁時間中央値はoff 1.539008秒、on 1.489310秒で3.23%短縮。5組中2組で遅くなり、10%以上かつ全組非悪化の事前条件は未達。固定小領域でのプロセス全体の実用効果は未確認としてR006を保留する。ROI、圧縮、回数は事前条件のまま比較を終えた。[計時集計](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/summary.json)

出力10件はL0〜L5のshape・dtype・チャンク座標・全復号値で一致した。圧縮本文とメタデータも含め、各出力14ファイル・2,211,236 bytesのSHA-256が全て一致した。L0はR005バイナリで作成した対照 `control-accum` の101 TIFFと復号後に一致した。実行引数の出力先は各回で異なり、Zarrの中に差は生じなかった。[出力照合](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/output-verification.json)

## 根拠・詳細

| 組 | 順番 | off 壁秒 | on 壁秒 | 短縮率 |
|---:|---|---:|---:|---:|
| 1 | off → on | 5.600470 | 1.670359 | 70.17% |
| 2 | on → off | 1.537373 | 1.443505 | 6.11% |
| 3 | off → on | 1.539364 | 1.386077 | 9.96% |
| 4 | on → off | 1.539008 | 1.654718 | −7.52% |
| 5 | off → on | 1.315401 | 1.489310 | −13.22% |

組ごとの短縮率の中央値は6.11%。user CPU中央値はoff 0.34秒、on 0.24秒、sys CPUは0.11秒と0.12秒、RSS中央値は両方88,563,712 bytes。各回は新規プロセス・新規Arrayで、初回offは5.600470秒のまま集計した。OSキャッシュは制御外で、壁時間のばらつきの寄与は分離できない。この一件の結果は外部利用例の大きなROIに外挿できない。[固定順・引数](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/measurement-order.json)

R113の観測なしソースを元ファイルと生成関数から再計算し、保存 `product/` と `reuse.patch` に一致する2ファイルをO3でビルドした。readerの先頭にO3オブジェクトを置いて再リンクし、計時前にlink map・ELF disassembly・ローダーのbindingsで、O3 gridのpoint、インラインHermite、O3 cacheのArray/MemoryCache関数が選ばれたことを確認した。[ビルド原票](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/build-settings.json) · [リンク検証](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/link-gate.json)

## 取得の経路と資源

固定CTの10チャンク20 MiBとメタデータを保存SHAと照合し、C:の同じfixtureを全10回で使用した。D:は読み取りのみ。元入力・既存ビルド等399ファイルの保存SHAは前後一致。WSL Ubuntu・CPU1・AS 4 GiBで、ビルド206.486秒、全render壁時間の合計19.176秒、最大RSSはビルド1,674,366,976 bytes、render 89,612,288 bytes。全10回が120秒以内に終了コード0で回収された。追加クラウド支出0円、CT新規取得0 bytes。ローカル電力・モデル利用費は未算定。[fixture原票](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/fixture.json) · [再現手順と原票の一覧](../experiments/vesuvius/r006/20261112-zarr-whole-process01/README.md)
