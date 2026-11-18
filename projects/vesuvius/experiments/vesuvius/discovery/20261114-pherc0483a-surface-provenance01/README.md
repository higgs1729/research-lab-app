# PHerc0483Aの固定三点とCT支持計画

2026-11-14 JST。[研究204](../../../../research/204-pherc0483a-surface-provenance.md)。atlasの選定窓 `[704,1024,512,512]` で、固定meshと公式元CTの座標対応を確認した。三点の元CT断面と点間を結ぶ断面では、同じ物理紙面を三点間に追えず未判定だった。

## 一次資料と座標

- 公式カタログはscan `20250510022723`、reconstruction volume `20250521140913`、8.64 µm、116 keVを別々に記録する。atlasの `scan` 欄は後者を指す。meshの生成対象は同volumeに登録された派生surface prediction `20250521140913-surface-20260413222639-surface-m7-L0-th0.2.zarr`。元CTの読取先は公式masked volumeのlevel 0。 [公式カタログ](https://scrollprize.org/data_browser/PHerc0483A) [固定mesh](https://github.com/ketchupbyheinz/vesuvius-scroll-survey/tree/1f12c1ceb14c1f24acc48249eaad60bcdf541721/results/meshes/PHerc0483A_3155_3610_11128) [meshメタ](mesh/meta.json)
- float32の112×112 XYZはgrid scale 0.05。atlasのrender scale 0.9でcanvas 2016×2016、原点 `[0,0]`、名目XY 9.6 µm。ピクセル中心のgrid座標は `(atlas XY+0.5)*mesh_scale/0.9`。非反転法線でstep 1.111 voxel。固定公開canvasの画像とmetaの寸法が一致した。実ボクセルの対応はd=0の再補間と公開PNGを比較して検証できる。 [atlas固定meta](../20261114-next-atlas-surface01/candidates/PHerc0483A-meta.json) [中央PNG](../20261114-atlas-mask-semantics01/originals/PHerc0483A-ct-mid.png) [支持計画](support-plan.json)
- level 0はZYX `[15898,8849,8849]`、非圧縮uint8・128³ chunk、C order、区切り `/`、fill 0。主担当確認後、6キーすべてのHEAD/GETで200と2,097,152 Bを確認し、ETag・実長・SHAを照合した。 [元CTレベル0メタ](ct.zarr/0/.zarray) [通信原票](ct-acquisition.json)

## 固定三点と判定範囲

中央PNGで弧の頂付近を通るx=832に固定。各点は64²文脈の中央。元CTのXYZはvoxel単位。

| 地点 | atlas XY | 元CT XYZ |
| --- | --- | --- |
| 上側 | 832,1152 | 3038.941,3655.216,11360.211 |
| 弧 | 832,1268 | 3061.761,3645.222,11483.924 |
| 下側 | 832,1392 | 3098.128,3623.477,11605.964 |

R180と同条件の既存観測版で、全12,288画素の座標と単位法線が有効だった。3×64²のd=0と中央行・列33層、各点の整数中心±32 voxelの直交3面を合併すると6キー。同じ6キーで3×64²の全33層も支持される。0.001 voxelの安全幅と三線形補間の全端点を含む。保存実験中に同volumeの再利用元は見つからなかったため、新規見積は6キー×2,097,152 B＝12,582,912 B。 [固定三点](anchors.json) [キー一覧とXYZ/法線](support-plan.json)

## 原寸断面と判断

三点が元CTで126〜129 voxel離れるため、独立65²断面に加えて、Z=11328..11638、Y=3584..3711の連結断面を固定した。Xは三点のXYZを通るX–Z折れ線から、Zごとに丸めて選んだ。原寸の39,808画素はすべて保存キーの実値で、追加キーは0。9直交断面は38,025画素。観測P/Nから33層を再補間した中央12,288画素は公開atlasと最大1 DN、12,205画素が完全一致。 [連結支持](continuity-plan.json) [断面原票](sections-result.json) [原寸連結断面](sections/continuous-yz-annotated.png)

上側では粒状の高コントラスト、弧の点は鋭い境界の縁、下側は低コントラストの繊維状領域に重なった。連結断面と各直交面で、同じラミナの輪郭を三点間に連続追跡できなかった。境界の物理帰属は未判定で、別紙面への飛びや空隙を確定できない。 [上側](sections/upper/orthogonal-annotated.png) [弧](sections/arc/orthogonal-annotated.png) [下側](sections/lower/orthogonal-annotated.png)

主担当は連結39,808画素と9直交面38,025画素を別のバイトアドレス計算で全値照合した。135点の三線形補間と保存uint8の差は最大0.490585 DN。原寸図の別目視でも、弧の鋭い境界は見えるが同じラミナは追えず未判定とした。 [独立検算と目視](lead-sections-check.json)

初期受信173,465 B、2.760秒。CTは12,582,912 B、HEAD+GET 15.706秒、再試行0。geometry-onlyは3区画2.365秒、最大RSS 59,686,912 B。既存バイナリをネットワーク分離、CPU1・AS4 GiB、D読取で起動した。Windowsの取得と集計はCPU1・process commit4 GiB。法線追従の細長い区画は、採取前に既存観測器の単一タイル制約で停止し、採用したX(Z)断面は既存三点から固定した。モデル・ビルド・GPU・クラウド支出は0。 [初期通信](acquisition.json) [観測原票](geometry/stage-start.json) [停止原票](continuity-geometry/832-1152/geometry.log)
