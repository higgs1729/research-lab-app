Status: resolved
担当: 研究（R009上流準備、2026-11-13）
Blocked by: 145

# R009: 現在の上流コードで再開・OME修正を提案できる形にする

## 依頼

2026-11-13。公開済み三件のうちR009を深掘りし、実用される可能性を高める。R121–125の修正とR131/132の実CT中断状態からの再開証拠を基に、現在のScrollPrize/villaへ適用可能な具体的な提案差分と再現手順をローカルに用意する。現行mainをSHAで固定し、同等修正や重複PRの有無、適用可否、変更済みコードと試験済みコードの一致/差異を確認する。範囲はR009のみでR007/R005を混ぜない。現在も同じ実装なら新たな全体ビルドや無意味な再試験はしない。適合のため実装変更が必要なら、その部分に応じた検証を行う。

成果は研究票、C:の分離した適用先/差分、英語PR本文案、再現コマンド、検証範囲と未確認事項、lab登録候補。本人が読める短い説明も添える。資料は現在の上流AGENTS/下位AGENTS/CONTRIBUTING/PRテンプレートに従う。上流はAI提案に人間自身の利用・人間が書いた有用性の説明、本人による検証のチェックを求めている。ユーザー本人が使った・書いた・レビュー済みと装わない。本人文/本人確認は空欄のまま、その不足を明示する。比較の実行結果は保存ログを正確に示し、過去のSIGKILL未確定をクラッシュ耐性と呼ばない。要求される画面は未取得なら未取得とし、ログを加工した絵を端末スクリーンショットと呼ばない。

新規外部PR、fork/push、issue、コメント、応募、連絡、公開repo変更は行わない。公開済み凍結成果物・登録済み原票は変更しない。D:読み取りのみ、新規作業C:。現行公式GitHubの小さいソース/メタデータ取得は可。既存ソースオブジェクト/ビルド/依存/実入力を優先し、再インストールや大規模clone/取得/全体ビルドは不要。課金・GPUなし、CPU計算は1CPU/4GiB、必要なら600秒以内の対象部分検証まで。手順のためだけの新規独自道具は作らず、Gitと既存確認スクリプトを使用する。追加subagentなし。新出力はexperiments/vesuvius/r009/20261113-upstream-preparation01/、ローカル適用先は.work/r009-upstream-20261113/。

担当モデルはgpt-6.1-sol、effort high。検証済み修正の現行上流への適合と、既存証拠の限界を解釈して簡潔にまとめる仕事のため。採否・外部送信の判断は主担当/本人が行う。

## 結論（2026-11-13 JST）

［一次・Git］ScrollPrize/villa の main を 14d4e725df8b569e6fc8ceb3c04d130f705c1565 に固定した。R009対象7ファイルの元blobは前回固定の0080fa393724575d4f19059d91402757f9351b28と全て同じ。凍結候補3パッチのSHA-256を原票と照合し、C:の部分作業ツリーにそのまま適用した。合成差分は7ファイル、70行追加、14行削除。indexでの適用、作業ツリーでの逆適用、空白チェックが通った。R005とR007は差分に含めていない。上流のサブプロジェクト別の分割指針に合わせ、vc_readerの共有処理・Pythonと、それを使うrendererの二つの差分も用意し、両方を適用順で確認した。[適用原票](../experiments/vesuvius/r009/20261113-upstream-preparation01/application.json) · [合成差分](../experiments/vesuvius/r009/20261113-upstream-preparation01/R009.patch)

［一次・上流］現行対象コードに等価な変更は見つからなかった。公開GitHub検索5条件で、近縁のPRはTIFFスライスの復旧、CT取得時のエラー、回転・反転、別ツールのOME出力や検査だった。調べた公開範囲に、単一part Zarrの欠落レベル補完やピラミッド無効時の対象rendererのOME修正と同等の提案はなかった。[固定上流ソース](https://github.com/ScrollPrize/villa/tree/14d4e725df8b569e6fc8ceb3c04d130f705c1565) · [検索条件と確認したPR](../experiments/vesuvius/r009/20261113-upstream-preparation01/duplicate-search.json)

［一次・実行原票照合］R123/R131/R132で使ったELFの共有C++ピラミッド実装とヘッダーは今回候補とSHA-256一致。rendererのコンパイル元はR007も含む。C:の比較コピーでR007だけを逆適用すると今回候補と一致した。R125の実バインディング、Python wrapper、回帰テストと共有C++は候補とSHA-256一致。実装調整が不要だったため、現行mainからのビルド、既存試験の再実行は実施していない。現行main全体と既存の依存バイナリの同一性は未確認。Pythonの通常初期化、wheel、pytestランナーも未確認。[R123ビルド](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/build-settings.json) · [R125実行](../experiments/vesuvius/r009/20261113-python-validation01/run01/test03/checks.json)

［一次・既存実CT］PHerc0139 w035の64×64×28層で、実描画をデバッガで停止した二状態から、結合版は正常描画の14ファイル、全6層の画素とOME参照に一致した。既存8件・2件は再開用コピー上でSHA・mtime・inodeを保持。L0メタデータだけの同一状態から修正前版はL0画素を書き、L1不在で終了1。ピラミッド無効の別試験では結合版の通常描画と --pre がいずれもL0だけをOMEに記録した。製品のOS終了シグナル、チャンク途中破損、停電、複数partからの復旧は未確認。[R132独立比較](../experiments/vesuvius/r009/20261113-interrupted-verification01/run01/result.json) · [R123 OME出力](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/result.json)

## 本人向け

描画をやり直すときに、作成済みのZarrレベル0を利用し、欠けたピラミッド配列を補える差分が現在の上流にも適用できた。現行ルールに従うには、本人が実際の巻物作業で使い、役立つ理由を自分の言葉で書き、修正前後を確かめて実画面を添える必要がある。英語案の本人記入欄と確認欄は空欄で、画面は未取得。保存済みの実CTとログから同条件を再現できる。上流に出す候補そのものの確認には固定mainの修正前後のビルドが要る。[英語案](../experiments/vesuvius/r009/20261113-upstream-preparation01/PR_DRAFT.md) · [再現手順](../experiments/vesuvius/r009/20261113-upstream-preparation01/REPRODUCTION.md) · [固定版の寄稿条件](../experiments/vesuvius/r009/20261113-upstream-preparation01/upstream-CONTRIBUTING.md)

適用先は C:\dev\kensyoukin\.work\r009-upstream-20261113。公開GitHubの小さいソース、規約、Gitメタデータのみを読み取った。ソースとGitツリーの保存本文は2,630,865 bytes。追加CT、ビルド、試験、クラウド支出、外部投稿は0。凍結済み資料は読み取りのみ。[lab登録候補](../experiments/vesuvius/r009/20261113-upstream-preparation01/record.json)
