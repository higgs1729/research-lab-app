# atlasの `sheet_fraction` と中央CTマスク

[研究203](../../../../research/203-atlas-sheet-mask-semantics.md)（2026-11-14 JST）。固定atlasの公開中央PNG 8枚に、著者が参照するvilla PR #2318のマスク関数を適用した。フォールバック後に採用する画素数は、8面すべてでメタの `pixels_used` と完全一致した。0175Bの `sheet_fraction=1.0` は、元の繊維交差マスクが小さく、正値のCT全体で比較した面の値。主担当も独立に実装した式で8面のマスク画素数と分岐を再現した。 [実測](measurements.json) · [独立計算](lead-formula-check.json) · [固定atlasカード](../20261113-next-target01/ink-atlas.md) · [PR原文](https://github.com/ScrollPrize/villa/pull/2318)

## PRの式と公開値

- [一次] PR head `4bbdf01314da473cd5bb720d0cb5a1498a32eddd` は2026-11-01にclose、mergeなし。中央CTを正値の1/99.5百分位で正規化して0–1へclip。12方向（0°〜165°、15°刻み）、λ=8pxの零平均Gaborの応答二乗を64×64平均して方向別エネルギーを求める。正規化CT >.02の64²局所割合 >.90をvalidとし、直交/最大エネルギー比をvalidで重み付けして129²で平均する。判定はcrossness≥.31かつvalid。局所平均なので、マスク内にCT値0も入り得る。 [固定PRコード61–83行](https://github.com/ketchupbyheinz/villa/blob/4bbdf01314da473cd5bb720d0cb5a1498a32eddd/vesuvius/src/vesuvius/ink_detection/face_check.py#L61-L83)
- [一次] PRのCLIでは予測とCTの最小共通H×Wに左上合わせで切り、`sheet_mask.sum()/(H×W) < .05` で `ct > 0` に切り替える。5%ちょうどは切り替えない。CLIは採用マスクの `pixels_used` を出す。採用マスクはモデルの百分位、IoU、768²タイルの支持と暗部比較にも入る。作者が意図した用途は、繊維模様や空隙の反応からモデルが片面で一致する領域を絞るための補助。surveyの `sheet_quality.good_fraction` はvalidが60%以上の512²級タイルを分母に、タイル内のcrossness中央値≥.31の割合を出す別指標。作者の閾値根拠は人が判断したgood 9/bad 7のtrace。 [PRコード](originals/pr2318-face_check.py) · [固定surveyコード](originals/survey-inkcheck.py) · [作者説明](https://github.com/ScrollPrize/villa/pull/2318)
- [実測・推論] 公開 `sheet_fraction` は、採用画素数を中央CTの正値数で割ると8面中7面で小数3桁が一致。PHerc1218の2面でこの分母を識別できる。3144は `2,880,845 / 3,467,573 = .830796` で公表.831に一致し、canvas割り.708825、`rendered_px` 割り.791340は合わない。一方0846Bでは `929,456 / 4,272,489 = .217544` で通常丸め.218に対し公表.217。全件の厳密な分母・丸めや歴史的実行版を確定できるatlas生成wrapperは、固定カード・meta・既存R197で保存した公開関連木と公開コード検索の範囲で見つからなかった。8面の実測はPR式との整数一致を示す。今回の8面では分岐の5%を全画素・正値で割る場合に通過面が同じなので、atlas側の分岐分母はPRの読み取り以上には絞れない。 [測定原票](measurements.json) · [既存公開来歴の調査](../20261114-hecate-atlas-provenance01/README.md)

| R202の固定三面 | 交差マスク画素 | 全画素の割合 | CT正値数の割合 | 採用マスク |
| --- | ---: | ---: | ---: | --- |
| PHerc0175B 3024_3577_11121 | 93,040 | 2.289% | 2.556% | CT正値 3,640,421 |
| PHerc0268 2704_5907_7421 | 251,458 | 6.187% | 6.907% | 交差マスク |
| PHerc0483A 3155_3610_11128 | 627,484 | 15.439% | 17.236% | 交差マスク |

選定表で比較する場合は `mask` と分母を確認し、フォールバックは交差マスク未採用と記録する。CT正値数、交差マスクの画素数、幾何上の `rendered_px` は別々に残す。R202では異種マスクを同一の紙面割合として比較していた。R195の0125/0191/0257は同じ交差マスク分岐（.863/.159/.163）。保存Discoveryメタ名・1MiB以下・同schemaの10面に限り、フォールバックは0175Bの1面だった。高い交差マスク割合から文字の有無は分からず、.863の0125で追試ROIは見つからなかった。既知文字の0343は.714。既存の判読結果・原票は保持する。 [保存10面の独立一覧](lead-saved-meta.json) · [R195事前選定](../20261114-unreviewed-atlas-face01/selection.json) · [R202事前選定](../20261114-next-atlas-surface01/selection.json)

## 次の無料課題

入力紙面の追跡を先に調べる。0483Aの固定面 `3155_3610_11128` で、外周128pxを避けた512²・64px刻み400窓のうち、交差マスクが最も広い `[704,1024,512,512]` を診断位置に固定した。183,956/262,144画素（70.17%）が通り、最大8連結は183,888画素。原寸CTでは上半分の粒状模様と曲がる層状線、下側の弧状境界、右下の暗部があり、一つの層を連続して追えるか未確認。主担当も原寸を別に見て、262,144 CT表示値の原画一致とマスク白183,956画素を確認した。 [原寸CTと固定マスク](0483a-texture-detail.png) · [座標と選択規則](0483a-texture-detail.json) · [表示の独立確認](lead-view-check.json)

次票ではこの一面・一窓だけのmesh/renderer来歴とatlas→元CT座標をまず照合し、上側・弧状境界・下側から事前固定した少数点で同じ層を追えるか元CTの直交断面を確認する。小メタと既存資産で座標を確定し、必要なCTキーを見積もってから限定採取の可否を決める。対応が決まらない場合はそこで止める。モデル推論・幾何修正・閾値調整はこの次案に含めない。 [次案の固定位置](0483a-texture-detail.json)

## 記録と再計算

新規保存4,696,058 B（中央PNGは0268/0483Aの固定2枚、合計4,638,046 B）。原文GETのうち計測した後半4件は5.477秒。先行curlの個別時間は未計測で、curlの回数・指定上限を積算して300秒未満。GitHub読取検索とweb参照は少数、受信厳密量は未計測。PNGはR202固定treeのLFS SHAと長さに一致した。Windows CPU1/commit4GiB、OpenCV 1thread/OpenCLなし。測定12.660秒、局所図1.164秒。新CTボクセル・XYZ・重み・GPU・モデル推論・課金・公開は0。再計算は空の出力先で `tools/research/run_windows.py` に `measure.py`、次いで `inspect_texture.py` を渡す。 [取得原票](acquisition.json) · [実行原票](measure-process.json) · [局所図実行原票](texture-process.json)
