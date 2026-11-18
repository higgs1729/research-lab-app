# R005 一成分w035の製品対照

固定入力は研究128の PHerc0139 w035、scan 20250728140407、9.362 µmのTIFXYZ。入力XYZ三枚とmetaを取得記録と独立union-find原票のSHA-256に照合し、R150 build01の観測なし製品ELFを借りた。 [取得原票](../../r011/20261113-w035-geometry01/run01/fetch.json) · [一成分の独立根拠](../../r011/20261113-w035-geometry-verification01/result-final.json) · [R150製品ELF](../20261113-grid-preserving-native01/build01/product-binary.json)

## 再現

原票のrun01は固定。別名run02が未使用なら、研究リポジトリをカレントにしたPowerShellで同じ条件を再現できる。WSLと既存R150のネイティブ依存は再利用。結果比較には手元のWindows PythonのNumPyとtifffileを使用する。

~~~powershell
$d = 'experiments/vesuvius/r005/20261113-single-component-control01'
wsl -d Ubuntu --exec python3 -B "/mnt/c/dev/kensyoukin/$d/run_w035.py" run02
python -B "$d/compare.py" run02
~~~

run_w035.py はR150の既存環境設定と bounded launcher を呼び、同じ入力・製品・keep100・5反復で既定、新フラグの順に各一回だけ起動する。2回合計の期限300秒。CPU affinity 1、数値スレッド上限1、AS 4 GiB、core 0、unshare -Urn。各起動のargv、環境差分、終了値、再開しない失敗時のログ、RSSはケースの原票で確認できる。出力と設定ディレクトリはケースごとに別の新規パス。

比較器は既存TIFFを復号し、XYZ全位置のfloat32のビット列とファイルSHA-256を別に照合する。生成metaの構造、SLIM energyの6行、進捗、PNGとテキストのレポート、条件・時刻付きの実行原票を個別に集計する。 [比較原票](run01/comparison.json) · [入力と制約](run01/inputs.json) · [完了時点の保護確認](run01/completion.json)
