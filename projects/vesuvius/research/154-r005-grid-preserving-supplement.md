Status: resolved
担当: 研究（R154担当 2026-11-13）
Blocked by: 153

# R005: 格子保持の追加成果を再利用できるローカル配布候補へまとめる

## 依頼

2026-11-13。研究149–153で格子保持配置の成立性、既存C++での実装、別担当による全三角形照合、固定CT、別巻物の一成分対照まで揃った。新たな試験を増やす前に、別の開発者がどの差分をどのコードへ適用し、何が確認済みかを追える小さな追加資料にする。初期公開三件の内容・公開commitは凍結したまま、追加分はローカルのレビュー可能な候補に保存する。外部へ送らない。

成果は deliverables/vesuvius/grid-preserving-supplement-20261113/ の自己完結した資料とZIP、experiments/vesuvius/r005/20261113-grid-preserving-supplement01/ の作成・照合記録、本票の結果、lab候補JSON。現在の試作を変更せず、上流固定commit 14d4e725df8b569e6fc8ceb3c04d130f705c1565 から適用する差分の順序、pre/post source hash、必要な再ビルド対象、既定/旧pack/新packの使い方、確認済みの入力・条件・結果・限界を説明する。元R005差分とR150差分をそのまま同梱する方式でもよく、無用に別の実装や新しい検証道具を作らない。観測パッチを入れるなら製品差分と分離する。既存の再現資料とコードの再利用を先に見る。

実データの由来と元のライセンスを明示。R150のコメント修正とコンパイル済みコードの関係、同じクラス定義でflatboi呼出元/ラスター定義を作り直した隔離ELFであることを正確に残す。共有ライブラリだけの差替えを手順にしない。固定CT図は実データの比較図で、利用画面のスクリーンショットではない。物理紙面、文字判読、未検証のkeep<100/store等は主張しない。採用候補は三件のまま。公開済み原本を複製・再集計して第四の成果に見せない。

既存の入力URL・サイズ・SHA、短い結果表/CSV/JSON、固定CT図、ライセンス、差分、再現コマンド、ファイルmanifestで十分。大容量のCT・モデル重み・全観測trace・個人パスや内部運用指示を公開候補へ詰め込まない。実験資料を単に別フォルダへのローカルリンクで済ませず、同梱資料だけで主張と使い方が分かるようにする。プライベートなローカル環境への依存が残る再現箇所は隠さず明記し、一般の上流CMake構築手順と今回実際に行った隔離ビルドを混同しない。

照合は新しいC:作業先での差分適用とソース同一性、数値の登録済み根拠との対応、パッケージ内リンク/manifest/ZIPに限る。製品再実行・新ビルド・データ取得・依存導入・GPU・課金・外部公開/PR/メッセージ/応募・subagentはなし。D:読取、登録済み根拠は不変。親が別照合と採否を行うためlab登録はしない。

モデルgpt-6.1-sol、effort highを選択。既存成果を組み立てる手順はあるが、製品差分と観測/ビルド範囲、データ由来、公開可能な説明の切り分けに解釈が必要なため。

## 結論

［一次・適用］固定villa commit 14d4e725df8b569e6fc8ceb3c04d130f705c1565から、公開済みR005の元差分とR150の格子保持差分をC:の部分作業先に順に適用した。製品3ファイルは清書済みR150のSHA-256と一致。別添のflatboi観測差分とCT renderer観測差分も、それぞれの保存済み観測ソースを再現した。R150差分が引き継ぐ既存ログ行の行末空白1箇所で厳格なGitチェックは停止した。凍結差分のバイトを維持し、--whitespace=warnとLF指定で適用した。 [適用原票](../experiments/vesuvius/r005/20261113-grid-preserving-supplement01/application.json) · [ソースSHA](../deliverables/vesuvius/grid-preserving-supplement-20261113/SOURCE_HASHES.json)

［一次・既存証拠］独立検証の二面で元所有40,944/254,263点の元面とXYZビットを保持し、異成分拒否189/399→0/0、同成分拒否1/358は維持。固定CTの純粋支持14,080標本は全ビット一致し、元混合1,280画素の対応先は両領域で無効。一成分w035の既定/新フラグはXYZ・scale・energyが一致し、生成meta差はUUIDのみ。CT図は保存した実データから生成した比較図。紙面対応、判読、別の窓や描画法、keep<100、storeは未確認。 [短い結果原票](../deliverables/vesuvius/grid-preserving-supplement-20261113/RESULTS.json) · [比較図](../deliverables/vesuvius/grid-preserving-supplement-20261113/images/ct-preservation-center.png)

［一次・配布候補］適用順、LF指定、元/適用後ハッシュ、3モードの実行、CT入力URL・サイズ・SHA、元ライセンス、診断の使い方を同梱。隔離ELFはflatboi呼出元とラスター定義を同じ変更ヘッダーでコンパイルし直した実測品。R150のコメント修正前後でコメント除去後の前処理SHAは同一で、ビルド実物との関係を説明した。共有ライブラリ単体の差替えと通常CMakeによる新しい一式の実行は未検証。厳密な観測再集計は元の所有配列とローカル試験資産を要する。 [README](../deliverables/vesuvius/grid-preserving-supplement-20261113/README.md) · [観測と再現](../deliverables/vesuvius/grid-preserving-supplement-20261113/OBSERVATION.md)

ZIPは22ファイル・66,215 B、SHA-256 df7e8ed44897d9d1b02b6528c2681758eb4404d2a6e2af97bb8f39346cd0d926。全ファイルのバイトとCRC、相対リンク18件を確認した。初期公開三件と登録済み資料は読み取りのみ。この追加候補の外部公開、新規ビルド、ネイティブ実行、データ取得、追加クラウド支出はいずれも0。 [ZIP](../deliverables/vesuvius/grid-preserving-supplement-20261113.zip) · [照合原票](../experiments/vesuvius/r005/20261113-grid-preserving-supplement01/package-check.json) · [lab登録候補](../experiments/vesuvius/r005/20261113-grid-preserving-supplement01/record.json)

## 主担当の別照合

固定Git blobを別フォルダへ展開し、製品二差分と観測差分を順に適用してR150のソースSHAと照合した。初回はGit for Windowsの改行変換でCRLFとなったが、LF正規化後は全製品ソースが一致。初回ファイルと原因原票を保ち、別フォルダでautocrlf=false/eol=lfを指定すると製品・観測とも原バイト一致した。候補資料にもこの設定を明記済み。完成した22ファイル・18内部リンク・ZIP全バイト・結果表の登録原票対応・CT図同一性を別スクリプトで確認した。新規計算・ビルド・通信はない。[差分照合](../experiments/vesuvius/r005/20261113-grid-preserving-supplement01/lead-sources.json) · [資料照合](../experiments/vesuvius/r005/20261113-grid-preserving-supplement01/lead-package.json)
