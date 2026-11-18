Status: resolved
担当: 研究（2026-11-13）
Blocked by: 136

# R013: 固定モデルを未学習・未読候補へ小さく試せる公開入力はあるか（2026-11-13）

## 依頼

主担当は既存三件の深掘りと、既知w035の元CT→描画→公式CPUインク候補の工程確認を終えつつある。今後の主軸を解読に置くか改善の深掘りに置くかは本人に質問中で、まだ本人の採用決定とは扱わない。この票では、次の低支出の探索試験を具体的に比較できるよう、公開入力の成立性だけを一件調べる。未読巻物の長期研究・有料計算・First Letters応募を開始する依頼ではない。

固定した公式9µmモデルは四つの巻物（PHerc0139、Scroll1667、PHerc Paris4、PHerc0814）の注釈で訓練されている。候補はこれと異なる巻物を優先し、公式にまだFirst Letters対象として列挙されるか、既読状況の一次資料、表面とCTの公開状態を分けて確認する。『ネットに発見がない』だけを未読・受賞可能の証明としない。最新の公式規定と既存受賞状況は主催側の原文で確認し、公開予測画像があることと判読・受賞済みであることを区別する。

有力候補は最大3件で十分。各候補について、正式な巻物ID/scan/segment、原CTとTIFXYZまたは表面Zarrの対応・解像度・軸・深さと法線の情報、必要な小領域の取得単位、公式モデルをそのまま使えるかの不足、データの利用条件と新発見の公開制約を、一次原文URLと取得日時付きで示す。1件を次の小試験向けに推奨できれば、理由と最小の確認事項・転送量/CPU案を添える。成立しなければ『候補なし』と具体的な不足を返す。候補数を埋めるために条件を緩めない。

既存資料の入口は `research/127-r011-readable-fixture.md`、133/134、135/136、保存済み公式モデルカードやS3一覧。`D:/kensyoukin-work/r003-villa` の固定ソース・ローカルGit objectも読取可能。公式9µmインク推論のCPU手順は `experiments/vesuvius/r012/20261113-known-ink-inference01/README.md`。ここではそれを再実行しない。PHerc0343等でchunk metadataの見積と実bodyが大きく違った既存記録があるので、本文を取得する前に既存情報と公開サイズを確認する。

調査は一次ページとメタデータ・一覧・HEAD程度に限定し、新規取得本文の目安5MiB以内。CTチャンク・画像・モデル・メッシュ本体の取得、推論、学習、コード修正、依存導入・有料計算・GPUは行わない。特定の不明点のために範囲を越える必要があれば親へ具体案を返す。新規出力は `experiments/vesuvius/r013/20261113-unread-input-feasibility01/` と本票。C:出力、D:読取のみ。外部連絡・応募・公開repo変更・追加subagent禁止。一件逐次で136完了後に着手。

モデル/effortはgpt-6.1-sol / medium。公式規定・保存済み訓練範囲・公開メタデータを照合し、次の実験の入力候補を整理する調査で、実装・新手法の設計はしないため。依頼を保持し、調べた原文と取得経路、未確定事項、結果とlab登録候補を返す。

## 結論

**小試験の候補は PHerc0800 の公式 segment `20251029010146-auto_grown_20251029010146642`。** 固定checkpointの公表学習対象外で、現行First Letters対象のCTと同じボリュームIDを持つ表面Zarrが公開されている。128²の試験入力を1オブジェクト507,904 Bで取得できることをHEADで確認した。未読候補への入力成立性を認める。対象領域に文字があるか、モデルが転移するか、発見の新規性は未確定。解読を主軸とする本人の判断は引き続き未確認。

## 根拠・詳細

- ［一次］公式カードの固定版は PHerc0139、Scroll1667、PHerc Paris4、PHerc0814で学習。MIT。対象は同じseed42/step-075000。カードでは約9 µm等方の表面を直接入力できる。8.64 µm、116 keVの対象での感度と、紙面の深さ・法線は別途確認が要る。 [固定版モデルカード](https://huggingface.co/scrollprize/ink_9um/blob/7109667e2607db1b90c37c8b09cb876ea7fe7bb1/README.md)
- ［一次］公式規定は対象20ボリューム、最大あと8巻で各$50,000、締切2027-06-25 23:59 Pacific。学習領域と重ならない再現可能なCT由来の画像で4 cm²内に判読可能な10文字、対応する平坦化TIFXYZ、スケール・行・手順・偽陽性対策・held-out検証を求める。受賞時は方法等を公開し、発見自体は主催発表まで非公開。公式WinnersでPHerc306B・PHerc0343の2026年10月First Letters受賞を確認。PHerc0800は規定に掲載され、Data BrowserはScannedとし、確認した受賞一覧で同巻のFirst Letters受賞は確認できない。これが確認時点の公式状態で、審査中の応募や非公開の判読は不明。 [公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [公式受賞一覧](https://scrollprize.org/winners) · [PHerc0800公式目録](https://scrollprize.org/data_browser/PHerc0800)
- ［一次］公式目録のCT・セグメント利用条件はCC BY-NC 4.0。出典表示、変更の明示、非商用条件を確認。規定は公開資産の使用を資産側の条件が許す範囲で認めている。今回の入力は公式資産を選択。新発見の公表時期は賞の規定に従う。 [データの利用条件](https://scrollprize.org/data_browser/PHerc0800) · [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) · [公式規定](https://scrollprize.org/prizes)
- ［一次］PHerc0800物理scan `20250510225703`、公式応募対象の再構成volume `20250521135224`、8.64 µm等方、116 keV、CT L0 ZYX `[24298,9867,9867]`、`128³` uint8非圧縮で、サンプル `0/94/48/26` はHEAD 2,097,152 B。segmentのTIFXYZ名と表面Zarr名はともに再構成volume IDを持ち、表面attrsは元のmasked CT・L0参照を持つ。XYZ bboxは `(3089.98,5907.08,11617.88)..(3703.02,6614.25,12497.98)`、格子scale 0.05、X/Y/Zの3 TIFFとmetaはS3一覧合計29,497 B。bboxはメッシュ全体のCT座標で、表面上の部分領域をCTへ引くには実際のXYZ座標と補間・法線の確認が必要。表面Zarrの軸はZYX（深さ、行、列）で原CTのZYXとは別、L0 `[31,980,980]`、チャンク `[31,128,128]`、uint8非圧縮、1ボクセル刻み。L1以降はXYのみ粗くなる。 [CT L0定義](https://vesuvius-challenge-open-data.s3.amazonaws.com/PHerc0800/volumes/20250521135224-8.640um-1.2m-116keV-masked.zarr/0/.zarray) · [TIFXYZ meta](https://vesuvius-challenge-open-data.s3.amazonaws.com/PHerc0800/segments/20251029010146-auto_grown_20251029010146642/mesh/20251029010146-on-20250521135224-8.64um.tifxyz/meta.json) · [表面Zarr attrs](https://vesuvius-challenge-open-data.s3.amazonaws.com/PHerc0800/segments/20251029010146-auto_grown_20251029010146642/surface-volumes/8.64um-1.2m-116keV-volume-20250521135224.zarr/.zattrs)
- ［一次・先行実験者報告］公式の6セグメントと別に、コミュニティはPHerc0800で95メッシュと公開インク確率マップを生成済み。配布者は自身の選別で文字として残ったものはないとし、2026-09-15の訂正で両方向の命名が公式と逆と説明。別の実験者は公式の別segment `20251028213516-auto_grown` で法線反転による公式順の再現を報告。今回の末尾146面の法線符号・文字側・紙面位置・既存95面とのCT上の重なりは未照合。公式S3で確認した6セグメント直下はmeshとsurface-volumes。公式のsurface/lasagna予測は形状用で、コミュニティのインク確率画像や、主催が判読・受賞と認めた結果とは区別する。 [公開確率マップの原文](https://huggingface.co/datasets/pscamillo/vesuvius-eligible-meshes-ink9) · [法線の先行確認](https://github.com/rodriguescarson/eligible-scroll-atlas/tree/main/repro/orientation)

### 比較した二巻

| 巻・公式の物理scan／volume | 現行規定・読まれた範囲 | 入力の不足 |
|---|---|---|
| PHerc0211・`20250720140115`／`20250821151803`（9.362 µm、113 keV） | 現行対象、公式Scanned。主催掲載のProgress Prizeで螺旋面を公開。作者は z=10000–11000 / w010–065 の窓で文字を主張せず。 | CT L0 ZYX `[19416,7948,7948]`、128³ uint8非圧縮。公式segmentsは0、S3の同prefix空。コミュニティには対応CTで作ったメッシュと予測があるが、小領域の配布単位とmesh/層方向・適用箇所の対応は未確定。 |
| PHerc0826・`20250720174915`／`20250821151701`（9.362 µm、113 keV） | 現行対象、公式Scanned。主催掲載のProgress Prizeは工程実証で、作者は試験窓でインクなしと報告。 | CT L0 ZYX `[16920,8169,8169]`、128³ uint8非圧縮。公式segmentsは0、S3の同prefix空。コミュニティのCC BY-NC 4.0 TIFXYZに3窓（z=6528–7328、8928–9728、9328–10128）があるが、作者が形状未検証と明記。小領域の配布単位と法線の対応は未確定。 |

［一次］両巻のCT/公式データは同じCC BY-NC 4.0。公式の読みの状態とコミュニティが走査した窓の結果を同一視しない。 [PHerc0211公式目録](https://scrollprize.org/data_browser/PHerc0211) · [0211先行報告](https://github.com/bnleft/first-light-pherc0211) · [PHerc0826公式目録](https://scrollprize.org/data_browser/PHerc0826) · [0826先行報告](https://github.com/millerandmuller/first-light-pherc0826) · [0826公開螺旋面](https://huggingface.co/datasets/rodriguescarson/eligible-scroll-spiral-fits)

### 次の最小試験案

1. ［推論］別の実行として、末尾146のL0 `0/0/3/3`（表面XY各 `[384,512)`）だけを、HEADのContent-Lengthと受信上限を照合して取得する。31層を保持し、空白・非ゼロ画素、紙面中心のずれを先に確認。公開metaに法線の符号と実紙面位置の明記がない。中央15を仮中心とし、まず公式CLIの17層 `[7,24)`、必要なら深さを反転した別の結果を同じ基準で記録。既知28層の `[6,23)` は流用しない。
2. ［推論］既存ローカル重みとCPU構成で128²、1ワーカー・1 CPU・バッチ1・TTAなし、単一パッチ約4.49秒が既知対照の実測。128 pxは約1.11 mmで、入力と出力の健全性確認に使う。256²（XY各 `[384,640)`）ならHEAD確認済み4オブジェクト2,031,616 B・50%重複で9パッチ約40秒、512²（XY各 `[256,768)`）なら16オブジェクト8,126,464 B・49パッチ約220秒。一方向の単純換算で初期化・転送・I/Oは別。試験を広げる判断は1パッチの有効な紙面・スコア・深さの確認後。絶対的な文字の有無はこの試験で判定できない。
3. ［推論］元CTからの再描画が次に必要なら、先に29,497 BのTIFXYZで部分領域のCT座標・周辺法線と補間ハローを確定し、必要なCTチャンクだけ全件HEAD。現時点で元CTの転送総量は未確定。まず公開レンダーでモデル入力を検査できるので、初回のCT転送は0 B。

## 取得の経路・メモ

2026-11-13 09:07:26–09:11:09 UTCにcurlで一次原文、S3一覧・属性、17件のHEADを保存。新規HTTP取得本文合計1,038,989 B（保存した404・401・上限で打ち切ったAPI一覧を含む）。個別URL・UTC・HTTP状態・本文実測は [取得原票](../experiments/vesuvius/r013/20261113-unread-input-feasibility01/http.txt) と [追加取得原票](../experiments/vesuvius/r013/20261113-unread-input-feasibility01/extra-http.txt)。`data_segments/` 等の一部ページはリダイレクトや404で、対応関係の根拠はS3の公式一覧と個別attrs・metaを使用。HEADのContent-Lengthは将来の転送見積もりで本文取得量には含まない。試験・推論・学習・応募・有料計算は未実施。
