# 局所m7 snapの既知対照とPHerc0191の元CT比較

PHerc0343の固定既知面で、再snap後も同じ位置に字画部分を追えた。親担当と担当が局所保持を確認したため、PHerc0191の固定三面を補正し、同じ元CTの9地点で前後を比較した。0191は中心3地点の紙層支持がどの面でも揃わず、通過0面。未知側のインクは未判定。 [研究票](../../../../research/216-m7-snap-known-control-and-local-ct.md) · [承認済み計画](../20261114-predicted-sheet-snap-plan01/next-plan.json)

## PHerc0343の既知字画

公式m7 L0の62キー27,235,944 Bを取得し、固定ETag・圧縮長・SHA、復号長192³を照合した。受賞0343の固定snapをmax_off 15、jump 6、σ1、level0とし、並列poolを同じI/O処理の逐次呼出しに変えた。範囲は既知384²に寄与するcoreと11-cell halo。元フル格子にはcore 756頂点だけを戻し、外側42,252点、valid mask、scaleを保持。coreのdirect runあり746点、中央値除外24点、direct runなしで補完した10点。最大節点移動4.939 voxel。親の独立計算はhalo込み75,950サンプルからrun、中央値、Gaussian、全局所XYZまで一致した。 [取得](m7-known-acquisition.json) · [snap原票](snap-known-result.json) · [上流差分](upstream-adapter.diff) · [親のsnap検算](lead-snap-check.json)

元面とsnap面は同じ絶対384²、33層、linear、nominal 9.6 µm、step 1.111で描画した。renderと断面に必要な元CT35キーは全て保存済みだった。再描画の元面はR185の保存入力4,866,048値と全バイト一致し、元のdense出力を再利用した。snap面だけdense-native reverseを1回、保存と同じ24→8の17枚、128²/stride64で25パッチ、同じ正規化とHannで推論。主256²の診断はPearson r=0.993606、MAE=3.037 DN、最大23 DN。親は確率の集約から全147,456 PNG値が一致することと、元CT断面全43,218画素を別検算した。 [描画入力差](input-comparison.json) · [CT支持](ct-render-support.json) · [固定比較](known-comparison-256.png) · [親の数値検算](lead-known-check.json)

右の囲まれた暗部と隣接する曲線、左の縦長部分は同じ位置に残った。親と担当は固定階調の原寸図と9地点のCT断面を別々に見て、新たな明白な融合、途切れ、層飛びを認めなかった。下左の点では1.797 voxel動いたが、元から曖昧な暗部境界で層の帰属は変わらず未確定。製品画素の変位は中央値0.403、最大3.695 voxelで、測った共有格子に向き反転なし。この面は元からsnap・Lasagna・接合済みで、再適用時の保持を確認する対照に限る。 [全384²](known-comparison-384.png) · [9地点のCT](known-sections-gallery.png) · [幾何統計](known-geometry-metrics.json) · [担当目視](known-visual-review.json) · [親の目視と通過](lead-known-visual.json)

## PHerc0191の同9地点

既知の対照通過後に、固定m7 L0の121キー71,124,890 Bを取得。元のw052/w053/w054の各9局所をそれぞれ元XYZから切り出し、同一条件で計27領域に適用した。R214の同じray、同じ高さで27交点はいずれも一意に再計算できた。元CT18枚の値・範囲はR214を再利用。親は局所XYZ全71,820成分、121チャンクSHA、保存CT18枚SHAを照合し、報告した27交点を別のNewton解で最大1.82×10⁻¹² voxel差まで検算した。 [取得](m7-unknown-acquisition.json) · [処理の原票](snap-unknown-result.json) · [全交点、支持と前後図](unknown-geometry-ct.json) · [親の独立検算](lead-unknown-check.json)

- 中央 z11952でw052とw053が暗帯の同じ境界に近づいた。固定ray上のw053−w052間隔は+6.195から−0.599 voxelになり、順番が逆転した。断面だけで三次元の交差全域や実ラミナの同一性は確定できない。 [元CT前後図](unknown-sections/z11952-x1024-ab.png)
- 左 z11760ではw053とw054の間隔が12.123から2.549 voxelに縮み、二面の独立した帰属を判定できなかった。右 z11760のw054は固定rayで+22.657 voxel移動した。これは固定面との交点の移動で、core節点の最大変位7.562 voxelと区別する。曲がる複数の帯の中で移動先の紙層の同一性は未確定。 [左比較](unknown-sections/z11760-x256-ab.png) · [右比較](unknown-sections/z11760-x1792-ab.png)
- 中央 z12240ではw052に細い明帯の局所的な支持が残り、w053は広い暗部内、w054はその縁付近。中央 z11760の三面は粒状域や曲がった境界にあり、帰属の確定には至らなかった。中心3地点を通る面がなく、今回の三面では広域予測へ進まない。 [z12240](unknown-sections/z12240-x1024-ab.png) · [z11760](unknown-sections/z11760-x1024-ab.png) · [担当目視](unknown-visual-review.json) · [親の別目視](lead-unknown-visual.json)

既知0343では局所CTでラミナ帰属が曖昧な地点を含んでも字画部分を再現できた。今回0191に使った事前条件は、紙層対応を強く確認する条件で、未知インクの検出感度との関係は未校正。 [親の別目視と限界](lead-unknown-visual.json)

## 実行量

m7計98,360,834 B（93.8 MiB）。既知の転送20.100秒、未知44.036秒、snap約1.054/3.555秒、dense1回15.093秒（外側）。新元CTは両段0。主要工程CPU1・commit/AS4 GiB、最大RSS約833 MB、C作業約229 MB、Dは読取。GPU、新重み、ビルド、支出、外部公開0。既知取得後の復号初回はcodec識別子の渡し方で停止したため、保存済み62本だけを再照合・復号した。最初のsnap入口はWindowsのZarr内部loopbackを制限して停止し、既存と同じループバック処理を許可してから実snapを一回実行した。どちらも通信や成功済み計算のやり直しはなかった。0191の上流中央値処理で支持のない窓にAll-NaNの警告が出た。保存したvalid maskと処理内容を保持し、警告を埋める追加試験は行っていない。 [復号初回](m7-known-process.json) · [保存本文の検証](m7-verify-process.json) · [snap初回](snap-known-process.json) · [推論時間](dense-snap-supervision.json)
