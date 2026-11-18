Status: resolved
担当: 研究（R160担当 2026-11-13）
Blocked by: 159

# 三件の改善を固定上流版で標準構築し、最小動作を保持できるか

## 依頼

2026-11-13。研究159では保存7ad02f4でR005の通常共有ライブラリ構築が成功した。一方、研究146–148の固定上流14d4e725df8b569e6fc8ceb3c04d130f705c1565では差分適用とソース対応までで、全体構築は未確認。本件では同じ固定版の構築に必要な3ソース範囲を揃え、既存三件をまとめて通常CMakeで構築し、既存の最小動作へ照合する。項目追加や新しい最適化ではなく、まとめた成果を再利用する際の未確認境界を調べる。

既存根拠は研究158の固定tree/不足blob一覧と159の成功手順。volume-cartographer、vc_reader、vc_object_storeの本文は既存ローカルGitを優先し、足りない本文だけ公式ScrollPrize/villaの固定commit/blobからC:へ取得してGit blob IDを照合する。158時点で375本文欠落、既存C側1件を除く374本文の未圧縮計6,965,009 B。既存Git・D:へ書き込まず、別のC側Git/ソース先を用いる。ネットワーク取得はこの既知ソースに限り、本文・metadata・pack等の総量上限32MiBを目安に上限を観測できる経路で行う。取得経路に不確実性が残る場合は小さな読取試行から判断し、制限を保てなければ原票を残して止める。全履歴や全モノレポの無制限cloneは不要。

製品差分は、154凍結候補のR005二段、147のR007.patch、146のR009.patch。原文を保持し、適用順・変更全ファイル・固定元blobと適用後SHAを記録する。新R005三ソースはR150清書済み製品SHAへ、R007/R009変更実装は既存実行対象への対応を確認する。競合、上流仕様差、追加依存が出れば独自shimや変更を足して押し切らず、根拠を保存して主担当へ返す。固定版に適用されるAGENTS/CONTRIBUTINGは保存原文も参照する。外部投稿はしない。

新規C上WSL ext4作業先にソースと必要依存を置き、159の作業・実行済み生成物・実験原票は変更しない。159で用いた既存依存ソースと標準CMake/ExternalProject、1CPU・数値/OpenMP1・AS4GiB・core0を再利用する。外部取得終了後はネットワーク分離、D:read-onlyで構築する。新しいbuildツールや製品/CMake改造、依存インストールは不要。新作業上限6GiB、ホストC空き10GiB以上を保つ。configure一回600秒、標準build一回2400秒。対象はflatboi、vc_core、vc_obj2tifxyz、vc_render_tifxyzで、GUI・Pythonパッケージ・全アプリの構築は含めない。構成が新たな外部依存を要求したら止める。

成功後は新共有ライブラリ、変更ヘッダーと利用側、依存パスの一致を確認する。実データ試験はすでに固定された以下の最小限に絞る。新データ/CT/モデル取得や設定探索はしない。

- R005: 第一PHerc0814 keep100・5反復・格子保持モードを一回120秒以内。研究150/159の172×683のXYZ3枚・全float32・scaleへ照合する。
- R007: 既存のデータ不要CLI回帰チェックを新rendererへ向ける。不完全指定が入力読取前に拒否されること、正当指定の受理を既存基準へ照合する。チェック本体は保存版を使い、不明なら現物を読んで最小同等確認とする。既存試験の無関係な全スイートは回さない。
- R009: 研究157の固定w035 crop [2239,1343,1,129]、28層、uint8・L0・bicubic・flipnormals・pyramid、保存済み2CT chunkを使う。正常と初回resumeを各一回60秒以内。正常L0だけを新しい別出力先へコピーしたL0-only状態からのresumeも一回60秒以内。Zarr論理6階層・OME・ファイルを正常対照と照合し、L0-onlyで既存L0ファイルの内容と時刻が保持されることを記録する。今回のnew baseline差が現れたら原票を残し、それを消す探索はしない。デバッガによる停止の再試験は不要。

成果は本票と experiments/vesuvius/bundle/20261113-fixed-main-integration01/ に条件・取得URL/総量/固定blob・ソース/差分/生成物・コマンドと時間/メモリ・原票・比較・lab候補。開始した各工程のPID/PGID・期限・作業先を直ちに保存し、既存仕事の重複を防ぐ。主担当が結果を別照合して採否・登録する。公開済みrepo・凍結候補・D:を不変とし、課金・PR・公開・応募・外部メッセージ・subagentはなし。通常Python初期化とwheelは今回の検証範囲に含めない。

今回の委任モデルは gpt-6.1-sol / xhigh。標準構築の手順は159で得たが、部分Gitからの固定ソース補完と三件の結合には未確認点があり、同じ実装担当の既存コンテキストを用いる。研究・検証は逐次進める。

## 結論

[一次・2026-11-13] 固定上流 `14d4e725df8b569e6fc8ceb3c04d130f705c1565` の構築に必要な3範囲を揃え、R005/R007/R009の凍結差分をまとめて標準CMake/Ninjaで構築した。`flatboi`、共有 `vc_core`、`vc_obj2tifxyz`、`vc_render_tifxyz` の4ターゲットが成功した。固定入力で三件の最小試験が通り、主担当が実ソース・出力を独立照合した。[実行・再現手順](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/README.md) · [独立照合](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/lead-check.json)

## 根拠・詳細

- [一次] 既存GitとR146の保存treeを照合し、公式raw URLから不足374本文だけを取得した。受信本文6,965,009 B、HTTP応答ヘッダーと要求側の余裕を含む計上7,824,340 B。TLS/TCP単位の実転送は未計測。取得後は通信分離・D:読み取り専用。別のext4作業先で2,269本文をGit blob ID・mode・長さに照合した。変更は10ファイル。R005の3ソースはR150清書版、R009単体の7ファイルはR146、R007/R009結合rendererはR123の実コンパイル元SHAに一致した。[取得台帳](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/fetch-plan.json) · [差分照合](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01/patch-result.json)
- [一次] readerの生成ヘッダーは正しいext4 symlink。libbacktraceは上流ExternalProjectを使い、保存ローカルGitの固定masterから `make -j1` で新規構築した。3つのラスター関連TUは同一ヘッダーを使い、両利用側とrendererは同じ新 `libvc_core.so` を解決した。rendererは新 `libvc_reader_native.so` を読み、変更したwriterヘッダーと4引数ピラミッド関数の実定義を確認した。[構成](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01/configure-check.json) · [共有ラスター](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01/link-check.json) · [rendererリンク](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01-smokes/renderer-link-check.json)
- [一次] R005の第一面はkeep100・5反復・格子保持モード1回。172×683のXYZ TIFF三枚がR150・R159にSHA-256および各117,476 float32画素で一致。名目scale一致、meta差はUUIDのみ。[R005比較](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01-smokes/comparison.json)
- [一次] R007は保存済みのデータ不要CLI試験18件が成功。不完全指定9件を入力オープン前に拒否し、正当指定5件は想定どおり欠損入力のオープン処理まで進んだ。残りはhelp・引数優先順位・mergeの確認。[R007比較](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01-smokes/r007-comparison.json)
- [一次] R009のw035固定crop 1×129×28、L0二チャンク。通常出力はR157と全15ファイル・全6論理階層・OME一致。空の出力先への初回resumeと、正常対照からコピーしたL0-only状態のresumeも同じ正常出力と一致した。L0-onlyの `.zgroup`、`0/.zarray`、既存L0二チャンクを同一コピー上でSHA・mtime_ns・inodeまで保持した。デバッガ停止・破損修復の再試験は行っていない。[R009比較](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01-smokes/r009-comparison.json)

## 取得の経路・資源

構成75.785秒、ビルド653.284秒・最大RSS1,672,572,928 B。R005 24.089秒、R007 0.376秒、R009の3起動は0.172／0.176／0.179秒。1CPU・AS4GiB、最終作業割当1,627,389,952 B、ホストC:の最終空き43,591,737,344 B。既存保護ファイルとR159原票のSHA不変。追加依存・課金0。固定上流の3サブツリー、指定4ターゲットと固定試験の範囲。GUI、通常Python初期化・wheel、全アプリの構築は未検証。[ビルド原票](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/run01/build-process.json) · [lab登録候補](../experiments/vesuvius/bundle/20261113-fixed-main-integration01/record.json)

## メモ

- R158のローカル欠落台帳とR146の固定ツリーを照合し、固定本文のみを取得する。R159の実行・計測のコードとR007/R009の保存対照を再利用する。
- 計測の初回 `ldd` 検査は `bin/../core` 形式を想定せず、正常にビルドした後に停止した。旧ログを保持し、実体パスへ解決した検査で同じ生成物を確認。未起動の試験を別の `run01-smokes` に保存した。構成・ビルドは各1回。
