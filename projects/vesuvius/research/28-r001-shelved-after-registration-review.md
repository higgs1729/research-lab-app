# R001: 既存読取機構を確認し、追加投入を保留

2026-11-11 19:14 JST。heartbeat時間枠996884。主担当の判断。R001の追加実験・実装を保留する。研究活動全体はrunningを維持し、次の候補を一件ずつ扱う。本人の判断待ちではない。

## 判断と残った成果

gen19 Hecateの既知の位置ずれは、同一セグメントの離れた3領域で再現し、別担当による検証も済んだ。ただし19pxと20pxの優劣は領域・条件で入れ替わる。既存issue #2442の報告を新発見として扱わない。前回決めた追加調査30分の見直し点を待たず、約6分の公開コード・メタデータ確認で、現時点では修正差分が具体化しないと判断した。

現在の `vc_reader` は画像からメッシュへの位置変換を `SurfaceRegistration.pixel_to_uv` で明示する機構を持つ。読取側へ位置補正機能を新設する必要はない。一方、公開Hecateメタデータに生成コマンド・生成コードの版・画素原点は見つからず、参照されている元データの公開一覧取得は403だった。その経路の探索は停止した。生成器が非公開だと断定するものではなく、今回確認できた経路の限界である。

既存の `InkDetectionOverlayController.cpp` は選択画像の表示に関わるが、問題のZarrを消費する実経路だとは確認できない。ここへ19pxを固定値として加える変更は行わない。`render_ink.py` はCTレンダラの呼び出し等を含むが、当該Hecate出力を生成したコードであるという証拠は得られなかった。

## 再利用できる知識

- tifxyzの `meta.scale` はXYの格子倍率。格子間隔20pxと、XYZが参照するCTの解像度は別の変換である。
- `vc_reader` のSurfaceRegistrationは画像座標をfull-resolutionのsurface UVへ写す。配列形状・ファイル名・解像度だけから登録変換を推定してはいけないと既存文書に明記されている。
- 仮に画像の読取位置が `p = 20*g + 19` であるなら、対応する画像→UV変換の平行移動は両軸 **-19** となる。文書の構文では `pixel_to_uv=((1,0,-19),(0,1,-19))`。これは符号と単位の代数的な整理であり、正しい原点の確定や実APIによる当該データの動作確認ではない。今回この値をカタログへ登録していない。
- partial HTTP Range、シャード索引CRC検査、TIFFの部分読取、保存本文の再利用、3D対応と固定マスク比較は、今後の関連実験へ再利用できる。一般ライブラリとして完成したとは扱わない。

## 根拠

コード参照は `c86cbd14bb34e0124684d3d97b03b310c947819a` に固定。

- [aligned-sampling文書](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/docs/aligned-sampling.md)、[保存本文](../experiments/vesuvius/r001/20261111-registration/aligned-sampling.md)
- [surface-sampling文書](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/docs/surface-sampling.md)、[保存本文](../experiments/vesuvius/r001/20261111-registration/surface-sampling.md)
- [paired.py保存本文](../experiments/vesuvius/r001/20261111-registration/paired.py)、[grid.py保存本文](../experiments/vesuvius/r001/20261111-registration/grid.py)
- [Hecateメタデータ](../experiments/vesuvius/r001/20261111-code-origin/hecate-group.json)、[元データ一覧の403応答](../experiments/vesuvius/r001/20261111-registration/source-listing.json)
- [3領域の結果と限界](27-r001-three-rois-and-origin.md)、[独立検証](26-r001-multiroi-verification.md)、[既存issue #2442](https://github.com/ScrollPrize/villa/issues/2442)

成果の新規性を主張する修正・PR・応募は作成していない。再開条件は、生成時の画素原点の一次情報、実際の消費経路で既存登録機構が使えない具体例、または明示された保守者の必要性が得られること。有料計算の新規調達0 USD。今回GPUや追加実データのROI取得は使っていない。LLM利用・ローカル電力は金額換算していない。

## 次の一件

未決監査提案を確認してから、事前調査の候補である永続ディスクキャッシュ容量問題（#2294）へ切り替える。最初は現行コード・PRとの重複確認と、ローカルCPUだけで再現可能かの判断に限る。実装前に現在の容量制御・並行利用の仕組みを確認する。
