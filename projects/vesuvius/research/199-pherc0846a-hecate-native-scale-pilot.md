Status: resolved
担当: 研究（R199担当、2026-11-14 JST）
Blocked by: 198

# PHerc0846Aの既存CTで、異なる構造のHecateに字画候補が現れるか（2026-11-14）

## 依頼

研究198ではHecate 9.6の中央16枚先切出し・反転という公開runnerの条件を合わせ、既知PHerc0343の公開部分像とのMAEを68.8%下げた。完全な歴史的再現や未知性能の証明ではないが、別構造のモデルを既知対照から未読面の小試験へ移すための入力条件が分かった。研究171/172/176のPHerc0846Aでは同じUNet系統の二つの重みで字画候補がなく、同じモデルの位相・深さ・閾値探索は終了している。本件はその設定走査を再開せず、3D ResNet＋depth attentionの別モデルを一度比較する。公開atlasには0846Aの個別生Hecate像がなく（heldを陰性根拠にはしない）、既存元CTを再利用して調べる意味がある。

対象は固定survey面PHerc0846Aのseed(2601,2784,3851)、171/176と同じ近傍一箇所。既存33層入力の実間隔は9.362µmで、Hecate9.6の公式±2%を外れるため、9.6と表示してそのまま渡さない。既存のネイティブrenderer/observerで、同じmesh・元CTからXY/Zとも名目9.6µmへ一度だけ描画する。画像を補間拡大したものを元CT描画と扱わない。scale=9.362/9.6、slice-step=9.6/9.362を出発点に、既存rendererの定義と実際のmetadataで確かめる。新規実装/ビルドは不要。

新9.6キャンバスの固定XYWHは **[896,896,384,384]**。旧native面でおよそ[918.8,918.8]〜[1312.5,1312.5]に対応し、176の448²範囲内に収まる近傍。Hecateの64²/stride32格子へ揃い、内部比較は新XYWH **[928,928,320,320]**。旧予測と同一ピクセル・同一面積と主張しない。中心や範囲を結果に合わせて移動しない。33層d=-16..16を非反転法線で描画し、中央16層[8:24]を先に選ぶ。Hecateへforward8→23とreverse23→8を各一回、同じ16枚で表裏を比較する。

まず171/176/173の固定mesh・CT cache・renderer/observer・入力契約を読み、保存先/実行環境を確認する。幾何と全描画支持を新しい計算に合わせて確定し、必要CTキーを既存44キーと照合する。物理紙面の正しさは数値同値から主張しない。全キーがcacheにあれば取得0。不足があっても新規元CTは最大8キー16MiB・通信180秒以内に限定、固定公式URL/L0/ETag/本文SHAを残す。上限超過ならROI変更や欠損のゼロ埋めで続行せず、その不足を結果として主担当へ返す。新しいmesh/重み/依存の取得・他領域・学習・GPU・有料計算・公開/応募/連絡は0。

描画準備はCPU1/AS4GiB/geometry600秒、製品描画一回120秒、C空き10GiB以上、作業512MiB以内。Windowsで公式Hecateを一度loadし、fp32/batch1/64²/stride32、二方向を逐次。最大121パッチ×2=242。計算の予測は直前198の765.9秒/81枚から約38分、混雑前196から約21分であり、保証値ではない。推論工程の絶対wall4500秒（両方向合計）、CPU1/commit4GiB、開始時空きRAM8GiB/途中4GiBを維持する。最初3枚は本番に含め、残り全方向の実測予測が期限に収まらなければ4枚目前に停止。範囲外の追加forwardやwarmupはしない。全実入力のraw/正規化SHA・支持を事前保存し、生確率とHann集約を親が照合できる形で保存する。196/198の正常完走した経路を借りる。

新しい幾何・描画と入力契約が確定した時点で主担当へ渡し、親が対応と資源を別確認してからモデルを実行する。これは技術検証で本人への新たな承認依頼は不要。担当/親とも原寸CT・両方向を見て、追試する字画/行の位置を具体的に指せるか判断する。スコアの高さ・表裏差だけでインク/文字/当選を主張しない。候補なしならこの一モデル・一窓・一領域を閉じる。既存モデル二つの負例との関係と、訓練露出不明の限界を残す。

出力は experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/。登録済み原票は読取。研究票へ結論・資源・原票を追記、manifest/record候補まで。主担当登録後に次へ進む。同時の別研究・サブ委任なし。今回の担当選択は **gpt-6.1-sol / xhigh**。既知Hecate手順は再利用できる一方、実物のサンプル間隔・mesh座標・CT再利用支持を整合させる不確実性があり、その判断を含むため。

## 実行記録

既存meshを使い、R171の44キーから描画に必要な32キーを既存cacheのみで確保した。固定領域を一度描画し、Z/Y/X 9.600000549/9.599999914/9.599999914 µmの33×384×384を保存。新規取得0。親が新canvas2184²、9点のmesh位置と45点のCT補間を独立確認し、両順の全242パッチ入力と実行コードを照合した。10:20:14.700 UTCに空きRAM 11,276,640,256 Bで単回推論を開始した。子PID 29876、両方向の上限4500秒。[幾何](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/roi.json) · [入力契約](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/input-contract.json) · [独立入力照合](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/lead-input-check.json) · [開始原票](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/supervisor-start.json)

## 結論

PHerc0846A固定近傍の9.6 µm描画とHecateの3パッチまでが成立した。残り239パッチの予測4,627.642秒が残り4,398.305秒を超えたため、第4パッチ前に計画どおり停止した。順方向3/121、逆方向0/121。両PNGは未生成で、字画・行の有無とR176の二モデルとの差は未判定。主担当が3入力の座標・SHA・支持、12,288確率値、停止判定、PNG未生成を独立確認した。 [所要判定](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/first-three.json) · [独立結果照合](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/lead-verified.json)

幾何36タイル288.275秒、製品描画一回9.419秒。Windows推論の壁時計102.500秒、strict load12.081秒、peak RSS 1,284,853,760 B。新CT・重み・依存取得、GPU、再実行、追加課金は0。中央CT原寸には繊維状の細線や暗い溝状部分が見える。数値照合とCT像から物理的な紙面やインクを同定していない。 [資源](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/resources.json) · [中央CT原寸](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/ct-centre.png) · [原票案内](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-hecate-pilot01/record.json)
