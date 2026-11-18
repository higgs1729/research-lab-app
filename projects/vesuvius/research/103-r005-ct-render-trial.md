# R005 第一面の梱包前後を実CTで描画した一例

2026-11-12 JST。PHerc0814 の保存済み第一入力から異成分の隣接辺を1本固定した。梱包前の中心切片では、成分0と成分2の間をつなぐ20画素幅の補間帯に横筋が出た。梱包後は同じ元面IDを含む2つのROIが別々に描画され、両方で異成分を混ぜる補間が0画素になった。[中心切片と成分マップ](../experiments/vesuvius/r005/20261112-ct-render01/figures01/ct-center-comparison.png) · [元CT断面とXYZの重ね合わせ](../experiments/vesuvius/r005/20261112-ct-render01/figures01/ct-source-sections.png)

## 選定と描画

CT取得前に、既知106辺から梱包後にも両端の元面IDを追えて、両側に有効な補間支持を持つ19候補を絞った。4つの単一成分領域の最小画素数、両成分の混合面積、取得量、他成分面積、座標順で固定した。選んだ辺は梱包前の格子YX `(120,373)–(121,373)`、元面 `53045` と `63364`。2つの端点は実空間で303.83 voxel（約2.84 mm）離れる。梱包後は元面IDで格子YX `(120,371)` と `(32,431)` に追った。ROIはすべて64×64画素で、各条件のUVを別々に切り出した。表の画素は同じXYZの1対1比較を意味しない。[選定規則・元面ID・頂点・XYZ・UV](../experiments/vesuvius/r005/20261112-ct-render01/freeze01/crops.json) · [106候補の記録](../experiments/vesuvius/r005/20261112-ct-render01/select02/geometry-candidates.json)

| 中心切片 | 有効画素 | 成分0のみ | 成分2のみ | 両成分混合 |
| --- | ---: | ---: | ---: | ---: |
| 梱包前 | 4,096 | 1,408 | 1,408 | 1,280 |
| 梱包後・成分0 | 2,048 | 2,048 | 0 | 0 |
| 梱包後・成分2 | 1,808 | 0 | 1,808 | 0 |

梱包前の混合帯では、出力の縦隣接1画素でXYZが最大15.47 voxel進む。中心切片で横筋と混合域が重なる。中心は法線オフセット0で、横筋は±法線オフセットをかける前から出ている。各ROIの−2、−1、0、+1、+2 voxelを保存し、全層で表と同数が有効だった。各ROIの法線は保存したUV格子から計算されるため、±切片間で共通の物理方向は仮定しない。表示窓は中心と元CT断面を合わせた分布から20–239に統一した。中心図の20 pxは名目UV幅。断面の20 voxelは187.24 µm。[全層の計測・マスク・XYZと法線](../experiments/vesuvius/r005/20261112-ct-render01/figures01/) · [ネイティブTIFF](../experiments/vesuvius/r005/20261112-ct-render01/render01/)

## CT座標の根拠と限界

公開9.362 µmメッシュに対して、同じ元入力の主成分0から非共線の3パッチ `53045`、`47056`、`40904` を比較した。各4点と公開の連続三角面の距離は0.005–0.464 voxel、絶対法線内積は0.998–1.000。元入力と公開CTに共通の座標系を使う根拠として、レベル0のZYX、倍率1、平行移動0を採用した。`z_crop_start=822` は適用していない。元CTの面 `53045` の断面でも元入力と公開XYZの線が重なる。[公開XYZの補足照合](../experiments/vesuvius/r005/20261112-ct-render01/coverage01/coverage.json) · [元データの座標根拠](102-r005-ct-render-feasibility.md)

選定した成分2の2パッチ `63364` と `64784` は公開連続面からそれぞれ45.61–52.91、24.69–31.94 voxel離れ、公開面との初回対応ゲートは失敗した。主担当の記録により、候補、CT座標、取得集合を維持して診断を続けた。元CT断面では成分2の線が明るい層の縁に沿う箇所と、暗い部分を通る箇所が見える。成分2と公開の同一表面との対応や、成分2が一枚の正しい紙面に沿うかは未確認。今回判定したのは固定した一例での混合補間と実CT画像上の現れ方まで。[初回ゲート](../experiments/vesuvius/r005/20261112-ct-render01/match01/match.json) · [続行判断](../experiments/vesuvius/r005/20261112-ct-render01/coordinate-gate-decision.json)

## 実行条件と凍結

- `vc_render_tifxyz.cpp` の隔離コピー1 TUを既存 `libvc_core`、`libvc_reader_native`、Boost にリンクした。補間とTIFF書出しは既存実装を使用。コピーで有効座標・法線・丸め前CT値を保存し、readerの64×64単一タイル、CPU affinity 1、数値スレッド1で実行した。選んだbuild02のコンパイルは29.48秒、最大RSS 1.48 GiB。3回の描画は7.15、0.39、0.43秒で、描画最大RSSは約73.4 MiB。[観測差分](../experiments/vesuvius/r005/20261112-ct-render01/build02/observation.patch)
- 公開XYZは1,133,394 bytes、CTは凍結した10チャンクの20,971,520 bytes。新規メタデータ転送は0 bytes。取得はそれぞれ5.06秒、36.65秒。原shape・キー・原点を保った疎Zarrへ置き、実行前に全キーのサイズとSHA-256を照合した。`unshare -Urn` 内で描画し、観測座標と事前のXYZ・法線がバイト一致した。39,760有効標本の三線形近傍をローカルの実バイトから再計算した最大誤差は `3.82e-5` 輝度単位。15枚のTIFFは丸め後の値と有効マスクから得られる結果に一致した。[取得キーと必要標本](../experiments/vesuvius/r005/20261112-ct-render01/freeze01/frozen-selection.json) · [取得証拠](../experiments/vesuvius/r005/20261112-ct-render01/ct01/fetch-result.json)
- 支出0 USD。前のビルドと候補選定の失敗、初回座標ゲートを保持した。入出力、URL、応答本文のバイト数、SHA-256、実行資源、既存保護資産の照合を凍結した。科学的独立検証は別担当が行う。[失敗履歴](../experiments/vesuvius/r005/20261112-ct-render01/failure-history.json) · [凍結マニフェスト](../experiments/vesuvius/r005/20261112-ct-render01/artifact-manifest.json)
