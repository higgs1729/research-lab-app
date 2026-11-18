Status: resolved
担当: 研究（R208担当、2026-11-14 JST）
Blocked by: 207

# 起動404から409へ進んだ台を当初の時間枠で待ち、準備済みの広域Hecateを完走できるか（2026-11-14）

## 依頼

207で新33×1024²入力・全1922パッチ契約・新先頭3CPU対照・約35.5MBの送信tarが完成し、親の別照合が通過した。共通旧384²の967/4,866,048値に±1DNの差があるが、36共通幾何はbit一致、支持mask同一、全差分の元CT独立補間は整数の中間値から最大0.0301DNで、製品128²tileのfloat原点の違いと整合する。旧入力を上書きせず、新入力のまま継続し出力差を測定する判断を親が記録した。

207の専用PodはGET200で存在を確認したのに最初のexecが404、その後409『Pod container is starting, retry shortly』へ移った。しかし404用の30秒窓を409にも適用したため、全体の240秒起動枠を使えず停止した。台は36.657秒で削除、親もID404/専用名0・別作業台保持を確認。転送/重み/モデル0で、広域の字画は未判定。台の実在GETとexec404の同時観測はできたが、事業者内部の原因を確定したとは扱わない。

次は、この起動状態遷移への局所修正だけで準備済み実験を一度実行する。R206の診断コードは凍結のまま、別の208実行コードとして、同一IDの所有/構成確認を通った後にexecが明示409/503へ移ったら404専用30秒窓を解除する。当初のcreate+240秒起動枠とcreate+1500秒削除期限を延長しない。404の最大3回、各404後の同一台照合、認証拒否/消失時の中止、非冪等処理の再送なし、一回だけの作成・finally削除は保持する。404が続くなら従来どおり止める。

まず局所差分と、207の実測に対応した『404→409を30秒以上→ready』『継続404停止』『409/503でも当初240秒を超えない』の模擬確認を行い、親へ提示する。旧全試験・CT描画・CPU対照・科学処理の再監査を繰り返さない。親が局所変更を確認したら同じ208で実起動まで進む。

207 `cloud-assets` と入力tarを読み取り再利用し、SHAを保持する。Hecate source/checkpoint/image、1024²範囲[576,576,1024,1024]、16層両順、FP32、64²/32/batch1、1922パッチ、先頭3のCPU閾値、入出力量は変えない。実行原票/出力/削除/請求は `experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/` に新規保存。旧207の登録後ファイルを更新しない。新しいCT/CPU/モデル/描画の条件探索はしない。

Runpodの必要分は本人から主担当へ委任済み。25分の段階配分240+500+250+450+60、Secure4090一台、単価≤US$0.90/時、20GB container、見積もり現行0.89なら約US$0.372・最大0.90なら約US$0.376税別、運用枠US$0.50を維持。事業者の強制上限とは扱わない。直前にautoPay false/残高/在庫/単価/既存台を確認し、残高が今回枠と他台25分の消費見積もりを賄うことを確認する。他作業の台は保持し、専用名/ID/起動時刻/期限をすぐ親へ報告。自動再作成しない。

同時に他作業台がある場合、口座残高差を本実験の実費と呼ばない。専用Pod請求行を記録し、未反映なら実費未確定・稼働観測からの専用見積もりと分ける。削除確認は専用ID404/TERMINATEDと専用名一覧からの消失で、全アカウント台0は要求しない。

成功時は新全画像の計算と旧共有パッチ/内部画像との差を照合し、原寸CTと予測から追試する字画/行があるか判定する。親も別検算と目視を行う。元CT入力の1DN差は保存したまま出力差を実測し、bit同一の条件比較とは書かない。未完走ならインク陰性としない。結果・費用・限界をこの票とREADME/manifest/record候補に残す。

今回は **gpt-6.1-sol / xhigh**。既存課題と同じ科学条件を保持するが、未確定の起動状態遷移を局所修正し期限付き課金資源を回収する判断が必要なため。逐次実行・再委任なし。

## 結論

同じ専用台のexecは404が2回、次いで起動中の409が14回。局所修正後、作成から100.128秒で準備確認を通過し、固定PHerc0846A 1024²のHecate両順1,922パッチが完走した。主比較960²（0.84934656 cm²）は従来の9倍で、CTと予測の原寸を確認したが追試する字画・行のROIは選ばなかった。親も別目視で同じ判断。インクの有無は未判定で、この固定範囲・深さの閾値探索は終了した。 [実験結果](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/README.md) · [原寸目視](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/lead-visual-decision.json)

## 根拠・詳細

- [一次、2026-11-14] 12:41:05.128 UTCに専用台のmarker一致。先頭CPU対照3枚は最大MAE 5.213×10⁻⁹、最大絶対差1.602×10⁻⁷。GPUのworker内106.272秒。回収した確率・全PNG値・全入力契約を親が再forwardなしで独立照合。先行する404の事業者内部原因は未確定。 [起動](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/run01/startup.jsonl) · [数値検算](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/lead-result-check.json)
- [一次、2026-11-14] 旧206の同じ内側320²への寄与座標・支持は各121パッチで同じ。旧新CT値は4,866,048値中967値が1 DN異なる。旧新のPNG差は順MAE 0.01734375 DN（最大2）、逆0.1165234375 DN（最大3）。GPU実行先も異なり、出力差の内訳は未確定。 [共通出力の独立照合](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/lead-overlap-output.json)
- [一次、2026-11-14] 専用台は12:49:30.966 UTCに削除・消失確認、605.966秒。専用ID 404と専用名0を独立確認し、別用途台を保持。12:54:40の専用明細照会は0行で実費未確定。専用稼働観測と単価による税別見積US$0.15028。口座全体の残高差US$0.3739071990は別用途台を含む。 [独立削除確認](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/lead-deletion-check.json) · [最終明細照会](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/post-delete-final.json)

## メモ

既存関数の409/503分岐に `deadline_404=None` の一行を追加。模擬で404→409の繰り返しから34秒でready、連続404三回で停止、Retry-Afterが元の240秒を超える場合も停止。207と同じtar 35,512,320 B・SHAを確認した。 [局所差分](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/readiness.diff) · [模擬原票](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/local-verified.json)

12:39:23 UTCに残高US$18.1142141672、自動入金false、Secure4090在庫HIGH・US$0.89/時、別用途の既存台一台を確認した。12:39:25 UTC、専用名 `r201-hecate-ddb021832f07fc02`、ID `454gtwei28qt70` を一度作成。期限13:04:25 UTC。最初の2回は404、再GETは同じIDのRUNNING。その後409へ移行し、元の404窓を過ぎても当初240秒内で確認を続けた。 [入場](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/admission.json) · [作成](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/run01/launch-receipt.json) · [起動](../experiments/vesuvius/discovery/20261114-pherc0846a-wider-hecate-run02/run01/startup.jsonl)
