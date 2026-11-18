# R242 固定下窓の文脈観測（2026-11-16 JST完了）

旧R239画像下端の先で、太い下降部の終端と、その下の弱い反応までの暗い間隔を観測した。担当/主担当の独立原寸所見は一致し、候補を形を持つ未確認反応として保持する。閉合・独立文字・インク・全ROI同一細層・新規性は未確定、新文字0。この固定下窓で終了し、深さ/モデル/閾値/再延長による救済はしない。

正本は `research/242-pherc0211-clipped-response-context.md`。科学判定は `joint-decision.json`、独立所見は `researcher-visual-review.json` / `lead-visual-review.json`。

## 固定条件と結果

- main parent XYWH `[4352,2176,1024,640]`、support `[4272,2096,1152,768]`。R236近似tile renderer、+8..−7、同Studio soft-loss model、FP32/TF32off/batch1、全親stride64/Hann。
- CT108keysの46を再利用、62keys/130,023,424B新取得。新input SHA `dd2a67a641784a256f6eca5b79f473d74fdbde4acf42a0bc7effeb40d7dde73c`。旧との重複入力4,718,592値差0。
- H100一回、228forward、model load1。既知CPU3最大差9.23871994e-7で通過。旧A40との共通51patch全470,016値、4種重複配列各131,072値、公開入力φ96,000値が差0。GPU一般の一致へは拡張しない。
- 親は全入力/正規化/CPU3と別float64 Hannを確認し、candidate最大差2.2348257944e-7。重複全値・raw5図とguideの全画素も独立確認。
- 旧R236 pairgateはmax0.0028054118/mean0.0006942505/falseのまま。公開φは公開入力の推論対照であり、未知近似入力全体の正しさを証明しない。

## 図の入口

`review/fixed-clipped-response-raw8-native.png`（固定384×768表示）、`review/context-union-raw8-native.png`（旧+新1024×1152）、`review/context-coordinate-guide.png`（座標だけ）。新窓単独、既知φ、CT max参考を合わせて6図。raw8はR239と同じ切捨て、補間/percentile/追加ROIなし。全重複一致条件を満たしたので結合した。

## 運用と費用の区別

| 仕様 | 結果 | 科学forward |
|---|---|---:|
| A40 | NONEで非起動、案/archive保持 | 0 |
| A6000初回 | HTTP400、IDなし。原本文未保存、原因不明 | 0 |
| A6000限定診断 | HTTP400、IDなし。要求仕様に合うinstanceなしとの本文保存 | 0 |
| RTX4000 Ada | NONEで非起動、案/archive保持 | 0 |
| H100 HBM3 / AP-IN-1 | 一台完走、回収、削除/GET404/全Pod0 | 228 |

H100 ID `3spuikvh641nms`、name `r242-studio-3883a61468d540c4`。実precreate16:40:49Z、削除期限17:10:49Z、16:49:54.924Zに不在確認。担当/親の後続GET404・同名0・全Pod0、期限helper不在・未使用予約不在。失敗2件のhelperと予約も所有照合後に解放し、原ログは保持した。IDなしの失敗は既知台の削除成功/GET404とは呼ばない。

H100見積US$0.40–0.90、運用上限2.25、rate上限4.40/h。実545.924秒×4.39/hのcompute参考値0.665724 USD＋小額disk見積と、専用明細pendingを区別する。明細空を実費0とは扱わず、口座差を流用しない。`resources.json` / `h100-resource-check.json` / `lead-h100-resource-check.json`。

## 保存と再利用

`cloud-plan-h100.json` / `cloud-input-r242-h100.tar.gz` / `control_h100.py` が成功時契約。archiveは直前案からfixed-assetsのGPU/rateだけ変更、他24member不変。`ada-to-h100-code.patch` が最終運用差分、旧全案/archive/二拒否原票も保持。`capture_h100.py`だけを384MiBへ変更し旧captureは不変。C空き2GiB/CPU1/hard commit4GiB、物理回収予約64MiB。回収archiveは12,842,731B、SHA `033c2b957b04d14b071083bcd9812828de219136ddeb2fc89ffb96e6e6c235b7`。

`manifest.json` は自身を除くローカル全ファイル・研究票・外部参照を固定する。`record.json` は親の登録用。親の原文/計画/入力/実出力/表示/残存検証とruntime script/processを含む。先の部分記録 `record-be8579e1eb5e` / `record-526f22584cbd` の根拠は不変。R236–241にも変更なし。追加計算・取得・課金・再予測なし、公開/応募/連絡/登録は担当から行っていない。
