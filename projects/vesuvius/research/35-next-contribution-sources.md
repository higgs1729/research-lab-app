# R004の候補比較

2026年11月11日。公開issue・コメント、関連PR、主催の募集要項と公開入力メタデータを確認した。照会と入力URLは[一次資料記録](../experiments/vesuvius/r004/20261111-candidate-review/sources.md)。この調査では画像・ラベル本体の取得や実験を行っていない。

## 推薦 — #2144の誤結合を一つ切り離した学習ラベル

**確認した事実。** Kaggleの公開surfaceラベルでは、誤ってつながった二枚の間にできたポケットを既存の穴埋めで埋めると、誤結合が増える。報告者は三断面で確認した6件をCUT、8件をFILLとした。issueはopen、コメント0件。後続の検討で計33件に人手判定が付き、19 CUT、11 FILL、3 UNCLEAR。検討者は専門アノテーターではなく、穴の形状・サイズ・局所CT強度を使った自動判定はいずれも事前の基準を満たさなかった。報告は候補座標と穴の体積を与える。削除すべき橋の三次元マスクや二枚を識別する正解ラベルは確認できなかった。[issue #2144](https://github.com/ScrollPrize/villa/issues/2144) · [人手判定と自動判定の結果](https://github.com/Wittmoon/vesuvius-label-topology-audit/blob/6a65a564fc239fe4d2d3d797d77b963697ef5d50/validation/errata_cutfill.md)

**重複する範囲。** openの[#2147](https://github.com/ScrollPrize/villa/pull/2147)には監査、CUTポケットを埋めない `fix_holes.py --veto`、FILLを適用してCUTを据え置く学習形式の書き出しがある。モデルとの不一致レビューでは欠落面を追加できる。実際の誤結合を切る差分は、確認したPR・公開根拠では見つからなかった。別のopen PR [#2368](https://github.com/ScrollPrize/villa/pull/2368) はtifxyzの頂点を法線方向にスナップするもので、合流したボクセルラベルを二枚に分離する機能は説明されていない。

**実利用。** 主催はこれらの公開surfaceラベルとCTを学習用として案内し、難所の正確なラベルとシートのトポロジー保持を求めている。現行パイプラインを支えるm7は同Kaggle大会のnnU-Net（786学習ボリューム）。このcropがm7の学習に含まれるか、後続学習で採用されるかは未確認。もう一つの主要checkpointのrecto 3D U-Netは、メッシュからボクセル化した別記載の学習データを使う。[公式データ説明](https://scrollprize.org/data_datasets#surface-labels-2026-07) · [公式Open Problems](https://scrollprize.org/2026_open_problems#surface-prediction) · [m7](https://huggingface.co/scrollprize/surface_m7_nnunet) · [recto 3D U-Net](https://huggingface.co/scrollprize/surface_recto_3dunet#training-data)

**入力と最初の試行の見立て。** [sample_00379のCT](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/images/sample_00379.tif) 30,376,525 B と[ラベル](https://huggingface.co/buckets/scrollprize/datasets/resolve/surfaces/kaggle/labels/sample_00379.tif) 32,821,210 B、合計60.27 MiB。公表座標は配列の `(z,y,x)`。E04の `[49, 274, 36]`（1,617穴ボクセル）とE05の `[125, 33, 60]`（833穴ボクセル）は別々のCUT。ラベル値の意味は背景0・表面1・ignore 2。両TIFFの実軸・shape・実値を読み出した上で座標を使用する。公開errataに同cropのFILLはなく、近傍の未掲載箇所には手を加えない。別のcropのFILL対照を追加するならE26のsample_00833（34,095,056 B、座標 `[64,21,265]`）。[座標原表](https://github.com/Wittmoon/vesuvius-label-topology-audit/blob/6a65a564fc239fe4d2d3d797d77b963697ef5d50/data/errata.csv) · [ラベル値](https://huggingface.co/scrollprize/surface_m7_nnunet#model-details)

最初はE04一箇所。CTとラベルを直交三断面および連続断面で見て、ポケットではなく橋を囲う。CTで両面と橋を区別できる場合、両側のシート上に固定した点群を使い、周囲を固定した局所の手動修正または局所分離を試す。未修正、穴埋め、修正後の比較を保存し、編集範囲の外とignoreをバイト値で保持し、各面の連続性と局所の二面間接続だけが解けることを確認する。曖昧な場合は削除を確定せず、そこで停止する。成功時の成果物は元TIFFのハッシュ、限定した差分、再適用手順、前後のCT重ね合わせ、学習形式で読み込める修正候補。CPUで既存のNumPy、SciPy、tifffileを使える。候補自体の実CT確認・別の人による判定・学習での効果は今後の検証。

**受賞との距離。** 正しい修正物ができれば公開監査への追加であり、公式が挙げる学習ラベル品質の改善に当たる。1箇所は成立性の試験で、学習上の優位性・利用実績・修正の正しさはここでは示していない。進捗賞は実データでの改善、導入と利用、再現性を重視し、次回締切は11月30日23:59 Pacific。主催の裁量で決まる。データREADMEが参照するライセンスではデータの再配布に書面承認を要するため、修正TIFFの外部配布可否は確認が必要。villaへのAI支援PRでは人が実データ上で取り組んだ経緯、本人によるコードレビューと有用性のコメントが必要。[進捗賞](https://scrollprize.org/prizes#progress-prizes) · [データREADME](https://scrollprize.org/data/datasets/surface-labels-README.md) · [データライセンス](https://dl.ash2txt.org/LICENSE.txt) · [CONTRIBUTING](https://github.com/ScrollPrize/villa/blob/08df18e46303cf7da9803c160217fa6ef8ea3392/CONTRIBUTING.md)

## 保留 — #2167のPHerc0139巻き順

**確認した事実。** w035欠損部でw036がw034の内側に来る事例があり、巻き順をスパイラルフィットの正解に使いたい利用者が、圧縮と誤トレースを区別できていない。issueはopen、コメント6件。#2147の監査では変位を加えた対照に失敗。別の1.129 µm CT、2.4 µm CTのrun count、3Dトレーサの対照を追加しても、密着した層は判別できなかった。報告者は信頼できる巻き順を要する下流処理から除外している。検索でこのissueまたはw036を直接直すPRは見つからなかった。[issue #2167](https://github.com/ScrollPrize/villa/issues/2167) · [3D試行の結果](https://github.com/ScrollPrize/villa/issues/2167#issuecomment-6548729110) · [報告者の最新コメント](https://github.com/ScrollPrize/villa/issues/2167#issuecomment-6567910221)

**次の試行と見立て。** X542（w036の行542・列1016付近、z 18,432）の上から入るシートが別巻きか、下で分岐するplyにつながるかを局所の連続断面で追う余地がある。1.129 µm公開CTのチャンクは2 MiB、既報のX542の部分取得は66.7 MB。既報のフル入力セットは130,729,862 B（別のメッシュ実験）。先に確実に分離しているE2の断面で経路追跡が成立するかCPUで試せる。CTに境界が見えない場合は巻きの同定を止める。シートの同一性を確かめて修正ジオメトリまたは下流で使える制約まで届けば直接貢献になるが、現在得られるCTでは結論が出ないリスクが高い。[CTとメッシュの取得手順](https://github.com/stantheman0128/vesuvius-pherc0139-gap-1129) · [公開CTメタデータ](https://vesuvius-challenge-open-data.s3.amazonaws.com/PHerc0139/volumes/20260413113053-1.129um-0.2m-59keV-masked.zarr/0/.zarray)
