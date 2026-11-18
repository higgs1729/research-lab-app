# R233 — PHerc0800の同じ固定窓をStudio softlossで比較

Studio softlossを、R220 Hecate・R223 Reader V3で追試ROIを選べなかった公式面4の同じ約9.2mm角へ適用した。既知0343のGPU参照3件と未知窓の順逆各324パッチを、モデル読込一回・計651 forwardで152.481秒で完走。担当の原寸目視では追試ROI0。明るい孤立塊、拡散した角状/鉤状の応答はあるが、連続した字画や文字行を選べなかった。主担当の独立検算・別目視も通過し、この窓のモデル比較を終了した。新文字0、追加応募項目0。

## 入力と推論

[計画](plan.json)は、保存R223 `native31.npy`（31×1536×1536、uint8、SHA bd6e0d94…）の一部を補間せず切り出す。native主域 `[142,640,1067,1067]`、支持bbox `[48,560,1216,1216]`、入力16×1216×1216＝23,658,496値。公式面は `20251028222030-auto_grown_20251028222030940`、8.64µm/20250521135224。新しいCT取得は0。

作者 `prepare_reader.py` は公開native Zarrのlabel_z−8〜label_z+7を保存順で使う。0800の中央index15に対して7〜22を選び、同じ16枚を逆順22〜7でも一回だけ処理した。公式metadataのZYX/31層/step1は確認したが、0800の法線と学習時方向の対応は未確定。0343原CTの符号から対応を推測していない。入力の同一性と原始深さindexを[入力契約](input-contract.json)・[パッチ契約](patch-contract.json)へ保存。

R232のモデル重みSHA96b32628…、223,355,921params、作者crop/central96/stride64、CUDA FP32 clip200/div255、sigmoid・pixel-centred Hann、batch1、TF32off/no TTA/no compileを維持。面全体の格子から寄与する全324パッチ/順を実行し、最後に16層all-zero画素を0にする。入力全256値と651パッチの実CUDA正規化SHAを事前の逆数乗算予測へ照合し、各forward直前にも照合した。[実GPU正規化](cloud-run/extracted/normalization-probe.jsonl) · [forward前原票](cloud-run/extracted/gpu/pre-forward.jsonl)

既知CPU0/47/95との出力最大差は順に1.93715e-7、9.23872e-7、6.25849e-7（許容1e-4）。未知入力のCPU forwardは追加していない。この3件は同じ実行経路の既知対照で、未知出力全体のCPU別計算ではない。[GPU実行原票](cloud-run/extracted/gpu/result.json) · [正規化集計](normalization-summary.json)

## 原寸比較

固定主域の生確率0〜1表示と、同じ主域の非ゼロCT画素で固定したmedian〜p99.5表示を保存。前モデルReaderのnative像、Hecate像を既知座標式でnativeへbilinear標本化した像と同位置に並べた。画像の範囲・層数・前処理・モデルは異なり、精度の順位にはしない。[表示契約と原寸ファイル](comparison.json)

担当は両順の原寸生画像と全4象限の比較図を確認した。順方向は中央下方と下辺近くの大きな丸い塊、上部の短い角/鉤状応答が中心。逆順は左中央や下方へ応答が変わり、表示を伸ばしても隣接する文字や一行の連続構造を選べなかった。CTには交差する繊維・縞と点状の濃淡があり、モデルの明るさだけからインクへ帰属できない。[担当所見](visual-review.json) · [左上](review/native-quadrant-00.png) · [右上](review/native-quadrant-01.png) · [左下](review/native-quadrant-10.png) · [右下](review/native-quadrant-11.png)

候補0は、この窓・二順・固定条件での追試選定結果だけを意味する。巻物全体やこの窓のインク不在、正しい紙層・表裏、未知性能は未判定。同じ窓を追加のモデル/閾値/深さで反復せず、第四応募項目や新規観測面積に加算しない。

## 主担当の独立検証

[出力検算](lead-output-check.json)はworkerをimportせず、スカラーFP32 lookupで全256種類のGPUビットと651入力SHA、既知CPU3件を別照合した。独立した格子列挙とfloat64のsin² Hannで両順各1,138,489画素を再構成し、保存確率との差は順方向最大1.57836728e-7、逆方向1.02513284e-7。両順とも非ゼロCT支持961,223画素を照合した。

[表示検算](lead-display-check.json)は9原寸画像10,246,401画素と36比較パネルの全表示値を照合し差0。Hecateの座標変換は別の軸別np.interpで再計算した。主担当もwhole raw2枚と全4象限を実際に確認し、[別目視](lead-visual-review.json)で追試ROI0を支持した。文字の存在・不在、紙層帰属、汎化精度の検証ではない。

## 回収と台の管理

[凍結クラウド計画](cloud-plan.json)、[R232差分](r232-diff.patch)、[オフライン確認](offline-check.json)、[主担当clearance](lead-cloud-clearance.json)を保存。CA-MTL-1 Secure A40一台、USD0.59/h、再作成0。入力archive21,762,239Bを141.439秒で転送し、Pod内で既存checkpoint893,443,724Bを一回だけ取得。結果archive34,856,330Bを64MiBの物理予約へ同fileIDで保存、SHA一致後670ファイル/55,156,084Bを展開した。[回収](cloud-run/capture.json) · [展開](extraction.json)

Pod `tbj4mepark90np` は11:25:01.134UTC作成、11:34:25.363UTCに削除・不在確認。絶対11:55UTC期限内。担当と主担当の別API照会はGET404、専用名0、全Pod0。作成から不在まで564.229秒で、計算と一時ディスクの時刻見積US$0.0929062。11:42UTCの追加照会でも専用請求明細は未反映で実費未確定。[資源](resources.json) · [削除原票](cloud-run/cleanup.json) · [主担当の不在確認](lead-cloud-resource-check.json)

Cの新規保存は約171MB（記録追加前）、512MiB運用上限内。Dへの書込は0。ローカル展開は各ファイルごとに保存量を全走査する実装で遅く、展開継続中を誤認して図を先行生成した。図の入力は既に展開済みだったが、集計は展開原票未存在で停止したため、展開完了後に集計だけ再実行した。凍結コード・入力・科学条件は変更していない。
