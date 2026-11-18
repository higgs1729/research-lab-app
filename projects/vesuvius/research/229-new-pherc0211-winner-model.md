Status: resolved
担当: 研究（r229_new_winner_model、gpt-6-astra/xhigh、2026-11-15）
Blocked by: 228

# 本日発表のPHerc0211受賞モデルは、現在の探索に使える新しい比較器か（2026-11-15）

## 依頼

本人の主目標は新しい文字の発見、低支出で初受賞、再利用物を残すこと。R228はrecord-4e54e23db6acへ登録済み。PHerc0306B上方の公開既出候補は元CTで一枚帰属を確定できず、事前条件に従い同候補の局所幾何診断を終了した。候補は未確定保存、新文字0、公開済み三改善と11月まとめ応募は維持する。同じCT診断や根拠のない深さ/閾値探索へ戻らない。

本日11月15日、公式がPHerc0211のFirst Letters受賞を発表した。主担当は公式原文を直接HTTP200で確認した。https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211 。受賞者は、native約9µmの16層を読むresidual3D U-Net、類似CTに基づく0009B/0841/0814ラベル、追加12巻/断片での継続学習、soft lossを説明し、競技巻では訓練していないと述べる。コードMIT https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt 、重みCC BY-NC4.0 releases/tag/studio-softloss-20261023 、学習データはHF paranke/vesuvius-814-841-9b-studio-training-data と paranke/vesuvius-expanded9-training-data、第三者reader-v2-labels。公式賞一覧には0211と残り8の古い表記がまだ残るが、新しい発表は0211受賞/残り7を明記。0211を未受賞対象にしない。これは他者の成果で我々の発見ではない。

問いは、この新公開モデルが既済seed42/dense-native/Hecate/Reader V3と実際に異なる入力契約・学習来歴を持ち、既存の保存CTを使う一回の低費用比較へ導入する価値があるか。まず原文/固定ソース/リリース/サイズとハッシュを取得し、既済チェックポイントの別名や同一実体でないこと、前処理・深さ順/分解能・tile/halo・正規化・モデル出力・学習露出/ライセンスを短く確認する。残差UNetという名前や作者の感想だけで性能優位を主張しない。

入力と実行見積もりが固まったら、既知対照一件の計画を主担当へ返す。そのまま本票の中で対照を実行してよいが、前処理・対象・パッチ/CPU参照・判定条件を予測前に凍結し、主担当の確認を受けてからforwardする。ここで必要なのはモデルの成立と既知字画の出方を確認する一回で、対照を何段も増やすことではない。既存PHerc0343の222入力は再利用候補の例。学習露出のある対照は実行整合の対照とし、汎化性能を測ったと主張しない。既済画像/原入力/CPU参照手順を再利用し、既知の文字構造を同じ表示で比較する。別条件を足して結果を救済しない。未知投入は本件の結果を主担当が見て一件選ぶ。

保存先 experiments/vesuvius/discovery/20261115-new-211-winner-model01/。初期取得はソース/メタ/本文計16MiB以内。重みはHEAD/APIで実量を確認し、計512MiB以内なら主担当への計画に含める。これを超えるときやC空き10GiBを割るときは代替と必要量を伝える。大きな訓練データの取得、学習、元CT追加取得、surface生成、汎用実行基盤は本件に含めない。推論は既存手元GPUのFIFO/所有権を守り、他用途ComfyUIを止めない。tools/gpu.py --help と222/223の実証済み経路を使う。CPU1/commit4GiB、C作業1.5GiB/空き10GiB、D読取。追加クラウド費0を第一案とし、手元で成立しなければ具体的Runpod見積を返す。Runpod必要分の判断権限は本人委任済みだが、この担当は台を勝手に起動しない。

この依頼を保持し、結論・取得原票・固定版/SHA・入力契約・実測・原寸図・所見・限界を本票に追記。重要ソースと図は早めに親へ渡し、親が別確認する。出力は新規ファイルのみ、過去登録物不変。manifestとlab登録候補を残し、rootが登録する。研究一件/再委任なし、公開・外部メッセージ・応募送信なし。recall追記もrootが重複確認して担当する。

担当はgpt-6-astra/xhighを今回明示的に選ぶ。新公開モデルの学習来歴と入力意味を既存パイプラインへ初めて接続し、既済モデルとの重複と既知/未知の評価を分ける判断が未確定なため。R228完了とinbox未決0を確認して逐次着手。

## 結論

新しい比較器として、固定ソース・学習来歴・入力契約とCPU参照3件を確認した。223,355,921パラメータのresidual3D U-Netは既済seed42/dense-native/Hecate/Reader V3の別名ではない。ただし、GPU結果が未回収のため、既知字画の全域再現・CPU–GPU一致・可読性の比較は未判定。新文字0。

手元GPUはRAM条件により120秒の入場で終了、forward0。親が許可した専用Runpod A40一台は起動後に結果収集へ進んだが、ローカル保存直前にC空き10 GiB条件を下回り、メモリ内のarchiveを保存できなかった。GPUは最大計画96、実forward数不明。finallyで台を削除し、親もGET404・専用名0・全Pod0を別確認した。自動再作成/再推論なし。本件をこの未判定原票で閉じるという主担当の判断に従いresolvedとする。

## 根拠・詳細

- [一次、2026-11-15 JST] 公式受賞発表とGit `235e3be8a06749344862c89a1e52c81d90b15e0e`、10月28日公開の重み893,443,724 B/SHA `96b326286e38de99047f7cab36170c53749a18d5f43e5fde0c7c20f2980b0e90` を取得照合。CPUで214テンソルをstrict load。コードMIT、重みCC BY-NC4.0の宣言を保存。[出典・契約](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/source-study.md)
- [一次、同日] R222既知主域 `[1344,1088,672,448]` とnative16層+8..−7を固定。入力128²/中央96²/stride64、clip200/255、sigmoid後pixel-centred Hann。親は全7,667,712入力値と96位置を別確認。追加CT/面生成0。CPU3参照は73.801秒、CPU1/commit4 GiB内で完了。[固定計画](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/plan.json)・[親の入力照合](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/lead-plan-check.json)・[CPU原票](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/patch-contract.json)
- [一次、同日] A5000は直前在庫NONEでcreate0。親がA40一台US$0.59/h、上限0.60/h、絶対1,800秒/運用枠US$0.35へ変更を許可。科学15ファイル/lifecycle3ファイル同一、固定条件のまま起動。収集時C floor AssertionErrorで科学出力を失った。GPU結果の検算器は未実行で、GPU数値/原寸の確認済みとは数えない。[失敗traceback](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/cloud-controller-stderr.txt)・[未回収記録](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/cloud-collection-failure.json)
- [一次、同日] Pod `fz22fx79xv6493` を09:30:03.778866 UTCに削除。実createdAtから190.607秒、compute+旧disk式の時刻見積約US$0.03139、専用明細未反映で実費null。親が独立GET404/name0/all0を確認。未登録の重みキャッシュ一ファイルの解放は親許可・SHA再確認の原票を保存。[資源・費用](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/resources.json)・[親の残存確認](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/lead-cloud-resource-check-a40.json)

[実験報告](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/README.md)・[manifest](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/manifest.json)・[lab登録候補](../experiments/vesuvius/discovery/20261115-new-211-winner-model01/record.json)

## 取得の経路

GitHub APIと固定raw、HFの固定revisionで本文/モデル契約/ラベルmanifestを直接取得。Substackはweb openが失敗した一方、直接HTTP200で原文を保存できた。既存R222/223の入力とFIFO/guard、R217/219のRunpod lifecycleを再利用。最終Linux workerは科学処理を変えずpath/runtimeだけ適合。重みはPodへ直接fetchする設計とし、手元の再送はしない。

## 本人への質問

なし。研究の次の投入先・出力回収条件は主担当が判断する。本件では次研究の起票/実装を行わない。

## メモ

2026-11-15。R228 resolved、inbox未決0を確認。CONTEXT、instruction-triage、AGENTS、lead、researchスキル、222/223を読んで着手。主担当の独立一次確認でリリース重みは893,443,724 Bと判明し、同じ1.5 GiB作業枠/C空き10 GiB条件で重み取得枠900 MiBへの拡張を主担当が許可した。重み公開は10月28日、本日11月15日は受賞発表。コードと入力の固定後、主担当へ計画を返すまでforwardしない。追加クラウド費0、再委任・recall追記・lab登録・公開なし。

2026-11-15 18時台。固定Git `235e3be8a06749344862c89a1e52c81d90b15e0e` と公式発表HTMLを直接取得。担当のソース/メタ本文は計673,944 B。重みは893,443,724 B、SHA `96b326286e38de99047f7cab36170c53749a18d5f43e5fde0c7c20f2980b0e90`、214テンソル・223,355,921パラメータと一致。公式コードはMIT、重み等はCC BY-NC 4.0、ReaderラベルはMITと記載。10月28日公開のsoft-loss EMAで、既済重みの別名ではない。学習はscratchの814/841/9B→他巻継続30,000更新→soft-loss3,000更新という作者記録。0211を訓練しないとの記録はあるが、0211の評価値を見て選択し、ラベルもStudio系画像に影響された可能性が作者文書に明記されるため、独立盲検評価とは扱わない。

主担当が `plan.json` SHA `d1a9774b2ad3816ade4234c4449577e86f2bf49cd6d809915a1a1c1ebebc0312` を別照合し承認。R222既知主域XYWH `[1344,1088,672,448]` のまま、入力支持 `[1264,1008,832,576]`、保存17層の16..1（符号付き+8..−7）を使う。8.64 µm、16×128²入力、中央96²、stride64の全面位相96パッチ。clip0..200/255、sigmoid後のpixel-centred Hann平均。新CT/再描画0。trainのPHerc0343Pはscan20250521134555、対照PHerc0343は20250521140437で別キー。partの物理的関係・完全な初期ラベル座標重複は未解決のため、本件は既知字画の実行確認に限定する。

CPU参照は固定0/47/95の3回をstrictロード一回、CPU1/commit4 GiBで完了。全監督73.801秒、ピークRSS2,007,961,600 B、最低空きRAM6,969,958,400 B。CPU PyTorch2.14.0、CUDA側の未初期化importは2.13.0+cu130、safetensors0.8.0、追加依存0。構文誤り一回と空きRAM不足一回は子作成/forward前の停止で原票を保存。その後、8 GiB入場条件が満たされ同じ科学条件で参照を完了した。主担当が最終GPU計画の18固定/186借用ハッシュと入口を別確認し、手元の入場を120秒一回だけ試す。RAM条件やC空き10 GiBを下げず、他用途プロセスを止めない。

手元FIFO入場は120.084秒でtimeout、GPU forward0。自launcher51212は消滅、worker未作成、待札0。他用途cw11-stageはそのまま保持した。主担当は同じCPU参照3・96パッチのためSecure A5000一台（API US$0.27/h、許容0.28、最長1,800秒、運用枠US$0.20）への切替案を採用した。既存R217/R219のreadiness/owned-Pod削除を借り、Pod PID1・outer finally・作成前に起動する別local期限監視を用意。作成は変更コード・入出力archiveの親確認後。

C空き低下（消費元は未特定）でcloud freezeを一度停止。親が今回未登録の重みキャッシュ一ファイルだけの解放を許可し、絶対path・bytes・SHAを再確認して削除した。C空き10,593,333,248→11,486,777,344 B、詳細 `cache-release.json`。重み取得原票・214テンソルヘッダ・CPU原票・閉じたlocal計画は保存。クラウドは同じ公開URLから重みを一回直接取得し、手元から転送しない。最終入力archiveは6,980,305 B、全メンバのSHAをoffline照合。科学処理は凍結 `studio_worker.py` のまま、Linux runtime/path adapterで実行し同じgpu出力構造を回収する。小依存safetensors0.8.0のLinux wheel516,040 BはSHA固定、Pod内だけにoffline展開する。クラウド起動0、費用US$0の段階で親へ実行前確認を依頼。

2026-11-15 最終記録。A5000在庫不足でcreate前停止後、親の具体承認を受けたA40一台を起動。結果archiveの全取得・SHA確認の後、保存直前のC空き10 GiB条件で停止し、成果は未回収となった。ディスク満杯ではなく回収設計の問題であり、空き低下の消費元は未特定。実GPU forward数は不明（最大計画96）、CPU–GPU一致・字画再現は未判定、新文字0。finally削除後のGET404/name0/all0とtraceback・collector順序は親が別確認し、`lead-failure-review.json` を原票に含めた。費用はAPI createdAt起点約US$0.03139、親のprecreate起点約US$0.03158という時刻見積を区別し、実費は未確定。追加CPU/GPU・再試行・次研究の実装を行わず、resolvedとして閉じる。
