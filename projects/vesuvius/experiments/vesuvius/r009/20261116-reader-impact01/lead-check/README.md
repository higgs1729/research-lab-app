# 主担当によるR245の独立確認

2026-11-16。担当の`probe.py`、入力記録、vc_reader/OME結果を読み、既存vc_readerの`zarr_group.py`125〜146行で`level(-1)`が正規の最粗レベル操作であることを確認した。直接L0/level(0)は旧出力でも成功するという限界を保持する。

`check.py`は担当の関数を使わず、同じ公式OME-Zarr Readerを直接呼ぶ別脚本。旧目録だけを移した実データ対照と修正後出力について、ファイル集合が等しく、目録以外は全ファイルのSHAが一致し、目録も欠けた1〜5の列挙以外は等しいことを確認してから読込。

- 旧目録対照：`ArrayNotFoundError`、存在しないpath 1で失敗。
- 修正後：1 node、1配列、uint8 (101,128,128)、全画素SHA256 `8d5f47fa26dfbc80a7c47869188bda056b49e1f5ed0d85f941a40dd80d8fc937`。
- 両方とも入力ファイルは不変。CPU1、commit4GiB、29.593秒、最大RSS144,945,152B、exit0。
- 実端末では両方に`version mismatch: detected: FormatV04, requested: FormatV05`というOMEのlogging診断が出た。Python warningsとは別であり、修正後に全診断が消えるという主張はしない。

検証は保存データと公式readerによるAIの実行。GUI・本人確認・現在mainにR123だけを適用したビルドの実証ではない。初回の元R121出力にある.zgroup欠落をR123の効果として数えていない。
