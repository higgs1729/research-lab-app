# R181 固定ソースのCT面補正を評価

2026-11-14 JST。**PHerc0343のR180三地点に自動面補正を適用する案は見送り。** `vc_objrefine` は、法線近傍のCT強度を所定の順に不透明度へ変換して頂点を移動する。紙面の連続性、同じ紙面の識別、空隙からの復帰、支持不足時の棄却に使える判定を出さない。R180のように複数の明暗帯がある場所では、この移動で物理紙面の帰属は決まらない。

## 固定版と入力契約

R160で保存した固定木 `14d4e725df8b569e6fc8ceb3c04d130f705c1565` の実体14ファイルを読んだ。実体のSHA-256、Git blob SHA-1、長さはR160の固定索引とすべて一致。番号付き範囲とハッシュは [source-evidence.json](source-evidence.json)、主担当による別読解は [lead-code-review.json](lead-code-review.json) にある。

- `vc_objrefine <zarr-volume> <src-surface> <out-surface> <json-params>` がローカル入口。既存tifxyzを読み、入力格子の大きさとscaleを保持して新しいXYZを `saveEdited` で保存する。無効点と無効法線は移動対象から外れる。法線は元の `QuadSurface::pointSurface()` の格子微分から求める。通常既定はbicubicで、R173/R180のlinearサーフェス描画と法線を同一視できない。ストア版は既存IDをその場で更新できるため、別出力への計測にはファイル入口が対応する。ObjAlphaCompRefinement.cpp 323–389、435–494、QuadSurface.cpp 354–371、438–447、QuadSurface.hpp 494、grid.hpp 53–65。
- `scale_group`（別名 `scale_level`）の既定は1。保存CT L0を使う場合は0を明示する。`reader_scale` の既定0.5は接線方向のサンプル間隔2 voxelを指定する。既定深さは−2、0、…、30 voxelの17面。既定キャッシュ上限は10,000,000,000 Bで、少量の試験では `cache_mb` 等を明示する。CPUが通常経路。上流CMakeの既存target `vc_objrefine` は `vc_core` をリンクする。R160で実在した3 executableに同targetはなく、そのCMake構成のCUDAはOFF。実行には既存の別実体の確認か、新規に許可された標準targetビルドが必要。ObjAlphaCompRefinement.cpp 35–96、435–494、apps/CMakeLists.txt 59–60、CudaSampling.cpp 183–224。

## 強度から移動量への変換と支持

各有効頂点を P、元法線を N、単位接線を Bx、By、`reader_scale` を s とする。L0では各層のサンプル位置は **P + i·Bx/s + j·By/s + dₖ·N** で、i,j は0…2r。各点の既定補間は三線形。PlaneのoriginはPで、コメントも画素(0,0)をPとしている。CPU実装の `centreOf` は座標変換の数値参照点で、画素の位置式を変えない。強度を0〜255に収めて255で割り、層ごとに (2r+1)² のGaussianBlurをかけ、画素(r,r)を評価する。したがって評価位置は **P + r·Bx/s + r·By/s + dₖ·N**。既定 r=3、s=0.5では接線二軸に各6 voxel、合計約8.49 voxel（8.64 µm/voxelでは約73.3 µm）離れる。紙面の縁や折れがこの距離内にあれば、入力頂点の直上と異なる構造を積算し得る。コード上の位置は確定したが、補正用途でこの配置が意図されたかは未確認。ObjAlphaCompRefinement.cpp 157–211、PlaneSurface.cpp 69–84、115–125、189–204、grid.hpp 113–122、150–186、grid.cpp 515–522、555–580。

評価画素のぼかし値 bₖ を `aₖ = clamp((bₖ−low)/(high−low),0,1)` とする。low/highの既定は118/255と165/255。T₀=1、wₖ=Tₖaₖ、Tₖ₊₁=Tₖ−wₖ の順で積算する。最終頂点は **P + N·(Σwₖdₖ/(1−T_end+10⁻⁵) + border_off)**。これは強度に由来する順序付き加重平均で、先に出会う明帯が後の帯を抑え、複数帯の間に移動先を置く場合もある。法線の向きと走査順の依存がある。頂点ごとの独立処理で、紙面を跨がない制約や信頼度による棄却はない。全層の不透明度が0なら加重分は0で、既定 `border_off=1` は残る。ObjAlphaCompRefinement.cpp 162–213、323–357。

ローカル疎Zarrで存在しないキーは、通常のCPU読み込みでは配列のfillとして補間に入る。座標外の補間角にもfillが使われる。保存CT L0のfillは0。別経路で値がNaNのときも補正器は0に置く。これらは有効な低CT値と同じ方向に不透明度を変え、空白が増えても処理が完了し得る。R173/R180の描画・断面で確認済みのキー集合は、それぞれの固定支持に限る。既定補正の深さ上端+30、接線方向0〜12 voxelの全49点、三線形の補間角を含む新しい支持の充足は未確認。grid.cpp 289–308、353–365、389–396、sample_point.hpp 63–107、ObjAlphaCompRefinement.cpp 190–195。

## 比較した入口

| 入口 | 入力・出力 | R180への判断 |
| --- | --- | --- |
| `vc_objrefine` | 同一座標系のZarrとtifxyzからXYZ移動。法線順にCT不透明度を積算する。 | 補正量の提案を作れるが、複数の明暗帯を物理紙面へ帰属させる条件がない。 |
| `vc_grow_seg_from_seed --resume <tifxyz> --correct <points.json>` | 再開面と人が置いた3D点列、全解像度uint8 volume。局所の補正・再成長を行い面を出す。ストア面も指定可。 | 点列の先頭を信頼できる既存面上に置き、補正先の同じ紙面を追って点を指定する契約。R180ではその点列を定める独立根拠がない。 |
| VC3D `LineOptimizer` | Lasagnaの `NormalSampler`、seed・制御点・既存線を使って線を最適化する。位置・曲率・法線との整合を扱い、線を返す。 | 今ある複数のCT帯から紙面を選ぶ入口は確認できず、面の補正出力もない。 |

後二者の根拠は `vc_grow_seg_from_seed.cpp` 195–199、265–277、324–347、657–670、1514–1518、`grow_patch_point_corrections.md` 1–30、`LineOptimizer.hpp` 186–225、`LineOptimizer.cpp` 239–279、372–396、`LineAnnotationController.cpp` 1302–1315、1348–1358。

## 既知対照と次の判断境界

R173では同じatlas位置の中央CTが全262,144画素で公開値の±1 DN以内で、dense reverseの既知字画の部分形状が再現した。R175は同じCTの入力を公開stride64へ合わせ、atlas XYWH [1408,1088,256,256] で公開との一致を改善した。ここを既知形状の保持を比較する固定領域として参照できる。CT内の真の紙面深さや既知字画を載せた物理層を一点ずつ注記した対照はない。R180の三地点 [5376,736]、[5504,704]、[5824,704] は固定断面で複数帯が残ったままなので、既知側の出力形状やCTの最大強度だけで移動先を選べない。元面・法線・stride64を固定し、対応する独立な紙面追跡点が得られた段階で、補正前後の位置と既知形状の保持を同じ座標で評価できる。[R173](../../../../research/173-pherc0343-ct-readable-control.md) · [R175の入力契約](../20261114-pherc0343-patch-phase01/input-contract.json) · [R180の座標・支持](../20261114-pherc0343-edge-probes01/plan.json)

別票での小さい機構対照案は、同じ既存 `vc_objrefine` へ、格子法線に直交する一様な明るい平面と、頂点Pを基準に接線方向に反転した傾斜明帯2つを個別に入力する。両傾斜帯のP直上の深さ列を同じにする。法線と頂点位置が確定した小さい有効tifxyz格子を使い、中央の同一頂点だけを判定対象にする。L0、既定深さ列、既定閾値、`cache_mb=32`、`overwrite=false`、`border_off=0` に固定して、r=0とr=3の符号付き法線変位を比較する。Pを中心とする対称なGaussianなら反転した2入力の深さプロファイルは一致する。一様平面でrによる差がなく、反転対でr=0が一致しr=3に差が出るかが、評価窓の偏りが変位に及ぶかを判断する軸となる。欠損の対照は別コピーで、明帯を担う1キーだけを取り除いて同じ座標の変位を測る。全0支持での既定+1は `border_off=0` と既定の一対で確認できる。既定は1頂点49×17=833サンプル、補間角は最大8個/サンプル。CPU1・4 GiB・オフライン、各fixtureは最大2キー/4 MiB（128³ uint8）、fixture工程60秒・C作業64 MiBを仮の上限とする。支持全角の事前照合、法線、反転対のP直上の同一性が成立しなければ実行しない。fixtureで測れるのはコードの位置とfillによる変位まで。R180の紙面帰属には、別途、同一紙面を独立して追跡できる位置情報が要る。 主担当の具体案は64³、16³チャンク、P=(32,32,32)、+Z法線、深さ−2…16 voxelを1 voxel刻みで固定する。既定r=3では49×19=931サンプル/頂点。完全支持で接線反転対と平面の5回を先に比較する。欠損対照はこの5回には含めない。必要な法線を作れる有効格子を用意して符号を事前に確認する。[固定fixture案](lead-proposed-control.json)

CLIを用意する場合の標準入口は、C上WSL ext4の新規先にR160の固定villaと既存のPaStiX/SPM、libigl、vc_delta3dを作業コピーし、R160の実configure引数を新パスへ付け替えて使う。既存ローカルlibbacktrace参照とオフラインの実行環境を借りる。`cmake --build <new-build> --target vc_objrefine --parallel 1` で上流targetのみを指定する。依存の `vc_core` などは新規作業先で標準ビルドされる。R160実測は構成75.8秒、core等を含む4 targetのビルド653.3秒、最大子RSS 1.67 GB、作業領域サンプル最大1.60 GB。今回のtarget自体は未計測のため、候補はR160同等の構成600秒・ビルド2,400秒、CPU1、AS4 GiB、作業6 GiB、ホストC:空き10 GiB。既存依存で構成できない、資源上限超過、実リンク先が新作業先でない場合は打ち切る。製品ソースの追加変更、既登録buildの更新、依存取得は要しない見込み。 [R160の構成原票](../../bundle/20261113-fixed-main-integration01/run01/configure-process.json) · [ビルド原票](../../bundle/20261113-fixed-main-integration01/run01/build-process.json)

## 実施範囲

固定ソースと既存原票の読取りのみ。外部取得0 B、製品実行・構成・ビルド・推論0、追加クラウド費0。実ランタイムでの変位、必要キー数、実行時間は未測定。参照ソースの照合に読んだ本文は1,198,772 B。原票、主担当の別読解、研究票のハッシュを [manifest.json](manifest.json) に保存。lab登録は主担当。[登録候補](lab-record.json)
