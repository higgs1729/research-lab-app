Status: resolved
担当: 研究（R118 Sol/high）
Blocked by: 117

# R008: 次に試す、実利用につながる小改善を一件選ぶ

## 依頼

2026-11-13（日本時間）。本人の方針は、少ない支出で複数の小改善を締切まで積み上げ、11月のProgress Prizesへ一件としてまとめること。R005の成分配置は採用済み。R006の幾何再利用はサンプリングだけ改善したが通常処理全体の基準に届かず保留。R007はcrop指定漏れの修正を実装し、研究117で独立検証する。研究117完了後に本調査へ着手する。

次に扱う候補を最大3件へ絞り、最初に試す一件と小さい判定実験を提案する。目的はVesuvius解読に使われる既存ツールを改善することで、項目数を増やすために一つの入力検証を細分化したり、汎用の評価器・監査器だけを主成果にしたりしない。実利用者の困りごとと現在のコード、未解決issue/PR、公式ワークフローなど一次根拠を使い、現在も残る問題と既存修正の重複を確かめる。実ユーザー報告がない場合はその事実を明記する。

研究107の既存調査と、研究116・117までの成果と保留判断を参照する。同じ不採用候補やR005の終えた微調整を根拠なく再開しない。既存案を再評価するなら何が新しく変わったかを示す。再利用できる環境・資産はUbuntu 24.04、D:の既存Volume Cartographer source/build（読み取りのみ）、C:のR115固定CT小fixtureとR005の面。これらを使える候補は低コストだが、対象をそれだけには限定しない。

各候補について、一次資料と取得日時、現行版、問題の具体的な発火条件、既存解、想定利用者、最小再現に必要な入力、無料ローカルCPUで判定できることとできないこと、採用・停止条件を短く示す。有望な候補がなければ無理に実装案を作らず、その根拠を返す。新しい大規模依存導入・データ取得・ビルド・実験・GPU・有料計算・外部公開/投稿は行わない。この段階は次の一件を決めるための調査に限る。

新しい根拠は `experiments/vesuvius/r008/20261113-candidate-sources01` に保存する。原文は保存し、ツール出力に長いissue本文を丸ごと出さず必要箇所だけ返す。D:へ書き込まない。依頼を保持し、結論・根拠・限界・取得経路をこのファイルへ追記してresolvedにする。追加subagentは禁止。モデル/effortはgpt-6.1-sol / highを選ぶ。先行調査の方法はあり、現行コード・利用状況・費用の解釈が必要な候補選定であるため。採否・次の実験は主担当が決める。

## 結論（2026-11-13 JST）

今回の範囲で次に実装を勧める候補は0件。最も実利用の根拠がある #2370 では、公開HF65ラベルのずれを `full_3d` が補正せずに読む。一方、調べた26面の公開係数では、既存 `tifxyz_label_transfer` の寸法比と定数オフセットで一般の線形補正との差が0.47画素以内と見積もられる。まず既存ツールの適用対象と考え、一般のdrift対応は見送る。学習経路のずれや、現物を既存ツールで補正したときの一致は未検証。 [利用者報告](https://github.com/ScrollPrize/villa/issues/2370) · [原文と取得記録](../experiments/vesuvius/r008/20261113-candidate-sources01/sources.json) · [寸法と係数の照合](../experiments/vesuvius/r008/20261113-candidate-sources01/size-ratio-comparison.json)

### #2370 の実利用と現行経路

- ［一次・利用者報告］Paris4 `w01_20230702185753_r15` のHF65第32層を同スキャンCTと照合し、ラベルと同じキャンバス座標からTIFXYZまでのずれが位置依存だと報告した。報告者の別リポジトリには係数と補正実装がある。同じ利用者はw01の単一面を12,000 step学習した比較で、補正ラベルの主評価AUCが元ラベルより0.0937高かったと報告した（各4 seed、95%区間0.0641〜0.1233、同じ面の3領域）。当方による再現、改善量、他の面への一般化は未確認。 [報告コメント](https://github.com/ScrollPrize/villa/issues/2370#issuecomment-6700279804) · [報告者の補正](https://github.com/stantheman0128/vesuvius-hf65-alignment/blob/23f2451f1c5cb2012a240ab25323e15b9be82594/correct/apply_fit.py#L55) · [学習比較](https://github.com/stantheman0128/vesuvius-hf65-alignment/blob/23f2451f1c5cb2012a240ab25323e15b9be82594/labelshift-w01/RESULTS.md#L5)
- ［一次・現行コード］`main` は `0080fa393724575d4f19059d91402757f9351b28`。`full_3d` は対応するTIFXYZ領域と同じ添字でlabelとsupervisionを読み取る。#2447 はopenで、寸法が違うと警告する提案。別のdrift適用PRは検索範囲で見つからなかった。HF側のw01の三種のZarrレベル0メタデータは `65×65419×56889` で、現行の `.zattrs` は2026年4月のオブジェクト。再生成済みとする告知は確認できず、チャンク本体の更新有無は未確認。 [現行学習読込み](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vesuvius/src/vesuvius/ink_detection/data/dataset.py#L376-L427) · [形状警告 #2447](https://github.com/ScrollPrize/villa/pull/2447) · [メタデータと検索記録](../experiments/vesuvius/r008/20261113-candidate-sources01/search-results.json)
- ［一次・現行コード］既存transferは、元TIFXYZの格子座標を `label.shape / source.shape` でラベルラスター座標へ変換し、フル解像度で渡したoffsetをラベル画素へ換算して引き、境界を検査してfloorする。元と先に同じTIFXYZを指定し、フル解像度を `--output-shape` で明示して、用意した2D inkラベルとsupervisionを `--additional-label` で同時に渡せる。`w01` の公開係数から換算するoffsetの例は `--label-canvas-offset 11.451 11.569`（行・列の順）。これはフル解像度の既存座標変換に追加する定数。公開Zarrは3D配列なので、必要な2Dカテゴリ面をどの層・規約で切り出し学習入力に戻すかは利用側の別工程となる。同一面でのCLI通し、タイル境界・画素中心・floor・無効マスクの実挙動は確認していない。 [CLIの単位と換算](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vesuvius/src/vesuvius/tifxyz_label_transfer/transfer.py#L385-L401) · [ネイティブ索引](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vc_reader/src/cpp/projection/transfer.hpp#L54-L80) · [同時転送](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vesuvius/src/vesuvius/tifxyz_label_transfer/transfer.py#L1197-L1220)
- ［推論・係数の照合］公開係数は、HF65ラベル側のレベル0画素 `p=(y,x)` をTIFXYZフル解像度画素 `q=p+a+Gp` に写す。既存コードの寸法比を前向きで表した `D=diag(H/h,W/w)` とし、ラベル側中央 `c=(h/2,w/2)` で合う定数 `o=a+(I+G-D)c` を取る。既存の写像は `q≈Dp+o`、残差は `(I+G-D)(p-c)`。26面の公開表の行列をそのまま用いた四隅の最大L2差はw00で0.468、w01で0.258、w05で0.350画素。これは公開モデル同士の差であり、現物の登録誤差や離散ラベル画素の一致率とは別。w01の寸法 `65419×56889 → 65698×56669` が大きな傾きをほぼ説明する。公式推定器の `shift_field` は投影したソースレンダーと同じラスター上で中央基準・各軸1画素当たりの変化量を返し、承認経路は定数モデルが成立する場合を選ぶ。HF65の未正規化係数をこのdriftへ直結すると寸法比を二重に数えうる。 [公開係数](https://github.com/stantheman0128/vesuvius-hf65-alignment/blob/23f2451f1c5cb2012a240ab25323e15b9be82594/correct/shifts/shifts.json) · [推定器の係数](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vesuvius/src/vesuvius/tifxyz_label_transfer/estimate_canvas_offset.py#L110-L195) · [承認条件](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vesuvius/src/vesuvius/tifxyz_label_transfer/estimate_canvas_offset_evidence.py#L28-L40)

［推論・見直し条件］現行の寸法比＋定数を通した実データで、独立した位置が2か所以上で1レベル0画素超の残差を示し、位置依存補正だけが改善する場合に再評価する。その確認を別途行うなら、w01の報告者が係数のfitに使っていない1024×1024領域2つ（原点 `(13312,28672)`, `(31232,15360)`）を固定し、同じCT・HF65第32層・TIFXYZと、必要ならink/supervisionの窓と変換用余白だけを用いる。無補正、既存の寸法比＋定数、公開の線形モデルを同じ座標・NCC・有効域で比べる。別面での効果、学習AUC、全域I/Oは判定対象外。無料CPU1、4 GiB、処理120秒、入力の範囲取得は累計128 MiBを上限案とし、既存のPython環境と小さい窓を使えることが条件。WSL既定Pythonに `vc_reader` と `vesuvius` がなく、既存のネイティブ転送ビルドを借りられないならCLI試験は見送る。R115とR005の固定入力は別スキャン・別面で、w01のずれを評価できない。 [報告者が固定した領域](https://github.com/stantheman0128/vesuvius-hf65-alignment/blob/23f2451f1c5cb2012a240ab25323e15b9be82594/correct/regions_new_w01.json) · [報告者の窓比較](https://github.com/stantheman0128/vesuvius-hf65-alignment/blob/23f2451f1c5cb2012a240ab25323e15b9be82594/correct/RESULTS.md#L45-L53)

### その他の見送りと取得経路

`render_ink.py` のRAMとrenderer既定キャッシュは #2446 と #2411 の既存open PRが対象。`flatboi --inpaint` の実利用障害は #2476 に既存修正案がある。`vc_transform_geom` の節点ずれは #2243 の追記で、#2358の統合により当該経路が消えたと報告。PHercParis4 gen-19のhecate画像の19 pxずれは公開成果物への個別回避が報告されている。生成時の現行コードで同じ不具合が残る根拠が得られず、今回の実装候補から外した。R005の微調整、R006の計測条件調整、R007周辺の入力検証は追加しなかった。 [メモリ #2446](https://github.com/ScrollPrize/villa/pull/2446) · [キャッシュ #2411](https://github.com/ScrollPrize/villa/pull/2411) · [穴埋め #2476](https://github.com/ScrollPrize/villa/pull/2476) · [節点ずれの追記](https://github.com/ScrollPrize/villa/issues/2243#issuecomment-6541244201) · [hecate #2442](https://github.com/ScrollPrize/villa/issues/2442)

GitHub連携でissue・コメント・PR・枝・コードを調べ、`git ls-remote` でmainを確認した。固定refのrawソース、GitHub RESTのissue・PR、HFの小さなメタデータを取得し、URL・UTC時刻・SHA-256と該当するGit blobを保存した。画像・CT・ラベル画素の取得、ビルド、実験、学習、外部投稿はなし。追加クラウド支出0円、D:は読取り。lab登録は主担当に返す。 [取得原票](../experiments/vesuvius/r008/20261113-candidate-sources01/sources.json) · [登録候補](../experiments/vesuvius/r008/20261113-candidate-sources01/record.json)
