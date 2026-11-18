Status: resolved
担当: 検証
Blocked by: 121

# R009: 再開時のピラミッド補完と既存出力の保持を独立確認する

## 依頼

2026-11-13（日本時間）。研究121の実装完了後、作成担当とは別に、研究120で再現した新規・L0のみの `--resume` 失敗を直し、従来の正常な描画・再開・multi-part契約を保持するか確認する。依頼作成時点では実装中で、成功や月次採用は未認定。

固定した元ソース、製品差分、実コンパイルソースとバイナリの対応を読み、観測コードが製品へ混入していないことを確認する。既存writer/pyramidとの境界、既存メタデータ・チャンクの保持、欠落レベルだけの作成、resume時の形式・圧縮の扱い、pyramid無効指定とmulti-part/--pre分岐を確認する。R007との適用共存も保存証跡から確認する。広い新APIの設計審査や無関係な拡張は求めない。

旧版の通常対照・失敗原票と、修正版の新規通常・新規resume・部分状態・完成済みresumeを独立に集計する。各レベルのメタデータと実ファイルハッシュ、既存L0のSHAと更新時刻、OME属性を照合する。全ファイルが既存対照にバイト一致する場合に新しいデコーダを実装し直す必要はない。非圧縮データや異形式の対照は必要な範囲で確認する。無条件の削除や再フォーマットをしていないことが重要。

保存済み修正バイナリを使い、欠落した中間レベルからの回復など、主要分岐を一つ、新しいC:出力で再実行する。全ビルド・全描画の繰返しは具体的な不一致がなければ不要。別の回帰や不確実な境界が見つかれば事実と範囲を記録して主担当へ返す。

CPU1・AS4GiB・core0・ネットワーク分離、追加のネイティブ試験合計120秒、C:作業128MiB。D:・元成果は読取。新規CT取得・クラウド支出・ビルドなし。モデル/effortはgpt-6.1-sol / highを選ぶ。固定再現と実装原票に対する意味の照合・限定再実行であり、新規設計は不要なため。追加subagent・外部送信は禁止。依頼を保ち、結論・根拠・残る範囲・資源を追記してresolvedへ。lab登録候補を返し、月次採用は主担当へ戻す。

## 引継ぎ補足

研究121では共通処理のpreserveExisting overloadを追加した。既存3引数の呼出しとシンボルは維持。vc_reader/AGENTS.mdに従うPython入口・capability mapの変更は別添差分として保存される。復元UbuntuにはPython開発ヘッダー・nanobind・NumPyがなく、Python側の実ビルド/実行は今回未確認である。別添の既存呼出し/defaultの保持とC++への転送を読んで確認し、ネイティブ実験と区別して限界を記す。擬似テストを増やしたり依存導入へ広げる必要はない。

## 結論（2026-11-13 JST）

［一次］固定した128×128・101層のZarr v2・uint8出力で、旧版は新規 `--resume` とL0のみの `--resume` の両方で、L0を通常対照と同じ状態まで作成または保持したあと、L1欠落で終了1となった。修正版の新規通常、新規resume、L0のみ、初期化途中、完成済みresume、`--pre` 後のpart 0の6ケースは終了0で、各ケースとも元の通常対照の **全14ファイル** と実ファイルSHA-256が一致した。L0と既存配列メタデータのSHA・更新時刻も保存原票と実ファイルで確認した。[独立監査結果](../experiments/vesuvius/r009/20261113-resume-verification01/audit-01/result.json)

［一次］限定再実行では、gzipレベル7・ドット区切りのL0、無圧縮・スラッシュ区切りのL1、bloscのL3を新規C:出力にコピーし、L2を空ディレクトリにした。保存済み修正CLIを一度実行すると、L2・L4・L5がL0と同じ圧縮設定・区切りで作成され、全15ファイルが保存された混在対照とSHA一致した。既存L0全ファイルとL1・L3の既存メタデータはSHA・更新時刻を維持した。保存混在対照は、既存デコーダを用いた再比較で全6レベルの復号画素とOME属性が通常対照と一致した。[限定再実行](../experiments/vesuvius/r009/20261113-resume-verification01/replay-01/result.json) · [実行ログ](../experiments/vesuvius/r009/20261113-resume-verification01/replay-01/renderer.log)

## 差分と契約

- ［一次］製品差分をD:の元3ソースへ個別に適用し、C:の実コンパイルソース・ヘッダーにバイト一致した。実コンパイルとリンクargv、`.d` に記録された変更ヘッダー、実オブジェクト・バイナリSHA、リンク後の `createPyramidLevels` 3シンボルを照合した。観測版の目印を含まず、R007と両方の順序で適用して同じrendererになることも確認した。合成版はビルド・実描画の範囲外。[ネイティブ差分](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid.patch) · [独立監査結果](../experiments/vesuvius/r009/20261113-resume-verification01/audit-01/result.json)
- ［一次］既存の3引数入口は保持モードを `false` にして従来の `Writer::create` へ進む。単一part・ピラミッド有効のresumeだけが、保存L0のshape・chunk shape・dtypeを照合し、`createOptionsLike` によりL0の保存形式から欠落レベルを作る。保持モードは既存配列のshape・chunk shape・dtypeを照合して書換えを省き、`overwrite` を無効化する。ピラミッドの下位チャンクとroot OME属性を再計算する処理は共通であり、下位チャンクの更新時刻までは保持しない。今回の混在ケースで既存下位チャンクのSHAは一致した。[差分](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid.patch) · [保存混在の前後記録](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/mixed-codecs-resume-after.json)
- ［一次］multi-partはL0がない状態で `--pre` を要求し、`--pre` の原票はL0–L5の配列メタデータとroot属性だけ。描画は行を持つpart 0を確認した。`--pyramid false` はL0だけを保ち、L1以降の配列を作らなかった。ただし保存出力のroot OMEは存在しないL1–L5を列挙する。元と修正版で `writeZarrAttrs` の呼び出しと属性生成は同じであり、この不整合は今回の初期化修正の範囲外。[無効時の監査結果](../experiments/vesuvius/r009/20261113-resume-verification01/audit-01/result.json)
- ［一次］固定main `0080fa393724575d4f19059d91402757f9351b28` に結び付いた保存資料のGit blobと、D:のrenderer・`pyramid.cpp` の実バイトから計算したblobは一致した。`zarr_write.hpp` はD:の元・パッチ・実ビルドの対応を照合した。固定mainに結び付くヘッダーの保存原文・blob IDは調べた保存資料に見当たらず、ネットワークを切ったローカルGitにも対象commitがなかった。固定mainの全3ファイル一致は未確認。[版の照合と限界](../experiments/vesuvius/r009/20261113-resume-verification01/upstream-provenance.json)
- ［一次］Python別添も元ソースに適用し、保存された適用後ソースと一致。Python 2ファイルの構文を再確認した。更新後のPythonラッパーと拡張を組にした場合、`preserve_existing=False` が既定で従来のC++入口と `overwrite` を使い、`True` は保存L0を開いて保持モードへ渡す。開発ヘッダー、nanobind、NumPy等が不足し、拡張のビルド・pytest・実行は未確認。ネイティブの採用根拠と区別する。[Python別添](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid-python.patch) · [Python確認の原票](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/python-patch-check.json)

## 採用判断に使える範囲と資源

［推論］月次候補のネイティブ実績として、固定fixtureで再現した欠落階層の補完、既存L0・配列メタデータと出力画素の維持、通常・`--pre` 付きpart 0の確認を記載できる。Zarr v3、他のdtype・codecの全組合せ、実際の強制中断、複数partの並行実行、Python連携、現行main全ファイルとの一致は今回の実証範囲外。月次採用と索引登録は主担当に返す。[lab登録候補](../experiments/vesuvius/r009/20261113-resume-verification01/record.json)

［一次］WSL Ubuntu、CPU 0、AS 4 GiB、core dump 0、ネットワーク隔離。追加ネイティブ1回は壁6.56秒・最大RSS 65,696 KiB。準備を含む再実行8.93秒、読取監査21.09秒。C:出力Zarrは2,017,186バイトで128 MiB以内。元実行10本も期待した終了コードで回収済み。D:は読み取りのみ、追加ビルド・CT取得・クラウド費用0。監査と再実行は初回で成功。固定main確認用のローカルGit照会はオブジェクト不在で止まり、取得は行わなかった。[再実行資源](../experiments/vesuvius/r009/20261113-resume-verification01/replay-01/renderer-time.txt) · [監査資源](../experiments/vesuvius/r009/20261113-resume-verification01/audit-01/time.txt)
