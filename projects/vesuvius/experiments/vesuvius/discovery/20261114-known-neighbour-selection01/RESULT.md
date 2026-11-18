# PHerc0343の既知面に続く公開応答

研究179、2026-11-14 JST。既知受賞面と同じメッシュの東側に、受賞画像の範囲をまたぐ横長の公開反応がある。受賞者の文字箱や公開範囲と座標照合できたが、独立した新しい字画や行は選べなかった。選定した次の一件は、既存公開反応の紙面対応を元CTで調べる局所診断。未読文字のROIは保留した。

## 公開済みと範囲不明

- 公式はErwin Nieuwlaarのw047/w048接合面で4行の部分を認め、主行の10文字を受賞の根拠とした。公式注記図は文字の読みを示す。受賞者の2本の基線と18個の箱は位置資料で、公式認定数や公式の全可読領域とは一致を前提にしない。受賞者の画像矩形全体を公開済み画像範囲として扱い、文字箱外も公開済み画像と記録する。公式は同じ巻物のGabriel Munoz MendoncaとBen Kylesらの別提出にも読みを報告する。保存した公式他提出図はMendonca段落の直後にあり、Kylesらは別地域と記述される。いずれも確認資料からwinner/atlas/CTへの位置対応は確定できなかった。公式リンク先ScrollFiesta公開repoの固定木6185件にも対象名の出力パスは見つからず、配布元全体での不存在までは確認していない。[公式発表](https://scrollprize.substack.com/p/50k-first-letters-prize-awarded-for) · [公式注記図](official-annotated.png) · [公式他提出図](official-other-submissions.png) · [ScrollFiesta固定木](https://github.com/Hob3rMallow/scrollfiesta_public/tree/3c46077968c0151dd185656c16d5063cdbb3f5aa)
- 受賞者の固定commit e8370f1f88a211166056df62ea6fcfffe4a1063e、連結面 concat_w047-w048_R5B2_z9500-11000、scan 20250509220833、masked volume 20250521140437、8.64 µm 116 keV。公式はsurface m7 (20260413222639) とlasagna予測の来歴も掲載。固定atlas ac5ffd7098120368216948c4e06c494bf8e67178 の kbh-POS_PHerc0343_erwin は、固定survey 1f12c1ceb14c1f24acc48249eaad60bcdf541721 の同名面。winner/R173のXYZ TIFFファイルSHAは異なるが、全43,008 float32/軸がビット一致した。親担当も独立照合した。受賞者と公式はPHerc0343を学習に使っていないと述べる。atlas metadataの両モデルはexposure unknownで、初期化を含む全学習座標の非重複は未検証。受賞者の4モデル31深さ・zero-pad＋パッチ位相マージと、公開atlasの7モデル・R175の局所対照は条件が異なる。R175はこの環境の再現差を確認した研究。[受賞者固定repo](https://github.com/Nieuwlaar/pherc343-first-letters/tree/e8370f1f88a211166056df62ea6fcfffe4a1063e) · [公式データ](https://scrollprize.org/data_browser/PHerc0343) · [親数値照合](lead-known-check.json)
- sidecarのraw XYXY [380,105,6021,2560] は両軸反転して画像panel XYWH [173,182,5641,2455] へ1:1配置。公開18箱のraw→reading localは [6021−x1,2560−y1,6021−x0,2560−y0] で全一致。受賞rawは6720×2560の8.64 µm、atlasは6048×2304の9.6 µm。同じ20 voxel格子の画素中心なのでatlas連続端は raw端×0.9、pixel indexは 0.9(raw_index+0.5)−0.5。受賞画像の東端はatlas x=5418.9、中心が外にある整数列はx≥5419。受賞PNGと公式注記図の画素登録は未実施。公開矩形の外を未読の境界にできない。[受賞原画](winner-original.png) · [sidecar](concat_w047-w048_R5B2_z9500-11000.json) · [同座標の全体図](atlas-coverage.png)

## 一領域と次の診断

既存公開atlasのXYWH [5248,512,768,768] は全面stride64位相、同等パッチ支持の内側 [5312,576,640,640]。受賞18箱と交差0、四隅が有効な面画素589,824/589,824、四隅有効セルの4近傍で箱1と連結する。これは座標上の連続性。CT中央には裂けや空隙があり、実物の同一紙面は未確認。ensemble reverseは画像境界をまたぐ横長の飽和した強い帯、dense reverseも広い帯、seed42 reverseは枝や明部が分かれる。親・担当の別目視で新しい字画や行を確定できなかった。公開予測が既にこの端を覆うため、同じ二モデルの中央窓を再実行して同様の絵を得る工程は今回の問いを解かない。[原寸比較](atlas-east-crop.png) · [位置計算](candidate.json) · [親目視](lead-known-visual.json)

次の一件は **同じ公開応答帯のCT紙面診断**。同一面のatlas座標 (5376,736) を受賞画像内・箱外の接続点、(5504,704) を画像外の帯、(5824,704) を画像外の離れた明部とし、公開予測の見え方を根拠に3地点を固定した。3点の元CT位置は既存メッシュの双線形から求め、各中心でネイティブ直交65×65を3面と、既存observer/公式rendererで64²×33層の法線断面を一件として見る。scale .9、step1.111、linear、同じmasked L0。暗部や折れが同じ紙面に連続するか、境界や別層を拾うかを事前の問いとする。支持と近傍が揃えば外側で連続紙面／裂け目・多重紙面／未判定を記録する。紙面確認はインクや新規性の証明にはならない。可読候補と既知提出のCT位置資料が揃った場合にのみ後段を再選定する。[固定3地点とキー包絡](probe-plan.json)

保守包絡18キー36 MiB、R173既存2キー4 MiB、追加16キー32 MiB。親の独立計算では3地点のXYZ差は最大9.1×10⁻¹³ voxel未満、キー集合と既存2キーは全一致。実observerで64²支持を確定し、固定直交断面のキーを加えHEAD・ETagを照合。追加40 MiBまたは取得180秒を超える場合、必要支持が欠ける場合は取得・解釈を停止する。R173の通信・描画実測から追加取得は1～2分程度、observer・描画・集計それぞれ120秒、CPU1/4 GiB、C作業128 MiBを提案。実行時間は見積もり。768²全域の保守包絡は133キー266 MiBで、今回の問いには3地点を優先。公式rendererとseed42/dense-nativeは同じ面・体積で再利用可能だが、今回提案は推論0回。別の既知面周辺は、既読図と固定meshをCTへ結び付けられる場合には価値がある。今回のPHerc0343紙面診断と並行せず、未登録の他提出面や別巻物は選定しなかった。[親の別計算](lead-probe-check.json) · [R173](../../../../research/173-pherc0343-ct-readable-control.md) · [R175](../../../../research/175-pherc0343-patch-phase.md)

## 取得と再現

既存R168/173/175と公式HTMLを再利用。新規保存本文12件14,562,993 B、最大8,801,558 B。コネクタのGit木・commit照会は取得票に分けて記録。最大16 MiB、全体64 MiBの範囲内。既存画像からの切り出しと保存meshだけで計算した。新CT本文、モデル、描画、推論、追加クラウド費は0。作成順は coverage.py、edge_view.py、position.py、probe_plan.py。[取得票](acquisition.json) · [lab登録候補](record.json)
