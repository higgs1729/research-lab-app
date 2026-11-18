# R241 旧Studio全親確率の公開所在

2026-11-16 JST。公式記事が案内する公開Drive、著者GitHub、リンク先の公開モデルを調べ、PHerc0211 v6の旧Studio全親確率原本はこの範囲で特定できなかった。形状と推論条件は公開v6 ZIPの親記録で確認できる。原本の形式・格納サイズ・確率SHA-256の対象は未判定。旧確率を取得できていないため、R239固定候補の旧反応、既読文字との対応、新規性は未確認のまま。新文字0。

## 成果と検証

- 公開Driveの9フォルダ計66件を確認。配布確率の2 TIFFはv6-line2と別手動版v9。匿名GETしたv6-line2 ZIPは、R234保存原本と同じ4,953,331 B・同一SHA-256。公開ZIP内の親記録は旧Studio epoch 9、親shape `[4600,6060]`、GH200 hybrid FP8/BF16、6,663 tilesを記録する。旧checkpointのSHA-256は、公開epoch 9モデルのLFS OIDと完全一致。公開本文の所在は得られなかった。
- R239の固定候補 parent XYWH `[4416,2048,384,256]` は親の半開範囲 `[2048:2304,4416:4800]`。公開line2の親範囲 `[2980:3580]` との重複は0行。旧Studio、公開soft-lossのGH200/BF16、R239 soft-loss/FP32ではモデルまたは数値条件が異なる。
- 著者GitHubの切断されていない3 tree、公開2 releases、公開issuesを確認した。crop1711比較JPEGと関連スクリプトは10月23日のDinoVol Original/Rev1系列。検索範囲、各応答、根拠ファイルは [証拠索引](source-index.md) に保存。
- 主担当がZIP全39項目の名前・サイズ・圧縮サイズ、旧2 JSONの記録一致、公開Drive全9フォルダと2 TIFF、HFの旧重みSHA、GitHub 3 treeと2 releases・3 assets、issues 0件、候補とline2の重複0を独立照合した。報告の初稿でZIPを38項目と数え違えたため、主担当の初回検算は件数assertで停止した。元一覧は全39項目を収録しており、直接照合後に報告の件数を訂正した。最終照合は [lead-source-check.json](lead-source-check.json) を参照。初回・再検算双方の実行記録と最終検算コードのSHA-256をmanifestに収録した。

再開条件は、旧全親mapを示す正規公開先または出力先を明示する原資料が見つかること。比較する場合は元の版・幾何・SHA-256の対象を確定し、同じ固定候補座標を使う。

## 保存資料

[研究票](../../../../research/241-pherc0211-historical-parent-probability.md)、[証拠索引](source-index.md)、[照合結果](source-evidence.json)、[主担当検算](lead-source-check.json)、[証拠と参照SHA](manifest.json)、[登録用記録](record.json)。

確率本文・新CT・GPU処理・モデル推論・支出は0。ZIPの再取得複製を含む一時保存は6 MiB未満。計算はCPU 1、hard process commit 4 GiB。公開・外部連絡・応募は0。
