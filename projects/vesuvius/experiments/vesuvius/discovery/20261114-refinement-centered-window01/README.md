# R183 中心化した採取窓

固定 `vc_objrefine` に JSON の `center_window: true` を追加した。明示時に限り採取原点を (P-r\,dx-r\,dy) として、評価画素 `(r,r)` を入力頂点上に置く。設定省略時は従来原点を使用する。[製品差分](build/center-window.patch)

省略のtifxyz 5出力はR182の全375 XYZ値と一致した。trueではr0反転対と一様平面の全XYZ値が一致し、r3反転対は中心変位が両方 +6.034847260 voxelになった。R182配置での差は5.999938965 voxel。OBJ A/r3でも同じ25点に明示+Zを与え、省略 +9.0348、true +6.0348 voxelを観測した。[tifxyz原票](trial/tifxyz-result.json) · [OBJ原票](trial/obj-result.json)

同じfixtureで再実行する場合は、`build.py`、`trial.py`、`isolate.sh` の3ファイルを同じ `discovery/` に新しく作った名前のディレクトリへコピーし、以下の `refinement-centered-window01-replay` をその名前に合わせる。WSL ext4の作業先は `/home/tomoy/<新ディレクトリ名>`（先頭の `20261114-` は省く）、C側原票は新ディレクトリ内の `build/` と `trial/`。既登録R182とR160を参照する。

```powershell
wsl -d Ubuntu --exec unshare -Urnm bash /mnt/c/dev/kensyoukin/experiments/vesuvius/discovery/refinement-centered-window01-replay/isolate.sh build
wsl -d Ubuntu --exec unshare -Urnm bash /mnt/c/dev/kensyoukin/experiments/vesuvius/discovery/refinement-centered-window01-replay/isolate.sh trial
```

今回の最初の製品は成功し、出力読戻しスクリプトのimport漏れでその後に停止した。保存済み出力を照合して読み戻し、未実行条件だけを起動した。実施した入口はtifxyzとOBJ。実紙面の補正、文字改善、応募採用は未評価。[実行条件](trial/input-contract.json) · [途中停止記録](trial/initial-readback-failure.log) · [研究票](../../../../research/183-refinement-centered-window.md)
