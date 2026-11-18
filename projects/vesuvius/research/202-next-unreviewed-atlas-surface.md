Status: resolved
担当: 研究（R202担当、2026-11-14 JST）
Blocked by: 201

# 未精査の別巻の公開面から、元CTで追試する字画候補を選べるか（2026-11-14）

## 依頼

研究201のPHerc0846A有料GPU一回案は具体化と親検算・lab登録まで完了した。本人へ約US$0.30/承認枠US$0.50税別を質問中で未回答、支出0。Runpod本人確認は条件付き手作業TASK-61。主担当は承認待ちを無料研究全体の停止理由にせず、別の公開面の候補選別を一件ずつ進める。有料実行の開始はこの票の範囲外。

既存の研究195ではPHerc0125一面を七モデル・両順で精査して追試候補を選べなかった。今回、まだ原寸で調べていない別巻の面を、同じ手順で一面選び、独立した字画や行を元CTで追試する根拠があるかを判断する。保存SharpMeow/first-letters-ink-atlasの固定revision ac5ffd7098120368216948c4e06c494bf8e67178には、PHerc0175B（4公開面）、PHerc0268（3）、PHerc0483A（4）がある。これらの小メタ・先行記述から最大三候補（一巻一候補）を比較して一面へ絞る。全面予測の受信前に選定理由を保存し、結果に応じて別面へ広げない。現在の公式対象・既読発表を一次で確認し、対象外や既受賞なら未受賞巻のFirst Letters候補と混同しない。

候補の選択では元CTへの来歴、紙面の有効範囲、中央CTと複数モデルの両順が揃うか、既存研究や先行判読との重複を比較する。crossnessや非ゼロ面積は文字の指標ではない。メタの紙面品質を実画像の輪郭・裂け/繊維との関係で確認する。強い反応、モデル間一致、表裏差だけで文字と扱わない。新文字があり得る画像はローカルに保持する。

資料の入口は experiments/vesuvius/discovery/20261113-next-target01/ink-atlas-index.json、研究186/188/192/195。既に閉じた面・中心窓は理由なく再開しない。研究199/200のPHerc0846Aは計算時間による未判定で、陰性例には数えない。研究198の既知対照再現性の改善も、未知面での識別性能とは区別する。

一面を選んだら、その中央CTと中心窓c+0_s1に配布済みの複数モデル・両順を原寸で確認する。195の画像取得/原寸表示/画素照合のコードを再利用し、元ファイルの固定SHA、同座標、0–255固定階調を保つ。見た範囲と自動画素検算だけの範囲を区別する。具体的な字画/行候補がある場合は位置を記し、その一点の追加CT計画を提案する。候補なしならこの一面で閉じ、インク不在や巻物全体の文字無しとはしない。

新規は小メタ/公式原文と選んだ一面の既存公開PNGのみ、受信合計64MiB、通信300秒以内。新CTボクセル、重み、モデルforward、学習、ビルド、GPU、有料資源、公開・応募・メッセージ送信は0。CPU処理は既存tools/research/run_windows.pyでCPU1/commit4GiB。保存C、D読取のみ。母面/訓練露出/2D→元CT写像の未確認点は隠さない。

保存先 experiments/vesuvius/discovery/20261114-next-atlas-surface01/。研究票に結論・一次根拠・実資源を追記、原画/目視記録・原寸パネル・次の判断・manifest/record候補を残す。主担当は重要な原図と候補を別目視し、表示画素も独立に検算する。主担当が登録後に次へ進む。再委任/別研究の並列実行なし。

担当は今回あらためて **gpt-6.1-sol / high** を選択。195と192で確立した公開面の比較・原寸確認手順を別の未精査群に適用し、画像の解釈と候補判断を伴うため。
## メモ

- 保存atlas indexの掲載順で各巻先頭の一面を代表にし、固定tree/metaと公式規定・Winners・Data Browserを取得。三代表の指定volume、七モデル中心両順、描画寸法と欠損chunk数を照合。原寸PNG取得前にPHerc0175B 3024_3577_11121を選定し、選定理由を保存した。
- 固定15PNGを取得し、担当が全体図と原寸25図を目視。候補未選定。重要位置と原寸索引を主担当へ共有した。

## 結論

2026-11-14 JST。[一次・目視] PHerc0175B `3024_3577_11121` の中央CTと七モデル中心窓両順から、元CTに戻す字画・行のROIを選べず一面で終了。Hecateの右上の塊は不規則で、中央右の短い反応はCTの層や空隙に隣接し、seed42・43の一部は画像内の描画境界に沿う。担当は原寸25図、主担当は原寸6図と全体図を別目視し、原寸全73,156,608値の独立照合も通過した。選定時の `sheet_fraction` は異なるマスクの値を比較したため、三面の紙面品質に関する順位は撤回した。 [原寸図と目視位置](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/README.md) [主担当の別目視・検算](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/lead-checked.json)

## 根拠・詳細

- [一次・推論] 各巻のatlas index掲載先頭から0175B `3024_3577_11121`、0268 `2704_5907_7421`、0483A `3155_3610_11128` の三面を代表とした。公式First Letters指定volumeはそれぞれatlas metaのL0参照と一致。公式Winnersページに該当三巻の記載は確認できなかった。三代表は同寸、欠損CT chunk 0、七モデル両順あり。選定時は `sheet_fraction` を同じマスクの割合と誤読し、1.0の0175Bを選んだ。主担当の照合で0175Bは `ct > 0 (sheet mask under 5 %)`、他二面は `sheet (crossness >= 0.31)` と分かった。三面の紙面品質はこの値では比較できず、1.0の正確な計算はコード未確認。原寸CT中央層には折れた層や空隙が見える。 [画像取得前の選定](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/selection.json) [マスク記載](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/README.md) [公式規定原文](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/candidates/official-prizes.html) [公式Winners原文](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/candidates/official-winners.html)
- [一次・実測] 固定atlas `ac5ffd7098120368216948c4e06c494bf8e67178` の中央CT＋中心窓 `c+0_s1` 七モデル両順15PNG。2016×2016のuint8で、固定木の長さとSHAに一致した。0–255を保持した原寸64図288パネル73,156,608値を元PNGと比較した。担当は全体図、Hecate/Reader V3/CTの原寸全16図、他モデル原寸9図を目視した。 [長さ・SHA](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/acquisition-plan.json) [原寸画素索引](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/review01/pixels.json) [目視原票](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/visual-review.json)
- [一次] 固定survey `1f12c1ce` のmeshと、公式scan `20250510115222` のvolume `20250521125822` L0をatlas metaで照合した。元CTは8.64 µm、atlasは9.6 µm/px、scale 0.9、65層。元meshのXYZは未取得で、2D→元CT写像、当該巻のモデル訓練曝露、完全な先行判読との重複は未確認。 [面meta](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/candidates/PHerc0175B-meta.json) [公式Data Browser原文](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/candidates/PHerc0175B-official.html)

## 取得の経路

R195の取得・原寸表示・画素照合を再利用。候補メタと公式原文424,677 B、選んだ一面の15PNG 16,558,105 B、通信計30.348秒。図生成と照合15.675秒、CPU1、commit上限4 GiB、数値スレッド1。新CTボクセル・XYZ・重み・モデル/GPU・ビルド・課金・外部公開0。 [取得原票](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/image-acquisition.json) [再実行](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/README.md) [manifest](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/manifest.json) [lab登録候補](../experiments/vesuvius/discovery/20261114-next-atlas-surface01/record.json)
