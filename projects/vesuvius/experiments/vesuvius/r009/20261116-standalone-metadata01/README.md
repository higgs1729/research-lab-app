# R246 R123単独の固定上流ビルドとw035再現

[研究246](../../../../research/246-r123-standalone-upstream.md)の原票。上流villaは `2d3fb38d33a18b257230c0bd23986436c3d4722e`、Git root treeは `e4da163ed927f2a195d2ed79bd5060d4101454f1`。固定API応答から署名付きcommitと各Git treeをハッシュ照合し、対象3プロジェクトとルート指示のファイルを展開する。旧R160は固定mainが異なり、旧結合パッチも入っていた。使うのは一致する上流本文、保存した外部依存、構成引数、計測コード。最初に通常のCMakeターゲット `vc_render_tifxyz` をビルドし、元ELFを同じbinに凍結。R123由来の3ハンクを適用後、同じCMakeターゲットを1回増分ビルドする。

## 実測

| run03の直接出力 | OME目録 | 実配列 | OME-Zarr画像reader |
| --- | --- | --- | --- |
| 元・通常 `--pyramid false` | `0`〜`5` | `0` | path `1` の `ArrayNotFoundError` |
| 修正・通常 `--pyramid false` | `0` | `0` | 1ノード、L0の1配列を読込 |
| 修正・`--pre --num-parts 2 --pyramid false` | `0` | `0`のメタデータ | — |
| 元・修正の既定動作 | `0`〜`5` | `0`〜`5` | — |

両方の通常falseは `.zgroup`（Zarr v2）付きで、ファイル差は `.zattrs` 一つ。属性の意味上の差は `multiscales[0].datasets` の `1`〜`5` だけ。直接L0と修正版のReader出力はZYX `(28,64,64)`・uint8、114,688画素すべて同じ（C順序SHA-256 `8d68bf7bbea4248bf0bf76cdd8c4707aeea70b4d95d6837e378f572698ea9630`、R129の保存L0とも一致）。preは `.zgroup`、`.zattrs`、`0/.zarray` が修正通常と同一、画素チャンク0。既定の元と修正は6レベル14ファイルすべてバイト一致。元・修正の通常false描画は0.566秒と0.495秒。[native全比較](run03/native-comparison.json) · [元描画ログ](run03/baseline-false.log) · [修正描画ログ](run03/fixed-false.log) · [主担当の独立native検算](lead-native-check.json)

Windowsの既存環境（OME-Zarr 0.21.0、Zarr 3.4.2）で `parse_url(..., mode="r")` → `Reader` → 配列 `compute()` を実行。両例ともOME 0.4自動判別時の `version mismatch: detected: FormatV04, requested: FormatV05` が出た。Python warning 0件。Readerで2出力を確認した時間は58.18秒、RSS最大136,773,632 B。本人の作業での実利用、動機の本人記述、コードの本人確認と前後の画面は別途必要。[両Reader端末ログ](run03/ome.log) · [リーダー実結果](run03/ome.json) · [画素・入力不変確認](run03/reader-confirmed.json)

## 再現

PowerShellの作業ディレクトリは `C:\dev\kensyoukin`。以下の `run05` を未使用名にする。run03の元・修正ELFと依存を読み取り専用で使い、R129/R131の保存入力を新しい出力先へ描画する。OMEはR245の既存環境を使う。

```powershell
$base = 'experiments/vesuvius/r009/20261116-standalone-metadata01'
$tag = 'run05'
$run = "$base/$tag"
wsl -d Ubuntu --exec unshare -Urnm bash "/mnt/c/dev/kensyoukin/$base/run.sh" replay $tag run03
if ($LASTEXITCODE -ne 0) { throw 'Native render failed' }
python -I -B tools/research/run_windows.py "$run/compare-process.json" "$base/check.py" prepare $tag
if ($LASTEXITCODE -ne 0) { throw 'Native comparison failed' }
python -I -B tools/research/run_windows.py "$run/ome-process.json" 'experiments/vesuvius/r009/20261116-reader-impact01/probe.py' ome "$run/reader-inputs.json" "$run/ome.json" *> "$run/ome.log"
if ($LASTEXITCODE -ne 0) { throw 'OME-Zarr probe failed' }
python -I -B tools/research/run_windows.py "$run/reader-check-process.json" "$base/check.py" ome $tag
```

ビルドから繰り返す場合は容量を確認し、最初の `replay $tag run03` を `$tag` に置き換える。[run03の各描画開始原票](run03/)にrendererの引数一式がある。元は `build/bin/vc_render_tifxyz.baseline`、修正後は `build/bin/vc_render_tifxyz`。`configure-start.json` と `*-build-start.json` に実CMake引数、`renderer-deps.txt` に実コンパイル時に参照したヘッダー、`baseline-elf.json` と `fixed-elf.json` にELFと動的依存の実体・SHA-256を記録する。`replay` は既存runのELF・共有ライブラリを再照合し、実証に使った描画処理を呼ぶ入口で、今回の実証はrun03の各描画1回。

## 固定した入力と資源

PHerc0139 TIFXYZ面 `20260317000000-w035_2026031718`、CT `20250728140407` のL0 9.362 µm。公開キャンバスXYWH `(2176,1408,64,64)`、28層、層間1、scale 1、bicubic、法線反転、圧縮なしのZarr v2 uint8。[R129の来歴](../../r012/20261113-known-ct-control01/README.md) · [開始時の入力ハッシュ](run01/inputs.json)

初期見積は既存C:空き約7.9 GB、今回C:増分2.2 GB以内。R160の通常ビルド実績は653秒、作業割当1.63 GB。今回のnative上限はC:増分3 GiBと空き2 GiB、CPUと数値/OpenMP各1、AS 4 GiB、core 0。CMake 600秒、通常ビルド1800秒、増分300秒、各描画90秒。D:とR160作業先はビルドのマウント名前空間でread-only、ネット名前空間のインターフェースはloのみ。システムへの依存インストール、新CT、GPU、クラウド支出、外部書き込みは0。

固定API応答、上流指示、取得本文300 blobの計9,449,765 Bを保存した。300 blobの本文は6,925,794 B。最初の疎通確認では同じtree APIを出力破棄で取得しており、計量外のその一回用に8 MiBを保守計上した。対象以外のモノレポ本文は取っていない。[取得計画](upstream/source-plan.json) · [取得原票](upstream/download.json)

初回153.690秒は固定mainに必要な `concurrentqueue` が見つからず終了1。WSL Ubuntu noble/universeの `libconcurrentqueue-dev 1.0.4+ds-1` amd64 61,138 Bを既存APT目録のSHA-256と照合し、新規WSL作業先へ展開。標準CMakeの `-Dconcurrentqueue_DIR=...` を追加した。2回目209.812秒は再構成で `blosc2>=2.13` が見つからず終了1。上流の依存差分からBlosc2とvc-delta3dの要求をまとめて特定した。[初回構成失敗](run01/configure.log) · [2回目構成失敗](run02/configure.log) · [Ubuntu公式concurrentqueue](https://archive.ubuntu.com/ubuntu/pool/universe/c/concurrentqueue/libconcurrentqueue-dev_1.0.4+ds-1_amd64.deb)

Blosc2にはnobleの `libblosc2-dev` と `libblosc2-2t64 2.13.1+ds-1.1ubuntu2` amd64（430,118 B）を使用。公式debのSHA-256、実行依存（既存libc6・liblz4-1・libzstd1・zlib1g）、局所 `pkg-config` の実体を照合した。vc-delta3dは上流 `v0.3.2` / `427248122a088bad7d5b1209ea55c311de3378bb` の公式tar（175,548 B）を取得し、121本文を固定Git blobと照合した。これらの局所展開・照合は壁0.46秒、ユーザーCPU 0.11秒。run03はrun02の途中構成cacheから続行し、別名で原票を残した。構成累計上限を主担当判断で900秒に変更し、3回合計743.695秒で構成を完了した。計量分通信の総計10,155,948 B。tree疎通の予約込みで64 MiB以内。[依存実物](run03/additional-dependencies.json) · [成功時の構成原票](run03/configure-process.json) · [vc-delta3dの公式タグ](https://github.com/ScrollPrize/vc-delta3d/releases/tag/v0.3.2)

baselineの序盤で同名のreader 12出力がR160の計54.69秒に対して258.17秒かかった。作業継続の価値と完了済み出力を踏まえ、主担当がbaselineの期限を開始から3600秒へ延長した。初回タイマーの1800.095秒で236/247工程を終え、プロセスグループを回収した。CMake graphと固定ソースを再照合し、同じ作業先で残り11工程を125.034秒で完了した。両プロセス壁時間は計1925.129秒。初回はGNU time自体も回収したため最終RSS/CPU値は欠測。続行分は最大RSS 1,889,284,096 B、ユーザーCPU 105.71秒、システムCPU 16.87秒。vc-delta3dのコンパイル・リンクはNinjaの30工程で壁15.472秒（CPU時間はbaseline内のため単独計測なし）。[初回プロセス](run03/baseline-build-process.json) · [残11工程](run03/baseline-build-continued.log) · [続行プロセス](run03/baseline-build-continued-process.json)

R123の3ハンクは既存パッチとバイト一致、SHA-256 `cca4821117c279939113e773c96c56c19d9d9b42c36bc8f1db1c531af63b9146`。差分は `volume-cartographer/apps/src/vc_render_tifxyz.cpp` のみ。元ELFは `045bae4f353b610a75d631a577b012a881edcfdf0d0edd1e4b63a6337fa49ab1`、修正ELFは `b9d909432e28ab84e0cb38c137dad3a8b141378ce09a1b46cb70f5ab8ea1fd4c`。両方の動的ライブラリ実体71件のpathとSHA-256が一致し、増分後も元ELFのSHA-256は同じ。元renderer TUとリンクが計49.248秒のため増分上限は300秒。実増分は38.627秒、最大RSS 1,639,174,144 Bで、製品TUのコンパイルは1件、リンクは1件。Qtの自動確認で生成mocソースと生成mocオブジェクトのmtimeは更新されなかった。[単独パッチ](run03/pyramid-metadata.patch) · [元ELF](run03/baseline-elf.json) · [修正ELF](run03/fixed-elf.json) · [増分実行](run03/incremental-build.log) · [自動生成ファイルの照合](run03/incremental-commands.json)

Ninja `-n` はCMakeのglob確認を実行できず再構成を予告し、試験ランナーが増分コンパイラ起動前に停止した。既存graphを保ったまま実ログを確認する形に変更した。実際の増分ではglob確認とQt MOC/UIC確認が走った。最初の実ログ判定はQtの確認命令を許容しておらず、終了0の実増分後に停止した。確認命令と製品TUのコンパイルを記録し、生成mocソースと生成オブジェクトのmtimeが増分開始前であることを確かめた上で、そのELFから描画を続けた。[事前判定の停止](run03/baseline-continuation-failure.json) · [増分後の判定停止](run03/incremental-autogen-gate.log)

native完了時のR246追加実割当は失敗構成の作業も含めWSL 1,718,312,960 B、Windows上の原票21,340,160 B、計1,739,653,120 B。C:空き4,894,015,488 B。新しいCT・GPU・追加費用・外部書き込みは0。Windowsでの本文取得は本文量で管理し、CPU affinityは指定しなかった。nativeとWindows reader/比較はCPU 1と数値スレッド1を指定し、4 GiB上限を適用した。[資源・入力・ライブラリ最終照合](run03/native-complete.json)

## 主担当による再現入口の確認

本人への引継ぎ前に、保存ELFをread-onlyで再利用するreplay入口をrun04で一度実行した。5描画すべて終了0、計1.696秒、native比較も終了0。新ビルドなし。run03のOME実行結果は不変で、同じreaderは重ねて再実行していない。これはAIの追加確認で、本人の実行ではない。受理するrun名はrun+数字のみで、本人用は未使用のrun05以降にする。
