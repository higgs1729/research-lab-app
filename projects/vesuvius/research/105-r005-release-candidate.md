# R005 公開候補と応募文

2026-11-12。成分配置の[製品実装](99-r005-pack-native.md)・[独立検証](100-r005-pack-native-verification.md)に、[限定CT比較](103-r005-ct-render-trial.md)と[その独立検証](104-r005-ct-render-verification.md)を追加した。主担当も中心・断面PNGを目視した。別成分の描画拒否と出力辺の混在を二つの入力で0にでき、一つの事前選定した辺では実CTの混合補間帯1,280画素が別ROI各0になった。成分2の正しい紙面対応・繊維や文字の改善は未確認のままとする。

## 具体物

- [公開候補の説明](../deliverables/vesuvius/flatboi-component-packing-release-20261112/README.md)。製品パッチ・再ビルド/再現手順・計測コード・二つの比較画像・元面ID/ROI・必要CTのURL/ハッシュ・独立検証の範囲を含む。
- [ZIP](../deliverables/vesuvius/flatboi-component-packing-release-20261112.zip)：28ファイル、190,659 bytes、SHA-256 `c8a564d6fcb8885db2241581585a2a258a41d316442635b4be1a35c2a060b573`。
- manifest SHA-256 `b2aafcea1c6a504c97ab0986c6e64a7ee98544df41bea05f444b84367adae409`。元の88KBパッケージの全ファイルはバイト不変。相対リンクと構文、ZIP内ハッシュ/CRCを確認した。新しい科学的実験ではない。
- [11月Progress Prizes応募文](../deliverables/vesuvius/PROGRESS_SUBMISSION_DRAFT.md)。実フォームの設問に合わせ、個人のAI研究であること、人間の利用・コードレビューを主張しないこと、未解決範囲を明記。公開URLと送信アカウントは未確定。氏名は本人プロフィール正本、GitHub名は接続ツールとCLIで確認した `higgs1729`。

[公式データの引用・ライセンス](https://scrollprize.org/data)に基づき、新しいVesuvius Challengeデータセットへの帰属とCC BY-NC 4.0の条件を追記した。製品変更全体には元Volume CartographerのGPLv3条件を維持し、新規実装の追加部分と独自計測コードにはMITの追加許諾を用意した。元コードやCTデータを一括でMITに変えるものではない。これらは本人が確認する公開候補に含めた。受賞適格性を保証しない。

## 次の境界

ユーザーの成果説明の依頼へ、別断片が画像上で混ざる問題、二入力での改善、残る同成分内の問題、実CT比較、再利用資産、有料GPU/クラウド計算0を説明した。現在、実装と限定CT比較について追加検証が必要な未解決不具合は見つかっていない。

次はGitHub `higgs1729/vesuvius-flatboi-component-packing` での公開と[11月の公式フォーム](https://docs.google.com/forms/d/e/1FAIpQLSeB6MC_--4UCCEGc3zalX57-uE4puRcE_vJoYJCrEt4uYaaaw/viewform)への提出。上流PRを人間の利用実績なしで送る経路は選ばない。公開・フォーム入力/送信・外部連絡はまだ実施していない。実行環境の外部送信に関する明示指示の要件により、具体物を整えた上で本人へ公開/応募の可否を質問した。これは有料計算の承認待ちや技術判断の差し戻しではない。

この時点で局所最適化・追加ケース・表示調整へ投入を増やすより、具体物を利用・評価につなげることを次の投入先と判断する。返答待ちの間は同じ検査を繰り返さない。主担当・監査・heartbeatの設定は保持し、本人判断だけを待つ状態はlabのholdに記録する。回答後は同じ主担当チャットで再開する。
