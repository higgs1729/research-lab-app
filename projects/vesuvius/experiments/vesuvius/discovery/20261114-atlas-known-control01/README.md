# PHerc0343の既知文字表示対照

2026-11-14 JST。対象は SharpMeow / Chase Hendrick の First Letters ink atlas、固定revision ac5ffd7098120368216948c4e06c494bf8e67178の kbh-POS_PHerc0343_erwin。アトラスと派生図はCC BY-NC 4.0、トレースの出典は ketchupbyheinz の vesuvius-scroll-survey。今回の作業は公開資料の照合、原画取得、固定表示と目視。既知の読解は Erwin Nieuwlaar と主催者・審査者の成果。 [固定アトラス](https://huggingface.co/datasets/SharpMeow/first-letters-ink-atlas/tree/ac5ffd7098120368216948c4e06c494bf8e67178/surfaces/PHerc0343/kbh-POS_PHerc0343_erwin) · [公式受賞発表](https://scrollprize.substack.com/p/50k-first-letters-prize-awarded-for)

## 受賞領域との対応

アトラスの固定meta.jsonを固定木のGit blobで照合した。metadataはreferenceと、固定surveyの POS_PHerc0343_erwin メッシュを指す。固定surveyのREADMEは Erwin の PHerc. 343 First Letters セグメントを文字あり対照とする。主催者は w047・w048を継ぎ合わせた受賞領域を記述し、受賞者の再現READMEも結合セグメント名を記す。この来歴で同じ受賞面に由来する表示対照と判断した。両配布のメッシュのバイト比較と、公式画像とアトラス画素の登録は未実施。公式発表の判読結果は外部根拠で、この比較から公式の各文字や行番号を再同定していない。 [固定面メタデータ](surface-meta.json) · [固定surveyのREADME](survey-readme.md) · [受賞者の再現README](winner-readme.md) · [対応原票](source-match.json)

## 固定表示で見えたもの

原画は各6048×2304、8bitグレー、9.6 µm/px。167と同じ0–255の表示で、一覧は3×3面積平均、原寸例は階調と画素を保持して同じXYを3チャンネルから切り出した。 [全体一覧](comparison.png) · [原画XY](native-boxes.json) · [原寸画素の照合](native-check.json)

- 主行中央 x=[2880,4130), y=[700,1110) のreverseで、横長の帯に、内側に暗い隙間を残す曲線、上に立つ太い画、曲がって戻る画が並ぶ。局所では飽和して画がつながる部分もある。CT中央層の繊維や黒い亀裂だけから同じ輪郭を一対一に同定できない。 [主行中央](native-main-center.png)
- 主行左 x=[740,2260), y=[980,1440) のreverseでは、輪状の空隙や区切られた明部が連なる。全体では右へ進むにつれ上がる主行として追える。 [主行左](native-main-left.png)
- 下段 x=[1420,3310), y=[1430,1830) では、主行の下に別の明部列があり、丸い斑点に加えて湾曲した立ち上がりや暗い切れ目が見える。 [下段](native-lower.png)

forwardにも局所の明部はあるが、同じ位置でreverseほど字画のまとまりと行は明瞭でない。表示の陰陽や両方向の一致を判定条件にしていない。今回のensemble/は保存深さ順の統計を両予測で使う7モデルzスコア平均で、表示域はz=[−2,+4]。飽和255は原寸主行中央のreverseで115,525/512,500画素。飽和や画の癒着を含むため、本画面からの文字転写は保留した。 [面メタデータ](surface-meta.json) · [飽和と同一性の原票](native-check.json)

この既知例では167と同じ表示で予測の行構造を識別できた。未知面での感度・特異度、学習と対象メッシュの重複、167の二面のインク有無は未評価。受賞者の手法と今回のアトラス7モデルの学習・合成条件は別。

## 再利用と資源

研究167の固定木・HEAD・LFS SHA検査の取得手順を使い、3原画だけを逐次取得。固定木と面meta、公式発表、survey・受賞者のREADMEの新規一次資料5件278,504 B。原画計11,311,667 B、GET 5.450秒、全件サイズ・SHA・ETag一致。計画は画像GET前に保存。 [取得計画](acquisition-plan.json) · [取得原票](get.jsonl) · [一次資料台帳](primary-sources.json)

画像処理3起動は既存WindowsランナーでCPU1、数値スレッド1、4 GiBプロセスcommit上限。合計2.468秒、最大RSS72,470,528 B。LinuxのAS/core制限は使用していない。元CT・メッシュ・モデル、推論、課金、外部公開はいずれも0。原画3枚と固定JSONを保持し、図を再生成する場合は別ディレクトリで既存ランナーから prepare_view.py、native_view.py、check_native.py を順に実行できる。 [一覧作成プロセス](analysis-process.json) · [原寸作成プロセス](native-process.json) · [検証プロセス](check-native-process.json)

主担当の別目視では、一覧図と主行左・中央・下段の原寸例で、同じ行構造と飽和・癒着を確認した。 [別照合](lead-check.json)
