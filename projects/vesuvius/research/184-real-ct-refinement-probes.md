Status: resolved
担当: 研究（R184、2026-11-14）
Blocked by: 183

# 実CTの既知文字側と未確定側で、採取窓の中心化はどの補正量を変えるか

## 依頼

2026-11-14 JST。主目標は未読文字の発見。181は物理紙面の帰属が未確定なため180への自動補正を見送り、182・183は人工CTで窓配置による約6voxelの差と、その差を解消する既定互換のopt-inを実証した。次は同じ実CTの小さな固定地点で、既存補正がどの帯に反応するのかを確かめる。補正の成功を真の紙面や文字の改善と同一視しない。

対象はPHerc0343、173と180で保存済みの同じ128×336 meshおよび20250521140437-8.640um-1.2m-116keV-masked.zarr。meshの列・行を (88,69)、(299,41)、(306,39)、(324,39) の4点に固定する。第一点は173/175の既知文字対照内、残りは180の三probeに近い節点。画素や応答を見て選び直さない。元meshから既存QuadSurfaceのbicubic経路で製品が使うP・Nと接平面基底を取得し、元節点との対応を明示する。小surfaceへの切り出しで境界条件を変える必要はない。4点に明示した同じP/Nを与えるOBJを使い、183の凍結CLIを再利用できる。

比較するのは183と同じ scale_group=0、reader_scale=.5、start=-2、stop=16、step=1、border_off=0、low/highは既存値、cache_mb=32。r3/center_window省略、r3/true、r0の計3条件のみ。4点一つのOBJなら製品3回。これは本番既定の全深さ設定ではなく、183から引き継ぐ固定診断条件。必要な各接平面の補間支持は、bicubicで得た実P/Nと実基底から実行前に確定する。保存173/180のCTキーを読み取りで再利用し、欠損fillを入力に混ぜない。不足キーがある場合は公式同一Zarrから追加上限8キー/16MiB、失敗を無制限に再試行しない。上限超過時は実行せず不足を返す。

欲しい結果は、4点×3条件の補正量、法線上のCT強度・ぼかし後強度・不透明度寄与、入力と補正候補位置を同じCT断面へ記した図、および次の実文字比較へ進む根拠があるかの判断。断面は既存180を位置違いのまま転用せず、固定点を正確に記す。全補間支持と基底・方向を保存し、親がCT値/積算量を独立に計算できる形にする。薄帯のどれが同一紙面か不明な場合はそのまま結論とし、強度の最大や既存インク予測を正解にしない。窓配置差と順序付きopacityの効果も区別する。既知字画を含む領域の中というだけで、第一点自体が墨画素とは呼ばない。

既存183製品・R160共有部品・保存CT/meshは不変。必要な観測helperだけを新規先へ構築できる。全処理CPU1、AS4GiB、各ライブラリ1thread、C/ext4新出力、Dは読取りのみ。helper構築120秒/1GiB、製品各60秒、追加通信合計16MiBと小メタデータ64KiBまで、C空き10GiB未満で停止。新しいモデル・依存・GPU・有料計算、全面補正、インク推論、閾値や点の探索、外部公開/送信はしない。製品成功後の後処理失敗で製品を再実行しない。

保存先 experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/。研究票へ結論と取得経路、原票・入力由来・再利用手順、manifestとlab候補を残す。親の重要な数値/図の別検証後に確定する。サブ委任なし、lab登録は親。追加クラウド費0。

今回はgpt-6.1-sol / xhigh。実CTで補正量と複数帯の帰属を結び付ける新しい診断で、単なる既定試験の繰返しではないため。183完了後の逐次実行。

## 結論

2026-11-14 JST [一次] R183固定CLIでPHerc0343の固定4点を、角基準r3、中心化r3、r0の3条件で各1回処理した。中心化による補正量変化は +0.988、+1.082、−7.329、−3.218 voxel。最大差の(306,39)では角基準 +7.774、中心化 +0.446、r0 −0.212 voxel。断面の明帯は複数あり、角基準の最大寄与はd=10、中心化はd=0、r0はd=−1。中心化しても対応する紙面は同定できない。主担当は未知面への全面適用を見送り、既知字画を含む一小領域で元面・角基準・中心化のCT→インク比較を次案に採用した。

[一次] 元meshからbicubic節点法線と実PlaneSurface基底を観測した。三条件は7キー、固定の2方向断面を含め8キー。R173/R180保存CTですべて充足し、欠損fill・追加通信は0。製品OBJは全12頂点で6有効桁の丸め範囲内。主担当が別計算した全16,188生CT補間は最大3.164×10⁻⁵ DN差、積算変位は最大3.294×10⁻⁶ voxel差。第一点は既知字画対照領域内で、墨位置のラベルはない。

## 取得の経路

既存のR183 ELF・R160ライブラリと保存CTをSHA照合。観測だけの小CLIはR182の既存構築設定を借り、C上WSL ext4の新規先へ構築した。補助CLI構築5.377秒、製品3回計0.341秒。製品の再構築・再実行、依存・CT取得、追加クラウド費0。

- [4点の結果と根拠](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/README.md) · [断面と不透明度寄与](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/sections.png)
- [全P/N・座標](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/geometry.json) · [支持・再利用キー](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/support-plan.json) · [量とOBJ比較](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/comparison.json)
- [主担当別検算](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/lead-verified.json) · [主担当別目視](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/lead-visual.json) · [ハッシュ目録](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-real-ct-refinement-probes01/lab-record.json)
