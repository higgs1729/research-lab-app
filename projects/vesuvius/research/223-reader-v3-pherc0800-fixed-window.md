Status: resolved
担当: 研究（R223、2026-11-15 JST）
Blocked by: 222

# Reader V3をPHerc0800の既観測一窓へ適用すると、追試する字画候補を選べるか（2026-11-15）

## 依頼

主目標は未読文字の発見。222はnative8.64µmの既知PHerc0343でReader V3の粗い曲線を再現したが、細い終端や分離の改善は確認できず、Hecate等に対する精度優位の証明ではない。主担当は広域優先投入を見送り、異なる文脈サイズ・前処理・学習重みの応答を未知面へ一度だけ試す。222を新文字・第四応募項目に数えない。

対象は220のPHerc0800公式面4（20251028222030-auto_grown_20251028222030940）、reconstruction20250521135224。同じ既観測物理窓を使う。220の9.6µm主域XYWH [128,576,960,960]に対応するnative8.64µmの整数画素領域を、220の実際の変換式から予測を見る前に一意に固定する。境界の丸めと面積差を明示する。範囲を字画らしい塊へ寄せず、同じ窓の深さ/閾値/補正を走査しない。220のHecate両順はROI0であり、この結果はそのまま保持する。

ここを選ぶ根拠は、公式面の原native31層・格子・来歴と220の対照があり、既取得チャンクを再利用して追加量を少なくできること。モデルを変えて同じ既観測窓を比較する一試験で、未観測面積を増やしたと数えない。物理紙層の成立とインクの有無は220でも未判定。既知対照での可読性優位が未確認なので、この試験から自動的に全巻へ展開しない。

まず219/220の元native surfaceと入力契約・原点・正規のfill値/欠落情報を読み、Reader384/stride192の全面位相と主域へ寄与する全周辺支持を確保する。9.6へ再標本化したHecate入力をnativeと称して流用しない。既存公式native31層から中央17層を先に選び、同じ17枚の順逆を一回ずつ処理する。222の固定checkpoint、公式make_model/strict load/robust-MAD/sigmoid/Hann、FP32/batch1/TF32off/no TTA/no compileを借りる。大きな生データ取得やモデル実行前に、native主域と支持域、列挙キーと再利用/追加バイト、無効/欠落の扱い、パッチ数、CPU参照と実行見積もりを主担当へ示す。正規に欠落したゼロと取得失敗を混同しない。原面の幾何とモデルの非ゼロ支持も区別する。

既存入力は読取、新規受信上限64MiBを初期見積もりの目安とし、必要分を列挙して確定する。上限やパッチ数が想定を超える場合は根拠を示して主担当が判断し、欠落や周辺を任意のゼロで埋めて通さない。新規重み/依存/ビルド/面生成は原則不要。手元GPUの追加クラウド支出見積US$0。資源は既存FIFO、CPU1/commit4GiB/VRAM4GiB、空きRAM4GiB/VRAM1GiB/C10GiB、C作業1GiB、D読取。222の他Comfyを止めず自ジョブを拒否/終了するshimと修正済み入口を借りる。CPU参照は両順各3パッチ、最大差1e-4でGPUと比較。推論数に基づいてGPU入場/処理/外側期限を事前固定する。成功・失敗とも自分のPID/列/予約の解放まで確認する。Runpodが必要なら本人へ再承認を求めず主担当に具体的な見積もり・期限・専用台管理案を示す。

原native CTと二方向のscoreを原寸で保存し、raw0–255と事前固定主域のmedian→p99.5による補助表示を区別する。元画像にない字画を描き足さず、両方向一致を文字の必須条件にしない。既存Hecateとの対応では座標/深さ/標本化/モデルが違うため、出力差だけから精度優位を主張しない。候補の採否は各方向の原寸で具体的な線/字画の連続を見て判断し、主担当も担当の判定前に別目視を残す。候補がなければこの固定Reader試験を閉じる。候補が出たら先行文字・独立モデル・元CT等の検証へ送り、文字解読や受賞を宣言しない。

保存先 experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/。コード・取得元・入力・生出力・費用・実行失敗/成功・再利用手順とmanifest/record候補を残し、この票へ結論を追記する。入力準備と試験を同一研究内で最後まで進め、計画だけで完了しない。登録済み222/220は不変。外部公開/PR/連絡/応募・学習なし。研究一件、再委任なし、lab登録と次の選択は主担当。

今回はgpt-6.1-sol / highを選択。222でモデル/公式前処理/CPU-GPU照合/ローカル入口が成立したため、その手順を別の既存native surfaceへ適用する。主な判断は有限窓の対応・周辺支持と欠落の解釈。222はrecord-a519457e3a2aで登録済み、inbox未決0を確認して着手する。

## 結論

PHerc0800公式面4の既観測窓をReader V3で順逆各一回調べ、担当と主担当の別原寸判定で追試する字画・行のROIは0件。順は孤立斑と下端の幅広い点列、逆は左上の斜め明部と左下の太くにじむ分岐が目立った。各方向で字画や行の連続を追える箇所は選べなかった。この窓の固定17層試験を閉じる。インク有無、物理ラミナ、Hecateとの精度差は未判定。 [担当の原寸判定](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/visual-review.json) · [主担当の別判定](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-visual-review.json)

## 根拠・詳細

- [一次、2026-11-15 JST] 9.6 µmの旧主域 `[128,576,960,960]` をR220の中心合わせ式でnative 8.64 µmの `[142,640,1067,1067]` に対応させた。離散化による差は+0.0530924544 mm²（+0.0625098%）。384／stride192の全面位相で文脈域 `[0,384,1536,1536]`、49位置／順。公式native31層から中央17層（7～23）を切り出し、その同じ17枚を反転した。試験対象に加えた新規観測窓は0。 [固定計画](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/plan.json) · [取得前の別照合](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-scope-check.json)
- [一次、同日] 必要144キーを列挙し、掲載済み118件を照合。91件46,219,264 Bを再利用、27件13,713,408 Bを9.627秒で新規受信し、26件は公式一覧・fill値に基づく正規ゼロ。主域の幾何proxy 965,983画素、元オブジェクト存在1,067,923画素、17層非ゼロ961,223画素。全主域にHannの加重値があり、うち70,566画素はオブジェクト不在の正規fill。元画像・幾何proxy・加重値を独立に保存した。 [取得](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/surface-acquisition.json) · [入力](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/input-contract.json) · [親の入力検算](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-input-check.json)
- [一次、同日] 公式raw-anyで完全ゼロ1位置を各順のforwardとHann分子・分母から除き、RTX 4060 Tiで各48／計96 forwardを144.068秒。CPU6参照との最大絶対差2.5629997×10⁻⁶、親の独立Hann再構成は全4,718,592値で最大差1.86872×10⁻⁷。GPU予約ピーク664,797,184 B、専用launcher・worker PID、待札、holder、予約の解放確認済み。クラウド費US$0。 [実行原票](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/gpu/result.json) · [親の出力検算](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-result-check.json) · [解放](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/resource-release-check.json)
- [一次・目視、同日] native中央CTと両方向のraw、固定主域中央値→99.5パーセンタイルの補助表示を原寸で確認。親はCT・マスク・スコアを含む10 PNGの全画素を照合した。補助表示のfloat64再現との差は逆順1画素1 DNで、実行のfloat32規則で一致した。HecateはR220のROI0を保持。位置対応の参考図を作り、標本化・深さ・モデルが異なる点を付記した。 [原寸と階調](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/review-panels.json) · [PNGの別照合](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-panel-check-v2.json)
- [一次、同日] 埋め込みPython初回はimport失敗で、モデルforward前に資源解放。222の入口設定を復元して実interpreterのimport-only確認後に完走した。また、保存ログの同名キーがactive行とCPU参照行の入力raw SHAを確率SHAで上書きしていた。推論直前の入力照合を行う固定コードと、全位置の入力SHA契約は保持されている。後処理で入力98パッチと出力確率のSHAを別に検証した。 [実験報告](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/README.md) · [初回起動](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/attempts/01-embedded-script-path/local-exclusive.log) · [初回後処理](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/review-first-attempt.json)

[資源記録](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/resources.json) · [manifest](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/record.json)

## メモ

2026-11-15 JST。220の変換式で画素セル境界を写し、半開区間に入る整数中心を選んだ。native主域 `[142,640,1067,1067]`、全面位相の49位置／順、支持 `[0,384,1536,1536]`。公式の完全一覧と取得原票から144キーのうち91再利用、27新規、26正規fillと固定。初版を保存し、親の公式コード確認を受け、raw-anyが偽のパッチは公式と同じくforward・Hann分子・分母から外すよう、通信・モデル実行前に訂正した。親の別確認後に取得へ進んだ。 [固定計画](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/plan.json) · [初版](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/plan-scope-v1.json) · [親の取得前検算](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-scope-check.json)

27件13,713,408 Bを9.627秒で取得し、長さ・ETag・MD5・SHA-256を照合。native31層を原値で組み立て、中央17枚を先に切り出した。空のindex 0を両順で外し、推論前に固定したCPU参照は両順index 1/25/48の計6件。CPU1・Windows Job 4 GiB・strictロード1回で監督35.096秒、最大RSS 1,115,062,272 B。親は全73,138,176 native値と40,108,032入力値、両順98ハッシュを別照合した。 [取得原票](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/surface-acquisition.json) · [入力契約](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/input-contract.json) · [親の入力検算](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/lead-input-check.json) · [CPU契約](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/patch-contract.json) · [GPU凍結](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/local-plan.json)

初回のローカルFIFOは配布Pythonのモジュール検索パスで終了した。CUDA文脈・モデル構築・forwardはいずれも0。旧launcher PIDと子プロセス、予約・待札・GPU保持の消滅を確認した。222で実証済みの検索パス設定を入口へ戻し、同じ配布PythonでCUDA非初期化のまま公式モデルと前処理のimportを確認。入力・科学処理・制限・CPU参照を維持し再凍結した。 [入口失敗原票](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/attempts/01-embedded-script-path/local-exclusive.log) · [初回解放](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/attempts/01-embedded-script-path/resource-release-check.json) · [修正入口のimport](../experiments/vesuvius/discovery/20261115-reader-v3-pherc0800-fixed01/cuda-entry-smoke.json)
