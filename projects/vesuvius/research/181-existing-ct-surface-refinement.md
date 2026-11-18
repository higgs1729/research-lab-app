Status: resolved
担当: 研究（R181担当、2026-11-14）
Blocked by: 180

# 既存のCTによる面補正を、紙面の曖昧さを減らす次の小試験に使えるか

## 依頼

2026-11-14 JST。180までの複数の紙面診断では、元CTと生成画像の座標一致を確認しても、モデルの強い反応を一枚の物理紙面へ対応付けられない例が続いた。180のPHerc0343では3地点のうち2地点でmeshが暗帯/縁を通るが、暗帯の意味や正しい補正量は未判定。既存面が誤っていると決め付けず、文字の見た目に合わせて深さを探索することも避ける。既知文字のある173/175を対照にして、CT構造から面位置を評価/補正する小実験を作れるか確認する。

軽い調達確認で、固定villa14d4e725の volume-cartographer/apps/src/ObjAlphaCompRefinement.cpp に、CTの法線方向の積算からoffsetを決め、tifxyzの各点を動かす既存機能が見つかった。同じ保存木には vc_grow_seg_from_seed.cpp、vc/lasagna/LineOptimizer.hpp と grow_patch_point_corrections.md もある。最初の候補を中心に1〜3機能まで、何を根拠に面を選ぶのか、異なる紙面や空隙へ移る可能性をどこまで扱うのか、今回の保存入力で試す条件を一次コード・公式資料から絞る。独自の補正アルゴリズムを先に作らない。全面的なOSS一覧や論文調査は不要。

固定ソースの既存Linux展開先は /home/tomoy/bundle-fixed-main-run01-pywin6ml/villa（C:/WSL/Ubuntu内）。既登録の三件パッチ入りだが対象機能はまだ改変していない。Dは読取だけ、原票と元ソースは変更しない。WSLにrgは無かったためfind/grepへ切替可能。一次原文と固定版は保存160の索引へ対応させる。必要なら公式の小さい資料を補足できるが、新規本文合計8MiBまで。重み・CT・surface predictionの本文取得、ビルド、モデル推論、外部公開/連絡、有料計算はこの選定では行わない。

成果は既存機能の正確な入力/出力/目的関数と限界、再利用する入口、次の一実験案または採らない理由。次案には173/175の既知文字を対照に含め、180の未確定応答に何を加えて判定できるか、入力・補正/比較条件・必要な支持・概算資源・停止条件を事前に固定できる程度にする。CT強度の極大や処理成功を正しい紙面の正解に置き換えない。既知文字を壊さず物理位置の根拠が増えるかを見られるか、既存コードの単純な移動が今回の曖昧さを解かないかも明示する。既存機能が適切でなければ無理に実行案を作らず返す。

保存先 experiments/vesuvius/discovery/20261114-surface-refinement-selection01/。研究票に結論と取得経路を残し、親が重要なコード/数式/入力位置を別確認できる原票とmanifest・lab候補を作成。追加クラウド費0、サブ委任なし、lab登録は親。今回はgpt-6.1-sol / xhigh。未確定なCT構造と既存機能の選択基準を結び、既知対照付きの新しい試験を設計するため。180完了後の逐次実行。

## 結論

2026-11-14 JST。**R180のPHerc0343三地点に既存機能で自動補正を適用する案は見送り。** 固定villa `14d4e725` の実ファイルをR160固定索引に照合した。対象14ファイルのSHA-256、Git blob、長さはすべて一致。保存R160の標準ビルドには `vc_objrefine` の実行体が含まれていない。

[一次・固定実装] `vc_objrefine` は元頂点の法線に沿ってCTの強度を前から不透明度として積算し、加重平均深さに既定+1 voxelを加えて頂点を個別に移す。評価窓は元頂点の接平面で (0,0) から始まり、既定では(r,r)の評価位置が接線二軸へ各6 voxel移る。合成で複数帯を隔離する制約はなく、ローカル疎CTの欠損キーはfill=0として評価に入り得る。全層の不透明度が0でも既定+1は残る。評価窓の位置が意図した補正契約かは未確認。主担当も座標と積算式を別読解した。

R173/R175の既知字画は形状保持の比較に使えるが、CT内の真の紙面深さは未注記。R180の複数帯の帰属は未判定のまま。人の3D点列を入力する `vc_grow_seg_from_seed --correct` と、法線場に沿う注記線の `LineOptimizer` も、この入力から同一紙面を選ぶ根拠は与えない。追加確認を行う場合は、同じ既存コードで一様平面と接線反転した傾斜帯、r=0/r=3、疎CTのfillを小さな既知fixtureで対照するところまで。R160の固定依存と標準CMake targetを別作業先で使う見積もりを添えた。現時点で未知側の頂点は移動していない。

[実施・費用] 固定版の読取りのみ。ネットワーク取得0 B、製品実行・ビルド・推論0、追加クラウド費0。実機構の変位とCT支持は未測定。

- [結果・CLIと根拠行・支持と停止条件](../experiments/vesuvius/discovery/20261114-surface-refinement-selection01/README.md)
- [固定原文抜粋・SHA](../experiments/vesuvius/discovery/20261114-surface-refinement-selection01/source-evidence.json)
- [主担当別読解](../experiments/vesuvius/discovery/20261114-surface-refinement-selection01/lead-code-review.json)
- [ハッシュ目録](../experiments/vesuvius/discovery/20261114-surface-refinement-selection01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-surface-refinement-selection01/lab-record.json)
