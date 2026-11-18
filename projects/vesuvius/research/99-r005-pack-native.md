# R005：flatboiの成分配置をCLIに組み込み、実データ二面で照合

2026年11月12日 JST。`flatboi --pack-components` を追加する一ファイルのパッチを作った。全解像度SLIMを5反復した二つのPHerc0814実入力で、別成分間の描画拒否と別成分をまたぐ有効格子辺がともに0になった。第二面のnative配置後UV・描画トレース・全XYZは、独立検証済みの保存UVにPythonで配置を適用した結果に一致した。第二面の同成分内拒否356件と自面標本のない13,100 quadは残る。[配布パッチ](../experiments/vesuvius/r005/20261112-pack-native01/pack-components.patch) · [PR下書き](../experiments/vesuvius/r005/20261112-pack-native01/PR_DRAFT.md)

## 実装

配布差分の起点は固定base `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5` のGit blob `2dcf5981008e6b68b8c29ef7e083fc769f40e163`。04:15 UTCに確認されたmain `f0e441016900cb946bc3861025eca3a7cc2aae19` の同ファイルと同じ。Gitから抽出したLF原本に `git apply --check --whitespace=error` と `git apply` を隔離ディレクトリで実行し、適用後の全バイトをビルドしたソースと照合した。R003のstride補正はalpaltianの[既存issue #2500](https://github.com/ScrollPrize/villa/issues/2500)に由来し、この差分の外にある。配置の再現条件と上流の限定検索は[前回の主報告](97-r005-full-resolution-controls.md)に記録した。[未変更原本](../experiments/vesuvius/r005/20261112-pack-native01/flatboi-base.cpp) · [変更ソース](../experiments/vesuvius/r005/20261112-pack-native01/flatboi.cpp)

成分抽出は既存依存のlibigl `vertex_components(F, labels)` を借りた。旧実験の独自union-findも候補にあったが、libiglでfineメッシュの頂点接続と最小頂点順の成分IDが得られる。格子点マスクの連結は、描画元の全四隅有効quadの三角形接続をそのまま表さないため対象から外した。[固定依存の実装](https://github.com/libigl/libigl/blob/ae8f959ea26d7059abad4c698aba8d6b7c3205e8/include/igl/vertex_components.cpp)

配置はSLIMと既存の細UVへの転写・有効面選択の後、ラスタライザーに渡す直前に行う。元fine成分全体の頂点数の降順で、同数なら最小元頂点が早い順。既存フィルタを通過し全コーナーが有限の面で外接範囲を求め、横に2ソースセル分の間隔で並べて各成分の最小yを0に揃える。描画側がソースscaleを使う場合はX軸の `2.0 / scale[0]`、その他はラスタライザーのUV単位に合わせて2を使う。実測のscaleは両軸 `0.05000000074505806`。シフトと加算をdoubleで行い、最後にfloat32へ戻す。各成分の有限・有効なUVを同じベクトルで移動する。対象となる成分が0または1の場合はUVが変わらない。

フラグは既定off。CLIの二つのモードのhelpに現れ、stored-surfaceの保存parametersにはboolean `pack_components` を含める。ストアへの保存は実行せず、二面ともローカルtifxyz入出力を通した。

```sh
flatboi input_tifxyz --output=packed --keep=100 5 --pack-components
```

## 全解像度の二面

第一面は `20250929040153-auto_grown_20250929040153260` の41,349頂点・78,624面・39,312 quad・5成分。第二面は `20250928235953-auto_grown_20250928235953722` の249,944頂点・478,224面・239,112 quad・9成分。どちらも `--keep=100 5`、symmetric_dirichlet、tol0、inpaint指定なし。入力TIFFとmetaのハッシュをmanifestに照合し、観測した元頂点順、元面とXYZを保存入力および元TIFFと照合した。[第一面の入力manifest](../experiments/vesuvius/r003/20261111-input01/manifest.json) · [第二面の入力manifest](../experiments/vesuvius/r005/20261112-input02/manifest.json)

| 指標 | 第一面 未配置 | 第一面 配置 | 第二面 未配置 | 第二面 配置 |
| --- | ---: | ---: | ---: | ---: |
| 出力格子 y×x | 172×553 | 172×680 | 252×2637 | 252×3027 |
| 有効出力点 | 40,944 | 41,149 | 254,263 | 254,668 |
| 全描画拒否 | 190 | 1 | 757 | 356 |
| 別成分間の拒否 | 189 | 0 | 399 | 0 |
| 別成分をまたぐ有効格子辺 | 106 | 0 | 284 | 0 |
| 自面標本0の元quad | 2,855 | 2,624 | 13,424 | 13,100 |
| 元quad中心の同成分距離 >20 voxel | 167 | 0 | 485 | 202 |
| 同 >40 voxel | 87 | 0 | 205 | 82 |
| 正規化SDの3D面積加重平均 | 1.00193546111065 | 1.00193546112089 | 1.00145941973236 | 1.00145942224834 |

第二面はフラグonのnative計測を一回。配置前のfine float32 UVは全点が凍結済みの未配置出力にビット一致し、粗SLIMの全UVとエネルギーファイルも一致。配置後の全UVはPythonの保存配列とビット一致。描画トレース全フィールドと3枚のTIFFファイルのハッシュは、Python配置を既存ラスタライザーで描画した結果に一致した。全元quadの同成分距離も凍結配列に照合した。20以内への回復288、新規20超5、共通197。配置前後とも無効・縮退・反転は0。[新nativeの状態](../experiments/vesuvius/r005/20261112-pack-native01/second-trace-on01/state.json) · [凍結した比較の独立検証](98-r005-full-resolution-verification.md) · [成分別の描画比較図](../experiments/vesuvius/r005/20261112-pack-native01/second-component-ownership.png)

第一面の既定offは計測版とpristineの既存バイナリを同じ5反復で比較し、3枚のTIFFがファイル単位で一致した。フラグonでは通常版と計測版の3枚のTIFFがファイル単位で一致した。4実行のSLIMエネルギーのハッシュは同一で、計測版の配置前UVもon/offで同一。配置後の全UVを既存Python `pack` と照合し、float32のビット一致を確認した。20以内への回復167、新規20超0。配置前後とも無効・縮退・反転は0。[計測off](../experiments/vesuvius/r005/20261112-pack-native01/first-trace-off01/state.json) · [pristine off](../experiments/vesuvius/r005/20261112-pack-native01/first-base-off01/state.json) · [計測on](../experiments/vesuvius/r005/20261112-pack-native01/first-trace-on01/state.json) · [通常on](../experiments/vesuvius/r005/20261112-pack-native01/first-product-on01/state.json)

第二面に残った356件は、凍結対照で元頂点を共有しない同成分面が連続UV上で正の面積をもって交差した記録に一致する。距離指標は標本密度・格子の位相にも依存し、元格子対照の20超は第一面49、第二面11。評価はこの入力と条件で観測された幾何と標本に限る。全域の内部重複探索、繊維の連続性、判読性は未評価。[元格子対照](95-r005-grid-control.md) · [全数値と配置量](../experiments/vesuvius/r005/20261112-pack-native01/analysis01/result.json)

## UV無効と単一の描画成分

第一面の `--keep=1.5 5 --pack-components` はstride8で成功。元41,349頂点中103頂点がUV無効で、既存フィルタの除外225面を保った。配置前の有効UVから期待値を再計算すると配置後の全有効UVとビット一致。元5成分に有効面があり、そのうち4成分に出力標本があった。155×617格子・23,003点・同成分拒否11,522。既存の転写や縮退への追加修復はこの試験の範囲外。[低keepの状態](../experiments/vesuvius/r005/20261112-pack-native01/first-low-trace-on01/state.json)

製品関数をそのまま抽出した補助検査では、第一面の実際の配置前UVとfine面を使った。有効面が0と1成分だけのケースで全UVのビット一致を確認。2成分のケースでは35,435頂点と289頂点を移動し、残りの成分にはUV有効な孤立点を一つ残しても変化せず、描画する二成分の隙間は2ソースセルだった。初回の補助検査は配置後UVを読んでおり、両成分が必ず移動するという強過ぎる条件で失敗した。元の失敗ログを保存し、配置前UV・実測の間隔・対象外UVの比較に訂正した二回目が成功した。[初回の記録](../experiments/vesuvius/r005/20261112-pack-native01/edge-checks01/state.json) · [訂正後の結果](../experiments/vesuvius/r005/20261112-pack-native01/edge-checks02/checks.log)

## 実行資源と保存物

WSL Ubuntu 24.04 / GCC 13.3 / O0。既存のCMake生成compile/link引数を複製し、通常版には既存ラスタライザー、計測版には既存 `SurfaceMeshing-trace.o` を使用。UV観測は既存診断ブロックを再利用し、配置前UVと入力XYZを追加した。配布差分に観測コードは含まれない。ビルド時と凍結時のハッシュで、既存作業木の対象ソース、build設定、既存バイナリ、リンク先の既存ローカルライブラリを確認した。[通常ビルド](../experiments/vesuvius/r005/20261112-pack-native01/build-product01/state.json) · [計測ビルド](../experiments/vesuvius/r005/20261112-pack-native01/build-trace01/state.json) · [観測専用差分](../experiments/vesuvius/r005/20261112-pack-native01/diagnostic-only.patch)

全ジョブを逐次、CPU1・OMP/BLAS/PaStiX各1スレッドで実施。WSL各プロセスはAS上限4 GiB・300秒、Windowsの評価は観測RSS4 GiB・300秒。通常版のcompile/linkは27.93秒・7.75秒、計測版は24.92秒・7.23秒。第二面native 115.50秒、最大子RSS1,029,111,808 bytes。第一面keep100の4実行は25.11〜25.81秒・最大219,754,496 bytes、keep1.5は7.75秒・110,202,880 bytes。数値照合は5.83秒・観測RSS898,854,912 bytes。共用ホスト上の単回測定で、速度比較の根拠には用いない。新規入力取得、GPU、有料計算は0。公開、PR投稿、応募は行っていない。[全実行のコマンドと資源](../experiments/vesuvius/r005/20261112-pack-native01/resources.json) · [凍結manifest](../experiments/vesuvius/r005/20261112-pack-native01/artifact-manifest.json)

実データ実行は自動計測。人間による実利用、コードレビュー、本人が書く利用理由の欄は下書きで未チェック。独立検証の対象は今回のnative差分と新規保存物。前回の第二面凍結対照には独立検証済みの記録がある。[上流のCONTRIBUTING](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/CONTRIBUTING.md) · [上流のPR書式](https://github.com/ScrollPrize/villa/blob/f0e441016900cb946bc3861025eca3a7cc2aae19/.github/pull_request_template.md)
