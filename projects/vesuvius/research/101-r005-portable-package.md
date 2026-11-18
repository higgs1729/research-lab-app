# R005 成分配置の再現パッケージ

2026-11-12。製品パッチの[実装](99-r005-pack-native.md)と[独立検証](100-r005-pack-native-verification.md)を終え、持ち運べるレビュー用成果を `deliverables/vesuvius/flatboi-pack-components-20261112` へ凍結した。公開・PR・応募は未実施。追加の有料計算は0米ドル。電力・LLMは個別金額換算していない。

## 成果と確認

- [日本語説明](../deliverables/vesuvius/flatboi-pack-components-20261112/REVIEW_JA.md)、[再ビルド・実行・計測手順](../deliverables/vesuvius/flatboi-pack-components-20261112/README.md)、一ファイルの製品パッチ、別の観測パッチ2枚、入力URLとSHA-256、比較結果、成分所有の図、持ち運べる計測コードを含む。
- [ZIP](../deliverables/vesuvius/flatboi-pack-components-20261112.zip) は15ファイル、88,274 bytes、SHA-256 `a005899e9c69a690fc51a7c307b31d33595f4588e62e9858c664290315276be5`。`__pycache__` は含めない。
- 内容manifest SHA-256は `b95fa4740c52caa1186a2adae976eae9dcdd1e6a7797be7b868dcaab07ce53a0`。ZIP内の全ファイルのハッシュとCRCを照合した。
- portable evaluatorを保存済みの第一面before/after/low-keep、第二面before/afterに実行し、独立検証済みの16個の数・距離の要約項目と一致した。新しい科学的独立検証ではない。
- 製品パッチとパスを正規化した観測パッチを別のソースコピーへ適用し、凍結済みの計測版ソース2ファイルとバイト単位で一致した。元の実験・通常バイナリを変更していない。
- 相対Markdownリンク、JSON/Python構文、Linux bash例の構文を確認した。任意の観測用CMake再ビルドの手順自体を最初から再実行したとは扱わない。

記録は `experiments/vesuvius/r005/20261112-pack-delivery01`。check01は5ケースの数値を確認した後、Windows GitのexFAT所有者判定で失敗。check02は適用後のCRLF変換でバイト比較に失敗。check03はソースのblobを照合し、コマンド単位の `core.autocrlf=false` で成功した。恒久的なGit設定は変更していない。bash構文の最初の確認もWindows subprocessのtextモードでCRLFが入り失敗し、同じ文をUTF-8 bytesで渡して成功。失敗を成功した実験として数えない。

## 応募との距離と次の一件

[公式Progress Prizes](https://scrollprize.org/prizes)と[2026年11月の応募フォーム](https://docs.google.com/forms/d/e/1FAIpQLSeB6MC_--4UCCEGc3zalX57-uE4puRcE_vJoYJCrEt4uYaaaw/viewform)を読み直した。現在の締切は2026-11-30 23:59 Pacific。フォームは公開成果URL、氏名・メール・チーム説明と、実データ・有用性・従来より可能になったこと・根拠の説明を求める。PRだけが公開先ではない。一方、受賞は裁量であり、公開しただけで受賞できるとは扱わない。

成分を分ける機能を主成果、評価コードを付属資料とする。実際の表面画像・断面での意味をまだ示しておらず、CTの繊維が見える、紙面を跨がないとは主張できない。次の一件は、既存の第一入力について元CTの公開対応と小領域描画の可否を調べ、保存済みbefore/after出力の実画像根拠を低費用で作れるか判断する。数値の微調整へは戻らない。

[上流のAI補助PR方針](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/CONTRIBUTING.md)の人間による利用・説明・レビューは未充足。AI実験を人間の行為として代筆して満たさない。Volume CartographerのGPLv3とvillaルートのMITを原文のまま同梱し、元コードを一律MITと扱わない。公開・応募経路と賞のライセンス条件を満たすと断定していない。
