# PHerc0800公式面4・面5の固定窓

手元RTX 4060 Tiで、Hecateの有効パッチ1,704件を191.438秒で完走した。画面4条件を担当・主担当が原寸で別に見て、追試の字画・行ROIを選ばなかった。調査を閉じる範囲はこの二窓と固定した16層。物理ラミナ、他の深さ、他の範囲のインクの有無は未判定。

| 公式面 | 主領域 XYWH | 主領域の固定支持 | 順・逆それぞれ |
| --- | --- | ---: | ---: |
| 4 | 736, 1600, 960, 576 | 412,428 px | 469有効 / 589 |
| 5 | 512, 96, 896, 512 | 326,968 px | 383有効 / 493 |

公式8.64 µmラスタの固定90キー45,711,360 Bを取得し、オブジェクト長・ETagと研究218の中央Rangeを全件照合。9.6 µmへfloat64でX、Y、Zの順に補間し、最近接偶数へ一回丸めた。公開層15は新k=8。同じ16枚の順逆、FP32、TF32無効、64×64／stride 32／batch 1。固定支持とモデルのdepth-anyは別記録。親は全19,333,120入力値と2,164グリッドを別検算した。CPU参照12件とのGPU実測差は最大絶対1.669×10⁻⁶。代表104確率配列を保存し、分母2枚・分子4枚から全2,416,640 PNG画素を再構成した。

[入力契約](patch-contract.json) · [担当検算](result-check.json) · [親の検算](lead-result-check.json) · [描画原票](review-panels.json) · [担当の原寸判断](visual-review.json) · [親の原寸判断](lead-visual-review.json)

RunpodのSecure 4090は1回の作成がHTTP 400で拒否され、IDなし。RTX 4000 Adaは1台を作成したが、起動確認の240秒枠でexec 409が解消せず、入力転送前に停止。作成基準から244.871秒で削除確認し、担当と親の別照会でもGET404・専用名0・全Pod0。税別稼働見積はUS$0.01923445。専用Podの明細0行で実費null。口座残高減少US$0.0185941は口座全体の観測値。以後、新規支出や取得を伴わず手元GPUを一回実行し、PID・holder・待ち札の解放を別確認した。

[4090作成原票](run01/startup.jsonl) · [Ada起動原票](run02/startup.jsonl) · [Ada削除](run02/cleanup.json) · [Ada残存の親確認](lead-resource-check.json) · [費用再照会](ada-billing-later.json) · [手元実行](local-supervisor-result.json) · [手元資源の親確認](lead-local-release-check.json)
