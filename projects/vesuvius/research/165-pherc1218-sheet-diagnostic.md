Status: resolved
担当: 研究（R165担当 2026-11-13）
Blocked by: 164

# PHerc1218の公開候補中央で、元CTから紙面の位置と連続性を診断する

## 依頼

2026-11-13。本人承認済みの未読文字発見の主軸に沿い、研究164の次の一実験を採用する。詳細は experiments/vesuvius/discovery/20261113-next-target01/README.md。主担当の原票照合と採用登録 record-18fa5abb87ee、inbox未決0件。主担当レビューで未判読の公開候補との非重複を一律条件にする誤った制限を削除した。今回の陽性が文字発見ではない点は維持する。

問いは、PHerc1218の固定派生面 w083_main 上にある既公開箱の中央で、元CTの紙面が平坦化面の法線原点の近くを連続して通るか。位置ずれ、隣接紙面の混入、紙面の飛びを分類する。公開6モデル×31深さのスコアを再推論せず、形状とCTの独立した証拠を得る。

固定入力は公式masked L0 20250521120456、8.64µm raw uint8 128³ chunk、Jake-vc固定revision6eba0e778fea52ac9044e4e3ec58dab0f82f968cの seg_big/w083_main/flat/tifxyz/flatten.tifxyz。既存一覧のLFS shaでx/y/z.tif（計2,239,008B）を確認する。model.ptは不要。固定ROIはcanvas x=[9162,9418), y=[2012,2268)の256²。49層d=-24…+24、scale1、bicubic、法線反転なし。x=9226/9354、y=2076/2204の4断面を固定。新データを見て窓・断面・深さをずらさない。

研究164の手順を実行し、既存R103幾何16区画で支持と必要キーを計算、全キーHEAD後に制限内なら取得、通信分離下で既存製品を同じ条件で1回描画する。基点・法線・CT8隅・代表画素の対応、無効領域、部分欠損を保存する。既存w035元CTの共通深さ範囲を同じ断面表示法の工程対照として再利用する。新しいw035データ取得や製品再描画は不要。

有効XY95%、4断面のうち3以上、代表的な紙面位置|d|≤2の条件は現状の幾何をそのまま使うための目安。普遍的な正解判定ではない。連続した一貫した位置ずれなら次の補正試験の可能性を残す。飛びや多重面があれば位置と根拠を示す。紙面を追えない場合は未判定とし、CTで字形が見えないことをインク無しへ拡張しない。断面図は固定階調・軸・物理寸法・中心線を示し、先行モデル図を隠して評価できるものを保存する。

上限はmesh3MiB、CT32キー64MiB、受信本文総計68MiB、作業512MiB、C:空き10GiB。CPU1/AS4GiB/core0/数値thread1。幾何全区画計120秒、製品描画120秒、集計120秒。取得は全体120秒を目安上限とし、期限/容量/キー一覧を起動前に保存。欠ける応答や変更ETag、支持不足、上限超過、別解像度/キャンバス、予期しない依存があれば原票を残し止める。サイズ確認後に順次取得、取得済みも含めて上限を数える。D:はread-only、新規保存はC:。

新たなビルド、モデル取得・推論・学習、有料計算、対象の変更、外部公開・応募・PR/メッセージ、サブエージェントは行わない。既存バイナリと入力のSHAを確認し、同時実行を避けるためPID/PGID/argv/絶対期限を開始時に残す。原票と実画像は experiments/vesuvius/discovery/20261113-pherc1218-sheet01/、研究票に結論と再利用知見を追記。lab登録候補を用意し、主担当が重要な結果を独立に確認して採否を決める。

今回の担当モデルは改めて gpt-6.1-sol / xhigh とする。既存の幾何・CT手順を使うが、新しい面の座標対応と初回の支持・資源管理を含み、紙面診断の成立性が未確定なため。逐次実行を維持する。

## 結論（2026-11-13 JST）

[一次・実行] PHerc1218の固定256²を公式元CTから一回描画し、指定した4断面を得た。平坦化面の基点・法線は全65,536画素で有効、隣接XYZ距離は最大1.032 voxel。元CTの4断面では、同じ物理紙面を法線原点付近に3本以上で一意に追えず、現条件の採用目安は満たさなかった。主担当の独立目視も一致した。紙面対応と一定の補正量は未判定。複数の濃淡帯はあるが、別紙面への飛び、紙面誤り、インクの有無はいずれも確定しない。[固定四断面](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/sections.png) · [目視記録](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/section-assessment.json)

## 根拠・詳細

[一次] Jake-vcの固定LFS三軸をSHA照合。実628×297・scale 0.05から全体キャンバス12,560×5,940、公開auto-crop `(19,19,12521,5901)` を再現。観測版16区画の原点と刻みが固定crop `(9162,2012,256,256)` に一致した。49層の全有効点・三線形支持と0.001 voxel余裕から18キーを確定。製品L0と49 TIFFは全3,211,264値一致。指定断面の代表196標本で基点・法線・CT8隅・独立float64補間値・保存uint8を追跡でき、最大差0.49548 DN。出力0値は0件。[幾何とキー](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/plan.json) · [代表CT値](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/ct-audit.json)

[一次・目視] w035元CTの工程対照には追える明るい連続帯がある。PHerc1218のY2204では中央近くに暗帯があり、局所x=96/128で `d≈+1`、160で `d≈+4`。負側にも別の暗帯があり、中央暗帯の紙面・空隙・境界の別は未確認。他の3断面も複数の濃淡帯や途切れがあり、原点や一定量のずれを採る根拠は得なかった。次に判定する場合は、保存元CTの直交断面で同じ物理ラミナを連続追跡し、固定面の `P+dN` への符号付き距離を独立に対応づける根拠が要る。[目視の所見と限界](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/section-assessment.json)

[一次・独立照合] 主担当はLFS、幾何16区画、18キーのSHA・ETagと保存全3,211,264値を確認し、4断面の重複を除いた49,980標本を元CTから再補間した。float64補間と保存uint8の最大差0.4999967 DN、固定float32丸めは全値一致。w035の明帯は工程対照であり、`|d|≤2` を普遍校正するものではない。照合1.666秒、製品再起動0。[独立照合結果](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/lead-check.json)

## 取得の経路と資源

[一次] 公式CTの18キー37,748,736 B、固定LFS三軸2,239,008 B、追加メタデータ3,042 B、合計39,990,786 B。全キーのHEAD/GET一致。取得工程計75.376秒。幾何16区画の工程13.477秒、製品1.733秒・RSS137,592,832 B、集計成功回0.454秒。1CPU、AS4 GiB、D:読取、製品工程はネットワーク分離。新規ビルド・モデル取得・推論・有料計算0。電力・モデル費未算定。[手順と全原票](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/README.md)

## メモ

- 固定LFS 3 TIFFを計2,239,008 Bで取得しSHA一致。公式 `.zgroup` と `.zattrs` を含め2,242,050 B。既存観測版16区画の幾何が13.477秒で完了。Windowsの計画集計はモジュールパス、次に元TIFXYZの `-1` sentinel を欠損とする規則で停止した。観測版の規則に合わせた修正後、保存幾何を再集計し、幾何を再起動せず65,536/65,536の有効点、18キー・36 MiBを確定した。[入力原票](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/mesh-result.json) · [幾何](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/geometry/stage-result.json) · [キー計画](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/plan.json)
- 18キーの全HEADで2,097,152 BとETagを確認し、CTを逐次取得。GET PID/PGID 2674、総取得上限の残り93.47秒を開始時に保存。[HEAD結果](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/head-result.json) · [CT取得開始](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/ct-start.json)
- 製品PID/PGID 2695が一回で終了0。後処理で出力 `canvas_size` の意味を取り違え、保存出力のcrop寸法と製品ログへ照合を修正した。既存製品の再起動は0。[集計初回](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/compare-process.json) · [lab登録候補](../experiments/vesuvius/discovery/20261113-pherc1218-sheet01/record.json)
