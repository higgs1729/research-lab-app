Status: resolved
担当: 研究（R158担当 2026-11-13）
Blocked by: 157

# R005: 格子保持を標準CMakeの構成でも小さくビルドできるか

## 依頼

2026-11-13。格子保持の試作は既存flatboi/ラスターを同じ新ヘッダーで二つの翻訳単位として作り直し、隔離ELFへ直接リンクして検証した。上流の通常CMakeからのビルドはまだ実行していない。UvGridRasterizerのクラス配置を変えたため、通常のvc_coreと利用側を同じヘッダーから構築する経路の成立性は、他の開発者が使う際に意味がある。独自のビルド基盤を増やさず、上流CMakeと保存済みのソース・依存を借りて確認できる最小範囲を調べる。

今回は軽い調達・成立性確認。既存CMakeCache、compile_commands、ソースと依存・生成物の置き場、標準ターゲットの依存関係、C:空き容量を読み、次の一回のビルド案を出す。configure/コンパイル/製品実行、clone/fetch、依存導入や大量コピーはまだしない。固定対象は追加候補の上流14d4e725df8b569e6fc8ceb3c04d130f705c1565を第一候補とし、そのソースが保存済みGitに揃うかを確認する。別の保存baseなら、差分が同じであることと、現在のmainの全体検証にはならないことを区別する。

既存R003/R123/R150の構築を参考に、D:を一切書き換えずC:で標準ターゲットflatboi・vc_coreと必要なら同じクラスの他の呼出元を構築できるか判断する。未変更の依存を読取で借りる箇所と、変更ヘッダーで再構築が必要な箇所を区別する。CMakeの依存取得やexternal projectがD:のsource treeへ生成物を書かないかも実際の設定を確認する。参考書を網羅する調査や汎用ビルダーは不要。

結果は本票とexperiments/vesuvius/r005/20261113-standard-build-feasibility01/ の根拠・推奨案一つ・見積もり・lab候補。新規コード/依存/データの必要量、C:使用量と既存空き、CPU一個・メモリ4GiBを保つ場合の時間/失敗の見込みと試行上限、成功時に既存の第一面出力と比較する最小実行を明示する。保存済み資産で成立しなければ、何が欠けるかを具体的に残す。有料計算は使わず、外部公開/PR/応募/メッセージ/subagentなし。既存の全登録物とD:は不変。

モデルgpt-6.1-sol、effort xhighを今回選択。標準CMakeと隔離リンクの依存/ABIの境界を整理し、新しい実行手順を設計する必要があるため。主担当が調査後に次の実行を選ぶ。

## 結論

[一次・推論、2026-11-13] 保存済み7ad02f4を使う標準CMake試験を一件提案する。C:上の既存WSL ext4 VHDに作業先を作り、上流の `flatboi`、共有 `vc_core`、同じクラスを実体化する `vc_obj2tifxyz` の3標準ターゲットを同じ新ヘッダーから構築する。14d4e725はcommitとtreeが存在するが、構築に関係する3範囲の本文が揃わない。旧基点の標準ビルド成立性を先に測れる。固定main全体の動作は未確認。[一件の実行案](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/README.md)

## 根拠・詳細

- [一次] オフラインのGit列挙と保存treeで、14d4e725の全6,462パス中2,693の本文がD: Gitに欠落。構築の3範囲では、volume-cartographer 80、vc_reader 5、vc_object_store 290の計375 blob・未圧縮7,069,787 B。C:の既存部分Gitで本文一致を確認できる1件を除くと374件・6,965,009 B。実転送量は未測定。readerとobject storeのCMakeLists、`QuadSurfaceStore.cpp` も不足するため、14d4e725を使う段階ではD:を変更せずC:に不足ソースの取得が必要。7ad02f4の3範囲2,159パスは全本文が揃い、試作の変更3ファイルと主要CMakeListsのblobは14d4e725と一致。`vc_obj2tifxyz.cpp` やreader・object store等にはコミット間差分がある。[ソース集計](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/source-availability.json)
- [一次] 通常CMakeのPaStiXは自身とSPMのCMakeListsをsource側で書き換える。PaStiX・既適用libigl・delta3dの保存ソースをC:側へコピーする案。3依存は `.git` 等を除く本文約21.6 MB。libbacktraceはsystem pkg-configが見つからず外部Gitへ進むため、既存ローカルGitをfile URLに差し替え、標準ExternalProjectを新規C側に置く。旧D:のCMakeCache/生成物・隔離ELFは構築に使わない。上流のPaStiX設定、ローカルGit URL差替えと実際の構成は次の一回で確認する。[依存の原票](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/dependencies.log) · [ローカルGit](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/offline-source.log)
- [一次・推論] `VC_BUILD_APPS=ON` で `vc_obj2tifxyz` が構成される。既存Qt6・Boostが見つかり、ビルド対象は3つに絞れる。新しい `libvc_core.so` の定義と両利用側の動的ライブラリ解決を照合し、旧バイナリとの混在を避ける。元の第一面・keep100・5反復・新モード1回でR150観測なしのXYZ TIFF三枚・全画素と名目scaleを照合する。旧ABIへの共有ライブラリ単体差し替えや14d4e725の配布検証は範囲外。[標準ターゲット](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/targets.log)

## 取得の経路・資源

C:空き45.7 GiB。旧D:ビルド2.1 GiBから、新規作業の見込み3 GiB、上限6 GiB。1CPU、AS4GiBで、configure 1〜4分、初回build 20〜35分を見積もる。上限は各600秒・2,400秒、最小実行120秒、各1回。旧R003のexFATでのヘッダー複製を避けるため、WSLのLinux側に置き、生成ヘッダーリンクを確認する。今回の調査は静的読取のみ。configure、ソース展開、依存コピー、ビルド、製品実行、新規取得・導入・課金は0。[見積もり・停止条件](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/README.md) · [lab登録候補](../experiments/vesuvius/r005/20261113-standard-build-feasibility01/record.json)

## メモ

- 固定14d4e725のローカルGit存在、R003の通常CMake、変更ヘッダーの呼出元と依存ソースの書込み先を調べる。
- Windows GitがD:のownershipで止まったため、WSL内・ネットワーク分離で読んだ。partial cloneに直接 `cat-file` を使うと不足blobの最初で停止するため、`rev-list --missing=print` と固定treeの積集合へ切り替えた。いずれも外部接続せず、採用原票はtree突合。
