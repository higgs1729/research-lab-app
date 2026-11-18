# PHerc0191 w052の原面と補正面を比較する

PHerc0191 w052の固定窓 `[0,32,2048,1024]` を9.6µmで描画し、主比較域 `[32,64,1984,960]` を原寸で調べる。R216では紙層の帰属を確認できた面が0だった。既知0343でもCTの層帰属が一部曖昧なまま字画が再現したため、w052のみを固定し、候補の有無を調べる探索を計画した。主比較域の名目面積は1.7553cm²、幾何支持は1,546,580画素。元面とsnap面は同じ場所の比較であり、一面分として扱う。 [研究票](../../../../research/217-pherc0191-fixed-pair-ink-exploration.md) · [R216の親判定](../20261114-m7-snap-local-control01/lead-unknown-visual.json)

## 入力

元XYZはR213のw052。全面格子255×56・scale 0.05で、core `[0,8,106,50)` と11-cell haloを含む `[0,0,117,56)` に上流m7 snapの既定値（±15、jump 6、sigma 1、L0）を一回だけ適用した。元格子への貼戻しと支持は親も別の計算で確認した。補正位置差の中央値1.299、95百分位5.022、最大12.171 CT voxel。これは物理的な紙層対応や他巻きとの独立性を示す値ではない。 [連続snap](snap-result.json) · [親の別計算](lead-full-snap-check.json)

m7は113キーを再使用して13キー6,624,110 Bを追加、元CTは29キーを再使用して255キー534,773,760 Bを追加した。製品描画は9.362µm CT L0、scale 0.975208342、法線方向step 1.025421977、線形補間、33層。64画素observerと128画素製品描画の浮動小数計算差が旧ガード0.002 voxelを最大0.000066 voxel超えたため、CT取得前に親確認を受けて余裕0.01へ更新した。必要キーは284のまま。親の独立CT補間では描画値との差は最大1 DN。 [CT支持](ct-support.json) · [CT取得](ct-acquisition.json) · [親入力検算](lead-input-check.json)

描画2条件とも幾何支持と中央16層の非零支持は1,596,532画素。有効patchは各条件各順1,699件、空patchは254件。Hecateのcheckpointと実装を固定し、中央16層 `[8:24]` の順逆、64²/stride32、FP32、TF32無効、batch 1を用いる。CPU参照は4条件の最初の有効3patchずつ、計12回を一度のモデルロードで取得した。 [全入力契約](patch-contract.json) · [CPU参照](cpu-reference.json)

## 専用台

91,157,638 Bのgzip入力をローカル照合し、1200秒以上を取得・転送に残す設計とした。15:34:07 UTCにSecure4090 US$0.89/時、既存残高US$17.5303355386、自動入金false、他のPod 0を確認。15:34:09 UTCに一台を一回作成した。削除の絶対期限は16:19:09 UTC。上限45分・US$0.75は運用枠。 [起動前確認](admission.json) · [作成原票](run01/launch-receipt.json) · [Runpod料金仕様](https://docs.runpod.io/pods/pricing)

作成直後のexec 404一回と409二十四回の後、152.676秒で準備確認。準備からモデル起動まで695.545秒（入力転送、固定重み取得・照合、起動を含む）。重み取得・照合は18.303秒、モデル処理365.678秒、モデル完了から削除確認まで72.780秒（結果の回収を含む）。モデル処理は準備を含むworker内の単調時計値で、UTCの区間とは端点が異なる。専用台の寿命1,284.559秒で、担当と親の独立GETは404、専用名・全一覧は0。 [起動ログ](run01/startup.jsonl) · [モデル結果](results/execution-result.json) · [削除原票](run01/cleanup.json) · [親の別照会](lead-resource-check.json)

専用台の寿命と実効単価・20GBのディスクからの見積はUS$0.31856。15:58:01 UTCの専用Pod明細は0行で、実費は未確定。口座残高のUS$0.2841550759減少は別の観測。 [請求照会](post-delete-final.json) · [資源原票](resources.json)

## 結果

4条件のGPU計6,796パッチを完走し、GPUとCPU参照12件の差は最大MAE 3.69e−9、最大絶対差5.59e−7。27,720,893 Bの結果をSHA照合して回収した。全パッチの位置・入出力ハッシュ、代表104パッチの確率配列、共通Hann分母と4分子を保存した。分母は空パッチを含む全1953位置で再計算し、全8,388,608出力画素を再生成できた。個々の確率配列を回収したのは代表104パッチ。 [担当チェック](result-check.json) · [親チェック](lead-result-check.json)

補正により予測は変化した。右上の大きな明部は分かれたり移動したりし、ゆがんだ繊維や裂け目の縁と重なる箇所がある。左側や下半分は孤立した塊が多い。担当は24原寸比較図、親は全原図と主域を覆う16原寸予測対およびCT対の一部を別に目視した。双方とも追試する字画や行のROIを選ばなかった。紙層帰属、他の深さ・別面、インクの有無は未判定。 [原寸比較図索引](review-panels.json) · [担当目視](visual-review.json) · [親目視](lead-visual-review.json) · [明度差の診断](pair-diagnostics.json)

## 由来と範囲

Carson Rodriguesの固定fitと、公式再構成 `20250821151635` のL0および対応する公式m7 L0を使用した。R209の公開加工カードは別の紙面であり、w052の比較に含めていない。同巻ですでに処理された別面があり、未公開作業の範囲とHecateの全学習座標は未確定。借用fitとCTはCC BY-NC 4.0。 [fit公開者のREADME](https://huggingface.co/datasets/rodriguescarson/eligible-scroll-spiral-fits/raw/63c641ba/README.md) · [データ由来確認](../20261114-unread-multiwinding-lane01/README.md) · [Hecate実装と学習由来](../20261114-alternative-ink-model-selection01/README.md)
