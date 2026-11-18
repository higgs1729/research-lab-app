# PHerc0800公式面4の既観測窓でReader V3を比較

担当と主担当が独立に原寸を確認し、追試に回す字画・行のROIは両者とも0件。この固定Reader試験を閉じる。紙層の帰属とインクの有無は未判定。 [担当の原寸判定](visual-review.json) · [主担当の別判定](lead-visual-review.json)

[研究票](../../../../research/223-reader-v3-pherc0800-fixed-window.md) · [固定計画](plan.json) · [入力契約](input-contract.json) · [パッチ契約](patch-contract.json) · [レビュー図の座標と階調](review-panels.json)

## 座標と支持

対象はPHerc0800、公式面4 `20251028222030-auto_grown_20251028222030940`、再構成 `20250521135224`。R220がHecateで検査した9.6 µm主域はXYWH `[128,576,960,960]`、ROI選択は0件。R220では元2580×2580・目標2322×2322の配列幅から、native中心を `(t-(2322-1)/2)*(10/9)+(2580-1)/2` と求めた。

旧主域の画素セル境界を写すとnative Xは `[2551/18,21751/18)`、Yは `[1279/2,10237/6)`。各半開区間の整数中心を選ぶため、両端をceilにして `[142,640,1067,1067]` とした。セル面積は84.934656から84.9877484544 mm²へ0.0530924544 mm²増（+0.0625098%）。差は離散化による。研究上の新規観測窓の加算は0。

全面384×384／stride 192の位相を原点0で作り、末尾の端揃えパッチも含め主域と交差する位置を選んだ。X開始は0から1152、Y開始は384から1536、各192刻み。文脈域は `[0,384,1536,1536]`。元公式Zarrの配列契約はZYX、L0の全軸8.64 µm、翻訳0、31層、`[31,128,128]`、非圧縮uint8、C順、fill 0。元31層のうち7～23を切り出して、その同じ17枚で順逆を作った。中央15。順逆は公開配列の添字の順序で定義し、物理法線の紙表裏は未確認。

## 入力・実行

[一次、2026-11-15 JST] 144キーのうち、公式一覧にある118件を検証。R220 83件とR219 8件をその場で読み、46,219,264 Bを再利用。27件13,713,408 Bを9.627秒で新規取得した。掲載予定ファイルの欠落や内容不一致で組み立ては停止する。26キーは完全公式一覧からの不在を確かめ、公開Zarr規定のfill 0で読み込んだ。元CTの追加取得・面生成・新規依存・新規重みは各0。 [取得原票](surface-acquisition.json) · [公式出典・キー](plan.json) · [取得前の別照合](lead-scope-check.json)

主域1,138,489画素のうち格納オブジェクト存在1,067,923、公開Zarrの不在fill 70,566、幾何proxy 965,983、17層のどれかが非ゼロ961,223。格納済みで全17層ゼロの106,700画素のうち4,760画素は幾何proxyの内側。幾何proxyは、既存TIFXYZの有限非負4頂点をR218の中央寄せ対応式で判定したもの。配置作成時の正確な3D対応や物理ラミナの帰属は未判定。入力の全格納値はそのまま保存し、幾何proxyを推論マスクには使わなかった。 [native31・各マスクの資産表](input-contract.json) · [入力の別照合](lead-input-check.json)

公式 `OmeZarrBlockDataset` のraw-anyが偽のindex 0は、公式dispatchどおりforward・Hann加重分子・分母から除外。各順49位置のうち48件が有効で、CPU6は各順の先頭／中央／末尾index 1/25/48。R222の固定checkpoint `ea405417450abd8ace1b8ff79ebce3adb646c5e48ab95da46844d77efe984d8a`、公式 `make_model`、strict、robust-MAD、sigmoid、Hann floor 0.001を借りた。IEEE FP32、batch 1、TF32・TTA・compileは無効。CPU1、Job commitとGPU allocator各4 GiB。GPU入場／モデル／外側120／300／480秒。既存の他ジョブ停止を抑止するshimを使用した。

## 起動の再現

結果と原票は各工程で排他的に新規作成する。再試験には別保存先と、その入力・実行ファイルに対応した別の検証原票を使う。

1. `python -B plan_scope.py` で入力範囲を固定し、親の取得前別確認後に `python -B native_input.py receive` と `python -B native_input.py assemble` を実行。
2. `python -B reader_worker.py select` で有効位置とCPU参照を固定し、`python -B cpu_stage.py` でCPU参照を計算。
3. 予約前に実際の配布Pythonで `local_gpu.py smoke` を直接実行。PowerShellで `CUDA_VISIBLE_DEVICES` を空にし、固定 `local-plan.json` の `cuda_python` と同じ実行ファイルを `-X utf8 -B -u` で呼んだ。CUDA非初期化、モデル構築0、forward 0で固定公式importが通ることを確認。次に `python -B local_gpu.py freeze`。
4. 実行契約の別確認後、`python -B local_gpu.py supervise` → `python -B finalize.py release`。成功時に `python -B review.py` で座標を保った画像と数値の検証を生成し、双方の別目視を保存して `python -B finalize.py finalize`。

初回のGPU用直接起動は埋め込みPythonの `._pth` により `plan_scope` を見つけられず、CUDA初期化・モデル構築・forwardの前に終了。初回FIFOの解放後、R222と同様に入口冒頭で実行ファイルのディレクトリを `sys.path` に入れ、上の実interpreter smokeと親の新旧SHA照合を通した。R187の標準入口によるCPU `runpy` の確認範囲には、この埋め込みインタープリターからの直接起動が含まれていなかった。 [初回のログ](attempts/01-embedded-script-path/local-exclusive.log) · [初回資源解放](attempts/01-embedded-script-path/resource-release-check.json) · [実interpreter smoke](cuda-entry-smoke.json) · [再凍結の別確認](lead-local-entry-fix-check.json)

## 完走・出力確認

[一次、2026-11-15 JST] RTX 4060 Ti、Windows PyTorch 2.13.0+cu130で1回のモデル工程144.068秒、順逆各48・計96forward。監督149.845秒、FIFO待ち0.713秒。PyTorch 2.14.0 CPUで6参照、最大差2.5629997×10⁻⁶。GPU予約ピーク664,797,184 B、GPU worker最大RSS 1,275,097,088 B。専用の子・launcher PID、待札、holder、予約が消滅した。追加クラウド費US$0、電力費は未計測。 [GPU原票](gpu/result.json) · [監督](local-supervisor-result.json) · [資源解放](resource-release-check.json)

別式のHannによる再集約で、両順の文脈域合計4,718,592値のスコア差は最大2.38419×10⁻⁷。主域1,138,489画素に両順とも加重値があり、そこには公式Zarr不在fillの70,566画素も含まれる。周辺の入力を含む推論から得たスコアなので、元CTの格納有無と加重値を別々に確認できるようにした。

パッチログ内の `raw_sha256` は、推論直前の入力契約確認後に、保存確率の生配列SHAで上書きされていた。CPU参照の行でも同じで、全入力位置の契約行には入力SHAが残る。後処理は元17層から両順98パッチの入力SHAを再計算し、出力の生配列SHAと別に照合した。実行コード、原票、予測値を保存したまま、レビュー生成をやり直した。 [初回後処理](review-first-attempt.json) · [検証・全画像](review-panels.json)

原寸は中央CT、raw 0–255、各方向の固定主域median→p99.5を保存。補助表示の端点は順 .251620／.422467、逆 .253940／.525742。9.6 µm参考図はReaderスコアをR220座標へ双線形で写し、Hecate側は元画像の960×960主域をそのまま切り出した。深さ、標本化、文脈とモデルが異なり、照合は同じ窓の位置対応に限る。 [中央CT](review/native-ct-centre.png) · [順 raw](review/native-forward-raw.png) · [逆 raw](review/native-reverse-raw.png) · [順補助表示](review/native-forward-median-p995.png) · [逆補助表示](review/native-reverse-median-p995.png)

順の右上から右中に強い孤立斑があり、下端の点列は幅が広く、字画の芯が続かなかった。逆の左上の斜め明部と左下の下向きと右へ延びる反応は太くにじみ、端や枝を分離できなかった。各方向の形で判断し、両順一致は基準にしなかった。親の独立集約では4,718,592値の最大スコア差1.86872×10⁻⁷、uint8出力は全値一致。親は原寸10 PNGをfloat32規則で全画素照合した。float64再現との差は逆順補助表示の1画素1 DNだった。 [親の別集約](lead-result-check.json) · [親のPNG照合](lead-panel-check-v2.json) · [親の解放確認](lead-local-release-check.json)

[資源](resources.json) · [manifest](manifest.json) · [lab登録候補](record.json)
