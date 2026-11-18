Status: resolved
担当: 研究（r234_pherc0211_context / Astra xhigh / 2026-11-15）

# 234: PHerc0211の受賞文字の周囲に、低費用で追試できる未確定の字画を選べるか（2026-11-15）

## 依頼

- 問い: PHerc0211の公開された受賞資料と同じ紙面の文脈から、既知文字を対照として、まだ確定していない隣接字画を調べる具体的な一件を選べるか。選べない場合は、何が足りないかを明確にし、この経路を閉じる。モデルを替えて既済の窓を繰り返すのではなく、文字が確認された場所の周囲を選ぶ介入である。
- 背景: R233はrecord-b8156e1cea1fへ登録済み。0800固定窓はHecate/Reader/Studioの比較でROI0、当該窓のモデル比較を終了した。PHerc0306Bの未確定候補の局所CT診断もR228で終了しており、ここへ戻らない。新文字0、公開済み改善三件、11月まとめ応募方針は維持。PHerc0211は11月15日に他者のFirst Letters受賞が発表済みで、未受賞巻とは扱わない。
- 欲しい形: 公開原文/資料の来歴、受賞文字・公開ラベル/公開予測の範囲、面ID/元CT/XY座標/表示方向/深さの対応を必要な範囲で確認し、原寸で追試候補を選ぶか、選べないと結論する。既知範囲と未確定範囲を混同しない。公開予測の新しい見方だけで自分たちの新発見としない。候補が出れば、次に何を観測すれば支持/棄却できるか、取得量・計算量・費用の具体案を一件示す。
- 材料の例: 公式発表 https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211 とリンク先の受賞者の公開資料。モデル作者 https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt の現行READMEは、提出用mesh ZIP内に画像生成コード/CT背景/カラーマップがあると記す。取得経路は限定しない。既存R229 sources/award.html・固定コードと記録を再利用できる。R232/R233でモデル実行は検証済みなので、この研究ではもう一度既知モデルの成立確認を繰り返さない。
- 資源: 初期調査は公開本文・メタ・小さな図/配列に限定し、追加計算料金0、GPU0、D読取のみ、C新規保存64MiB以内・空き2GiB以上。大きなZIP等はメタデータ/サイズを先に調べ、必要な部分だけが正規の経路で取得できるかを確かめる。範囲取得等を使う場合は全体の完全取得と区別する。64MiBを超える取得が必要なら主担当へ実量/必要性/代替を先に報告する。未知の大規模データ/訓練/面生成/有料実行はここではしない。
- 成果物: experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/ に取得原票、URL/日時/bytes/SHA、原寸の必要図、座標と変換、選定判断を保存し、本票へ結論を追記する。主担当が重要原文/図/座標を別確認するまで最終manifestを凍結しない。上流原文を自分で取得したものを一次とし、作者の自己評価と独立検証を区別する。
- 進め方: この一件だけ。新規公開/応募/連絡はしない。台は起動しない。再委任・次研究の実行・lab登録・recall追加は主担当が行う。最初に小さい資料から有望性を確かめ、次々と別資料を大量収集して研究の目的を広げない。所見と残る問いを途中にも報告し、重要な座標/図の検証可能性を優先する。

## 結論

**一件を選べた。受賞済みの二行目右端で、面の境界に上部右枝を切られた湾曲する縦成分を、既知のφを対照に追試候補とする。** これは受賞者が既に公開した未確定応答であり、我々の新発見ではない。新文字0、新規推論0。次に判定するのは、固定した元CTの小領域内で同じ紙面が境界外へ続くか、欠損・分岐によって続きが決められないかの一件である。主担当が原文・原寸・座標・取得量を別確認し、この有限観測案を採用した。

候補は `PHerc0211-crop1711-lines123-manual-20261028-1316-legacyuv20-v9` の原寸XYWH `[5820,800,160,160]`、文脈表示は `[5600,680,420,480]`。対照φは同面 `[4640,780,320,300]`。右端の形を単独で文字名に結び付けない。公開済み予測の表示変更を新発見に数えず、受賞記事の緑枠外を未公開・未読範囲とも扱わない。

次案はCT26 chunk / **54,525,952 bytes（52 MiB）**、CPU1・追加料金US$0・GPU0。8枚の固定XY断面と6枚の固定接線/法線断面を、二つの固定表示で観測する。今回のCT本文取得は0。面の継続が判別できなければ箱拡大・追加モデル・局所CT診断の反復へ進まず、この候補を閉じる。成功しても、後続の限定的な面延長へ進む根拠に留め、文字の確認とはしない。

## 根拠・詳細

### 公開範囲と来歴

- [一次資料、2026-11-15再確認] [公式受賞発表](https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211)は、四cmの範囲に11字を認めた他者の受賞を報告する。37提出・15参加者/チームで同じ付近の重複提出がある。保存原文はR229の `sources/award.html`、SHA `45346fbb05600bda2df15ce1b9d35d00fa27ec558c5e73e54ae2eb4513a2f3ce` を再利用。主担当が記事4図の元画像を直接取得し、既知範囲外にも既出応答があることを実見した。[独立記事確認](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/lead-article-review.json)
- [一次、2026-11-15取得] 記事の[公開Driveフォルダ](https://drive.google.com/drive/folders/1bvKolL_TIE3k5Ixi1qlOiAmofQ6r2ocH)に、v9三行面、v6単行面/親面、CT背景、全確率、入力、生成コードがある。v9 ZIP 9,264,958 B、v6 ZIP 4,953,331 B、v9確率38,709,184 Bを完全取得した。HTTP範囲取得ではない。大きい入力NPY 167,596,928 B・58,176,128 Bは取得していない。v9は一部だけ展開し、v6はZIP内を直接読んだ。[取得原票](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/acquisitions.jsonl)
- [一次、同日] v9確率のファイルSHA `527c6fbbc5ac2d5a81d7cfb7ccc2925f2dc4b4d74627a0e7b08200d6874f071c` と全画素SHA `4c0249cd8ee5258450278e63f8d086c4698b9ebc2b8a43cb0034c94573d693c6` は作者の `reproduction.json` と一致。v9 36件、v6 38件のZIP内support SHAも一致する。作者の履歴 `results.json` の値域等は現行配布確率と異なるので、実取得と `reproduction.json` を基準にした。現行確率maxは0.9474670291。これは推論やGPU再現の独立検証ではない。[実取得検査](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/source-check.json)
- [一次/限界、同日] ZIPの `labels.json` は「row 1」等の表示用文字画像を指し、インクの正解マスクではない。作者の固定READMEはPHerc0211の既存9評価セグメントと、当時のunlabeled stitched cropを区別するが、後のv9全域が未ラベル/未読である証拠にはならない。今回選んだ成分は、確認した受賞資料では確定した文字名が付かない**既出応答**という扱いに限定する。

### 面・座標・表示・深さ

| 対象 | 確認した対応 |
| --- | --- |
| v9三行面 | 6020×1740画素、normalized tifxyz 87×301、scale `[0.05,0.05]`、9.362 µm/voxel |
| 元CT | `PHerc0211/volumes/20250821151803-9.362um-1.2m-113keV-masked.zarr`、L0 ZYX shape `[19416,7948,7948]`、非圧縮uint8、128³ chunk |
| 表示方向 | 原確率・CT背景と同じXY、回転/反転なし。投稿画像の下端220画素はスケール用余白。quarter overviewはXY各1/4で、原寸cropに拡大処理なし |
| v9端アンカー | grid row42/col298 のXYZ `[4210.22509765625,4210.63916015625,8398.435546875]` |
| φアンカー | grid row45/col240 のXYZ `[3516.6298828125,3347.90625,8367.599609375]` |
| 画像座標との区別 | `(20c,20r)`は連続キャンバスの格子位置。整数画素中心のXYZと同一とはしない。記事図からv9への厳密な画像登録も主張しない |
| 公開深さ契約 | 31層-15..+15の23..8を入力順に使用、作者規約で+8..-7。背景は14..17の最大値。normal_sign=-1は継承値、`physical_face_verified:false`。今回renderer再実行なし |

[一次計算、2026-11-15] v6のfull parentは230×303。v9端に近いv6点は概ねcol299–301の同じ右端側にあり、maskを外すだけで十分な右方向支持が現れるとは認められない。直線接線に沿って外へ40 voxel等進めた位置の全v6最近傍はcol90–93付近の遠いUVへ移る。3Dの近さを同じ紙面の接続とみなせない。これは外側の紙面が存在しない証明でも、面延長の実行でもない。[座標原票](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/geometry-inspection.json)

[原寸所見/推論、同日] φ右隣・上行・二行目右端を生0..1確率、CT、公開方式カラーで実見した。内部の強い応答を表示し直すだけでは新しい判定が増えない。一方、右端の湾曲する縦成分は、その上部右枝の先が保存面の支持外にあり、紙面の継続という新しい観測対象を限定できるため、一件だけ採用した。[原寸図](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/review/row2-right-edge-turbo-native.png)・[生確率図](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/review/row2-right-edge-probability01-native.png)・[親の独立所見](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/lead-visual-review.json)

### 一件の次観測

[一次HEAD/計画、2026-11-15] 候補のCT箱XYZ半開 `[4096,4096,8320]`–`[4352,4352,8576]` は8 chunk/16 MiB。既知φの対照箱 `[3328,3200,8192]`–`[3712,3456,8576]` は18 chunk/36 MiB。26件全てHEAD200、各2,097,152 B。全キー・ETag・時刻を保存し、本文は取っていない。

- 候補はgrid r40/42/44/46,c298、対照は同r,c240を原CTへ直接対応。XY断面のZは候補8359/8398/8438/8478、対照8269/8309/8348/8387の8枚。
- さらに候補4点と対照r42/r46の計6点で、局所u接線tと `du×dv` の単位法線nによる観察平面を固定。接線距離-80..120、法線距離-32..32、1 voxel刻み、201×65標本、float64 trilinear。候補端は後退u差分、対照は中央u差分、vはいずれも中央差分。面の生成や成長ではない。
- 14断面をnative0..255と固定46..169の二表示、計28図にする。サンプリング8角が固定箱外なら欠測とし、箱を広げない。主担当は最終計画の全点/全8角が箱内であることも別計算で確認した。
- CPU1、予想ピークRAM1 GiB未満、実制御は既存 `tools/research/run_windows.py` のprocess commit 4 GiB、ピーク実測記録、15分、C新規96 MiB/空き2 GiB。CT chunkだけ保存し箱配列を二重保存しない。追加料金US$0、GPU0。R234では未実行で、次票の実施判断/実行は主担当が行う。
- 支持: 既知対照の座標対応が成立し、候補端の同じ紙面を固定箱内で追える。主張は限定的延長を検討できることまで。棄却/停止: 紙面が欠ける、複数の続きが区別できない、既知対照が不成立。追加箱・別モデル・同種診断の反復で救済しない。

[最終計画](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/candidate-plan.json) SHA `621c238f4e49a5916ea064f89fc958b1aaaf0671c127e712069a787dbee5e7db`。親の[最終独立確認](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/lead-plan-final-check.json)を受けて凍結した。

## 取得の経路

Google Drive pluginのlist/fetchで公開フォルダとREADMEを確認。ZIPのfetchはTransport closedだったため、サイズ確認済みの公開 `drive.google.com/uc?export=download&id=...` を直接HTTPで取得した。READMEはpluginが返したauthenticated file_uriのraw bytesを取得し、期限付きURLは保存原票から除いた。ZIPのコードは読んだだけで実行せず、確率・CTを保存した独自の非生成的検査コードで表示した。Windows Python既定cp932でUTF-8本文の入出力に一度失敗し、以後 `-X utf8` を用いた。範囲取得・入力NPY取得・学習・GPU・新面生成・新規公開・外部連絡なし。

[成果物の案内](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/README.md)・[manifest](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/manifest.json)・[登録候補](../experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/record.json)。lab登録とrecall追加は主担当が担当する。

## 本人への質問

なし。候補一件と次の有限観測案は主担当の判断範囲で採用済み。新文字0、公開済み三改善、11月まとめ応募方針を維持する。

## メモ

- 2026-11-15 着手。共通CONTEXT/instruction-triage、AGENTS、system/lead、researchスキル、README・構成を確認。作業名 `r234_pherc0211_context`。追加計算料金0・GPU0・D読取のみ・C新規64MiB以内。最終manifestは親確認後。開始時C空き9,164,251,136 bytes。
- 既知範囲の外を未公開と推定しない。親より公式Drive出力folderの既存取得リンクと、37提出15team・他提出との同領域重複への注意を受領。
- Drive本文/小メタから開始。三行面のZIPを全取得した後、原寸候補選定のため公開float32確率を取得。入力NPYや全ZIP展開を避け、初期64 MiB枠内に維持。親は記事4図の直接取得と原寸・全画素・36support SHA・v6総当たり最近傍・CTキー/箱・最終観察座標を独立確認した。
- 二行目右端を一件選定。親の要請により固定XY8枚へ局所接線/法線6枚を追加し、予想RAMと既存runnerの4 GiB実制御を区別。最終計画SHAの親承認後、候補計画へ追加せず記録を凍結。R235の起票/実行は担当範囲外。
