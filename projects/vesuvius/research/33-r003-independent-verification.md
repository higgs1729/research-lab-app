# R003 独立検証

2026-11-11。パッチ作成担当とは別の担当が、固定したソース・ビルド記録・保存済み4実行と、公開 PHerc0814 面 `20250929040153-auto_grown_20250929040153260` の入力を検証した。計測は保存TIFFの再読込と距離の全探索で行った。

## 差分と実行条件

- checkout は `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5`。作業ツリーの変更は `volume-cartographer/libs/flatboi/flatboi.cpp` の初期 `TC` の2軸への `stride` 乗算とコメントのみ。保存パッチの改行をLFにそろえると `git diff` に一致し、逆適用のチェックが通った。保存パッチはCRLFで、LFのソースに対して通常の `git apply --reverse --check` に渡すと失敗した。配布する差分にはLFを使う。 [保存パッチ](../experiments/vesuvius/r003/20261111-patch01/initial-uv-units.patch)
- `decimateGrid` が粗格子 `(r,c)` に置く点は元格子 `(r × stride, c × stride)` から来る。`meshGrid` の `cells` は渡された配列内の行・列。したがって全解像度の格子1ステップに対する `1/scale` を使うときの初期UVは `(c × stride / scale_x, r × stride / scale_y)`。入力の `scale ≈ [0.05, 0.05]` では元格子のステップは各軸約20 CT voxels相当、stride 8で約160。stride 1では元と同じ整数をfloatへ変換する。正常に構築された粗格子の有効行・列について積は元配列の範囲内、すなわち `0..rows-1` と `0..cols-1` のintで表せる。極端に小さい正のkeepでの `decimationStride` のfloat→int変換や、巨大格子での丸め上げ用 `dim + stride - 1` のオーバーフローは既存コードの条件として残る。 [初期化](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/libs/flatboi/flatboi.cpp#L899-L936) [格子化](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/src/SurfaceMeshing.cpp#L17-L56)
- WSL Ubuntu、GCC 13.3.0、QuickBuild `-O0` のCPUビルド。変更前の完了ログと既存のSLIM assemblyの36合成系を確認。生成ヘッダー201個の内容が原本へのincludeのみで、原本と転送側のSHA-256がmanifestと一致することを確認した。変更後のビルドログはflatboi.cppの再コンパイルと再リンクを記録。現存する両実行ファイルのSHA-256は各runの記録と一致。 [変更前ビルド](../experiments/vesuvius/r003/20261111-build02/state.json) [変更後ビルド](../experiments/vesuvius/r003/20261111-patch01/build.log) [assembly結果](../experiments/vesuvius/r003/20261111-header-debug/slim-assembly-result.json) [転送manifest](../experiments/vesuvius/r003/20261111-header-debug/forwarders-manifest.json)
- 入力の4ファイルは計1,110,638 bytesで、全サイズとSHA-256がmanifestと一致。4実行の終了コードは0。条件は `symmetric_dirichlet`、50反復、`tol=0`、affinity CPU 0。保存runnerはOMP、OpenBLAS、PaStiXを各1スレッドに指定し、W&Bを無効化。両keep=1.5のログはstride 8、50反復、PaStiX 1スレッドを確認できる。ログにある `hardware_concurrency=6` はスレッド設定値とは別。 [入力manifest](../experiments/vesuvius/r003/20261111-input01/manifest.json) [保存runner](../experiments/vesuvius/r003/run_flatboi.py)
- 4実行のstateに載る成果物40ファイルのサイズ・SHA-256はすべて一致。最初の変更前keep=1.5のrunnerは `output/` の4点だけを実行時のハッシュ対象にした。後のrunnerとの差は成果物一覧を作る1行。対象外だった同実行のログ・runnerなど8ファイルは今回のハッシュを結果JSONに記録した。 [初回state](../experiments/vesuvius/r003/20261111-runs/baseline_keep1p5_01/state.json) [検証結果](../experiments/vesuvius/r003/20261111-verification01/result.json)

## 保存TIFFの再計測

入力と出力の点の有効性は上流の `validSurfacePoint` に従い、全成分が有限、どの成分も `-1` でなく、z > 0。入力TIFFは162行 × 570列、有効点41,349。4頂点が有効な39,312四角形のCT座標の算術平均を求め、各中心から出力の全有効点までの3Dユークリッド距離の最小値を求めた。元の解析はcKDTree、独立検証は `scipy.spatial.distance.cdist` の二乗距離を中心256点ずつ全探索した。最大の距離行列は67,119,104 bytes。20と40の閾値はともに厳密な超過。 [点の有効性](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/vc_object_store/include/vc_object_store/geometry/Geometry.hpp#L80-L95) [検証コード](../experiments/vesuvius/r003/20261111-verification01/verify_saved_runs.py)

| 指標 | keep=1.5 変更前 | keep=1.5 stride補正 |
| --- | ---: | ---: |
| 出力行 × 列 | 157 × 402 | 157 × 548 |
| 出力の有効点 | 21,445 | 32,773 |
| 最近傍が20 CT voxelsを超える四角形中心 | 19,062 | 9,483 |
| 最近傍が40 CT voxelsを超える四角形中心 | 12,823 | 6,388 |
| 最近傍距離の中央値（CT voxels） | 18.29867 | 9.55323 |
| 初期L2(mean)、ログ表示値 | 8.25439 | 1.0318 |
| 最終L2(mean)、ログ表示値 | 1.00064 | 1.00064 |
| lift後にUVがなく除外された三角形（ログ） | 225 | 225 |

keep=100の出力は両方とも179行 × 556列で有効点40,684。3軸のTIFFを直接読み、各ファイルがバイト単位で一致することを確認した。出力の `meta.json` はUUIDが異なる。 [検証結果](../experiments/vesuvius/r003/20261111-verification01/result.json)

## 解釈と範囲

この一面のstride 8では、初期UVの単位補正により、出力点が近くにある入力四角形が増えた。初期化の仮説、stride倍の比較、18件の複数成分面と20件の単一成分面の比較はissue作者alpaltianの先行結果。今回確認した有効点数とL2の表示値は作者の主入力の報告を再現している。作者が報告した9,384 → 48は「UV上で縮退していない入力セルで、20 voxels以内に出力点がない」数。今回の分母は有効な入力四角形の全数で、粗格子化・liftの損失、縮退、ラスタライズの標本化などの影響が含まれる。 [issue #2500](https://github.com/ScrollPrize/villa/issues/2500) [主担当の比較図](../experiments/vesuvius/r003/20261111-coverage.png)

最近傍の計測は出力点の対応関係を追跡しないため、別の面片に近い点も拾い得る。四角形を面積で重み付けしておらず、重なり数、保存された実表面積、トポロジー、判読性の改善はこの結果から確定できない。SLIMの伸び指標は面ごとの変形量を集計する。最終L2(mean)は表示桁で同じだが、最終Area Errorは0.017604と0.0176075で、最適化結果の完全一致は示さない。パッチは成分間を分離する制約を追加せず、複数面が同じ出力セルに達したとき最初の面を採るラスタライズも続く。 [SLIMの伸び指標](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/libs/flatboi/flatboi.cpp#L374-L489) [ラスタライズ](https://github.com/ScrollPrize/villa/blob/7ad02f4f6e306b744ef6d2742dfe31fd55713ee5/volume-cartographer/core/src/SurfaceMeshing.cpp#L480-L500)

保存済み4実行の検証であり、バイナリの再ビルド・flatboiの再実行・追加の入力取得はしていない。別の面、stride、非等方scale、OBJ・GUI・store経路、最適化ビルドでの挙動や性能は未検証。外部投稿と追加の有料計算は行っていない。

作業ツリーとビルド成果を保持している環境では、リポジトリ直下から以下で検証結果を標準出力に再計算できる。保存済みJSONと入力・出力は上書きしない。

```powershell
python -B experiments/vesuvius/r003/20261111-verification01/verify_saved_runs.py
```
