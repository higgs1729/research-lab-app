Status: resolved
担当: 研究（R246 Sol/xhigh）

# R123単独を固定上流版で構築し、実描画からreaderの前後差を示せるか（2026-11-16）

## 依頼

本人の上流PR方針に向けた、R245に続く一件。R245は実w035由来の同一画像に旧OME目録だけを付けると、公式OME-ZarrのReaderはpath1で失敗し、vc_readerの正規最粗level(-1)も失敗することを確認した。主担当が別脚本でOMEの前後差を確認済み。しかし入力は旧結合版による保存出力で、R123単独を現在の固定mainから構築した実描画は未実証。この境界を埋め、本人がClaude側で行う実利用・コード確認へ具体物を渡す。

問い：上流villa固定main `2d3fb38d33a18b257230c0bd23986436c3d4722e` の通常rendererと、R123メタデータ修正だけを加えたrendererで、同じ実w035入力のpyramid=false描画→実reader読込の前後差が再現するか。製品差分は既存 `experiments/vesuvius/r009/20261113-pyramid-metadata01/pyramid-metadata.patch` の範囲（writeZarrAttrsへwantPyramidを渡しlevelsを0にする）に限定。R007/R121/他R009/R005を含めない。既存PR #2529のresume修正に広げない。

欲しい形は、元と修正の正確なソース/依存/生成物の版、単独の小パッチ、実データ前後のログと出力、本人が未使用のrun名で繰り返せる短いコマンド。上流AGENTS/CONTRIBUTING/局所READMEを先に読み、本人の動機・本人レビュー・スクリーンショットをAI試験で置き換えない。外部fork/push/PR/コメント/公開/応募はなし。ローカルGitを使うなら作成する対象だけにhiggs1729とGitHub noreplyを設定し、既定の個人メールを使用しない。実際のnoreplyは既存公開コミットや本人の設定を読み、捏造しない。コミット自体が不要ならしない。

再利用の参考は研究160の固定main通常CMake成功。`experiments/vesuvius/bundle/20261113-fixed-main-integration01/README.md`、同run01のsource/blob/build記録、C上WSL `/home/tomoy/bundle-fixed-main-run01-pywin6ml`。旧R160のソースは修正済みで、そのまま新基点にはしない。原blobや固定treeと照合し必要な上流差分だけ取得する。手順は現物から適応してよいが、全履歴・巨大モノレポの無制限cloneやD:でのGitは禁止。Dは読取専用で、依存がsourceへ書き込む場合は新Cコピーを使う。既存研究のソース・build・生成物・データ・結果を変更しない。

新しいC/WSL作業先と原票は `experiments/vesuvius/r009/20261116-standalone-metadata01/` から参照。まず既存能力・サイズ・必要本文の取得量を確認し見積を残す。初期上限：C追加3GiB、C空き2GiB維持、ネット応答本文64MiB、CPU1・数値/OpenMP1・AS4GiB・core0。構成600秒、標準baseline build一回1800秒、修正後増分一回300秒、固定実描画各90秒。基点を揃えるために新依存/全体の大規模再構築が必要で上限に収まらない場合は、事実と最小の代案を返す。新CT/GPU/有料0。取得終了後はネット分離しビルドする。新設/変更する入力原票の境界は小さい現物で保存→読み戻し→使用を先に確認。汎用基盤追加や既存全出力の再監査は不要。

前後二つの大規模buildを繰り返す必要はない。R123が単一TUだけを変えるなら、新しいbaseline buildで元ソース/ELF/依存を固定して保管し、同じ新作業先で修正後の標準増分buildを使ってよい。元ELFから共有ライブラリの実体とSHAを固定し、増分後も不変であることを確かめる。取得済み原ソースとmanifestを残し、baselineの版を後から推測する状態にしない。上流の要求に必要な意味ある回帰確認は既存の試験を優先し、同じ条件を再実行し続けない。

実例は既存w035の入力を利用し、どの面・CT・crop・層数なのかを明記する。R123の128×128×101と保存CTが使えるなら同じ入力が比較しやすい（例）。固定同入力で通常pyramid=falseを元/修正各一回描画し、目録・実階層・L0画素一致とOME-Zarr Readerの前後差を示す。必要な補助として修正版pre falseの目録、pyramid true既定の不変を有限確認する。実描画の旧出力には.zgroupもあることを確認し、R245の対照移植を再現そのものとして使わない。追加のreader探索/GUI/模型入力/未知巻研究へ広げない。

今回の担当はgpt-6.1-sol / xhigh。既存の通常build手順を再利用できるが、現在mainへの固定本文の補完、修正を含まない基点と生成物の分離、実readerまでの統合に未確定部分があるため。再委任なし、一件のみ。最初の短い状態報告で使用する作業先・資源見積・実行開始を知らせる。主担当はClaudeへWSLの使用時間を伝え、重要結果を別検証しlab/recallとHUMAN_REVIEW_HANDOFFを更新する。担当は本票の結論と範囲・再現手順・限界を記しresolvedへ。既存凍結証拠は不変。

## 主担当からの来歴訂正（実行前、11月16日11:09 JST）

依頼のR245/R123の「w035由来128×128×101」は主担当の誤記。正しくはPHerc0814、crop[7356,2272,128,128]、元面20250929040153-auto_grown_20250929040153260。R006 zarr-whole-process READMEとR005 first-trace-on01/state.jsonの取得URLから確認した。R245の固定入力とreader結果は変更しない。R246でw035を使うならR131/R132の64×64×28やR160の1×129×28など、本当にPHerc0139の保存原票を確かめて使う。PHerc0814の同じ128²×101を用いる方がこの有限比較に適するなら、正しい来歴で使う代案も可。架空のw035ラベルで進めない。原依頼は履歴として保持する。


## 結論（2026-11-16 JST）

［一次・実行］villa `2d3fb38d33a18b257230c0bd23986436c3d4722e` の通常CMake rendererと、`writeZarrAttrs` にR123だけを適用したrendererで、実描画から差を再現した。PHerc0139のTIFXYZ面 `20260317000000-w035_2026031718`、保存CT `20250728140407` のL0（9.362 µm）、公開キャンバスXYWH `(2176,1408,64,64)`、28層・層間1を固定。通常 `--pyramid false` は新旧ともZarr v2 `.zgroup` があり、実配列はL0のみ。元のOME目録は `0`〜`5` を指し、OME-Zarr Python 0.21.0 / Zarr 3.4.2 の画像Readerが path `1` の `ArrayNotFoundError` で停止した。修正後は目録が `0` だけになり、同Readerで1画像ノード・1配列を読めた。[両Zarrと実行原票](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/) · [OME実端末](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/ome.log) · [Reader確認](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/reader-confirmed.json)

［一次・実行］前後の通常falseは `.zattrs` だけが変わり、属性の意味差は存在しない `datasets` 1〜5の削除。両方の直接L0と修正後のReader配列は全114,688画素で一致。ZYX `(28,64,64)`、uint8、C順序SHA-256 `8d68bf7bbea4248bf0bf76cdd8c4707aeea70b4d95d6837e378f572698ea9630`。修正後 `--pre --num-parts 2 --pyramid false` は同じ3メタデータと0チャンク。元・修正の既定は6実レベルと目録を持ち、14ファイルがバイト一致した。主担当の別脚本もnative現物とローカルPR作業ツリーの修正ソースを照合した。OMEの版自動判別loggingは前後両方に出た。[全ファイル比較](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/native-comparison.json) · [独立native検算](../experiments/vesuvius/r009/20261116-standalone-metadata01/lead-native-check.json)

## 根拠と再現

- ［一次］固定commitとGit treeを検証し、対象2,362ファイルをblob SHAと実本文SHA-256で記録。上流と製品ハッシュ差は `volume-cartographer/apps/src/vc_render_tifxyz.cpp` 一つ。3ハンクは既存R123パッチとバイト一致。元ELFを凍結し、前後の動的ライブラリ実体71件のパス・SHA-256を照合。元ビルドは1800.095秒で236工程、同じgraphの残11工程を125.034秒で完了。修正後はrendererの製品TU一つとリンクを38.627秒で完了。glob確認とQt自動生成確認も走ったが、生成mocソース・オブジェクトのmtimeは増分開始前のまま。局所依存と二つのランナー判定停止の原票を保存した。[版・時間・再現コマンド](../experiments/vesuvius/r009/20261116-standalone-metadata01/README.md) · [単独パッチ](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/pyramid-metadata.patch) · [実増分命令](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/incremental-commands.json)
- ［一次］native完了時の作業実割当は失敗構成も含め1,739,653,120 B、C:空き4,894,015,488 B。既知の通信本文10,155,948 Bと初回疎通の保守8 MiBを合算して64 MiB以内。有料0、新CT・GPU・外部書き込み0。Windowsでの本文取得はCPU affinity未指定。nativeとreaderはCPU 1、数値スレッド1、4 GiB上限。保存入力と共有ライブラリを再照合した。[資源原票](../experiments/vesuvius/r009/20261116-standalone-metadata01/run03/native-complete.json)
- ［推論］この条件で壊れていたのは、目録から階層を開くreaderの経路。L0直読の内容は同一だった。範囲は固定データの端末rendererとOME Python画像reader。本人の実利用・動機の本人記述・本人レビュー・前後画面は引き続き本人側で必要。

## メモ

- 2026-11-16 ［一次］固定commitとroot treeを再構成し、上流指示、該当READMEと既存build依存の入口を確認。R160とblob/modeを比較し、旧パッチ適用ファイルを流用せず原本を復元。不足300 blob 6,925,794 B。R129/R131の現物ハッシュと公開来歴からPHerc0139 w035の64×64×28を選択。
- ［一次］構成run01は固定mainの新要件 `concurrentqueue` が無く153.690秒で終了1。APT目録のSHAと照合したUbuntu公式 `libconcurrentqueue-dev 1.0.4+ds-1` 61,138 Bを局所展開。run02はそれを通過し、`blosc2>=2.13` が無く209.812秒で終了1。通常ビルド起動0回。
- ［一次］旧版とのCMake依存差分を一括照合。Ubuntu公式Blosc2開発・実行パッケージ2.13.1、上流vc-delta3d v0.3.2 commit `427248122a088bad7d5b1209ea55c311de3378bb` を追加。R160依存を変更せず新C内のprefixに展開。run03はrun02の途中CMake cacheを使い、主担当が変更を認めた構成累計900秒の範囲で開始。R123パッチは既存凍結版とバイト一致。[原票](../experiments/vesuvius/r009/20261116-standalone-metadata01/README.md)

- ［一次］run03の構成380.193秒、3回累計743.695秒。通常buildを11:34:24 JSTに開始。序盤の同名reader 12出力はR160の計54.69秒に対して258.17秒。固定版を構築する価値と完了済み出力を踏まえ、主担当がbaseline期限を開始から3600秒に延長。既存タイマーが1800秒に達した場合は同じNinja graphと完了済み出力を保存したまま、残工程だけを絶対期限内に続行する。
