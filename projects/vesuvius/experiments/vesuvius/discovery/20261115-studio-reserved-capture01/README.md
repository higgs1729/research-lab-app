# R230 Studioの結果領域を事前確保する

Windowsの実割当を確認した12 MiBの専用ファイルに、R229と同じ結果collectorでarchiveを書き戻した。模擬C空き3 GiBでは旧版が全チャンク取得後に停止し、新版は同一file IDへ書込み、fsyncと読戻しSHA照合を経て失敗workerの原票を保存した。過大サイズ、誤SHA、予約欠損、所有ID違いは拒否した。開発中に逐次伸長でNTFSが15 MiBを一時割当したため、採用版は最初に12 MiBへ長さ設定してから全域を書き、実割当を12 MiBに固定した。 [回帰試験](offline-collection-test.json) · [collector差分](collector.diff)

有償試行の作成前にも、親が独立して物理割当12,582,912 Bと所有IDを確認した。予約後のC空きは10,407,673,856 Bで旧入場条件の10 GiBを下回った。入力のR229 A40 gzipは同じSHA、全17メンバ同一で、plan、CPU0/47/95、固定重み、Pod内の科学workerと資源条件を維持した。 [使用計画・入力SHA](cloud-plan.json) · [親の実割当確認](lead-live-reservation-check.json)

Secure A40一台はEU-SE-1で起動した。サービスの状態表示はRUNNINGだったが、起動確認のexecは409が36回、初期404が2回。10:02:06 UTCのproviderログには固定イメージを取得中とあり、240秒枠にPID1 readyが成立しなかった。入力転送、Pod内の重み取得、GPU forwardはいずれも0。実結果archiveの回収、CPU–GPU比較、字画再現、原寸図、親の再構成は未評価。 [起動原票](cloud-run/startup.jsonl) · [providerログ](startup-probe/startup.jsonl) · [終了traceback](controller-stderr.txt)

Pod `1rznb9oa1abxn1` は10:02:54.690520 UTCに削除確認。親は独立にGET404、専用名0、全Pod0を確認した。独立local監視PID56456はcreate前に起動、終了後に残存なし。未使用予約は所有IDを再照合して解放した。実createdAtから244.51752秒の時刻見積は計USD0.04026238。専用明細は空で実費未確定。 [資源・費用](resources.json) · [削除原票](cloud-run/cleanup.json) · [親の再照会](lead-cloud-resource-check.json) · [予約解放](reservation-release.json)
