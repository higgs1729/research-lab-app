# PHerc1218の固定候補中央における紙面診断

[研究165](../../../../research/165-pherc1218-sheet-diagnostic.md)。元CTから固定四断面を作った。w035の工程対照では明るい連続帯を追えた。PHerc1218では4断面中3以上で同じ紙面を法線原点付近に一意に追う条件を満たせず、現条件での紙面対応は未判定。紙面が一貫してずれているか、別の紙面が混ざるか、紙面を飛び越えているかも確定しなかった。[四断面](sections.png) · [目視記録](section-assessment.json)

## 固定入力と再現

PHerc1218、公式masked L0 `20250521120456`、8.64 µm。Jake-vc固定revision `6eba0e778fea52ac9044e4e3ec58dab0f82f968c` の `seg_big/w083_main/flat/tifxyz/flatten.tifxyz`。`box_C2f_w081` は先行箱の名前。実面名 `w083_main` との物理的な巻きの同一性は未確認。全体canvasの `x=[9162,9418), y=[2012,2268)` を使用。L0、scale 1、bicubic、非反転法線、49層 `d=-24…+24`。断面は `Y=2076/2204`、`X=9226/9354`。先行の予測画像は取得せず、目視からも外した。データ提供はVesuvius Challenge、派生面はJake-vc、CC BY-NC 4.0。[研究164の固定計画](../20261113-next-target01/README.md) · [派生面の固定版](https://huggingface.co/datasets/Jake-vc/first-light-pherc1218/tree/6eba0e778fea52ac9044e4e3ec58dab0f82f968c)

`acquire.py` は公式メタデータとLFSの3 TIFFを確認し、元CTは計画に入ったキーだけを扱う。`native_run.py` はR140の実引数とR159の計測関数、既存R103/R123バイナリと依存を使う。`launch.sh` はD:を専用mountでread-onlyにする。`analyze.py` はR103既存Windowsランナーで計画と集計を実行する。取得・描画なしで再確認する場合は `plan.json`、`ct-audit.json`、`sections.png` と `section-assessment.json` を読む。再実行を選ぶ場合は別の作業コピーで、mesh→geometry→plan→head→ct→render→compareの順。各工程は既存原票の出力を上書きしない。

## 計測

- TIFXYZ三軸の実628×297とfloat32 scaleからcanvas 12,560×5,940を再構成。`-1` 欠損を除く既存renderer規則により、公開のauto-crop `(19,19,12521,5901)` を再現。16区画のUV原点・刻みを照合し、有効基点・法線は65,536/65,536。隣接XYZ距離の最大はY 1.0002、X 1.0319 voxel。2 voxel超は0件で、平坦化幾何自体に大きな局所飛びは観測されなかった。この指標は物理紙面との対応とは別。[計画原票](plan.json)
- 全49層の三線形8隅と±0.001 voxelの余裕から18キーを凍結。範囲は `z=85..87, y=39..40, x=28..30` の直積。HEAD全18件のContent-LengthとETagをGET時に照合。raw CT 37,748,736 B、LFS 2,239,008 B、追加公式メタデータ3,042 B、本文計39,990,786 B。ネットワーク取得工程計75.376秒。[メッシュ取得](mesh-result.json) · [HEAD](head-result.json) · [CT本文](ct-result.json)
- 製品をオフラインで1回実行。49枚のTIFFとZarr L0の4チャンクは全3,211,264値で一致。L0 shape `[49,256,256]`、chunk `[49,128,128]`、OME参照L0のみ。Zarrの `canvas_size` は出力crop寸法で、全体キャンバスの対応は入力幾何と製品ログで確認した。固定断面の各7横位置×7深さ、計196点の元CT8隅、基点、法線、float64補間とuint8値を保存。最大差0.49548 DNで全196点が最近接丸めの範囲。出力0値は全深さで0件。[製品ログ](render/render.log) · [CT照合](ct-audit.json)
- w035対照は保存元CTの28層、中央行、全深さのうち中心±13.5 voxel、既存反転法線を表示時だけ反転して幾何法線順にそろえた。対象では中央の暗帯がY2204の局所x=96と128で `d≈+1`、x=160で `d≈+4` に出る。負側にも別の暗帯があり、中央帯を空隙・境界・紙面のどれとするか決められない。他の断面にも複数の局所帯と途切れがあり、紙面の代表深さは未測定。目視結果を主担当も同じ予測画像なしの図から独立に確認した。[目視記録](section-assessment.json)

現状を次に判定するには、保存CTの直交断面上で紙面の両縁または連続した実層を独立に追跡し、同じラミナの点を `P+dN` へ戻す根拠が必要。一定の補正は符号付きの距離が一貫した場合に判断できる。今回の濃淡のみから深さ補正、紙面誤り、インクや文字の有無は判定できない。

主担当の別コードは幾何16区画のヘッダー・SHA、固定LFSと18 CTキー、保存全3,211,264値を照合。4断面の重複を除く全49,980値のfloat64補間と保存uint8の最大差は0.4999967 DNで、固定float32丸めは全値一致した。w035の明帯は工程対照の一例で、`|d|≤2` の普遍的校正ではない。独立照合1.666秒、製品再起動0。[独立検査コード](lead_check.py) · [独立照合結果](lead-check.json)

## 資源と原票

1 CPU、数値thread 1、AS4 GiB、core0。幾何16区画の工程13.477秒、製品1.733秒・最大RSS137,592,832 B。Windows集計の成功回は計画1.283秒・集計0.454秒、最大RSS92,684,288 B。新規ファイルの総量は結果保存時点で約52 MB、ホストC:空き約42.4 GB。新ビルド・推論・モデル取得・追加クラウド支出0。電力・モデル費は未算定。開始票にnative/取得のPID・PGID・期限を保存。Windows集計にはPID・期限と既存Jobの4 GiB制限がある。[幾何工程](geometry/stage-result.json) · [製品プロセス](render/render-process.json) · [集計プロセス](compare02-process.json)

計測コードの初回停止は原票を保持した。計画ではWindows `runpy` のモジュール経路、次にTIFXYZの `-1` 欠損の扱いを修正した。集計では出力の `canvas_size` を全体キャンバスと見込んだ照合を、実際のcrop寸法と製品ログの照合へ修正した。観測版と製品の再起動はなく、停止後は同じ保存結果を集計した。[計画初回](plan-process.json) · [計画二回目](plan02-process.json) · [集計初回](compare-process.json) · [lab登録候補](record.json)
