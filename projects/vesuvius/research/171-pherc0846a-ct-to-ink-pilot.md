Status: resolved
担当: 研究（R171担当 2026-11-14）
Blocked by: 170

# PHerc0846Aの種点周囲512²で、固定公式モデルの連続予測を直接観察する

## 依頼

2026-11-14 JST。170では元CTとメッシュの局所対応を確認したが、紙面/割れを一意に同定できなかった。同じCT目視だけを繰り返さず、固定面の周囲を一回だけ広げて、元CTから固定公式モデルまでを通す。物理紙面の未判定は残したままの探索試験であり、誤った紙面やインク無しを前提にしない。既存カードの再現でもない。

公開meshとCTは170の同版を再利用。種点最近接のcanvas中心(1099,1099)を保持し、XY各[843,1355)の512²を取得前に凍結。linear、scale1、非反転法線、33層d=-16…16、9.362um native。別地点・深さ・モデル・強調法の探索をしない。有効幾何と必要CTの正確なキーを事前に求め、170の8キーは再利用。追加必要キーのみHEAD後にGETする。

全CT必要キー96個以下、追加CT192MiB以下、追加メタ含む194MiB、取得工程180秒、作業512MiB、C空き10GiB。新しい観測64区画と描画はCPU1/AS4GiB/core0/数値threads1、各180秒。既存R103/R123と170の取得・plan・renderを借り、新ビルドなし。上限超過なら勝手にROIを選び直さず見積もりを返す。通信は取得工程のみ。D readonly、新出力C。

保存33層を研究133/135/138/139で検証済みの公式CPU経路へ通す。公式commit47a9c37f6f8e99afdab47bb46ad425aa726f5dc0、HF ink_9um seed42 step075000 SHA e635558ae6a1a807a7e5ec1e83adfd45bc3c0ac53883ea43f1d4e085d62a9cab、robust-MAD、128²パッチ・stride64・Hann・batch1/workers0・TTA/compileなし。33層の中央17層[8,25)を保存順8→24と逆24→8に各一回。両方49patch、逐次。depthの物理向きと上流のreverse名称の同一性は未確認として記す。再標本化せずnative9.362um、公式9umモデルとの尺度条件を明記する。既存Windows CPU Torch2.14+cpu/隔離依存・通信拒否ラッパーを再利用、CPU1/commit4GiB、各120秒（R138512²の実測は各約15秒）。新weight/依存導入/GPU/学習/有料計算なし。

今回の数値検査は入力層/XY/有効域、既存170中央128²との比較、同じ保存float重みから量子化された出力といった入力・出力対応に絞る。検証済み全ソースや全依存を理由なく再監査しない。中央128²が大きく異なる場合は同じ座標の意図が成立しているかを確認してから推論する。微小浮動小数差があれば実測を残し、無条件に全ビット同一を要求しない。

CT中央層と両予測の未加工原画、固定0–255比較を保存して親に先に図パスを伝える。原寸で、独立した画のまとまり/行があるか、強反応が暗い穴や割れに偏るかを見る。教師なしのスコアからインクの真偽・受賞を主張しない。候補があればXYを固定して次の独立確認を提案、無ければこの一回は陰性/未判定として閉じ、深さ探索へ自動移行しない。

保存先 experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/。原票は上書きせず、条件・実時間/RSS・費用範囲・画像creditと結論、研究票、lab候補を残す。外部連絡/公開・サブ委任なし、登録は親。

担当は gpt-6.1-sol / xhigh を選ぶ。既存のCT取得とCPU推論を別の面・拡大ROIで接続し、取得量・座標対応・停止判断を一貫させる統合に不確実性があるため。研究は逐次、追加クラウド支出0。

## 結論（2026-11-14 JST）

[一次・実行] 固定PHerc0846Aの512²を元CTから33層描画し、中央17層を公式固定seed42へ保存順・逆順で各一回通した。中央のR170 128²は全540,672値が一致。両予測は49パッチ、合成floatから公式TIFFまで全262,144画素をそれぞれ照合した。原寸ではforwardに局所的な霞状斑点、reverseに広い明部が見えた。独立字画や行を一意に追える領域は選べず、主担当の独立目視も一致。この固定一回を閉じ、転写・深さ探索は行わない。物理紙面と先行カードの座標対応、暗い割れと反応の因果、インクの有無は未判定。[原寸比較](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/comparison.png) · [目視原票](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/assessment.json)

## 根拠・詳細

[一次] 固定canvas XY各 `[843,1355)` の全262,144点でP/N有効、中央4観測バイナリはR170とSHA一致。L0/scale1/linear、非反転法線、9.362 µm、33層 `d=-16…16`。TIFとZarr L0の全8,650,752値が一致し、中央17層には全深さ0のXYがない。再標本化なし。固定モデル、既存CPU環境、robust-MAD、128²パッチstride64・Hann、TTA/compileなし。実ログは保存層8→24と24→8、各49パッチ。`reverse` はこの保存順の呼称。[入力契約](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/input-contract.json) · [手順と実行条件](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/README.md)

[一次] uint8平均116.922/133.540、両順の平均絶対差38.518 DN、相関0.21468。≥128画素85,932/140,706、交差56,852。CT中央の暗部を記述する固定集計では単一モデル上位3%相当の暗部重複が8.96%/12.99%だった。CT暗部は割れの正解ラベルではなく、片側の高スコアをインク率とは扱わない。[比較原票](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/comparison.json) · [暗部集計](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/dark-overlap.json)

[一次・独立照合] 主担当が同じ座標のR170全540,672値、CT中央PNG全262,144値、実引数と層順、保存float和・重みからの両方向TIFF/PNG全524,288値を照合。両方向の重みは同一。製品・推論の追加起動0。[独立照合](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/lead-check.json)

## 取得と資源

[一次] 全44 CTキー。追加36のHEAD成功後、初回180秒でGET 26件52 MiBを完全保存して停止。途中本文は量不明・最大2 MiB。主担当が同じ残10件に90秒の別工程を採用し、31.861秒で完了。追加完全本文75,497,472 B、途中込み最大77,594,624 B。取得工程計約211.861秒。R170の8キー16 MiBとmesh・メタデータを再利用。幾何92.953秒、既存製品1回3.011秒、公式CPU推論17.613/16.788秒、ピークRSS744,996,864 B。作業約125 MB。新モデル、依存、ビルド、GPU、追加クラウド支出0。[取得完了](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/ct-result.json) · [資源原票](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/README.md)

## 取得途中の主担当判断

2026-11-14 JST。必要CTは全44キー・88MiBと確定し、170の8キー16MiBを再利用、新規36キー72MiBを凍結した。36 HEADは72.349秒で完了したが、GET途中で元の取得180秒上限に達して停止した。完全保存26キー52MiB、27件目の受信途中量は未記録（最大2MiB）、描画/推論は未開始。

主担当は未取得の同じ10キー20MiBだけを、別開始票・90秒上限の第2取得工程で続ける案を採用した。新規キー/座標/モデルは追加しない。保存HEADの長さ/ETagと第2工程のGETを照合し、既存入力はSHAで再使用する。元の上限内成功とは扱わず、完全保存量と途中量の上限・二工程の時間を分けて記す。無料ローカル実験の通信時間の調整で、本人判断待ちにはしない。

## メモ

- R170のmesh・メタデータを保存SHAで照合して再利用。XY各 `[843,1355)` の64幾何区画が92.953秒で完了し、262,144点すべて有効。中央の4幾何バイナリは同一XYのR170とSHA一致。CT全44キー、R170保存8キー、追加36キー75,497,472 BをHEAD前に凍結。PID/PGID・取得期限は各開始票に保存した。[幾何工程](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/geometry/stage-result.json) · [支持計画](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/plan.json)
- 追加36件のHEADは全件成功。合計180秒の取得期限でGETを停止し、26件54,525,952 Bを完全保存した。27件目の途中受信は量不明、最大2 MiB。残りは固定10件20,971,520 B。初回PID/PGID 410は回収済み。この時点の描画・推論は0。[期限停止と残キー](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/ct-deadline.json)
- 主担当は同じ固定10件だけの第2取得を90秒上限で採用。開始票に別PID/PGID 376・期限を保存。初回26件とR170の8件をSHAで再利用し、GET応答の長さ・ETagは保存HEADと照合する。[第2取得開始](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/continue-start.json)
- 入力照合でlinear指定のログ表記を誤って要求し停止した。実引数を照合して保存画像のみを再集計。推論の最初の起動は既存R138の一時ディレクトリの `mkdir` で停止し、公式推論0回。R171内の別一時ディレクトリで各方向を一回ずつ実行した。描画の再起動は0。[入力照合初回](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/input-analysis.log) · [推論前停止](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/forward-analysis.log)
- 原寸図を先に主担当へ渡し、別目視と別コード照合を受領。保存原票とlab登録候補を閉じた。[lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-ink-pilot01/record.json)
