# 公開Hecate像とR196の生成条件

2026-11-14 JST。公開当日のInk Lensコードには、中央16層を先に選び、その中で逆順にする処理がある。保存33層に換算すると23→8となり、R196が使った24→9より1層ずれる。公開PNGの生成記録には実行時のソース・引数・実入力がなく、当該PNGにこの経路が使われたことと、画像差に占める影響は未確定。[担当の配列照合](saved-input-check.json) · [主担当のソース照合](lead-source-checked.json) · [主担当の配列照合](lead-depth-checked.json)

## 時系列とコード

- [一次] HFの履歴ではデータ本体の初回公開は2026-10-27 14:28:12–14:29:02 UTCの5コミット。固定版 `ac5ffd7098120368216948c4e06c494bf8e67178` は23:57:39 UTCのカード・例文の変更。公開カードはInk Lensとink-sdkのHecate adapterを記載し、対象面メタはCT、65層レンダー、中心窓・両方向とlivenessを持つ。生成CLI・生配列・per-map backend receiptはこの面の固定木、meta、公開ルートに見つからなかった。公開日同日付のGitHubコードに生成結果を直接結ぶ記録は得られていない。[HF履歴](originals/hf-atlas-commits.json) · [固定面meta](../20261114-atlas-known-control01/surface-meta.json) · [固定HFカード](https://huggingface.co/datasets/SharpMeow/first-letters-ink-atlas/blob/ac5ffd7098120368216948c4e06c494bf8e67178/README.md)
- [一次] 初回公開前の `4527c6a`（04:43）と `d7b41fd`（08:22）、同日公開後の `8250b23`（23:53）のInk Lensに同じ順序がある。 `compare.run` がモデル深さから `windows_for` を呼び、`SDKModel.run` が `volume[idx]` の16層を先に用意し、Hecate adapterがそれに `predict(reverse=True)` を適用する。この公開入口が存在したことまで固定できる。GitHubの同日Ink Atlas PRは公開データを読むSpace/MCPの追加で、同じrepoの `kit/atlas.py` は別のSegment Atlas。 [公開前runner](originals/pre-upload-runners.py) · [公開前compare](originals/pre-upload-compare.py) · [Ink Atlas PR](originals/release-commit.json)
- [一次] 公開前Ink Lensの `zoo.py` とink-sdk `1dbfac2178958ca4bca7469582477963d4d08ecf` のHecate 9.6 profileはHF `9cb86e500e944b11a06a7020403cde5dffb5bcb2`・522,576,086 B・重みSHA `809f4f10f7cb7afa19b4bee0f7d2ab31edd7e11b664f9f210cc9c17f22fcfe5d` を指定。公開runnerはローカル指定を含め長さ・SHAを照合し、SDK側もcheckpointを検証する。vendorの `hecate.py` はR189/196の公式配布ファイルと全バイト一致、SHA `c232c18a1a86cfb91257a00db13288202bb8ae33732ba26f7291a9b8adb8da59`。ここで確認できたのは公開コードのpinと一致する実装。[zoo](originals/pre-upload-zoo.py) · [profile](originals/sdk-profile.toml) · [adapter](originals/sdk-adapter.py) · [vendor](originals/sdk-vendor.py)

## どこが違うか

| 経路 | 保存33層での逆順 | atlas 65層での逆順 | 中央相対 |
| --- | --- | --- | --- |
| R196・公式predictへ奇数層を渡す | 24→9 | 40→25（同関数の仮定） | +8→−7 |
| 公開同日コード・中央16層を先に切り出す | 23→8 | 39→24 | +7→−8 |

[実測] 保存済み `190/input.npy` の全33層SHAを固定し、両経路の生入力を比較。15層を1段ずらして共有し、同じチャンネル番号で比較すると1,587,621/1,638,400値が変化、平均絶対差14.494643 DN、最大112 DN。全81パッチに入力差があり、同じraw-any支持列は81/81で一致した。先に選ぶ16層の全パッチraw/正規化SHAと支持列数も保存した。33/65という長さだけを変えて公式の奇数層経路を使った場合は中央相対の16層が揃う。[配列原票](saved-input-check.json)

[一次・実測] 同じvendorの既定はuint8/255、clipなし、深さ方向のraw-any支持を反復、64²/stride32、非周期Hann floor .001、sigmoid・正規化加重平均・rintでuint8。SDK profileはbatch1/fp32で、adapterは明示AMPでbf16を許す。歴史的device・AMP・ライブラリ版は不明。SDKがuint8をfloat32/255へ戻す部分について、全256階調の再量子化を確認し、単純な×255→roundまたはcastだけなら全階調不変だった。atlasカードは個別マップの0–255を公称し、z-scoreはensembleに記載される。実PNGのエクスポート処理は未確認。[adapter](originals/sdk-adapter.py) · [vendor](originals/sdk-vendor.py) · [表示の小計算](saved-input-check.json)

[一次・実測] 公開canvasは6048×2304、名目9.6 µm、CT 8.64 µm×メタのstep 1.111は9.59904 µm。保存入力のXY/Zは9.600000254/9.599039497 µm。R196の主ROIへ寄与する全面の64²/32格子と保存cropの81開始座標は順序まで一致した。保存中央層と公開中央CTの同じ320²は101,922/102,400値一致、最大1 DN、MAE .004668 DN。これは中央層の照合であり、法線や非中央層の生配列の同一性は未確認。公開時の実パッチ開始・余白の処理と実レンダーコードも確定していない。[R173幾何原票](../20261114-pherc0343-ct-readable01/preflight.md) · [R190入力契約](../20261114-hecate-known-text-control01/input-contract.json)

## 次の一回

同じ保存33層から `[8:24]` の16層だけを公式predictへ渡し、`reverse=True` の一回で23→8を評価する。R196の既存PNGを対照に用い、重み、ソース、XY、CPU fp32/batch1、64²/stride32、81パッチ、集約・表示を固定。Windows CPU1/commit4GiB、開始時空きRAM8GiB・途中4GiB、4500秒以内。最初の3枚を本番に含め、事前SHA・有限性・見積に違反したら次枚前に停止する。新規取得・依存・GPU・支出0。固定256²のMAE/相関と上明部・暗い分離を、R196・公開像・新出力で比べる。改善の程度からこの一層の寄与を評価する。歴史的実行条件や未知面での性能はこの比較の外。[次の研究票](../../../../research/198-hecate-crop-before-reverse-control.md)

一次取得はGitHubコネクタの固定コード・メタとHFの固定コミット・ルート木。取得量と通信工程の根拠は原票に記録した。保存配列の検算はWindows CPU1/commit4GiB、5.307秒。新CT・画像・重み・GPU・推論・支出0。[取得明細](acquisition.json) · [担当処理原票](input-check-process.json)
