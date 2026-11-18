# 公開未読候補の再選定

2026-11-14 JST。担当と主担当が固定surveyの公開JPEG三枚を原寸表示で確認し、次の元CT取得に結び付けられる独立字画や行を選べなかった。三面についてはCT追加を見送る。次に調べる一面は、別来歴のPHerc0813 `z12496_w020`。まず公開済みの順逆予測を原寸で確認し、元CTへ戻せる位置が得られるか判定する。画像本体の取得とCT試験は別の研究票で扱う。[主担当の別目視](lead-visual.json) · [主担当の資料照合](lead-source-check.json) · [次の一面](next-plan.json)

## 三候補

[一次] 現行First Letters対象は20件。候補三巻は以下の再構成で対象。0813と1545はGrand Prize対象にも含まれる。三巻とも公式Data BrowserはScanned、9.362 µm、113 keV、CC BY-NC 4.0。今回保存した公式Winnersと対象一覧には三巻の既読発表を見つけなかった。公開範囲での確認で、未公表の判読までは扱えない。First Lettersの基準は単一4 cm²内の可読10字とCT・対応面に由来する画像。予測領域との訓練重複を認めない。[公式規定](https://scrollprize.org/prizes#first-letters-prizes) · [公式Winners](https://scrollprize.org/winners) · [0846B](https://scrollprize.org/data_browser/PHerc0846B) · [0813](https://scrollprize.org/data_browser/PHerc0813) · [1545](https://scrollprize.org/data_browser/PHerc1545)

| 固定surveyの面と公式CT | 先行観測 | JPEG原寸で見える範囲と判断 |
|---|---|---|
| PHerc0846B `3962,4983,7051`。scan `20250719185515` → CT `20250804142305`。面積4.442 cm² | 追試のforward、強いタイル8対0/13、面比4.053。四モデル六対の内外比1.516–4.053。暗部率.246、chain 1.375（逆側1.448）。初回周辺14追試のタイル側は内10・外3・不明1。著者は平坦部で内外判定の不確かさを報告。 | 右パネルx=[1100,1290), y=[320,450)の強い反応の複数が暗い割れに接する。上方の点や横長の短い塊から独立した字画が続く行を選べない。 |
| PHerc0813 `4654,5413,8615`。scan `20250720160015` → CT `20250821151723`。面積4.307 cm² | 初回 `4779,5850,8497` の追試。forward、6対0/12、面比2.366、暗部率.106、chain 1.345（逆側1.017）。4追試の側は内2・外1・不明1。初回の全域優勢はreverse、タイル側はforward。別高さ `3131,2667,11895` の面比2.963に対し、この追試は暗部率.155より低い。 | x=[1104,1144), y=[469,548)の縦長片と、x=[999,1046), y=[184,237)の短い横片は互いに離れる。左下の反応には空隙縁が重なる。字画の反復や基線を選べない。 |
| PHerc1545 `3051,3484,14673`。scan `20250720045926` → CT `20250821151648`。面積4.041 cm² | 初回surveyの別高さ。reverse、7対0/11、面比2.481、暗部率.126、chain .960（逆側1.357）。四モデル・近傍の追試はR177/R178で使った種点 `3499,4074,9431` の側で、本面への確認はない。本面metaのZ=[13242.126,16110.5]、既試験の親面metaは[8378.277,10591.978]で分離。 | x=[870,1015), y=[350,505)に癒着した大きい反応、x=[1190,1450), y=[550,700)に斜めの繊維に沿う斑点。独立字画の並びを選べない。 |

[一次] 三つのmetaはそれぞれ公式指定volumeのm7 `20260413222639` L0 th0.2を使った `vc_grow_seg_from_seed`、step20、TIFXYZ scale約.05、物理XYZ seedとbboxを持つ。固定木に各x/y/z TIFF（各56,329 B）がある。三JPEGは1773×786 RGB。表のXYはJPEG全体の左上原点、上限を含まない。JPEG右の黄色はsheet goodの範囲に限定した正規化2予測の平均をクリップしてCTへ重ねた加工表示。暗部率は別に、2モデル上位3%の交差画素がmask内CTの最暗10%に落ちる割合。単一の字画ごとの暗部率とは扱えない。[固定survey原文](../20261114-atlas-known-control01/survey-readme.md) · [数値表原文](survey.csv) · [カード・メタの固定照合](github-docs-verified.json) · [描画コード](../20261114-pherc0846a-lead-audit01/report_card.py) · [固定JPEG一覧](preview-plan.json)

[一次・範囲] 固定treeとsurvey入口から、原寸予測の `seed42_s6[_reverse].tif` と `dnative_s6[_reverse].tif` はローカルwork出力。三候補の公開木で確認できたのは集計、加工カード、面meta/XYZ。固定描画コードは縮小パネル二つと定幅欄を足す幅式が偶数になる一方、保存JPEGは1773幅。ローカルのrender範囲、実際のJPEG変換、画素→native対応を示す資料を確認できない。固定atlas ac5ffd7098120368216948c4e06c494bf8e67178 で公開された0813面は `2999_3156_5096`、0846B面は `2768_2813_9748`。1545は公開0・held13。確認した別面IDから各候補の画素対応や物理的な重なりは得られない。 [survey入口](survey-entry.py) · [固定atlas一覧](../20261113-next-target01/ink-atlas-index.json)

[一次・範囲] seed42/43公表学習一覧はPHerc0139、1667、Paris4、0814。dense-native step16000の公表資料の追加対象はPHerc0139、初期化はKLAVIS dense-ex016。調べた公表一覧に候補三巻を見つけなかった。起点重みを含む全座標との照合とHecateの学習来歴は未検証。seed42/43は同じレシピでseed違いであり、R172がdense-nativeとseed42のモデル構造も一致と確認した。モデルペアの一致は信号の候補を整理する情報に留める。 [公表モデルカード保存](../20261113-next-target01/official-model.md) · [R172の固定学習資料と照合](../20261114-pherc0846a-dense-native01/README.md)

[推論] PHerc0211は著者が近傍の側の反転とseed43の不支持（dense-nativeとの比1.06）で主候補から外している。PHerc0306Bは固定survey後に公式First Lettersで既読発表。PHerc0846Aの171/176、PHerc1218の165–167、PHerc0800の137–143、PHerc1545の178で見た範囲を今回の再取得先にはしない。R185の補正は今回の候補に適用しない。[固定survey原文](../20261114-atlas-known-control01/survey-readme.md) · [公式Winners保存](originals/official-winners.html) · [R185](../../../../research/185-known-text-refinement-pilot.md)

## 次は別来歴の公開予測を一面で見る

[一次] pscamilloのGitHub固定版 `620769e2e1e70d1e61b588092229cb76d3af4804` は、umbilicusとlasagnaを使うspiral fitをflattenした一巻きごとのTIFXYZとindexを公開する。PHerc0813 `z12496_w020` のindexは1.73 cm²、目視ゲート `aprova`。配布カードの例示 `z12496_w100` は同じ高さで `reprova`、予測2本で15,990,932 B。著者がゲートで扱ったのは紙面の繊維の見え方で、文字の判定とは別。配布全体について著者は文字screen通過例がなかったと記す。w020を優先する理由は、目視ゲートを通った面と小さい予測本文を同じ固定面IDで確認できること。今回のsurvey面と同一とする証拠はなく、こちらは別の高さ・面生成経路。1.73 cm²は4 cm²以内の範囲条件を満たす面積だが、この面に可読10字がある証拠は得ていない。[固定index](originals/pscamillo-mesh-index.csv) · [固定生成法](originals/pscamillo-mesh-method.md) · [GitHub固定面](https://github.com/pscamillo/vesuvius-eligible-meshes/tree/620769e2e1e70d1e61b588092229cb76d3af4804/meshes/PHerc0813/z12496_w020)

[一次] Hugging Face固定版 `dd968475bca14ccfbfd7b06cc6ba87723bb25642` の `PHerc0813/z12496_w020.tif` 1,135,632 Bと `PHerc0813/z12496_w020_reverse.tif` 1,300,494 B。合計2,436,126 B。著者は単チャンネルuint8、面と同じ格子と記載する。scale1・L0・31層・step1、seed43 step060000、層7:24。著者訂正で `_reverse` がチームのforwardに相当し、無接尾がreverse。実画像の幅・高さ、native canvasとTIFXYZ節点格子の対応、当時のrenderer版とこの面の厳密なCT接続は本文未取得のため未検証。公式PHerc0813に表示されるscanは1件、指定CTも1件。次票でw020のmeta、XYZ、公開予測の寸法と原点・方向を照合する。[配布カード原文](originals/pscamillo-hf-readme.md) · [固定ファイル木](originals/pscamillo-hf-PHerc0813-tree.json) · [公式Data Browser保存](originals/official-PHerc0813.html)

[推論・次票] 新規はこの一面の2予測（計2,436,126 B）とTIFXYZ3枚（合計2 MiB上限）、必要なメタ（512 KiB上限）、合計5 MiB以内。固定版で長さとSHAを照合後、固定0–255・原寸の予測2枚を面の有効範囲と並べ、輪郭や間隔が独立して読める部分と、繊維や面端が連続する部分を確認する。ROIを出す場合は親が別目視し、座標来歴と支持を確認する。画素対応や字画候補が得られなければ、その一面で閉じる。作者の体積レンダーが同じ面・同じ画素で使えるかは未検証。今回は予測画像の存在と取得量を確認した段階。 [固定計画とハッシュ](next-plan.json)

[推論・後段の条件付き予算] 独立字画候補があり画素と面が対応した場合に限り、別票で同じ面の一つのnative 512² ROIを固定し、紙面と空隙への位置を検証する。先に実幾何とL0のチャンク定義・HEADで本文の正確な支持と量を凍結する。R171では別面512²に44キー88 MiB、幾何92.953秒、描画3.011秒。今回の概算上限案は64キー/128 MiB、通信300秒、既存observerとrenderer各180秒・CPU1/AS4 GiB・追加クラウド0円。支持や上限が成立しなければ本文取得前に閉じる。比較に再推論を含めるかは公開予測と紙面の所見で判断し、追加モデルやopacity補正は計画しない。[R171実測](../../../../research/171-pherc0846a-ct-to-ink-pilot.md)

## 取得の経路

原文・小メタ24件、487,508 B。GitHub connectorで14件97,671 B、公式5件304,571 B、HF API等3件80,169 B、GitHub REST目録2件5,097 B。公式はWebでも現行条文を確認し、集計は保存したHTTP本文とconnector本文。JPEG三枚1,016,367 Bは既存の固定treeで長さとGit blobを照合して保存した。XYZ TIFF・新しい予測TIFF・CTボクセル0 B。取得先C、追加の推論・GPU・ビルド・クラウド支出0、外部公開なし。JPEG原寸は復号した保存画素の表示で、局所強調や生成補完は使っていない。[取得明細](acquisition.json) · [ファイル照合](manifest.json)

