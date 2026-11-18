Status: resolved
担当: 研究（R159担当 2026-11-13）
Blocked by: 158

# R005: 標準CMakeの共有ライブラリと利用側を揃えて構築し、既存出力へ照合する

## 依頼

2026-11-13。研究158の一案を主担当が採用する。保存済み7ad02f4f6e306b744ef6d2742dfe31fd55713ee5を基点とし、上流の標準CMakeを使ってvc_core・flatboi・vc_obj2tifxyzを同じ格子保持の変更ヘッダーから構築する。R150の隔離リンクと異なる通常構築の成立を問いとする。現行main14d4e725の全体検証には数えない。

入力、依存、CMakeフラグ、GitローカルURL、既存assetの根拠はexperiments/vesuvius/r005/20261113-standard-build-feasibility01/README.mdの具体案。C:/WSL/Ubuntu/ext4.vhdx上の未使用のLinux専用作業先へ旧基点の3サブツリーと必要3依存を展開し、D:は全て読取専用で扱う。Gitはlazy fetchを無効化し、外部通信を遮断する。PaStiX/SPMのsource変更はC側コピーだけ。libbacktraceは上流ExternalProjectを維持し、既存ローカルGit固定masterをfile URLで供給する。Dの古いCMakeCache・生成物・R150オブジェクトを新ビルドへ持ち込まない。新たなbuilder/compatibility shimや上流ソース/CMakeの改造を足さない。

製品差分は154追加候補の二段だけ、変更3ファイルをR150の清書済みSHAに合わせる。configure後にreaderの公開headerがLinuxシンボリックリンクであること、external libbacktraceの並列数とsource/buildの書込先、使う依存が計画内であることを確認してからbuildへ進む。初回構成で不足依存や想定外の取得要求が出た場合、ログを保存して止め、無制限に補修しない。

制限はCPU一個・数値/OpenMPスレッド1・AS4GiB/core0・ネットワーク分離。作業量目安3GiB、上限6GiB、ホストC:空き10GiB以上を保つ。configure一回600秒、標準3ターゲットbuild一回2400秒、製品比較一回120秒。構築中も進展・失敗と実測資源を短く親へ知らせる。上限超過や失敗時は自分が起動したプロセスだけを回収し、原票を保つ。追加依存導入・外部取得・課金はしない。

構築成功後、nm/ldd/compile_commandsで新vc_coreの実定義、flatboiとvc_obj2tifxyzの同一新ヘッダー/共有ライブラリ解決を確認し、Dの旧共有ライブラリを探索経路に入れない。第一PHerc0814固定入力をmanifest照合して新flatboiのkeep100・5反復・--pack-components-preserve-gridを一回実行。R150観測なしfirst-preserve-productの172×683、XYZ三枚SHA/全float32画素、名目scaleへ比較。生成UUIDは別扱い。vc_obj2tifxyzはhelpと共有ライブラリ確認までで、OBJ生成・CT・推論・他の入力試験は不要。

成果は本票とexperiments/vesuvius/r005/20261113-standard-cmake-build01/の準備/構成/ビルド/実行の条件・原票・sourceと生成物の同一性・費用・lab候補。Linux側作業先の実パスと、C:に出力された根拠の関係を明記する。既存登録物・D:・公開/追加候補は不変、外部PR/公開/応募/メッセージ/subagentなし。主担当が別照合と採否・登録を行う。

モデルgpt-6.1-sol、effort xhighを今回選択。手順案は158で得たが、実際の初回CMake構築とライブラリ配置には未確認の境界が残るため。同じ調査担当に引き継いで既存依存の読み直しを減らす。

## 結論

[一次・2026-11-13] 保存済みvilla `7ad02f4` に研究154の製品差分2つを適用し、上流の通常CMake/Ninjaで `vc_core`、`flatboi`、`vc_obj2tifxyz` を構築した。3翻訳単位は同じ変更済み `SurfaceMeshing.hpp` を使用し、両実行ファイルが作業先の新しい共有 `libvc_core.so` を解決した。第一面の新モード出力は172×683、XYZ TIFF三枚が研究150の観測なし出力とSHA-256および各117,476画素のfloat32ビットで一致。名目scaleも一致し、`meta.json` の差は生成UUIDのみだった。[構築と実行](../experiments/vesuvius/r005/20261113-standard-cmake-build01/README.md) · [画素比較](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/comparison.json)

## 根拠・詳細

- [一次] 旧基点を各サブツリーから展開し、公開済み配置と格子保持の二差分だけを適用。実ソース3件は研究150の清書済みSHA-256と一致した。作業先は `C:/WSL/Ubuntu/ext4.vhdx` 内の `/home/tomoy/r005-standard-cmake-run02-4lvsfbul`。C:の実験フォルダに構成・実行の原票とXYZ出力を保存。D:はプロセス専用のmount名前空間でread-onlyにし、保護ファイルの前後SHAも一致した。[ソースSHA](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/patched-source-sha256.json) · [保護照合](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/final-state.json)
- [一次] readerの公開ヘッダーは作業先ext4上のsymlink。libbacktraceは保存ローカルGitの固定 `0b9b49cf` を標準ExternalProjectでclone・configure・build・installし、生成コマンドの `make -j1` と全作業先を確認。構成後のcompile_commands・ビルドコマンドにD:への参照はなかった。通常CMakeの971ステップを完走し、新しい共有ライブラリの `packComponentsOnGrid` 定義、3TUの実Ninja依存と両バイナリの `ldd` を照合。`vc_obj2tifxyz --help` は終了0。[構成後の検査](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/configure-check.json) · [実リンク](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/link-check.json)
- [一次] 固定第一面の入力4件を既存manifestと照合し、keep100・5反復・`--pack-components-preserve-grid` を1回実行した。固定main `14d4e725` 全体、旧利用側への新共有ライブラリの単独差し替え、OBJ生成、CT・推論は検証範囲外。[実行条件](../experiments/vesuvius/r005/20261113-standard-cmake-build01/run02/native-process.json)
- [一次・独立照合] 主担当が実ソース3件、新ビルド4生成物の実体SHA、構成と工程成功、Linux実出力と保存XYZ三枚の全値・SHA・名目scaleを別コードで確認した。[独立照合原票](../experiments/vesuvius/r005/20261113-standard-cmake-build01/lead-check.json)

## 取得の経路・資源

CPU affinity 1、数値/OpenMP 1スレッド、AS4 GiB、core 0、ネットワーク分離。実測はconfigure 77.208秒・RSS52,690,944 B、build 686.787秒・RSS1,672,716,288 B、第一面26.793秒・RSS230,363,136 B。Linux作業の最終割当1,449,947,136 B、監視時点のホストC:空き最小45,294,411,776 B。追加ネットワーク取得、依存導入、クラウド支出0。R158案で使ったGitコマンドの準備失敗を下に記録し、上流CMake構成・ビルド・第一面は各1回で完了した。[再現手順・原票](../experiments/vesuvius/r005/20261113-standard-cmake-build01/README.md) · [lab登録候補](../experiments/vesuvius/r005/20261113-standard-cmake-build01/record.json)

## メモ

- 既存CMakeとR103計測ランナーを使用する。ソース準備からfirst面照合まで、新しい実験原票とLinux専用作業先に分離する。
- 初回準備の `git archive <commit> <3 paths>` がGit 2.43の部分cloneにある範囲外の `.github/CODEOWNERS` blobを要求して停止した。通信分離・lazy fetch無効のまま、同じ固定commitの `<commit>:<subtree>` を3回読む方法へ変更。run01ではconfigure未起動。run02のパッチ適用に凍結差分由来の行末空白警告1件があり、原文を維持して3SHAを照合した。
