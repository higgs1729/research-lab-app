# R001: 3領域での再現と、修正経路の絞り込み

2026-11-11 JST、heartbeat時間枠996883。主担当登録はrunning、未決監査提案0件、重複する実験プロセスなしを確認。前回と同じw00セグメント内で、予測を見る前に選んだ離れた2領域を追加した。事前の選定と閾値は [計画JSON](../experiments/vesuvius/r001/20261111-multiroi-plan.json)。

## 再現結果

| ラベルタイル YX | 共通有効点 | 無補正 AUC | +19px AUC | +20px AUC |
|---|---:|---:|---:|---:|
| (8,44)、前回 | 7,597 | 0.960546 | 0.992378 | 0.991532 |
| (26,67)、今回 | 8,100 | 0.601115 | 0.898003 | 0.909535 |
| (27,51)、今回 | 9,601 | 0.804867 | 0.972185 | 0.967019 |

主担当の実験後にSol / highへ逐次委任し、前回の独立検証コードを入力指定可能にして適用した。HTTP本文からXYZ、ラベル・supervision全画素、予測値を再構成して一致。倍精度・全三角形再投影では2番目の領域の有効点が3点入れ替わるが、補正と無補正の順位は維持された。位相と幾何距離閾値の15条件でも両補正が無補正を上回った。中心点を取得済み26行・全幅で比較した範囲では、クロップ外の面へ切り替える根拠なし。[独立検証の条件と限界](26-r001-multiroi-verification.md)。

同じ領域内の点は相関があるため、25,298点を独立標本と扱う信頼区間は作っていない。3領域とも同じセグメントであり、別セグメントや未知文字の汎化検証ではない。19pxと20pxの優劣は領域で逆転し、これらのスコアだけでは画素原点の契約を確定できない。

[比較図](../experiments/vesuvius/r001/20261111-multiroi-comparison.png)は、同じラベル座標で各シフトの予測値を並べ、全列で同じ除外点を青く示した。表示時の画像位置調整はしていない。保存済みサンプルだけを使う [描画コード](../experiments/vesuvius/r001/plot_roi_comparison.py)も残した。Matplotlibが未導入だったため、既存Pillowで作成した。

## 公開コードと来歴の確認

GitHubコネクタで [issue #2442](https://github.com/ScrollPrize/villa/issues/2442) を再取得し、open・コメント0、更新日2026-11-04を確認。19pxと回避式は報告者の既知の成果。こちらの貢献候補は実利用できる修正であり、再現結果だけを新規成果とはしない。

当該 [Hecateグループ](https://vesuvius-challenge-open-data.s3.us-east-1.amazonaws.com/PHercParis4/segments/20260926044226-spiral-output-generation-19/ink-detection/PHercParis4-20260926044226-2.4um-0.22m-78keV-volume-20260411134726-20260915161132-hecate-9.6um-L2-l64-accmax4-reverse.zarr/zarr.json) は、元データを `s3://philodemos/sean/paris4_full_100226/ink/hecate/accum025_reverse/` と記載。`grid_transform` は元ストリップから180度回転したという文字列、OME multiscalesの各translationは0、縮小方法はmean。生成コマンド・生成コミット・画素原点は記載されていない。元S3の認証情報は探しておらず、取得もしていない。

調査対象の公開villaコードは `c86cbd14bb34e0124684d3d97b03b310c947819a` に固定した。全ファイルの木は取得したが全内容を調べたわけではない。GitHubのキーワード検索と以下の経路を確認した範囲では、当該Zarrの回転・公開処理を特定できなかった。

- [surface_orientation.py](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/spiral-fitting/surface_orientation.py) は節点格子を反転する。これだけでは元ラスターの画素位相は決まらない。
- [render_ink.py](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/spiral-fitting/render_ink.py) はメッシュ配置を扱い、CTからの描画を呼ぶ経路。公開Hecate Zarrを作ったコマンドとの対応は未確定。
- [InkDetectionOverlayController.cpp](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/volume-cartographer/apps/VC3D/overlays/InkDetectionOverlayController.cpp#L256-L310) は選択した画像をメッシュ節点数/画像寸法で拡大縮小し、grid00へ配置する。この関数では画素原点の平行移動を読んでいない。ただし、これは画像オーバーレイ経路で、対象Zarrそのものの表示・予測の読み出しと同一と確認できていない。ここへの一律19px補正は行わない。
- [FIT_NOTES.md](https://vesuvius-challenge-open-data.s3.us-east-1.amazonaws.com/PHercParis4/segments/20260926044226-spiral-output-generation-19/mesh/spiral-fit/FIT_NOTES.md) はフィッティングとatlasへの取り込み来歴を述べるが、調べた本文にHecate回転コマンドはない。

取得した原文は `experiments/vesuvius/r001/20261111-code-origin/` に保存した。これらから「公開リポジトリのどこにも生成コードがない」とまでは結論しない。

## 投入と次の判断

追加2ROIの主担当通信量は47,560,019 bytes。前回分との合計78,787,000 bytes（約75.14MiB）。別担当の今回検証は追加通信0。これとは別に公開ソース木1,851,702 bytesと小さいコード・メタデータを読んだ。初回資料調査の上限10MiBを含めても、初期の100MiB見直し点の内側。追加2ROIの取得は約15秒・12秒、比較は各約4秒。モデル作業時間をこれらの実行秒数には含めていない。有料計算の新規調達は0 USD、LLM利用・電力の総費用は未換算。

取得コードにタイル指定と旧HTTP本文の再利用を追加した。既存の計算条件は変えず、保存済み証拠ファイルも上書きしていない。各実行の入力・コード・出力とハッシュを保存する。

同セグメントの評価領域追加はここで止める。次は当該データの生成・公開経路か、既存読取APIへ正しい登録変換を渡す具体的方法に限定して調べる。追加調査は30分を見直し点とし、成果の利用先と修正差分が具体化しなければ、既知問題の再現としてR001を保留し、別の低支出課題へ切り替える。評価ツール単独の整備を続けない。有料計算も本人判断待ちも現在はない。
