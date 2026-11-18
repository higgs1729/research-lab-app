# R224：次の一実験の固定資料

結論と採否の理由は[研究票224](../../../../research/224-discovery-bottleneck-next-intervention.md)に記載。これは次の実験の選定であり、Reader V3の新実行や新文字の認定ではない。

- [次の固定計画](next-plan.json)：PHerc0306Bの上方帯と既知行帯、公開TRACE/Reader V3、取得3ファイル171,424,048 B、推論/GPU/クラウド0。
- [座標と数値幾何支持](coordinate-support.json)：公開PNGのfloat32 remapからcarrierへの変換。作者のpx/20規約を使い、現行rendererの半画素規約を持ち込まない。
- [原寸上方応答・claim](review/claim-upper-lead-native.png) / [TRACE単体](review/trace-upper-lead-native.png)：公開画像に既出の応答。両者はTRACEを共有する。
- [縮小全景](review/claim-overview-20percent.png)：位置把握用。原寸の代わりにはしない。
- [担当の目視](visual-review.json) / [親の上方別目視](lead-upper-visual-review.json) / [親の既知対照別目視](lead-visual-review.json)。
- [先行tracingとの位置](prior-reading-overlap.json) / [先行の読み・学習露出の限界](provenance-and-novelty.json)。
- [取得1](acquisition.json) / [メタと面座標](acquisition-metadata.json) / [先行の読み](acquisition-prior-readings.json) / [保存資源](resources.json)。
- [親の画像照合](lead-image-check.json) / [親の座標照合](lead-grid-review.json) / [次案の別確認](lead-plan-check.json)。
- [manifest](manifest.json) / [lab登録候補](record.json)。登録と次の着手は親担当。

## 再利用時の入口

`next-plan.json` のHF revision、各本文の長さとSHAを使う。NPYはC順float16、shape `(4900,7780)`、header 128 B。次の取得では全ファイルのSHAを確認する。R224は先頭1024 BだけをRangeで確認しており、全予測値は未取得・未評価である。

比較は原native carrierの整数窓を取り、上下反転を一回だけ適用する。これは公開PNGのbilinear remapを伴う表示と画素同一ではない。公開画像の原寸crop自体はPNG画素を1:1で保持している。元XYZは作者の固定tifxyz、4隅の数値有効率を物理ラミナの確定に使わない。

`build_next_plan.py` は原資料から座標と計画を作ったコード。`inspect_pngs.py` と `crop_upper_lead.py` はこの選定で行った表示だけのコード。`acquire_*.py` は固定資料の取得原票用で、既存出力があれば上書きせず停止する。別実験で再利用する場合は新しい保存先へ写す。

既存の小窓で候補を選べなかった結果と既知対照の結果は保持した。Cへ新規保存、D書込0、外部送信・新規課金・再委任0。
