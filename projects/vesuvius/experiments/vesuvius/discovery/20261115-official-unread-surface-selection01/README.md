# PHerc0800の公式展開済み二窓を次の探索に選ぶ

[推論] 公式再構成 `20250521135224` の展開済み面4（20251028222030）下方と面5（20251028225813）上方を一回のHecate比較に使う。旧研究138–143の末尾146・中央512²を対象から外した。今回採用した二窓では公開中央層に横に続く繊維帯があり、旧面の範囲との幾何関係も確認できる。両窓の原寸予測を組にして、一面の同じ小窓で設定を変える工程を増やさず新しい位置を観察する。 [固定計画](next-plan.json) · [原寸の面4](middle-preview/mesh4.png) · [原寸の面5](middle-preview/mesh5.png)

## 選定の根拠

| 候補 | 前の観測と今回得られるもの |
|---|---|
| **PHerc0800 二窓** | [一次] 公式は8.64µmの展開済み6面。先行43対象の研究は当該6面を含み、4 checkpoint・両順で検査したが、数値ゲートで全件が止まり目視対象0。後日の監査でも完全なゲートは既知対照を保持できなかった。gmDeviは別のflat 9µmで0800/1447公式面群に散漫な反応や一部の面飛びを報告し、0800別fitの帯内にも先行予測がある。今回の二窓について、対応する同一公式面のHecate原寸予測を確認できず、閉じた512²の外から具体的に観察できる。 [旧43対象の原報告 §8.4/§10](../20261113-next-target01/25_scouting_eligible_volumes.md) · [別作者の報告](../20261114-unread-multiwinding-lane01/originals/gmdevi-report.md) · [旧R013の独立検証](../../../../research/143-r013-depth-sensitivity-verification.md) |
| PHerc1203 `20250820131727` | [一次] 公式目録の展開済み面0。先行者のraw GrowPatch 22面は互いに重なると報告され、今の試験へ公式XYと同じ展開済み入力を渡せる根拠が不足する。別の2.403µmの再構成も公開されている。 [公式目録](https://scrollprize.org/data_browser/PHerc1203) · [原報告 §2](../20261113-next-target01/25_scouting_eligible_volumes.md) |
| PHerc0211 `20250821151803` | [一次] 公式目録の展開済み面0。公開著者はすでにz10000–11000の56巻きを展開し、巻きの向きと層順の両方を確認した。最大反応を散漫な塊と判断し、字画を報告していない。同公開帯の別探索を優先する独立の位置根拠が乏しい。 [公式目録](https://scrollprize.org/data_browser/PHerc0211) · [作者の保存原文](../20261113-next-target01/community-0211.md) |

pscamilloの340面にはHecate9.6両順の著者報告があり、0800の95面もその系統に含まれる。主実験で使うのは別の公式mesh IDと表面Zarr。既存340面との物理的重なりは未照合。現行First Letters対象に0800の同再構成があり、公式Winnersには同巻のFirst Letters受賞記載を確認できなかった。0343と0306BはFirst Letters受賞済み。非公開の判読、訓練の全巻・全座標、公開歴の網羅は未確定。CTと公式meshはCC BY-NC 4.0。 [340面の固定原報告](https://github.com/rodriguescarson/eligible-scroll-atlas/blob/0c0566ccd07652ef4bc9fa1926491983d520942f/README.md) · [R212の原文照合](../20261114-unread-multiwinding-lane01/lead-prior-coverage-review.json) · [公式条件](https://scrollprize.org/prizes#first-letters-prizes) · [受賞一覧](https://scrollprize.org/winners) · [公式目録とライセンス](https://scrollprize.org/data_browser/PHerc0800)

## 固定範囲と支持

| 面 | 9.6µmのcrop、主域（絶対XYWH） | 中央層原寸 | 取得キー・片順上限 |
|---|---|---|---|
| 4 `20251028222030-auto_grown_20251028222030940` | `[704,1568,1024,640]`、`[736,1600,960,576]`。主幾何支持412,428/552,960、支持の名目0.3801cm²。 | 交差する繊維帯、下方に裂け目・空隙と斑状暗部。 [8.64µm原寸](middle-preview/mesh4.png) | 50キー25,395,200 B、589 patch |
| 5 `20251028225813-auto_grown_20251028225813045` | `[480,64,960,576]`、`[512,96,896,512]`。主幾何支持326,968/458,752、支持の名目0.3013cm²。 | 比較的連続した横帯と縦繊維、所々に皺と暗部。 [8.64µm原寸](middle-preview/mesh5.png) | 40キー20,316,160 B、493 patch |

この二窓は全有効セルの四隅包絡が、旧146全面のXYZ bboxを32元CT voxel膨張した箱を避ける。セルごとに異なる軸で分離し得る。計画内で相互のZ包絡も約939.48 voxel離れる。これは公開面とTIFXYZの中心・格子対応を仮定した幾何上の根拠。実際の公式生成座標や物理ラミナは未検証。両窓の合計0.9324cm²は名目主画素面積、0.6814cm²は幾何支持画素換算。独立した可読紙面積には用いない。原寸中心層は全90 Range 206、同一オブジェクトETagに照合。担当と親が別目視し、親が両PNG全1,494,203値を別に組み立てた。 [XYZとキー一覧](preview-inputs.json) · [親の幾何確認](lead-geometry-check.json) · [親の画像確認](lead-preview-check.json)

## 次の一回

公開Zarr L0はZYX、非圧縮uint8、31層・各軸8.64µm。全深さchunkは `[31,128,128]`。必要な90オブジェクト45,711,360 BをETagに照合して読む。元3D CTの取得や描画は不要。各XY軸で新全長を `round(0.9*旧全長)` とし、中心登録 `旧座標=(新index−新中心)×10/9+旧中心`。深さは公開中央15を新index 8に固定し、`旧Z=15+(k−8)×10/9` の16枚をlinearで作る。float64をX、Y、Zの順に補間し、最後に最近接偶数でuint8へ丸める。逆順はその同じ16枚を逆転する。XY・深さとも9.6µmにする契約はHecate固定cardと一致する。公開の法線符号はこの二窓で独立検証していないため、forward/reverseは公開配列順の名称。 [固定式と全キー](next-plan.json) · [Hecateの一次カード](../20261114-alternative-ink-model-selection01/originals/hecate-card.md)

補間支持は対象格子と元の4標本の幾何有効域、および4標本の完全オブジェクト存在の交差。面4の外周で144画素減り、両主域は同値。実値の0はマスク内で保持する。中心層は別の原寸対照。既存217/208の入口を借り、サイズの違う二窓・各順逆を合計最大2,164パッチ、CPU参照各3件、GPUの重みロード一回で測る。全パッチ契約と代表確率を保存し、4原図を固定階調の原寸で別目視。続く字画・行を指定できた場合だけ別確認へ進める。候補がなければ今回の窓・深さで終了する。 [実行・停止条件](next-plan.json)

ローカル取得43.594 MiB、上限48 MiB/300秒、CPU1・commit 4 GiB・作業1 GiB、C空き10 GiB以上。クラウドへは真に使う16層のみで、生19,333,120 B、入出力各24 MiB上限。217/208から推論約116–120秒、台8–12分と見込み税別US$0.119–0.179。25分なら現単価と20GB一時diskで約US$0.372、単価上限US$0.90/時で約US$0.376。US$0.45は運用枠。親の直近読取はSecure4090 US$0.89/時・残高US$17.21338・自動入金false・全Pod0。実起動時に再取得し、一台一回、削除と同ID/名前の残存確認まで行う。 [料金読取](lead-rate-snapshot.json) · [Runpod公式料金](https://docs.runpod.io/pods/pricing) · [R217の実測](../20261115-pherc0191-fixed-pair-ink01/resources.json)

R218の保存した新規本文はXYZ/メタ/一覧770,358 Bと公開中央層1,474,560 Bで合計2,244,918 B、計測通信71.05秒。公式ページの直接取得3件は403で本文を読まず、現行webと既存の公式原文を参照。初回の公開中央層入口はZ軸だけで旧bbox+32外を求める誤ったassertで通信前に止まった。候補は変えず、セルごとの三軸包絡判定と実Z範囲を別に記録して続行。元3D CT、新重み、forward、ビルド、Pod、公開は0。 [資料取得](acquisition.json) · [中央層取得](preview-acquisition.json) · [初回停止原票](preview-process.json) · [公式現況確認](lead-current-official-check.json) · [既取得公式規定](../20261113-next-target01/prizes.html) · [既取得公式受賞一覧](../20261113-next-target01/winners.html)

親が計画の両支持マスク全1,208,320値、固定位置・16層・パッチ数と取得容量を別計算し採用した。R217の専用Pod明細は16:19 UTCの追補照会でも0行で、R217の実費は未確定のまま。 [親の計画照合](lead-plan-check.json) · [R217明細の追補](lead-prior-run-billing.json)
