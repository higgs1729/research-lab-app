# R005 再現手順

## 適用確認

PowerShellで固定 main の元ファイルをindexに置いたC:の部分作業ツリーを確認する。対象は volume-cartographer/libs/flatboi/flatboi.cpp。

~~~powershell
$w = 'C:/dev/kensyoukin/.work/r005-upstream-20261113'
$p = 'C:/dev/kensyoukin/experiments/vesuvius/r005/20261113-upstream-preparation01/R005.patch'
git -C $w apply --cached --check --whitespace=error $p
git -C $w diff --check
git -C $w diff --stat
git -C $w apply --reverse --check --whitespace=error $p
~~~

将来手元で実行する場合は、固定SHA 14d4e725df8b569e6fc8ceb3c04d130f705c1565 の完全なソース作業ツリーで配布手順どおりにパッチを適用し、設定済みビルドの flatboi を使用する。前後で別々の新規出力先を指定する。この研究では実行していない。

~~~sh
git -C "$VILLA_SOURCE" apply --check "$R005_PATCH"
git -C "$VILLA_SOURCE" apply "$R005_PATCH"
cmake --build "$VILLA_BUILD" --target flatboi --parallel 1
"$VILLA_BUILD/bin/flatboi" "$SEG" --output="$BEFORE" --keep=100 5
"$VILLA_BUILD/bin/flatboi" "$SEG" --output="$AFTER" --keep=100 5 --pack-components
~~~

二つの PHerc0814 入力のID・URL・SHA-256と、観測ビルド・集計コマンドは凍結資料にある。前後は元面IDと成分で追跡する。格子の幅と位相が変わるため、同じ画素番号の差分では評価できない。観測は別の差分・バイナリで行われ、通常の製品ビルドも第一面で実行確認済み。 [実行と計測の手順](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/flatboi/README.md) · [入力台帳](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/flatboi/inputs.json) · [独立検証](../../../../research/100-r005-pack-native-verification.md)

## 保存済みの図とCT条件

- 所有図の色は格子を所有する元成分で、赤は異成分拒否。画像は観測記録から作った比較図。 [成分所有図](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/flatboi/images/component-ownership.png)
- CT中心比較と元CT断面は第一面の元面53045と63364に沿う。9.362 µmの元CT、64×64の3 ROI、5層。前と後の別ROIで、両成分の頂点を使う補間を1280→0/0画素と測定した。画面撮影ではなく、既存rendererの観測出力と元CTから生成された図。 [CT中心比較](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/ct/ct-center-comparison.png) · [元CT断面](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/ct/ct-source-sections.png) · [固定切り出しと描画コマンド](../../../../deliverables/vesuvius/november-workflow-improvements-20261113/component-packing/ct/README.md)
- 成分2の物理的な紙面対応は未確定。研究144/145の固定近接ラベル候補から、異成分混合の影響を判読で比較できる対照は得られなかった。 [CT独立検証](../../../../research/104-r005-ct-render-verification.md) · [ラベル候補の位置確認](../../../../research/145-r005-label-candidate-affected-region.md)
