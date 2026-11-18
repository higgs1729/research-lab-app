# w035の既知インク領域のCT描画対照

固定入力はPHerc0139 `20260317000000-w035_2026031718` の公開9.362 µm TIFXYZ全体、`20250728140407` のCT L0、20260918ラベル。公開キャンバスの0始まりXYで `(2176,1408)` から64×64。出力は `(layer, y, x)` の28×64×64、uint8、元の輝度。ラベルは `(y, x)` で、全4,096画素を監督対象とする。ローカル配列の `[:, j, i]` は公開の `[:, 1408+j, 2176+i]` に対応する。全28層とラベルを使っても既知訓練面の工程確認の範囲になる。[研究129](../../../../research/129-r012-known-ct-control.md)

- 元CT由来の値は `run01/native-roi.npy`、`run01/render/tiff/`、`run01/render/control.zarr/0/` に保存した。ZarrのL0は `0/.zarray` で読める。旧観測版の出力rootは `--pyramid false` でもL1〜L5を列挙する。上流独自属性 `chunk_size` も固定タイル寸法を記載するため、実チャンク寸法の読み取りには `0/.zarray` を使う。root属性は実出力の証拠として保存している。
- 直接取得した公開サーフェス値は `run01/public-roi.npy`。両出力の比較差と層別集計は `run01/comparison.json`、差の空間分布と元CT八近傍は `run01/audit.json`。公開版の画素が必要な下流試験には公開側の値を渡せる。
- `run01/plan.json` は取得前の固定条件とキー、`run01/http.jsonl` は一次本文の応答とハッシュ。`run01/geometry/geometry.bin` はCT画素取得前に既存ELFが出した6個のfloat64ヘッダー `(u0,v0,du,dv,w,h)` と、float32 XYZ・法線の各64×64×3。法線は反転前。反転を含むオフセットはplanに記載した。

## 保存CTを使った再実行

`C:/dev/kensyoukin` のPowerShellから実行する。`run03` は未使用タグにする。`run02` では同じ手順を実行し、ROI、座標、浮動小数出力、TIFF 28枚、L0チャンク、比較値など42ファイルが `run01` とSHA-256一致した。[再実行の照合](run02/replay.json)

```powershell
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$r012Relative = '../../r012/20261113-known-ct-control01'
$r012Wsl = '/mnt/c/dev/kensyoukin/experiments/vesuvius/r012/20261113-known-ct-control01'
$tag = 'run03'
function Invoke-R012Windows($stage) {
    python -B "$r103/run_windows.py" "$r012Relative/$tag/$stage-process.json" "$r012Relative/control.py" $stage $tag
    if ($LASTEXITCODE) { throw "R012 $stage failed: $LASTEXITCODE" }
}
function Invoke-R012Wsl($stage) {
    wsl -d Ubuntu --exec python3 -B "$r012Wsl/native_run.py" $stage $tag
    if ($LASTEXITCODE) { throw "R012 $stage failed: $LASTEXITCODE" }
}
Invoke-R012Windows roi
Invoke-R012Wsl geometry
Invoke-R012Windows plan
Invoke-R012Windows reuse
Invoke-R012Wsl render
Invoke-R012Windows compare
Invoke-R012Windows audit
Invoke-R012Windows confirm-replay
```

`reuse` は `run01` と同じplan・3本文・HTTP台帳を照合してコピーする。一次取得をやり直す場合の入口は `fetch`。今回の `fetch` は事前通知したキーのみを逐次取得した。`render` は `run*/ct.zarr` と完全なTIFXYZを入力にし、`unshare -Urn` 内で行う。CLI、元source、`libvc_core.so`、`libvc_reader_native.so` のハッシュは `run*/render/settings.json`。D:の既存ELF、WSL Ubuntuと既存Windows Python依存を再利用し、作業ディレクトリはC:の `.work/r012-known-ct-control01/`。Windowsの解析はR103 runner、ラベル読取はR001、CTバイト照会はR104の既存コードを使う。
