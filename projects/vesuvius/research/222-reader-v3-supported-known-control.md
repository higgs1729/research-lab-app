Status: resolved
担当: 研究（R222、2026-11-15 JST）
Blocked by: 221

# Reader V3を十分な入力範囲の既知文字対照で再現し、未読探索に加える根拠を得られるか（2026-11-15）

## 依頼

主目標は未読文字の発見。220までのHecate未読窓では追試する字画を選べず、221のPHerc0813広域公開seed43両順の別目視でもROI0だった。新しい窓を増やすだけでなく、可読例の実績がある別の構造・前処理を評価する。189で比較済みのReader V3は、作者のPHerc0343等の可読例、公式October Progress受賞と0306B受賞での利用がある。当時見送った主因は、R175保存384²の範囲では384patch/stride192の全面支持を揃えられず、CPU実行の負担も未検証だったこと。モデルの低品質が実測されたわけではない。219/220で手元4060Tiの一回実行と期限/資源管理が成立したため、この制約を再検討する。

問いは、Reader V3を正しい入力・前処理・パッチ位相・層順で既知文字へ一度通し、既存baselineとの違いと未読面へ持ち込む条件を確かめられるか。候補選定の一般論をもう一度広く調べず、189の保存一次資料、既存0343の元CT/mesh/字画位置/公開比較を起点にする。公開作者の正規実装・現行配布から借りられる範囲を調べ、独自モデルの作り直しを避ける。モデル本体の重み/設定/完全strict loadと推論前処理を固定する。既存本文に反映されていない変更があれば必要箇所を一次で確かめる。

既存のR175主域256²には既知字画の一部しかない。主評価域は既存対照との比較ができ、終端/隣の明部を含む位置に事前固定し、必要なら受賞者の既知箱が全体で含まれる範囲を選ぶ。全面のパッチと等価な支持を周辺まで確保する。既存384²の端へzero-paddingを足しただけで全面再現と称さない。元CTや公開renderの再利用・必要範囲の追加・公開予測の直接利用など、最小で妥当な経路を選ぶ。新旧の座標/解像度/深さ/階調が異なればその差を記録し、対照を同一入力として誤比較しない。初期化からの訓練座標重複が不明な場合、既知字画の再現試験と汎化検証を明確に区別する。

最初は保存資料と新しい小本文/メタ8MiB程度以内で、具体的な入力範囲・必要通信量・重み・依存・パッチ数・CPU参照・GPU資源と所要時間・停止条件を決めて親へ示す。189の固定配布は HF domenicor046/reader-v3@aee1d64bced4eb35546348f3d276b9e2a0b99c46、reader-v3.pth 138,379,659 B、SHA ea405417450abd8ace1b8ff79ebce3adb646c5e48ab95da46844d77efe984d8a。計画採用後はこの同じ研究内で取得/実行/検証/記録まで進める。計画だけで形式的に完了しない。親のチェックは本人承認待ちではなく同一研究の別検証と投入判断。

手元GPUは既存FIFO、CPU1、commit/VRAM4GiB、空きRAM4GiB/VRAM1GiB、C空き10GiBを保つ。既存Hecate入口をモデルに適合させる際、科学処理の差分と借りたガードを分けて検証する。初回は未知面を同時に実行せず、既知対照一条件・一回の推論で十分。計算量とメモリはHecateから機械的に外挿しない。入力/CPU参照/実行ファイルが固定された段階で親の別チェックを受けてからGPUへ入れる。他作業の停止や共有CUDA環境の変更をしない。必要な依存は既存環境をまず読み、追加が必要なら隔離先と容量を示す。

Runpod必要分は本人から主担当へ委任済み。手元で成立せず外部台が妥当な場合は、ここで実験の見積もり・運用枠・台ID/起動期限/削除・残存確認を具体化して主担当が決める。別サービス有料計算、外部公開/PR/メッセージ/応募、新モデル学習は含めない。技術上の選択を本人へ繰り返し質問しない。

保存先 `experiments/vesuvius/discovery/20261115-reader-v3-known-control01/`。C書込/D読取のみ、既登録証拠は不変。研究一件、再委任なし。原図ができたら結論の共有前にパスを親へ知らせ、双方の原寸判定を独立に残す。数値整合は主張に必要なチェックを一度行い、成功した同じチェックを理由なく繰り返さない。コード/条件/出典/入力/出力/資源/費用/manifest/lab候補を残し、票に結果を追記。登録は親。

今回はgpt-6.1-sol / xhighを明示選択する。入力支持の不足を解消し、未導入モデルの前処理と実行条件を既存のGPU資源管理へ接続する手順がまだ固まっていないため。221の登録後に着手する。

## 結論

PHerc0343の受賞面をnative 8.64 µmで描画し、Reader V3で既知字画の大まかな形を再現した。右の暗部を囲む曲線と左の主明部を原図の同位置で追えた。曲線の下に分かれた明部や左の二つの細い終端は分離しなかった。主担当も原寸を別に確認した。既存モデルに対する可読性向上は未確認で、広域への優先投入は見送る。主担当は既知字画の部分再現、Hecateと異なる応答、作者の可読例と一回の負担を根拠に、未読の固定一領域へReader V3を追加する限定試験を選んだ。本研究の範囲は既知面の比較まで。 [native原寸](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/review/comparison-native.png) · [担当の目視](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/visual-review.json) · [主担当の目視](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/lead-visual-review.json)

## 根拠・詳細

- [一次、2026-11-15 JST] 既知箱9・10の全体を含むnative主域 `[1344,1088,672,448]` と、384²／stride192の全20パッチ支持 `[1152,768,1152,960]` を固定した。元CT17層は正の法線側から逆順。幾何有効1,105,920画素、17層の18,800,640 CT値が描画TIFFとZarrで一致。主担当は全支持キー135件と旧資産52件を独立照合し、別計算した45点のCT補間も確認した。XY位置を対応させた旧256²における中央CTはr=.999177、MAE .925 DN。 [入力契約](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/input-contract.json) · [幾何検算](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/lead-geometry-check.json)
- [一次、同日] 作者の配布重みを公式 `koine_machines` で構成し、同じ選択規則で508テンソルをstrict load。robust-MADの1/99、公式Hann、IEEE float32、batch 1。RTX 4060 Tiの一回で20パッチ37.345秒、CPU参照3件の最大差1.401×10⁻⁶。主担当の独立Hann集約は全1,105,920出力で最大差2.120×10⁻⁷。CPU/CUDAはそれぞれPyTorch 2.14.0 / 2.13.0。 [重みと設定](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/cpu/model.json) · [GPU原票](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/gpu/result.json) · [出力検算](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/lead-result-check.json)
- [一次・目視、同日] 共通256²ではReaderの曲線が連続し、Hecateでは強い反応が分かれた。dense-nativeにも粗い曲線が見える。Readerのスコアのみnativeから双線形に対応させると、同じ位置の公開Reader逆とr=.947360、MAE 17.350 DN。作者の中央値から99.5パーセンタイルへの変換は固定native主域の表示だけに使用し、raw階調も保存した。親は11原寸パネルと別式の共通座標65,536点を検算した。比較元は9.6 µmで深さ刻み、階調、モデル実行条件が異なる。初期重みまで含む訓練座標重複は未確認。 [共通原寸](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/review/comparison-atlas-256.png) · [画素集計](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/comparison.json) · [図の別照合](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/lead-panel-check.json)
- [一次、同日] 新規受信315,538,718 B、既存CT再利用109,051,904 B、クラウド費US$0。GPU peak reserved 664,797,184 B。終了後PIDとFIFOを親が照会し、自ジョブの残存0。隔離CUDA依存の追加は2 wheelのみ受信し、純Pythonは既存資産を複製した。4 GiBの既存Windows Jobと、他ジョブを止める動作を無効にしたFIFO入口で実行した。 [実験報告](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/README.md) · [資源記録](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/resources.json) · [終了後照会](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/lead-local-release-check.json)

[manifest](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/record.json)

## メモ

当該既知対照が成立しても、新文字・未知巻の性能・第四応募項目とは数えない。次の未読投入判断へ使う。既存三件の一件まとめ応募の方針は維持。

2026-11-15 JST。受賞面のnative 8.64 µm固定主域XYWH `[1344,1088,672,448]` に既知箱9・10の全体と旧R175主域を含めた。全20パッチの支持はXYWH `[1152,768,1152,960]`、17層を逆順に読む。観測版の64²制約により270タイルを観測。全体期限で初回136タイルまで。完了分を残し、ディスク全件集計の間隔を広げて残る134タイルを77.297秒で回収。全1,105,920支持画素に有効幾何がある。CT支持135キー、R173再利用52キー、新規83キー174,063,616 B。重み、公開単独Reader逆、隔離CP313用wheel2件を含む新規本文315,538,718 B。親の取得前確認待ち。 [入力計画](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/plan.json)

親の取得前確認後、固定素材を取得して一回描画。CPU参照3件とGPU前の独立照合を完了した。GPU監督入口でCUDAの実行ファイルパスの型不一致が起き、投入前に停止。Path変換を一行修正し、親が新旧の実行契約を再照合した後、一回の固定GPU試験を完走した。 [投入前の停止原票](../experiments/vesuvius/discovery/20261115-reader-v3-known-control01/local-verification-path-fix.json)
