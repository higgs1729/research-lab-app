Status: resolved
担当: 研究（R167担当 2026-11-14 JST）
Blocked by: 166

# PHerc1218の別来歴二面の公開CT・予測画像に、追試する価値のある文字候補があるか

## 依頼

2026-11-13。未読文字の発見が本人承認済みの主目標。165/166のw083_main固定256²は元CT対応の計算は正しいが、物理紙面対応と一定補正量は独立目視でも未判定。根拠のない補正や同じ小領域の再推論を行わず、同巻の別来歴二面について、既存の公開結果を借りて次の投入価値を判断する。

対象は研究164で保存したSharpMeow/first-letters-ink-atlasの固定revision ac5ffd7098120368216948c4e06c494bf8e67178、PHerc1218の kbh-PHerc1218_3144_3279_16272 と kbh-PHerc1218_4203_4343_16272。入口は experiments/vesuvius/discovery/20261113-next-target01/{ink-atlas.md,ink-atlas-index.json,1218-atlas-info.json,atlas1218-3144-meta.json,atlas1218-4203-meta.json}。画像実体はまだ取得していない。メタデータのaliveやface一致は文字の証明ではない。

問いは二面に、CTの紙面・繊維と位置が対応した字画様のまとまりや行構造があり、元CTから独立に確かめる一件を選ぶ根拠になるか。公開予測は他者の成果であり、その画像を再表示・読み取るだけで自分たちが検出法を開発したと主張しない。未判読の公開候補は利用できるが、先行判読・訓練/予測重複・出典と私たちが加える差分を区別する。

画像を開く前に固定版のファイル一覧で入力URL・サイズ・LFS/本文SHAの根拠を確定する。取得はまず各面の ct_mid.png と ensemble/forward.png・ensemble/reverse.png（計6枚）。同じ図に各モデルの追加マップを大量に増やさない。図に分かりやすい候補がある場合だけ次に必要な確認を別に提案する。無ければ陰性/未判定を区別して閉じる。原画を保持してネイティブ解像度で見る。必要な一覧図は同じ固定階調・物理尺度・出典付きで作り、内容補完・生成画像・手描き文字・局所的な選別強調は行わない。

model ensembleの正規化と順方向/逆方向の意味をカード・metadataから確認する。逆方向モデルが文字を出さないことを必須条件にはしない。幾何や繊維に沿う反復模様・亀裂・境界の高出力と、文字らしい別々の画が行をなす場合を分ける。文字を確信できない場合は転写を捏造せず、保存全図と候補座標（あれば）で親へ独立目視を依頼する。既存のw035既知文字の出力を表示の工程対照に使う場合、訓練領域であり未知性能対照でないことを明記する。

取得上限は固定6画像の本文計24MiB、取得工程120秒、作業128MiB、C:空き10GiB。最初に全HEAD/固定木のサイズを確認し、上限内のみ逐次GET、取得SHA/実サイズ/ETagを保存する。予期しない大きさ・欠損・版不一致・上限超過で停止し、別画像を黙って追加しない。解析/一覧図はCPU1/AS4GiB/core0/数値thread1、120秒。通信は取得時だけで、画像評価中の新推論はしない。

元CTチャンク、メッシュ本文、モデル、学習/推論/ビルド、外部公開/メッセージ/応募、サブエージェント、有料計算は行わない。C:新folder experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/ に固定入力、実画像、判断と資源を保存。研究票に結論と根拠を追記、lab候補を用意。初期月次三件の成果は変更しない。

今回の担当は gpt-6.1-sol / high を明示選択する。候補二面と画像六枚を固定した既存公開成果の取得・比較で、方法開発やパラメータ探索を含まず、解釈しながら品質を確かめる仕事としてhighを選ぶ。逐次実行を維持する。

## 結論（2026-11-14 JST）

［一次・目視］SharpMeowの公開アトラスの固定二面を、各CT中央層・ensemble forward・reverseの計6原画で確認した。固定6画像から、元CT追試へ進める字画のまとまりや行の位置を選べなかった。3144では右下の裂け・変形の形状が予測にも現れ、4203では周縁の帯、孤立した広い斑点、細かい不定形の明点が主だった。方向一致は判定条件にしていない。採択座標・転写なし。インクの有無、物理紙面、別深さ・別モデルでの結果は未判定。主担当も一覧と全6原画を別に目視し、追試候補なしで一致した。 [比較図](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/comparison.png) · [目視・再利用条件](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/README.md) · [主担当別照合](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/lead-check.json)

［一次］公開カードはzスコア平均を説明し、両面のmetadataでは7モデル・z表示域−2〜+4。今回のensemble/は保存深さ順を基準とし、逆順にも基準側の統計を使う。公表学習リストに対象巻がないというカードの記述に対し、両面の面metadataは全7モデルでexposure unknown、source null。学習・先行判読・w083_mainとの物理重複は未確認。3144の欠損4 CTチャンクの位置と影響は未確定。予測・CT図は公開アトラス作者の成果で、今回追加したのは固定取得と比較・選定判断。 [固定アトラス](https://huggingface.co/datasets/SharpMeow/first-letters-ink-atlas/tree/ac5ffd7098120368216948c4e06c494bf8e67178) · [比較根拠](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/README.md)

［一次・取得］固定木と全6 HEADを先に照合し計画を凍結。その後6本文だけを逐次取得し、計9,565,668 B、GET 10.919秒。本文SHAは固定木LFS SHAと全件一致。原画は2016×2016の8bitグレー、原画9.6 µm/px。原寸タイルは全24パネルの画素一致を照合し、一覧は共通の3分の1縮小で局所階調調整なし。図生成はCPU1・Windows commit上限4 GiB・数値スレッド1、2.398秒、最大RSS97,296,384 B。WindowsではLinuxのAS/core上限は適用していない。追加CT・メッシュ・モデル・推論・課金・公開0。 [凍結計画](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/acquisition-plan.json) · [取得結果](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/acquisition-result.json) · [lab登録候補](../experiments/vesuvius/discovery/20261113-pherc1218-map-screen01/record.json)
