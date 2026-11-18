Status: resolved
担当: 研究（R195担当、2026-11-14 JST）
Blocked by: 194

# 未精査の公開面から次に元CTで追試する一領域を選べるか（2026-11-14）

## 依頼

本人は未読文字の発見を主目標とし、少ない支出で研究を一件ずつ続ける方針。194でHecate既知対照一回のRunpod見積もりを用意し、主担当が承認枠US$0.50を質問したが現在未回答。有料計算は開始しない。無料で進められる別の候補選別を一件行う。本人の最新の希望は「進み具合はどう？ 成果があったら教えて」で、同じ待機状況の繰返しでなく意味のある候補/改善を報告する。

固定SharpMeow/first-letters-ink-atlas ac5ffd7098120368216948c4e06c494bf8e67178には、まだ本研究で原寸精査していない公開面がある。既存研究と公開来歴・CT/モデル画像の読める範囲を整理し、未精査から最大三面を比較して一面を選ぶ。選定した一面の公開原寸で、元CTを追加取得して追試するに値する字画や行の一領域を選べるかを判定する。見込みが薄ければ選ばない。陽性面が少ない理由を「インクがない」と決めない。単に明るい/モデル一致/ランキング上位で文字と扱わず、輪郭・線の並びとCTの割れ/縁/繊維・層構造との関係を確認する。明度の再正規化や閾値調整で候補を作らない。

既存入口: experiments/vesuvius/discovery/20261113-next-target01/ink-atlas-index.json と ink-atlas.md、研究164/186/188/192。既に閉じた領域はPHerc0800 R137–143、PHerc1218 R165–167、PHerc0846A R169–176、PHerc1545 R177–178、PHerc0813 pscamillo z12496_w020 R188、PHerc0846B 2768_2813_9748 R192。Hecate既知PHerc0343の試験は別途承認待ち。PHerc0343は既知対照、PHerc0306Bは既にFirst Letters受賞のため、未受賞巻での最初の発見候補と混同しない。同じ固定面・中心窓の再検査や既存三件の再包装は行わない。

まず保存済み資料を再利用。新規取得は候補比較の小さい一次メタ/資料と、選んだ一面の中央CT・中心窓の公開予測まで。複数モデルと両方向が配布されていれば、該当する中心窓の一組を揃える。既存の原寸タイル化の仕組みを利用し、画像元SHA/座標/固定表示範囲と、目視した場所を残す。全面画像が大きければタイルで覆い、取得・表示に上限があるなら実際に見た範囲を区別する。候補が見つからないからと、同じ実験で別面や追加深さへ広げない。

新規取得は本文合計64MiB、通信300秒まで。予測画像一枚の巨大ファイルなら取得前に選択を見直す。新CTボクセル・新重み・モデルforward・学習・GPU・クラウド資源作成・外部公開/送信は0。処理は既存tools/research/run_windows.py等でCPU1/commit4GiB。D:は読み取り限定、新規原票はC:。技術的な来歴の未確定点は明示し、元CTへの正確な3D写像が未検証ならそのまま記す。読めそうな公共画像を見つけただけで本人の新発見とはしない。

この研究票に結論と根拠を追記し、experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/へ一面の原寸証拠、取得原票、再現コード、入力と表示のhash/画素照合、次に進める場合だけ具体的ROIと停止条件、manifest/lab候補を残す。主担当が別目視・表示の独立検算を行い採否を決める。サブ委任なし。他研究・本人確認を並列起動しない。

モデルは今回あらためて gpt-6.1-sol / xhigh。既存陰性結果と未精査面の来歴を区別して候補を選ぶ判断には不確実性があり、その後の原寸画素確認は既存手順を再利用する。継続の担当設定をそのまま採用せず、この選定の内容に応じて選んだ。

## メモ

- 固定atlas indexと過去の原寸確認を照合。既知・受賞済み・既精査範囲を除き、公開面が一枚ずつで来歴条件が揃うPHerc0125、PHerc0191、PHerc0257の三面を固定メタで比較する。
- 原寸受信前にPHerc0125を選定。固定PNG15枚の取得、描画、担当目視、主担当の別目視と画素照合を完了。

## 結論

2026-11-14 JST。[一次・目視] 固定atlasのPHerc0125 `5409_5288_14587` を一面選び、中央CTと七モデルの中心窓両順を比較した。元CTで追試する字画・行のROIは選ばず、一面で閉じた。独立した輪郭や字間が続かず、確認した強い反応には孤立塊、割れ・繊維近傍、CT有効域の外周に沿う帯があった。判断範囲はこの面の中心窓。 [原寸図と所見](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/README.md) · [主担当の別目視](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/lead-checked.json)

## 根拠・詳細

- [一次・推論] 既精査と受賞済みを外し、同じ解像度・canvas・欠落chunk 0で比較できるPHerc0125、0191、0257の三面を固定メタで比較。atlas作者のcrossness sheet maskは86.3%、15.9%、16.3%。0125は紙面構造を比較できる範囲が広く、中心の七モデル両順が揃うため選んだ。公式First Letters規定のCT `20250821151825` と固定metaのZarr L0が対応する。 [選定原票](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/selection.json) · [現行公式規定](https://scrollprize.org/prizes#first-letters-prizes)
- [一次・実測] 全15枚の2184² PNGを固定木のLFS SHAと照合した。原寸64図の288パネルで85,857,408値が元画像に一致し、主担当の独立照合も同じ結果。担当目視は全体図と原寸28図、主担当はCT・Hecate逆の原図、全体図と原寸6図。描画bboxの4,272,489画素中、8値は0。主担当は初回検査で非ゼロ数と描画画素数を同一視した仮定を修正し、再照合した。 [画素索引](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/review01/pixels.json) · [主担当の独立照合](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/lead-checked.json)
- [一次・範囲] 9.6 µm canvas、scale .975、65層、方向名はatlas層順。七モデルの当該巻の訓練曝露は公開面metaでunknown。XYZ未取得のため厳密な2D→元CT写像は未検証。 [固定面メタ](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/candidates/PHerc0125-meta.json)

## 取得の経路

候補メタと選定面のPNGだけを受信。計20,962,896 B、通信34.878秒。既存Windows入口とR192の同座標パネル方式を借り、描画・照合4.731秒、CPU1、commit上限4 GiB。新CTボクセル、重み、推論、GPU、クラウド、有料計算、外部送信0。 [取得原票](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/image-acquisition.json) · [manifest](../experiments/vesuvius/discovery/20261114-unreviewed-atlas-face01/manifest.json)
