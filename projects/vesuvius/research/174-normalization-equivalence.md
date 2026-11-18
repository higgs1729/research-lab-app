Status: resolved
担当: 研究（R174、2026-11-14）
Blocked by: 173

# 保存した同じCTパッチで公式NumPy前処理と公開Torch前処理を比べる

## 依頼

2026-11-14 JST。173のPHerc0343固定領域はCT中央が公開atlasと±1DN内、dense-native逆順に既知の輪の部分形状が現れたが、seed42の公開出力との対応は弱い。173で列挙した候補原因は法線・パッチ位相・NumPy対Torchの前処理・実行環境で、まだ原因を特定していない。ここでは同じ保存パッチを与えたときの正規化の差だけを切り分ける。実験条件の探索ではない。

研究133/171/173が使用した固定公式47a9c37の実際の正規化関数と、173保存のInk Lens固定0139cf33bb443db42602bf1b201dd05f8a666413のrunners.pyが呼ぶengine.robust_torchを一次コードで照合する。既存の保存コードが先、足りない本文のみ固定版で取得する。GitHub連携のfetch_file/fetch_blobが使えるので優先。本文の完全な保存ができない等の不足があれば説明して固定rawへ続行してよい。新規文書/コードは計6件512KiB、本文にSHAを付す。新モデル・依存・ビルドを導入しない。

問いは、同じ入力、同じバッチ内の並べ方で、軸・百分位・中央値/MAD・クリップ・ゼロ/マスク・定数入力の扱いが同じか。173の中央17層、128patch/stride64の49パッチを両順で固定し、保存した元CTを読むだけで比較する。実際に呼ぶ形状/float型/バッチ軸を合わせ、現在のCPU Torchで計算する。CUDAと異なる点や公表された実生成版と未固定な点は限界に残す。公表関数のソースをそのまま実行し、独自に書き直して同じ実装と呼ばない。重いモジュールを丸ごとロードできない場合の関数取り出しは、固定AST/原文から行ったことを保存する。

全パッチで数値差と非有限の有無、差が出る条件を集計。必要な代表の入出力だけ保存し、巨大な全中間テンソル群は不要。通常のfloat32差なのか、関数契約の実質的な相違なのかを判断できる原票にする。バッチ数だけで変わる実装なら同一パッチを単独/複数で処理してその事実を確認できる。過去のモデル出力の差の原因と断定するには別の根拠が必要だと区別する。

この研究では描画・モデルforward・新CT取得は0回。前処理が同等なら原因候補を一つ除き、そのまま閉じる。意味のある差を見つけたら、どの入力/どの式で起きるかと、保存元CTを使う最小の次の比較を返す。新しい網羅試験や汎用フレームワークは作らない。既存のCPU1/commit4GiB/threads1/通信拒否ランナーを借り、一回の分析上限120秒、作業32MiB、追加クラウド支出0円。登録済み173は読み取りのみ、新出力はC上の experiments/vesuvius/discovery/20261114-normalization-equivalence01/。

研究票へ結論・根拠・限界を追記し、lab候補を用意。親は重要な式/代表数値を確認する。外部投稿/公開・サブ委任なし。今回は gpt-6.1-sol / high を選択。固定された二つの実装と保存入力を比較する限定された検証であり、既存の計算・保存手順を解釈して使えるため。173完了後に逐次実行。

## 結論

[一次・実行、2026-11-14 JST] 研究173の同一入力を与えたCPU比較で、公式NumPyと固定Ink LensのTorch正規化にはfloat32丸め幅の差だけが出た。前後各49パッチ・13,647,872値の最大絶対差は各2.38419×10⁻⁷、平均絶対差は各1.11614×10⁻⁸、非有限値は0。差は両順で同じ9パッチに限られ、`1.4826×MAD` の積をfloat32へ丸める順で説明できた。この条件では前処理を実質的な差の候補から外せる。公開seed42との差の原因、実際の公開PNG生成版とCUDAでの値は未確定。[全パッチ結果](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/result.json) · [丸めの照合](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/rounding-check.json)

## 根拠・詳細

### ソースと呼び出し

- [一次] 公式は研究133/134の固定villa `47a9c37f6f8e99afdab47bb46ad425aa726f5dc0` の `normalize_robust`。固定CLIはZYX float32の一パッチごとにマスク引数なしで呼ぶ。Ink Lensの保存 `runners.py` は非ゼロのパッチを残して `(B,D×H×W)` にflattenし、float32で `engine.robust_torch` を呼んでから `(B,1,D,H,W)` に戻す。Ink Lens参照固定版は `0139cf33bb443db42602bf1b201dd05f8a666413`、そのengine内のvilla pinは `8aa507c1215f1fa8758f13d0538f7af9710e02d7`。正規化について比較したのは実際の呼出先であり、モデルロードやatlas生成パイプラインは起動していない。[公式CLIの先行照合](134-r012-known-ink-verification.md) · [Ink Lensの保存runners](../experiments/vesuvius/discovery/20261114-pherc0343-ct-readable01/ink-lens-runners.py)
- [一次] 欠けていた `engine.py` 一件24,944 BをGitHub連携の固定版取得で補った。base64から元バイトを保存し、Git blob `c21f141e25857039db3ae1a019afafec0cf4d7b4` と本文SHA-256 `280309c7bf86bd2d8c55bb64feb52168cbde230d02912fec72d1288260ccffa7` を確認。両方式の関数と直接ヘルパーのみを固定原文のASTから取り出して実行し、行範囲・関数部分SHAを保存した。Ink Lens自身の `robust_np` も同じ入力で公式NumPyと全ビット一致した。[固定engine本文](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/ink-lens-engine.py) · [検証コード](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/compare.py)
- [一次] 両関数はパッチ内の全17×128×128値から線形1・99百分位を求め、クリップ後の中央値を引き、`1.4826×MAD` で割る。偶数長の中央値は中央二値の平均。MADスケールが非有限または1e-6未満ならクリップ前の母標準偏差、半百分位幅、1.0の順でフォールバックし、結果の非有限を0へ置き換える。混在する0は有効な入力値として含む。公式のマスク引数は今回の呼出しでは使われず、Torch版には同じ引数がない。全部0のパッチはInk Lensで正規化前に除外され、公式は空パッチを出力集約の対象から外す。今回の保存パッチに値0はなかった。定数、混在0、MAD=0、分数百分位を使った小対照も保存した。[関数契約の対照](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/result.json)

### 保存パッチの実測

| 固定条件 | forward 8→24 | reverse 24→8 |
|---|---:|---:|
| 128²・stride64のパッチ数 | 49 | 49 |
| 比較したfloat32値 | 13,647,872 | 13,647,872 |
| ビット差のある値 | 2,220,299 | 2,220,299 |
| 非有限値 | 0 | 0 |
| 最大絶対差 | 2.38419×10⁻⁷ | 2.38419×10⁻⁷ |
| 平均絶対差 | 1.11614×10⁻⁸ | 1.11614×10⁻⁸ |

[一次] R173の16 Zarrチャンクを入力契約SHAへ照合して33層を組み、中央17層から固定49パッチを選んだ。Torchは既定batch上限64で一回に収まる49行のfloat32テンソルを使った。両順それぞれの代表3パッチを単独で処理しても、49行バッチでの値とビット一致した。reverseの出力を深さだけ戻すと、両実装とも全値がforwardとビット一致した。[全パッチ結果](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/result.json)

[一次] MAD 24・31・34の同じ9パッチで、NumPyのPython floatによる積を除算時にfloat32へ変換した値と、Torchがfloat32で積を作った値が1 ulp異なった。代表パッチのatlas左上XY `(1384,1108)` は上下限30/153、中央値101、MAD 24。除数はNumPy 35.5824012756、Torch 35.5823974609。forwardの生値31では正規化値が−1.9672646523と−1.9672648907になった。丸め順だけを変えた除算から代表の各278,528値を両方式・両順ともビット単位で再現した。[丸めの照合](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/rounding-check.json)

## 実行条件・限界

Windowsの既存1CPU・Job commit 4 GiB・数値スレッド1ランナー、既存Torch 2.14.0+cpu、NumPy 2.5.2。R133のsocket監査関数を固定ASTから借りて計算中の外部通信を拒否。比較8.319秒、最大RSS 1,156,661,248 B、保存物約5.2 MB。モデルforward・CT取得・描画・導入・ビルド・追加費用は0。本文保存の初回はWindowsのコマンド長上限を超えたため、取得済みbase64を分割して同じblobを保存した。新規取得はengine一件のみ。

今回の比較は保存された同じ入力の正規化に限る。法線差、パッチ位置、モデル実行と集約、公開PNGの正確な生成版やCUDAは別条件であり、下流スコアへの丸め差の伝播は未測定。この丸め差について新しいモデル比較を追加する根拠は得られなかった。[計測原票](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/compare-process.json) · [再利用手順](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/lab-record.json)

## 主担当の別照合

[一次] 主担当は固定原文の両関数と呼出しを別に読み、マスクなしの同じ処理契約を確認した。代表両順の元配列から百分位30/153、中央値101、MAD 24を再計算し、丸め順による除数35.5824012756と35.5823974609でそれぞれ保存全278,528値をビット再現した。[別照合コード](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/lead_check.py) · [別照合原票](../experiments/vesuvius/discovery/20261114-normalization-equivalence01/lead-check.json)
