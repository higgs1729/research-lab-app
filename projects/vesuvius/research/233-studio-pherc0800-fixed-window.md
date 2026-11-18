Status: resolved
担当: 研究（r233_studio_pherc0800）

# 233: Studio softlossは保存済みPHerc0800の固定窓にCT追試する字画を残すか（2026-11-15）

## 依頼
- 問い: R232で実行検証したStudio softlossを、R220/R223で字画候補を選べなかったPHerc0800公式面4の同じ約9.2mm角の保存済み窓へ適用すると、元CTへ追試する字画または文字行が選べるか。
- 背景: R232は既知0343の輪と主明部を再現したが細部の分離は弱い。新モデルによる独立した追加介入として有限の一窓比較を選ぶ。従来より良いと仮定せず、候補0ならこの窓のモデル比較を終了する。PHerc0306Bの未確定候補の局所幾何診断へは戻らない。
- 材料の例: `experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/` のnative31.npy、入力契約、plan、原寸比較。面20251028222030-auto_grown_20251028222030940、native主域[142,640,1067,1067]、既存support[0,384,1536,1536]。新CT取得は不要。上流コード/重み/モデル・推論の基準はR229/R232。
- 欲しい形: 入力の元データ・座標・深さ順と上流モデルの関係を明示した事前計画、固定窓の全支持パッチ、正規化のデバイス別照合、結果と原寸図、前モデルとの同じ座標での比較、採用ROIか候補0の判断。深さ順を0343の符号だけから推測しない。公式生成/作者のデータ準備の根拠を読む。向きが決められなければ事前に二順まで固定して比較してよいが、出力を見て追加の深さ/閾値/向きを試さない。
- 検証: R232で検証したcrop・GPU FP32 clip200/div255・central96・stride64・sigmoid/Hann・nonzero maskを維持。入力/位置/深さ/shapeは厳密に照合し、全出力再構成を主担当が別実装で確認する。既存0343 CPU参照3件を同じモデル実行でGPU比較する方法を使用可（新CPU forwardの重複を避ける）。未知入力自体のCPU参照を追加するなら必要性と費用を説明。CPU/GPU出力許容1e-4、他の資源余裕は下げない。
- 資源と費用: Dは読取のみ、Cへ新規成果物。既存キャッシュを再利用し、モデル重みは必要ならRunpod内に一回だけ取得する。出力と入力サイズから結果物理予約・C最大書込量・転送/回収枠を具体的に見積もる。大きな入力/結果へ12MiB予約と120秒回収枠を無根拠に流用しない。Runpod一台・USD0.35運用枠・絶対30分以内削除を基本上限に、実行前に主担当へplan/diff/見積を提示する。本人への再承認要求は不要。ローカルFIFOの空きを長く待たず、一件ずつ。全ての台の削除と別不在確認まで担当する。
- 科学判断: 明るさ・モデル間一致・輪の形だけを文字の証拠にしない。採用するなら固定座標と元CTで判定する問いを残す。候補0でも巻物全体のインク不在や未知性能を主張しない。新文字の発見は別の検証まで0とする。第四応募項目にも数えない。
- 終了: 全結果の評価・記録までこの研究内で進める。候補0ならこの窓の比較終了、候補があれば次の科学的追試案を一件だけ提示。新しい外部公開や投稿はしない。登録済み原票は変更しない。研究票へ結論を追記し、主担当の独立検証後にmanifest/record候補を凍結する。

## 結論

[一次・担当と主担当の別目視、2026-11-15] **追試ROIは0。PHerc0800のこの固定窓でのモデル比較を終了する。** R220 Hecate、R223 Reader V3と同じ約9.2mm角へStudio softlossを適用し、中央16層の二順を全支持パッチで比較した。明るい孤立塊や拡散した角/鉤状応答はあるが、元CTへ追試する連続した字画・文字行を選べなかった。文字の発見0、第四応募項目0、新しい観測窓0。これをこの窓や巻物全体のインク不在と解釈しない。

651 GPU forwardを152.481秒で完了。既知CPU参照3件の出力最大差9.23872e-7は許容1e-4以内。主担当の独立float64再構成は両順各1,138,489画素で最大差1.57837e-7、表示9画像/36パネルの差0。台は564.229秒で削除され、担当・主担当の別照会でGET404・専用名0・全台0を確認。費用の時刻見積US$0.0929062、請求明細未反映で実費未確定。

[実験まとめ](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/README.md) · [独立出力検算](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/lead-output-check.json) · [独立表示検算](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/lead-display-check.json) · [主担当の別目視](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/lead-visual-review.json)

## 根拠・詳細

### 固定した入力と向き

- [一次、2026-11-15] R223保存のnative31（31×1536×1536、uint8、SHA `bd6e0d9469710378cf349d13698d0fa917941213377c5314d349f9e318384691`）から、原点 `[0,384]` に対する `[48:1264,176:1392]` を切り出した。新しいCT取得・補間は0。主域は同じnative `[142,640,1067,1067]`、文脈域 `[48,560,1216,1216]`。面全体2580角のstride64格子から主域へ寄与する全324位置/順を採用し、all-zero入力でもパッチを省かず、最後に元CT16層が全0の画素を0へ戻す作者方式を維持する。
- [一次、同日] 作者 `prepare_reader.py` は公開Zarrの `label_z−8 … label_z+7` を保存順のまま用いる。0800の31層の中央index15にこの選び方を当て、7〜22の16枚と同じ16枚の逆順22〜7に凍結した。公式metadataはZYX・31層・step1・8.64µm・translation0を示すが、0800面の法線方向と学習時方向の対応は示さない。0343の原CTオフセット符号との一致は仮定しない。法線・表裏は未確定であり、出力を見た後の深さ移動・第三の向きは行わない。
- [一次、同日] 入力値・座標・深さ順・shapeとCPU直接除算のSHAを事前固定。モデル前CUDAプローブは全256値と全651パッチを、FP32 clip200/div255のGPU実算術（丸めた逆数乗算）のSHAへ厳密に照合する。R232と同じ作者crop、モデル、central96、sigmoid、pixel-centred Hann、batch1、TF32 off/FP32を用いる。未知入力のCPU forwardは追加せず、R229の既知CPU参照0/47/95を同じモデルloadで先にGPU照合する。これは実行経路の対照で、未知入力のCPU出力全体を別に測ったものではない。

[入力計画](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/plan.json) · [入力契約](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/input-contract.json) · [パッチ契約](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/patch-contract.json) · [主担当の元入力・格子照合](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/lead-source-grid-check.json)

### 実行・判定・資源

- [一次、2026-11-15] 既知0343の3パッチを先にGPU比較してから未知forward324・reverse324を実行。モデルload1回、CPU forward追加0。入力全256値と全651 SHAのGPU照合を完了。既知CPU出力との差maxは0/47/95の順に1.93715e-7、9.23872e-7、6.25849e-7。主担当は全651行、全256ビットと両出力の全画素を別コードで照合した。
- [一次・原寸目視、同日] 固定主域の生表示と非ゼロCT画素median〜p99.5表示、およびCT/Reader/Hecateを同位置で比較。順方向は中央下方・下辺近くの丸い塊、上方の拡散する角/鉤状応答、逆方向は左中央・下方の塊に強調が変わったが、担当・主担当とも字画の連続や文字行を選べずROI0とした。図4象限はnative1:1。Hecateの9.6µm像は保存座標式に従ってnativeへbilinear変換した比較であり、深さ・前処理・モデルの差を含む。高応答・一致だけを文字の証拠にしない。
- [一次、同日] Secure A40一台 `tbj4mepark90np`、CA-MTL-1、USD0.59/h。作成11:25:01.134UTC、削除・不在11:34:25.363UTC、絶対11:55UTC期限内。重み893,443,724BはPod内で一回取得。入力archive21,762,239B、回収archive34,856,330B（64MiB物理予約の同fileID・SHA一致）、展開670ファイル/55,156,084B。C保存約171MBは512MiB上限内、D書込0。計算/一時ディスクの時刻見積US$0.0929062、11:42UTC専用明細0行で実費null。担当・主担当の不在確認は別API読取で各GET404/専用名0/全台0。

[担当所見](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/visual-review.json) · [表示原票](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/comparison.json) · [資源](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/resources.json) · [主担当の削除別確認](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/lead-cloud-resource-check.json) · [追加請求照会](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/resource-billing-followup.json)

## 取得の経路

R223保存native31と公式metadataを再利用し、R229保存の作者prepare_reader.py/README/hf推論を読んで深さを固定した。R232 archiveから同じモデルsource/runtimeを借り、変更は入力・二順のループ・結果規模に応じた64MiB物理予約/360秒回収を中心に限定。[差分](../experiments/vesuvius/discovery/20261115-studio-pherc0800-fixed01/r232-diff.patch)と親clearanceを保存した。新しい環境構築・CT取得・手元GPUの空き待ち・実行再試行は0。

## 本人への質問

なし。候補0の事前終了条件に従ってこの窓の比較を閉じた。法線方向・紙層帰属・インクの有無は未判定だが、今回の結果を救済する追加深さ/向き/閾値の試行は行わない。次の投入先は主担当が別に選ぶ。

## メモ

- 2026-11-15 着手: 共通指示・lead・researchスキルとR223/R229/R232を確認。R223 native31を切り出し、新CT取得・CPU forward再実行なしでR232の実行経路を再利用する。作者prepare_reader.pyは公式Zarrをlabel_z−8..label_z+7の保存順で使用するが、0800面の法線/学習方向対応は未検証。中央z15の7..22と同じ16枚の逆順22..7を事前固定する案。324支持パッチ/順と既知0343 CPU参照3件を同一モデルloadで実行予定。計画・回収予算を作成中、Pod作成0。

- 計画凍結: 作者prepare_reader.pyのlabel_z−8..label_z+7保存順から7..22と22..7を採用（主担当も採用）。metadataはZYX/31層/step1/8.64µm/translation0、0800のモデルに対する法線向きは未確定。native主域[142,640,1067,1067]、全支持324/順、bbox[48,560,1216,1216]。651パッチのraw/CPU正規化SHAを生成、既知CPU3との同一値照合と全23,658,496未知入力値の保存元一致をオフライン確認。plan・cloud-plan・差分を主担当へ提示。archive21,762,239B、NPY結果53,683,530B、物理予約64MiB、回収360秒、C新規上限512MiB/予想約240MiB。8〜16分US$0.079〜0.159、運用枠0.35、絶対1380秒までモデル→1740秒回収→1800秒削除。CPU forward追加0・Pod作成0。初稿の旧予算ラベルはattempts/01-draft-budget-labelsへ保持し、実効予算を訂正した。

- 回収後: Podは11:34:25UTC削除。archive34,856,330Bの保存SHA一致。ローカルextractは各ファイルでwritten_bytes()が全木を走査するため時間を要した。私が継続中sessionを終了と誤認しfiguresを先行起動し、必要なmain配列は既に保存済みで図生成は成功したが、summarizeはextraction.json未存在で停止（出力未書込）。既存展開を完走させ、summarizeのみ再実行する。凍結コード・科学条件は変更せず、別の性能研究は起こさない。担当はwhole raw2枚と原寸4象限を目視し追試ROI0と判定、独立数値/別目視は主担当待ち。

- 完了: 主担当の全入力・全出力・表示検算と別目視が通過。担当/主担当ともROI0。この固定0800窓のモデル比較だけを終了し、研究票をresolvedとした。manifest/record候補は親原票を含めて凍結、lab登録は主担当が行う。
