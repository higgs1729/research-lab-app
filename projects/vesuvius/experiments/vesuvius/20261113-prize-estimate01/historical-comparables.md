# Vesuvius Progress Prizes の過去事例

2026年11月13日時点。公式受賞一覧と公式発表から、今回と技術領域が近い小規模修正と、上位の比較対象を計6件選んだ。表の日付は受賞対象月。発表日が公式記事で確認できた場合に併記した。

| 受賞対象月・金額・受賞者 | 公式発表の短い原文 | 内容と実利用・上流統合の根拠 | 今回との比較 |
| --- | --- | --- | --- |
| 2026年9月・$250・Kaden Pool | “Five merged villa PRs” | ink modelの入力層選択の修正を含む5件のvilla PRがマージ済み。個別の実利用は発表で確認できない。[公式受賞一覧](https://scrollprize.org/winners#40500-progress-prizes-september-2026) | 既存機能を複数修正した点が近い。上流統合済みでもこの金額の事例がある。 |
| 2026年9月・$500・Christopher William Scheirer | “greatly reducing memory use” | 同じ表面レンダラーで、実際に参照するチャンクだけを先読み。公開PHercParis4メッシュとインク予測を用い、16 GB制限で従来版が終了したレンダーを修正版で完走。比較出力のTIFFはバイト一致。9月30日にvilla mainへマージ済み。[公式受賞一覧](https://scrollprize.org/winners#40500-progress-prizes-september-2026) [villa PR #1905](https://github.com/ScrollPrize/villa/pull/1905) | 対象ツールと実データでの修正検証が最も近い。先例は実際に困った処理から始まり、メモリ・転送量・時間の効果と上流統合まで確認できる。 |
| 2026年7月・$1,000・Prasad Khake（8月6日発表） | “PRs improving zarr reading” | Python VolumeのZarr 3マルチスケール読込を修正し、別PRで任意のキャッシュを復元。PRにScroll 1のHTTPS読込実測あり。両PRのmain統合は発表後の8月9日。[公式発表](https://scrollprize.substack.com/p/335k-awarded-in-july) [公式受賞一覧](https://scrollprize.org/winners#33500-progress-prizes-july-2026) [villa PR #1177](https://github.com/ScrollPrize/villa/pull/1177) [villa PR #1373](https://github.com/ScrollPrize/villa/pull/1373) | 既存のZarr階層処理と検証という点が近い。先例はPython標準入口の読込が失敗する問題、今回の主対象は中断後の再開と出力階層の整合性。少なくともこの先例では、発表前のマージは不要だった。 |
| 2024年11月・$1,000・Chuck（2025年1月23日発表） | “convert them to the multi-resolution OME_Zarr format” | 単層のZarrを多解像度OME-Zarrに変換するスクリプト。値域、チャンク、圧縮も指定可能。公式記事がKhartesViewerのコードと文書へリンクし、外部利用は明記していない。[公式発表](https://scrollprize.substack.com/p/vesuvius-challenge-progress-prizes) [公開コード](https://github.com/KhartesViewer/scroll2zarr/blob/main/zarr_to_ome.py) | OME-Zarrの出力が近い。先例は変換の新機能を提供し、今回は既存出力の正しさと復旧を改善した。 |
| 2026年7月・$2,500・William Stevens（8月6日発表） | “run across all of Scroll 4” | パッチの誤接続によるシートの取り違えを除外する最適化をScroll 4全域で実行。公式記事はVC3Dで扱えるtifxyz出力を確認し、上流マージや第三者利用は明記していない。[公式受賞一覧](https://scrollprize.org/winners#33500-progress-prizes-july-2026) [公式発表](https://scrollprize.substack.com/p/335k-awarded-in-july) | 誤接続を避けるという狙いがUV改善に近い。先例は巻物全域に対するアンラップ手法の改善。今回の成果は公開メッシュ2点と、うち選定領域の実CT例で検証した。 |
| 2025年5月・$5,000・Philip Allgaier（6月13日発表） | “the return of prebuilt docker packages” | VC3Dの配布Dockerを復活させ、複数のメモリリーク、CIビルド、Ubuntu/Qt互換性、診断表示を改善。公式GitHubでDockerイメージ配布とダウンロード数を確認できる。人数や解読での利用は特定できない。[公式発表](https://scrollprize.substack.com/p/may-progress-prizes-and-updates-to) [ScrollPrizeの公開コンテナ](https://github.com/ScrollPrize/volume-cartographer/pkgs/container/volume-cartographer) | 既存ツールの安定性と使いやすさへの貢献も$5,000になった例。配布・導入・UI・運用に及ぶ改善で、今回より適用範囲が広い。 |

## 今回の評価（過去事例からの推定）

三件を一件で応募した場合、受賞時の見立ては **$250〜$1,000、中心は$500**。不完全cropで128×128のつもりが13,600×3,440を選ぶ問題と、中断後に欠けたZarr階層を回復する修正は、$500のレンダラー事例と同様に無駄な処理・再作業を防ぐ。UV成分の分離で二つの公開メッシュの成分間グリッド辺を106本・284本からゼロにした検証や、ZarrとOME目録の再現資料まで合わせると、$1,000のZarr修正に並ぶ評価もあり得る。今回の上流採用・第三者の実利用・人間レビュー・新しい文字の確認は未確認で、$2,500以上の例にあった巻物全域への適用や公式配布に相当する効果は今の資料では確認できない。[今回の公開成果](https://github.com/higgs1729/vesuvius-workflow-improvements) [公式の賞金区分](https://scrollprize.org/prizes#progress-prizes)

2026年7月には58件を審査し13の個人・チームが受賞したという公式発表がある。同種の応募の母数や非受賞案件の内容、11月の応募件数・競争状況は分からないため、今回の受賞確率は推定できない。[7月の公式発表](https://scrollprize.substack.com/p/335k-awarded-in-july)

