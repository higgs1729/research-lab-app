Status: resolved
担当: 研究（R161担当 2026-11-13）
Blocked by: 160

# 追加成果を三件のまま再利用できる公開候補へまとめる

## 依頼

2026-11-13。三件の先行公開は a35e2d49124758bc28e7fcf499bd656387e74f5c、higgs1729/vesuvius-workflow-improvements。その後R005格子保持モード149–155、R009中断再開131–132/157、通常CMake159と固定上流14d4e725への三件統合160が完了した。研究160は record-62c2e0c9644b、159は record-20468128f2bb、親も独立照合済み。本件はこれらを第三者が理解・確認・利用できる、具体的な追加公開候補へまとめる仕事。応募項目を増やさず、未知文字や判読効果を主張しない。

新規の deliverables/vesuvius/november-workflow-supplement-20261113/ と同名ZIPを作り、実験根拠は experiments/vesuvius/bundle/20261113-followup-release01/ に保存する。既存の公開repo・凍結候補・149–160登録原票は不変。今回はローカル候補だけで、公開・PR・応募・外部メッセージを送らない。公開更新の判断を本人へ戻す場合は主担当が完成物を提示して行う。

内容は原則英語、冒頭に一般の研究者がわかる成果と範囲。三件の概要、先行公開との関係、追加の格子保持と固定上流の統合成功を示す。必要な製品差分四つ（154のR005二段、146のR009.patch、147のR007.patch）をそのまま収め、160で成功した順序 R005二段→R009→R007、固定commit、LFの条件、変更10ファイルの期待SHAを明示する。既存の検証済み差分を新しく書き直さない。大きい上流全ソース・ビルド・モデル・CT・mesh・全生ログは梱包せず、公式URL/入力ハッシュと小さい結果・実測図で再利用に必要な情報を残す。

研究154の22ファイル候補と同じ内容を無条件に複製せず、追加候補として一本の入口へ整理する。例えばREADME、REPRODUCE、EVIDENCE/範囲、DATA、SOURCE_HASHES、patches、必要な既存CLI/Pythonチェック、少数の証拠JSONと実CT比較図、既存ライセンスを用いる。実験原票にしかないC:/D:/homeの個人作業パスを、公開資料の実行前提にしない。原票に由来する数値は出所と原票SHAを記録し、公開用の抜粋と原本を区別する。必要な元資料へのリンクは梱包内か実在する公式/既存公開URLとし、未公開の研究フォルダへのリンク切れを残さない。PNGは研究152の実CT図を改変せず使える。生成文字画像や人間の実利用の装いは使わない。

再現案内では、普通のLinux/WSL ext4上の標準CMakeを入口にする。実測は既存Ubuntu依存を用いた固定版の構築であり、新OSからの全依存導入を検証済みとは書かない。159の旧基点と160の14d固定版を混同しない。通常Pythonパッケージ初期化・wheel、全アプリ/GUI、旧ABI差替えは未評価。追加モードは任意・既定off、旧pack/default挙動の検証と区別する。

R005は元40,944/254,263所有点保持と189/399露出、固定CT純粋支持14,080標本一致/混合1,280無効化、一成分対照、低keep元21,350保持/1,671露出/同成分競合177表面化を正確に扱う。低keepで同成分拒否件数不変を主張しない。R009の複数チャンク保持は既存skip動作も含み、R009固有の欠落階層救済と区別する。OS終了シグナル未確定、停電や途中チャンク破損耐性は未評価。三件の独立検証と統合160の結果を区別する。既存のライセンス（上流GPL/reader MIT/新規追加MIT/データ既存条件）を維持する。

検査はパッケージの内容・差分/図の元SHA・相対リンク・公開抜粋の数値対応・manifest/ZIPバイト一致を必要最小限で行う。製品再ビルドやnative試験、追加ネットワーク取得は不要。凍結差分をバイト一致で複写するなら、既に実行した適用・ビルドを繰り返す必要はない。実験フォルダに構築スクリプトや元→公開ファイルの対応、結果、費用0のlab候補を残し、親の別確認を待って凍結する。親側の月次一覧・応募文は主担当が更新する。個別成果を過度に検査・包装し直すことを目的にしない。

今回の委任は gpt-6.1-sol / high。研究154のパッケージ化の既存手順があり、今回は新たな研究実装を作らず、解釈しながら範囲・再現情報を整理するため。逐次で進め、subagentを作らない。

## 結論

［一次・パッケージ照合］三件の追加ローカル候補を作成。154のR005二段、146のR009、147のR007を160の成功順でバイト一致複写し、固定14d4e725の元blob・元SHA、途中SHA、最終10ファイルのSHAを収録した。最終SHAは主担当の160別照合とも一致。R005の格子保持・固定CT・一成分・低keep、R009の単一チャンクでの欠落配列救済と複数チャンク保持、159の旧基点ビルドと160の固定版統合を、それぞれ該当する原票SHAとともに示した。実CT図は152のバイトをそのまま収録した。 [候補README](../deliverables/vesuvius/november-workflow-supplement-20261113/README.md) · [差分と10ソースSHA](../deliverables/vesuvius/november-workflow-supplement-20261113/SOURCE_HASHES.json) · [結果抜粋](../deliverables/vesuvius/november-workflow-supplement-20261113/RESULTS.json)

［一次・ZIP］32ファイル、82,500 B、SHA-256 dda8b9f2c5ebc6e2d086db70b4cfe013a3e74545bcff1f3960dca4d3266e91b8。ZIPのCRCと全収録バイト、manifest、パッケージ内部32リンクを確認した。固定上流READMEの存在は保存treeで確認した。資料は標準CMakeの対象4ターゲットと実測制約、固定入力・CTのURL/ハッシュ、既存CLI/Python確認スクリプトと元ライセンスを含む。通常Python初期化・wheel、クリーンOSからの導入、旧ABI共有ライブラリ差し替え、紙面対応と判読は未確認。 [ZIP](../deliverables/vesuvius/november-workflow-supplement-20261113.zip) · [再現手順](../deliverables/vesuvius/november-workflow-supplement-20261113/REPRODUCE.md) · [作成・照合記録](../experiments/vesuvius/bundle/20261113-followup-release01/package-check.json)

既存公開版・凍結候補・登録原票は読み取りのみ。新規製品実行、ビルド、追加データ・コード取得、支出、公開・投稿・応募は0。主担当は公開更新案の準備のため、GitHub connectorで既公開READMEのみを読み取った。候補の公開可否は主担当から本人に提示する。 [元資料の対応表](../experiments/vesuvius/bundle/20261113-followup-release01/source-map.json) · [lab登録候補](../experiments/vesuvius/bundle/20261113-followup-release01/record.json)

## 主担当の別確認

パッケージのコピー23件、出典39件、内部リンク32件、固定変更10ソースのSHA、R005/R160の主要数値抜粋、ZIP全収録バイトを直接照合し一致した。R007の元公開リンクをcrop-guard/README.mdへ訂正した後の候補を採用する。親チェッカーの初回は一箇所の既定cp932読取で停止し、UTF-8指定後に成功。製品試験は増やしていない。[独立照合](../experiments/vesuvius/bundle/20261113-followup-release01/lead-check.json)。
