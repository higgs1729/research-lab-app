Status: resolved
担当: 研究（r235_pherc0211_edge_ct）

# 235: PHerc0211の既知行右端から同じ紙面を短く追えるか（2026-11-15）

## 依頼

- 問い: R234で選んだ公開v9二行目右端の切れた応答について、保存面の先へ同じ紙面を追う次の限定延長を行う根拠が、固定した元CT箱内にあるか。紙面が終わる/分岐して区別できない/対照の対応が不成立なら、この右端候補の局所診断を終了する。新文字やインクの確認を目的とした推論ではなく、次の新観測が可能かを調べる一回である。
- 背景: R234はrecord-e4f98902cb7cへ登録済み。親・担当が原寸生予測と元の描画CTを別目視し、右端の縦成分の上部右枝が有効範囲で切れることを確認した。反応は他者の公開済み資料であり、我々の新文字0。v6親面にも単純に続くUV支持はなく、近い3D点を別の遠方UVから繋がない。0800固定窓比較と0306B局所CT経路には戻らない。
- 固定計画: `experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/candidate-plan.json` SHA `621c238f4e49a5916ea064f89fc958b1aaaf0671c127e712069a787dbee5e7db`。同ディレクトリの `lead-plan-final-check.json` で親が承認済み。この計画を読み、版を確認してから実行する。26キー/52MiB、候補箱XYZ半開[4096,4096,8320]–[4352,4352,8576]と既知φ対照箱[3328,3200,8192]–[3712,3456,8576]を変更しない。
- 観測: 計画の候補4/既知4の固定XY断面と、候補4/既知2の局所接線・法線断面の計14断面。原始0..255と固定46..169の二表示、計28図。接線法線面はs=-80..120・d=-32..32・1voxel刻み、float64 trilinear。サンプルを保存して親の独立照合を可能にする。格子ノードXYZを使い、整数画像画素中心と混同しない。接線や描画の補助線は紙層を追跡した結果ではないと明記する。
- 実行: ダウンロードと図の生成は本票内で進めてよい。上記計画の本人再承認や親への再承認は不要。すべて同一の公式Zarr、HEAD200/2MiB/ETagをR234で確認済み。既存の取得・補間・原寸表示のコードを短く確認して再利用し、入力と出力は新フォルダへ保存。借用元の登録済みコード/原票は変更しない。取得したbodyのbytes・SHA・ETagを残し、欠損を0埋めして結論しない。
- 資源: 保存先 `experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/`。D読取のみ、C新規96MiB以内/空き2GiB以上。CT chunkだけを保存し、組み立てた3D箱はRAM内に置いて二重保存しない。CPU1、既存 `tools/research/run_windows.py` のhard process commit4GiB、予想RAMピーク1GiB未満と実測ピークを区別する。取得・描画の実行は最大15分。GPU0、クラウド台0、追加料金USD0。表面生成、モデル推論、範囲拡大、別の深さ/閾値探索をしない。
- 判定: 元の面の端から連続した紙層状の支持を、この固定箱内で追えるかを既知対照と比べる。既知対照でも紙層識別ができない場合は診断の限界として記す。連続性を確認できないことをインク不存在にしない。支持があれば後続の限定延長の具体案を一件だけ返す。曖昧なら同候補へのCT診断の連鎖を終える。結果を見て追加断面や箱を増やす救済はしない。
- 成果物: 計画の参照/実行条件、全26chunkの取得原票、14断面の元配列・28原寸図・座標と表示契約、所見、資源・費用を保存し本票へ追記。途中で原寸図と所見を親へ渡す。親は補間・表示と科学判断を独立確認する。親の確認後にmanifest/recordを凍結。lab/recall登録・次研究の選定と起票は親が行う。再委任・新規公開・外部連絡・応募送信はしない。

## 結論

[一次・2026-11-15] 候補4点はいずれも層状の帯の近くにある。元の格子点より正接線側では、近い帯が接触したり見かけ上分岐したりし、元の面と同じ一枚を固定箱内で一意に追えなかった。既知φの格子点付近では暗い間隔に縁取られた帯を比較的明瞭に見分けられた。親は担当判定を読む前に同じ14断面の両表示を別目視し、同じ判定を得た。 [担当所見](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/visual-review.json) · [親の別目視](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/lead-visual-review.json)

[推論] 事前に定めた停止条件を適用し、この右端候補への局所CT診断を終了する。限定延長の採用0、確定新文字0。公開済み応答の位置は未確定のまま残す。物理紙層の終端、異なる層への切替、インクの有無は未判定。 [凍結計画](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/candidate-plan.json)

## 根拠・詳細

| 箇所 | 観測 |
| --- | --- |
| 候補r40・r42 | XYでは格子点近くの斜走する細帯が右下へ続く。斜断面では原点から少し続く縞の境界が、正方向で近接・接触する他の帯と切り分けられない。 [r40斜断面](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/candidate-r40-sd-window.png) · [r42斜断面](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/candidate-r42-sd-window.png) |
| 候補r44・r46 | XYでは暗い間隔の縁を含む細帯群が正側で近づく。斜断面では格子点付近に層状の縞があるが、正側の密な帯から一条を選べない。 [r44 XY](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/candidate-r44-xy-window.png) · [r46斜断面](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/candidate-r46-sd-window.png) |
| 既知φ | XYの4点では格子点が弧状の帯の上か縁付近にあり、周囲の暗い間隔で輪郭が見えやすい。斜断面のr42・r46でも原点の帯と正のd側の暗い間隔を見分けられる。帯内部の細い層まで一枚として識別できるという根拠は得ていない。 [r42 XY](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/known_phi-r42-xy-window.png) · [r46斜断面](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections/known_phi-r46-sd-window.png) |

[一次] 既定のXY 8断面・接線法線6断面を保存した。XYは全655,360値のuint8原軸抽出、斜断面は全78,390値のfloat64 trilinearで全標本の8近傍が固定箱内。親は26本文と14配列を独立に照合し、XYの差0、斜断面の最大差8.53×10⁻¹⁴ DN、0–255の全表示値と窓46–169の補助線外画素の一致を確認した。補助線はv9の格子点と接線に基づく。φのXY 2枚（r40・r44）の補助線はr42・r46と同じ中心u差分で導出した。 [座標・配列・画素索引](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections-result.json) · [親の数値照合](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/lead-numeric-check.json)

[一次] 公式元CTの取得は26チャンク54,525,952 B。取得ネットワーク63.025秒、取得・初回描画・索引回復の各処理は64.657・28.573・19.485秒。担当処理の最大ピーク作業セットは52,195,328 B、親の独立数値照合は108,273,664 B。CPU 1、hard process commit 4 GiB、C新規96 MiB未満・空き2 GiB以上。追加料金USD 0。 [資源](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/resources.json) · [manifest](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/manifest.json) · [登録候補](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/record.json)

## 取得の経路

- R234で凍結した公式S3 masked L0について、R204/R226の限定読取手順を使い、保存済みHEADのURL・長さ・ETagとGETを照合した。取得本文のSHA256・MD5を記録し、R204から借りたtrilinearは戻り値の整数化を外して保存した。 [取得原票](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/ct-acquisition.json) · [入力参照](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/input-references.json)

## メモ

- 2026-11-15 [一次] R234の計画SHA256と親承認が一致。保存済みL0メタデータはZYX、uint8、無圧縮128³、C順。R226が借りたR204の取得・描画の前例を確認し、今回の固定26キーと断面に適用する。
- 2026-11-15 [一次] 全26 GETの前計画ETag・本文MD5と長さが一致し、54,525,952 Bを保存。14断面の元配列と28原寸図を作成した。初回の索引JSONにNumPy整数の変換漏れがあったため、ログと部分索引を保持し、既存42出力の全値・画素照合後に索引を正常保存。親には判定より先に断面索引を共有。 [取得原票](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/ct-acquisition.json) · [断面索引](../experiments/vesuvius/discovery/20261115-pherc0211-right-edge-ct01/sections-result.json)
