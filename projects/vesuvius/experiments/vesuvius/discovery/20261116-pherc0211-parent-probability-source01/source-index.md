# PHerc0211 v6 旧Studio全親確率の公開所在

2026-11-16 JST。確認した公開範囲では、旧Studio全親確率の原本と取得先を特定できなかった。現時点の証拠で固定候補の旧確率値、既読文字との対応、新規性は判定できない。新文字0。

## 一次資料と確認範囲

| 確認先 | 応答・照合結果 | 保存先 |
| --- | --- | --- |
| [公式受賞記事](https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211) | 匿名GET HTTP 200、201,495 B。記事の成果物リンクは下記Drive。GitHubモデル・weights・訓練データ・VC3D forkへのリンクも確認。画像の配信URLからプロキシ署名部分を除いてHTMLを保存。生レスポンスのSHAは保存 | [記事HTML](sources/award-current-public.html)、[リンクとSHA](source-evidence.json) |
| [公式公開Drive](https://drive.google.com/drive/folders/1bvKolL_TIE3k5Ixi1qlOiAmofQ6r2ocH) | 連携のフォルダ一覧を直下22件、全8下位フォルダ44件まで確認（各上限100、全応答で100件未満、計66件の列挙）。READMEを連携で確認後、匿名GETで5,897 B・HTTP 200、R234の原本とSHA一致 | [一覧とファイルmetadata](sources/drive-inventory.json)、[原README](sources/drive-README-raw.md) |
| [公開line2 ZIP](https://drive.google.com/file/d/1CGqmGKvKznjKCXw1xmo_OPclnLn681D3/view) | 匿名GET HTTP 200、4,953,331 B、R234の保存ZIPとSHA `9e9105d9bb812e6d2af454b30cb724e6339f0f0403e06eb28a302b484d31db36` が一致。39エントリ。親側はメッシュ・座標・orientation・case・results・平坦化記録。旧確率SHAが現れるのは `mesh/parent/results.json` と `mesh/results.json` の同一 `models.studio` 記録。確率本文・対応する `studio-mask.png` は一覧に出ない。再取得したZIPの複製は照合後に除いた | [ZIP一覧と記録](source-evidence.json)、[R234保存ZIP](../20261115-pherc0211-adjacent-context01/sources/v6-line2-mesh.zip) |
| [著者のGitHub repo](https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt) | 連携。現行のmainとsoft-lossブランチ先端、Drive README固定commitのrecursive treeは各115・106・114エントリ、いずれも `truncated=false`。公開releaseは2件・assets3件でcheckpoint。crop1711の公開用スクリプトは2026-10-23のDinoVol Original/Rev1へCPT結果を追加する。参照JPEGはその系列のstock/CPT比較 | [treeとrelease](sources/github-inventory.json)、[著者CPT README](sources/github-cpt-README-current.md)、[公開用スクリプト](sources/github-publish_crop1711.sh)、[推論アダプタ](sources/github-infer_studioms.py) |
| [著者repoのissues](https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt/issues) | 連携。 `crop1711`、`PHerc0211`、旧確率の完全SHAを各title/body/commentsで検索し各0件、`incomplete_results=false`。issues一覧・全stateの応答も0件。repo metadataは `has_discussions=false`。Discussionsのrepo限定web検索も関連ヒットなし | [検索条件と応答](sources/github-search.json) |
| [Studio epoch 9モデル](https://huggingface.co/paranke/vesuvius-814-841-9b-resunet-studio-20260926)、[CPTモデル](https://huggingface.co/paranke/vesuvius-studio-multiscroll-cpt-20261023) | 著者READMEからの公開モデル。匿名GETで両方のルートtreeはHTTP 200、11・6件。epoch 9のLFS OID `ffffbf4f…dbd91145` は全親記録のcheckpoint SHAと完全一致。モデルカードはepoch 9のweightsと一般の再推論手順を記載。旧全親mapへの参照は見つからなかった | [epoch 9 tree](sources/hf-model1-tree.json)、[CPT tree](sources/hf-model2-tree.json)、[epoch 9モデルカード](sources/hf-stock-README.md) |

記事参照のVC3D forkのREADMEはソフトと利用手順を案内する。学習用データ本文、CT本文、Gitの全履歴、公開Discord等は検索範囲外。公開webでは親の完全ID、旧確率の完全SHA、記事とcrop1711の組合せで限定検索し、既知記事以外の同定情報は得られなかった。

## 照合した識別子と座標

- 旧親の行列shape `[4600,6060]`、geometry SHA `7ca0b190874dd574f08c9caf257e85d6b28250d4f1295bb03596975bbf5c36bd`、確率SHA `0bf20b28456e449568b55ffdf4f51f87ace093cbc66f4e7a23b9a0547070f3e1`。旧checkpointは上表のepoch 9。GH200 hybrid FP8/BF16、6,663 tiles、stride 64、normal sign −1。旧推論記録の `output_bytes=111504000` は `4600 × 6060 × 4` と一致する。媒体のファイル形式と格納サイズ、`probability_sha256` の対象（シリアル化ファイルまたは画素バイト列）は、原記録と公開推論アダプタでは確定できない。アダプタの保存処理はケース別 `infer.py` の `commit()` を呼ぶ。 [旧親原記録](../20261115-pherc0211-candidate-sheet01/sources/mesh__parent__results.json)
- 固定候補 `XYWH [4416,2048,384,256]` は、親配列の半開範囲 `[2048:2304,4416:4800]`。公開line2の親範囲 `[2980:3580]` と重なる行は0。現行line2は600×6060、11,940,462 B、soft-lossのGH200/BF16再現。3行版v9は1740×6020、38,709,184 B、別manual revision（同soft-loss系列）。R239の候補出力はsoft-loss/FP32の窓計算。現在公開の2 TIFF・R239候補・著者のDinoVol比較JPEGのいずれからも旧候補値は取り出せない。

再開の根拠は全親mapを指す正規の公開リンクと、版・幾何・ハッシュ対象を定める原資料。揃えばその形式とサイズを確認し、ファイル全体または画素列全体で旧SHAを照合できる取得方法を選ぶ。確率本文が8 MiB超の場合は、その時点で取得案を主担当へ戻す。ROIの比較はこの座標で行う。

確率本文の取得0 B、追加CT観測・モデル推論・対外送信・支出0。再取得ZIPを含む一時保存は6 MiB未満。局所照合は[実行記録](source-evidence-process.json)上、CPU 1、commit上限4 GiB、RSS約32.3 MiB、終了値0。採取時のC空きは9,724,116,992 B。
