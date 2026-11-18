# w035の既知インク領域の公式CPU推論

[研究133](../../../../research/133-r012-known-ink-inference.md)の原票。公式model card指定 `koine_machines.inference.infer` を、villa `merge-ink-pipelines` のcommit `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` から実行した。原文は既存D:のGit objectからC:へ抽出した。重みは `scrollprize/ink_9um` commit `7109667e2607db1b90c37c8b09cb876ea7fe7bb1` の `hybrid_3d2d-seed42/step-075000.pth`。checkpointの固定SHAと処理ログは `checkpoint-http.jsonl` と `infer01/` にある。[公式コード](https://github.com/ScrollPrize/villa/blob/47a9c37f6f8e99afdab47bb46ad425aa726f5dc0/ink-detection/koine_machines/inference/infer.py) · [公式モデル](https://huggingface.co/scrollprize/ink_9um/tree/7109667e2607db1b90c37c8b09cb876ea7fe7bb1)

- `input.zarr` は公開L0の1チャンク、`0/0/11/17` をそのまま再配置したZarr v2。0始まりの公開XY `(2176,1408)` から128×128、9.362 µm。`[:,j,i]` の公開座標は `[:,1408+j,2176+i]`。左上64×64は研究129の公開対照と全値一致する。元CT側の64×64出力は使っていない。
- 推論は保存28層のうち0始まりの6〜22をforwardで使い、公式robust-MAD処理と128×128の1パッチを実行した。バッチ1、ワーカー0、0.5 overlap、Hann、TTAなし、compileなし、CPUの通常浮動小数演算。公開キャンバス全体の重なり推論とはパッチ境界の文脈が異なる。
- `infer01/probability.tif` は公式CLIの128×128 uint8 LZW出力。値は `floor(255*p)` 相当の量子化済みスコア。比較は固定ラベルのうち `supervision>0` の10,715画素のみ。評価の二値閾値は保存値128以上。`infer01/evaluation.json` に順位指標・混同行列・正負のヒストグラム、`infer01/comparison.png` に固定の比較図がある。

## 保存済み環境での再実行

PowerShellから `C:/dev/kensyoukin` で実行する。下のコマンドは既存Windows CPython 3.14と `.work/r012-known-ink-inference01/` の専用依存targetおよび保存checkpointを再利用する。実験時の推論は一回。再現時は新しいタグとログ名を使う。

```powershell
$r133 = 'experiments/vesuvius/r012/20261113-known-ink-inference01'
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$relative = '../../r012/20261113-known-ink-inference01'
$tag = 'infer02'
$python = (Get-Command python).Source
$arguments = @('-B', (Resolve-Path "$r103/run_windows.py").Path, "$relative/$tag-process.json", "$relative/run_local.py", 'infer', $tag)
$process = Start-Process -FilePath $python -ArgumentList $arguments -PassThru -WindowStyle Hidden -RedirectStandardOutput "$r133/$tag.stdout.log" -RedirectStandardError "$r133/$tag.stderr.log"
if (-not $process.WaitForExit(300000)) {
    $process.Kill()
    $process.WaitForExit()
    throw 'Inference exceeded 300 seconds'
}
if ($process.ExitCode) { throw "Inference failed: $($process.ExitCode)" }
python -B "$r133/evaluate.py" $tag
```

既存R103 runnerの1 CPU affinity・Windows job commit 4 GiB上限を利用し、TorchとZarrの並列設定を1にした。`run_local.py` は公式CLIをローカルパスで呼ぶ。HF offlineとPythonソケット監査を設定し、外部への接続と名前解決を拒否する。Windows asyncioの内部ループバックは許容する。checkpointのZIP内メタデータをロード前に確認し、追加backboneやURL参照がないことを記録した。

`setup_target.py wheels` と `setup_target.py checkpoint` は空の専用作業先で一次取得を再構成する入口。今回の保存先は既に使用済み。`wheel-plan.json` とHTTP原票を用いれば、保存済みwheelを新しいtargetへ `uv pip install --no-index --no-deps --no-build --no-cache --link-mode copy --target ...` で展開できる。公式宣言のZarr2/Python環境の厳密再現とは範囲が異なり、既存CPU Torch 2.14.0とZarr 3.1.5の環境でZarr v2データを読み書きした。`smoke03/result.json` に依存版、公式builder、全入力画素、前処理とLZWの無重み確認を保存した。
