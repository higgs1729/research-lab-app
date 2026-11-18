# PHerc0306B 公開予測の同面比較

公開済み上方群のうち一件を、原CTまたは独立面で紙層を確認する候補に残した。既知行の粗い縦画・交差・下側横画と右の輪の暗い内側をReader V3でも同位置に確認した。上方群では、TRACEで分かれた左の曲がりと下の小塊の間をReaderがつなぎ、暗い内側を囲む弧と下辺を描く。隣のまとまりにもおおまかな配置対応がある。接続の過剰補間や共通CT由来の応答はあり得る。確定新文字は0。 [研究票](../../../../research/225-pherc0306b-upper-public-map-context.md) · [担当所見](visual-review.json) · [主担当の別目視](lead-visual-review.json)

| 原寸表示 | TRACE | Reader V3 | CT |
|---|---|---|---|
| 既知の縦画と下側横画 | [補助](review/known_control/t01-trace-aux.png) | [raw](review/known_control/t01-reader-raw.png) · [補助](review/known_control/t01-reader-aux.png) | [t01](review/known_control/t01-ct.png) |
| 既知の輪と暗い内側 | [補助](review/known_control/t02-trace-aux.png) | [raw](review/known_control/t02-reader-raw.png) · [補助](review/known_control/t02-reader-aux.png) | [t02](review/known_control/t02-ct.png) |
| 上方の弧と隣接応答 | [raw](review/upper_test/t01-trace-raw.png) · [補助](review/upper_test/t01-trace-aux.png) | [raw](review/upper_test/t01-reader-raw.png) · [補助](review/upper_test/t01-reader-aux.png) | [t01](review/upper_test/t01-ct.png) |
| 上方の左側と共有部 | [補助](review/upper_test/t00-trace-aux.png) | [補助](review/upper_test/t00-reader-aux.png) | [t00](review/upper_test/t00-ct.png) |

原寸5タイルのraw x半開範囲は [2432,3584), [3456,4608), [4480,5632), [5504,6656), [6528,6848)。各帯は高さ1152、左から右に128画素重複。原native整数crop後に上下反転を一度だけ適用した。raw0..1と補助表示は高い応答ほど明るい。位置用の全景は1/4。CT値、CT>0、有限正XYZの4頂点支持、モデルの有限正値・有限ゼロ・NaNを区別した。上方群の追試用位置目安はraw半開XYXY `[3424,3424,4160,3824]`。これは目視で応答を囲うキャリア範囲。 [全表示とSHA](display-manifest.json) · [原票参照](input-references.json) · [主担当の画素照合](lead-panel-check.json)

取得は固定HFの3本文のみ。全SHAを照合し、画像生成は既存Windows資源制限ラッパーで実施した。新規取得171,424,048 B、原CTボクセル0 B、GPU・モデルforward・有料計算0。 [取得ログ](acquisition.json) · [計算ログ](render-process.json) · [資源記録](resources.json) · [成果物目録](manifest.json) · [lab登録候補](record.json)
