Status: resolved
担当: 研究（r009_data_path_scout）

# R009: データの読込み・保存・再開に残る小さい実利用障害を一件探す

## 依頼

2026-11-13（日本時間）。月次の応募候補はR005（成分配置）とR007（不完全なcrop指定の拒否）。R006の最適化は全体性能で基準未達。研究118はHF65の線形ずれ補正の大部分が既存transferの寸法比と定数で表現できるため実装を見送った。本人の低支出・一件ずつ・複数改善を一応募にまとめる方針を維持し、今度はVesuviusのデータを取得・読み込み・保存・再開する既存経路を調べる。

現在も使われる公式ツールと利用者の一次報告から、ローカルの小さな入力や失敗応答で再現できる障害を最大2件に絞る。対象は実際の巻物処理を止める、出力やメタデータを誤らせる、または不要な繰り返し作業を生む問題。一般的な堅牢化リストや新しい監査器、些細な引数検証の追加は求めない。研究107と118の見送り一覧・既存PRを先に把握し、同じ提案の再探索を避ける。特に既存downloader PR、メモリ・cache PR、label drift案を新規成果として扱わない。

今回の目的は一件の再現試験へ進める情報だけ。現在の公式ソース/版と問題報告、既存修正の有無、具体的な発火条件、小さい再現、期待する利用者の改善、CPUとデータの見積/停止条件を短く返す。候補が明確になったら広い探索は閉じる。候補の必要性や未解決性を確認できなければ、その理由を記録して実装を勧めない。公開原文は保存するが、調査した全周辺ファイルを網羅的に集める必要はない。

この段階はソースと一次資料の読み取りに限る。新規実験・ビルド・依存導入・大きなデータ取得・有料計算・外部送信を行わない。D:は読み取りのみ。根拠は `experiments/vesuvius/r009/20261113-data-path-scout01` に随時保存し、長い本文をツール出力へ丸ごと出さない。依頼を保ち、このファイルに結論と根拠を追記してresolvedにし、lab登録候補を返す。追加subagentは禁止。

モデル/effortはgpt-6.1-sol / mediumを選ぶ。今回は既知の一次資料調査手順による限定的な問題の選別で、アルゴリズム設計や実装は含めないため。難しい実装判断が必要なら確定せず未確認点として主担当へ渡す。

## 結論

次の再現試験に渡す候補は1件。単一partの通常Zarr出力がL0だけ残った状態で、`vc_render_tifxyz --resume` がL1–L5を作成せず、再開を完了できない疑いがある。現行ソースで失敗条件を特定した。同条件の利用者報告と現行CLIの結果は未確認で、候補は予防的な確認として扱う。

## 根拠・詳細

- ［一次、2026-11-13取得］研究107と118に従い、downloaderのスケールずれ #2371/#2379、メモリ・キャッシュ #2294/#2446/#2411、HF65 label drift #2370を除外した。保存・再開の報告でも、セグメント保存でサブフォルダが消える #2222 は #2223、Open Dataの再起動後にパッチが表示されない #1466 は #1801、破損TIFFを完了扱いする #1404 は #1695 にそれぞれ同じ問題を扱うPRがある。配布繊維の取込 #2320、recompressの誤レベル選択 #2186、奇数寸法ピラミッド #2135、配布flowsnapの読込 #2458、深度とZスケールが食い違う #2107 にも同一事象を扱う提案がある。PRが見つかった時点で新規候補から外した。 [保存 #2223](https://github.com/ScrollPrize/villa/pull/2223) · [Open Data #1801](https://github.com/ScrollPrize/villa/pull/1801) · [TIFF再開 #1695](https://github.com/ScrollPrize/villa/pull/1695) · [繊維 #2321](https://github.com/ScrollPrize/villa/pull/2321) · [recompress #2199](https://github.com/ScrollPrize/villa/pull/2199) · [奇数寸法 #2415](https://github.com/ScrollPrize/villa/pull/2415) · [flowsnap #2463](https://github.com/ScrollPrize/villa/pull/2463) · [深度 #2501](https://github.com/ScrollPrize/villa/pull/2501)
- ［一次］Zarr出力が再開時にも落ちる #1673 は5月の古いコンテナでの報告。追試では同じPHerc1447の面・巻物を公式リリース `8aa507c` で描画し、Linux AppImageとmacOS版でピラミッド6階層を出力できた。#1673は11月1日に完了として閉じられた。#1220のリモート mmap は、現行の有効な読込経路としての必要性を支持する材料がなく、メンテナも別の経路で足りるとのやり取りを経て完了扱いとした。 #2500は成分が重なって上書きされる症状で、R005の扱う問題と重なるため除外した。 [Zarr出力 #1673](https://github.com/ScrollPrize/villa/issues/1673) · [リモート mmap #1220](https://github.com/ScrollPrize/villa/issues/1220) · [成分重なり #2500](https://github.com/ScrollPrize/villa/issues/2500)
- ［一次・現行コード、推論］`main` の `0080fa393724575d4f19059d91402757f9351b28` では、単一partの `--resume` が既存のL0を開き、Zarrのみの出力では既存L0チャンクをスキップする。一方、`--resume` はL1–L5の作成も省く。ピラミッドは既定で有効で、その後の処理はL1の書込先を `Writer::open` する。対象箇所を修正するPRは検索範囲で見つからなかった。ヘルプの `--resume` は既存チャンクをスキップする指定で、単一partで `--pre` を必須とは記載していない。コードには「multi-part/resume: --pre created them」のコメントがあり、初期化済みを仮定する実装。ピラミッドの欠落を許容する仕様は確認できず、実際に開こうとするため、欠落したままの成功を意図した制御にも見えない。通常実行でL0のメタデータを書いた直後からL1作成前までに中断するとL0のみの出力が残り得る。既存チャンク入りの試験治具では、それに加えて完了チャンクの再利用も確認できる。#1673の再開例は既述の別のクラッシュ。 [mainの版](https://github.com/ScrollPrize/villa/commit/0080fa393724575d4f19059d91402757f9351b28) · [CLI仕様](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L881-L888) · [L0チャンクのスキップ](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L447-L453) · [L1–L5の作成条件](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L1450-L1571) · [ピラミッド書込み](https://github.com/ScrollPrize/villa/blob/0080fa393724575d4f19059d91402757f9351b28/vc_reader/src/cpp/zarr/pyramid.cpp#L183-L195)

### 一回の再現試験案

R115の `pair-01-off.zarr`（L0〜L5、全体2,211,236 bytes）を既存対照とする。新規C:作業先の `resume.zarr` に対照の `0/` だけをコピーする。元出力に変更を加えず、コピー前後のL0メタデータ・チャンクのSHA-256を記録する。CLIはR007で使った元の未修正バイナリをC:へコピーして借りる案。依存または版の照合で使えなければ、R115のC:バイナリの試作offを予備とし、該当ソース分岐の同一性を確認した範囲で結果を扱う。R115の `measurement-order.json` の先頭argvを使い、実行ファイルと出力先をC:の今回の作業先に置き換え、末尾に `--resume` を追加する。 `--pre`、`--pyramid false`、TIFF同時出力は付けない。 [R115の固定argv](../experiments/vesuvius/r006/20261112-zarr-whole-process01/run01/measurement-order.json) · [元CLIの実行原票](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/original-help-process.json)

```bash
base=/mnt/c/dev/kensyoukin
fixture="$base/.work/r006-zarr-whole-process01/run01"
trial="$base/.work/r009-zarr-resume01" # 新規ディレクトリ
mkdir "$trial" && mkdir "$trial/resume.zarr" || exit 1
cp -a "$fixture/pair-01-off.zarr/0" "$trial/resume.zarr/" || exit 1
cp /mnt/d/kensyoukin-work/r005-ct-render01/build02/vc_render_tifxyz "$trial/renderer" || exit 1
# 既存のR115実行条件に従い、上限・隔離を付けて実行する候補
ulimit -v 4194304
OMP_NUM_THREADS=1 OMP_THREAD_LIMIT=1 TMPDIR="$trial" \
  timeout 120s unshare -Urn taskset -c 0 "$trial/renderer" \
    --volume "$fixture/ct.zarr" \
    --segmentation "$base/experiments/vesuvius/r005/20261112-pack-native01/first-trace-on01/output" \
    --zarr-output "$trial/resume.zarr" --scale 1 --group-idx 0 \
    --num-slices 101 --slice-step 1 --voxel-size 9.362 --voxel-unit micrometer \
    --cache-gb 1 --crop-x 7356 --crop-y 2272 --crop-width 128 --crop-height 128 \
    --accum 0.5 --accum-type mean --resume
```

比較は終了コード、ログの `[resume]` と `[pyramid]`、L0のSHA-256、L1–L5とOME属性の有無。L1を開けず終了し、L0のハッシュが維持されれば故障条件を確認。成功した場合は対照とshape、dtype、復号画素・属性を照合し、L0を捨てず完全出力へ戻ったか判定する。元CLIに固有の起動失敗やABI違いを除くため、必要な場合だけ同じCLI・同じ引数から `--resume` を外した新規出力を対照として先に確認する。全体CPU 1、壁120秒、AS 4 GiB、C:作業データ64 MiBを上限案とする。D:は元バイナリ参照のみ、CT新規取得0。対照が落ちる、固定入力・バイナリを借りられない、上限に達する、別のエラーに先に当たる場合に停止する。この調査では実行していない。

## 取得の経路

GitHub連携で `resume/save/load/download/checkpoint/restart/export/zarr` 等のIssueと、症状・番号に対応するPRを確認。取得した報告とPR本文、mainの版・ソース、絞り込み時の検索結果を [根拠ディレクトリ](../experiments/vesuvius/r009/20261113-data-path-scout01/) に保存した。閉鎖理由の根拠として #1673 と #1220 のコメント原文も保存した。
