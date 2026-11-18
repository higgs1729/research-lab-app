# R009 再現手順

## 差分の確認

現行 main の確認対象は 14d4e725df8b569e6fc8ceb3c04d130f705c1565。C:\dev\kensyoukin\.work\r009-upstream-20261113 は対象7ファイルと規約4ファイルだけを収めた適用済みの部分作業ツリー。Git の index に固定元、作業ツリーに適用後を置いた。PowerShell で研究リポジトリから確認する。

~~~powershell
$w = 'C:/dev/kensyoukin/.work/r009-upstream-20261113'
$p = 'C:/dev/kensyoukin/experiments/vesuvius/r009/20261113-upstream-preparation01/R009.patch'
git -C $w apply --cached --check --whitespace=error $p
git -C $w diff --check
git -C $w diff --stat
git -C $w apply --reverse --check --whitespace=error $p
~~~

現行 SHA が既存の上流リポジトリにある場合は、別の空き C: パスへ作業ツリーを作って適用できる。上流リポジトリのパスは実環境に合わせる。

~~~powershell
$villa = 'C:/path/to/existing/villa'
$trial = 'C:/dev/kensyoukin/.work/r009-author-review'
git -C $villa worktree add --detach $trial 14d4e725df8b569e6fc8ceb3c04d130f705c1565
git -C $trial apply --check --whitespace=error $p
git -C $trial apply --whitespace=error $p
git -C $trial diff --check
~~~

## 保存済み実CTからの再開

既存の Ubuntu WSL 環境で、run146review01 が未使用であることを確認して PowerShell で実行する。既存R132の検証器は実停止出力を新しい出力先へ複製し、固定CT・面・ELFをハッシュ確認して三回の再開を比較する。追加停止や再ビルドは発生しない。

~~~powershell
wsl -d Ubuntu --exec python3 -B /mnt/c/dev/kensyoukin/experiments/vesuvius/r009/20261113-interrupted-verification01/verify.py run146review01
~~~

修正前の終了1と L1 不在、修正版の終了0と正常14ファイルの一致が比較点。二つの既存ELF・同一CT・同一設定を指定した正確なコマンドは各 process.json の command 配列にある。手動確認時は保存済みの L0 メタデータのみの状態を出力ごとに別々に複製し、--zarr-output をそのコピーに向ける。正常出力や保存途中状態を入力先のまま再開しない。撮影するときは実際に実行した端末で失敗と成功を記録する。

- [修正前のコマンドと終了値](../20261113-interrupted-verification01/run01/old-resume-process.json) · [修正前ログ](../20261113-interrupted-verification01/run01/old-resume.log)
- [修正後のコマンドと終了値](../20261113-interrupted-verification01/run01/before-pyramid-arrays-process.json) · [修正後ログ](../20261113-interrupted-verification01/run01/before-pyramid-arrays.log)
- [途中状態の出力パスと固定境界](../20261113-interrupted-render01/run03/before-pyramid-arrays-gdb-config.json) · [独立比較結果](../20261113-interrupted-verification01/run01/result.json)
- [ピラミッド無効の通常描画](../20261113-pyramid-metadata01/run01/disabled-normal-process.json) · [ピラミッド無効の --pre](../20261113-pyramid-metadata01/run01/disabled-pre-process.json) · [実Python拡張の隔離試験手順](../20261113-python-validation01/README.md)

R132の既存実行は R007/R009 結合版の証拠。実CTを使って上流提出候補そのものを確かめるときは、同じ固定 main から修正前と R009 適用後を別々にビルドし、保存した設定を使って双方の実行を確認する。上流の依存案内は固定 SHA の [Volume Cartographer の手順](https://github.com/ScrollPrize/villa/tree/14d4e725df8b569e6fc8ceb3c04d130f705c1565/volume-cartographer) を参照。
