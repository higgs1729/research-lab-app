Status: resolved
担当: 研究（R170、2026-11-14）
Blocked by: 169

# PHerc0846Aの公開追試面の種点近傍で、紙面と割れを元CTから識別できるか

## 依頼

2026-11-14 JST。169の公開カードから文字ROIは採らず、同じ公開面への独立の小実験を行う。公開JPEGの正確な再現や元カードの高反応部との同一性は主張しない。実行計画の入口は experiments/vesuvius/discovery/20261114-pherc0846a-lead-audit01/README.md の「一つの条件付き識別実験」。主担当がその計画を採用した。

入力はsurvey固定1f12c1ceb14c1f24acc48249eaad60bcdf541721の results/meshes/PHerc0846A_2601_2784_3851。169保存meta・固定木を再利用。3 TIFFは各56329B、計168987B。公式masked L0は PHerc0846A/volumes/20250728152254-9.362um-1.2m-113keV-masked.zarr。表面予測ZarrをCTとして扱わない。公式メタの寸法/型/codec/chunk規則を確認し、既存処理が扱えない形式なら新依存やビルドをせず返す。

TIFXYZの有効頂点から公開種点XYZ(2601,2784,3851)への距離最小を選ぶ。同距離は行・列昇順。距離と対応を保存し、renderer画素中心規約に最も近いcanvas整数を中心に128²を凍結する。種点とメッシュの対応が取れない、128²が入らない場合は別地点へ動かさない。R103観測版の64²四区画でP/Nを取得。L0、scale1、linear、非反転法線、33層d=-16…+16。元CT必要キーを8隅から凍結し、HEAD合計の見積もり後に本文GET。

限度：mesh1MiB、CT16キー/32MiB、全本文34MiB、取得工程120秒、作業128MiB、C空き10GiB。CPU1/AS4GiB/core0/数値threads1、幾何120秒・描画120秒・解析120秒。CTは予告リストのみ、超過は停止して見積もりを返す。通信は取得段階だけ。既存165/166の取得・観測・描画・表示コード、R103/R123等の検証済みバイナリを借り、再ビルドしない。D読み取りのみ、新出力C。料金0、GPU/学習/インク推論/外部投稿/サブ委任なし。

判定するのは、種点近傍のP/Nが連続した一枚のCT組織に沿うか、割れ/空隙との位置関係を追えるか。4固定断面はローカルx=32/96、y=32/96。CT中央層と断面を原画の固定0–255で表示。十分なキャッシュ被覆があるなら同じP中心のXYZ直交3断面も64²の整数voxelで直接抽出できる。追加キーをそのために取らず、未取得位置は欠測と明記する。文字らしい形を探すための座標・深さ探索はしない。画素の明暗だけで空隙/紙面/インクを確定しない。根拠が弱ければ未判定を残す。|d|<=2等の未校正基準を普遍条件にしない。

数値の検査は既存の検証済み補間経路を再利用し、固定代表点の元CT8隅・P/N・出力、TIFF/Zarr同一性を確認する。親は図を別目視する。目的に不要なバイナリ再検査や大規模全点検査を重ねない。失敗時は原票を保持、修正や実行条件を変える場合は別ファイル。

保存先 experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/。原票と目視結論、資源、次に識別する問いを研究票へ反映しlab候補を作成。登録は親。

委任は gpt-6.1-sol / high。既存165/166の手順と固定座標規則があり、それを別入力へ適用する仕事としてhighを選ぶ。逐次実行を維持する。

## 結論

[一次・実行と目視、2026-11-14 JST] PHerc0846Aの公開種点に最も近いメッシュ頂点を基準に固定128²を設定し、元CTの8チャンクから33層を描画した。固定法線4断面とアンカー中心の整数voxel直交3断面では、Pの列が明るい帯に沿う区間と、暗い領域の縁を通る区間が見える。近接する複数の帯から同じ物理ラミナを一意に追えず、暗域を一つの割れや空隙として断面間で対応させることもできなかった。紙面の対応と一定の補正量は未判定。公開カードの反応位置はこの元CT座標に登録されていない。[中央層と法線断面](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/normal-sections.png) · [直交原画](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/orthogonal-raw.png) · [P/N投影](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/orthogonal-mesh.png)

## 根拠・詳細

### 種点・幾何・取得

- [一次] Survey固定 `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の追試面のXYZ三軸各56,329 Bを保存固定木のGit blob IDに照合し、169のmetaを再利用した。公式masked volume `20250728152254` のL0はZYX `[14019,7726,7726]`、128³、Zarr v2、無圧縮uint8。入力本文と公式メタデータをHEAD/GETの長さ・ETagとハッシュで照合した。[準備原票](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/prepare-result.json)
- [一次] 112×112 TIFXYZの有効頂点11,664から、公開seed XYZ `(2601,2784,3851)` とのユークリッド距離が最小のgrid YX `(55,55)` を選んだ。同距離候補はこの一点。XYZ `(2599.264648,2784.303467,3844.219482)`、距離7.005637 voxel（65.587 µm）。既存rendererの浮動小数点中心・scaleで得たcanvas座標は各1099.4999836で、最寄り整数 `(1099,1099)` を局所 `(64,64)` としてcrop XYWH `(1035,1035,128,128)` を固定した。[種点原票](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/roi.json)
- [一次] R103観測4×64²はL0・scale 1・linear・非反転法線で全16,384点のP/Nが有効。隣接P距離は最大1.0136 voxelで、幾何の大きな局所飛びは見られなかった。33層のCT 8隅に±0.001 voxelの余裕を加え、Z 29/30、Y 21/22、X 19/20の直積8キーを本文前に凍結した。全HEADが2,097,152 B、計16,777,216 B。予告した8キーだけを取得し、HEAD/GETのETag、本文MD5とSHA-256が一致。メッシュ168,987 B、公式メタ3,281 Bを含め、新規本文総計16,949,484 B。各上限内だった。[固定幾何とキー](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/plan.json) · [HEAD](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/head-result.json) · [CT取得](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/ct-result.json)

### 元CTとの照合と断面

- [一次] R123製品で固定cropを一回描画。33枚のTIFFと無圧縮Zarr L0の全540,672値は一致。固定4断面とアンカーの重複を除いた17 XY、各5深さの計85標本で、P/N、元CT8隅と三線形値を照合し、保存uint8との差は最大0.496771 DN。出力に値0が4個あり、全P/N有効・CT支持の全キー取得済みなので値0を欠測マスクには使わなかった。[集計結果](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/result.json) · [代表点の8隅](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/representative-ct.json)
- [一次] 法線断面はX/Y各局所32・96に固定し、`d=-16…+16`。中央層d=0と断面は `raw/` に元寸の8-bit PNG、一覧では最近接拡大で表示した。直交断面の中心はアンカーPの各軸を `floor(p+0.5)` で丸めたXYZ `(2599,2784,3844)`。固定軸を除く2軸で `[center−32,center+32)` の64²を直接読み、各4,096値の全数被覆を確認した。欠測0、直交断面専用の追加キー0。投影図では固定平面から0.5 voxel以内のメッシュPだけを水色、アンカー法線の平面外点をオレンジ輪郭で示した。明暗の再調整は行っていない。[直交座標](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/orthogonal-coordinates.json) · [表示方法と原画の場所](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/README.md)
- [一次・目視] X=2599とZ=3844ではP列が明るい細帯と局所的に並走し、両側に暗い帯が複数ある。Y=2784ではP列が広い暗域の縁付近と不均質な領域を通る。法線断面でもd=0付近の濃淡帯の位置が変わり、合流・分岐のように見える箇所がある。同じ実ラミナや割れの境界として対応点を置ける強さの証拠は得られなかった。符号付き距離は未測定。インク、文字、紙面の表裏は未判定。[目視記録](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/assessment.json)

次に識別する問いは、先行カードの反応がこの種点近傍に実際に含まれるか。照合には同じ描画の元CT・未合成予測・評価マスクとglobal XYへの登録が要る。固定断面から得た局所濃淡だけでは、公開反応と暗域の因果関係も、モデルを使うための紙面補正量も決められない。

## 主担当の別照合

[一次] 主担当は担当所見の受信前に固定3図を別目視し、局所的なPと明帯の並走を確認した。同一ラミナ、同じ割れ、一定補正の判断は未判定で一致した。アンカー5深さで元CTの8隅からfloat64補間し、保存Zarrとの最大差0.436383 DNを確認。製品の追加起動は0。[別照合コード](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/lead_check.py) · [別照合結果](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/lead-check.json)

## 実行条件・再利用

取得の累計33.363秒。WSLで1CPU・AS 4 GiB・core無効、幾何と製品は数値1スレッド・ネットワーク名前空間分離・D:読取mount。四区画の幾何は1.650秒、製品工程2.117秒のうち描画0.834秒、製品最大RSS83,259,392 B。Windowsの集計は1CPU・4 GiB commit・各120秒上限、ROI0.139秒、支持3.175秒、最終解析0.388秒。後処理初回は既存Windowsランナーから同階層モジュールを読めず停止したため、importパスを指定して別原票で再実行した。再取得・製品再描画は0。成果フォルダは約19 MB、追加費用0 USD。新ビルド、依存導入、モデル取得、推論は実施していない。[初回後処理のログ](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/analyze-analysis.log) · [最終後処理](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/analyze02-process.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-seed-ct01/lab-record.json)
