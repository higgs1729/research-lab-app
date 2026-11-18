# 取得前照合（2026-11-14 JST）

meshは固定survey Git treeの同じ3 TIFF（各178,293 B）とmeta（4,639 B）。metaのuuidは `concat_w047-w048_R5B2_z9500-11000`。CTはatlasが指定する公式8.640 µm/116 keVのmasked L0。同じ公開CT・面の512²を、atlasのXYWH [1320,980,512,512] のまま固定した。

製品の `computeCanvasOrigin`、`surfaceCenterFor`、`gridRaster` を組み合わせると、出力座標 `i` のメッシュ座標は `(i-(C-1)/2)*s/r+M/2`。このmeshは128×336、`s=.05`、`r=.9`、`C=r*M/s` が両軸で整数の2304×6048のため、式は `(i+.5)*s/r` になる。atlas READMEの製品と同じcanvas規則、固定surveyの画素中心式に合う。scale .9、slice step 1.111 CT voxel、linear、非反転法線で、65層の中央と同じd=0を持つ33層を1回描画する。33層の中央17層はatlasの層24..40に相当。

観測版64タイルの全画素が有効。公開survey幾何関数を有効scale .05/.9で呼んだ参照とのXYZ差は中央値 .000488、p99 .001119、最大 .002072 CT voxel。法線dotは最小 .65033、中央値 .99664、最大浮動小数誤差範囲1。向きの符号は全画素同じ。survey関数は近接ノード法線を選ぶため、深さ方向の物理点は一致を前提にしない。atlas自身の実生成を直接追跡できた範囲は公開メタデータ・文書・保存画素まで。55キー、110 MiBの全支持をCT本文取得前に固定した。

Ink Lens参照はGitHub HEAD照会で得た固定 `0139cf33bb443db42602bf1b201dd05f8a666413`。R171/172の両重み・dense configのSHAが現存する `zoo.py` の仕様と一致する。 `runners.py` はTorch版のパッチrobust処理、stride半分、Hann、sigmoid、既定batch64、CUDAの場合AMPを示す。今回の公式CLIはNumPy版パッチ処理・CPU float32・batch1。全面atlasと512²にはパッチグリッドの位相差もある。XY開始1320と980は各64の倍数から40と20ずれている。atlas公開PNGと自前推論の一致を再現成功条件に置かない。

初期取得はmesh metaと3TIFF、公式Zarr v2の3メタデータ、Ink Lensの木と2ファイル。再帰木の最初の照会はcurlの300,000 B上限で切れてJSON解析が失敗し、その部分ファイルを保存した。ルートからspaces固定木を取得して目的の2コード本文を特定できた。部分ファイルも数えると、メタデータ・文書・コード9レスポンス、保存本文計415,973 B。early requestの時間枠は全体予算へ保守的に165秒を算入した。公開seed42 PNGはログ失敗前に本文を保存できたのでSHA検査して再使用し、dense PNGだけ続きで取得した。両PNG計6,160,131 B。
