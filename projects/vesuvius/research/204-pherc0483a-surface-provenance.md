Status: resolved
担当: 研究（R204、2026-11-14）
Blocked by: 203

# PHerc0483Aの選定窓は元CTのどの紙面を通るか（2026-11-14）

## 依頼

研究203で固定atlas面 `kbh-PHerc0483A_3155_3610_11128` のCT中央PNGを確認した。固定診断窓XYWH `[704,1024,512,512]` のGabor交差マスクは70.17%でも、中央画像には粒状模様、下側の弧状境界、右下の暗部があり、同一物理紙面を追う根拠にはできない。指標の修正は文字の発見ではない。

本人はRunpodの必要分を使う判断を委任した。実験201の支出承認は完了したが、本人確認TASK-61によるBilling条件の確認待ち。待つ間の無料課題として、上の一面一窓の入力来歴と紙面追跡可能性を先に確認する。201と同時にモデル計算を始めない。

まず固定mesh→atlas座標→元CTの対応を確定し、窓内の上側、弧状境界、下側の三点だけを事前固定する。保存小メタと既存renderer/幾何手順を借り、公式volume、ボクセル寸法、mesh scale、atlas canvas、法線と座標の対応、欠損の扱いを照合する。必要な元CTキーと最小支持を見積もり、保存資料で足りるか、新取得の量はいくらかを示す。この票では新CTボクセルを取得する前に一度主担当へ計画を提示する。単一の紙面と認定できる条件と、中央PNGだけでは区別できないことを具体的にする。

主担当が範囲を確認した場合に限り、見積もった同じ三点に必要な少量CTを取得し、既存手順で直交断面とメッシュ法線を作る。追加取得上限はこの票の計画確認時に確定する。紙面を特定できなければ未判定で閉じ、見栄えや最も明るい帯に合わせた自動補正・未知文字の主張はしない。複数面への探索拡大、モデル推論、学習、重み取得、ビルド、有料資源、外部公開・送信なし。201の認証が完了した場合は、実行中の小処理を安全に区切れる地点を示す。

入力は203のCT・meta・固定PRではなく、幾何診断に必要なmesh/renderer一次情報。入口の例は202候補meta中のsurvey commit `1f12c1ceb14c1f24acc48249eaad60bcdf541721`、公式volume `20250521140913`（8.64 µm）、atlas revision `ac5ffd7098120368216948c4e06c494bf8e67178`。既存の少数点診断は165/180/184、非整数canvasの確認は199。過去の紙面未判定という失敗も踏まえ、同じ曖昧な図を増やすだけなら取得前に見送る判断でよい。

初期の新規受信はmesh XYZ・小メタ・必要ソースの合計16MiB、通信180秒以内。CT取得は初期範囲に含めない。CPU1/commit4GiB、C保存・D読取のみ。保存先 `experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/`。この票に結論・一次根拠・資源・次の判断を追記し、取得原票・固定三点と支持計画・manifest/record候補を残す。重要な対応と計画を主担当が独立確認する。再委任・別研究並列なし。

今回の担当は **gpt-6.1-sol / high**。既存のmesh座標と少数点CT診断の手順を別面に適用し、取得価値の判断と入力解釈を行うため。

## 結論

2026-11-14 JST。[一次] PHerc0483Aの固定mesh・元CT・atlasの座標対応を確認した。三点の中央層12,288画素は公式元CTからの再補間と公開PNGが全画素で1 DN以内、12,205画素は完全一致。連結原寸断面では、上側の粒状域から弧の鋭い境界を経て下側の繊維状領域に移る。同じ物理ラミナを三点間に追えず、紙面帰属は未判定。 [実験報告](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/README.md) [原寸連結断面](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/sections/continuous-yz-annotated.png)

## 根拠・詳細

[一次] 公式scanは `20250510022723`、masked volumeは `20250521140913`、8.64 µm・116 keV。固定112² meshのgrid scale 0.05とatlasのrender scale 0.9から2016² canvas、ピクセル中心、原点を照合。三点は上 `[832,1152]`、弧 `[832,1268]`、下 `[832,1392]`。観測全12,288座標と単位法線が有効で、主担当の独立27点との差は最大0.000861 voxel。 [支持計画](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/support-plan.json) [主担当座標検査](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/lead-geometry-check.json)

[一次] 三点の各3直交面38,025画素と、固定X(Z)折れ線上のY–Z連結断面39,808画素を6キーから抽出した。連結断面のXはZごとに変わり、三点の整数中心では一致する。弧の点は明るい細帯と濃淡境界の付近、下側は弱い繊維状の複数帯。連続した同一ラミナの根拠は得られず、空隙・別層への飛び・紙面内模様を確定できない。この一窓を閉じ、補正や文字の判定へ拡張しない。 [連結支持計画](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/continuity-plan.json) [断面原票](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/sections-result.json) [担当目視](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/visual.json)

[一次] 主担当は全生断面77,833画素を別アドレス計算で照合し、135点の三線形補間と保存uint8の差は最大0.490585 DNだった。原寸の別目視でも同じラミナの連続は未判定。 [主担当の数値・原寸確認](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/lead-sections-check.json)

## 取得の経路と資源

[一次] XYZ・小メタ173,465 Bを2.760秒で受信。主担当の支持確認後に6キー12,582,912 BをHEAD/GETで15.706秒、再試行0。既存観測器で3区画2.365秒、最大RSS 59,686,912 B。Windows CPU1・commit4 GiB、WSL CPU1・AS4 GiB、C書込・D読取。追加ビルド・モデル・GPU・クラウド支出は0。 [初期取得](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/acquisition.json) [元CT取得](../experiments/vesuvius/discovery/20261114-pherc0483a-surface-provenance01/ct-acquisition.json)

## メモ

2026-11-14 JST。[一次] 保存公式カタログのscanとvolumeを区別し、atlasの固定meshパス、8.64 µm元CT、9.6 µm canvasを照合。元CTやmeshを読む前に保存中央PNGの同一x上で上側・弧・下側の三点を固定した。

法線追従1×241案は、取得前に既存観測器の単一タイル制約で停止。X(Z)折れ線案を固定して支持を確認し、既存6キーだけで原寸抽出した。
