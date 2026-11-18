# PHerc1545の次の元CT領域

[研究177](../../../../research/177-pherc1545-target-selection.md)の原票。2026-11-14 JST。次の一案は親面 PHerc1545_3499_4074_9431 のnative XYWH [640,640,1024,1024]。

## 公開根拠

- 公式First LettersとGrand Prizeにvolume 20250821151648がある。実スキャンは20250720045926、ESRF 113 keV、9.362 µm、データCC BY-NC 4.0。masked L0の非圧縮uint8 Zarr v2はZYX [20961,7506,7506]、128³、2 MiB/キー。公式データブラウザはScanned・segments 0、公式WinnersでPHerc1545の掲載を確認できなかった。surveyの候補は先行公開済みで、他の未公開成果の有無は不明。First Lettersは単一4 cm²内の可読10文字、CT由来画像と対応mesh、方法を要求し、出力と学習領域の重複を認めない。[公式対象と条件](https://scrollprize.org/prizes) · [公式データ](https://scrollprize.org/data_browser/PHerc1545) · [公式Winners](https://scrollprize.org/winners) · [CT L0メタ](ct-l0-zarray.json)
- 固定survey 1f12c1ceb14c1f24acc48249eaad60bcdf541721。親面はWindows end-to-end試験のvc_grow_seg_from_seed、step20、成長種点XYZ [3499,4074,9431]、m7 20260413222639 L0 threshold .2。面積4.0314 cm²、TIFXYZ 112×112、native canvas2240²。コードMIT、派生データCC BY-NC 4.0。固定atlasの1545は公開0・held13で、これは公開状況。seed42/dense-nativeの公表学習一覧に1545は見当たらず、起点重みを含む全学習領域の非重複は未検証。[mesh meta](parent-mesh-meta.json) · [survey原文](../20261114-atlas-known-control01/survey-readme.md) · [固定atlas index](../20261113-next-target01/ink-atlas-index.json) · [R172重み調査](../20261114-pherc0846a-dense-native01/README.md)
- 親のreverseが上流のinner。seed42、dense-native、seed43、Hecateの6組で、sheet-check有効画素のd=0における上位3% IoUのinner/outer比が2.309～5.124。seed42/denseのreverse .2029、forward .0396。768²・stride384・mask面積50%以上の16タイルで、局所IoU>.1かつ他面の3倍超がreverse 5、forward 0。暗部率 .190はreverseの2モデル上位3%交差画素のうち、mask内CTの第10百分位未満の割合。暗部の原因は不明。letter-chainはreverse 1.019、forward 1.398。黄色は正規化した2スコア平均の加工表示。元の交差マスクと生確率は固定木に見つからなかった。[親カード統計](PHerc1545_3499_4074_9431.json) · [六対](model_pairs_PHerc1545_3499_4074_9431.json) · [集計・描画コード](../20261114-pherc0846a-lead-audit01/report_card.py)
- 近傍6件のタイル一貫性による側は、オフセット−45から順に不明・内・内・内・内・外。全域IoUが高い側は6件ともreverseで、評価定義が異なる。近傍の最大asymは [3524,4074,9385] の4.150、consistency .375、暗部 .147。近傍は同じ起点周辺の幾何を共有する。親と担当が両JPEGを原寸目視し、離れた塊と短い曲線から独立字画の連なりや行を一意に選べなかった。転写なし。[向き原票](../20261114-pherc0846a-lead-audit01/side.json) · [親JPEG](PHerc1545_3499_4074_9431.jpg) · [近傍JPEG](PHerc1545_3524_4074_9385.jpg) · [親目視](lead-visual.json)

## 追跡起点の逆照合

上流のneighbour_seeds.pyは、768²タイルの優勢面と反対面の局所IoU差を最大化し、中心を20で整数除算したTIFXYZ節点で差分法線を求める。節点から−45, −30, −15, +15, +30, +45 voxelの順に法線方向へ移動し、丸めて公開surface predictionの各軸±5 voxel内へスナップする。固定のseeds_leads7.jsonが6結果を同順に保存する。[seed作成コード](neighbour_seeds.py) · [タイル定義](tile_asym.py) · [公開seed列](seeds_leads7.json)

16候補中、6件全てが±5以内の唯一のタイルは **XYWH [768,768,768,768]**。中心XY [1152,1152]、節点YX [57,57]、XYZ [3525.843,4086.694,9393.549]。最大残差4 voxel、次点356。親面の成長種点最近接はYX [55,55]。親担当が独立float64式で一意性を再確認した。上流コードの条件から選択タイルを推定した結果で、元の局所IoU値やsurface予測でのスナップ選択は未再計算。JPEG位置は使っていない。[全16候補](selection.json) · [親別計算](lead-check.json)

## 次の一実験

1. **XYWH [640,640,1024,1024]**。同じ親面・native 9.362 µm・全面原点0のstride64に固定。上流タイルとその四方128 pxを含む。タイルを支えるパッチ開始は各軸704～1472の13点。全面と同じ支持を持つ内部XYWH [704,704,896,896]を判定に使い、外周も原寸保存する。9.587 mm四方、名目0.919 cm²、全面の画素20.90%、四隅有効セル由来画素の22.90%。残りの面や近傍は今回の範囲外。
2. R103 observerを64²×256、既存公式rendererを1回、native scale 1・linear・非反転法線・33層d=−16…+16。2,704セルの四隅を各軸±16.01 voxelとtrilinear角まで広げた保守計算で132キー・264 MiB。単一3D bboxなら360キー。親が別ループで集合を再確認。実observerで必要キーと有効率を確定し、HEAD長とETagを照合してから本文取得。上限320 MiB（160キー）、通信900秒、C作業1 GiB・空き10 GiB。超過または支持不成立なら本文前に停止し、ROIは固定。既往観測64タイル80–93秒から256タイル320–372秒、上限600秒。描画上限120秒。33×1024²のuint8は33 MiB、非圧縮TIFFと併せて約66 MiB、観測XYZ/法線約24 MiB。作業量は推定。
3. 既存seed42/dense-nativeで中央17層8→24、24→8を各一回、計4回。128²/stride64/Hann、CPU float32/batch1、最大225パッチ/回、CPU1・4 GiB・120秒/回、取得後通信分離。既往から約62～73秒/回の見積もり、512²最大RSS約849 MB。1024²の時間とメモリは未実測。固定0–255のCTと連続4予測を並べ、複数字画と行方向を追えるか、強い点が割れや空隙境界へ集中するかを見る。候補なしならこのROI/中央窓の記録で閉じる。

近傍[3524,4074,9385]の根拠は二モデル。離れた[3051,3484,14673]のconsistency .64は、同じ6近傍や今回の四モデル追跡起点とは別の所見。全面2240²は1,156パッチ/方向で局所の5.1倍。今回の優先は四モデル調査の親面上で位置根拠のある一領域。[資源計算](selection.json) · [R173](../../../../research/173-pherc0343-ct-readable-control.md) · [R175](../../../../research/175-pherc0343-patch-phase.md) · [R176](../../../../research/176-pherc0846a-aligned-patches.md)

## 取得と計算

固定GitHub connectorを使用。mesh3TIFF 151,086 B、JPEG2枚695,600 B。テキストは計画16件に対し、種点ファイル探索で候補6本文を取得し新規19件・20,100 B、保存14件・12,896 B。既存side.jsonを1件25,049 B重複受信し、同一SHAなので既存参照へ戻した。重複込み20件45,149 B。公式ページはブラウズ確認。CTは .zarray 239 Bのメタのみ、ボクセル本文0。ローカル集計は初回にNumPy整数のJSON直列化で停止し、部分票を保存して型だけ修正。描画・推論・ビルド・クラウド追加費0。[取得明細](acquisition.json) · [局所計算](select.py) · [初回部分票](selection01-partial.json) · [親計測](lead-process.json)
