Status: resolved
担当: 研究（R197担当、2026-11-14 JST）
Blocked by: 196

# Hecateの公開像とローカルCPU像の差を、生成来歴と入力契約から切り分ける（2026-11-14）

## 依頼

研究196で固定Hecate既知対照をCPU1/fp32で単回81/81完走した。約418秒、追加費用0円。190のCPU3枚全12,288確率値はbit一致、親も全81入力・保存確率331,776値・Hann再集約→最終PNG102,400画素の全一致を確認した。一方、同座標の公開Hecate像との差はMAE36.238922 DN/相関0.688255556で、主担当と担当の原寸目視でも上明部が縦に伸びて下明部とつながり、公開例の暗い分離が弱まる。計算実装は成立したが、既知字画の形状維持は未確認のため、未知面へ同じモデルを増やす前に差の来歴を調べる。

この一件では、比較している二つのHecate像が同じ重み・コード・入力定義・集約・表示条件を持つと確認できるか、差を説明しうる具体的な不一致を特定できるかを問う。公開像と一致するまで設定を走査しない。まず保存済み原文と入力を使い、必要な一次のコード/配布メタだけを補う。対象はHecate一モデル・同じ既知PHerc0343で、他モデル/未知領域/新しい候補選びは混ぜない。

ローカル固定値: Hecate HF revision9cb86e500e944b11a06a7020403cde5dffb5bcb2、source SHA c232c18a1a86cfb91257a00db13288202bb8ae33732ba26f7291a9b8adb8da59、weight SHA809f4f10f7cb7afa19b4bee0f7d2ab31edd7e11b664f9f210cc9c17f22fcfe5d。研究190保存33×320²、global XYWH1376,1056,320,320、主比較1408,1088,256,256、reverse24→9（16層）、64²/stride32、fp32/batch1、CPU Torch2.14.0+cpu。研究189/190/196、196のcomparison-256.png・lead-verified.json・lead-visual.json・実行/入力原票を参照。

公開参照: SharpMeow/first-letters-ink-atlas ac5ffd7098120368216948c4e06c494bf8e67178、surfaces/PHerc0343/kbh-POS_PHerc0343_erwin/maps/hecate-9.6/c+0_s1_reverse.png、196のR190参照原票にある通り。PNG SHA67795f34e27c0b7b974e8d84780df8ecdf14cff5dd7893bc3891f7dc7d678427、全体6048×2304。R168/173/175/189の保存atlas資料を先に読む。R175は既存二モデルのパッチ開始位置を全面へ揃えて公開再現が改善したが、Hecateの入力/歴史的adapter/weightの同一性をそれだけで証明していない。

調べる具体点の例は、公開生成時のモデル/adapter版と重みSHA、深さの中心と反転を適用する順序（16枚の偶数窓と33/65層の奇数入力）、モデル実入力の正規化・マスク、パッチ位置と余白、名目/実際のサンプル間隔、公開予測のprecision・丸め/再正規化。これは仮説の例で、どれかを原因と前提にしない。確定事実/推論/未確認を分け、時点不明の最新コードを公開時点のコードと同一視しない。公開のパラメータ名やファイル名だけで実際の生配列を知ったことにしない。

ソースから明確な不一致が見つかった場合は、モデルを再実行せず、保存された配列の選択範囲/数値/位置を小さな独立計算で再現して差を示せるか確認する。仮の設定で似た画像を作る調整は行わない。重みの歴史や生成コードを一意に戻せなければ、その制限と比較に使える/使えない範囲を結論にする。次の最小一実験を提案する場合は、原因を識別する一つの変更と必要資源・停止条件を具体化する。追加forwardは次の票で主担当が決める。

新規取得は小さい一次テキスト/メタ/コードのみ、本文合計8MiB/通信180秒まで。新CT・メッシュ・画像・重みのダウンロード、モデルforward/GPU/学習/依存追加、有料計算、公開/応募/連絡は0。既存大配列を確認する場合はWindows CPU1/commit4GiB、元の登録原票は変更しない。194有料GPU案は196の完走を受け今回は実施せず、本人には回答不要と伝えた。新たな支出権限はない。

研究票に結論と一次根拠を追記し、experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/へ来歴比較・取得原票・必要なら非forwardの独立再現コードと結果・次の一実験案を保存する。manifest/lab登録候補まで。主担当が根拠と次の採否を別確認する。同時の別研究・サブ委任なし。

担当は今回 gpt-6.1-sol / xhigh。モデルの歴史的生成条件に不確実性があり、比較可能性と因果の手がかりをコード/入力から調べるため。既存の数値検証を再実行する仕事ではない。

## メモ

- 168/173/175/189/190/196の原票と、10月27日付Ink Lensおよび固定ink-sdkの一次コードを照合中。
- 当時公開されていた経路の層選択差を確認し、既存配列で差を独立計測。主担当もソースと保存入力から別検算した。

## 結論

[一次・実測] 公開当日のInk Lensは中央16層を切り出してから逆順にする。公開65層では39→24、保存33層では23→8に相当し、R196の24→9から1層ずれる。固定ink-sdkのvendorコードはR196の公式ソースと全バイト一致し、公開runnerの重みpinも同じ。公開PNGそのものの実行記録は得られず、歴史的実行条件と画像差の因果は未確定。[来歴の比較](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/README.md)

## 根拠・詳細

- [一次] HFの初回公開は2026-10-27 14:28 UTC。公開前04:43、08:22と同日公開後23:53のInk Lensコードで同じ層選択順を確認。固定版ac5ffd7の時刻は23:57でカード・例文変更。面メタは中心窓・CT・レンダー記録を含むが、生成時のコードcommit、実引数、環境と入力tensorは紐づいていない。[公開履歴](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/originals/hf-atlas-commits.json) · [公開前コード](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/originals/pre-upload-runners.py) · [主担当ソース照合](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/lead-source-checked.json)
- [実測] 190の保存配列で1,587,621/1,638,400値が変化、平均絶対差14.494643 DN、全81パッチに差。raw-any支持列は全パッチで一致。中央CTの同じ320²は最大1 DN、平均絶対差.004668 DN、64²/32の主ROI支持81開始位置も一致。公開側の非中央層、実行時AMP・device・版、実エクスポートは未検証。[担当配列照合](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/saved-input-check.json) · [主担当配列照合](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/lead-depth-checked.json)
- [推論・次の一回] 保存33層の `[8:24]` を固定して23→8だけをCPU1で一回比較する。196の保存出力を対照に、同じ主256²で公開PNGとのMAE/相関と既知字画部分の分離を見る。入力SHA・有限性・3パッチ後の時間見積をゲートにする。別の深さ・向き・モデルへの展開はこの試験に含めない。[次の研究票](198-hecate-crop-before-reverse-control.md)

## 取得の経路

保存済みR168/173/175/189/190/196を再利用し、固定GitHubコードとHFメタだけを取得した。保存配列の検算5.307秒、CPU1/commit4GiB。新規CT・画像・重み・モデルforward・GPU・課金・公開は0。[取得明細](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/acquisition.json) · [ファイルmanifest](../experiments/vesuvius/discovery/20261114-hecate-atlas-provenance01/manifest.json)
