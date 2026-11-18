Status: resolved
担当: 研究（R175、2026-11-14）
Blocked by: 174

# 同じCTでパッチ開始位置だけを公開側へ揃えると既知字画はどう変わるか

## 依頼

2026-11-14 JST。173は元CTの位置をほぼ再現でき、dense-native逆順で既知の輪の部分形状が出たが、seed42は公開出力との対応が弱い。174では同じ入力に対する正規化の違いがfloat丸めの範囲と判明した。次はパッチグリッドの位相だけを変え、同じCT値に対する出力変化を比較する。未知領域・深さ・閾値の探索ではない。

173の保存33×512²入力（atlas XY開始1320,980）だけを使う。公開の全面グリッドのstride64へ揃う固定crop XYWH [1344,1024,384,384] を取り出す。173内のlocal XYWHは[24,44,384,384]。中央17層と方向は逆順24→8に固定し、既存seed42とdense-nativeを各1回、合計2推論だけ行う。モデル・正規化・batch1/CPU float32/Hann/128patch/stride64は173と同じ、入力は元CT値のそのままの部分配列。モデルごと25パッチのはずで、起動前に契約を保存する。

主評価領域は端の重みや切り出し境界の影響を避ける共通内部 atlas XYWH [1408,1088,256,256]、新cropのlocal[64,64,256,256]。この内部で、全面stride64の全被覆パッチが今回の384²へ収まることを位置一覧とHann支持から確認する。旧173出力の同位置も内部にある。共通内部を使う理由と残る限界を説明する。公開atlasの実生成版/CT法線/実行環境差は消えないため、予測の完全一致や予測精度を合格条件にしない。

比較は旧173・今回・保存公開単独reverseの三者で、各モデルの同じXY画素を見る。未加工固定0–255の全384²表示を保存し、256²内部の出力差・公開との相関/平均差を記述的に集計。相関改善を読める文字の増加と同一視せず、輪や隣の線が以前より追えるかは親も原寸で判定する。結果に応じてさらに別の位相を試すことはしない。

既存のR133公式ランナーと173入力/出力保存を借り、新コードは切り出し・起動契約・比較に必要な部分だけ。新CT・コード/重み取得・描画・依存追加・ビルド・GPU・課金0。CPU1/commit4GiB/threads1、各推論120秒、通信拒否。作業128MiB、C空き10GiB、D読み取りのみ。入力と各出力は experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/ に保存し、登録済み173/174には書かない。

親へ判断文前に比較図のパスを渡す。研究票へ結果/限界/資源を追記しlab候補を用意する。標準モデルロードや変換の検証は再利用し、今回変えた部分配列・パッチ位相・共通内部へ検証を絞る。外部投稿/公開/サブ委任なし、登録は親。今回は gpt-6.1-sol / high を選択。既存の実行手順を使い、一意に固定した位相と同一CTで比較する限定実験のため。174完了後、逐次実行。

## 結論

[一次・実行、2026-11-14 JST] 同じ元CT値でパッチ格子を公開側のstride64原点へ揃えると、共通内部256²で公開単独reverseに近づいた。seed42の画素相関は0.07552から0.94810、MAEは37.89から7.44 DN。dense-nativeは相関0.87506から0.98970、MAEは13.90から4.08 DN。目視ではseed42の広い曲線状の並びが公開に近づき、dense-nativeでは以前も見えた囲まれた暗部の輪郭と隣の明部の位置が公開に近づいた。この図で新たに判読できる文字列は確認できなかった。[共通内部の原寸図](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/comparison-interior-256.png) · [384²の原寸図](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/comparison-384.png)

## 根拠・詳細

- [一次] 研究173の33×512² Zarrを入力契約の16チャンクSHAと照合し、ローカルXYWH `[24,44,384,384]`、atlas XYWH `[1344,1024,384,384]` を切り出した。新Zarrを読み戻し、全4,866,048値が元の部分配列と一致した。中央17層はreverse `24→8`。旧パッチ位相はatlas原点からmod64で `(40,20)`、新位相は `(0,0)`。新Zarrの物理XY平行移動は元の画素間隔と固定atlas原点から設定した。[入力契約](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/input-contract.json)
- [一次] 公開画像の6048×2304と保存Ink Lensの端寄せを含むパッチ開始規則を使った。主評価のatlas XYWH `[1408,1088,256,256]` に128²の支持が届く公開全面パッチは、X開始1344〜1600、Y開始1024〜1280を各64刻みとする25パッチ。すべて新384²内に収まる。Hannは0.001の下限があるためパッチ端も支持に数えた。保存重みは独立計算と最大3.04×10⁻⁷差で、内部は全画素約0.97572〜1.00300。旧173でも同じ評価域はcropの端から離れていて重みが正。公開全面と比べるための支持の確認で、公開実生成時のマスクや各パッチの処理順は未確認。[パッチ位置一覧](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/patch-plan.json) · [重み照合](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/comparison.json)
- [一次] 既存seed42・dense-native各1回で25パッチ、reverse 24→8を記録。173と各checkpoint・公式ソースSHA・入力出力以外のCLI引数・一時ディレクトリ以外の環境が一致。CPU float32、robust-MAD、128²、stride64、Hann、batch1の条件を保った。既存173の観測・出力保存経路を呼び、連続スコアと確率和・重みを保存した。PNG/TIFFおよび比較図のパネルは保存uint8と全画素で一致した。[seed42実行条件](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/seed42-reverse/execution.json) · [dense-native実行条件](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/dense-reverse/execution.json)

| 共通内部65,536画素 | seed42 | dense-native |
|---|---:|---:|
| 公開との相関 旧 → 新 | 0.07552 → 0.94810 | 0.87506 → 0.98970 |
| 公開とのMAE 旧 → 新（DN） | 37.8853 → 7.4413 | 13.9046 → 4.0781 |
| 公開との差の符号付き平均 旧 → 新（DN） | +8.2035 → +3.1250 | −1.2808 → +0.6663 |
| 新と旧のMAE（DN） | 39.9288 | 12.7665 |

[一次・目視] seed42の旧図では左寄りに孤立していた明部が、整列後は公開図に見える上から中央への曲線状の並びに近づいた。閉じた輪や隣の独立した線の連なりは明瞭には追えなかった。dense-nativeは旧図にも囲まれた暗部があり、整列後はその輪郭と隣の明部が公開図により近い。主担当は原寸二図を別に見て、形状の近づき方と判読の範囲について一致した。定量値は公開uint8への近さであり、字画の正解ラベルや読める文字数は計っていない。[原寸図](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/comparison-384.png) · [比較原票](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/comparison.json)

## 実行条件と限界

Windows既存1CPU・Job commit 4 GiB・数値1スレッド・通信拒否ランナー、各120秒。seed42 10.835秒、最大RSS745,017,344 B。dense-native 10.570秒、最大RSS849,170,432 B。両実行は逐次。新規取得・CT描画・依存導入・ビルド・GPU・追加費用はゼロ。保存済み元CTに対して、評価領域にかかるパッチの切り出し位置と重みが変わったときの感度を観測した。公開atlas実生成版、CT法線、モデル実行環境や集約の差は残る。結果は固定の既知領域・逆深さ順に限る。[実行入口](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/README.md) · [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/lab-record.json)

## 主担当の別照合

[一次] 主担当は新CTの全4,866,048値を173の部分配列に照合した。公開全面6048×2304の開始点を別に列挙し、評価内部を支える25パッチが今回の位置と一致することを確認。各モデルの公開との画素相関とMAEも別式で再計算して一致した。[別照合コード](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/lead_check.py) · [別照合原票](../experiments/vesuvius/discovery/20261114-pherc0343-patch-phase01/lead-check.json)
