# R245 ピラミッド無効の実reader比較

[研究票](../../../../research/245-r123-reader-impact.md)の2026-11-16実行。readerが返した状態、画像配列、診断を [vc.log](vc.log) と [ome.log](ome.log) に保存した。例外はログに出し、後続の対照も読めるように捕捉している。プロセス終了0は全ケースを観測できたことを表す。

## 固定入力

| ケース | 内容 |
| --- | --- |
| `saved-old` | R121の保存 `--resume --pyramid false` 出力。L0を播種した試験でrootの `.zgroup` が無く、`.zattrs` は0〜5を列挙 |
| `saved-fixed` | R123の保存 `--pyramid false` 通常出力。rootの `.zgroup` があり、`.zattrs` は0のみ列挙 |
| `legacy-attrs-only` | `saved-fixed` の新規コピーに `saved-old` の `.zattrs` をバイト単位で移した対照 |
| `pyramid-on-control` | R123の既定ピラミッド有効の保存出力。旧 `.zattrs` とバイト一致し、0〜5の全配列が実在 |

[inputs.json](inputs.json) に全4ケースのファイルサイズ、SHA-256、参照パスを固定した。作成直後に再読込して出力現物と照合し、両readerの実行前後でも照合した。同じL0実ファイルを持つ `saved-fixed` と `legacy-attrs-only` の差は `.zattrs` 一つ。古い属性と新しい属性の意味上の差はdatasetsからの1〜5削除だけ。R121保存出力の `.zgroup` 欠落は既存のL0播種条件を含むため、要因分離には `legacy-attrs-only` を使う。fixture SHA-256は `4701f368c254fb4bcbc2d4065e2489ff2750358bf15307ed2eef9f77b03775d5`。

## 結果

| ケース | OME-Zarr Pythonの画像reader | villa Python `vc_reader` の最粗レベル |
| --- | --- | --- |
| `saved-old` | `parse_url` が `None`、画像配列なし | `KeyError: no array '5'` |
| `saved-fixed` | 1ノード、L0の1配列 | L0成功 |
| `legacy-attrs-only` | `ArrayNotFoundError`、path `1` で画像ノードの構築が中断 | `KeyError: no array '5'` |
| `pyramid-on-control` | 1ノード、6配列 | L5成功 |

OME-Zarrは `parse_url(..., mode="r")` → `list(Reader(location)())` → 返った表示用Dask配列の `compute()`。villa Pythonは `ZarrGroup.open(...)` → `group.level(0)` と `group.level(-1)`。比較のため、それぞれの実配列readerで `0` を直接開いた。全ケースで直接L0は `uint8`、ZYX `(101, 128, 128)`、全画素SHA-256 `8d5f47fa26dfbc80a7c47869188bda056b49e1f5ed0d85f941a40dd80d8fc937`。villa Pythonのgroup openと `level(0)` も全ケースで同じ値を返す。Python warningsは両readerとも全ケースで0件。OMEのloggingにはroot groupがある3ケースで `version mismatch: detected: FormatV04, requested: FormatV05` が出た。この版自動判別メッセージは修正後も残る。例外とloggingは端末原票に記録した。[vc.json](vc.json) · [ome.json](ome.json) · [OME端末原票](ome.log)

## 再現

既存fixtureを再利用し、未使用の結果・ログ名を指定する。リポジトリルートからPowerShellで実行する。WindowsのOME環境は同じ隔離先に用意した [wheel一式](ome-install-retry.json) を使う。fixtureが未作成の環境では同じ保存出力を揃え、`probe.py prepare <新規inputs.json>` で旧属性の対照を作る。既存の対照コピーとJSONを使った反復ではprepareは不要。

導入時は `python -B tools/research/run_windows.py <新規process.json> <install_ome.pyのパス> <新規ome-install.json>` で公式配布からwheelの取得と展開前見積まで実行する。既取得のwheelを使うオフライン導入は同じコマンドに `--reuse-wheels` を追加し、初回の `ome-install.json` と同じディレクトリに新しいprocessと導入原票名を使う。試験の実行コマンドは次のとおり。

```powershell
$run = 'experiments/vesuvius/r009/20261116-reader-impact01'
python -I -B tools/research/run_windows.py "$run/ome-replay-process.json" "$run/probe.py" ome "$run/inputs.json" "$run/ome-replay.json" *> "$run/ome-replay.log"
$wslCommand = @'
set -eu
cd /mnt/c/dev/kensyoukin
run=experiments/vesuvius/r009/20261116-reader-impact01
cpu=$(/usr/bin/python3 -B -c 'import os; print(min(os.sched_getaffinity(0)))')
ulimit -v 4194304
ulimit -c 0
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
timeout 60s taskset -c "$cpu" unshare -Urn /usr/bin/time -v -o "$run/vc-replay-time.log" /usr/bin/python3 -B -S "$run/probe.py" vc "$run/inputs.json" "$run/vc-replay.json"
'@
wsl -d Ubuntu -e bash -lc $wslCommand *> "$run/vc-replay.log"
```

OMEはWindows CPython 3.14.6、OME-Zarr 0.21.0、Zarr 3.4.2、Dask 2026.8.0、NumPy 2.5.5、Numcodecs 0.17.1。Windowsの既存site-packagesはreaderのモジュール検索パスから除いた。villa PythonはWSL Ubuntu CPython 3.12.3、`vc_reader` 0.1.0、NumPy 2.2.6。R125の実 `_reader` と `_catalog` を保存済みビルドのSHA-256と照合した。ソースと拡張両方を探索パスに指定し、実パッケージの初期化を実行した。ビルド済みファイル名とSHA-256は結果JSONにある。[OME-Zarr公式配布](https://pypi.org/project/ome-zarr/0.21.0/) · [公式Reader API](https://ome-zarr.readthedocs.io/en/stable/api/reader.html) · [R125のビルド原票](../20261113-python-validation01/run01/build04/result.json)

## 資源・範囲

- WindowsはCPU 1、プロセスcommit 4 GiB。WSLはCPU 1、AS 4 GiB、core dump 0、ネットワーク分離。制限runnerで計測した試験・導入を含む壁時間は合計172.711秒。OME-Zarr読込48.199秒、最大RSS 144,826,368 B。villa読込10.01秒、最大RSS 79,236 KiB。[OME実行原票](ome-process.json) · [WSL時間とRSS](vc-time.log)
- 初回導入はwheel取得後、保守的な展開時見積595,934,662 Bが当初の512 MiBを超えたため、展開前に停止。主担当が本試験の上限を640 MiBへ変更し、同じwheelのSHA-256を照合してオフラインで導入した。初回のpipの応答本文は107,407,463 B、そのうち保存wheelは98,229,964 B。事前に直接取得した公式版情報・napari経路の調査資料は計149,194 Bで、ローカル計測分の合計応答本文は107,556,657 B。HTTPヘッダー等と文書閲覧ツールの通信量は含めない。最終照合時の担当作業＋原票のpayloadは350,374,694 B、C空き8,263,979,008 B。[初回停止](ome-install-process.json) · [導入再試行](ome-install-retry.json)
- 保存ZarrとD:は読取のみ。新CT、描画、ビルド、GPU、有料計算、外部書込は0。R123の `saved-fixed` はR007/R121/R123結合版の出力。本試験の実証範囲は、その出力と旧属性だけを移した対照に対する固定readerの挙動。R123単独の再ビルド、VC3D/napari GUI、現在の上流mainの実行は対象外。
