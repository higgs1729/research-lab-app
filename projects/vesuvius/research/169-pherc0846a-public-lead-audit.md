Status: resolved
担当: 研究（R169担当 2026-11-14）
Blocked by: 168

# PHerc0846Aの先行有力候補を、公開原票から次の実験へ絞れるか

## 背景と問い

2026-11-14 JST。168で同じatlasの既知文字対照は原寸で識別できた。一方、167のPHerc1218二面から追試ROIは選べなかった。闇雲に未読面を増やす前に、一次資料が強い候補とするPHerc0846Aの一組を評価する。

168保存の survey-readme.md は、固定 ketchupbyheinz/vesuvius-scroll-survey commit 1f12c1ceb14c1f24acc48249eaad60bcdf541721 のREADME。PHerc0846Aの最初の候補 (2765,2952,4205)、最も強い追試 (2601,2784,3851) を紹介する。後者は各モデル組の片面比2.6–8.9、深さ0〜+2で最大、暗いCTへの反応約0.24という留保があり、文字は読めていない。これらは上流の主張で、私達の検証済み数値ではない。

他方、164保存 atlas fixed ac5ffd7098120368216948c4e06c494bf8e67178 のindexは0846Aがpublished=0/held=29。1545もpublished=0/held=13。公開選択の差を文字/インク否定と解釈せず、何が比較できて何が不明かを確認する。

## 範囲

まず公式prizesの最新のFirst Letters対象にPHerc0846Aが残ることを確認し保存。続いて上記survey固定木から一組のreport card JSON/JPEGと、必要なら既存depth-sweepのJSONを特定する。metadata/コード/文書の本文計4MiB・最大12件、画像最大4枚/計16MiB、取得工程120秒。固定木・HEADでサイズとURLを先に保存し、版とSHA/ETagを残す。原CT/mesh/weights/新推論/新ビルド/paid/外部公開/連絡/サブ委任なし。上限や欠損で対象を無断に増やさない。固定原票が不足なら不足を結論にする。

カードの強い反応がCTの暗帯・裂けと重なるのか、独立した字画や行の位置を選べるのかを原寸で確認する。167/168の既存保存図を基準に利用可能。候補が確信できなければ転写しない。原画の画素保持・表示条件を記録し、局所的な強調や生成補完をしない。

カードで使われる尺度、深さ/方向、モデル、集計域、固定木の版、atlasとの相違について、公開原票から根拠が取れるものだけ整理する。heldの理由が無ければ未判定とする。すべての原因を推測で列挙することやモデルの大量追加を目的にしない。

結論は、独立に確かめる具体的な一つのROIまたは一つの対照実験を選ぶ根拠があるか。あるなら次段の元CT/モデル等の最小投入、取得/計算の上限、停止条件、何を判別するかを計画まで示す。無ければ一組を閉じ、残った不確実性を記す。公開画像の再表示と新しい発見・検出法を混同しない。

作業先 experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/ 、C空き10GiB、作業128MiB、図処理CPU1/メモリ4GiB/120秒/threads1の既存ランナー。制限実方式を記す。票追記・再利用入口・費用/時間・lab候補を用意し、親が別目視して登録する。

今回の委任は gpt-6.1-sol / xhigh。取得自体より、上流の有力候補と別公開系の選択の食い違いを一次資料に戻して解釈し、次に識別力のある小実験を設計する不確実性があるため選択。逐次実行を維持。

## 結論（2026-11-14 JST）

[一次・目視] 公開JPEG二枚から文字を追試するROIは採らなかった。強い追試カード `2601,2784,3851` は中央から左下の斜め帯と右上の枝分かれに黄色が偏り、複数が暗い割れや穴に接する。独立した画が続く行は一意に指せず、親の原画目視も一致した。黄色は加工した予測合成で、弱い字画やCT・生mapの対応は未確認。[追試原画](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/2601_2784_3851.jpg) · [親の独立目視](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/lead-review.json)

[推論] 次の一件は、同じ公開TIFXYZ上でseed `(2601,2784,3851)` に最近接する有効頂点を基準に、独立した128²の元CT診断を行う案。予測を見ずに位置を固定し、33層の断面で一枚の連続した紙面と暗い空隙の位置関係を確認する。カードから生mapへの正確な座標対応は未確定なので、カード上の反応を再現する実験とは位置づけない。固定メッシュ3 TIFFの目録は168,987 B。次回はメッシュ≤1 MiB・CT≤16キーかつ≤32 MiB・全本文≤34 MiB・作業128 MiB・各工程120秒・CPU1/AS4 GiB・追加クラウド0円を上限案とし、CTキー数は幾何とHEADで確定する。生mapが公に確認できれば既存反応を直接照合できるが、未確認のままでも独立の紙面診断は計画できる。[次の一案と停止条件](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/README.md#一つの条件付き識別実験)

## 根拠・詳細

[一次] 公式First Lettersの現行20件にPHerc0846A再構成 `20250728152254`。目録は9.362 µm・113 keV、別の2.403 µm再構成は指定IDと異なる。追試面の固定メタは同じ9.362 µmのsurface m7予測・L0を指す。[公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [公式目録](https://scrollprize.org/data_browser/PHerc0846A) · [固定面メタ](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/followup-mesh-meta.json)

[一次] 上流集計で両方reverse、sheet good .755/.802、片面比3.62/5.548、一貫性.500/.643、暗部率.159/.244。追試の4モデル6対の内外比2.615–8.875はsheet-check-good・`d=0` の上位3% IoU。別の44層描画を用いた3モデル・17深さの公開JSONはreading faceの `z>2` 最大0.0306がd=0、反対側最大0.0135がd=+1。こちらの再計算は公開JSONの比・タイル数・最大点の照合に限る。物理面、暗部率、IoUの生入力からの再計測は行っていない。[公開深さ](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/depth-sweep.json) · [集計値からの再計算](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/inspection.json)

[一次] 固定カードコードの黄色は、選んだ面の正規化済み2予測の平均を再正規化し、クリップとgoodマスクを掛けた合成。暗部率の上位3%交差マスクとは別。固定コードの幅式は偶数だが保存JPEGは1773×786で、正確なエクスポートと元のrows/colsは確認できなかった。別atlas固定indexのPHerc0846A公開0/held 29、PHerc1545公開0/held 13は公開選択の結果。65層・7モデル・9.6 µm共通キャンバスの別設定で、個別のheld理由や同じ面のスコアは未確認。インク陰性には数えない。[カードコード](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/report_card.py) · [固定atlas index](../experiments/vesuvius/discovery/20261113-next-target01/ink-atlas-index.json)

## 取得の経路と資源

[一次] 2026-11-13 15:18:07–15:19:43 UTC（11月14日JST）、固定木・HEAD、本文のGit blob IDとSHA、ETagを保存。資料12件532,602 B、JPEG2件696,855 B、取得工程計5.355秒。既存WindowsランナーCPU1・数値thread1・4 GiB commit上限で画素保持とJSON集計を0.190秒、最大RSS44,290,048 Bで確認。元CT・メッシュ本体・重み・推論・ビルド・有料計算0。[取得と再利用](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/README.md#取得と再利用)

## メモ

- 画像を先に主担当へ渡し、判断前に独立目視を依頼。親レビュー後、公開カードの座標が取れない場合でもseed基準の独立CT対照を選べるようにした。新規実験の実行は主担当が判断する。[lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/record.json)
