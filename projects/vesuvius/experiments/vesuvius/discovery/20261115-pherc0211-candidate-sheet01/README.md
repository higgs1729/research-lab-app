# R240: 固定候補の紙面と公開来歴

候補 parent XYWH `[4416,2048,384,256]` は、**局所CT支持のある未確認反応として保留**する。固定した3点とも幾何原点付近に紙様の層状帯が見えるが、q25/q50、特にq50のu-n断面は密集・接触があり、同じ細かい紙層をROI全体で追えているとは確認できない。q75は比較的明瞭な局所帯を持つ。既知φ対照も曲率・近接層を含み、直線接線面が全幅にわたり曲面を追うとは扱わない。インク・読字・新規性の確認はなく、新文字0。

研究票は `research/240-pherc0211-candidate-sheet-and-provenance.md`。R236–239の入力・判定・凍結資料は変更していない。R236–238のbit-exact不成立とR236の旧pairgate不合格は残る。本研究はモデル推論や近似render改善ではなく、R239で選んだ一候補の有限な構造・来歴確認である。

## 固定観測と結果

候補3点 `[4512,2176]`, `[4608,2176]`, `[4704,2176]` と、公開既知φの3点 `[4784,3270]`, `[4864,3270]`, `[4944,3270]` を、CT値を見る前に各ROIの相対1/4・1/2・3/4、縦中央へ固定した。旧R236の幾何による局所原点と法線を使い、各点のu-n/v-n断面を原CTから採取した。これらは反応の画線を選び出した点ではない。

- 12断面、各193×65、計150,540値。s ±96 vox、n ±32 vox、1 vox刻み。元CTは9.362 µm/voxel。
- R235/R204の既存float64 trilinearを使用し、未丸め値をNPYで保存。新しい描画面・モデル入力は作らない。
- 24枚の原寸PNG。無注記raw 0–255 DNと、事前固定46–169 DNの表示。固定窓には幾何の原点・軸マーカーのみ。拡大・断面追加・表示選び直しなし。
- 25 CTキーの24個は既存本文を直接再利用。新規はknown側 `0/65/26/29` だけ、2,097,152 B。全SHA、ETag/MD5を確認。
- 主担当が別の8corner重み和・一次元CT byte offsetで全値を検算し、最大差 `8.526512829121202e-14 DN`。24図の全画素とマーカーが一致。`lead-section-check.json`。

図・配列とhashは `sections-result.json`、図は `sections/{candidate,known_phi}-q{25,50,75}-{un,vn}-{raw,window}.png`。生値全体の範囲は3.3297209684289886〜255.00000000000003 DN。数値整合は紙層・文字の証明ではない。

## 初回停止を保持した修正

初回 `observe_ct.py` は、計画にない厳密な0–255端点assertを追加したため、5番目のcandidate-q75-unで停止した。全12面のshape/dtype/finiteを個別診断し、5値だけが255を `2.842170943040401e-14 DN` 超えていた。5値とも元8cornerは全て255で、float64重み和の丸めに由来する。初回の「最初の面」という報告は保存済み4面の確認後に訂正した。

親の診断・修正許可の下で、未計画の端点assertだけを除き、原計画どおり有限float64値をそのまま保存した。入力・位置・補間式・図のclip/round・モデル基準は変更していない。初回コード/失敗receipt/診断全値/差分を残し、取得済み1keyを再使用。初回4面のNPYとPNGは全値照合して上書きせず、残り8面を保存した。`resume-correction.json` / `resume-diff.patch` / `observation-process.json` / `observation-resume-process.json`。

## 独立目視と来歴

担当は24原寸を実見して `researcher-ct-visual-review.json` へ保存し、その後に主担当の `lead-section-visual-review.json` を読んだ。所見は一致し、局所紙様帯の支持、q50の密集・接触による限界、全ROIの同一細層未確認を保持した。反応の横接続/下降部が繊維・割れ・層接触のどれに対応するかも決まらない。`joint-decision.json` に照合結果を記録する。

一次資料照合は `provenance.md` と `sources/mesh__*.json`、原ZIP参照に保存。v6 parent/resultsは旧Studio checkpointによる全親4600×6060推論の履歴を含む。現在の公開line2 soft-loss再現記録とは別で、記録にある旧全親確率本文は未入手。候補がline2 crop外、別手動版v9のXYZ範囲外にあることは新規性の根拠にしない。公式記事の原HTML/4図と、固定commitの著者crop1711比較JPEGを確認したが、候補への正確な登録は未解決。著者の非公開先行作業も未確認。

次の一手として、旧全親確率原本の公開所在と座標対応を一度確認する来歴調査を提案する。入手できれば同じ固定ROIへ登録するが、旧model差を保持し、反応の既往と読字の既往を区別する。所在が不明なら未確認のまま止める。これは別票の候補案であり、R240では追加の検索・取得・計算を開始しない。

## 資源・証拠

CPU1、各実行hard process commit4 GiB、C空き2 GiB以上。追加観測総保存上限64 MiBに対し約4.6 MB。新CT2 MiB、公開JPEG544,889 B、既存CT48 MiBは複製なし。初回実行9.374秒、修正再開6.914秒。計画・診断・検証等を含むreceipt別内訳は `resources.json`。GPU/モデルforward/Pod/追加料金は全て0。D書込み/Git操作なし。

主担当の `lead-plan-geometry-check.json`、`lead-observation-clearance.json`、`lead-section-check.json` と独立所見を含め、`manifest.json` に本ディレクトリの全ファイル（manifest自身以外）・研究票・外部原資料/既存CT/検証receiptのhashを固定する。`record.json` は主担当の登録用で、担当はlab/recall登録・外部連絡・公開・応募を行わない。
