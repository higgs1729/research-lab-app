# R005 固定障害面を含む初期UV配置の既存手法

一次資料・実装の取得確認は2026-11-12 01:43 UTC。対象は224頂点・346面の円板で、境界100点中34点が固定（粗点5点を含む）。障害356面のUVも固定する。前回の100点割当てでは境界だけで決まる2面が反転し、内部辺2本が輪郭を出た。未割当ての境界点を決める段階に自由度が残る。[試行82](82-r005-boundary-routing-trial.md) [検証83](83-r005-boundary-routing-verification.md)

**採用候補はDu et al. (2021)のSEA-QN一件。** 元の面接続で対象と障害面を同じ求解へ入れ、34点と障害の全頂点を固定したまま自由な境界点を動かせる。R005で求解が成功するかは未確認。研究用基準はIを維持する。[原著 §§3–6](https://www.cs.wustl.edu/~taoju/research/bijective.pdf) [著者実装](https://github.com/duxingyi-charles/Smooth-Excess-Area)

## SEA-QN

- **確認済み。** 原著は複数の辺連結成分と複数境界を明記し、固定点を満たす非単射UVから開始する。既存CLI `SEA_QN` は元座標・初期UV・三角形 `F`・固定頂点IDを受け取る。`Arc_Overlap_Formulation` は初期UVを保持し、固定IDを除いた変数だけを更新する。全 `F` の有向境界辺を抽出して一つの円弧配置で面積を評価し、CLIは入力順のUVを出力する。元 `F` を使って戻せるため、追加頂点・再分割・エッジflip・固定点の順序変更を要さず、元面ID・元XYZ・粗点との対応を保てる。リポジトリはMIT表記で、著作権者欄はプレースホルダーのまま。[原著 §§3–6](https://www.cs.wustl.edu/~taoju/research/bijective.pdf) [CLI](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/apps/SEA_QN.cpp) [固定点と評価](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/src/Arc_Overlap_Formulation.cpp#L7-L112) [境界抽出](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/src/geo_util.cpp#L191-L215) [ライセンス](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/LICENSE)
- **R005への適用は推論。** Jの対象UVまたはIを初期値にできる。既存検証で障害2成分は対象と頂点を共有せず、全356面が正向きかつ障害面同士の内部重複0。障害間の接点108876は元の単一頂点として扱える可能性がある。円弧の半辺構築には次数4以上を角度順に処理する経路がある一方、外側のセルの特定では最左端が頂点の場合に入次数1を仮定する。接点を含む今回の数値動作は未確認。輪郭への割当ては不要で、前回の切り抜き輪郭上に自由点を拘束する機能や、1 UVの離隔を課す機能は確認できなかった。[障害の検証74](74-r005-seam-obstacles-verification.md) [円弧配置](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/src/Arrangement.cpp#L234-L300) [外側セルの選択](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/src/Arrangement.cpp#L433-L478)
- **成功の判定。** 原著Proposition 5.3は、可解で成分ごとに2点以上固定した場合の大域最小解について、十分小さいパラメータで重複面積の上限を与える。実装のL-BFGSでの到達や重複0は未保証。CLIの `globally_injective` は局所判定に円弧交点の有無を加える。円弧交点を伴わず別成分が完全に内包される重複はこの停止判定を通り得る。CLIは停止条件未達でも座標を書き出す。採用判定には元の三角形での符号・固定座標・内部重複と、全周囲面との重複の独立検査が要る。[原著 §5.2・§6](https://www.cs.wustl.edu/~taoju/research/bijective.pdf) [停止判定](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/apps/SEA_QN.cpp#L403-L445) [交点フラグ](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/src/Arc_Occupancy.cpp#L70-L110) [保存経路](https://github.com/duxingyi-charles/Smooth-Excess-Area/blob/main/apps/SEA_QN.cpp#L743-L760)

## Progressive EmbeddingとMatchMaker++

- **確認済み。** Shen et al. (2019)の基本法は固定境界内で一時的に辺を縮約し、逆操作で元の接続に戻す。非単射開始可。保証は3頂点連結と凸な固定境界を使う。付録は最粗段の1頂点を置ける非凸の星形境界にも言及する。R005の両端が境界の内部辺29本はこの3頂点連結条件を破る。MatchMaker++は部分位置固定を扱い、目標を凸部分へ分ける。経路が取れないときはSteiner点を追加し、3連結でないパッチでは境界間の内部辺を分割する。経路を処理する順序の変更は、固定点の境界巡回順を変更する操作とは別である。今回の非凸輪郭で元接続を保つ入口は未確認。著者実装の入口は `untangle_bin` と `matchmaker_bin`。リポジトリはMPL-2.0。[原著 §3.2・§4・付録A](https://cims.nyu.edu/gcl/papers/2019-Progressive.pdf) [著者実装](https://github.com/hankstag/progressive_embedding) [ライセンス](https://github.com/hankstag/progressive_embedding/blob/master/LICENSE)

## Xu et al. (2011)のAlgorithm Embed

- **確認済み。** 3頂点連結の三角形平面グラフと、全境界頂点の座標を入力する。グラフLaplacianで始め、境界を固定したままcotangent Laplacianを更新して内部座標を解く。初期埋込みの単射性は不要。非凸境界を扱うが、例えば1内部頂点の扇では境界のカーネルに内点が必要で、入力によって解が存在しない。再分割・点の追加・エッジflip・境界順の変更を使わない。R005を一括で解くには3頂点連結と全境界座標が不足する。内部辺で既存面を分けて試す場合も、各部分の境界となる辺の座標が先に必要。公開された著者実装の入口とコードライセンスは未確認。[原著 §§1–3・§5](https://citeseerx.ist.psu.edu/document?doi=2e1529ea6ce693d821f8360018a57b6cb2e964d0&repid=rep1&type=pdf) [著者掲載ページ](https://faculty.ustc.edu.cn/chenrenjie/en/lwcg/30268/content/19820.htm)

## 既存実装の前提

libiglの `bijective_composite_harmonic_mapping` は元 `F` を使い、正向きの初期UVから指定した `b,bc` を線形に補間する。34点だけを `b` にしても、自由点を輪郭上へ割り当てる制約や障害データはAPIにない。反転チェックは負面積とNaNを数える。手元の同ヘッダー・実装はMPL-2.0。CGALの固定境界Tutte/Mean Valueの単射保証は凸境界の場合で、非凸な今回の輪郭には適用できない。CGALの当該パッケージはGPL表記。[libigl API](https://libigl.github.io/dox/namespaceigl.html) [libigl実装](https://github.com/libigl/libigl/blob/main/include/igl/bijective_composite_harmonic_mapping.cpp) [CGAL API](https://doc.cgal.org/latest/Surface_mesh_parameterization/group__PkgSurfaceMeshParameterizationRef.html) [前回結果](82-r005-boundary-routing-trial.md)
