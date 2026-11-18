# PHerc0800公式面4左中央の原寸検査

手元RTX 4060 Tiで同じ16層の順逆を比較し、担当と主担当が原寸で別々に確認した。両者とも追試に回す字画・行のROIは0件。固定した主域 `[128,576,960,960]` と深さを閉じる。物理ラミナの帰属とインクの有無は未判定。 [順の原図](results/mesh4-forward.png) · [逆の原図](results/mesh4-reverse.png) · [中心CT](pair/mesh4-ct-centre.png) · [研究票](../../../../research/220-next-contiguous-unread-window.md)

## 候補と採用範囲

| 候補 | 来歴と今回の観察 |
|---|---|
| PHerc0800公式面4左中央 | 固定9.6 µm主域960×960のうち782,112画素に幾何支持。うち570,456画素が既済窓の拡張XYZ箱外で、いずれも主域内で4連結。R219同面下方とのUV非交差と、公開中央層で左右に続く交差繊維を確認して採用。 |
| PHerc0800公式面1・3の候補 | 同じ公式展開群で同等の軸・支持条件を比較。最上位候補の拡張箱外は457,520／472,104画素、幾何支持は645,216／644,700画素。いずれも面4より今回の計画上の観測範囲が小さい。 |
| PHerc0813公開atlas `z14304_w100` と `z14896_w080` | 指定再構成 `20250821151723`。spiral-fitの展開で著者の繊維目視は両方 `aprova`、既存表のink_pass_v1/v2は両方false。固定公開treeには両順3モデルの原寸TIFFがある。著者の公開表にはHecate両順の集計があり、treeで具体的に確認したTIFFはseed42、seed43、soup42。先に検査したR188の `z12496_w020` とIDは異なる。物理的重なりと既存予測の原寸内容は未照合。 |

[一次、2026-11-15 JST] PHerc0800では公式8.64 µm再構成 `20250521135224`、面4 `20251028222030-auto_grown_20251028222030940` の公開表面Zarrを使った。固定範囲は9.6 µm座標でcrop `[96,544,1024,1024]`、主域 `[128,576,960,960]`。R138–143の旧面6末尾146中央512²およびR219の面4下方・面5上方の実crop XYZ箱を32 CT voxel膨らませて比較した。箱外570,456画素は観測範囲を選ぶ幾何上の指標。箱内の再検査面積、実際の公開面producer座標対応、物理ラミナの帰属は未確定。 [候補幾何](candidate-geometry.json) · [親の独立選定](lead-selection-check.json) · [固定計画](plan.json) · [PHerc0813 atlas表](atlas-manifest.csv) · [z14304 tree](z14304_w100-tree.json) · [z14896 tree](z14896_w080-tree.json)

[一次・推論、2026-11-15 JST] 同日R218で確認した公式規定と受賞一覧では、同再構成はFirst Letters対象で0800の受賞記載は見当たらなかった。先行43面の検査はこの公式面群を含んだが、別checkpointの数値ゲートで止まり、著者の後日監査で既知対照の通過も安定しなかった。別作者のflat 9 µmでは0800公式面群で散漫な反応と面飛びが報告された。公開atlasにも0800の95面と著者のHecate両順検査がある。同一公式ID・範囲の原寸Hecate予測は照合資料で確認できず、面4左中央をこの一回で固定比較する。先行の展開との物理重なり、チェックポイントの全学習座標は未確定。 [R218の公式確認と先行原報告](../20261115-official-unread-surface-selection01/README.md) · [Hecate公開モデルカード](../20261114-alternative-ink-model-selection01/originals/hecate-card.md)

## 入力と実行条件

公開中央層を79 Rangeで取得し、219の4全オブジェクトを再利用。原寸4分割を別確認した後、全層83オブジェクト42,156,032 BをETag・長さ・中央Rangeに照合。全層の新規受信は40,124,416 B、27.063秒。公開Z中心15を新k=8に置き、全軸8.64→9.6 µm、float64 X→Y→Z補間と一回の最近接偶数丸めで16×1024×1024 uint8にした。幾何・全元標本存在の固定支持857,584画素のうち4,392画素は実値が全16層0へ丸まり、Hecateのdepth-any支持は853,192画素。順逆は同じ16枚を使った。 [取得原票](surface-acquisition.json) · [中央層原寸](native-ct-centre.png) · [中央層取得](preview-acquisition.json) · [全パッチ契約](patch-contract.json)

219の実証済み入口を一窓に適応した。既存Hecate 9.6 µm公式重み・固定ソース、64×64／stride 32、公開順と逆順、FP32・TF32無効・batch 1。各961格子のうち844有効。CPU参照は各順の最初の有効3パッチ、計6、CPU1／commit 4 GiB／strictロード1回で監督34.127秒。手元RTX 4060 Tiの既存Windows PyTorch 2.13.0+cu130環境、専用FIFO、入場120秒・実行600秒・外780秒、commitとVRAM allocator各4 GiB。 [219からの差分](219-adaptation.diff) · [CPU原票](cpu-supervise.json) · [手元実行計画](local-plan.json)

主担当は実行前に全16,777,216入力値、両順の全1,922格子契約、中心CT PNG、取得83オブジェクトと中央層79応答・再利用4オブジェクト、CPU参照6件と固定資産を別照合した。公開配列のスライス順で定義した順逆を比較し、法線の物理的な向きは未確認。 [入力の独立検算](lead-input-check.json) · [実行資産の独立検算](lead-local-check.json) · [手元実行判断](lead-local-clearance.json)

## 完走と原寸判定

[一次、2026-11-15 JST] GPUのFIFO待ち0.714秒、監督201.260秒。先頭3パッチからの残り予測192.950秒に対し残予算593.759秒で継続し、順844件と逆844件をモデル工程194.031秒で完走。GPU strictロード1回（2.621秒）。CPUの6代表パッチとの最大絶対差3.4273×10⁻⁷、最大MAE 1.3856×10⁻⁸。実測プロセスRSSピーク1,684,721,664 B、GPU peak reserved 897,581,056 B。主担当は全実行位置・入力ハッシュ、代表確率52件、全961格子のHann分母、分子・分母から再構成した2,097,152 PNG値を別確認した。 [実行原票](results/execution-result.json) · [担当の検算](result-check.json) · [主担当の出力検算](lead-result-check.json)

[一次・目視、同日] 中心CTと両順を同じ0–255階調で原寸確認。左の順は斜め支持端近くの幅広い明部と孤立斑があり、逆は支持端の弱い点列と分割線付近の縦長斑が目立つ。右中段の順の斜めの明斑並びは逆で境界のぼけた塊になる。主担当が逆で見た幅広いL状反応も、隣接字画や行を伴わない孤立斑だった。全主域で追試位置を選ばなかった。幾何支持上の順逆差はMAE 9.880 DN、相関0.1324。これは順による出力差の記述で、原寸判定は固定階調の画像に基づく。 [原寸分割図](review-panels.json) · [分割図の全画素照合](lead-panel-check.json) · [担当の判定](visual-review.json) · [主担当の判定](lead-visual-review.json)

## 資源と再現

資料・中央層・全層の全新規HTTP応答本文は41,834,615 B。既存重みをその場で読み、元3D CTと新重みの取得は各0。専用FIFO終了後、PID 11420と51208、holder、待ち札が消えたことを親が別照会した。クラウド作成0、費用US$0。手元の電力費は未計測。 [資源記録](resources.json) · [入口と監督](local-supervisor-result.json) · [解放の独立確認](lead-local-release-check.json)

凍結済み入力・モデルで、`cpu_supervise.py` → `local_gpu.py freeze` → 承認済みSHAと空きの別確認 → `local_gpu.py supervise` を一回実行した。数値・パネルは `verify_output.py local-run` と `review_images.py` で生成した。この保存先は各工程が新規ファイルを作る契約なので、再実験する際は別保存先へ移して原票を保つ。 [Hecate固定資産](local-run/fixed-assets.json) · [SHA-256目録](manifest.json) · [lab登録候補](record.json)
