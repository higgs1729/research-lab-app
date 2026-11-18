Status: resolved
担当: 研究（R168担当 2026-11-14 JST）
Blocked by: 167

# 同じ公開atlasの既知文字対照で、文字を識別できるか

## 依頼

2026-11-14 JST。167のPHerc1218二面は6原画に追試する字画/行の候補を選べなかった。未知面の追加計算へ進む前に、同じ表示・予測系が既知文字を識別可能に出すかを一面で確かめる。新モデルや候補の広い探索はしない。

固定atlasは SharpMeow/first-letters-ink-atlas revision ac5ffd7098120368216948c4e06c494bf8e67178。既存164の ink-atlas-index.json は PHerc0343 の reference 七面を列挙し、一面は surfaces/PHerc0343/kbh-POS_PHerc0343_erwin。この一面を対照候補とする。名前だけで既知可読文字があると決めず、固定meta.jsonと上流の一時資料で受賞領域との対応を確認する。公式発表へのカードリンクは https://scrollprize.substack.com/p/50k-first-letters-prize-awarded-for 。必要な一次資料は5ページ以内、本文合計2MiB以内。学習一覧との非重複未監査と、既知文字での表示対照という役割を区別する。

対応を確かめた後、この一面の ct_mid.png, ensemble/forward.png, ensemble/reverse.png の3枚のみを取得する。対象固定木とHEADを先に確認し、URL/サイズ/LFS SHAを取得前に保存する。もし候補IDが受賞面と対応しない、メタデータ欠損、サイズ上限超過なら新しい面を黙って選ばず理由を返す。元CT/mesh/重み/各モデル追加マップの取得や推論を行わない。

取得上限は画像本文計24MiB、画像取得工程120秒、作業128MiB、C空き10GiB。図の処理は120秒、CPU1/メモリ4GiB、数値thread1。既存の制限ランナーを再利用し、Windows commitまたはLinux ASなど実際の制限方法を正確に記す。追加依存導入・ビルド・GPU・有料計算・外部公開/連絡・サブ委任なし。Dは読み取りのみ。

原画を保持。CTと両予測を同じ9.6um尺度・固定0–255で並べ、目視は原寸も使う。画像生成モデル、文字の補完、局所的な選別階調強調は使用しない。既知文字らしい独立線/行構造を特定できるかを記録し、根拠となる原画XYの範囲を保存する。公式読解を知った上で同じ文字を想像して補うのでなく、図で見える線と読解済みという外部根拠を別に書く。逆側の反応が無いことを必須条件にしない。親が原画で別目視する。

この対照も字画を示さない場合、167の陰性結果がatlas表示・ensembleによる見落としを含み得ることを残す。示す場合も、未読巻全体に対する感度/特異度を示したことにはしない。1つの工程対照として次の候補選定に活かす。

保存先 experiments/vesuvius/discovery/20261114-atlas-known-control01/ 。出典・credit・CC-BY-NC4と計測、結論、再利用手順、研究票追記、lab候補を用意する。登録は親。167の取得と表示コードを借りられる箇所は借り、検査の新実装を主な成果にしない。

担当は今回の一面・3画像・既存手順の確認に gpt-6.1-sol / high を選ぶ。一次資料の対応づけと視覚比較の解釈が必要であるためhighとし、研究は引き続き逐次。

## 結論（2026-11-14 JST）

［一次・目視］同じ公開atlasの既知PHerc0343面では、167と同じ固定0–255表示と9.6 µm/px原寸で、reverseに複数の字画様の部分が並ぶ行構造を確認できた。根拠は主行中央 x=[2880,4130), y=[700,1110)、主行左 x=[740,2260), y=[980,1440)、下段 x=[1420,3310), y=[1430,1830)。輪状の暗い隙間、縦画状の立ち上がり、湾曲した部分と間隔があり、forwardより並びを追いやすい。飽和・癒着も残り、公式画像との画素登録、公式行番号の同定、今回の画像からの転写はしていない。 [全体比較](../experiments/vesuvius/discovery/20261114-atlas-known-control01/comparison.png) · [原寸XYと所見](../experiments/vesuvius/discovery/20261114-atlas-known-control01/README.md)

［一次・来歴］固定面metaは固定surveyのPOS_PHerc0343_erwinを指し、同surveyがErwin NieuwlaarのFirst Lettersセグメントを文字あり対照と記す。主催発表と受賞者資料は、w047/w048をつないだPHerc0343の受賞面を記述する。受賞面に由来する表示対照と判断した。メッシュ同一バイト・公式判読画像とatlasの画素登録は未照合。学習重複の独立監査、未知面での感度・特異度、167二面のインク有無は未評価。 [公式発表](https://scrollprize.substack.com/p/50k-first-letters-prize-awarded-for) · [来歴照合](../experiments/vesuvius/discovery/20261114-atlas-known-control01/source-match.json)

［一次・取得］一次資料5件278,504 B。固定木とHEADで計画を凍結後、3画像11,311,667 B、GET 5.450秒で取得し、LFS SHA・サイズ・ETagを照合した。原画は6048×2304の8bitグレー。原寸の3領域×3パネルの全画素は元と一致。図生成と照合2.468秒、最大RSS72,470,528 B、CPU1・数値スレッド1・Windows commit上限4 GiB。追加CT・メッシュ・モデル・推論・クラウド支出・外部公開なし。 [取得結果](../experiments/vesuvius/discovery/20261114-atlas-known-control01/acquisition-result.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-atlas-known-control01/record.json)

［一次・別照合］主担当は比較図と原寸3範囲を別に目視し、reverseの主行と下段で同様のまとまりを確認した。3原画の固定木SHA・サイズ・PNGヘッダーも別照合済み。逆順優位はこの一例の観測。 [主担当別照合](../experiments/vesuvius/discovery/20261114-atlas-known-control01/lead-check.json)
