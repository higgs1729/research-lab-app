Status: resolved
担当: 研究（R198、2026-11-14）
Blocked by: 197

# 公開runnerの深さ窓へ一変更するとHecate既知対照の画像差を説明できるか（2026-11-14）

## 依頼

研究197で公開同日付のInk Lens二版に、中央16枚を先に切り出してから反転する経路が見つかった。65層では39→24、保存33層へ対応させると23→8。研究196の公式CLIへ33層を渡した24→9とは全パッチで一層ずれる。両経路のvendorコードSHAと重みpinは一致し、主担当も原文・AST抽出・保存1,638,400値を別確認した。ただし公開PNGの生成receiptはなく、公開時の厳密な実行条件や差の因果は未確定。

この一件では、**保存33層から8:24の16層を選んで公式Hecateへ渡し、reverse=Trueで23→8を使う**一変更だけで、196と同じ既知ROIの公開画像への対応と字画部分の形状がどう変わるか検証する。モデル/重み/XY入力/パッチ位置/正規化/集約/表示は196と同一。既存196出力を対照とし、対照を再forwardしない。新しい深さ・位相・向き・モデルの走査はしない。改善なしも確定結果として閉じる。

入力は190/input.npy（SHA5f1caf23443ed3f4933803ab668e566de9c0deb06ab4878977a00b0ae9e49566）のuint8[8:24]だけ。出力320²、global XYWH[1376,1056,320,320]、主比較[1408,1088,256,256]。197親の変更後rawSHA589f7ba0dd646f2f3b37d41ff6708236a07787344282615420c4891783c4b5afと照合。重み809f4f10…、公式source c232c18a…、CPU fp32/batch1/64²/stride32の81パッチ。実際の正規化入力と支持を事前計算した値へ照合し、生の確率を保存する。

196の正常完走したWindows経路・supervisor・比較処理を再利用する。CPU1、プロセスcommit4GiB、初期空きRAM8GiB以上/実行中4GiB以上、絶対wall4500秒以内。最初の3枚で残り78枚が時間内に終わる見積か判定し、超過予測/非有限/入力不一致なら次枚前に停止する。196の3枚とのbit一致は**今回期待しない**（入力を変えているため）。無意味な追加warmup/再現forwardはしない。196は約418秒だったが混雑状態で変わる。外部取得・依存追加・GPU・クラウド費・公開・応募・連絡は0。194の旧有料案は使わない。

主評価は同じ公開ROIとのMAE/相関と、同じ0–255原寸で明部の分離・輪郭・暗部を196/公開/今回で見ること。画素相関は認識率にしない。画像の改善は新しい文字の発見や未知面への一般化と区別する。親が入力・別集約・原寸図を独立確認する。報告には一層変更で説明できた範囲と残った差を明記する。

出力は experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/ 。研究票に結論を追記し、原票/コード/manifest/record候補を残す。登録済み196以前の資料は変更しない。研究197が完了し主担当が開始を伝えるまで実行しない。今回担当選択は gpt-6.1-sol / high（正常完走した既存手順を、確定した一入力変更に適用する仕事）。別研究・サブ委任なし。

## 結論

2026-11-14 JST。[一次] 保存33層の `[8:24]` を先に切り出し、公式Hecateのreverseで23→8を使った。深さ窓一層の変更で、同じ公開256²とのMAEは36.239→11.307 DN（68.8%減）、Pearsonは0.688256→0.949139になった。上中央と右下の明部の間の暗い分離が公開像に近づいた。左縁の明部の位置と右上の淡い信号には差が残った。公開PNGの歴史的な生成条件や新たな判読は確定していない。 [実験報告](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/README.md) [原寸比較](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/comparison-256.png)

## 根拠・詳細

[一次] 全81の実入力をR197の座標、raw/正規化SHA、supportと照合した。最初3枚の実測では残78枚の見通し469.812秒で継続し、単回765.861秒で完走。CPU時間436.500秒、peak RSS 1,283,772,416 B、commit上限4 GiB、最低空きRAM9,412,988,928 B。 [最初3枚の原票](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/first-three.json) [資源実測](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/resources.json)

[一次] 主担当は81入力・331,776確率値を検査し、独立Hann再集約の全102,400画素が公式PNGとビット一致することを確認した。公開像との完全一致画素は4,573→12,784/65,536。目視では箱9側の上明部の縦伸長と右下への連結が弱まり、箱10側の左縁明部の残差が見える。この固定既知面の画像再現性の結果で、文字認識率や未知面は未検証。 [独立検算](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/lead-verified.json) [主担当目視](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/lead-visual.json)

## 取得の経路

[一次] R196のWindows supervisorを同一バイトで借用し、モデル・重み・XY・正規化・Hann集約を固定した。R196の対照は登録済みPNGを使用。新規ネットワーク・CT・依存・GPU・クラウド支出は0。 [固定資産SHA](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/preflight.json) [監視原票](../experiments/vesuvius/discovery/20261114-hecate-depth-window-control01/supervisor-result.json)

## メモ

2026-11-14 JST。[一次] R197の独立深さ照合と81パッチの事前SHAを確認。R196からWindows実行・メモリ制限・期限監視を借用し、入力16層と照合元を切り替える。

親の事前確認後に一回だけ実行し、独立検算と目視の完了後に確定した。
