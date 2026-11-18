Status: resolved
担当: 研究（R010 Sol/medium）

# R010: 実際の巻物処理で残っている障害から、次の小さい再現へ進める一件はあるか

## 依頼

2026-11-13（日本時間）。月次候補はR005の成分分離、R007のcrop指定、R009のZarr出力改善の三件。三件の公開候補を完成し、先行公開の時期を本人へ確認中だが研究はrunningのまま継続する。少ない支出で最初の受賞を目指す方針に沿い、次は人が実際の巻物データの処理で遭遇している未解決の問題に限って、一件の再現試験へ進めるか判断する。理論上の不具合や件数の積み増しを目的とする新規コード探索は求めない。

現在の使用経路・具体的な利用者報告・公開の再現材料・未解決性を確かめ、必要性と小さいローカル再現の両方を支持する候補を最大一件返す。情報を集める入口は任せる。既存の課題・提案・修正で既に同じ問題を扱っているものは新規成果として勧めない。研究107・118・119の見送り一覧を引き、同じものを調べ直さない。とくに既存downloader、memory/cache、label drift、TIFF再開、Open Data保存、奇数寸法pyramid、fiber/flowsnap取込、深度scale、R005/R007/R009の微調整や再包装を外す。

候補には、誰のどの作業がどう止まる/誤るか、現行版と既存解、最小の発火条件と比較対象、借りられる入力・ツール、無料ローカルCPUで判定可能な範囲、計算/入力の見積りと停止条件を添える。人の利用を確認できる根拠がない、未解決性がない、再現が大きい、または既存解への貢献で十分なら、その理由を返す。候補ゼロは有効な結論で、無理に別のコード仮説を作らない。上流CONTRIBUTINGの人による利用・コメント・レビューの要件は、我々が満たした事実へ読み替えない。

この依頼は次の投入先選定に必要な調べだけ。実験・ビルド・依存導入・CT/画像/大規模データ取得・GPU・有料計算・外部公開/投稿を行わない。D:は読取のみ。新しい一次根拠は `experiments/vesuvius/r010/20261113-workflow-candidate01` に随時保存し、調べ方と未確認点をこの依頼に追記してresolvedへ。原文は保存するが、長い本文や周辺の全ファイルをツール出力に列挙しない。lab候補を返す。追加subagentは禁止。

モデル/effortはgpt-6.1-sol / mediumを今回選ぶ。既存の一次資料調査手順で候補の必要性と重複を絞る範囲であり、未確立のアルゴリズムや実装設計には踏み込まないため。難しい判断は確定せず根拠と未確認点を主担当へ返す。

## 結論

次の小さい再現試験へ進める候補は0件。PHerc0139のOffsetと巻き追跡には具体的な利用報告があるが、報告者の比較や既存PRが同じ対処を扱っていた。配布データ・チェックポイントの問題は現在も確認できたものの、公開資料だけで正しい配布物を作り直せる根拠が得られなかった。

## 根拠・詳細

2026-11-13 JST取得。照合した villa `main` は `0080fa393724575d4f19059d91402757f9351b28`。研究107・118・119の除外を適用した。 [main](https://github.com/ScrollPrize/villa/commit/0080fa393724575d4f19059d91402757f9351b28) · [研究107](107-r006-candidate-sources.md) · [研究118](118-r008-candidate-sources.md) · [研究119](119-r009-data-path-scout.md)

- ［一次］ChaseHendrickのPHerc0139での隣巻きOffset（#2391）は、30回のCPU fitで配布 `offset.json`、報告者が修正した `offset_snap.json`、重みを変更した `offset.json`、初期面を比較済み。隣の手動トレースがある29 fitの平均で目的の巻きに達した点は、配布設定12.5%、修正したsnap 69.3%、重み変更65.5%。現mainの `offset.json` には同じ重みが残り、`offset_snap.json` にも欠落したカンマとsnap段の `pred_dt` 上書き不足が残る。後者は報告者と合意したopen PR #2418が扱う。前者の重みを変えるかはPR本文でもメンテナ判断とされ、報告者の実データ比較を再度行うだけでは新規成果にならない。公開した再現はPHerc0139の予測場・複数の登録済み手動面を要し、小窓だけで設定選択の妥当性を広げられる根拠は得られなかった。 [利用報告 #2391](https://github.com/ScrollPrize/villa/issues/2391) · [配布設定](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/lasagna/configs/offset.json) · [snap修正 #2418](https://github.com/ScrollPrize/villa/pull/2418)
- ［一次］#2080ではPHerc0139の自動トレースで `normal_grid_path` が省略され、正常終了した面が予測に沿わず、報告者が全ゼロ入力との比較で確認した。警告を出す既存案 #2081 はclosed・unmergedなので解消済みとは扱わない。報告者の警告案をそのまま繰り返す増分はなく、今回の候補から外した。同じく実巻物で報告された巻き矛盾 #1855 は接続点の移送と修復ソルバの両方にmerged PRがあり、umbilicus中心 #2029 と線形補間の法線 #2246 には同じ現象を対象にするopen PRがある。 [トレース #2080](https://github.com/ScrollPrize/villa/issues/2080) · [警告案 #2081](https://github.com/ScrollPrize/villa/pull/2081) · [矛盾 #1864](https://github.com/ScrollPrize/villa/pull/1864) · [ソルバ #2023](https://github.com/ScrollPrize/villa/pull/2023) · [中心 #2030](https://github.com/ScrollPrize/villa/pull/2030) · [法線 #2449](https://github.com/ScrollPrize/villa/pull/2449)
- ［一次］#1231はPHercParis4のTutorial 5実行で検証パッチが0件になった報告。配布マスクをどうするかは報告の公開コメントでも未決で、データセットごと保持して検証する機能は #2126 が既にmerged。#2444では公開sheet tracerをPHerc1667の学習外部分で評価するために、学習時の保持範囲を必要としている。現行Hugging Faceのツリーは報告どおり `.gitattributes` と `last.pt` のみで、公開された当時の分割を特定できない。現在のカタログから推定しても過去の分割を証明できないため、どちらも新規の再現試験へ進めない。#2299は利用者が報告したW&B Forge接続の環境変数による回避があり、同じ手順の追記はopen PR #2298が扱う。 [Tutorial #1231](https://github.com/ScrollPrize/villa/issues/1231) · [データセット単位の検証 #2126](https://github.com/ScrollPrize/villa/pull/2126) · [sheet tracer #2444](https://github.com/ScrollPrize/villa/issues/2444) · [配布ツリー](https://huggingface.co/scrollprize/sheet_tracer_7pt_gap60/tree/main) · [W&B #2299](https://github.com/ScrollPrize/villa/issues/2299) · [既存PR #2298](https://github.com/ScrollPrize/villa/pull/2298)
- ［一次・公開メタデータ］#1965のPHerc0343P 8.64 µmは、L0の `.zarray` が非圧縮・`|u1`・`128³`（2,097,152 B）を宣言する一方、HEADの `0/0/3/2` は134,217,728 B、対照 `0/0/0/11` は2,097,152 B。報告のメタデータ不整合は現在も存在する。公式リーダーの挙動は未確認で、報告者の独自strict readerの拒否のみ報告されている。余分なバイトを捨てる、別形状と解釈する等では正しいボクセル座標を保証できず、配布元の元データを使った再生成が必要。HEADとメタデータだけを取得した。 [報告 #1965](https://github.com/ScrollPrize/villa/issues/1965) · [保存した取得原票](../experiments/vesuvius/r010/20261113-workflow-candidate01/)

## 取得の経路と未確認点

GitHub連携でopen Issue一覧、番号・症状によるPR検索、PR状態と固定版の関連ソースを確認した。補助の公開Web検索では公式の利用経路とコミュニティの報告へのリンクを確認した。Discord内の報告は未調査。原文と取得資料は [根拠ディレクトリ](../experiments/vesuvius/r010/20261113-workflow-candidate01/) に保存した。公式CONTRIBUTINGの人による実データ利用・PR要件は、公開報告を読んだことで満たしたとは扱わない。実験、ビルド、CT・重みのダウンロード、投稿は行っていない。 [公式CONTRIBUTING](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/CONTRIBUTING.md)

## メモ

2026-11-13 着手時の監査inboxは空。Issue本文と対応PRを早い段階で保存し、Offset設定・PR状態とPHerc0343Pメタデータを追加照合したところで探索を終了した。
