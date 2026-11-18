Status: resolved
担当: 研究（R007上流準備、2026-11-13）
Blocked by: 146

# R007: 描画範囲ガードを現在の上流へ提案できる形にする

## 依頼

2026-11-13。R009の上流提案準備146に続き、公開済みR007の描画範囲ガードだけを現行ScrollPrize/villa向けに準備する。主担当の課題選定であり外部投稿は含めない。146で固定したmain 14d4e725df8b569e6fc8ceb3c04d130f705c1565のrendererは過去元版と同じ。対象箇所と凍結パッチを照合し、適用差分、既存の実CT試験との対応、現行の同等PRの確認、短い英語PR下書きと再現手順を残す。効果は不完全指定の早期拒否であり、全画素描画や料金節約を実測したと表現しない。

146と同じ作業の二件目で、既存手順がある。重複取得や再ビルド・既に合格した試験の再実行は不要。固定上流資料は146から参照可。現行版対象の変更がなければその事実を保存し、独自の一般化や機能追加はしない。人間の実利用/本人が書いた説明/本人確認checkbox/前後実画面は未充足なら空欄と明示し、代理で満たしたとしない。AIの研究としての再現と本人の体験を区別する。PRテンプレートとAGENTS/CONTRIBUTINGに従い、R009とR005を差分に混ぜない。短い再現手順は既存証拠を参照し、凍結資料は変更しない。

成果は本票とexperiments/vesuvius/r007/20261113-upstream-preparation01/、適用先は.work/r007-upstream-20261113/。D:読み取り、C:新規出力。新規CT/GPU/ビルド/導入/クラウド支出なし。外部fork/push/PR/issue/コメント/メッセージ・応募・公開repo変更・追加subagentなし。GitHubの小さい公式ソース/検索の読み取り可。研究146の登録済み原票・上流作業ツリーは読み取り専用扱い。

モデルはgpt-6.1-sol、effort medium。手順確立済みで対象一ファイルの適用確認と短い資料化のため。重要なコード差異や想定外が出たら、勝手に追加研究へ拡大せず原票と未解決点を戻す。lab登録候補を返し、主担当が最終確認する。

## 結論

［一次・Git］研究146で固定したvilla main `14d4e725df8b569e6fc8ceb3c04d130f705c1565` のrenderer blob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` に、公開済みR007の凍結差分をそのまま適用できた。変更は `vc_render_tifxyz.cpp` の11行追加・4行削除。C:の分離作業先で適用・逆適用・空白検査を確認し、LFに揃えた適用済みファイルは研究116で実際にコンパイルした製品ソースとバイト一致した。初回のWindowsの改行変換はローカルで補正した。現行main全体のビルド、既存試験の再実行は省略した。 [固定ソース](https://github.com/ScrollPrize/villa/blob/14d4e725df8b569e6fc8ceb3c04d130f705c1565/volume-cartographer/apps/src/vc_render_tifxyz.cpp) · [適用原票](../experiments/vesuvius/r007/20261113-upstream-preparation01/application.json) · [適用差分](../experiments/vesuvius/r007/20261113-upstream-preparation01/R007.patch)

［一次・上流］GitHubの公開PRを4条件で検索。各検索の総数は25・5・4・27、全件受領。近い6件の実差分は、レイヤー間隔の文書、ログ後処理、描画設定の記録とOME、先読み、回転・反転、法線補間だった。固定mainと検索した範囲に、不完全なmanual cropを入力を開く前に拒否する同等修正は確認できなかった。検索対象外の提案は未確認。 [検索原票](../experiments/vesuvius/r007/20261113-upstream-preparation01/search-http.txt) · [#1901](https://github.com/ScrollPrize/villa/pull/1901) · [#1905](https://github.com/ScrollPrize/villa/pull/1905) · [#2403](https://github.com/ScrollPrize/villa/pull/2403)

［一次・既存実CT］PHerc0814の観測版は、高さの指定を欠いたとき13,600×3,440の範囲を選択したところで停止した。製品修正版では不完全指定を入力オープン前に拒否。全指定時の128×128の実CT描画は3層とも保存対照とファイルSHA・復号画素が一致した。18件の独立回帰試験には無効指定9件、既定・原点・auto・help・merge経路を含む。全面の描画・転送量・料金削減は未計測。 [実CT試験](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/README.md) · [独立検証](../experiments/vesuvius/r007/20261113-crop-input-verification01/audit-02/result.json)

## 本人向け

幅や高さの指定が欠けたとき、広い範囲を処理し始める前に誤りを知らせる差分です。英語案には研究で得た前後の結果を記載し、本人の実利用例・本人が書く有用性・確認チェック・実画面は未記入です。上流の投稿条件を満たすには本人の作業が残ります。 [英語PR案](../experiments/vesuvius/r007/20261113-upstream-preparation01/PR_DRAFT.md) · [再現手順](../experiments/vesuvius/r007/20261113-upstream-preparation01/REPRODUCTION.md) · [固定版寄稿条件](../experiments/vesuvius/r009/20261113-upstream-preparation01/upstream-CONTRIBUTING.md)

適用先は `C:/dev/kensyoukin/.work/r007-upstream-20261113/`。2026-11-13 10:28–10:29 UTCのGitHub読取は公開PR検索と差分メタデータのみ。追加CT・GPU・ビルド・依存導入・支出・外部投稿0。 [lab登録候補](../experiments/vesuvius/r007/20261113-upstream-preparation01/lab-record.json)
