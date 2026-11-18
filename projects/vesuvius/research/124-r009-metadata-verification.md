Status: resolved
担当: 検証
Blocked by: 123

# R009: ピラミッド設定に合うOME参照と修正の結合を独立確認する

## 依頼

2026-11-13（日本時間）。研究123完了後、そのメタデータ修正とR007/R009との結合を作成担当とは別に確認する。研究122で確認済みの共通resume処理を全て繰り返す必要はない。

元版のpyramid無効出力がL0のみなのにOMEは0〜5を参照する根拠、変更後の通常/pre無効出力で参照が0だけになること、参照先にarray metadataが存在することを現物で確認する。--preはメタデータ作成のみなので、画素チャンクの有無を故障と扱わない。通常無効出力のL0は元対照と一致し、root属性はdatasets以外の既存意味を保持すること。有効時の通常・初回resumeは全14ファイルが元対照と一致すること。

製品差分、R007とR009と今回の差分の適用結果、実コンパイルソース・header・リンクされたR121 pyramid.oの対応を確認する。保存原票のデータ不要CLI回帰が結合バイナリを使い通過しているかも確認する。固定mainヘッダーの根拠は `experiments/vesuvius/r009/20261113-header-provenance01/result.json` にあり、GitHub blobとD:元ファイルが一致している。

新C:出力で、保存済み結合CLIの `--pre --pyramid false` を一度だけ再実行し参照先を確認する。追加ビルド・全再描画・新規デコーダ・Python実ビルドは不要。CPU1/AS4GiB/core0/network隔離、壁60秒、C:64MiB、D:と既存成果は読取、CT取得とクラウド支出0。モデル/effortはgpt-6.1-sol / high。固定結果の意味とコード・現物の照合が中心で新規設計を要しないため。追加subagent・外部送信禁止。

依頼を保ち、結論・根拠・範囲・資源を追記しresolvedへ。Python別添は実ビルド未確認のままと区別する。lab登録候補を返し、まとめ応募への採用は主担当が決める。

## 結論（2026-11-13 JST）

［一次］固定128×128・101層のZarr v2出力で、修正前の `--pyramid false` はOMEのdatasetsに `0`〜`5` を列挙し、実配列メタデータは `0/.zarray` だけだった。結合版の通常無効・`--pre --num-parts 2` 無効の両出力は、OMEの参照・実配列とも **`0` のみ**。通常無効のL0メタデータとチャンクは既存対照にバイト一致し、root属性は対照からdatasetsの `1`〜`5` だけを除いた内容だった。既定ピラミッド有効時の通常・初回resumeは、R120とR115の対照と **各14ファイル** のSHA-256が一致した。[独立検証結果](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/run-02/result.json)

［一次］保存結合バイナリの `--pre --num-parts 2 --pyramid false` を新規C:出力で一度だけ実行し、終了0。OMEはL0を参照し、参照先 `0/.zarray` が実在した。`.zgroup`、`.zattrs`、`0/.zarray` の3メタデータファイルは保存 `--pre` 対照とバイト一致。画素チャンクは0件で、メタデータのみを作る `--pre` の仕様どおりだった。[再実行の実物](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/run-02/disabled-pre.zarr/.zattrs) · [実行ログ](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/run-02/renderer.log)

## 根拠・範囲

- ［一次］製品差分はrendererの `writeZarrAttrs` に既存の `wantPyramid` を渡し、`omeMultiscales` の追加レベル数を有効時5、無効時0にする。単一partの通常出力と `--pre` の両呼出しを確認した。配列生成、サンプリング、画素書込の変更はこの差分にない。固定元ソースへの単独適用と、R007→R121→メタデータ／メタデータ→R007→R121の両順を新規C:コピーで照合した。結合ソース・ヘッダーは保存実コンパイル入力とバイト一致した。[製品差分](../experiments/vesuvius/r009/20261113-pyramid-metadata01/pyramid-metadata.patch)
- ［一次］実コンパイルとリンクのargv、renderer依存ファイルが指すC:変更ヘッダー、実オブジェクトと実行ファイルのSHAを照合した。借りたR121 `pyramid.o` は保存SHAと一致し、実ELFに3つの `createPyramidLevels` シンボルがある。D:の元 `zarr_write.hpp` は固定main `0080fa393724575d4f19059d91402757f9351b28` の保存GitHub原文と同じで、再計算したblobは `9b2e88c6189e326673b2bd979b57bbe2cc6c7057`。結合版で実行した保存R007回帰18件の診断・終了・回収票も照合した。[ヘッダーの版確認](../experiments/vesuvius/r009/20261113-header-provenance01/result.json) · [原票の独立照合](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/run-02/audit.json)
- ［推論］月次候補に記載できるのは固定fixtureのOME参照修正と、試験した通常・初回resume・`--pre` およびR007の動作維持。結合版の既存・中断出力へのresumeは再実行していない。共通resume処理の部分状態は研究122の確認範囲。Pythonバインディング実ビルド・実行は未確認で、研究125に引き継ぐ。追加デコーダや全描画を使わず、同一形式の画素はチャンクのバイト一致から確認した。[研究122](122-r009-resume-verification.md) · [lab登録候補](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/record.json)

## 検証資源

［一次］WSL Ubuntu、CPU 0、AS 4 GiB、core dump 0、ネットワーク隔離。追加ネイティブ実行は1回、壁2.18秒・最大RSS 59,776 KiB。最初の読取監査は空mergeの診断に含まれる作業パスまで一致と判定して停止した（4.72秒、CLI起動前）。診断の共通部分を照合するよう修正し、成功試行は監査とCLI込み7.69秒。計測壁合計12.41秒。新規Zarrは1,654バイトで、C:の検証作業は64 MiB以内。D:・既存成果は読取のみ。追加ビルド・全描画・CT取得・クラウド支出0。[実行・失敗・資源](../experiments/vesuvius/r009/20261113-pyramid-metadata-verification01/README.md)
