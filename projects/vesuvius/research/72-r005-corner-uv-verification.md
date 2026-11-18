# R005の別UV番号を持つOBJの独立検証

2026-11-12 JST。PHerc0814二面目の保存済みGを使い、OBJの3D頂点番号とUV番号を分けたときに、既存の読取り・描画・tifxyz保存まで届くかを確認した。直前のmanifold-split-close manifestのSHA-256 `d6f8326897c51961c0e382d734b18e28a3097b18576e7f1a2685678d6cdf3491` と、記載されたworkspace内77ファイル・外部2ファイルを再ハッシュした。今回の独立検証でネイティブ描画、ビルド、求解、データ取得は行っていない。[前回の独立検証](70-r005-manifold-split-verification.md)

## 元データとOBJの対応

元TIFFから全249,944点のXYZと478,224面の接続を再構成し、GのUVをnative probeと配置後配列の両方で照合した。元頂点121019 `(126,990)` はC非固定・非粗点で、元面230495・234444のみに属する。面230495の第3コーナーだけ、旧UV `[10335.810546875, 2744.798583984375]` とその面の対辺中点との中点を有理数で求め、float32へ丸めた新UV `[10370.2412109375, 2721.806884765625]` に置き換えた。面234444のコーナーUVは全て保持した。

| 入力 | 3D頂点数 | UV点数 | 面230495の第3コーナーの3D番号／UV番号（0始まり） | 面230495の符号付きUV面積 |
| --- | ---: | ---: | --- | ---: |
| baseline | 249,944 | 249,944 | 121019／121019 | 1130.29579949 |
| corner | 249,944 | 249,945 | 121019／249944 | 565.14718807 |
| duplicated | 249,945 | 249,945 | 249944／249944 | 565.14718807 |

duplicatedの追加3D点は元121019のXYZと同一。cornerとduplicatedは全コーナーのXYZ・UVが同一で、面順と元面IDも全数保持した。全3ケースの面は正向き。変更面の面積はfloat32丸め後に厳密な半分とは異なる。元コーナーを参照して全粗点3,954と全C固定点183,893のUVがG比で同じことを確認した。

adapterは既存の `igl::writeOBJ` を使い、数値を17有効桁で書く。既存 `readUvObj` が3D番号とUV番号を読み分け、解析配列を `parsed.bin` に保存する。その配列が各 `mesh.bin` とバイト一致した。独立にOBJの `v`、`vt`、`f` を読み、正の1始まり番号の `v/vt` 三角形について、float32の値と全インデックスが `parsed.bin` とビット一致した。照合範囲はこの出力形式に限る。ハーネス、writerのヘッダ、binary、共有ライブラリ、保護対象ファイルを再ハッシュし、同じ `SurfaceMeshing-trace.o` が既存Gのoverrideバイナリと今回のadapterにリンクされたことを確認した。[adapter](../experiments/vesuvius/r005/20261112-corner-uv01/corner_obj.cpp) [ビルド記録](../experiments/vesuvius/r005/20261112-corner-uv01/build01/state.json) [配列・OBJの検証結果](../experiments/vesuvius/r005/20261112-corner-uv-verification01/check01/result.json)

## 別UV番号が実際のXYZに届くこと

baselineのtraceは旧Gとバイト一致し、全float32 XYZも旧GのTIFFとビット一致した。3ケースとも全traceがバイト一致し、有効点247,527、拒否イベント564。格子245×3043、scaleは両軸 `0.05000000074505806`。cornerとduplicatedでは `points.bin` もバイト一致し、各ケースの出力TIFF XYZは同じケースの生XYZとビット一致した。寸法はTIFFと生配列から、scaleとformatはmetadataから照合した。UUIDとnameは診断用metadataで、比較一致の対象外。

baselineからcornerへの変更で、所有面の変化、有効点の消失・追加は0だった。XYZビットが変わったのは面230495が所有する画素 `(y,x)=(136,519)` の1箇所。元quadは115247 `(125,989)`。UV番号を使って格子座標を1/256に丸め、整数の辺関数から画素の重心係数を独立に求めた。別に3D番号で参照したXYZを、その係数のfloat32値で合成すると、保存XYZを全3ケースでビット単位に再現した。

| 入力 | 画素の厳密な重心係数 | 再現したfloat32 XYZ |
| --- | --- | --- |
| baseline | `(1221,1165,1323)/3709` | `(2894.744140625, 3888.31103515625, 3256.603271484375)` |
| corner・duplicated | `(5604,5023,26460)/37087` | `(2897.533203125, 3887.57080078125, 3253.27197265625)` |

cornerでは3D番号121019とUV番号249944を使った座標からこの結果が得られた。面234444はコーナーUVを保持したが、3条件とも所有画素0。実際の描画で確認できたのは面230495側の1標本。[各コーナーの整数座標・係数・XYZ](../experiments/vesuvius/r005/20261112-corner-uv-verification01/check01/result.json)

## 保存結果で追跡できる範囲

3条件とも標準tifxyzディレクトリには `x.tif`・`y.tif`・`z.tif` と `meta.json` があり、metadataのキーは `bbox`・`format`・`name`・`scale`・`type`・`uuid`。この出力自体には元面IDや元コーナーUV番号が入らない。別保存のowner traceと、`face_to_source_face`・`geometry_to_source_vertex`・`uv_to_source_vertex` を組み合わせ、全247,527所有画素について所有元面と対応する元コーナー3点を確認した。所有元面は244,596枚。画素ごとの重心係数はtraceに保存されないため、点の三角形内での対応は保存済みtrace単体からは読めない。今回の1画素はOBJのUV、面、格子情報を使って再計算した。人工的な一面変更の経路確認に限り、継ぎ目を跨ぐ下流補間、全体の重複改善、可読性、製品採用は未確認。[correspondenceの入力記録](../experiments/vesuvius/r005/20261112-corner-uv01/input01/result.json) [owner trace](../experiments/vesuvius/r005/20261112-corner-uv01/corner01/raster_trace.json)

独立検証は既存runnerで1 CPU・1スレッド、300秒・RSS 4 GiB監視。壁時計10.95秒、最大観測RSS 334,807,040バイトだった。[検証コード](../experiments/vesuvius/r005/20261112-corner-uv-verification01/verify_corner_uv.py) [資源記録](../experiments/vesuvius/r005/20261112-corner-uv-verification01/check01-execution/state.json)
