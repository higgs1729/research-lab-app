Status: resolved
担当: 研究（219実行）
Blocked by: 218

# PHerc0800の公式二窓を同じ条件で調べ、追試すべき字画・行を選べるか（2026-11-15）

## 依頼

本人の主目標は未読文字の発見、Runpod必要分の使用は委任済み。218でPHerc0800の公式面4下方と面5上方を選び、公開中央層と計画上の座標を担当・主担当が別確認した。両窓は以前の面6全面bboxを32 voxel広げた箱の外にあり、互いにも離れる。これまでの別モデルの自動ゲート不通過を文字不存在とは解釈しない。物理ラミナと公開面生成時の正確な対応は未確定。

問いは、218で固定した二窓の全主域をHecateで一回調べ、独立した追試につながる字画・行のROIを選べるか。入力は `experiments/vesuvius/discovery/20261115-official-unread-surface-selection01/next-plan.json`（SHA256 `950fc1d327740e8ed538e3b41d244d8bcb2808830750093680006739f553d715`）。目的なく窓や深さ・モデルを増やさない。同じ16層の順逆を比較する。中間結果の数値閾値だけで原寸確認を飛ばさない。

公開表面Zarrの固定90キー45,711,360Bを長さ/ETag/218中央Rangeと照合して取得し、計画どおり全軸8.64→9.6µm、16層をfloat64 X/Y/Z補間後一回最近接偶数でuint8へ丸める。中心深さは公開15を新k=8（−8..+7の16枚）、両順は同じ16枚。対象/元4標本の幾何支持・オブジェクト存在を固定マスクで保持し、実CTの0と欠損を区別する。新しい元3D CT・重み・描画ビルド不要。主域と32px余白、64/32位相を固定し、中心層CTを別対照として残す。

217/208の入力契約・Hecate入口・クラウド管理を借り、二種の長方形と16層入力に必要な最小変更を行う。CPU参照は各窓/順の先頭3有効パッチ、計12、strictロード一回・CPU1・commit4GiB・480秒以内。GPUはFP32/TF32無効、batch1、strict一回、最大2,164パッチ。全入力ハッシュ・位置、代表確率・分子/分母・原寸出力を残す。入力と変更コードを主担当が別確認するまでPodは作らない。確認後に同じ研究で一台を起動し、回収、削除、親の別残存確認まで完了する。

取得上限48MiB/300秒、C作業1GiB・空き10GiB以上、D読取のみ。クラウド見積はSecure4090 US$0.89/時で8–12分、税別US$0.119–0.179、運用枠US$0.45（事業者の強制上限ではない）。実行前に価格≤US$0.90/時・残高・自動入金無効・既存台を再確認。絶対期限はcreate直前から25分。既存の起動240秒・入力/重み480秒・worker480秒・回収240秒・削除余白60秒の予算と内外削除を保つ。入出力gzip各24MiB、一回create・所有ID/名前のみ操作。他用途台に触れず、専用台の明細が未反映なら実費nullと稼働見積を区別する。費用の再承認は不要。

結果は4つの原図を固定階調、原寸で担当と主担当が別に確認し、続く字画・行として追試するROIを具体的に指定できるかを判断する。候補なしなら、この二窓・固定深さを閉じる。これは巻全体やインク不存在の結論ではない。入力等の不一致なら課金前に止め、必要な限定修正を根拠とともに主担当へ伝える。同研究の処理を技術上の小段階ごとに別研究へ分割しない。

保存先 `experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/`。この票に結論を追記し、コード・条件・原票・推論結果・費用/削除証拠・manifest・record候補を残す。登録済み218/217等の証拠は書き換えない。研究一件のみ、再委任なし、公開・応募・外部連絡なし。

担当はgpt-6.1-sol / highを明示して選択する。既存217/208の実証済み手順を使い、218の固定計画を解釈しながら二つの形へ適用する作業であるため。主担当は同研究の入力・数値・視覚・台残存を別確認する。

## メモ

218で対象と計画を親が採用、inbox未決0。本文は実行の依頼として凍結し、以後の経過・変更・結果は下へ追記する。

2026-11-15 JST、公式Zarrの全90キー45,711,360 Bを119.903秒で取得し、ETag、長さ、218中央Rangeを全件照合した。固定支持は面4が462,964 px、面5が371,148 px。支持した全深さで実CTの強度が0へ丸まる位置はそれぞれ4,428、4,779 pxで、欠損と区別して保存した。Hecate有効パッチは面4各469件、面5各383件。親の独立補間では全19,333,120入力値・2中心PNG・全2,164グリッドの入力契約が一致した。CPU参照12件をstrictロード1回で実行し、CPU1・commit4 GiB・監督60.403秒。入力gzipは10,870,603 B、クラウド作成0台。親へクラウド差分と凍結bundleを渡した。

## 初回作成試行の経過

二窓の全入力とCPU参照12件を凍結・検算した。初回計画の1回の作成リクエストがHTTP 400で終わり、GPU推論0件、原図0枚。字画・行の追試ROIは未判定。初回実行は技術停止し、入力を固定したまま主担当が続行可否を判断している。

## 根拠・詳細

- [一次、2026-11-15 JST] 面4の主領域は `[736,1600,960,576]`、面5は `[512,96,896,512]`。支持画素は412,428と326,968。8.64→9.6 µmのfloat64 X→Y→Z補間、公開層15を新k=8、丸め一回。両順の16層は同一。幾何・存在マスクとHecateのdepth-any支持は別に保存した。
- [一次、2026-11-15 JST] 初回の直前照会はSecure 4090在庫NONE。再照会でLOWへ戻った後も、二度はコントローラの再確認で作成前に終了した。最終直前照会はLOW、EU-RO-1、US$0.89/h、残高US$17.2133792655、自動入金無効、全Pod0。JST 01:31:31を基準に一度だけ作成を試み、HTTP 400を受けた。専用名 `r219-hecate-7a311283ffd8bcc8`、IDなし、設定した絶対期限はJST 01:56:31。書き込みリクエストの既存ログは応答の詳細を省略するため、400の理由は未確定。
- [一次、2026-11-15 JST] 既存finallyはPod IDが得られなかった場合、60秒の照会の後に削除未確認フラグを記録する。担当の別の読み取りはfinally終了後も専用名0・全一覧0・IDなしで、残高は直前と同じだった。入力転送、重み取得、GPU稼働とも0。Pod ID別の実費はnullで、残高差0は口座の観測値。
- [一次、2026-11-15 JST] JST 01:33:41の読み取り専用カタログでは、CUDA 13条件のSecure対象で在庫LOWかつUS$0.90/h以下が8種。元の4090もUS-IL-1、US$0.89/hでLOWだった。このスナップショットの段階で追加の作成は0回。

[取得原票](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/surface-acquisition.json) · [親の入力検算](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-input-check.json) · [クラウド凍結](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/cloud-plan.json) · [作成応答](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/run01/startup.jsonl) · [終了後の担当照会](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/post-create-read02.json)

[読み取り専用カタログ](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/secure-catalog-readonly.json)

親の別照会でも旧専用名0・全Pod0を確認した。主担当は同じ219を続けるため、拒否された旧作成1回に加え、Secure RTX 4000 Ada Generation（20 GB）を追加で1回だけ試すと決定。公開の二窓、入力配列、CPU参照12件、固定Hecateとworkerは同一。固定条件はFP32／TF32無効、batch 1、モデル480秒、絶対期限1,500秒。US$0.28/hを前提とした8〜15分の税別見積US$0.04〜0.08、25分上限見積US$0.117824。許容単価US$0.29/h、運用枠US$0.20。Adaでの速度は未実測。親が旧版と新版の全gzipメンバを比較し、`fixed-assets.json` のGPU・単価以外が同一と確認した。

[旧専用名の親照会](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-failed-create-check.json) · [Ada計画](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/ada-plan.json) · [Ada差分の親検算](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-ada-check.json)

Adaは在庫NONEの照会を挟み、JST 01:38:42にLOW（EUR-IS-1）、US$0.28/h、残高US$17.2133792655、自動入金無効、既存Pod0を確認。JST 01:38:44基準の追加POSTで専用名 `r219-hecate-1bbaf595bd401713`、Pod ID `4grhbmsglcz5tj` を作成した。絶対削除期限はJST 02:03:44。他の台と手元GPUは起動していない。

Adaの起動確認は当初のexec 404が2回、起動中409が38回。240秒枠までにwatchdog markerを取得できず、入力・重みの転送前に終了した。finallyがJST 01:42:48.871に削除確認（基準から244.871秒）。担当別照会は01:42:54、GET404・専用名0・全Pod0。専用課金明細0行で実費は未確定。単価と一時ディスク費による税別稼働見積はUS$0.01923。追加POSTは一回、Runpodでの本推論は両試行とも0件。

[Ada起動原票](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/run02/startup.jsonl) · [削除原票](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/run02/cleanup.json) · [別残存照会と費用](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/ada-post-delete.json)

親がAdaのGET404・専用名0・全一覧0を独立確認し、同研究を空いている手元RTX 4060 Tiで続けると決定。R191の既存CUDA環境とGPU排他を利用し、同じ二窓・16層・Hecate・CPU照合を保つ。既存重みをローカルから読み、取得や共有環境変更を伴わない。入場120秒、モデル600秒、総時間780秒、CPU1、Job commit／VRAM割当上限各4 GiB、残余RAM／VRAM各4／1 GiB。先頭3パッチ実績による時間予測を保持する。手元実機のモデル完走は191／193でも未観測。今回の手元実行前プローブはRTX 4060 Ti、PyTorch 2.13.0／CUDA 13.0を認識し、モデルforwardは行っていない。

[Adaの親残存別確認](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-resource-check.json) · [手元計画](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/local-plan.json) · [手元worker差分](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/local-worker.diff)

## 結論

手元RTX 4060 Tiで同じ二窓の有効パッチ1,704件を、Hecateで191.438秒で完走した。両者が4原図と対応する中心CTを同じ階調で原寸確認し、追試に値する字画・行のROIを選ばなかった。面4の主窓 `[736,1600,960,576]` と面5の主窓 `[512,96,896,512]` を、今回の16層に限って閉じる。物理ラミナの帰属やインクの有無は未判定。

- [一次、2026-11-15 JST] 手元FIFOには一回だけ入り、待ち0.716秒、全監督196.653秒。実機はRTX 4060 Ti／Windows PyTorch 2.13.0+cu130、CPU1、Job commitとGPU allocator各4 GiB、実測プロセスRSS最大1.685 GB、GPU予約最大0.898 GB。原cloud bundleの資産表にある4090表記はクラウド用の記録で、手元実機は結果のenvironment欄に記録した。手元の前進予測は残192.819秒で通過。終了後、親がPID 14384／4180、holder、待ち札の消滅を別確認。
- [一次、2026-11-15 JST] 面4は各順469件、面5は各順383件。正式モデルstrictロード一回、CPU参照12件との最大絶対差1.66893×10⁻⁶、最大MAE 4.66082×10⁻⁷（確率0..1）。親は全有効パッチの位置・ハッシュ、代表確率104件、全グリッドを含む2分母、4PNGの全2,416,640 DNを別検算した。
- [一次、2026-11-15 JST] 面4の順は斜め支持境界付近と局所の明部が主体で、逆では縮小・分離した。面5は両順で孤立塊の強度・位置が変わり、親が区別した局所の角・ループ状反応も、周辺に続く字画列や行を伴わなかった。定量閾値による原寸確認の省略なし。
- [一次、2026-11-15 JST] クラウドは作成POST計2回、割当1台、入力転送／GPU推論0。4090はHTTP 400でID発行なし、Ada台は起動前停止・削除の別確認済み。01:52:12の再照会はGET404・全Pod0・Adaの専用明細0行。専用実費null、税別稼働見積US$0.01923445。口座残高差US$0.0185941は口座全体の観測値。手元実行での追加クラウド支出・取得・共有環境変更なし。

[実験報告](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/README.md) · [親の数値検算](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-result-check.json) · [担当の原寸確認](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/visual-review.json) · [親の原寸確認](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-visual-review.json) · [手元GPU資源の解放](../experiments/vesuvius/discovery/20261115-pherc0800-two-window-hecate01/lead-local-release-check.json)
