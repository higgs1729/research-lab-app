Status: resolved
担当: 研究（2026-11-16 R241）

# 241: 旧Studio全親確率の公開原本と候補座標を確認できるか（2026-11-16）

## 依頼

- 問い: R240で確認したv6親面の過去の全体推論について、公開されている確率原本を特定できるか。特定できる場合、R239の固定候補が過去にどんな反応を示していたかを正しい座標で比較するための根拠を揃える。
- 前提: R240は `record-bd5e4f932a73` に登録済み。候補parent XYWH **`[4416,2048,384,256]`** は部分的な局所CT支持を得たが、全ROIの同一紙層・インク・読字・新規性は未確認、新文字0。科学上の保留であり本人判断待ちではない。局所CTの追加断面/深さ探索は終了。研究の主目的は発見で、公開済み三改善を11月一件応募へまとめる方針は維持。
- 元資料: `experiments/vesuvius/discovery/20261115-pherc0211-candidate-sheet01/provenance.md`、同`joint-decision.json`、`sources/mesh__parent__results.json`。元ZIPは `experiments/vesuvius/discovery/20261115-pherc0211-adjacent-context01/sources/v6-line2-mesh.zip`、SHA`9e9105d9bb812e6d2af454b30cb724e6339f0f0403e06eb28a302b484d31db36`。親IDは`PHerc0211-crop1711-manual-20261026-1237-legacyuv20-v6`、親shape4600×6060、旧checkpoint`ffffbf4fcb2f1eb91940a6899366cd0d22b2ea03987270d07dc2a205dbd91145`、確率SHA`0bf20b28456e449568b55ffdf4f51f87ace093cbc66f4e7a23b9a0547070f3e1`、geometry SHA`7ca0b190874dd574f08c9caf257e85d6b28250d4f1295bb03596975bbf5c36bd`。元記録は6663tiles/stride64/GH200 hybrid FP8/BF16で、今回R239のsoft-loss/FP32と同じではない。SHAの対象がファイルbytesかraw画素かは原文/生成元に従い、推測しない。
- 公開資料の既知入口: 公式受賞記事 `https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211`、記事からの公式公開Drive folder `https://drive.google.com/drive/folders/1bvKolL_TIE3k5Ixi1qlOiAmofQ6r2ocH`、著者公開repo `https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt`。R234の`sources/drive-README.md`、`drive-folder-list.json`、`sources/cpt-README-fixed.md`、R240の`sources/github-reference-metadata.json`が保存済み。現在のファイル一覧や更新の確認に必要な範囲で最新の公開原文/metadataを読む。これらは入口の例で、原文が示す別の正規公開先も調べてよい。
- 欲しい成果: 旧全親mapの公開所在/形式/大きさ/版・モデル・幾何の一致を明確にする。現在配布されるline2 soft-loss cropや別manual v9 fullmap、旧stitched比較JPEGを、この全親原本と取り違えない。保存済み原文と、今回実際に確認したURL/応答/件数・検索範囲を残す。見つからない場合は「確認した公開範囲では特定できなかった」とし、不存在・未推論・未読の証明にしない。R239の新規性は引き続き未確認とする。
- 取得と比較: まずmetadata/小さい原文で所在・identity・サイズを特定する。対象確率の本文が8MiBを超える場合は取得前に、全取得か形式に沿った限定読取か、保存量/C空き/ハッシュ照合可能性を具体化して親へ返す。親の内部判断で無料取得を進められるので本人の許可を求めない。原本が小さく確実に取得可能なら、初期16MiB枠内で取得してよい。画像比較は必ず固定候補ROIの座標契約を先に保存し、モデル差/精度差/入力差を保持する。比較図の解釈は担当が先に保存し、親へ初報は図pathと数値だけ渡す。原本がないままJPEGへの探索的な画像合わせを繰り返さない。
- 運用: 研究は本件一つ。再委任なし。主担当の登録/phase/automationを変更しない。R236–240の凍結根拠を書き換えない。Dは直接ファイル読取のみ、Git/新規書込みなし。C新規16MiBの初期上限、C空き2GiB以上。計算は `tools/research/run_windows.py` のCPU1/hard commit4GiBで実行。ネットワークは正規の公開資料への限定読取、認証情報/署名URLを記録や標準出力へ漏らさない。既存コネクタが対応する場合は優先、未対応なら原文に示された公開経路を利用する。
- 範囲外: 新CT、surface変更、モデル推論、GPU/有料サービス、無制限の全データ探索、他ROIへ変更、他者へのメッセージ、公開/応募。私有アカウントのデータを推測して探したり、認証・アクセス制限を迂回しない。
- 残すもの: 保存先 `experiments/vesuvius/discovery/20261116-pherc0211-parent-probability-source01/`。区切りで本票メモへ追記し、本人質問なしで有用な一次照合を進める。重い取得・座標付き画像比較へ進める具体案があればその段階で親へ返し、単に探索が終わった場合は結論/検索範囲/未確認点/次に必要な一手を票へ追記する。親の独立確認後にREADME/manifest/recordを凍結。lab/recall登録・次課題選定は親が行う。

## 結論

確認した公開範囲では、PHerc0211 v6の旧Studio全親確率原本を特定できなかった。候補 `XYWH [4416,2048,384,256]` の旧確率値、既出文字との対応、新規性は引き続き未確認。新文字0。 [調査範囲と証拠の索引](../experiments/vesuvius/discovery/20261116-pherc0211-parent-probability-source01/source-index.md)

## 根拠・詳細

- [一次、2026-11-16] 公式記事と公開Driveを確認した。Drive直下22件と8下位フォルダ44件にある確率TIFFは、現行soft-lossのv6-line2と別v9の2件。公開line2 ZIPを匿名で取得し、R234の保存ZIPとのSHA一致と全39エントリを照合した。旧Studioの全親shape `[4600,6060]`・geometry SHA・確率SHAはZIPに記録される。旧確率本体と対応マスクの公開ファイルはこの範囲で特定できず、旧SHAの対象と媒体形式・格納サイズも未判定。 [公開Drive](https://drive.google.com/drive/folders/1bvKolL_TIE3k5Ixi1qlOiAmofQ6r2ocH)
- [一次、2026-11-16] 著者GitHubの2ブランチ先端、READMEの固定commit、2公開リリースを照合。crop1711の比較JPEGと公開用スクリプトはDinoVol Original/Rev1系列。GitHubのissues検索3件は各0ヒット、一覧0件、Discussions無効。Hugging Faceの公開メタデータでは、親に記録された旧checkpoint SHAがepoch 9のLFS OIDと完全一致。 [著者repo](https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt) [epoch 9モデル](https://huggingface.co/paranke/vesuvius-814-841-9b-resunet-studio-20260926)
- [計算、2026-11-16] 固定候補は親配列の `[2048:2304,4416:4800]`。公開line2の親行 `[2980:3580]` と重なる行は0。旧StudioのGH200 hybrid FP8/BF16、現行line2のsoft-loss/GH200 BF16、R239のsoft-loss/FP32ではモデルまたは数値条件が異なる。候補比較図は作成せず、公開所在の判定に絞った。 [照合記録](../experiments/vesuvius/discovery/20261116-pherc0211-parent-probability-source01/source-evidence.json)

## 取得の経路

DriveとGitHubは連携を使用。記事HTML・DriveのREADMEとZIP・公開HFメタデータは公開URLのHTTP応答で確認した。Web検索の完全ID/完全SHA等は探索補助として使い、一次資料へのリンクと件数を索引へ保存した。再開するなら旧全親mapを示す正規公開URLまたは原記録の明示する確率出力先を先に確認し、サイズ・版・幾何・ハッシュ対象を揃えてから取得を判断する。

## メモ

- 2026-11-16 R240を登録後に主担当が起票。旧全親推論の履歴は元JSONで確認済みだが、原本の公開所在と候補個別の旧反応は未確認。追加GPUや同じ局所CTの救済観測より先に、この欠けている来歴を限定して確認する。
- 2026-11-16 公開Driveの直下22件と全8下位フォルダの44件をメタデータ照合。確率の配布名は現行line2と別v9の2件。GitHubの現行2ブランチ先端・Drive README固定commit・公開リリース2件も取得。公式記事HTTP 200。次は記事の配布リンク、v6 ZIP内の親記録・実ファイル一覧、著者repoのcrop1711公開用スクリプトを照合する。
- 2026-11-16 元ZIPとのバイトSHA一致、全39エントリ、DinoVol用スクリプト、旧checkpointのLFS OID、公開issues/discussionsの範囲を照合。旧全親確率の候補URLは見つからず、重い取得の判断事項は生じなかった。証拠索引と結論を保存し、主担当の独立確認へ渡す。
- 2026-11-16 主担当の独立確認で、v6 ZIPの全項目数を39件（ディレクトリ0）と再確認した。研究票と証拠索引に記載した38件を39件に訂正。保存済みの全項目一覧は39件で一致していた。
- 2026-11-16 主担当の独立検算が完了。ZIP全39項目、旧2 JSONの一致、公開旧checkpoint、公開Drive全9フォルダと2 TIFF、GitHub 3 tree・2 releases・issues 0件、座標非重複を再確認した。初回件数assertの停止記録も保持し、この票と全根拠をmanifestへ固定。 [研究成果と検算](../experiments/vesuvius/discovery/20261116-pherc0211-parent-probability-source01/README.md)
