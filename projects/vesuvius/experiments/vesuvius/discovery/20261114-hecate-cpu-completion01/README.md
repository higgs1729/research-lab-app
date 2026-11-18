# Hecate CPU既知対照の完走

2026-11-14 JST。[研究196](../../../../research/196-hecate-free-cpu-completion.md)。R190が時間見通しで停止したPHerc0343の固定入力・Hecate 9.6 µmをCPU 1個で一回完走した。主比較はatlas XYWH `[1408,1088,256,256]`。公開Hecateと主要明部の位置は概ね対応したが、弧・囲まれた暗部の維持はこの切り出しで確認できなかった。

## 実行と照合

- 保存済みHecate revision `9cb86e500e944b11a06a7020403cde5dffb5bcb2`、`input.npy` 33×320×320、reverse 24→9の16層、64²・stride 32、fp32・batch 1で公式 `predict` 一回。R190のCPU環境を再利用し、R191/193の4資産とCPU3参照をSHA-256で照合した。主担当が実行前に資産・コードと条件を別確認した。 [固定SHAと入力条件](preflight.json) [主担当preflight](lead-preflight.json)
- 最初の3枚は入力の座標・raw/正規化SHA・supportがR190の事前期待値と一致し、予測12,288値も旧CPUとビット一致。残り78枚の予測376.482秒は残枠4,480.263秒内だった。全81枚について座標・入力SHA・support・確率・時間を保存した。 [最初3枚の原票](first-three.json) [全パッチ原票](patches.jsonl) [最終PNG](hecate-reverse.png)
- 主担当は81入力と331,776確率値を検査し、保存確率・support・Hannから再集約した320²の102,400画素が公式PNGに全値ビット一致することを確認した。 [独立検算](lead-verified.json)
- PID 38548は終了0。supervisor実測417.994秒、プロセスCPU時間361.641秒、peak RSS 1,283,129,344 B、commit上限4,294,967,296 B、実測最低空きRAM 14,448,824,320 B。厳密ロード1.380秒、パッチforwardの中央値4.823秒。最初3枚は今回4.571〜4.934秒、R190は44.817〜49.236秒。R190のプロセスCPU時間は36.719秒、経過184.106秒だった。混雑条件が異なる2回の実測比較である。 [資源実測](resources.json) [監視終了](supervisor-result.json)

## 原寸比較

保存CT中央層、R175のseed42・dense-native reverse、ローカルHecate・公開Hecateを同座標・固定0–255で並べた。公開Hecateとの画素一致4,573/65,536、MAE 36.239 DN、Pearson 0.688256。主担当もMAEと相関を独立計算した。箱9の交差範囲では上の明部が縦に伸び、下の明部との暗い分離が公開画像より弱い。箱10の左縁明帯は両方に見えるが切り出し外へ続く。既知字画の保存や改善を確認できず、公開予測との数値は同一面での再現性を示す。公開版とローカルの処理差の原因は今回判定していない。 [原寸図](comparison-256.png) [比較数値](comparison.json) [担当目視](visual.json) [主担当目視](lead-visual.json)

比較の初回は既定の `tifffile` からLZW codecを参照できず停止した。既存のR190依存先を使う入口で比較のみ再実行した。モデルforwardの再実行、新規CT取得、依存追加、GPU利用、外部計算費はいずれも0。 [初回原票](compare-process.json) [再試行原票](compare02-process.json)
