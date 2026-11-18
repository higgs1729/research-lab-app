Status: resolved
担当: 研究（R179担当、2026-11-14）
Blocked by: 178

# 既知文字を対照にできる隣接未読領域を、小実験の対象として選べるか

## 依頼

2026-11-14 JST。本人の主目標は未読文字の発見。178までのPHerc0800・PHerc1218・PHerc0846A・PHerc1545の固定試験では独立した字画/行候補を確認できず、各条件の追加探索を閉じた。一方、PHerc0343の既知受賞面では元CTと公開画像が対応し、175でモデルの全面パッチ位相を揃える効果が確認できている。次の一件は、文字がある根拠を持つ既知面の隣接部分へ進めるか、公開済みの文字と切り分けて判断する。

PHerc0343を第一候補として、受賞者と公式の公開成果が覆う範囲、利用可能な面/CT/予測の来歴と範囲、近傍に延ばせる面の有無を一次資料から調べ、次の小さい試験一件を提案する。既存の173/175や168の保存一次資料を利用し、同じ資料の再取得を避ける。既知の可読性を再表示するだけの候補は新規発見と呼ばない。公開された未読面や予測の利用自体は除外しないが、既存の可読部分・学習露出・既存予測と比べて何を新しく判定するかを明確にする。既存成果の外周であるだけで未読と断定せず、座標対応が不明なら不明として残す。

出力は、可読/未確認/不明の範囲の根拠、候補のsurface/volume IDと固定参照、次の入力位置または位置を決めるための最小の問い、想定する処理と追加取得量・時間・停止条件。現在のseed42/dense-nativeと公式rendererを再利用できるかも判断する。PHerc0343で根拠が足りなければ無理にROIを選ばず、不足点と、別の既知文字の周辺を調べる価値があるかを明示する。全巻物を再調査する一覧作成や、既存の陰性試験の設定変更は行わない。

この研究は資料と既存データによる選定まで。新規CTボクセル、モデル重み、ビルド、推論、GPU、有料計算、外部投稿/公開/連絡は行わない。必要なら小さな位置資料や原画像・メッシュは取得できるが、新規本文合計64MiB・単体16MiB以内。超えるものは本文取得前に主担当へ見積もりを返す。新しい取得の参照/件数/実長を保存し、ソース全文の大量表示を避ける。Dは読取のみ、Cへ保存。既登録原票は変更しない。

保存先 experiments/vesuvius/discovery/20261114-known-neighbour-selection01/。研究票へ結論と取得経路を追記し、根拠原票とmanifest・lab登録候補を残す。重要な位置や範囲は主担当が別確認できる形で渡す。追加クラウド費0、サブ委任なし、lab登録は主担当。今回はgpt-6.1-sol / xhighを選ぶ。既知可読範囲と隣接候補の来歴・座標・新規性の境界を結び付ける未確定の選定で、固定手順の実行ではないため。178完了後の逐次実行。

## 結論

**未読文字の候補ROIは保留し、PHerc0343の受賞面東側で、公開予測の横長の帯が同じ紙面に沿うかを調べる小さい元CT診断を一件選んだ。** 受賞者の原画と文字箱を既存atlasへ結び付けた結果、強い帯は受賞画像の東端をまたぎ、atlasですでに公開されていた。親・担当の原寸目視で新しい独立字画や文字行は確認できなかった。受賞画像外という条件から未読は判断できず、公式が公表した他提出の位置との重なりも未確定。[同座標の原寸比較](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/atlas-east-crop.png) · [親目視](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/lead-known-visual.json)

## 根拠と範囲

- [一次、2026-11-14 JST] 公式はErwin Nieuwlaarのw047/w048接合面で4行の部分を報告し、主行を受賞根拠とした。受賞者の公開18箱・2本の基線は位置資料。公式は同巻のMendoncaとKylesらの別提出にも読みに言及したが、確認資料から他提出をwinner raw/CTへ登録できなかった。既存予測が公開されている範囲と、読みが公表された範囲を別々に記録した。[公式発表](https://scrollprize.substack.com/p/50k-first-letters-prize-awarded-for) · [公式注記図](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/official-annotated.png) · [受賞者固定版](https://github.com/Nieuwlaar/pherc343-first-letters/tree/e8370f1f88a211166056df62ea6fcfffe4a1063e)
- [一次・計算] 受賞面 concat_w047-w048_R5B2_z9500-11000 とR173 atlas面 kbh-POS_PHerc0343_erwin は、XYZ各43,008 float32全値がビット一致。scan 20250509220833、masked volume 20250521140437、8.64 µm 116 keV。受賞raw XYXY [380,105,6021,2560] は上下左右反転して公開原画のpanel [173,182,5641,2455] に配置。18箱の座標変換を親も独立照合。9.6 µm atlasでの公開画像東端は連続座標x=5418.9、画素中心が外にある列はx≥5419。原寸比較領域 atlas XYWH [5248,512,768,768] は18箱と交差せず、メッシュ上は既知箱と連結するが、局所に裂けや空隙があり物理紙面の対応は未確定。[全体図](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/atlas-coverage.png) · [位置計算](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/candidate.json) · [親の独立照合](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/lead-known-check.json)
- [一次・範囲] 固定atlasはac5ffd7098120368216948c4e06c494bf8e67178、固定surveyは1f12c1ceb14c1f24acc48249eaad60bcdf541721。受賞者・公式は使用モデルのPHerc0343未学習を報告する。atlasの2モデルのexposureはunknownで、初期化を含む全学習座標との重複は未検証。受賞者自身がzero-padと位相マージを記載しており、175はこの環境での再現差を測った結果。[根拠と来歴](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/RESULT.md)

## 次の一件

atlasで受賞画像内・未箱の [5376,736]、画像外の帯 [5504,704]、画像外の明部 [5824,704] を固定し、各地点の元CT直交3断面65²と、同一面64²×33層の短い法線断面を比較する。3地点はいずれも公開応答を調べる点。既存R103/公式rendererを借り、scale .9・step1.111・linearで幾何と支持を先に確認する。保守18キー36 MiB、R173再利用2キー、追加16キー32 MiB。親の独立計算でXYZと集合を確認した。取得上限40 MiB・180秒、各処理120秒・1CPU/4 GiB。支持不足や上限超過で停止する。確かめるのは、帯が同じ紙面に沿うか、裂けや多重紙面を拾うか。既存seed42/dense-nativeは再利用可能だが、この診断に再推論は不要。字画と先行範囲の根拠が揃えば後段を別に選ぶ。別の既知面周辺は同じCT上で位置を登録できる場合に価値があり、今回は選定しなかった。[固定点・資源](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/probe-plan.json) · [親の別計算](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/lead-probe-check.json)

## 取得の経路とメモ

GitHub固定木で本文サイズを確認し、受賞sidecar・箱・行・コード等は固定commitのconnector、PNGとXYZは固定raw。公式原画像2枚は保存済み168の発表HTMLから取得。新規保存原文・画像・mesh12本文14,562,993 B、最大8,801,558 B。Git木等の照会容量は別記。既存atlas画像を同じ座標で切り出した。新規CTボクセル・推論・描画・重み取得・追加クラウド費0。[取得票](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/acquisition.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-known-neighbour-selection01/record.json)
