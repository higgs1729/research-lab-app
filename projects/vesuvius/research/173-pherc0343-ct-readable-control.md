Status: resolved
担当: 研究（R173担当、2026-11-14）
Blocked by: 172

# 既知PHerc0343の字画を元CTから二つのモデルで再現できるか

## 依頼

2026-11-14 JST。主目標は本人決定の未読文字発見。研究168では受賞面由来の公開ensemble画像に字画が見えたが、手元の元CT→推論工程で確認した既知文字はPHerc0139の訓練由来w035だけ。171/172はPHerc0846Aの固定領域で候補なしだった。次の探索へ投資する前に、同じ二checkpointの元CT工程が既知PHerc0343の字画を捉えるか、一つの既知領域で調べる。未知性能評価・新発見とは扱わない。

研究168の固定atlas ac5ffd7098120368216948c4e06c494bf8e67178、surface kbh-POS_PHerc0343_erwin、survey固定1f12c1ceb14c1f24acc48249eaad60bcdf541721が入口。保存のnative-main-left.pngの逆方向に曲線・輪・縦画の連なりがある。結果を見る前の領域はatlas上XYWH [1320,980,512,512]、中心[1576,1236]とする。この既知字画領域を物理CT座標へ結び、既存rendererで一つの固定入力を作る。公開atlasはcanvas9.6um/CT8.64um/render_scale0.9、法線深さstep1.111であり、native CTの画素座標と無条件に同一にしない。

最初に保存メタデータ・公式/著者のコードで幾何・原点・縮尺・深さ方向の対応を確認する。新しい描画アルゴリズムは作らず、既存公式rendererと170/171の資源制限つき観測/取得を借りる。atlasと同じ格子を既存機能で表現できるなら同じ格子を使い、できない場合は同じ物理領域をnative8.64umで覆う一意な512または576四方へ座標変換して実行前に固定し、相違を明示する。画像の恣意的な平行移動・回転や予測を見た後の位置変更はしない。座標対応を根拠つきで一意に確定できない場合はCT本文を取らず、不成立点と最小の次案を返す。

必要なら同じatlasの中央窓c+0_s1_reverseにあるseed42とdense-nativeの公開PNG各1枚を取得できる。固定の原寸領域で単独モデルの字画が見えるか比較し、自前推論と混同しない。著者モデル版/入力契約とatlasの版/処理が異なる場合は同等再現と呼ばない。保存したct_mid/ensemble/資料は再取得しない。訓練由来について公表記述と確認済み範囲を分け、受賞者の新規性は再検証しない。

元CTは公式PHerc0343 volume20250521140437-8.640um-1.2m-116keV-masked.zarrに限定。本文取得前に全必要キー・容量と入力条件を記録する。本文枠はmeta/文書/コード12件2MiB、固定mesh3TIFF計16MiB、公開モデルPNG2枚計16MiB、CT192MiB。取得全体600秒、必要キーが上限超過なら本文取得前に親へ返す。通常の通信障害は原票を保存し、同じ未完了キーの範囲で残り時間内のみ再取得できる。別領域・新モデル・新ビルド・依存追加・GPU/有料計算は含めない。C空き10GiB、作業1GiB、D読み取りのみ。

元CT描画は一回、33層（中央を一意に固定）、幾何観測は推論前に完了。CPU1、ASまたはcommit4GiB、threads1、取得後はネットワーク分離。公式推論は保存済みseed42と172のdense-nativeの二つ、中央17層の両深さ順で各1回、計4回まで、各120秒。既存の入力SHA/加重和/連続予測保存を再利用。モデル失敗や入力無効なら先の呼出しを止める。

元CT中央層、二モデル両順と必要なら公開対照を、座標・縮尺を明記した未加工0–255の比較図で見せる。読み取り補助の別表示を作る場合も原画を保存し変換式を明示し、字画を描き足さない。親へ判断文の前に図パスを送る。どの方向で既知字画に対応する形が見えるか、複数の線や輪を区別できるか、原画に対応しない反応や粒状模様にとどまるかを述べる。正解画素ラベルなしに精度数値や未知性能へ外挿しない。見えない場合も同じ領域の深さ/閾値探索はせず、工程・領域対応・モデル感度のどこまで確定したかを残す。

保存先 experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/。研究票に結果追記、コード・入力参照・条件・成功/失敗・費用とlab候補を用意。外部投稿/公開/サブ委任なし、登録は親。追加クラウド支出0円。

今回は gpt-6.1-sol / xhigh を選ぶ。既存手順の再利用だが、別atlas格子と公式rendererの物理座標対応が未確定で、その解釈と実行可否判断が必要なため。研究172完了後、逐次実行する。

## 結論

[一次・実行、2026-11-14 JST] **元CTから既知字画の部分形状を再現した。** PHerc0343の固定atlas領域を元CTから描画し、dense-nativeの逆方向出力で公開単独denseおよび公開ensembleと同じ位置の曲線・囲まれた暗部を追えた。周辺は太くぼけ、複数の独立字画や文字列の判読・転写には至らなかった。seed42の逆方向では明部が分かれ輪の閉じ方が弱く、両モデルの順方向でも対応形が弱かった。親担当も結論文の前に原寸を見て同じ判定。[自前比較図](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/comparison-local.png) · [公開比較図](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/comparison-published.png)

## 根拠

- [一次・実行] atlas固定 `ac5ffd7098120368216948c4e06c494bf8e67178` とsurvey固定 `1f12c1ceb14c1f24acc48249eaad60bcdf541721` の同じ面を使い、製品の全canvasと画素中心式を照合してXYWH [1320,980,512,512] をそのまま維持した。公式masked CT `20250521140437`、8.640 µm L0、出力9.6 µm、scale .9、深さstep 1.111 voxel、linear・非反転法線で33層を1回描画。新中央層16とatlasの中央層32は260,873/262,144画素完全一致、全画素±1 DN以内、MAE .004848 DN。製品TIFF/Zarr全8,650,752値一致。親担当も元mesh位置9点、5深さ×9点の生CT補間および中央全画素を独立照合した。[固定条件](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/roi.json) · [中央全画素照合](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/ct-mid-comparison.json) · [親独立照合](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/lead-numeric-check.json)
- [一次・実行] 既存seed42 step075000とdense-native step16000で中央17層8→24、24→8、各49パッチを1回ずつ実行。公開単独の同方向PNGとの同じ座標の表示値相関はseed42 .384、dense-native .879。Ink Lensの公開仕様にある重み・dense config SHAは保存済み重みと一致した。法線にはsurvey参照との差があり、全面atlasに対する窓の位相とモデル実行・集約実装も異なる。中央CT一致から全深さの入力一致やseed42差の原因は確定しない。公表学習一覧にはPHerc0343の記載がなく、atlas metaは両モデルをunknownとする。起点モデルを含む座標レベルの非重複は未検証。この既知対照から未知の読取性能は推定していない。[計測](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/comparison.json) · [公開仕様と幾何の照合](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/preflight.md)

## 実行条件と費用

CT55キー110 MiB、HEAD 32.968秒、GET 157.205秒。mesh3TIFF 534,879 B、公開単独2 PNG 6,160,131 B、メタ・コード9レスポンス415,973 B（途中まで取得した木を含む）。製品1回3.064秒、推論4回16.116–17.863秒、各120秒上限、CPU1、ASまたはJob commit 4 GiB、通信分離。C作業約155 MiB、追加クラウド0円、ローカル電力費未計上。初回公開PNGログはJSON import漏れで中断したが保存本文を再利用し、supportのimportは既存検索パスで解消。元CT再取得・描画再実行・推論再実行は0回。[実験記録と再現](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/record.json)

## メモ

- 2026-11-14 JST。公開meshの固定3 TIFFとmetaをGit blobに照合。固定領域全262,144画素が有効。公開surveyの座標式をscale .9にした参照とのXYZ差最大 .002072 voxel、法線dotは全画素正で局所差あり。固定55キーを全取得し、描画1回・推論4回・原寸比較と親独立照合まで完了。[取得前照合](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/preflight.md)
