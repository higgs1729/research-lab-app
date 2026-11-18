# R005 flatboi の UV lift で残る表面欠落の一次資料確認

2026-11-11。対象は R003 の初期 UV 補正後も残る出力欠落。公開 issue、PR、固定版ソースを読み、既報と現行実装の範囲を確認した。[取得記録](../experiments/vesuvius/r005/20261111-source-review/README.md)

## 結論

- [一次] 確認した公開 main `f0e4410` の `SurfaceMeshing.cpp`、`SurfaceMeshing.hpp`、`flatboi.cpp` は R003 の固定 base `7ad02f4` と同一 blob。無効な粗 quad で最近傍の粗頂点 UV をコピーする動作が残る。確認した公開 issue・PR に、欠落を抑える同等修正は見つからなかった。[main の UV lift](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/volume-cartographer/core/src/SurfaceMeshing.cpp#L59-L105)
- [一次] #2500 の作者が実施した介入は初期 UV の stride 倍。重なり判定の分母・条件は報告固有で、UV で縮退したセルを数えない。修正後の 48 件と有効出力 32,773 点を同時に報告している。唯一のコメントは別セグメントで同じ補正を比較した図。UV lift fallback の変更、保守者の入力仕様回答、関連 PR は公開タイムラインに見当たらない。R003 の全 39,312 quad 中心の距離評価 9,483 件と issue の 48 件は評価対象が異なる。[issue #2500](https://github.com/ScrollPrize/villa/issues/2500) [作者コメント](https://github.com/ScrollPrize/villa/issues/2500#issuecomment-6772985629) [R003 実験](34-r003-initial-uv-trial.md)

## コード上の機序と仕様

1. [一次] `decimateGrid` は原点から stride ごとの行・列をサンプリングする。`meshGrid` は有効な四隅を持つ quad を固定対角線で二分する。粗い quad が無効でも、そこに属する細かい quad は有効でありうる。`liftGridUVs` は粗 quad が有効なら格子座標で区分アフィン補間し、無効なら丸めた座標から各軸 ±2 の範囲で最近傍の粗メッシュ頂点 UV をコピーする。候補がないときは無効のまま。[固定実装](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/src/SurfaceMeshing.cpp#L17-L105)
2. [一次・推論] 最近傍 fallback で同一の粗頂点へ対応した細かい頂点同士は同じ UV を持つため、同じ細かい三角形のうち二頂点が一致すると面積がゼロになる。別の経路として、末尾のサンプル以降でも clamped quad が有効ならこの補間分岐に入り、末尾方向の補間係数が 1 に固定される。この方向にのみ離れた細かい頂点は同じ UV になる。API ヘッダーは末尾を最近傍に送ると記述しており、この条件では実装と一致しない。現行テストの値比較は有効 quad 内のみで、範囲外には `valid` だけを検査している。[補間実装](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/src/SurfaceMeshing.cpp#L72-L102) [ヘッダー](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/include/vc/core/util/SurfaceMeshing.hpp#L35-L48) [テスト](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/test/test_surface_meshing.cpp#L64-L110)
3. [一次] flatboi の UV 欠落警告は、頂点の `valid` が偽で除外した面だけを数える。valid のまま UV が縮退した面はラスタライズまで進む。ラスタライザは固定小数点に丸めた後の符号付き面積がゼロなら何も書かず、複数面が同一出力セルを覆う場合は先着面を残す。[flatboi](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/libs/flatboi/flatboi.cpp#L955-L985) [ラスタライザ](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/src/SurfaceMeshing.cpp#L432-L501)

## 先行実装と関連 PR

- [一次] #941 は大きな入力を SLIM に通すために旧 `vc_obj_uv_lift` を導入し、原格子で対応させる理由として、3D 最近傍では巻きが空間的に接近したところに筋や裂けが出ることを挙げている。旧実装は粗い格子 UV の bbox に座標を clamp して三角形内を再探索し、なお見つからなければ近隣 bin 内の粗頂点の UV をコピーした。末尾の勾配を延長する処理はない。#2358 が旧 CLI を削除し、現在の `SurfaceMeshing` に置き換えた。[導入 #941](https://github.com/ScrollPrize/villa/pull/941) [旧 fallback](https://github.com/ScrollPrize/villa/blob/7154682e174205bcaafe06a4962668becd85bb56/volume-cartographer/apps/src/vc_obj_uv_lift.cpp#L283-L349) [置換 #2358](https://github.com/ScrollPrize/villa/pull/2358/files)
- [一次] #2437 と #1972／#2476 はオプション `--inpaint` で**SLIM 前の 3D 格子**が縮退し NaN になる件。#988 も tracer の 3D 隣接点が潰れて SLIM が失敗する問題。#1012 は UV のない旧 OBJ 入力の初期化、#2158 は SLIM のメモリ・時間、#2128 は ABF++ の面品質フィルタでできる穴、#2484 はラスタライズ後の scale、#2383 は lasagna の出力 UV 逆写像の高速化を扱う。[#2437](https://github.com/ScrollPrize/villa/issues/2437) [#1972](https://github.com/ScrollPrize/villa/pull/1972) [#2476](https://github.com/ScrollPrize/villa/pull/2476) [#988](https://github.com/ScrollPrize/villa/pull/988) [#1012](https://github.com/ScrollPrize/villa/pull/1012) [#2158](https://github.com/ScrollPrize/villa/pull/2158) [#2128](https://github.com/ScrollPrize/villa/pull/2128) [#2484](https://github.com/ScrollPrize/villa/pull/2484) [#2383](https://github.com/ScrollPrize/villa/pull/2383)
- [一次・推論] 固定版 libigl には任意次元の三角形に対する重心座標、メッシュへの最近点・primitive ID、境界値付きの調和補間がある。近傍三角形を格子空間で選び、投影前の点の重心座標を使えばその三角形のアフィン写像を延長できる。最近点に投影した座標だけを使うと外向き勾配を失う。異なる三角形への切り替えによる不連続、折り返し、粗い成分間の誤対応は別途確認を要する。調和補間も、この用途で必要な局所単射性や欠落成分への対応を保証するものではない。[重心座標](https://github.com/libigl/libigl/blob/ae8f959ea26d7059abad4c698aba8d6b7c3205e8/include/igl/barycentric_coordinates.h) [最近点](https://github.com/libigl/libigl/blob/ae8f959ea26d7059abad4c698aba8d6b7c3205e8/include/igl/point_mesh_squared_distance.h) [調和補間](https://github.com/libigl/libigl/blob/ae8f959ea26d7059abad4c698aba8d6b7c3205e8/include/igl/harmonic.h)

## 未確認

実データで最近傍コピー、末尾 clamp、UV 未割当、面の競合、出力サンプリングがそれぞれ欠落に占める割合は未計測。粗格子で消えた細い成分がどこまで残せるか、アフィン延長が反転や重なりを増やさず回復できるかは未検証。公開 GitHub の検索対象と確認したコミットに限った結果であり、未索引の開発や他所での同等実装は未確認。
