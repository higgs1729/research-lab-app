# R182 vc_objrefineの評価窓を人工CTで検証

2026-11-14 JST。反転した2つの傾斜明帯は入力頂点直上で同じ強度列を持つ。固定 `vc_objrefine` を実行すると、r=0では中心頂点の法線変位が同じになり、r=3では約6 voxelの差が出た。R181で追った評価窓の配置が、この完全支持の入力で返る法線変位に影響した。

## 固定入力と対照

- [一次] A・B・Cともに64³ uint8のZarr v2 L0。16³の全64キーを各々保存。A/Bは `2(z−38) ≥ ±(x−32)`、Cは `z ≥ 38` を満たす点で255、それ以外は0。3体の生チャンク計786,432 B。tifxyzは5×5の単位間隔格子、XYZ=(30+列,30+行,32)。評価頂点は格子(2,2)、XYZ=(32,32,32)。
- [一次] 補助CLI `fixture-check` は、固定の `QuadSurface` で入力を保存・読戻しし、製品と同じ `pointSurface()->pointsAt` で中心の有効法線+Zを確認した。`PlaneSurface` の接線は+X/+Y。OpenCVの `getGaussianKernel(7,0,CV_32F)` は [2,7,14,18,14,7,2]/64。補助CLIは実行入口と別ELF。
- [一次] 全25頂点を囲うr=3の全深さの候補補間角6,480点、XYZ各軸の範囲[30,47]、[30,47]、[30,49]を先に確認した。必要なL0キーは12/体で、3体とも全キー実在。全候補角の生値を式と照合し、中心直上の−2…16 voxelで3体とも0が8点、255が11点と確認した。r=0の支持はこの中に収まる。[生CT・入力tifxyz](run02/fixture/) · [事前照合とSHA](run02/input-contract.json) · [実法線とGaussian](run02/fixture-check.log)
- [一次] 5回ともL0、reader_scale=0.5、start=−2、stop=16、step=1、既定118/255・165/255、border_off=0、cache_mb=32、overwrite=false、CPU。順にA r0、B r0、C r3、A r3、B r3を別出力へ各1回。r0対とC r3の中心変位一致を確認してからr3反転対へ進んだ。[r0設定](run02/fixture/r0.json) · [r3設定](run02/fixture/r3.json)

## 製品出力

| 固定入力 | 中心の出力Z | 符号付き法線変位 (voxel) |
|---|---:|---:|
| A r0 | 37.999938965 | +5.999938965 |
| B r0 | 37.999938965 | +5.999938965 |
| C r3 | 37.999938965 | +5.999938965 |
| A r3 | 41.034816742 | +9.034816742 |
| B r3 | 35.034877777 | +3.034877777 |

[一次] r3のA−Bは **5.999938965 voxel**。5出力とも25頂点、無効頂点0、全頂点で接線方向変位0。各出力の16頂点が法線方向に動き、9頂点のXYZは元と一致した。製品が保存したx/y/z TIFFとmetaをそのまま採取し、出力先とコピーのSHAを照合した。比較表は実TIFFを読み戻した結果。[実出力](run02/output/) · [全頂点の比較](run02/comparison.json)

[推論・事前計算] Pを中心とする対称Gaussianでは、接線反転したA/Bのぼかし列が各深さで一致する。生CTと実Gaussian係数で計算した対称配置のA/Bはともに6.034846566 voxel。現行の角基準の式ではA=9.034816567、B=3.034876566 voxelとなり、製品値との差は各1.22×10⁻⁶ voxel以内。対称配置は計算上の対照で、製品を変更して実行する試験は行っていない。この結果から分かるのは固定人工CTの変位差まで。窓配置の設計意図、実CTの紙面帰属、文字の改善は未評価。[計算列](run02/input-contract.json) · [主担当の事前見積もり](lead-predicted-offsets.json)

## 固定CLIの構築経路

[一次] R160の固定 `14d4e725df8b569e6fc8ceb3c04d130f705c1565` 展開から、`ninja -t commands vc_objrefine` の生成済みターゲット定義を取得。両コンパイル行は依存票用フラグを除いて実 `compile_commands.json` と一致した。ObjAlphaCompRefinement.cpp のSHA-256とGit blobをR160索引に照合。新WSL ext4作業先 `/home/tomoy/refinement-window-control01-build03` に自動生成の出力パスだけを移し、CMake `cmake_autogen` で実moc TUを生成。実フラグと同じPCH指定で製品cppと生成TUを各1回コンパイルし、実リンク列の順序とRPATHを保持してリンクした。ライブラリはR160の絶対実体へ解決し、既登録の `vc_core`、`vc_reader_native` の両SHAと一致。入力ソース、PCH、生成定義、借用ライブラリのSHAは構築前後で一致。共有ライブラリの再構築は0。helperは別ソースを同じライブラリにリンクした。[実argv・固定SHA](build/build-plan.json) · [ELFと実リンク先](build/build-result.json) · [製品ldd](build/vc_objrefine-ldd.txt)

[一次] C/ext4新作業、CPU affinity 1、AS 4 GiB、core 0、OpenMP/数値ライブラリ各1スレッド、ネットワーク名前空間はloopbackのみ、DとR160実体を読み取り専用で使用。構築6工程は計17.034秒、最大子RSS 1,410,183,168 B。fixture準備0.827秒、790,270 B。製品5回の合計0.288秒、最大子RSS 65,241,088 B、比較ループ0.956秒。実作業の最終割当11,190,272 B、C空き33,326,325,760 B。追加取得、依存導入、クラウド費0。[工程別ログ](build/) · [実行原票](run02/)

## 取得の経路と途中の停止

- 構築前の2回は読み取り専用bindの重複表示と空のroute表の検査で停止した。mountの有効側と `ip -o link` を検査する形へ修正し、本構築を1回実行。構築後、helperの依存票の名前を取り違えて収集が停止し、後処理入口の最初の呼び出しも引数読取りで停止した。実 `-MF` からファイル名を読む収集処理を使い、同じELFの依存票、ldd、SHAだけを確認した。[前処理1](launch-build.log) · [前処理2](launch-build02.log) · [実構築](launch-build03.log) · [後処理](launch-build-finish.log)
- fixtureの初回は `/mnt/c` のtifxyz原子的公開が EINVAL で停止。製品実行は0回だった。生CT原票と失敗ログを保持し、同じELF、座標、式、設定でWSL ext4へ入出力先を変更。製品実行前に完全支持と保存コピーを照合した。成功後の製品再実行は0回。[初回エラー](run01/fixture-check.log) · [5回の起動](launch-trial02.log)

## 主担当の別照合

[一次] 主担当は保存生CT全786,432値を別の整数不等式で照合し、192キーと元の25点を確認した。元と5出力のx/y TIFFから計250接線座標を読み、全値一致。事前の分数計算と実TIFFの中心変位の差は最大1.211×10⁻⁶ voxelで、実Gaussian係数も一致した。照合は製品を起動せず0.153秒で終了。[別照合コード](lead_verify.py) · [照合結果](lead-verified.json) · [計測](lead-process.json)

[研究票](../../../../research/182-refinement-window-control.md) · [ハッシュ目録](manifest.json) · [lab登録候補](lab-record.json)
