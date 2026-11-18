# PHerc0306B上方候補の元CT追試

- [研究226](../../../../research/226-pherc0306b-upper-original-ct.md)に判断と限界を記載。[plan.json](plan.json)は元CT本文取得前の凍結計画。[lead-plan-check.json](lead-plan-check.json)は主担当の独立した座標・キー集合の計算。
- [元CTの取得ログ](ct-http.jsonl)は73キー分のHEADとGET、[取得原票](ct-acquisition.json)はファイルとハッシュの対応。[入力一覧](input-references.json)からメタデータ、作品側のmeshと図の出どころを確認できる。
- [section一覧](sections-result.json)は原データDNのPNG、注釈図、連続断面のXYZ・法線NPZを対応付ける。各図は同じ0–255のCT DN表示。注釈図の拡大は最近傍。

## 図の読み方

1. [上方の位置図](sections/upper-locator.png)と[既知輪の位置図](sections/known-locator.png)は上がcarrierの大きいy。上段は今回の元CTから独自に採ったd=0、下段はR225の公開確率原票。明るいほど予測インク確率が高い。CTの暗さとインク確率は別の量。
2. 上方は[左曲線](sections/upper-bend-normal-marked.png)、[横断](sections/upper-across-normal-marked.png)、[右の隣接群](sections/upper-adjacent-normal-marked.png)。対照は[輪の横断](sections/known-across-normal-marked.png)と[輪の縦断](sections/known-down-normal-marked.png)。各列は図の経路順、上下は独自の法線方向。横軸はcarrier約1 px/列。縦軸は元CT 1 voxel/行を表示上3倍。両端のシアン印がd=0。図の色は候補位置の案内に使用した。
3. 各点の `*-orthogonal-marked.png` は丸めた元CT座標を中心とする±32 voxelの整数面。固定軸、左右・上下の軸、半画素未満で丸める前のmesh XYZを表示。シアン印を外した `*-axis-*.png` はCTの値をそのまま持つ。

METHOD §2 は著者のlayer20を中央名目層と記述する。歴史的な描画実装との完全同一条件は確定していないため、この実験のd=0図に著者のlayer20 PNGを使用していない。紙層の帰属は断面の連続した明帯・境界と方向別の原軸面から評価した。

## 再実行

取得条件と方法は `plan_ct.py`、`acquire_ct.py`、`render_sections.py`。既存のCT本文を使った描画再実行は、新しい作業ディレクトリに同じ参照構成を揃えて行う。ソースは上書きを避けるため既存出力があると停止する。実行ログにはCPU 1基とWindowsプロセスの4 GiBコミット制限を付けた。
