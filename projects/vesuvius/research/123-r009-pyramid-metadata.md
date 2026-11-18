Status: resolved
担当: 研究・実装（R123 Sol/high）
Blocked by: 122

# R009: ピラミッドを無効にした出力のOME参照を実配列に合わせる

## 依頼

2026-11-13（日本時間）。研究122で、研究121の `--pyramid false` 出力はL0のみなのに、root OMEのdatasetsがL0–L5を列挙すると判明した。元rendererのwriteZarrAttrsも同じ挙動で、再開修正の回帰ではない。別の項目として件数を増やさず、R009のZarr出力改善の中で修正する。研究122完了後に着手する。

既存のメタデータ生成能力を使い、実際のpyramid有効/無効に合わせた参照を書く。単一part通常出力と `--pre` の両方を対象とし、既定のピラミッド有効時のメタデータ・出力画素・再開動作は維持する。必要のないAPI変更や他のメタデータ整理はしない。

製品差分を元の固定ソースに対する独立した差分として保存し、R007のcrop修正、R009のresume修正と適用が共存することを確かめる。今回は可能なら3つを適用したrendererを一つコンパイルし、研究121のpyramidオブジェクトと既存ライブラリを再利用する。過去の実行・登録済み差分・元ソースは書換えない。

最初に保存した旧 `pyramid-disabled.zarr` で、メタデータが参照するpathと実際のarray metadataの有無を記録する。修正後は無効時の通常実行と--preで参照がL0だけになり、有効時の通常出力はR120/R115の14ファイル対照と一致することを確認する。L0画素は全条件で既存対照と一致すること。新規--resumeの成功、R007のデータ不要CLI回帰も結合版で必要最小限に確認する。--preの空チャンクは仕様なので、array metadataが存在するかと実画素の検査を混同しない。

元の固定入力と出力は研究120・121のC:ファイルとR115 CT。D:は読取のみ。CPU1、AS4GiB、core0、ネットワーク分離。コンパイル/リンク合計300秒、ネイティブ試験合計120秒、C:作業128MiB。追加データ取得・依存導入・クラウド計算なし。見積は追加クラウド0円。Pythonバインディングの実ビルドは本件には広げない。

モデル/effortはgpt-6.1-sol / highを選ぶ。原因と正常対照は確定しており、既存の描画設定をメタデータに反映する限定的な変更と結合検査であるため。追加subagent・外部投稿は禁止。依頼を保ち、修正前後の根拠・実行条件・限界・資源を追記しresolvedへ。別担当の独立確認と月次採用は主担当へ返す。lab登録候補JSONを用意する。

## 結論

2026-11-13 [一次・保存出力とネイティブ実行]。R121の保存済み `pyramid-disabled.zarr` は、OMEのdatasetsが `0`〜`5` を参照し、実在する `.zarray` は `0` だけだった。結合版では、`--pyramid false` の通常出力と `--pre --num-parts 2` の両方で、参照・実配列とも `0` だけになった。通常出力のL0復号画素は既存対照に一致。`--pre` はL0の配列メタデータを作成し、チャンクは作らない。無効時のroot属性は、参照をL0に絞った点以外も既定対照と照合した。[旧出力原票](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/old-pyramid-disabled.json) · [新出力原票](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/result.json)

既定の通常出力と新規出力先への初回 `--resume` は、R120/R115の既定対照14ファイルとSHA-256が全て一致した。L0〜L5の全画素を既存Bloscで復号して一致を確認した。R007のデータ不要CLI回帰18件も通過。今回の結合試験の再開条件は新規出力先で、既存・中断出力の検証は研究122の範囲。Pythonバインディングの実ビルドは本件の対象外。[試験結果と独立確認手順](../experiments/vesuvius/r009/20261113-pyramid-metadata01/README.md)

## 実装と資源

製品差分はrenderer内の `writeZarrAttrs` に既存の `wantPyramid` を渡し、`omeMultiscales` への追加レベル数を切り替える。配列生成と描画の既存処理を使う。固定rendererへの単独適用と、R007・R121に続けて適用した際の同一ソースを確認した。rendererのみコンパイルし、R121の `pyramid.o` を保存SHAで照合してリンクした。コンパイラ依存ファイルでC:の変更ヘッダー、ELFで再開に使うピラミッド関数を確認。主担当は元 `zarr_write.hpp` を固定mainのGitHub blob `9b2e88c6189e326673b2bd979b57bbe2cc6c7057` と照合した。[製品差分](../experiments/vesuvius/r009/20261113-pyramid-metadata01/pyramid-metadata.patch) · [ビルド条件](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/build-settings.json) · [元ヘッダー照合](../experiments/vesuvius/r009/20261113-header-provenance01/result.json)

ビルド113.286秒、ネイティブ試験110.074秒で、22試験プロセスを全て回収した。最大RSSはビルド1,585,221,632 bytes、試験96,710,656 bytes。C:作業量22,710,582 bytes。CPU0固定、AS 4 GiB、core dump 0、ネットワーク分離。D:は読取のみで、固定CT、対照、借用オブジェクトの一致を確認した。追加CT取得0 bytes、クラウド支出0円。ローカル電力とモデル利用費は未算定。独立確認と月次採用の判断は主担当へ返す。[ビルド結果](../experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/build-result.json) · [索引用候補](../experiments/vesuvius/r009/20261113-pyramid-metadata01/record.json)
