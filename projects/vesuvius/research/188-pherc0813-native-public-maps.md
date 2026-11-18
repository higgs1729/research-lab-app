Status: resolved
担当: 研究（R188担当、2026-11-14 JST）
Blocked by: 187

# PHerc0813の別来歴一面の原寸予測から、元CTへ戻せる字画候補を選べるか（2026-11-14）

## 依頼

186の固定計画 next-plan.json に従い、PHerc0813 z12496_w020 の公開予測を原寸で確認する。同巻のsurvey面とは別のspiral-fit由来の一面。作者の繊維目視ゲートaprova、面積1.73cm²。ただし作者は配布全体に自身の文字screen通過例がなかったと明記している。CTを取り直す前に、今回の一面に独立字画や行の候補があるかを調べる限定探索で、文字発見済みとは扱わない。

固定mesh GitHub pscamillo/vesuvius-eligible-meshes 620769e2e1e70d1e61b588092229cb76d3af4804、固定予測HF pscamillo/vesuvius-eligible-meshes-ink9 dd968475bca14ccfbfd7b06cc6ba87723bb25642。一面の無接尾TIFF1,135,632 Bとreverse TIFF1,300,494 Bは186 next-planにLFS SHAを保存。順逆ラベルは作者訂正済みでreverse suffixが公式forward相当、無接尾が公式reverse。これは既存seed43 step060000・31層中7:24で生成した公開予測の比較で、新しい推論は行わない。

取得前に固定meta/XYZの公開ファイル長を確認する。新規予測2本計2,436,126 B、XYZ3枚合計2MiB以内、必要meta512KiB以内、総5MiB/通信120秒を上限。CTボクセル、別面画像、重み、依存、build、有料計算、外部公開/送信なし。新規C出力、D読取のみ。188へ進む前に187で直した入口を使用し、その入口で同階層import/保存資産の解決を確かめる。CT取得・描画・モデルforwardは不要。

欲しい形は、二方向の実寸・dtype・長さ/SHA、mesh節点格子/scaleと予測full canvas寸法の関係、元CT/生成履歴/方向の確認、同じ固定0–255階調での原寸図、有効範囲と画素座標、字画/行の独立目視による判断。出版社のsame gridを低解像度XYZ節点と画像の一対一対応とは仮定しない。小さい範囲の直接幾何検算で位置式を確認できれば示すが、nativeの新ビルドは不要。寸法だけ一致して厳密な同一生成条件が不明ならその限界を残す。

全体縮小図だけで字画判定せず、有効部の原寸を見られるページ/切出しと固定座標を残す。閲覧用の回転/拡大/階調変更を使う場合は元画像と区別する。単独のモデルスコア、孤立塊、格子や繊維沿いの反応を文字と断定しない。輪郭・間隔・同じ向きの連続がある場合に具体的なnative ROIを提案し、主担当も別目視する。なければその一面で閉じる。新たな深さ探索や面補正へ進まない。

CPU1、commit4GiB、数値ライブラリ1thread、局所画像処理120秒目安。予測の原寸表示は逐次で構わない。重要な結論を主担当が別確認後に記録を確定する。保存先 experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/。研究票へ結果、再利用経路、原票/図、manifest/lab候補を残す。lab登録親、サブ委任なし。

今回はgpt-6.1-sol / high。固定された公開一面の取得・既存表示手順の適用と座標契約の確認で、R186選定と187入口修正後の逐次作業のため。
## メモ

- R186固定計画・作者カードと生成法を確認。GitHub固定ディレクトリのファイル長を先に確認してから、XYZ三枚・metaと固定二予測を取得。Git blob/LFS SHAが一致。原寸は両予測2560×1120 uint8、XYZは128×56 float32。続けて有効範囲の検算と原寸比較を行う。

## 結論

2026-11-14 JST。[一次・目視] PHerc0813 `z12496_w020` の二方向を担当と主担当が原寸10枚で別々に確認した。広がった塊、Y/T状の分岐や弧は見えるが、線幅と輪郭が続く独立字画や行を選べなかった。この一面で閉じ、CTの追加取得、深さ探索、面補正は行わない。 [原寸図一覧と手順](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/README.md) [主担当の別目視](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/lead-visual.json)

## 根拠・詳細

- [一次・実測] 固定二予測は2560×1120、単チャンネルuint8。公式forwardは `_reverse` 接尾で1,300,494 B、reverseは無接尾で1,135,632 B。長さとLFS SHAはR186の固定計画に一致。取得前に固定GitHubのXYZ長を確認して取得し、Git blob SHAも一致した。予測・XYZ・metaと一覧の受信は計2,531,901 B、通信6.806秒。 [固定入力・SHA](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/acquisition-plan.json) [取得原票](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/acquisition.json)
- [一次・実測] XYZは128×56 float32、scale 0.05。保存rendererのscale 1の名目式でfull canvasは2560×1120。実4節点を用い、画素 (1850,550) は元ボクセルXYZ (3372.214947,3271.628152,12941.100107) と算出した。主担当は元XYZからこの点、有効5,138節点・四隅有効4,946四辺形、原寸全5,734,400画素の値を別検算した。 [座標原票](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/review01/pixels.json) [主担当の検算](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/lead-check.json)
- [一次・実測] 四隅有効支持は1,978,400画素、bbox `[20,60,2520,1040)`。両予測の共通非ゼロ2,582,528画素は支持域を全包含し、各604,128画素が域外。非ゼロ領域は左上起点64×64のブロック占有で再現するが、その生成原因は未確認。 [支持域とブロック原票](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/support-check.json)
- [一次・推論] 公表生成法はspiral fit → flatten → TIFXYZ、scale1・L0・31層/step1、seed43 step060000・層7:24。公式のscan `20250720160015`・volume `20250821151723`（9.362 µm、113 keV）と公表条件は整合する。面metaにvolume URLやrenderer commitはなく、当時のレンダーとCTの厳密な画素対応や物理面の正しさは未確認。 [来歴と確認範囲](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/README.md)

## 取得の経路

Windowsの新入口で同階層 `common.py` と保存済みのR186計画を解決し、固定取得と原寸図・支持域の生成を実行した。LZW TIFFは既存のPillowで読めた。元TIFFの0–255を保持した原寸図と位置索引を保存した。CT、描画、新規推論、ビルド、依存追加、支出、外部公開は0。 [再実行](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/README.md) [manifest](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/manifest.json) [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0813-native-public-maps01/record.json)
