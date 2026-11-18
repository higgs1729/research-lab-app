Status: resolved
担当: 研究（R248 gpt-6.1-sol / xhigh）

# 既知文字を覆う手直し前後の面を、他の条件を揃えて比較できるか（2026-11-16）

## 依頼

R247は未受賞1218/0358/1203の三案を即時推論に採らなかった。外部担当Claudeの `board/posts/20261116-1236-claude-discovery-allocation-advice.md` 案1を入口調査として採用する。PHerc0211は受賞済みで、R244の既出候補は閉じたまま。今回は新発見/既読範囲探索ではなく、既知文字が紙面の手直し前後でどう変わるかを比べる対照の成立性を調べる。

問い：公開一次資料に、同じ既知文字領域を覆う、手直し前の自動fit/成長面と手直し後の面が固定版付きで存在し、同じ描画・深さ・モデル・前処理で面だけを変えた比較を準備できるか。Claudeは受賞者の緑枠4cm²/11字を例にしたが、その原寸座標が一意に特定できなければ、保存済みの既知小φなど比較可能な範囲を優先してよい。複数のmanual版があるだけで、自動→手直しの対と呼ばない。

先に控えと既済原票を読む。R229〜235の面/原入力/Studio条件、R236〜238の1DN差と確率対照失敗、R239の公開小φと近似未知の分離、R243の親v6と別manual v9対応の未確定、R244の公式既出判断が関係する。R235〜244がすべて受賞者のどの面を使ったかはClaudeの未確認部分なので実物で確かめる。同じ資料の大規模再取得をせず、保存されたDrive目録と元メタ/XYZを再利用する。

この一件では公開版の来歴・提供範囲・座標と、有限比較の設計まで。必要なら小さなXYZ/metadataから重なりを調べてよい。新しいfit、面の手直し、CT voxel取得、モデルforward、GPU、ビルド、学習、有料計算、外部投稿は行わない。初期本文64MiB/単体16MiBまで。Cへ新規保存、D読取だけ。数値処理が要れば既存run_windows.pyでCPU1/4GiB、原ファイルと型/shape/有効マスクを保存して読み戻す。固定版が無い/自動面なし/同じ紙面へ対応しないなら、その制約を正直に残し、比較を無理に成立させない。自己生成の粗い面や人工摂動を手直し前データの代わりにしない。

後続実験案は、何が唯一の介入変数になるか、既知文字の保持をどの元画像で二者が判断できるか、座標/層順/描画とモデルの交絡が残らないか、追加量と停止条件を具体化する。公開過去の確率画像との完全一致を成功条件としてR236〜238を再試行しない。新たに共通rendererで両面を描画する案なら、修正後面が同じ既知文字の主要形状を再現することを対照とし、旧公開画素との違いは残す。解釈はその一領域の字画保持まで。残る/消えるをもって未受賞巻全体の律速を場所/面へ二分しない。

保存先 `experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/`。本票へ結論と根拠を追記してresolved。重要な対応図は主担当が別確認し、lab登録と後続の採否を行う。一件のみ、再委任なし、主担当/heartbeat変更なし。外部のIssue待ちではなく、公開の対の可用性という具体的な入口を調べる仕事。

今回の担当はgpt-6.1-sol / xhigh。原資料・既存の取得/座標照合手順はあるが、自動面とmanual版の来歴、同一物理範囲、交絡を除いた比較の成立に不確実性があるため。新しい広域探索や新基盤実装を任せる依頼ではない。

## 結論

2026-11-16。**確認した公開範囲では、手直し前後の一対を用意できない。** 受賞者の緑枠の図は公開 v9 の二行目の CT と近似対応し、既存の小 φ（v9 XYWH `[4640,780,320,300]`）が緑枠内に入る。一方、v6/v9 のメタが参照する手直し前の元面 `PHerc0211-spiral-stitch-rev01-crop-20261022-1711` は、版を固定した XYZ として特定できなかった。字画の保持や消失は未判定。 [調査報告](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/README.md) · [受賞者図と v9 の対応](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/winner-panel-v9-ct.png)

## 根拠・詳細

- [一次・計算] 受賞者 fig01 の3区間と v9 の CT テクスチャは同じ縮尺 .306 と位置に対応した（NCC .789/.727/.687）。緑枠の近似 v9 XYXY は `[859,725,4974,1197)`。公開 v6-line2 の同じ照合は変換が揃わない。主担当も原図と XYZ から独立に対応を確認した。fig02 は Vincent Lemonnier の掲載図で、R244 候補の公式既出判断の根拠はこの図。受賞者図との区別を確認した。 [公式記事](https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211) · [計算](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/figure-registration.json) · [独立照合](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/lead-check.json)
- [一次・推論] R241 保存の Drive 66件と著者 repo 目録、公式 S3/spiral dataset、別著者の固定 fit 報告・公開目録を確認。v6 親と v9 は別々の manual スナップショット。旧 P737 grown にも手作業が入り、既知 φ の座標支持とは Y で899.14 voxel離れる。旧3305の source-tifxyz は manual 拡張済み。Bryant Le の報告は z10000–11000 で、v9 全体 Z 上限9312.36と非重複。公開前面の不存在までは確定しない。 [来歴・範囲](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/README.md)
- [一次・推論] R235 は v9 の局所 CT、R236–238 は v6 手直し後の同親面の描画差、R239–242 は v6 の公開単行対照や親面、R243 は異なる manual 版間の不完全な幾何対応。1 DN の差と旧確率 gate 不通過を面変更の効果に数えない。
- [推論] 元面の固定版/SHA と同じ紙面への登録が得られた場合、小 φ 一領域を共通チャート、CT、renderer、層順、モデル、前処理で比較できる。まず v9 の固定原寸資料で確認できる主形状が共通 renderer の後面でも保たれることを二者で確かめる設計。両面合計72 forward、追加 CT は最大8キーの条件案を保存。紙面の対応や後面の再現が成り立たなければ停止する。解釈は当該字画の保持まで。 [条件付き比較](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/README.md#条件付き比較)

## 取得の経路

R234 の原図・v6/v9 ZIP・公開確率と、R241 の Drive 目録を再利用。公開 HTTP で補って保存した目録・テキスト・メタの本文は2,027,363 B、最大単体833,292 B。v9 の XYZ と有効マスクの shape・dtype・SHA を記録して読み戻した。CPU1/commit4GiB。新 CT、モデル取得・forward、GPU、ビルド、学習、費用、外部投稿は0。 [取得原票1](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/acquisitions.jsonl) · [取得原票2](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/followup-acquisitions.jsonl) · [座標資料](../experiments/vesuvius/discovery/20261116-surface-pair-feasibility01/coordinate-evidence.json)
