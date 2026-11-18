Status: resolved
担当: 研究（R192担当、2026-11-14 JST）
Blocked by: 191

# PHerc0846Bの別面に、公開原寸予測から追試する字画候補を選べるか（2026-11-14）

## 依頼

発見を主目標に、GPUが他作業で使われている間も、既存の公開予測から物理位置に戻せる未読候補を一面ずつ探す。191はGPU環境の認識と入口準備までで入場120秒を超え、モデルは未実行。190/191のHecate既知対照は未完なので、今回の公開予測をそのローカル再現の代わりにしない。GPUを再度並べない。

今回の対象は固定atlas ac5ffd7098120368216948c4e06c494bf8e67178 の PHerc0846B `surfaces/PHerc0846B/kbh-PHerc0846B_2768_2813_9748` 一面。既存 `experiments/vesuvius/discovery/20261113-next-target01/ink-atlas-index.json` に唯一の公開0846B面として掲載。186の加工カードで見た別面 `3962,4983,7051` と混同しない。186はこのatlas別面の原寸をまだ見ていない。公開済みであること自体は追試対象から除外する理由にしないが、先行の判読・訓練重複・座標来歴と新たな貢献は区別する。

既存の固定README/atlas index、186保存公式Data Browser/規定を先に参照し、この面のmeta、固定ファイル木と原寸画像の条件を取得する。モデルを見た後で選び直すのを避け、中心c+0_s1のHecate、Reader V3、seed42について同じ面・両方向の計6枚、および同じ面のct_mid一枚を最初の比較集合とする。モデル名の正確なパスは固定tree/metaで確認。別深さ・別モデル・別面への拡張は今回しない。本文全7枚の長さ/SHAが分かったら計画を保存し、合計64MiB以内・新通信合計300秒以内の範囲で取得可。予定画像が存在しない、または超過する場合は勝手に切り替えず、得られたメタで結論を残す。メタ/原文は1MiB、必要なら同じ面のXYZ3枚を合計2MiBまで。新しいCTボクセル・レンダー・学習・モデルforward・依存追加・有料計算は0。

保存先 experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/。C新規、既存は読取り、追加作業256MiB以内、CPU1/process commit4GiB/数値1thread。R187 tools/research/run_windows.py を新規実行に使える。188の原寸比較・独立照合の経験は使えるが、上流が違うので188の向きの逆命名やscale/canvas式は転用しない。

元0–255の表示と原寸を保ち、CT、Hecate、Reader V3、seed42の同じ画素位置を比較する。予測を生成補完しない。overviewで位置関係を示し、原寸の全体確認を可能にする分割図を用意する。短い塊・繊維沿いの線・空隙端と、独立した字画形や行/間隔の反復を区別する。複数モデルの一致や強い画素値を判読の証明とは扱わない。親は候補/否定判断に用いた原図を別目視し、共通pixelと原寸図の一致を独立確認する。

追試候補がある場合は一つのnative ROIを固定し、metaのmesh.base/CT参照、格子scale・原点・描画サイズからXYZに戻れるか確認する。対応を裏付ける資料がない場合は推定を明記し、CTの取得計画を確定しない。候補を選べなければこの一面を閉じ、巻物全体のインク不在へ一般化しない。可読文字の転写・10字達成・受賞や新発見は根拠が揃うまで主張しない。

結果をこの票へ追記、元ファイル/取得原票/条件/比較図/実測資源/manifest/lab候補を残す。登録は親、サブ委任なし。今回は gpt-6.1-sol / high を選ぶ。固定公開画像を原寸・同座標で比較し、既存の逐次比較手順を別面の来歴に合わせて実行するため。GPU解放待ちの反復や新環境構築は並行しない。
## メモ

- R166保存atlasカード・index、R186保存公式Data Browserと規定から対象を確認。固定木・面metaを照合し、七PNGの長さ/LFS SHAと取得計画を先に保存した。全七画像が2184×2184のuint8でSHA一致。原寸16図で担当目視を終え、主担当に同じ図と画素索引を共有した。

## 結論

2026-11-14 JST。[一次・目視] PHerc0846B `2768_2813_9748` の中心予測で、元CTに戻す字画・行のROIを選べず、一面で閉じた。担当は原寸16図を、主担当は全体図・Hecate両順原図・原寸4図を別目視した。主担当による固定SHA・原寸33,388,992画素の独立照合も通過した。観察範囲はこの一面の中心窓。 [原寸図と位置](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/README.md) [主担当の目視](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/lead-visual.json) [主担当の数値照合](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/lead-checked.json)

## 根拠・詳細

- [一次・実測] 固定atlas `ac5ffd7098120368216948c4e06c494bf8e67178` の中心窓 `c+0_s1`。Hecate 9.6、Reader V3、ink_9um seed42（step 75,000）のforward/reverseと中央CT PNGで計七枚。すべて2184×2184単チャンネルuint8、取得前に保存した公開の長さ・SHAと一致した。0–255の画素値を保った同座標原寸16図を保存し、元画像との112パネル全値比較に合格した。 [固定取得計画](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/acquisition-plan.json) [全体図と原寸図一覧](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/README.md)
- [一次・目視] Reader V3の中央下の横帯（概略 `[1092,1450,1950,1610)`）はCT中央層の裂けや層境界に重なり、左上寄りの斜め帯は曲がる繊維・空隙に沿う。Hecateの強い反応は散在する短い塊、seed42は両順で外縁に沿う帯と内部のぼけた塊が目立つ。比較した形に独立字画や一定の字間・方向が続く行を選べなかった。 [位置別原図](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/README.md)
- [一次] 元meshは固定survey `1f12c1ce` の `PHerc0846B_2768_2813_9748`。公式Data Browserはscan `20250719185515`、volume `20250804142305`（9.362 µm、113 keV）を掲載し、atlas metaのCT参照は同volumeのL0。atlasの描画は9.6 µm/px、scale 0.975、全canvas box、65層。方向はatlasのファイル名どおり。三モデルの学習曝露はmetaでunknown。XYZは取得しておらず、画素→CTボクセルの写像は未検証。 [面meta](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/surface-meta.json) [保存した公式Data Browser](../experiments/vesuvius/discovery/20261114-unread-lead-reselection01/originals/official-PHerc0846B.html)

## 取得の経路

固定木・metaでパスを確認してから、中心七PNGだけを取得した。計8,156,193 B、通信15.006秒、原寸作成と画素照合8.544秒。R187のWindows入口でCPU1・数値ライブラリ1スレッド・commit上限4 GiB。新規CTボクセル・レンダー・GPU・モデル実行・依存追加・有料計算は0。 [取得原票](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/acquisition.json) [再実行手順](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/README.md) [manifest](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/manifest.json) [lab登録候補](../experiments/vesuvius/discovery/20261114-pherc0846b-native-atlas01/record.json)
