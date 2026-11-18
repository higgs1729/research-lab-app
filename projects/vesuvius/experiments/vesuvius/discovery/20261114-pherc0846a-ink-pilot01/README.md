# PHerc0846Aの種点周囲における元CTと固定CPU予測

[研究171](../../../../research/171-pherc0846a-ct-to-ink-pilot.md)の原票。公式PHerc0846A masked L0 `20250728152254`、9.362 µm。ketchupbyheinzの固定survey `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の派生面 `PHerc0846A_2601_2784_3851`。元CTはVesuvius Challenge、派生面はketchupbyheinz。CT・派生画像はCC BY-NC 4.0、固定公式モデルはMIT。[公式目録](https://scrollprize.org/data_browser/PHerc0846A) · [派生面の固定木](https://github.com/ketchupbyheinz/vesuvius-scroll-survey/tree/1f12c1ceb14c1f24acc48249eaad60bcdf541721/results/meshes/PHerc0846A_2601_2784_3851) · [モデルカード](https://huggingface.co/scrollprize/ink_9um/blob/7109667e2607db1b90c37c8b09cb876ea7fe7bb1/README.md)

## 固定入力

R170の種点最近接頂点 `(row,col)=(55,55)`、canvasアンカー `(1099,1099)` を保持。canvasのXY各 `[843,1355)`、512²（名目4.793 mm四方）。linear、scale1、L0、法線反転なし、33層 `d=-16…16`、刻み1 voxel。物理紙面の対応と表裏、上流カードの座標登録は未確定。mesh・公式ZarrメタデータはR170保存物のSHAを照合し、新規取得0 B。[R170](../../../../research/170-pherc0846a-seed-ct-diagnostic.md) · [固定ROI](roi.json) · [保存入力の再利用](prepare-result.json)

既存R103観測版の64区画の全262,144点で基点と単位法線が有効。隣接点距離最大1.0836 voxel、2 voxel超0。中央4観測バイナリはR170とSHA一致。全33層の8隅と±0.001 voxel余裕でCT44キーを凍結。R170の保存8キーと、追加36キーを使用。既存製品を1回だけ実行し、33 TIFFとZarr L0の全8,650,752値が一致。中央128²の全540,672値はR170と一致。中央17層は4,456,448値中4,456,404値が非ゼロで、全深さが0のXYは0。元CTの画素値と物理紙面の正しさは別の判定になる。[幾何・キー計画](plan.json) · [中央比較](central-compare.json) · [固定入力契約](input-contract.json)

## 推論と表示

固定公式commit `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0`、seed42 step075000 SHA-256 `e635558ae6a1a807a7e5ec1e83adfd45bc3c0ac53883ea43f1d4e085d62a9cab`。R133/138で使った既存Windows CPU Torch 2.14.0+cpu、隔離Zarr 3.1.5等、Pythonの外部通信拒否とHF offlineを再利用した。既存の互換依存環境で、モデル配布の9 µm近傍にあたるnative 9.362 µmのまま入力した。robust-MAD (`tifxyz_robust`)、128²、stride64、Hann、batch1、workers0、TTA/compileなし。保存層8→24と24→8を各49パッチ、一回ずつ逐次実行。深さ順のラベルは本入力の保存順を示し、物理の表裏や上流カードのreverseと対応づけていない。[forward実行](forward02/execution.json) · [reverse実行](reverse/execution.json)

出力直前に保存した合成和と同一SHAの正重みから、両方向ともfloat値と公式LZW TIFFの262,144値を再現した。比較図はCTの中央層と各TIFFを固定0–255階調、1:1で並べ、図のパネル画素と各原画が一致することを確認した。[比較図](comparison.png) · [CT原画](ct-mid-raw.png) · [forward原画](forward-raw.png) · [reverse原画](reverse-raw.png)

| 保存順 | スコア平均 / 中央値（uint8） | ≥128画素 | 秒 | 最大RSS（B） |
| --- | ---: | ---: | ---: | ---: |
| 8→24 | 116.922 / 111 | 85,932 | 17.613 | 742,285,312 |
| 24→8 | 133.540 / 134 | 140,706 | 16.788 | 744,996,864 |

平均絶対差38.518 DN、相関0.21468、≥128画素の交差56,852/和169,786。128は分布の記述に用いたしきい値で、インクの判定基準ではない。ラベルがなく精度・インク率・物理紙面は未評価。[集計原票](comparison.json)

## 目視判定

forwardには局所的な霞状の斑点、reverseにはより広く連結する明部が見える。左下のCT暗帯に接するreverseの明部がある一方、明るいCTにも反応が広がり、弱いスコアの暗穴もある。全図を原寸で確認し、独立した字画が並ぶ行を一意に追える領域は選べなかった。主担当も固定比較を独立に目視し、候補なしで一致。転写はしていない。[目視原票](assessment.json)

記述値として、CT中央層の第10百分位40 DNを下回る画素は24,943/262,144。各方向で単一モデルの第97百分位以上（同値込み）を採り、forwardは7,877画素（全体の3.005%）、reverseは8,129画素（3.101%）。その暗部と一致するのはforward 706/7,877（8.96%）、reverse 1,056/8,129（12.99%）。暗い画素には割れの正解ラベルがなく、先行カードの2モデル上位3%交差や異なる評価域とは比較できない。紙面、割れ由来、インクの有無は未判定。この固定一回から文字追試ROIを採らず、深さ探索へは進めない。[暗部の記述集計](dark-overlap.json) · [先行カードの境界](../../../../research/169-pherc0846a-public-lead-audit.md)

主担当は保存中央のR170全540,672値、CT中央PNG、両方向の実引数と層順を別に確認した。保存float和・重みから両方向のTIFFと原寸PNGを再計算し、全524,288値が一致。重みも一致し、製品・推論の追加起動0。[独立検査コード](lead_check.py) · [独立照合](lead-check.json) · [独立プロセス](lead-process.json)

## 取得と再利用

全36 HEAD成功。初回はHEADとGETの180秒上限で、GET 26件52 MiBを完全保存して中断した。27件目は応答200・ETag一致後の本文読取中で、途中受信は量不明・最大2 MiB。主担当は同じ残10件だけの第2取得を90秒上限で採用し、31.861秒で完了。保存HEADの長さ・ETagに全GETを照合し、取得済み26件とR170の8件をSHA確認して再利用。追加完全本文75,497,472 B（72 MiB）、途中込み上限77,594,624 B（74 MiB）。取得二工程の計測合計約211.861秒。再取得の待機時間、TCP/TLS・HTTPヘッダーは含まない。[期限停止](ct-deadline.json) · [第2取得開始](continue-start.json) · [取得完了](ct-result.json)

既存のnative手順 `acquire.py prepare`、`launch.sh geometry`、既存Windows制限ランナーの `run_analysis.py support`、`acquire.py head`、`acquire.py ct` の順。再開は本番の停止票と対応する固定残キーがある場合だけ `acquire.py continue 90`。描画 `launch.sh render` 後に `run_analysis.py input input02`、`forward forward02`、`reverse`、`compare` を使用。WSLは取得を `setsid --wait`、nativeを `unshare -Urnm` でD: read-only、1CPU・AS4 GiB・core0。Windowsは既存JobのCPU1・commit4 GiB・数値thread1、各120秒。各開始票とログを保存。幾何工程92.953秒、製品3.011秒・RSS167,354,368 B。作業は約125 MB、C:空き約41.2 GB。新モデル・依存・ビルド・GPU・追加クラウド支出0。電力・モデル費は未算定。[描画プロセス](render/render-process.json) · [推論forwardプロセス](forward02-process.json) · [推論reverseプロセス](reverse-process.json)

描画後の初回入力照合では、linear指定でも補間名がログに出ると仮定して停止した。実argvとcropログを読む計測側だけを修正した。推論前の初回ラッパーはコピー元R138の一時ディレクトリへの `mkdir` が拒否され、公式推論は起動しなかった。R171の一時ディレクトリへ変更し、別の開始票から予定の各方向一回を実行した。元原票、製品・モデルコードへの変更なし。[入力照合停止](input-analysis.log) · [推論起動前停止](forward-analysis.log)
