Status: resolved
担当: 研究
Blocked by: 147

# R005: 任意成分配置を上流へ提案するための適合と証拠を整理する

## 依頼

2026-11-13。R009/R007の準備146/147に続き、公開済みR005のflatboi任意成分配置だけを現在のScrollPrize/villa向けにローカルで準備する。上流mainは146の14d4e725df8b569e6fc8ceb3c04d130f705c1565へ固定して比較。凍結パッチと対象ソースの一致/差異、適用可否、同等の公開PR有無、実CT証拠との対応を確認する。適合変更が必要な場合は範囲と未確認事項を示し、勝手に大きな修正へ広げない。R007/R009の差分を混ぜない。

成果は短い研究票、適用先と差分、英語PR案、再現手順とlab候補。原票の膨大な複製を作らず、106/284の別成分跨ぎ辺、189/399の異成分拒否、固定小領域の混合1280→分離ROIで0/0という既存検証を正確に参照する。平行移動以外のXYZ・solver変更をしたと表現しない。幅/画素位相は変わり、同じ出力画素比較ではない。第二成分の物理的紙面や判読改善は未確認。144/145の既知ラベル候補では読取対照が得られなかったことを限界として保持し、この準備で新しい文字/賞候補を増やさない。

146/147の固定上流規定を参照し、対象ディレクトリのAGENTSも確認する。人間の利用経験・本人が書いた有用性・本人確認・必要な実画面を代理で満たさない。既存図を使う場合は実データからの比較図として由来を明記し、端末実スクリーンショットと混同しない。本文は短く、詳しい条件と既存図の入口は再現手順へ。本人が研究利用したと装わない。

新規画像/CT取得、描画、インク推論、ビルド、依存導入、課金なし。対象ソースが同じなら再試験は不要。146の保存上流treeは読取再利用可。D:読み取り、C:新規出力。外部fork/push/PR/issue/コメント/連絡/応募/公開repo変更、追加subagent不可。小さい公式GitHubソース/公開PRの読取のみ可。登録済み資料は不変、新規はexperiments/vesuvius/r005/20261113-upstream-preparation01/、適用先.work/r005-upstream-20261113/。

モデルgpt-6.1-sol、effort high。適用自体の手順はあるが、幾何/紙面/描画の複数段の証拠と限界をレビュー向けに解釈する必要があるため。146/147と同様の小さい準備で完了する。

## 結論

［一次・Git］villa main 14d4e725df8b569e6fc8ceb3c04d130f705c1565 の flatboi.cpp は、既存試験base 7ad02f4 の blob 2dcf5981 と同一。ラスタ実装・ヘッダー、flatboi CMake、参照rendererの4ファイルも各blobが一致した。凍結R005差分をC:の .work/r005-upstream-20261113 に適用し、適用・逆適用・空白検査を確認。1ファイル82行追加・6行削除で、適用後のSHA-256は実コンパイル元と一致した。現行main全体のビルドや実行は今回行っていない。R007/R009の差分は含まない。 [適用原票](../experiments/vesuvius/r005/20261113-upstream-preparation01/application.json) · [凍結差分と同一のR005.patch](../experiments/vesuvius/r005/20261113-upstream-preparation01/R005.patch)

［一次・上流］公開GitHub検索で4条件のPR結果0・6・6・0件を受領し、近縁4件の本文とファイル一覧を確認した。調べた範囲で同等PRは見つからなかった。関連issue #2500は低keepの初期UV strideを報告しており、今回の変更は既存solver後の成分別UV平行移動に限定した。固定ツリーには対象経路に適用される下位AGENTSがなく、ルートのVolume Cartographer指針、寄稿条件、PRテンプレートを参照した。 [検索原票](../experiments/vesuvius/r005/20261113-upstream-preparation01/duplicate-search.json) · [関連issue](https://github.com/ScrollPrize/villa/issues/2500) · [固定寄稿条件](../experiments/vesuvius/r009/20261113-upstream-preparation01/upstream-CONTRIBUTING.md)

［一次・既存証拠］二つの実面で別成分をまたぐ有効格子辺106/284→0/0、異成分拒否189/399→0/0。第一面の事前選定した辺の実CTでは両成分混合1280画素→分離した2 ROI各0。平行移動はsolver後のUVに適用し、幅・画素位相が変わる。元面IDを追った比較で、同一出力画素の比較ではない。同成分の重なりは残り、CT比較の成分2の紙面対応は未確定。144/145の固定ラベル候補では異成分混合に近い判読対照を得られず、文字の読みやすさは未確認。 [幾何独立検証](100-r005-pack-native-verification.md) · [CT独立検証](104-r005-ct-render-verification.md) · [注釈対応](144-r005-known-label-overlap.md) · [影響範囲](145-r005-label-candidate-affected-region.md)

## 本人向け

離れた表面片を横に並べて、展開画像の中で隣の片のCTが混ざる箇所を減らす任意設定です。英語案では本人の実利用例、本人が書く有用性、本人確認欄を空欄にし、必要な前後の実画面は未取得とした。所有図とCT図は、実データから作った比較図として再現手順に載せた。新規の画像・CT取得、ビルド、描画、推論、外部投稿、追加費用はいずれも0。 [英語案](../experiments/vesuvius/r005/20261113-upstream-preparation01/PR_DRAFT.md) · [再現手順と既存図](../experiments/vesuvius/r005/20261113-upstream-preparation01/REPRODUCTION.md) · [lab登録候補](../experiments/vesuvius/r005/20261113-upstream-preparation01/record.json)
