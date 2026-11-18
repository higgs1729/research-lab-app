Status: resolved
担当: 研究（R211担当、2026-11-14 JST）
Blocked by: 210

# 固定された行形状の順位は、既知文字行を明度順より少ない確認枠へ拾えるか（2026-11-14）

## 依頼

210をlab record-910f8bbe2247に登録済み。受賞0306Bの広域探索と現在の小窓中心の差から、既存全面予測を変えず行構造で候補を順位付けする一試験を選んだ。実行条件は experiments/vesuvius/discovery/20261114-winning-method-gap01/next-plan.json と next-inputs.json で固定され、親のlead-plan-review.jsonに事前SHA照合と採用判断がある。この一件を実装・実行し、成否を判定する。

主要な問いは同じ行候補集合で、幾何スコア順が候補のzmean順より既知主行を上位へ拾えるか。全条件・入力・36方位・上位3・既知箱の対応・停止基準は210の計画をそのまま使う。0343全6048×2304のreverseを露出済み既知対照、0125/0175B全体の両順をストレス例（真の陰性ではない）とする。新しい巻物/窓/深さ/重みを足して結果を救済しない。

不足するReader v2逆の固定PNG一枚2,084,949 Bだけを90秒内で取得し、固定LFS SHA/寸法を照合する。既存12 PNGは210で親が全hash照合済み。PNGのuint8はfloat32/255として確率値へ戻してから、固定二モデルz→等重み平均→再zを適用する。CT>0を明示的な統計・描画支持近似とし、外周48pxを除外。品質mask未測定・物理紙面未確定・量子化PNGを使うという制限を保持する。

固定306b-line_find.pyを読取importしてrun_mapを呼ぶ。glyph=None、ct=None、全ケース共通[-90,90)5度刻み、元の幾何条件を変えない。明示マスクを渡し、load_mapのz!=0を物理面判定として追加しない。二順位は同一候補・同一固定検出順をタイブレークとする。作者の校正済みスコア閾値・偽陽性率や1/191再現を主張しない。元laneの9.6µm既定Hecate+TRACEではなく、8.64µm二モデル融合を借りた適用試験と明記する。

既知箱は179のraw端×.9から位置を作り、13箱・5箱の各行軸を検出前に固定。親の別計算 lead-next-reference.json と照合する。候補polygonが同じ行の箱中心4以上/他行1以下、無向主軸差15度以内なら対応。主行の幾何順位がtop3かつzmean順位より上なら数値端点を通過し、原図の字画を別目視する。等位/悪化/未検出はそのまま結果とし、条件調整を行わない。

各順位上位3の和集合を、rank名を隠して事前固定seed=20261114の順で確認する。CTと二モデルの0–255原図を同じ条件で表示し、必要な場所はnative pixel表示に戻れるよう座標と元画像を添える。長い行は全体位置と原寸部分を区別し、縮小overviewだけを原寸目視と呼ばない。主担当へ重要な図と位置を早めに共有する。対照の既知字画もストレス例の見慣れた模様も隠せないため、順位名を隠す比較以上の盲検とは主張しない。

実行は既存tools/research/run_windows.py、CPU1/commit4GiB/計算合計300秒/作業512MiB、一面一向きずつ。新CT・重み・モデルforward・GPU・追加課金0。原処理は一回だけ、失敗時は原票を保持し、実装不備の修正と科学条件の変更を区別する。検査のために同じ行検出を全部もう一回流さない。親は保存出力・固定入力・順位と既知座標から独立照合する。

保存先 experiments/vesuvius/discovery/20261114-line-priority-trial01/。コード・入力参照/出力/原寸確認・実測資源・主張の限界をこの票へ追記し、README/manifest/record候補を残す。結果が陰性でもink不存在とせず、元CTへの投資へ進める根拠が得られたかで判断する。新たな文字の可能性はローカル保持。登録は主担当、逐次、再委任なし。

今回の担当は明示的に gpt-6.1-sol / xhigh。事前計画は固まったが、既存検出器を初めて別入力契約とWindows上で組み合わせ、既知座標・不完全な支持マスク・数値順位を保つ実装と解釈が必要なため。道具は再利用し、追加の一般基盤を作らない。

## 結論

行形状順は事前の改善条件を満たさなかった。PHerc0343の既知主行は幾何・zmeanとも1位で、同じ候補が13箱中心を含んだ。下段は幾何3位・zmean2位。主行には原画像で分かれた対応字画があった。0125/0175Bは各順につき候補2件で、上位3件に入る集合は同じ。順位名を伏せて原画像を確認したが、追試する字画や行のROIは選べなかった。この固定条件の順位による追加CT投資は見送り、インクの有無は未判定。 [全体結果](../experiments/vesuvius/discovery/20261114-line-priority-trial01/README.md) · [既知の順位](../experiments/vesuvius/discovery/20261114-line-priority-trial01/ranks/PHerc0343-reverse.json)

## 根拠・詳細

- [一次、2026-11-14] 13 PNGをSHA照合し、固定5面向きを各一回検出。0343の主行候補は他行の箱中心0、行軸差1.9023°。下段候補は5箱中心・他行0、軸差12.9684°。0125の逆順のみ二候補が順位を交換。元検出indexを二順位に共通で使用した。既知面は曝露済み位置対照で、ストレス例に真の陰性ラベルはない。 [実行原票](../experiments/vesuvius/discovery/20261114-line-priority-trial01/execution.json) · [実装契約](../experiments/vesuvius/discovery/20261114-line-priority-trial01/implementation-contract.md)
- [一次、2026-11-14] 担当は上位集合12件の縮小全体図と原寸13タイルを順位開示前に目視。既知主行は曲線や縦画の並びを部分原寸で確認。0125は丸い塊、0175Bは暗い空隙と繊維に沿う明部があり、二予測で共通する字画列を選べなかった。面自体は既視で、伏せた情報は順位名。親は順位を知った状態で8全体図・6原寸を別目視し、追加ROIなし。親の別実装で全13候補の得点・順位・箱対応と端点を確認し、検出器の反復は0。 [担当目視](../experiments/vesuvius/discovery/20261114-line-priority-trial01/visual-review.json) · [親の別目視](../experiments/vesuvius/discovery/20261114-line-priority-trial01/lead-visual-review.json) · [独立検算](../experiments/vesuvius/discovery/20261114-line-priority-trial01/lead-numeric-check.json)
- 新規1 PNG 2,084,949 B、取得2.512秒、CPU処理22.616秒、最大RSS365,211,648 B。CPU1・commit4 GiB。新CT、重み、モデルforward、GPU、課金、外部公開0。 [取得](../experiments/vesuvius/discovery/20261114-line-priority-trial01/acquisition.json) · [単回の処理ログ](../experiments/vesuvius/discovery/20261114-line-priority-trial01/run-process.json)
