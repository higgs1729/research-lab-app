# R005：flatboiの成分配置パッチの独立検証

2026年11月12日 JST。検証対象は既定offの `--pack-components` を追加した一ファイル差分と、PHerc0814の二つの保存済み実入力。元の記録から差分、ビルドと実行条件、入力・UV・描画出力を照合した。[主報告](99-r005-pack-native.md) · [検証コード](../experiments/vesuvius/r005/20261112-pack-native-verification01/verify_saved.py)

## 差分と呼び出し

配布パッチをLF原版へ独立に適用し、製品ソースの全バイトを再現した。原版のGit blobは `2dcf5981008e6b68b8c29ef7e083fc769f40e163`。手元のvilla Gitでbase `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5` と当時参照したmain `f0e441016900cb946bc3861025eca3a7cc2aae19` が同じblobを指すことを確認した。既存のstride処理は差分に含まれない。libiglの `vertex_components` は面の頂点接続から成分を作り、未訪問の最小元頂点からIDを振る。fineメッシュ生成は有効quadの角だけを登録するため、この呼び出しでは全UV頂点にラベルがある。安定ソートは元fine頂点数の降順で、同数時にその成分ID順を保つ。[製品パッチ](../experiments/vesuvius/r005/20261112-pack-native01/pack-components.patch) · [適用検査の状態](../experiments/vesuvius/r005/20261112-pack-native01/edge-checks02/state.json)

変更位置はSLIM・細UV転写・既存の有効面選択の後、`setMesh` の前。元面とコーナーUVは同じ頂点IDを使う。配置bboxは既存の有効面リストのうち全コーナーUVが有限の面から作る。描画対象成分の有限かつ有効なUVをdoubleで平行移動し、float32に戻す。観測した全ケースの有効UVは有限で、配置bboxに使う面とラスタライザーへ渡す面は一致した。有限かつ正のソースscaleのときX方向の名目間隔は `2.0 / scale[0]` UV単位。ソースscaleを設定しない分岐では間隔は2 UV単位で、既存描画器の既定は概ね1 UV単位あたり1セル。実出力はbboxから丸めた格子全幅へ写すため、間隔は名目値である。非有限のscaleやfloat32変換後の非有限UVを持つ入力での挙動は、今回の実行証拠の範囲外。製品の有限判定は配置bbox用で、既存ラスタライザーの入力検証の代わりにはならない。[製品ソース](../experiments/vesuvius/r005/20261112-pack-native01/flatboi.cpp)

既定offは `Options` とCLIの初期値で確認した。フラグの分岐を外れた場合は元のUVをそのまま描画へ渡す。ローカルtifxyzとストアのusageにフラグがあり、共通の `Options` を両モードへ渡す。ストア経路では `parameters(opt)` がbooleanを含めて `store.create` に渡す。実際のストア書き込みは今回の検証対象外。[製品help](../experiments/vesuvius/r005/20261112-pack-native01/cli-help01/stdout.log) · [ストア呼び出し](../experiments/vesuvius/r005/20261112-pack-native01/flatboi.cpp#L1058)

観測パッチを製品ソースへ適用して計測版を全バイト再現した。追加箇所は環境変数で有効になる配置前のUVコピーとSLIM・細メッシュ配列の出力。保存したコンパイル・リンク引数をCMake生成引数と突き合わせ、別ソース／オブジェクト／出力名への差し替えと、計測版だけの既存ラスタ観測オブジェクト追加を確認した。既存ソース、build設定、バイナリ、リンクライブラリは保護ハッシュと一致した。[観測差分](../experiments/vesuvius/r005/20261112-pack-native01/diagnostic-only.patch) · [製品ビルド](../experiments/vesuvius/r005/20261112-pack-native01/build-product01/state.json) · [計測ビルド](../experiments/vesuvius/r005/20261112-pack-native01/build-trace01/state.json)

## 二つの全解像度入力

元TIFFの全四隅有効quadから頂点順・二三角形の順・元XYZ・成分を再構成した。第一面は41,349頂点・78,624面・39,312 quad・5成分、第二面は249,944頂点・478,224面・239,112 quad・9成分。両入力の成分移動と全配置後UVを独立に再現した。第一面の全78,624面は配置前後とも正の向きで、3D面積加重の正規化SDをGram行列から計算した。元quad中心から同成分の全出力標本への距離を分割総当たりで調べた。所有記録から固定小数の内包判定とXYZ補間を再現し、配置前40,944点・配置後41,149点のTIFF XYZがすべてビット一致した。記録された全拒否でも、両面が同じ画素を覆うことを確認した。[検証結果](../experiments/vesuvius/r005/20261112-pack-native-verification01/check01/result.json)

| 指標 | 第一面 配置前→後 | 第二面 配置前→後 |
| --- | ---: | ---: |
| 出力格子 y×x | 172×553 → 172×680 | 252×2637 → 252×3027 |
| 有効出力点 | 40,944 → 41,149 | 254,263 → 254,668 |
| 全描画拒否 | 190 → 1 | 757 → 356 |
| 別成分間の拒否 | 189 → 0 | 399 → 0 |
| 別成分をまたぐ有効格子辺 | 106 → 0 | 284 → 0 |
| 自面標本0の元quad | 2,855 → 2,624 | 13,424 → 13,100 |
| 元quad中心の同成分距離 >20 voxel | 167 → 0 | 485 → 202 |
| 同 >40 voxel | 87 → 0 | 205 → 82 |
| 同最大距離 voxel | 110.972630 → 15.976095 | 118.265996 → 71.726938 |
| 面積加重正規化SD | 1.00193546111065 → 1.00193546112089 | 1.00145941973236 → 1.00145942224834 |

第一面は閾値20以内への回復167件、新規20超0件。配置前の拒否190件は190ユニーク元面ペアで、すべて元頂点を共有せず、保存float32を整数化した厳密SATで正面積交差と判定した。配置後の1件も、元面16500と17195（0始まり）が同成分で元頂点を共有せず、連続UV上で正面積交差した。配置前に観測された同成分内の1件は別ペアの13716と15107。配置は格子幅・格子位相を変えるため、拒否件数が同じでも同じ交差の標本とは限らない。既定offの製品原版／計測版、onの製品版／計測版のそれぞれで3枚のTIFFがファイル単位で一致し、4実行のSLIMエネルギーも同一だった。[第一面の配置前配列](../experiments/vesuvius/r005/20261112-pack-native-verification01/check01/first-before.npz) · [第一面の配置後配列](../experiments/vesuvius/r005/20261112-pack-native-verification01/check01/first-after.npz)

第二面は配置前の全UVと粗SLIM配列を凍結済みの実行に、配置後の全UV・描画トレースの全フィールド・3枚のTIFFファイルを凍結済みのPython配置と描画に照合した。関連する凍結10ファイルのハッシュを確認したうえで、独立再計算済みの全239,112セル評価を引き継いだ。閾値20以内への回復288件、新規20超5件、共通197件。残る同成分356件は前回の保存拒否ペアの厳密交差分類に対応する。二面とも交差の判定範囲は描画拒否ログに現れた元面ペアである。[前回の独立検証](98-r005-full-resolution-verification.md) · [今回の第二面実行](../experiments/vesuvius/r005/20261112-pack-native01/second-trace-on01/state.json)

## 部分有効UVと補助検査

第一面のkeep1.5はstride8。保存済み粗UVから三角形内補間と既存の近傍頂点転写を再現し、無効103頂点と全有効UVを照合した。有効面フィルタによる225面除外を保ち、配置可能5成分のうち4成分が標本を持つ。格子155×617・出力23,003点のXYZビットを照合した。11,522拒否はすべて同成分内で、全拒否で両面の画素内包を再現した。部分有効UVの連続交差は分類していない。[低keepの検証配列](../experiments/vesuvius/r005/20261112-pack-native-verification01/check01/first-low.npz)

製品から抽出した関数と第一面の実UVを使う補助検査は、描画対象0・1成分で全UV不変、2成分で35,435・289頂点が変化し対象外は不変。配置後bbox間隔はソースセル単位で2.0000000298。初回は配置後UVを読み、配置済みの成分も必ず動くことを要求したため終了コード134で失敗した。配置前UVを使う修正版で、間隔と対象外不変を確認した。製品ソースは両補助検査で同一だった。[失敗した初回](../experiments/vesuvius/r005/20261112-pack-native01/edge-checks01/checks.log) · [訂正後](../experiments/vesuvius/r005/20261112-pack-native01/edge-checks02/checks.log)

## 資源と再現性

製品側の凍結manifestのrepo 145件、外部Dドライブ10件を全照合した。記録上の20プロセスは時刻上重なりがなく、失敗は初回補助検査の1件。全6入力実行のSLIMログで明示5反復・tol0・進捗0〜5とエネルギー6値を確認した。Windows評価を除きCPU1・各スレッド1・300秒・AS4 GiBで、最大子RSSは計測版のコンパイル1,563,000,832 bytes。独立検証は保存物の読み取りと数値照合をCPU1・数値スレッド1のbounded Python一回で実行し、86.360秒・観測ピークRSS808,067,072 bytesで完了した。独立検証での再ビルド、SLIM・native再実行、外部取得、GPU、有料計算は0。[製品側資源記録](../experiments/vesuvius/r005/20261112-pack-native01/resources.json) · [凍結manifest](../experiments/vesuvius/r005/20261112-pack-native01/artifact-manifest.json) · [独立検証の実行状態](../experiments/vesuvius/r005/20261112-pack-native-verification01/check01-execution/state.json)

## 配布説明

検証した入力経路と動作範囲で製品パッチに修正が必要な問題は見つからなかった。READMEのパッチ適用から実行までの例には、対象の `flatboi` ターゲットを再ビルドしてその実行ファイルを指定する手順が必要。PR下書きは自動計測を明記し、人間の利用・レビュー・本人の記述を求めるチェック欄は空欄のまま。libiglの既存実装を使う点を明示し、元のstride補正の出典は主報告にある。二つの保存入力で測定した範囲に同成分内の拒否と欠標本が残る。全域の連続UV交差、大規模性能、判読性は今回の評価範囲外。[README](../experiments/vesuvius/r005/20261112-pack-native01/README.md) · [PR下書き](../experiments/vesuvius/r005/20261112-pack-native01/PR_DRAFT.md)
