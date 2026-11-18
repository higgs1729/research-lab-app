# PHerc0191の同一fit三面を使う広域探索案

PHerc0191の公式再構成 `20250821151635`、L0 z11600–12400、Carson Rodrigues公開fitの `w052 / w053 / w054` を選ぶ。次の一件は元CTで各面の紙層対応を確認する無料試験。通過した固定面について各2048×1024のHecate順逆の広域推論を計画し、同じラミナか区別できない面は代表一面を選ぶ。候補間の順位に先行インク予測の強さは使っていない。 [研究票](../../../../research/212-unread-multiwinding-discovery-lane.md) · [固定入力と条件](next-plan.json)

## 選定の根拠

| 候補 | 得られる範囲と先行との違い | 今回の扱い |
| --- | --- | --- |
| PHerc0191、z11600–12400 | 公式9.362 µmの同一来歴に固定された連続mesh番号が取得可能。同プロトコルSQMで中央値0.413、768-voxel集計の最良帯z11520で0.538。細かいSQMの候補点XYZ `(4656,4656,11952)`、0.913を試験の方位に使う。 | 選択。SQMは元CTの鮮明さと位置を指し、選択した三面の層帰属や可読性は未測定。 [固定fit](lead-hf-fit-readme.md) · [SQM集計](originals/sqm-atlas.json) · [座標](originals/sqm-targets.json) |
| PHerc0358、SQM最良帯z9216付近 | 同プロトコルでCT指標は0191より高い。gmDeviはz8000–9500と9500–11000、三つ飛びのw021–099、rows20–60をflat 9µm両順で調査。一部に押し潰れた多層域を報告。異なる推論は未検討だが、原票からそのfitの座標本体を再利用する入口は確認できなかった。 | 新fit先として保留。著者報告の30k-band fitは24 GB GPUで7件1.0–2.4時間、作業は主に自前3090と無料枠。毎回の入力量とfit条件は異なる。 [先行報告](originals/gmdevi-report.md) · [著者の計時報告](https://manifund.org/projects/search-every-2025-2026-herculaneum-scroll-for-ink-from-one-consumer-gpu?tab=similar) |
| PHerc0826の三fit、またはpscamillo既存mesh | 0826の同公開fit集には前後帯で面番号の一致不良と密度の不確実性があり、巻内の別チームの進捗もある。pscamilloの固定340面は別作者がHecate9.6両順を処理済み。 | 同じmesh・モデルの反復を避ける。340面の先行スクリーニングは未公開結果や可読性の証明を含まない。 [fit作者の重なり評価](lead-hf-fit-readme.md) · [固定340面の処理報告](https://github.com/rodriguescarson/eligible-scroll-atlas/blob/0c0566ccd07652ef4bc9fa1926491983d520942f/README.md) · [親の先行照合](lead-prior-coverage-review.json) |

0191の公式カタログ上でscan `20250720024445` とreconstruction `20250821151635` を区別した。後者はFirst Letters対象。現行の公式Winners一覧に0191の受賞記載は確認できなかった。公開一覧の範囲の確認で、未公表の判読状況は不明。賞の条件は単一4 cm²内の可読10字、学習領域との非重複等。Hecateのモデルカードに0191は確認できないが、全学習座標を確定できず応募適格性は未判定。CTと借用fitはCC BY-NC 4.0。Carson Rodriguesを出典に残す。具体的な公開・応募に使う場合は由来と各条件を改めて照合する。 [公式対象と条件](https://scrollprize.org/prizes#first-letters-prizes) · [カタログ](https://scrollprize.org/data_browser/PHerc0191) · [公式受賞一覧](https://scrollprize.org/winners) · [Hecateの保存カード](../20261114-alternative-ink-model-selection01/README.md) · [借用fitのライセンス](lead-hf-fit-readme.md)

0191の既存 `p191_a` 加工カードのmeshはz8437.77–10576.14、別の公開原寸atlas `kbh-PHerc0191_2707_2976_13281` はz12736.84–14342.55で、ともに今回のfit帯の外。gmDeviの同CTの既存flat seed42（w021–099、三つ飛び、両順54枚）は別fit。固定fitterスクリプトの既定z9000–10500とbatch logの識別子は整合するが、その実行時zを記録するmanifestは確認していない。調べた固定資料では今回の三面のHecate予測を確認できず、過去に誰も見ていないとは判断できない。 [R209の既存カード・固定面](../20261114-unread-surface-evidence01/README.md) · [別atlas面の固定meshメタ](originals/survey-0191-older-atlas-mesh-meta.json) · [既存0191 batch](originals/gmdevi-0191-batch.log) · [fitter既定値](originals/gmdevi-fit-remote.py)

## 無料の元CT試験

三面のmeshはscale 0.05、幅255/260/265×高56節点。作者の全mesh面積は3.585 / 3.655 / 3.719 cm²、計10.959 cm²。面積の値は適格な紙面や重複しない探索面積を表さない。作者のz12000密度評価では厳しいpeakの12/12本でfitが多い一方、緩いpeakの4/12本ではfitが同数以下で、自己相関の推定はfitの上下にまたがる。順番が連続する三面の、実物の一層ずつの対応は未知。主担当がmetaのGit blob、TIFFヘッダ、L0仕様と面積・パッチ算術を別照合した。 [meshメタ、固定木、ヘッダ](fit-metadata.json) · [作者の密度評価](lead-hf-fit-readme.md) · [親の独立照合](lead-metadata-check.json)

まず9本のXYZ TIFF全525,366 Bを固定木のblobに照合する。SQM点の方位でz11952の交点が一意なら、共通方位に合わせて三つのcropを製品座標に固定する。L0 9.362 µmから9.6 µmへの描画scaleは名目0.9752083333、Z stepは約1.0254219184 voxel。cropに有効な面があることを座標で確かめ、CT値を読む前に全断面の位置を保存する。raw CTは非圧縮uint8の128³、2 MiB/キー。既存のR199/R207座標観測とR204の断面抽出を借り、三つの高さ×三方位で三面を同じCT断面に照合する。上限48キー・96 MiB・通信240秒、局所工程900秒、CPU1/4 GiB、C作業512 MiB・空き10 GiBを維持、D書込なし。 [入力座標契約](next-plan.json) · [公式L0メタ](originals/ct-L0-zarray.json) · [既存断面法](../20261114-pherc0483a-surface-provenance01/README.md) · [製品座標と実float](../20261114-pherc0846a-wider-hecate01/roi.json)

両レビュー担当が、各候補面について中心3地点と左右各2地点以上でラミナを追えるかを見る。層間や複数層への明白な横断があった面は除外する。重複または独立性が判定不能な面は、明瞭な地点数、幾何支持率、巻き番号の順で代表一面を選ぶ。幾何支持率65%以上は入力範囲の運用条件。共通断面の基準w053が座標化できない場合と、全候補不通過は停止。通過しても、検査地点以外の全弧の層帰属は残る。 [断面位置、通過条件](next-plan.json)

## 通過時の推論と費用

各2048×1024の中央1984×960を主に読む。1–3面で名目画素面積1.755316–5.265949 cm²、両順3,906–11,718パッチ、R208実測から推論比例約216–648秒、CT中心・順逆の画像生画素量6–18 MiB。描画支持画素を計数し、物理紙面の実面積と区別する。既存製品の33層中心16枚を同じ位置で順8→23、逆23→8。Hecate FP32、64²/stride32、batch1、1 load、各向き各1953。支持のないパッチは公式処理と同様にskipし、元CT中心と順逆の原寸を全域確認する。 [R198の深さ検証](../20261114-hecate-depth-window-control01/README.md) · [R208実測](../20261114-pherc0846a-wider-hecate-run02/README.md) · [固定比較条件](next-plan.json)

ローカルで必要なCTキーを合併し、3 GiB/1536キー以内で取得する。1,048,576画素のR207実測は146キーで、新規102キー204 MiBを約292秒。今回のキー数と有効面積はXYZ確認後に測る。CPU1/4 GiB、C 6 GiB以内・空き10 GiBを維持し、Dは読取。全33×3積層は生207,618,048 B。固定tarを圧縮し160 MiB以下と見通しが確認できた場合にPodへ送る。CTチャンクは送信しない。R208の実績から保守試算した0.10 MiB/sでは上限160 MiBに1,600秒。回収上限32 MiBで、原寸画像、支持、全patchの入力・出力hashと位置、固定少数の確率配列を残す。圧縮率・通信の実測は次工程。 [R207元CT・描画](../20261114-pherc0846a-wider-hecate01/README.md) · [転送見積と停止条件](next-plan.json)

Runpodは単回作成のSecure RTX 4090、20 GB一時container、永続領域なし。起動240・転送/重み1,800・推論900・回収300・削除60秒、作成前から絶対55分。税別 $0.81838（$0.89/h）～$0.82755（入場上限$0.90/h、20 GB、月720時間換算）。US$1は運用管理枠。最新価格・在庫・残高・自動入金と対象台を作成前に再確認し、同じID・名前の自分の台のみを消してGET 404と一覧を独立照合する。親が13:42 UTCに読取した時点は$0.89/h、在庫LOW、残$17.53034、自動入金なし、Pod 0。先行Pod別明細は207 $0.00730、208 $0.05716で、保持時間による見積との区間差は未解明。 [親の照会](lead-resource-cost-snapshot.json) · [公式料金](https://docs.runpod.io/pods/pricing) · [公式削除](https://docs.runpod.io/pods/manage-pods)

R212の計測した固定小資料取得は19応答127,351 B、6.300秒。親のfit原文5,731 Bは別。先に確認した小資料照会とweb表示の転送総量は未計測。三面のTIFF本文、元CTボクセル、描画、重み、推論、GPU、課金、公開は0。 [取得原票](acquisition.json) · [親の原文取得](lead-hf-fit-readme-source.json)
