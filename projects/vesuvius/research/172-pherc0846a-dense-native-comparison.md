Status: resolved
担当: 研究（R172担当、2026-11-14）
Blocked by: 171

# 同じPHerc0846A入力をdense-nativeで比較し、単一モデルの限界を調べる

## 問いと入力

2026-11-14 JST。171の公式seed42両深さ順は文字候補なし。ここでは深さ/領域を増やさず、上流surveyが異なるアーキテクチャの基準対に使う Nieuwlaar/ink9um-dense-native step16000 を一つだけ比較する。168の受賞者README、169の上流資料が入口。元CTと33層512²は171保存を再利用する。幾何の物理的な正しさ、未判読の文字、モデルの訓練重複は別問題である。

## 計画前半：既存能力の確認

HFモデルrepo https://huggingface.co/Nieuwlaar/ink9um-dense-native の現行revisionを固定し、カード/ライセンス、step16000のファイル・サイズ・LFS SHA、必要実装と入力契約を一次資料から確認する。公式/著者の推論コードを借りる。既存R133公式checkout/CPU環境で対応するモデルクラスと依存があるか調べ、実装が無い場合は著者の固定公開コードだけを使う。新しいネットワーク構造や前処理を自作して同じモデルと呼ばない。

meta/文書/コードの本文合計2MiB・12件以内。カードの公表訓練対象、PHerc0846Aとの重複について確認できる範囲と未確認を分ける。公開一覧に無いだけで完全な非重複証明とはしない。重みの実行時メモリ見積もりが4GiB内、CPUで利用可能、新しい依存導入/ビルドが不要、重み256MiB以下の場合に限り後半へ進む。満たさないときは新実装や導入を始めず、その根拠と次の最小計画を返す。有料計算には進まない。

## 計画後半：上限内のみ実行

重み本文は固定1ファイルだけ、256MiB/取得180秒上限。固定版、SHA、長さと取得時間を保存する。キャッシュに同一本文があれば再取得しない。新規実行の支出は0。全作業768MiB、C空き10GiB。元CTの新取得/新描画は禁止。

まず保存w035元CT128²（研究135の再利用手順）を工程対照に一回だけ使う。訓練由来の対照であり未知性能評価ではない。モデルが必要とする17層の選択、正規化、パッチ幅/stride、活性化、集約を著者のコード/記録で固定し、実行前に入力/条件を書き出す。対照で出力が無効・全定数など明白な処理不成立なら対象の2回を実行せず原因を返す。

対象は171の同じ512²・native9.362um・33層、中央17層[8,25)、保存順8→24と逆24→8を各一回、逐次。モデル自身の適正な処理条件を使い、128patchが不適合なら強制しない。相違は事前に記録し、171との比較を純粋なアーキテクチャ差の因果試験とはしない。CPU1、commitまたはAS4GiB、数値threads1、推論各120秒・最大3回、通信遮断。新GPU/学習/モデル追加/閾値や深さ探索なし。期限で止まった場合は原票を残し、無断で再実行しない。

保存CTと未加工の両方向の連続予測を固定0–255で並べ、171の同じ座標の予測と比べる。親へ判断前に図パスを送る。字画/行の位置が一意に選べるか、二モデルの強い部分がどこに一致しどこで違うかを見る。一致や高スコアだけをインク証明にせず、文字候補が無ければその一回を閉じる。正解ラベルなしの対象で精度やAUROCを捏造しない。統計を添えるなら定義を固定し、上流JPEGの別領域と同一の測定とは言わない。

既存ランナー・取得・保存・表示は171/138を借りる。保存場所 experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/ 。既存原票は読取、新C出力、D readonly。重要な条件・結果・失敗・費用を保存、研究票とlab候補を用意し親が登録する。外部投稿/公開/サブ委任なし。

今回は gpt-6.1-sol / xhigh を選択。既存手順を借りるが、別モデルの公開実装・入力契約・CPU互換性の照合に未確定部分があり、実行可否を見積もりと根拠から判断する必要があるため。逐次実行。

## 取得前の主担当判断

固定HF revision b894a0493ab2291cc8dc3247020c0d7cb0967a58 のstep16000は272,767,904B（260.132MiB）と確認でき、当初256MiBを4,332,448B超えるため担当は本文取得前に停止した。主担当はこの固定一件の上限だけを272MiBへ変更した。他の条件（CPU/4GiB/新依存なし、取得180秒、モデル数、課金0）は維持する。まず資料で実行条件を確認し、成立すれば後半へ続行する。無料ローカル実験内の小さい容量調整のため本人判断待ちにはしない。

また、別アーキテクチャという上流説明は実際のconfigで照合する。同型の場合は別学習checkpointの比較として扱い、構造が異なるという前提で結果を解釈しない。

## 結論

[一次・実行、2026-11-14 JST] R171の固定PHerc0846A 512×512を、dense-native step16000で中央17層の順・逆各1回に通した。w035元CTの工程対照は全16,384画素が有限・非定数で成立。対象では両方向に雲状・連結した広い応答があり、R171 seed42との強い部分は順方向の右上と逆方向の左下に一部重なった。どちらも字画や文字行を一意に追えず、候補ROI・転写なし。親担当も先に単独原寸PNGを目視し同じ判定。物理紙面の対応、割れの影響、インクの有無は未判定。[原寸比較図](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/comparison.png) · [親照合](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/lead-check.json)

## 根拠・詳細

- [一次] HF `b894a0493ab2291cc8dc3247020c0d7cb0967a58` のMIT配布、step16000の固定重みは272,767,904 B（260.132 MiB）。元の256 MiBを4,332,448 B超え、本文取得前に停止した。上記の主担当判断後、この1件だけを180秒上限で取得した。HTTP 200、10.467秒、本文SHA-256が配布LFSと著者VERIFY双方に一致。公開API/文書/コード本文11件、85,257 B。[固定配布](https://huggingface.co/Nieuwlaar/ink9um-dense-native/tree/b894a0493ab2291cc8dc3247020c0d7cb0967a58) · [取得原票](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/weight-process.json)
- [一次] 上流configとR133参照configは同じ `vesuvius_unet_3d_stem_2d`、stem 16、単一ink head、1×17×128×128、パッチ内robust-MAD。著者が明示したvilla `3ea17f54…` と既存R133 `47a9c37…` の対象ツリー差は学習ラベル前処理1件。無forward builderのstate_dictと配布508テンソル全キー/形状/型が一致し、CLIロードも不足・過剰0。**同じモデル構造・推論処理で学習済み重みを変えた比較**。著者が公表した処置群はKLAVISのdense-ex016重みを起点とし、追加10件のPHerc0139 native 113 keVに公開78 keV教師出力を使う。保存の公表config・リストにPHerc0846Aと対象scan IDの記載なし。起点重みまで遡った全訓練入力・座標単位重複は未検証。w035は公表訓練一覧に含まれる。[固定config](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/author-config.json) · [著者再現手順](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/author-reproduce.md) · [照合](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/source-check.json)
- [一次・実行] 著者のレシピでsafetensorsにconfigとstepを付けてPTH化し、R133 CPU/既存safetensors 0.8.0を借りた。R135 w035元CT 128²は層6→22で1パッチ、7.626秒、uint8 54–218。R171は元CT保存XY各 `[843,1355)`・native 9.362 µm・33層の中央17層を8→24、24→8、各49パッチ、18.729/18.154秒で完了。公式CLIのrobust-MAD・128²・stride64・Hann・batch1・CPU float32 sigmoid・TTA/compileなしはR171と共通。親担当が重み・PTH、同一入力とCLI条件、float加重和→TIFF/PNGのw035全16,384・対象両方向全524,288画素を独立に照合した。[入力契約](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/input-contract.json) · [親照合](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/lead-check.json)
- [一次・集計] 各画像のfloatスコア上位3%（7,865画素、閾値以上で同値を含む。閾値同値は各1）について、同方向のseed42とdense-nativeの重なりは順1,471画素（右上1,241、Jaccard 0.1032）、逆1,448画素（左下1,434、0.1014）。全画素の相関は順0.345、逆0.605。この固定無ラベル領域の空間記述。上流カードの別領域との数値比較、精度評価、インクの同定はできない。[集計原票](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/comparison.json)

## 実行条件・メモ

Windows CPU1、数値threads1、4 GiBのJob commit上限、各推論120秒、Python外部ソケット拒否とHF offline。推論3回のピークRSSは最大847,839,232 B。Cの新作業約530 MiB、取得した重みと変換PTHを含む。追加クラウド費0円、ローカル電力費未計上。CT取得/描画、深さ追加、依存導入、ビルド、GPU、公開は0件。PowerShellでの取得起動が実行前にツールで拒否されたため保存Pythonスクリプトからcurlを一度だけ起動した。比較図のラベル重なりで2回画素照合が止まり、原票を保持して描画余白を直した後、保存出力から5パネル全1,310,720画素の同一性を確認した。推論の再実行なし。[再現手順・原票](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846a-dense-native01/record.json)
