# m7紙面予測への局所snapを既存面に適用する前の計画

PHerc0343の既知面に対する再snapが既存の字画と紙層を崩さないかを先に確認する。通過時に限り、PHerc0191の固定三面をR214の同じ9地点・18元CT断面で補正前後を比較する。一つの固定条件を段階実施する試験で、215ではソース、予測メタ、オブジェクトヘッダ、資産を確かめた。 [研究票](../../../../research/215-predicted-sheet-snap-feasibility.md) · [次試験計画](next-plan.json)

## 受賞工程の位置合わせ

- PHerc0343。公開e8370f1fの`w047/w048`は、m7距離場・Lasagna法線・軌跡でspiral fitし、m7 L0へのsnap、Lasagna平坦化を済ませた。公開concatはその二巻きを接合し、局所の2Dパラメータを移す。今回使うR173の既知concatへの再適用は、すでに良好な入力の保持を調べる対照。未補正からの回復の実証や、受賞工程全体の再現は含まない。 [受賞者のmesh原文](originals/343-mesh-readme.md) · [既知入力](../20261114-pherc0343-ct-readable01/preflight.md)
- コードでは有効な頂点ごとに、接線格子差分の外積で法線Nを求める。P＋dNの±15 voxelを整数最近接で採り、`m7>0`の連続runのうち中心が0に最も近いものを選ぶ（同距離は配列で先のrun）。`[1,2,1]`で平滑化したプロファイルの放物線で中心を小修正。変位は法線×1スカラーで、接線を直接動かさない。5×5中央値から6 voxel超離れたraw変位を除外し、近傍からの正規化Gaussian補完と最終Gaussian（σ=1 grid cell）を使い、±15へclipする。direct hitなしでも近傍が支持すれば移動する。`--z0/--z1`はparseのみ。各巻きの処理は独立し、同じラミナへの重複や層飛びは幾何と元CTで別検証が必要。 [固定snap実装](originals/343-snap_meshes.py) · [親の読解](lead-source-reading.json)
- PHerc0306Bの発見工程は、同じ0343ソースをm7 L0で呼び、別段でLasagnaを実行。最終提出の右端touch-upは、GrowPatchに対して二つの独立fitとm7トラッカーが4 voxel内で一致し元面が外れる局所を対象にする。今回は独立fit二本を持たないので最終touch-upを借りず、前段の同じsnapだけを試験対象とする。 [発見lane](originals/306b-lane_box.sh) · [最終touch-up](originals/306b-touchup.py) · [採用条件原文](../20261114-winning-method-gap01/originals/306b-surface-decision.json)
- R185はCTの強度から順序付きopacityの深さを計算した。今回のm7法は公開の紙面予測runを対象にする。両方とも面を移動させるため、R185で失った字画の連続性を今回の安全対照で確認する。 [R185固定比較](../20261114-known-text-refinement-pilot01/README.md)

## 公式予測の入手性

両巻の公式m7予測は同じ再構成IDを含む `surface-20260413222639-surface-m7-L0-th0.2.zarr`。ZYX、L0変換scale `[1,1,1]`、CTとshapeが一致。Zarr v2、非符号8-bitのC order、192³、`/`区切り、fill0、Blosc zstd clevel1 shuffle1。元CTの128³とアドレスを分ける。公式公開値の正しさは未知。取得時は同じヘッダ・実長・ETagを照合し、全必要キーを揃えたうえで復号して、欠けたキーをライブラリの暗黙のゼロとして使用することを避ける。 [0191公式カタログ](https://scrollprize.org/data_browser/PHerc0191) · [0343公式カタログ](https://scrollprize.org/data_browser/PHerc0343) · [保存メタと親照合](lead-metadata-check.json)

| 入力 | L0 shape ZYX | 必要m7キーのHEAD 200 | 圧縮本文の合計（Content-Lengthのみ） |
|---|---|---:|---:|
| PHerc0343 `20250521140437`、8.64 µm | 17998×8595×8595 | 62 / 62 | 27,235,944 B |
| PHerc0191 `20250821151635`、9.362 µm | 18977×8387×8387 | 121 / 121 | 71,124,890 B |

上流既定の5×5中央値と二回のGaussianはraw変位に2+4+4、法線差分込みで元XYZに11 grid cellsの依存幅。既知384²の描画必要節点を含むcoreでは11節点のhaloを付け、描画用の全面コピーへcoreだけ戻す。0191はR214の固定交点セル周辺に同じhaloを付ける。両者の読取キーを元meshから算定し、親の別実装と全件一致した。Pythonの既存R133依存でZarr3.1.5、NumCodecsにzstdの存在、SciPy1.18.1、TIFFを読めることを確認。WindowsではPOSIXのfork poolを同じchunk関数の逐次呼出しに替える。実予測チャンクの復号とsnapは次試験で確認する。 [支持範囲](support-estimate.json) · [HEAD原票](prediction-key-heads.json) · [親の支持照合](lead-support-check.json) · [局所依存の確認](lead-locality-reading.json) · [SciPyのGaussian仕様](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html)

## 一件の実行計画

1. **PHerc0343で保持確認。** R185と同じ `[1344,1024,384,384]`、主256²、元mesh・snap後を同一既存製品で描画する。保存されたR185元入力の再現を先に確認。dense-native reverse、中央17枚24→8、128²/stride64/25枚、patchごとの公式robust MAD、Hann、同じ表示0–255。同じ入力なら保存元予測を再利用し、許容した1 DN以内の描画差の場合のみ既存条件で基準を1回再生成。親・担当が元CTと箱9/10に重なる字画部分を別々に確認し、新たな合体・散乱・字画の途切れ・層飛びを判定する。大移動後に紙層への帰属が新たに不明となった場合も止める。元から同程度に曖昧な箇所はその限界を記録。主領域のrとMAEは診断値で、既知の改善は必須にしない。 [R185の比較契約](../20261114-known-text-refinement-pilot01/README.md) · [固定条件](next-plan.json)
2. **通過時にPHerc0191の同9地点。** 同じ上流既定のsnapを固定局所coreに一度適用する。元CT画像はR214の18枚のグリッド・DNを保持し、重ねる交点のみを新旧で比較。隣接面の順序、同じ層への収束、位置の飛び、変位の直接/補完由来と面の折れを調べる。固定断面から外れた点は未判定。必要中心3、左右各2の紙層支持を再確認し、区別できない面を合算しない。未知側のink推論は0。通過は局所の判定で、その時点では広域描画を始めない。 [R214の元CTと所見](../20261114-pherc0191-bounded-crop-gate01/README.md) · [固定条件](next-plan.json)

後続一件でm7新規は最大128 MiB。元CTは既知の不足最大16キー32 MiB、未知の追加0。手元CPU1/4 GiB、stage通信各300秒、合計計算上限600秒、全体1,500秒、C作業2 GiB。dense既知は最大2回50パッチ、各120秒。必要な作業は既存CPUで可能と見積もり、GPUや外部支出の予算を設けない。今回の記録済み一次本文12件44,670 B（5.303秒）、実寸を確かめたHEAD 183件（16.555秒、本文0）。事前の小メタ確認やweb表示の転送時間・ヘッダ転送量は未計測。予測・CTのボクセル本文、ビルド、推論、GPU、費用、外部公開0。 [取得原票](source-acquisition.json) · [キーHEAD](prediction-key-heads.json)
