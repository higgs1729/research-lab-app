# R004候補の一次資料取得記録

- 2026-11-11 21:08–21:12 JST、GitHubコネクタで `repo:ScrollPrize/villa is:issue is:open` をupdated降順40件、候補のコメントを取得。コネクタの `is:pr` がissueを返し、正規化結果のstate等も空だったため、PRはGitHub REST・CLIに切替。対象時のmainは `08df18e46303cf7da9803c160217fa6ef8ea3392`。
- [最近更新されたPR 40件のRESTクエリ](https://api.github.com/repos/ScrollPrize/villa/pulls?state=all&per_page=40&sort=updated&direction=desc)。PRを全状態で `2144`、`2167`、`label topology`、`fix_holes`、`w036` で検索。#2144に直接関係する候補は#2147のみ。w036と#2167の直接検索は0件で、#2147の本文には#2167への参照がある。検索で未発見の別実装が残る可能性はある。
- [#2144 issue REST](https://api.github.com/repos/ScrollPrize/villa/issues/2144) はopen、コメント0、最終更新 `2026-10-18T20:13:34Z`。[#2147 PR REST](https://api.github.com/repos/ScrollPrize/villa/pulls/2147) はopen、最終更新 `2026-11-05T09:35:38Z`、head `b67f708eb9eb42270ff1664af411ab3dcfb9e3fd`。作者の最新会話コメントは10月19日のsurface placement audit追加。実装は [veto](https://github.com/ScrollPrize/villa/pull/2147/commits/408f098) と [学習書き出し](https://github.com/ScrollPrize/villa/pull/2147/commits/5681008)。[#2368](https://github.com/ScrollPrize/villa/pull/2368) は法線方向の頂点移動。
- [#2167 issue REST](https://api.github.com/repos/ScrollPrize/villa/issues/2167) はopen、コメント6、最終更新 `2026-11-02T02:53:39Z`。[最新コメント](https://github.com/ScrollPrize/villa/issues/2167#issuecomment-6567910221) は局所の巻き順を未検証とする。[公開メッシュ一覧、CTの入力とバイト範囲](https://github.com/stantheman0128/vesuvius-pherc0139-gap-1129#inputs)。
- [公式Open Problems](https://scrollprize.org/2026_open_problems#surface-prediction)、[進捗賞](https://scrollprize.org/prizes#progress-prizes)、[surface-labels説明とライセンス参照](https://scrollprize.org/data/datasets/surface-labels-README.md)、[m7モデルカード](https://huggingface.co/scrollprize/surface_m7_nnunet)、[recto 3D U-Netモデルカード](https://huggingface.co/scrollprize/surface_recto_3dunet)、[CONTRIBUTINGの現行版](https://github.com/ScrollPrize/villa/blob/08df18e46303cf7da9803c160217fa6ef8ea3392/CONTRIBUTING.md)。
- 除外根拠。#2437のinpaintは[#2476](https://github.com/ScrollPrize/villa/pull/2476)、#2320のfiber ingestは[#2321](https://github.com/ScrollPrize/villa/pull/2321)、#2107の深さピラミッドに[#2501](https://github.com/ScrollPrize/villa/pull/2501)、#2239の中心線に[#2242](https://github.com/ScrollPrize/villa/pull/2242)が対応。#2370のHF65は[公開補正](https://github.com/ScrollPrize/villa/issues/2370#issuecomment-6520937101)と[追試](https://github.com/ScrollPrize/villa/issues/2370#issuecomment-6700279804)がある。#2478は[既存の見積もり提案](../../../../research/29-r002-current-cache-sources.md)に記録済み。

## sample_00379

2026-11-11 21:10 JST、[images](https://huggingface.co/api/buckets/scrollprize/datasets/tree/surfaces/kaggle/images) と [labels](https://huggingface.co/api/buckets/scrollprize/datasets/tree/surfaces/kaggle/labels) のAPIおよび公開URLのHEADを照合。下記の2点は最終応答HTTP 200。xetHashは公開APIの内容識別子であり、ローカルSHA-256は未計算。

| 入力 | バイト数 | xetHash |
|---|---:|---|
| [CT](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/images/sample_00379.tif) | 30,376,525 | `4b1e94d21e822396cacf655c6f408ab051eb0d77d5913ac2f857154e98ea5626` |
| [ラベル](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/labels/sample_00379.tif) | 32,821,210 | `e9396a14225b28358b7c13f88050ef756527a0ad2f1f82b4b62c3b7a52cd9461` |

```text
https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/images/sample_00379.tif
https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/labels/sample_00379.tif
```

[errata.csv](https://raw.githubusercontent.com/Wittmoon/vesuvius-label-topology-audit/6a65a564fc239fe4d2d3d797d77b963697ef5d50/data/errata.csv) での原文行。座標は `center_zyx`。

```csv
id,rank,crop,center_zyx,hole_voxels,verdict_A,verdict_B,consensus,human_verdict,suggested_action
E04,2,sample_00379,"[49, 274, 36]",1617,CUT,CUT,CUT,CUT,separate merged sheets (pocket between sheets)
E05,2,sample_00379,"[125, 33, 60]",833,CUT,CUT,CUT,CUT,separate merged sheets (pocket between sheets)
```

同cropにFILL行なし。公開の[FILL対照E26](https://github.com/Wittmoon/vesuvius-label-topology-audit/blob/6a65a564fc239fe4d2d3d797d77b963697ef5d50/data/errata.csv) は別cropのsample_00833（[CT](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/images/sample_00833.tif) 33,358,455 B、[ラベル](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/labels/sample_00833.tif) 736,601 B）。[穴の形状計測](https://github.com/Wittmoon/vesuvius-label-topology-audit/blob/6a65a564fc239fe4d2d3d797d77b963697ef5d50/data/errata_hole_geometry.csv) はあるが、切断する誤結合の範囲・ボクセルマスク・2枚のIDは確認できなかった。資料の配列軸はz,y,x。ラベルの定義は0背景・1表面・2 ignore。対象TIFFの軸タグ、実shape、ラベル値集合は本体未取得につき未検証。

この調査ではissue・PR・入力のメタデータと軽量な公開テキストのみ取得。サンプル本体、ビルド、実験、外部投稿、有料計算なし。

