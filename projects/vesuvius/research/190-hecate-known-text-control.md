Status: resolved
担当: 研究（R190担当、2026-11-14 JST）
Blocked by: 189

# Hecate 9.6µmで保存済み既知字画を一度再現できるか（2026-11-14）

## 依頼

189の比較と親の独立契約確認からHecate 9.6を選んだ。既存seed42/denseと異なるResNet152 3Dと学習した深さ集約を持ち、既知PHerc0343の保存CTを利用できる。今回は未知面へ進まず、一つの既知対照で入力/出力・資源・字画部分の対応を確認する。新しいモデルだから良くなるとは仮定しない。

固定HF scrollprize/hecate 9cb86e500e944b11a06a7020403cde5dffb5bcb2、189保存hecate.py SHA c232c18a1a86cfb91257a00db13288202bb8ae33732ba26f7291a9b8adb8da59。重み hecate_9.6um.pth 522,576,086 B、SHA809f4f10f7cb7afa19b4bee0f7d2ab31edd7e11b664f9f210cc9c17f22fcfe5d。重み取得上限512MiB、189で特定する同じ固定atlas面の公開Hecate reverse一枚を参照（2,114,372 B、上限3MiB）。この二本文以外の新CT/重み/画像を取得しない。全通信180秒。長さ/固定hash、取得時間と実受信量を残す。

入力は175保存33×384×384 uint8の、local XYWH [32,32,320,320] を全33層そのまま切り出す。global XYWH [1376,1056,320,320]、主比較 [1408,1088,256,256]。親はatlas全体からこの主比較へ寄与する64²/stride32の全81パッチと、切出しの全81パッチが順序を含め一致することを確認した。XY間隔9.600000254µm、Z9.599039497µmは名目9.6からZ約.010%差があり、同じ保存入力の限定比較として許容するが厳密等方再描画とは呼ばない。新補間/深さずらし/方向追加を行わない。

作者コードのCPU fp32、batch1、uint8/255・clipなし、16×64×64、stride32、nonperiodic Hann floor.001、2D reverseだけを実行する。33層でreverseは[9,25)を反転＝24→9（既存seed42/denseの17層24→8と区別）。公式weights_only/mmap/strict loadを保ち、code/weight/入力SHAと実バージョンを記録。モデルの実装は修正せず、小さいラッパーで入出力・計時・原票を扱う。既存CPU Torch/NumPy/隔離Zarr等を再利用し、新しい依存やbuildを入れない。187の新Windows入口で資産解決を先に確認する。

一つの推論処理でモデルを一回ロードし、最初の三パッチも本番の81に含めて計時・保存する。三パッチ後の実測から残りが総上限900秒を超える見込みなら途中で停止し、途中結果と資源を記録して返す。成功済み/途中パッチを試験用として再推論しない。CPU1、process commit4GiB、数値ライブラリ1thread、作業768MiB、C空き10GiBを条件にし、物理空きメモリも開始前に確認。C新規、D読取のみ。GPU・有料計算は使わない。上限超過/メモリ不足/不正な重みや入力なら条件を変えず終了する。

親がモデルを再実行せず検算できるよう、各パッチの位置・入力のhash・時間と、予測確率または集約前の値を残す。作者の集約・丸めを変更しない。最終の原寸画像と公開Hecate参照、175の二モデルを同じglobal主比較・固定0–255で並べる。公開予測との一致は再現性で認識精度ではない。当時の公開版/処理条件が確定しなければ差の原因を断定しない。既知箱9/10の部分にある弧・囲まれた暗部の形、融合・散乱、位置対応を担当と親が別目視する。新文字の転写・物理紙面の正解・未知への汎化は主張しない。

保存先 experiments/vesuvius/discovery/20261114-hecate-known-text-control01/。研究票に結果、原票/条件/費用、比較図、再利用入口、manifest/lab候補を簡潔に残す。重要な出力を親が別確認後に確定。lab登録は親、サブ委任なし。追加クラウド費0。

今回はgpt-6.1-sol / xhigh。新しいモデルの初回実行を、保存CT・資源制限・標準入力契約・再実行不要の検証へ接続するため。189登録後の逐次実行。

## 結論

2026-11-14 JST。Hecate 9.6 µmのstrict loadと3/81パッチのforwardは成立した。最初の3パッチで後二つの境界間隔が44.831秒、46.232秒となり、残り78は3,606.064秒と見積もった。残枠715.990秒を超えたため4番のforward前に停止した。CPU1の900秒枠では固定試験の完走を見込めず、既知字画と公開参照の全体再現性は未判定。[計時](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/first-three.json) · [実行結果](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/execution-result.json)

固定入力の320²全33層のSHAは親の独立切り出しと一致。reverse 24→9、CPU fp32、64²/stride32を保持。親は捕捉3件の位置、raw/正規化入力SHA、有限なfloat32確率3×4,096値、停止条件を再forwardせず別に確認した。Windowsの残存memmapは分子3件・分母4件の途中状態で、全体PNGは未生成。[実験報告](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/README.md) · [主担当検算](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/lead-verified.json)

strict load 16.920秒、実行入口184.106秒、外部監視186.832秒、最大RSS 1,283,719,168 B。固定重みと参照一枚の取得は計524,690,458 B、32.496秒。新CT・依存導入・ビルド・GPU・追加クラウド費0。モデル本番は一回。[取得原票](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/acquisition.json) · [資源](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/infer-process.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-hecate-known-text-control01/record.json)

## メモ

- 初回準備は共有CRC32Cパス不足で停止。R133の順に揃えて準備を再実行した。本番は見積条件で一回を停止し、未完出力の救済処理は行っていない。
