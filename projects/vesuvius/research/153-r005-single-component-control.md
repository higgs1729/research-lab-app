Status: resolved
担当: 研究（R153担当 2026-11-13）
Blocked by: 152

# R005: 一成分の実面では新しい配置設定が何も変えないか

## 依頼

2026-11-13。新しい格子保持モードは149–151の二つの複数成分面と、152の固定CTで支持保持を確認した。実用上の基本境界である一成分の実入力は未確認。研究127/128で公開PHerc0139 w035の9.362µm面を確保し、使用頂点63,499、三角形125,826が一成分と独立確認済み。この既存実データを対照として、既定のflatboiと--pack-components-preserve-gridが同じ出力を作るかを調べる。

既存R150 build01の観測なし製品バイナリと、127/128で固定済みのw035入力だけを使う。keep100・5反復、同じ条件で既定/新フラグを各一回、新出力へ実行し、XYZ TIFF三枚のファイルSHA/全画素、格子寸法、scale、SLIM energyと実行状態を比較する。生成メタデータやレポートのうち日時/識別子/設定記録が異なれば、何を比較対象に含めたか明記する。元の固定入力hashと一成分の根拠を確かめ、R150で使っていた複数成分の別入力との取り違えを避ける。従来packの再試験やCT/モデル推論は不要。

変更コード・新しい観測版・新ビルドは作らない。R150の既存実行ランナーを必要な2起動に再利用し、全runセットを回し直さない。追加取得/依存導入/GPU/課金なし。D:読取C:出力、1CPU/AS4GiB/core0/ネットワーク分離、ネイティブ2回合計300秒以内を目安。失敗や想定外があればコード修正や追加探索はせず、原票と原因を分かる範囲で返す。上流の規定と研究の共通指示を読む。外部公開/PR/メッセージ/応募/追加subagentなし。

成果は本票、experiments/vesuvius/r005/20261113-single-component-control01/ の再現条件・比較・費用・lab候補。作業先.work/r005-single-component-control01/。この比較で一成分全般やkeep<100/store等を保証しない。親が出力の別照合と採否を行う。

モデルgpt-6.1-sol、effort high。実行手順は既存で、別の既知実面の入力対応と出力同一性を解釈するため。

## 結論

［一次・実行］PHerc0139 w035の一成分の公開面で、同じR150製品ELFをkeep100・5反復で既定と --pack-components-preserve-grid 各一回実行した。両方終了0。出力格子は286行×259列、各62,646有効格子点。XYZ各TIFFのファイルSHA-256と、復号した各74,074個のfloat32の全ビットが一致した。scaleは両方とも [0.05000000074505806, 0.05000000074505806]。SLIM energyは初期と5反復の6値がファイル単位で一致し、最終値は8.0024943049。 [比較原票](../experiments/vesuvius/r005/20261113-single-component-control01/run01/comparison.json)

［一次・保存物］生成metaで異なったのは出力uuidだけ。4枚のSLIMヒートマップと表示範囲テキストもSHA-256一致。コマンド、出力パス、時刻、資源を記録する条件・ログ・計時原票はケースごとに保存した。主担当の別スクリプトでも固定入力とELFのSHA、XYZ各画素とファイルSHA、scaleとenergyの一致、meta差がuuidだけであることを確認した。 [独立照合](../experiments/vesuvius/r005/20261113-single-component-control01/lead-check.json)

## 根拠と範囲

［一次］公開9.362 µm w035の保存XYZ三枚とmetaのサイズ・SHAを、取得台帳と独立幾何原票に前後照合した。元格子291×262、使用63,499頂点、62,913 quad、125,826三角形、一成分。新フラグは有限なscale・面UVを確認し、配置対象が2成分未満ならラスターの配置処理は戻る。この入力のTIFXYZ入口・keep100・固定5反復での結果であり、keep<100、store入口、他の一成分入力、CTと判読への一般化は未確認。 [入力とELF](../experiments/vesuvius/r005/20261113-single-component-control01/run01/inputs.json) · [幾何の独立根拠](../experiments/vesuvius/r011/20261113-w035-geometry-verification01/result-final.json)

2026-11-13 JST。既定68.075秒、新フラグ90.298秒、2起動の区間158.404秒、最大RSS 341,733,376 B。CPU affinity 1、数値スレッド上限1、AS 4 GiB、core 0、ネットワーク分離、2回共通の期限300秒。この各一回の計時は性能比較には使わない。入力・製品・既存依存ハッシュは前後一致。追加取得・ビルド・CT・推論・クラウド支出0。 [再現手順](../experiments/vesuvius/r005/20261113-single-component-control01/README.md) · [lab登録候補](../experiments/vesuvius/r005/20261113-single-component-control01/record.json)
