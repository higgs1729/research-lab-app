# R246 主担当の確認

11月16日11:30 JST時点。ビルドと描画の成功はまだ確認していない。

- 固定元はGitHub一次APIで確認したmain `2d3fb38d33a18b257230c0bd23986436c3d4722e`。#2529はopen/draftでresume条件と試験のみを変更し、R123のwriteZarrAttrsを変更しない。
- 担当の`acquire.py`を読んだ。固定commit/treeの同一性を検査し、R160で改変したファイルを元ソースの再利用候補から除き、必要な本文だけGit blob ID・長さを照合して取得する。新元ソースを旧結合版のコピーとして扱わない。
- R123の3 hunkを読んだ。引数wantPyramid、ome.levelsの条件、normal/preの2呼出しだけ。担当の`make_patch`は変更行が保存したR123と一致することを検査する。resumeの条件変更はない。
- `run.py`の描画はR131実コマンドのELF・出力先・pyramid条件だけを今回用へ変更する。baseline-false/default、fixed-false/pre-false/defaultの有限比較で、登録済み出力は書き換えない。
- 主担当もR129 `run01/plan.json`の実S3キーとR131 `run02/normal-process.json`を直接読んだ。対象はPHerc0139 w035 `20260317000000-w035_2026031718`、CT `20250728140407` L0 9.362um、crop[2176,1408,64,64]、28層、bicubic、法線反転、uint8・圧縮なし。R245のPHerc0814 128²×101とは別の正しい来歴である。
- `check.py`を読んだ。native出力のファイル集合と目録、L0実バイト、preの未描画状態、既定pyramidの前後同一性を確認してから、凍結済みR245 readerへ新しい入力原票を渡す。読込例外を含めて全ケースを観測するので、readerプロセス全体の終了0を旧出力の成功とは解釈しない。

## 完了時の確認（12:12 JST）

担当の実際のnative出力に対して、担当の関数を使わない `lead-native-check.py` を実行し、`lead-native-check.json` にpassを保存した。false前後の全ファイル集合は同じで、異なるのは `.zattrs` だけ。意味上の差もdatasetsの1〜5を除くことだけで、両方に `.zgroup` がある。L0の114,688 byteは全一致、SHA256 `8d68bf7bbea4248bf0bf76cdd8c4707aeea70b4d95d6837e378f572698ea9630`。既定pyramidの全14ファイルも前後一致し、pre falseの3 metadataは修正後normalと一致する。ローカルPRブランチの製品ソースも試験済みfixedソースと一致した。

元・修正のELF原票を読み、71共有依存の実体パス・byte数・SHAの辞書が一致することを別コマンドで確認した。元ELF SHAは `045bae4f353b610a75d631a577b012a881edcfdf0d0edd1e4b63a6337fa49ab1`、修正ELFは `b9d909432e28ab84e0cb38c137dad3a8b141378ce09a1b46cb70f5ab8ea1fd4c`。増分実ログはglob/Qt autogen確認、renderer TU一つのcompile、linkだけで、38.627秒で終了0。baselineの1800秒終了と同じgraphの125.034秒続行を成功一回の時間に隠さず保持する。

`run03/ome.json` と実行原票を読んだ。公式OME-Zarr 0.21.0のReaderはbaselineで実在しないpath 1のArrayNotFoundError、fixedで1node/1arrayの全画素を読み込み、上記のraw SHAと一致。L0直接読みは前後とも成功。R245で主担当が別脚本から同じmetadata機構を既に再現しており、R246では追加の同一reader再実行を重ねず新しいnative出力の独立照合と実reader原票の確認を組み合わせた。OMEの版判別ログは残る。

本人の実利用、本人レビュー、GUI確認は別途であり、このAI検証から推定しない。新CT・GPU・有料計算なし。この結果は修正の実用効果と単独差分の検証で、未読文字の発見や上流採用を意味しない。
