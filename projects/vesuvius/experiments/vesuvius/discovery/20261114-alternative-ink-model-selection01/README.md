# 保存済み既知CTで比較する公開インクモデル

2026-11-14 JST。次の一実験に **Hecate 9.6 µm** を選ぶ。R175の保存CTから、既知字画の評価域に必要な81パッチを含む320²を取り出し、公式実装でreverseの2D予測を一回だけ作る。大きさと深さ集約が既存二重みと異なり、保存CTの物理間隔を変えずに比較できる。CPU完走と字画の見え方は未測定。[実験条件](next-plan.json) · [主担当の契約・座標照合](lead-contract-check.json)

## 三候補の比較

| 候補 | 公開来歴と評価 | 保存CT・既存CPUとの適合 |
|---|---|---|
| **Hecate 9.6 µm** | MIT。canonical 2 µm由来のResNet-152 3D encoder＋3D decoderに、深さ方向の学習済みattentionを持つ。既存2D注釈とParis4等の3D教師で2.4 µm版を学習し、2D/3D出力を9.6 µm版へ転移。開発に公式ink datasetと公開スキャンを使用。PHerc0139の面に沿う例を公式カードに掲載。同じPHerc0343受賞面の固定atlasにも単独reverseがある。カードは完全な巻物・座標別学習manifestを示さず、PHerc0343の重複は未確認。 | **16×64×64、stride32、uint8/255、Hann**。公式コードはCPU fp32を持ち、R175保存CTは各軸が名目9.6 µmに適合。比較の利点は異なる構造と入力適合。Reader V3作者の比較では偽陽性が多い評価もあり、文字改善は前提にしない。[公式カードとコード](https://huggingface.co/scrollprize/hecate/tree/9cb86e500e944b11a06a7020403cde5dffb5bcb2) · [atlas固定メタ](../20261114-atlas-known-control01/surface-meta.json) |
| **Reader V3** | MIT。Reader v2の構造・データを保って256²、次いで384²で追加学習。作者はPHerc0841、1447、PHerc0343 U08の可読例と、同じ領域での比較を公表。公式Progress受賞。PHerc0306Bの受賞手法では4教師の一つに使われた。作者設定は8巻物・断片を含み、0343Pは公式で別の断片とCT、0343の受賞面と同じ入力とは扱わない。初期重みまで含む位置重複は未検証。 | **17×384×384、標準overlap .5 → stride192、Hann、patch robust-MAD（1/99）**。公式koine CLIはチェックポイントから構成しCPU経路を持つ。作者の公表速度はGPU。R175には深さは足りるが、R175の原点Yはstride192で64余り、主比較に届く全面9パッチを包含しない。作者の手順はnative 8.64/9.36 µm。固定atlasは9.6 µmでも使用するが、R175の一枚パッチから全面の結果を再現したとは扱えない。[作者の固定報告・設定](https://github.com/DomRusso2/reader-v3/tree/4a9f1c633d2f30d9b522922ec1cb52c082013183) · [公式受賞一覧](https://scrollprize.org/winners) · [306Bの公式報告](https://scrollprize.substack.com/p/writing-seen-in-pherc-306b-for-the) · [0343P](https://scrollprize.org/data_browser/PHerc0343P) · [0343](https://scrollprize.org/data_browser/PHerc0343) |
| **Rectina m2** | 重み・カードCC BY-NC 4.0、レシピコードMIT。既存と同じ `vesuvius_unet_3d_stem_2d` 系。初段に0139、1667、Paris4、0814、0009B、0343P、0500P2、0172、続段の配分は未公表。著者評価はReader V3より14単位中11でAUCが高い（平均差+0.0104）。単一学習、同じ評価単位で派生候補を選択。segment keyの非重複確認から近接領域や全初期化の非重複は確定しない。 | **23層内の17層×7開始、384²、四つのquarter-patch位相、2視点（180°）、forward**。uint16の保存階調を65280で割りrobust-MAD。R175に深さ枚数はあるが、幅384²では公表した四位相の周囲支持が揃わず、作者のCPU読みは未検証（RTX4090、7,631 MiB peak、約102秒/MP）。固定の小CPU比較には採らない。[作者の固定m2カード](https://huggingface.co/evilaliv3/rectina/blob/2f9eaf043512be4f89d22a3d39804dc55e387585/m2/README.md) |

配布版・本文長・SHA-256は[固定一覧](weights.json)。既存seed42とdense-nativeは同じモデル構造の別学習重み。候補比較は作者の公表値と保存資料の読解で、画像の新規取得や数値の再現はしていない。

## 次の一回

- **入力と深さ**　R175 `input.zarr/0` のuint8 33×384²、atlas開始(1344,1024)、物理ZYX間隔 (9.599039497, 9.600000254, 9.600000254) µm。local XYWH [32,32,320,320] を値のまま切り出し、atlas XYWH [1376,1056,320,320] へ対応。Zは名目9.6から約0.010%差。公式CLIへ `--spacing-um 9.6 --device cpu --precision fp32 --batch-size 1 --stride 32 --reverse`、2D PNGだけを指定。33層からコードが採る実深さは24→9（R175の24→8とは1層違う）。[R175入力](../20261114-pherc0343-patch-phase01/input-contract.json) · [固定コード](originals/hecate.py)
- **座標と目視**　主比較atlas XYWH [1408,1088,256,256]。64²・stride32で、6048×2304の全面からこの範囲に届く全81パッチが320²に含まれる。R175の既存図で暗部を囲む輪の一部と隣の明部を観察し、融合・消失・連続性を同一XYで判定する。R179の受賞者箱9、10はいずれもこの内部と部分交差するため、輪郭の比較に使い、完全な文字の転写や認識率は求めない。保存済みCT、既存二モデル、Hecateを同じ固定0–255・原寸で並べる。固定atlasのHecate reverse 1枚（2,114,372 B）も同位置の再現性参照に使う。公式CLIとatlas生成の深さ窓・法線・アダプタの一致は未確認で、画素相関を判読精度に使わない。[パッチ集合](contract-math.log) · [既知原寸比較](../20261114-pherc0343-patch-phase01/comparison-interior-256.png) · [受賞者位置の照合](../20261114-known-neighbour-selection01/lead-known-check.json)
- **資源と停止**　追加は固定重み522,576,086 B（512 MiB上限）と参照PNG一枚（3 MiB上限）、通信180秒。C作業768 MiB、CPU1・Windows Job commit4 GiB・数値1thread、推論開始から900秒上限。既存Torch 2.14.0+cpu、NumPy 2.5.2、Zarr 3.1.5、numcodecs .16.5は公式要件を満たす。重みはmmap付きの安全なweights-only読込とstrict load。モデル配置とmmapに加え、CPUカーネル作業領域は未実測。convだけで213.09 GMAC/patch、81パッチは約34.52 TFLOP（1 MAC=2 FLOP）。仮の実効10–50 GFLOP/sなら約11.5–57.5分で、900秒完走には平均約38.4 GFLOP/sが要る。実効値は未測定。最初の3パッチを同じ処理の一部として計時し、初期化後の遅い方の実測から残り78の予測が残り時間を超える場合に途中停止。上限・入力不整合・strict load不成立・非有限/実出力無効時も閉じる。条件を替えた救済は別票。新CT、未知面、3D出力、GPU、追加クラウド費はこの次案の範囲外。[既存Windows入口](../../../../tools/research/run_windows.py) · [計算と固定値](next-plan.json)

## 取得

公式、配布元、作者の固定本文と小メタを保存。実画像、重み、CTボクセルは取得せず、依存導入、ビルド、モデル実行、外部公開、クラウド支出は0。固定版・取得UTC・受信量・原文ハッシュは[取得原票](acquisition.json)。

