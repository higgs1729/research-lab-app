# R005 配置とサンプリング格子の成立性

[研究149](../../../../research/149-r005-packing-grid-phase-feasibility.md)の再計算原票。研究99/100の二面のkeep100・5反復、配置off/on、元面と成分IDの対応を使用。`check.py` は既存の `grid_and_snap` と `fixed_point_weights` を読み込み、保存した全所有・拒否点で整数格子移動を照合する。新しい面や格子点を探索するラスターは使わない。

```powershell
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$relative = '../20261113-grid-phase-feasibility01'
python -B "$r103/run_windows.py" "$relative/run03-process.json" "$relative/check.py" run03
```

`C:/dev/kensyoukin` から未使用のタグで実行する。成功済みの `run02.json` には入力とソースのSHA-256、実UVピッチと成分ごとのずれ、二種類の整数UV対照、元の固定小数点での再配置、標準描画の1次元画素位相検査がある。`run02-process.json` が資源原票。`run01` はNumPy整数のJSON直列化で止まった初回。途中までの出力と実行原票を保持した。

## 固定条件と解釈

- 実測の写像は、座標ごとに元UVをdoubleへ昇格し、float32のbbox幅で割り、`N−1` を掛ける。保存された全頂点・bbox・格子寸法を照合した。元UVを実ピッチの整数倍で動かす対照は、Y移動0・同じ成分順。現行bboxの再計算を使う場合と、元affineを使い続ける場合を分けた。
- 固定小数点の対照は、元の格子で丸めた後にX方向の整数セルを加える。成分X区間の間隔は固定小数点で2セル以上を取り、元Yのキャンバス位相を維持。重なりで失われていた標本は、保存拒否も移動し、成分内の先着面順で選んだ。保存所有・拒否の補間ウェイトは移動前後でfloat32の全バイトが一致した。この対照の配列・画像は生成していない。
- 1次元画素位相検査は `render_scale=1`、標準128画素タイル、同じ `meta.scale`、無回転・無反転、全キャンバスのコード式。成分ごとの重なる整数画素範囲を算術比較した。CTや曲面補間を通した実画素比較は含まない。
