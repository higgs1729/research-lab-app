# 検証実行の経過

初回はCTの読込と独立補間計算後、TIFFをtifffileで読む段階で `ValueError: <COMPRESSION.LZW: 5> requires the 'imagecodecs' package` により終了した。result.json作成前。元データの不一致ではなく、検証側の既定Pythonパスには隔離したimagecodecsを加えていなかった。

依存を追加せず、既存PillowのLZW読取を使用するよう検証コードの読取部だけ変更して再実行する。描画・入力・比較条件は同じ。
