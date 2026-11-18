# PHerc0343 既知領域の元CT工程対照

[研究173](../../../../research/173-pherc0343-ct-readable-control.md)の2026-11-14 JST原票。公開atlas `ac5ffd7098120368216948c4e06c494bf8e67178` の `kbh-POS_PHerc0343_erwin`、事前固定XYWH [1320,980,512,512]。原点・scale・中心層の式、配布物、法線と公開実装の相違は[取得前照合](preflight.md)に記載。

## 元CTと公開位置の照合

固定survey `1f12c1ceb14c1f24acc48249eaad60bcdf541721` のmesh3TIFFは計534,879 Bで全Git blob一致。atlasと同じ8.640 µmの公式masked L0、出力XYは9.6 µm、`--scale 0.9 --slice-step 1.111`、linear、非反転法線、33層を一回描画した。64区画の観測80.130秒、全262,144画素有効。公開surveyの幾何式を.9にした参照との面位置差は最大.002072 voxel。法線dotは全画素で正、中央値 .99664、最小 .65033で、深さ付きの全座標には差がある。[固定入力](roi.json) · [支持点計画](plan.json) · [描画実行](render/render-process.json)

固定55キーをHEAD 32.968秒、GET 157.205秒で取得。本文115,343,360 B（110 MiB）、全応答200、HEADのETagと本文のMD5、SHA一致、再取得0。製品3.064秒、ピークRSS203,771,904 B。TIFFとZarr L0の全8,650,752値を照合した。[HEAD](head-result.json) · [CT取得](ct-result.json) · [入力契約](input-contract.json)

製品の中央層16と公開atlasの中央層32を同一XYで直接比較。260,873/262,144画素が完全一致し、全値が±1 DN以内。MAE .004848 DN、Pearson相関 .999997668。平行移動・回転・再サンプリングなし。中心層は法線と深さ間隔に依存せず、この結果は固定XYの位置対応を裏づける。残る±1 DNにはfloat演算順序・位置・補間量子化の違いが寄与し得るが、原因内訳は未分離。atlasの深さ付き各層と同一とは扱わない。[中央CT照合](ct-mid-comparison.json) · [製品中央](ct-mid-render.png) · [公開中央](ct-mid-atlas.png)

## モデルと実行

研究171/172の保存seed42 step075000・dense-native step16000と公式CPU `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` を使った。同じ3D stem＋2D U-Netの別学習重み。中央17層 [8,25)（atlas相当24..40）で保存順8→24と逆24→8、各49パッチ。robust-MAD、128²、stride64、Hann、batch1、workers0、float32 sigmoid、TTA/compileなし。推論のWindows JobはCPU1・commit 4 GiB・各120秒・Python外部ソケット拒否とHF offline。描画はWSLのD: read-onlyとネットワーク名前空間分離、CPU1、AS4 GiB。既存R171/172のラッパーと保存float観測を借りた。[R171](../20261114-pherc0846a-ink-pilot01/README.md) · [R172](../20261114-pherc0846a-dense-native01/README.md)

公表atlas metaはPHerc0343への学習露出を両モデルともunknownと記載し、atlas READMEは公開学習一覧にPHerc0343の記載がないと述べる。受賞者READMEもPHerc0343に未訓練と述べる。初期化元を含む全訓練入力・座標レベルの非重複はこの試験で確認していない。受賞・既知面の工程対照で、未知性能や新発見を評価する試験ではない。[atlas meta](../20261114-atlas-known-control01/surface-meta.json) · [atlas README保存](../20261113-next-target01/ink-atlas.md) · [受賞者README保存](../20261114-atlas-known-control01/winner-readme.md)

## 字画の比較

| 自前推論 | 実測秒 | ピークRSS B | 保存uint8範囲 |
|---|---:|---:|---:|
| seed42 8→24 | 17.863 | 744,910,848 | 52–192 |
| seed42 24→8 | 16.638 | 743,948,288 | 52–233 |
| dense-native 8→24 | 17.788 | 848,060,416 | 64–194 |
| dense-native 24→8 | 16.116 | 848,707,584 | 64–204 |

固定0–255・1:1の図で、公開ensembleの中央右寄りに明るい曲線が暗部を囲む形が見える。dense-nativeの自前逆方向でも、同じ位置に曲線と囲まれた暗部を追えた。明部は太くぼけており、隣接する複数の独立した字画や文字列はこの512²で判定できなかった。seed42の自前逆方向は左右の明部が分かれて同じ輪の閉じ方が弱い。自前の両順方向では対応形が弱い。親担当が結論文を読む前の別目視でも同じ判定。固定領域での既知字画の部分形状を再現できた。文字の判読や転写は未達。[自前両順とCT](comparison-local.png) · [公開単独/ensembleと自前逆順](comparison-published.png)

公開単独逆方向の同座標とのuint8相関はseed42 .384、dense-native .879、MAEは26.43/12.05 DN。公開単独denseにも輪の位置が残り、公開単独seed42ではこの切り出しの輪が弱い。公表Ink Lens仕様の重み・dense configのSHAは再利用資産と一致した。今回の製品法線とsurvey参照法線に局所差があり、atlas全面と固定ROIの窓位相、Torch版robust処理と既存CLIのNumPy版、公開コードの既定batch64/対応GPU AMPと今回のCPU batch1も差分候補。どの要因がseed42の差を生んだかは未分離。相関は保存表示値の対応を表す。[集計原票](comparison.json) · [公開仕様の照合](preflight.md)

親担当の独立照合では、元meshの9点を直接双線形補間した位置との差が最大.000971 voxel。5深さ×9点の45生CT標本を8隅から直接補間し、保存値との差が最大.488507 DN。保存atlasの中央全画素比較も再現した。[親数値照合](lead-numeric-check.json) · [親実行](lead-process.json) · [親の独立目視](lead-visual.json)

## 再現と取得記録

保存した入力を用いる場合は再取得不要。`geometry.py prepare` は固定mesh/CTメタデータを照合。 `adapt_native.py` と `adapt_infer.py` は凍結されたR171/172スクリプトの設定差を出力するための原票。既存WSL入口で `launch.sh geometry`、`geometry.py support`、`acquire.py head`、`acquire.py ct`、`launch.sh render` の順。supportのWindows既存runnerには `PYTHONPATH` にこの実験先、R133隔離deps、runtime/python-depsを順に入れた。 `run_stage.py input` で中央CTと固定全値を照合後、seed42-forward、seed42-reverse、dense-forward、dense-reverseを逐次、最後にcompare。記録済みの製品や推論は同じ出力先で起動しない。

初回公開PNG取得はseed42保存直後にJSON import漏れでログ停止し、本文SHA再確認のうえその一枚を再利用してdenseだけ取得。support初回は隔離Zarr未参照、続く計測2回は作業フォルダ、CRC32Cの順にPython検索パスが不足。既存検索パスの設定で解消し、幾何・描画・推論の再実行は発生していない。Ink Lensの過大再帰木は300,000 Bで中断し部分本文を保存、ルートの小木から必要なコードだけを照合した。初期9メタ/コードレスポンス415,973 B（中断部分を含む）、mesh534,879 B、公開2PNG6,160,131 B、CT115,343,360 B。CT以外の再取得/部分転送の制限経緯は[取得前照合](preflight.md)。追加クラウド支出0円、ローカル電力費未計上。新依存・モデル取得・ビルド・GPU・公開は0件。
