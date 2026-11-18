Status: resolved
担当: 研究（R221、2026-11-15 JST）
Blocked by: 220

# PHerc0813の未精査の広い公開予測から、元データで追試できる字画候補を選べるか（2026-11-15）

## 依頼

本人の主目標は未読文字の発見。220はPHerc0800公式面4の別窓1024²・両順1,688パッチを手元GPUで194.031秒で検査し、担当と主担当の原寸判断とも追試ROI0で固定窓を閉じた。登録 record-cc49cadee0b1、追加クラウド費0、資源解放済み。閉じた窓のモデル設定を増やすより、未精査の観測範囲を見つける。研究は一件ずつ、監査inbox未決0。

220の候補に残ったPHerc0813公開atlas `z14304_w100` は作者公表の支持約853万画素、`aprova` とされるが、物理紙面の正しさやインクの感度を保証しない。`z14896_w080` は別候補。両方の固定HF treeが220にあり、seed42/seed43/soup42の両順の原寸TIFFは存在する。作者の数値inkゲートは両方不通過、Hecateは集計のみで原図を確認していない。R188で閉じた `z12496_w020` とは別IDだが、物理重なりは未確認。既知対照でも旧ゲートが不安定だった履歴があるので、数値ゲート不通過だけで原寸を見る前に棄却しない。公開済み予測の観察は他者の計算を利用するもので、自分のモデル成果とは扱わない。

問いは、広い未精査公開面の原寸予測を直接確認すると、元CTへ戻して追試する価値のある字画・行・まとまりを一つでも選べるか。まず来歴と既検査範囲を小さく照合し、z14304_w100を第一候補に固定する。重大な重複や別の合理的な理由があれば、取得前に代替の具体的範囲を親へ示す。候補比較だけで研究を終えず、選んだ一面の原寸確認と判断までこの票で行う。

公開ファイルの型・寸法・バイト数・SHAを小メタで先に確かめ、必要な原寸像と表示法を固定する。例えばseed43両順と同じcanvasのCT中央像、必要なら公開別モデル両順が材料になるが、既存道具に合うからという理由だけで六画像全部を新規取得する必要はない。広い一面を欠落なく見るための原寸切出しは既存188/192/195/202の実装を借りられる。縮小全景は位置把握に使い、字画を判定する部分は原寸を示す。元0..255、マスク、回転、コントラスト調整は区別し、変更が有用なら元図との対応と方法を残す。既存数値スコアの再開発はしない。

新規通信は予測・メタ/必要な元CT中央の公開画像を合計64MiB/600秒以内の目安、Cの追加1GiB以内・空き10GiB、CPU1/commit4GiBで既存画像処理。大きなsurface tar、元3D CT、学習重み、新ビルド、モデルforward、GPU、有料資源、外部への公開・メッセージ・応募は現段階で不要。文字らしい具体ROIを親も独立に採用した場合は、この同じ研究内で限定的な元データ照合と次の一回の検査を具体化する。何も選べなければその面・公開モデル群の確認を閉じ、インク不存在や巻全体へ一般化しない。

重要なのは、単独の明斑や線が並ぶ繊維を文字と断言せず、同時に未校正の必須ゲートで弱い候補を機械的に捨てないこと。具体的な位置、輪郭、線幅、隣接構造、CT対応、モデル依存性の観察と限界を示す。親の独立判定を先に保存できるよう、画像ができたら自分の結論を送る前に原図・表示原票のパスを連絡する。

原出典は220の固定atlas manifest/tree/HF SHA、R188の生成条件と方向訂正を入口として再確認する。対象資格と既受賞状況は当日の公式ページを必要箇所だけ一次で確かめる。過去の原票を上書きせず、今回取得原票と引用は自分で確認した本文へ結び付ける。

保存先 `experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/`、C書込/D読取のみ。研究票に結果を追記し、コード・来歴・原図・原寸一覧・独立検証・費用0・manifest・record候補を残す。lab登録は親。再委任なし、次研究を同時に進めない。

担当モデルはgpt-6.1-sol / highを今回明示選択する。公開原寸の固定取得・表示・支持域確認は既存188等に実証済み手順があり、今回は広い別の面への適用と目視判断が中心だからである。

## 結論

2026-11-15 JST。[一次・目視] PHerc0813 `z14304_w100` の公開seed43両順を担当と主担当が全域で別々に確認し、元CTへ移す字画・まとまりのROIはともに0件。太い湾曲、鉤、開いた輪状反応を原寸で比較した。強い方向で見ても輪郭・線幅が続かず、周りの明部と混ざっていた。両方向に残る周期的な筋は予測の段状境界に沿っていた。数値ゲートや字列の必須条件は設けなかった。この面のseed43公開両順の精査を終了する。元CT中央層、他checkpoint、物理紙層、巻全体のインクは未検証。 [原寸図一覧](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/README.md) · [担当の原寸判断](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/visual-review.json) · [主担当の別判断](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/lead-visual-review.json)

## 根拠・詳細

- [一次・実測] 固定TIFFは両順とも12352×1920のuint8。原寸は両順65対、中心960×432以下に32px周辺付き。担当・主担当とも非ゼロを含む50対を原寸で見て、15対は全ゼロを数値確認した。主担当は入力16ファイルと中心47,431,680値、周辺付き57,098,240表示値を別検算した。マスクは12340×1860の採点用画像で9,008,610画素。作者manifestの `valid_px` 8,530,433とは別値。表示にはマスクを適用していない。 [取得原票](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/acquisition.json) · [主担当の入力照合](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/lead-source-check.json) · [表示の別照合](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/lead-panel-check.json)
- [一次・目視] `[9148,988,9385,1220)` のforwardの輪状反応は左下が開き、下端は隣へ拡散。reverseでは明部がずれる。`[3950,1030,4290,1260)` のforwardの鉤は太い斜帯に入り、終端が分かれない。`[8160,508,8670,650)` の筋は両順の上縁で反復し、左上位置合わせでは全域が作者マスク外。座標は左上原点の半開区間。CT対応では三例とも未照合。 [観察座標とマスク位置](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/review01/observations/coordinates.json)
- [一次・実測] 作者指定のmesh `0c966f8f11f92cffb09dbc6320a706161405ad0b` の有効節点とR188 `z12496_w020` の有効節点のZ箱は1,011.9668 voxel離隔。元画像の独立CT中央配布は固定treeで見つからず、同面の380,538,880 Bのsurface tarは取得していない。 [XYZ照合](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/mesh-overlap.json) · [固定面tree](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/originals/atlas-segment-tree.json)
- [一次] 公式First Letters対象再構成にPHerc0813 `20250821151723` がある。公式Winners掲載本文で同巻は見当たらなかった。公式データは9.362 µm、113 keV、scan `20250720160015`。 [公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [公式データ](https://scrollprize.org/data_browser/PHerc0813) · [公式Winners](https://scrollprize.org/winners)

## 取得の経路

Carson Rodriguesの公開atlas `33b4fc81f13a32332b179bf8c34f42ec3cfe7589` のカードとinfer原票から、forwardは接尾辞なし、reverseは `_reverse` と確認した。R188の別配布の順逆訂正はこのatlasへ適用していない。R220の固定HF treeで二予測のLFS SHA-256とマスクのGit blob SHA-1を取得前に固定した。XYZ節点は固定GitHub treeとGit blob SHA-1を照合。HTTP本体は合計16,080,613 B。主担当の最初の入力検証ではマスクのpadded寸法を仮定して失敗し、原寸を保持して左上に置いた比較へ訂正した。新規CT・推論・GPU・有料計算・外部提出は0。 [固定公開カード](https://huggingface.co/datasets/rodriguescarson/eligible-scroll-atlas-renders/blob/33b4fc81f13a32332b179bf8c34f42ec3cfe7589/README.md) · [計画・SHA](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/acquisition-plan.json) · [資源記録](../experiments/vesuvius/discovery/20261115-pherc0813-wide-public-review01/resources.json)

## メモ

220の登録と資源解放後に着手する。前回の独立確認は親の全入力/出力照合と別原寸判断で完了した。受賞候補は既存三件のまま、新文字・応募送信なし。

2026-11-15 JST。R220登録済み、未決inbox 0、R188の控えを確認。atlas固定カードとinfer原票から、当atlasのforwardは接尾辞なし、reverseは `_reverse`、原寸予測canvasは12352×1920、元surfaceは12340×1860と確認。R188の別作者配布に適用した方向ラベルの訂正はここへ移さない。対象の同面公開CTは380,538,880 Bのsurface tarに収められ、外側treeには独立の中央CT画像がない。元meshの作者指定revは `0c966f8f11f92cffb09dbc6320a706161405ad0b`。

担当は原寸50対を見て2026-11-15T06:16:46Zに観察を保存。主担当は別判定を06:18:12Zに保存。両者の判断は保存後に共有した。双方が追試ROIを0件としたため、別の公開checkpointと元CTの追加取得は行わなかった。
