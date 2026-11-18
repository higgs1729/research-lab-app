Status: resolved
担当: 研究（R182、2026-11-14）
Blocked by: 181

# 既存vc_objrefineの評価窓の配置は、反転したCT対照で変位差を生むか

## 依頼

2026-11-14 JST。181で、固定14d4e725のvc_objrefineが入力頂点Pを窓の(0,0)へ置き、Gaussian後の(r,r)を評価していると分かった。既定r3/reader_scale0.5なら評価窓中心がPから接線方向8.49voxel離れる。頂点の接線移動や、意図しない欠陥と確定したわけではない。実CTの紙面をそのまま補正せず、完全支持の人工CTで、この配置が返る法線方向変位に実際に効くかを一件だけ調べる。

181のlead-proposed-control.jsonを採用。64³ uint8・16³チャンクを全て保存した3つのZarr L0を作る。中心P=(32,32,32)、+Zの有効な中心法線を持つ小さい平坦tifxyz格子を入力する。Aは z>=38+0.5(x−32) で255、他0。Bは z>=38−0.5(x−32) で255、他0。Cは z>=38 で255、他0。yには依存しない。中心法線上のA/B入力列は一致し、Pを中心に対称なGaussianであれば接線反転のA/Bは各深さで同じぼかし値になる、という性質を比較軸とする。格子サイズは中心の既定bicubic法線が有効になる最小の十分な大きさを選び、実際の法線符号・採取座標・全支持を確認して凍結する。

製品パラメータはscale_group0、reader_scale0.5、start−2/stop16/step1、既存low118/255・high165/255、border_off0、cache_mb32、overwrite=false、CPUに固定。実行は A r0、B r0、C r3、A r3、B r3 の計5回。それぞれ別の出力先へ1回ずつ。主判定は中心の同一頂点の符号付き法線変位で、全頂点数・無効点・tangent方向の変化も記録する。r0 pairとflatで入力/法線/積算が成立した後にr3 pairを比較する。対照不成立や製品失敗時は後続を止め、条件を変えず親へ返す。モデル、実CT、未知文字、欠損chunk、全0+border_offの追加ケースは対象外。元点を窓中心へ直す製品パッチもまだ加えない。

未構築のvc_objrefineは、保存R160の固定ソース・依存・既存ライブラリから、新しいC/ext4作業先へ用意する。まずCMakeが生成済みの同targetのcompile/link定義と共有ライブラリを再利用し、必要なtargetソースだけを新出力へ構築できるか確認する。既存の構築先・登録済みソース/バイナリは変更しない。正確な生成フラグ・link先・Git blob/SHA・使ったライブラリSHAを保存し、単独手書きの代替アルゴリズムに置き換えない。正確に借りられなければ、新規CMake全体再構築へ進む前に必要性と見積もりを親へ返す。181の標準新規build上限は代替案であり、自動で全依存を再構築する指示ではない。

初期構築上限はCPU1/AS4GiB、600秒、C/ext4作業1GiB・C空き10GiB。D読取のみ、通信分離、数値/OpenMP1thread、core0。新しい依存・重み・ソースの取得、CUDA/GPU、有料計算、外部公開/連絡なし。fixtureはCへ作り60秒・64MiB以内、製品各60秒、全5回計300秒以内。少なくとも中心で使うL0補間角がすべて保存され、fillに置き換わらないことを先に確認する。書き込み先は既存データから分離し、root用の実CLI/座標/元出力を残す。

保存先 experiments/vesuvius/discovery/20261114-refinement-window-control01/。結果は移動量の差と位置契約の範囲に限定し、実際の文字の改善や紙面の正解と混同しない。研究票へ結果、実条件、資源を追記し、独立照合用の原票とmanifest・lab候補を保存する。rootが別に中心頂点とraw CT/式を確認する。追加クラウド費0、サブ委任なし、lab登録は親。

今回は gpt-6.1-sol / xhigh。既存CMake構築物を変更せず別CLIへ正確に再利用する経路と、座標を保証した新しい人工対照を初めて作るため。181完了後の逐次実行。

## 結論

2026-11-14 JST [一次] 固定 `vc_objrefine` の人工CT対照5回を完了。中心頂点の法線変位はA r0、B r0、一様平面C r3で同じ +5.999938965 voxel。反転対のA r3は +9.034816742、B r3は +3.034877777 で、A−Bは +5.999938965 voxel。各出力25頂点のうち16頂点が法線方向に移動し、9頂点はXYZ不変。無効0、接線変位0。人工CTでは、R181がソースで確認した評価窓の配置が返る法線変位に影響した。

[一次] A/Bの頂点直上の強度列は一致。実tifxyzの中心+Z法線、接線+X/+Y、OpenCVのGaussian 7係数 [2,7,14,18,14,7,2]/64、3体の全64キーと必要な補間角6,480点を事前照合した。[推論] 対称配置ならA/Bの各深さのぼかし列は一致し、現行配置の式による事前値は製品出力と最大1.22×10⁻⁶ voxel差。評価窓の設計意図や実CTの紙面位置、判読効果は未評価。

[一次] R160の生成済みvc_objrefineのフラグ、PCH指定、ライブラリ順序を再利用し、固定製品cppとCMake生成moc TUだけを別ext4作業先で構築した。借用core/readerのSHAはR160一致。構築計17.034秒、最大RSS1.410 GB。fixture 0.827秒、製品5回計0.288秒。ネット取得・製品パッチ・追加クラウド費0。

[一次・主担当別照合] 生CT全786,432値と192キー、全出力の接線250値を独立確認した。事前分数計算と実TIFFの5中心変位は最大1.211×10⁻⁶ voxel差。追加製品起動0。[別照合](../experiments/vesuvius/discovery/20261114-refinement-window-control01/lead-verified.json)

## 取得の経路

構築前の環境表示検査と構築後の依存票収集の停止を原票に保持し、実構築は1回。初回fixtureは `/mnt/c` のtifxyz原子的公開で EINVAL、製品0回。固定座標・値・条件・ELFを保持し、WSL ext4に入出力して成功、Cへの証拠コピーをSHA照合した。成功後の製品再実行は0回。

- [結果と再利用経路](../experiments/vesuvius/discovery/20261114-refinement-window-control01/README.md)
- [実行条件・支持と事前計算](../experiments/vesuvius/discovery/20261114-refinement-window-control01/run02/input-contract.json) · [製品の全頂点比較](../experiments/vesuvius/discovery/20261114-refinement-window-control01/run02/comparison.json)
- [ハッシュ目録](../experiments/vesuvius/discovery/20261114-refinement-window-control01/manifest.json) · [lab登録候補](../experiments/vesuvius/discovery/20261114-refinement-window-control01/lab-record.json)
