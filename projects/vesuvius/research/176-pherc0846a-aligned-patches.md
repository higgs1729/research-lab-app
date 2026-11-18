Status: resolved
担当: 研究（R176、2026-11-14）
Blocked by: 175

# PHerc0846Aの保存CTを固定の全面パッチ位相で見直す

## 依頼

2026-11-14 JST。171/172ではPHerc0846Aの一領域に字画/行の候補がなかった。一方175の既知PHerc0343対照では、同じCTでも128patch/stride64の開始位置を全面へ揃えると公開予測への対応が大きく変わった。この新しい根拠に基づき、保存したPHerc0846Aを一意な全面0位相で一度だけ見直す。陰性の入力へ根拠なく設定探索を重ねるものではなく、今回の対照で分かった要因を取り除く。再検査後に候補がなければこの固定入力の位相・深さ・閾値探索を閉じる。

171の33×512²、canvas XYWH [843,843,512,512]から、新規取得なしで含まれる最大のstride64整列正方形 [896,896,448,448] を取り出す（元local[53,53,448,448]）。中央17層[8,25)、両順8→24/24→8を既存seed42とdense-native各1回、計4回のみ。128patch/stride64/Hann/CPU float32/batch1は維持し、各36パッチの契約を起動前に保存。448は128の倍数でないのでZarr端チャンクの格納paddingと論理形状を区別し、モデルが読む全論理画素が元CT部分配列と一致することを確認する。通常のZarr保存機能か既存の正しい端チャンク規則を借り、画素を補間・拡大縮小しない。

主比較は境界を除くcanvas [960,960,320,320]、新local[64,64,320,320]。この内部を支える全面stride64のパッチがすべて含まれることを確認する。比較対象は171/172の同じXY、同モデル・同方向。固定0–255の448²原画とCTを保存し、主担当にも判断文前に図を渡す。独立した字画・行の候補が見えるか、旧とどう違うかを判定。値や相関の変化だけをインク証明にしない。正解ラベルや公開生予測がないため精度は算出しない。先行カードの黄色との正確な登録や物理紙面を今回確定したと扱わない。

175/173の公式ランナーと入力/加重和保存を再利用。新CT/mesh/モデル/コード取得・描画・依存/ビルド・GPU・課金0。CPU1/commit4GiB/threads1/通信拒否、各推論120秒、作業128MiB、C空き10GiB、D読み取りのみ。保存先 experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/ 。登録済み171/172/175は読取。標準実行器の再監査をせず、新しい部分配列・支持と出力に絞って確認する。

研究票へ結果/限界/資源を追記しlab候補を用意。外部投稿/公開/サブ委任なし、登録は親。今回は gpt-6.1-sol / high を選択。直前175の手順を、固定入力と一意な新cropへ適用する限定実験であるため。175完了後、逐次実行。

## 結論

[一次・実行と目視、2026-11-14 JST] PHerc0846Aの同じ保存CTを全面のstride64位相に揃え、固定448²でseed42とdense-nativeの両層順を各一回実行した。整列後も独立した字画や行の候補は確認できなかった。旧出力との共通内部320²では、とくにseed42の明暗分布が変わった。dense-nativeは旧と概形が比較的近く、淡い帯や局所的な塊が残った。この固定入力での位相・深さ・閾値探索はここで閉じる。[seed42原寸比較](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/comparison-seed42.png) · [dense-native原寸比較](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/comparison-dense.png)

## 根拠・詳細

- [一次] 研究171の33×512²、canvas XYWH `[843,843,512,512]` を元に、stride64の開始・終端で完全に入る最大の正方形 `[896,896,448,448]` を切り出した。元のローカルXYは `(53,53)`。旧位相mod64は `(11,11)`、新位相は `(0,0)`。新Zarr v2の論理形状は33×448×448、物理チャンクは33×128×128。端は0で格納し、物理チャンクにある論理形状外2,027,520値は推論用の論理配列には含まれない。推論と同じ既存Zarr 3.1.5で読み戻した全6,623,232値が元の部分配列と一致した。初回のreadbackは既存CRC32Cの検索パス不足で停止したため、公式ランナーが使う既存パスを追加し、保存チャンクを上書きせずに再照合した。[入力契約](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/input-contract.json) · [準備初回ログ](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/prepare.log)
- [一次] 共通内部canvas XYWH `[960,960,320,320]` に支持が届くパッチは、2240²全面の各軸896〜1216を64刻みとする36個。128²のHannは端でも0.001以上なので、交差するパッチの全支持を数え、36個がすべて448²に収まることを確認した。全四実行の保存重みは同じSHA-256で、独立計算との差は最大3.04×10⁻⁷、内部全画素の重みは0.97572〜1.00300。画像の比較は旧171/172と同一canvas XY・同一モデル・同一層順で行った。[固定位置](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/patch-plan.json) · [比較結果](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/comparison.json)
- [一次] 中央17層 `[8,25)` のforward 8→24、reverse 24→8。既存のseed42とdense-nativeの各checkpoint、公式CLI、128パッチ、stride64、Hann、CPU float32、robust-MAD、batch1を再利用。全実行が36パッチ・終了0で、保存PNG/TIFFの全画素と固定0–255の原寸図パネルを照合した。中央CTはd=0を同じXYで別保存した。[中央CT](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/ct-centre.png)

| 共通内部102,400画素の旧と整列後 | 相関 | 平均絶対差（DN） | 符号付き平均 新−旧（DN） |
|---|---:|---:|---:|
| seed42 forward | 0.4882 | 26.501 | +9.012 |
| seed42 reverse | 0.4398 | 31.802 | −10.264 |
| dense-native forward | 0.8453 | 9.256 | −2.019 |
| dense-native reverse | 0.8818 | 7.495 | −0.409 |

[一次・目視] seed42は整列後に幅のある明暗塊の配置が変わる。dense-nativeは旧と共通する広い斜めの帯や局所塊が見える。いずれも判読に進める独立した筆画や行を指せなかった。旧との相関は出力の位相感度を記述する値。正解ラベルと座標登録済み公開生予測がないため精度は算出していない。先行カードの黄色と今回のスコアの対応、物理紙面、インクの有無は未判定。[原寸比較図](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/comparison-seed42.png) · [目視記録](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/assessment.json)

## 実行条件と限界

既存Windows 1CPU・Job commit 4 GiB・数値1スレッド・外部通信拒否、各推論120秒上限。四実行は逐次で、seed42 forward/reverse 14.193/13.311秒、dense-native 13.072/14.817秒、最大RSS 848,281,600 B。新規取得・CT描画・モデル再取得・導入・ビルド・GPU・追加費用0。比較は既存の一面、一領域と中央17層に限る。[再現入口](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/lab-record.json)

## 主担当の別照合

[一次] 主担当は両モデルの原寸図を別に見て、整列後も独立字画や行の候補が確認できないと判断した。元部分配列の全6,623,232値、論理形状外の2,027,520値のゼロpadding、全面パッチ開始点から求めた共通内部の全36支持、四条件の相関・MAEを別計算して一致した。この固定入力の設定探索を終了した。[別照合コード](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/lead_check.py) · [別照合結果](../experiments/vesuvius/discovery/20261114-pherc0846a-aligned01/lead-check.json)
