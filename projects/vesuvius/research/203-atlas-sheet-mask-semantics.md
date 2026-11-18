Status: resolved
担当: 研究（R203担当、2026-11-14 JST）
Blocked by: 202

# atlasの紙面割合は何を測り、次の入力選定に使えるか（2026-11-14）

## 依頼

研究202で、PHerc0175Bの `face_check.sheet_fraction=1.0` を他候補の0.069/0.172より広い紙面支持と誤読して一面を選んだ。親確認で同じmetaの `mask` は `ct > 0 (sheet mask under 5 %)`、他二面は `sheet (crossness >= 0.31)` と分かった。事前選定原票は保持し、誤読は202で訂正済み。画像の陰性判定を巻物全体には広げない。

この指標の正確な計算・分母・fallback分岐を一次ソースで確かめ、現在の入力選定を修正する。名前だけで別種の割合を比較したことが原因なのか、値が示すのがCT支持・繊維交差・物理紙面のどれかを分ける。公開作者の意図と、こちらの使い方の誤りも分ける。研究195やそれ以前の候補選択で同じfallback比較があったかは、保存記録から関係のある範囲を確認する。過去に登録した根拠ファイルは変更せず、訂正はこの研究と生きた月次一覧に追記する。

必要な実測は既存CT中央PNGと小メタ・既存ソースを優先する。202の三候補の内、0175Bの15画像だけ取得済み。紙面割合を比べるために0268/0483AのCT中央画像を追加取得する必要がある場合は、その二枚だけ取得してよい。品質指標を新しい文字検出器や物理紙面の正解へ読み替えない。既知PHerc0343と保存された未読面で区別の限界が分かるなら、必要最小限で対照を取る。大規模閾値探索、全atlas画像取得、幾何修正、インク推論は範囲外。

最後に、無料で進める次の一件として、未精査の面を選ぶ根拠が残るか、または入力の紙面追跡を先に調べるべきかを具体的な根拠付きで判断する。指標を直すだけで文字が読めるとは扱わない。コードの短い比較や確認を超える汎用基盤は作らない。

入口の例は固定atlas `SharpMeow/first-letters-ink-atlas` revision `ac5ffd7098120368216948c4e06c494bf8e67178` のREADME/meta、リンク先のInk Lens/Scrolls、villa PR2318、survey `1f12c1ce`。保存資料は `experiments/vesuvius/discovery/20261113-next-target01/ink-atlas.md` と研究195/202。調査は一次のコードと実メタを照合し、歴史的に使われた実行版が不明なら明記する。

新規受信は64MiB、通信300秒以内。CT中央PNG最大二枚以外は小メタ・ソース。新CTボクセル・XYZ・モデル・重み・GPU・ビルド・有料資源・外部公開・送信なし。CPUは既存 `tools/research/run_windows.py` でCPU1/commit4GiB。Cへ保存、D読取のみ。保存先 `experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/`。結果をこの票に追記し、コード・原文・実測・次の判断・manifest/record候補を残す。親が独立に式と分岐を確認してから登録する。他の研究を並列で始めない。

担当は今回あらためて **gpt-6.1-sol / xhigh** を選ぶ。実装の分岐とデータ生成来歴を追い、誤った選定の影響範囲を診断して次の研究判断へつなぐため。

## 結論

[一次・実測] PHerc0175Bの `sheet_fraction=1.0` は、交差マスクが全画素の2.289%（93,040画素）に留まり、正値CT 3,640,421画素を採用した面の値。公開中央PNG 8枚でvilla PR #2318の式と5%フォールバックを再計算し、採用画素数 `pixels_used` は公表値と全件一致した。PHerc1218二面では公開 `sheet_fraction` の分母としてCT正値数を支持し、全画素数・幾何 `rendered_px` を排除できた。PHerc0846Bは正値数で割った通常の3桁丸めが公表値と.001ずれ、atlasの厳密な分母・丸め・生成実行版は未確定。 [実測原票](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/measurements.json) · [原文と式](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/README.md)

保存メタ10面の範囲でフォールバックは0175Bのみ。R195の3面はいずれも通常の交差マスクで、R202と同じ異種マスク比較は確認されなかった。交差マスクは中央CTの繊維方向の局所特徴を測る。CT正値、幾何支持、単一の物理紙面は別の情報。 [保存メタ独立一覧](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/lead-saved-meta.json)

## 次の無料課題

未精査のPHerc0483A `3155_3610_11128` は交差マスクが全域15.439%で、最大の内部512² `[704,1024,512,512]` では70.17%が通る。この512²の中央CTに粒状模様、曲がる層状線と弧状境界があり、同じ層を追えるか未確認。追加予測を選ぶ前に、この一面・一窓のmesh/renderer来歴とatlas→元CT座標を照合し、座標が確定する場合だけ、上側・弧状境界・下側の固定少数点の直交断面で紙面を追う。未確定ならそこで終了。 [原寸CTとマスク](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/0483a-texture-detail.png) · [固定窓](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/0483a-texture-detail.json)

## 取得の経路と資源

PRの固定head、survey固定版、atlasの保存メタを利用。R202の固定treeで長さとLFS SHAを照合した中央PNG二枚（0268/0483A）だけ追加。新規保存4,696,058 B、計測済み後半4件のcurl 5.477秒、先行の個別通信秒は未計測。Windows CPU1/commit4GiBで測定12.660秒と局所図1.164秒。新CTボクセル・XYZ・推論・GPU・有料資源・公開0。 [取得原票](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/acquisition.json) · [測定実行](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/measure-process.json) · [局所図実行](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/texture-process.json)

## メモ

固定atlas生成wrapperは既存公開関連木とコード検索で特定できなかった。主担当も別実装で8面の交差マスクと採用画素数を再現し、診断窓のCT表示262,144値と原画の一致を確認した。 [独立計算](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/lead-formula-check.json) · [表示の独立確認](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/lead-view-check.json) · [月次一覧](../deliverables/vesuvius/2026-11-bundle/README.md) · [登録候補](../experiments/vesuvius/discovery/20261114-atlas-mask-semantics01/record.json)
