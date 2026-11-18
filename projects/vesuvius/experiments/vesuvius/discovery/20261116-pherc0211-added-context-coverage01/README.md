# R243 — 追加文脈の公開v9範囲確認

2026-11-16 JST resolved。正本は [研究票](../../../../research/243-pherc0211-added-context-public-coverage.md)。

旧小ROI98,304pxのcell支持はv9 global box外。追加196,608pxは29,984pxだけ除外、166,624pxは除外できない。旧ROIの結論を固定384×768全体へ拡張できない。

結果前固定840 anchor / 全22,434cellの一回の幾何Aを完了した。旧273点の評価bilinear残差142.536–455.939voxelに対し、追加567点は0.002660–241.966（中央値2.717360）。実点への残差上界と近似下界を保持した名目座標であり、厳密逆写像・同じ紙・既読範囲を与えない。4近傍の複数component120はtopology集計で、別紙の数ではない。

親の全行box確認、全840点のXYZ/距離/法線cos、均等12点の全cell距離/潜在集合の独立検算が一致した。CT深さ/8corner envelopeだけは親独立値検算未実施であり、中央面の確認済み結論と分ける。

Bの公開確率crop/画像比較は実施しない。公開v9は旧主候補の過去出力の代替にならず、下側の近接から同紙・新規性へ進めない。R242の形の候補を保持、新文字0、ink/同一細層/読字/新規性は未確定。旧R236 pairgate不合格は不変。次に必要なのは送信済みIssue #1で尋ねた原全親出力/既読範囲で、主担当が扱う。

根拠入口：

- [metadata-inspection.json](metadata-inspection.json)、`sources/`：既存ZIPからの一次原文。
- [geometry-box-check.json](geometry-box-check.json)、[geometry-row-boxes.json](geometry-row-boxes.json)、[lead-cell-box-check.json](lead-cell-box-check.json)：固定全域のcell支持。
- [nominal-mapping-plan.json](nominal-mapping-plan.json)、[lead-stage-a-clearance.json](lead-stage-a-clearance.json)：結果前固定計画とAだけの承認。Bは案のまま未実施。
- [stage-a-geometry-result.json](stage-a-geometry-result.json)、[stage-a-summary.json](stage-a-summary.json)、[lead-projection-check.json](lead-projection-check.json)：全結果・記述集計・独立検算。
- [closest-analytical-check.json](closest-analytical-check.json)：内部/辺/頂点/退化を含む解析既知6例。実geometryの退化三角0。
- [lead-mask-source-read.json](lead-mask-source-read.json)、[joint-decision.json](joint-decision.json)：提供maskと入力全0ゼロ化の区別、B見送りの理由。
- [record.json](record.json)、[manifest.json](manifest.json)：親の根拠登録用。担当は登録しない。

metadata64KiB制限停止とA承認guard停止は元脚本/失敗receiptを保持。A初回guard失敗時に投影はなく、訂正後の840点一回のみ。計算本体25.227秒、runner全体25.621秒/最大RSS118,009,856B、CPU1/commit4GiB。新規保存上限16MiB/空き2GiBを維持。CT本文読取・取得・prediction画素・新図・モデルforward・GPU・外部連絡・追加費用はすべて0。既存凍結研究は不変。
