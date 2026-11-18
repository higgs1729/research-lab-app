# R239 fixed approximate-window screen — proposal for lead review

2026-11-15。Pod未作成。主担当が本plan hashと具体UTC枠を承認した後だけ実行する。

## Scientific decision

保存96² public/render確率のraw差はmax0.0028054118、mean0.0006942505。旧R236 mean<=0.0005は不合格のまま残す。同じ固定raw8表示の差は最大1 DN、1,689/9,216画素で、担当・主担当の別目視では粗い形の差を認めなかった。取得済み公開v6の固定knownφ320×300では双方が粗い環状部と縦軸を確認した。単独の確実な読字試験ではない。

今回は「原CTで追試する字画/行ROIを選べるか」を問う別の近似探索である。旧gateの値・閾値・passedを観測として保存し、finiteのみをこの対比較の進行条件とする。モデル/入力hash、228パッチのdevice-specific正規化SHA、既知0343 CPU出力3点のmax差<=1e-4、出力finite/0..1、資源・時間の停止条件は維持する。R236–238の不合格/未成立は変更しない。

knownφ36は**公開原入力**であり、「同じFP32推論実装で既知の粗い形が出る」対照である。近似renderによる全体φ再現ではなく、未知入力全体の正しさも証明しない。小φ対、既存幾何/CT照合と合わせても、この不確かさは残る。

## Fixed execution and judgement

- 順序は既知0343参照3、publicφ1、renderφ1、公開knownφ36、未知187。計228、同じStudioFP32モデル1回load。新CPUforward0、新CT0。
- R236の全case・input bytes・depth+8..−7・全親stride64・mask・Hann結合・主域 `[4352,1664,1024,640]`・支持 `[4272,1584,1152,768]` をそのまま維持。新renderer/窓/depth/model探索なし。
- native raw0..1、固定nonzero median..p99.5、CT max indices6:10というR236の事前表示だけを使う。knownφ320×300を今回取得した同じ公開raw8原寸と比較し、未知1024×640も原寸で別評価する。
- 担当が所見を先に保存し、主担当が解釈を読む前に別目視する。既知形を認められなければ未知反応を採用しない。両者が原CT追試の明確なROIを選べなければこの窓を終了。明るさだけで文字/新発見と呼ばず、救済の閾値/depth/model/窓追加をしない。

## Assets and changes

- `cloud-input-r239.tar.gz`: 21,535,991 B、SHA `089b3e2f44196cb556ae8a96ce36f3f744d0df1b1dafe5f66ce04c2d68b6fc37`。
- `cloud-plan.json`: SHA `4016e04378aa91630b29e4ee33d164a1dd3904ccbafb498bd6bff5601e1c94fc`。
- `plan.json`: SHA `f609d253d655bba5792d3892ce8d0cd178d496ff6da0d1af677a433ee7aa43fa`。
- 25 archive members中、変更は`gpu_loop.py`、planとそれを参照する2contract、`fixed-assets.json`の5件。残る20件はR236とSHA一致。checkpoint893,443,724 Bは同じ固定URL/SHAでPodへ一度だけ取得、ローカルには取得しない。
- `r236-to-r239-diff.patch`にworker/gate、controller/台prefix、capture上限、result表示条件、plan/contractの差分。`bundle-change-report.json`に全member比較。
- `capture.py`の実上限を768→192 MiBへ変更。回収64 MiBの物理割当と同一fileIDでの公開処理、親controllerのfinally削除、独立deadline処理は再利用。旧foreign allowlistは削除した。
- `offline-check.json`は実アーカイブ228パッチ、3CPU参照、実gate式に保存R236失敗を通す確認、nonfinite/欠落時停止、controller組立、所有prefix/旧foreign拒否、容量を確認済み。model/GPU/network/createは0。

## Resources and lifecycle

`live-plan-read.json`（2026-11-15T14:19:36.203669Z）で現存Pod0、Secure A40 $0.59/h、CA-MTL-1 LOW、auto-pay=false、残高$15.9947288895を読取確認。旧foreign idは今回の許可根拠に使っていない。実admissionと作成直前の両方で現存0を再確認し、変化があれば作成せず主担当へ返す。

一台のみ・自動再作成0。想定8–16分で$0.08–0.16、運用上限$0.35、live rate<=0.60/h。20GB一時diskを含む30分見積最大$0.30139。これは事業者の強制上限ではない。実precreateを起点にprovision600秒、transfer1080秒、model1380秒、collection1740秒、削除1800秒の絶対境界を保つ。主担当が`lead-cloud-clearance.json`へplanSHA・latest_precreate_utc・absolute_delete_not_after_utcを記録するまでrunしない。

現保存約34.32 MB。以降の64 MiB物理回収予約+48 MiB展開+24 MiB図枠を足した実計算上限176,918,613 B（約168.7 MiB）、宣言見積174 MiB、総新規上限192 MiB。作成前にこの残余容量とC空き2 GiBを同時確認する。CPU1/commit4 GiB、C作業のみ。回収する配列18,202,880 B+logs metadata5 MiB、archive64 MiB上限、展開48 MiB上限。

専用`r239-studio-<16hex>`名、作成前exact-name0、即時保存したidとcreatedAt範囲で所有を限定。finallyと独立hidden deadline watcherはこのidだけを削除し、GET404/TERMINATEDとexact-name0を確認する。主担当が独立再照会し、専用Podのbillingを記録する。アカウント残高差を研究実費とみなさない。R236–238のファイル、既存別用途台には書き込まない。

実行入口（承認後のみ）: `python -B tools/research/run_windows.py <new run-process receipt> <HERE239>/control_coexist.py run`。

主担当の今回独立照合前に研究manifest/recordは凍結しない。
