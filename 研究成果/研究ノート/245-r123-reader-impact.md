Status: resolved
担当: 研究（R245 Sol/xhigh）

# R123のピラミッド無効時のメタデータ修正は実readerで何を変えるか（2026-11-16）

## 依頼

本人は応募を上流villaへのPRの形にする方針を決め、Claudeは最初をR123のOMEメタデータ修正に絞る案を出した。主担当は採用。`board/posts/20261116-1034-claude-upstream-pr-direction.md` のaを実行する。R123/R124は実CTの`--pyramid false`出力について、旧`.zattrs`が存在しない階層1〜5を列挙する不整合と修正後L0だけになることを実証したが、既存readerでの影響は未確認。

問いは、保存済みの修正前/後出力を実際に使われる既存readerへ渡すと、読込・表示用配列・エラー/警告にどんな違いがあるか。独自の厳格validatorを作って害を成立させない。実readerが無視して成功するならその結果をそのまま残す。reader名と固定版、入力同一性、再現コマンド、端末出力と読み込まれた配列の事実を残す。利用可能なreaderと入力は自分で確認する。例はVC3D、vesuvius Python reader、OME-Zarr Python/napari経路。大きい依存環境やGUIを作ること自体を目的にしない。

保存先は `experiments/vesuvius/r009/20261116-reader-impact01/`。既存根拠は上書きせず、読み出しが書込を伴う場合は新しい出力先へコピーする。Dは読取のみ、DでGit禁止。重い処理はCPU1/commit4GiB（Windowsなら`tools/research/run_windows.py <receipt> <script>`）、初期の実行合計10分、C追加容量上限512MiB、C空き2GiB以上。既存出力で足りるなら新render/buildは不要。新CT・GPU・有料計算・外部書込み0。通信が必要なら一次のreader配布/公式ソースに限定し取得量を残す。

参考入口：`research/123-r009-pyramid-metadata.md`, `research/124-r009-metadata-verification.md`、`experiments/vesuvius/r009/20261113-pyramid-metadata01/run01/disabled-normal-process.json`、同`old-pyramid-disabled.json`、`.work/r009-pyramid-metadata01/run01/disabled-normal.zarr`。既存ELFは同run01の`renderer`。このELFは結合版で、R123単独PRのビルド実証とは区別する。現在の上流PR #2529とresume修正は別課題で扱わない。

モデルはgpt-6.1-sol / xhighを選ぶ。既存readerの選定と実害判定に未確定部分があり、単なる決められたテスト実行ではないため。再委任なし、一件のみ。主担当が重要結果を別検証し、lab/recallと本人手順への反映を行う。担当は本票の結論・取得経路・限界を埋めresolved、必要な根拠を固定し、主担当へ小さく返す。変更したJSON入出力境界は実物小fixture一件で書出し→読み戻し→使用を先に確認する（採用監査audit-ba4944065d0b）。既存の全記録への検査追加はしない。

## 結論（2026-11-16 JST）

［一次・実行］修正前の `.zattrs` をR123修正後の保存出力へ移した対照は、**OME-Zarr Python 0.21.0の画像readerで path `1` の `ArrayNotFoundError`** になった。修正後の同じZarrは1画像ノードとL0の表示用配列を返し、全画素を読めた。ピラミッド有効の実配列6段対照も1ノードと6配列を返した。OME 0.4の自動判別に伴う `version mismatch: detected: FormatV04, requested: FormatV05` のloggingは修正前後に出る。Python warningsは0件。主担当の独立OME再実行でも、同じ例外と修正後配列を確認した。[OME結果](../experiments/vesuvius/r009/20261116-reader-impact01/ome.json) · [端末原票](../experiments/vesuvius/r009/20261116-reader-impact01/ome.log) · [独立確認](../experiments/vesuvius/r009/20261116-reader-impact01/lead-check/result.json)

［一次・実行］villa Pythonの `vc_reader` 0.1.0では、保存したR121出力と旧属性だけの対照は、groupを開くと0〜5を列挙する一方、`group.level(-1)` が最粗のL5を開いて `KeyError: no array '5'` になった。修正後は最粗としてL0を読み、ピラミッド有効対照はL5を読めた。両readerで各ケースの直接L0は成功し、全画素が一致した。villa Pythonの `group.level(0)` でも全ケースで同じ `uint8`、ZYX `(101, 128, 128)`、全画素SHA-256 `8d5f47fa26dfbc80a7c47869188bda056b49e1f5ed0d85f941a40dd80d8fc937` を得た。[villa結果と固定版](../experiments/vesuvius/r009/20261116-reader-impact01/vc.json) · [端末原票](../experiments/vesuvius/r009/20261116-reader-impact01/vc.log)

## 根拠と限界

- ［一次］R121の旧現物はL0だけを播種した `--resume --pyramid false` 試験由来で、`.zgroup` も欠く。その原状をOMEに渡すと `parse_url` が `None` を返した。欠落パスの影響の判定には、R123修正後と `.zattrs` だけが異なる対照を使った。旧 `.zattrs` はピラミッド有効対照の実物とバイト一致し、修正属性との内容差は参照1〜5だけ。全4ケースのL0の配列メタデータと圧縮チャンクはバイト一致。入力ハッシュの小JSONを保存し、再読込して現物照合に使用した。[入力原票](../experiments/vesuvius/r009/20261116-reader-impact01/inputs.json)
- ［推論］上流PRの再現例に使えるのは、同じL0に存在しない参照を足すとOMEの画像読込が中断し、それらの参照を除くとL0を読み込めるという差。保存修正後出力はR007/R121/R123結合版によるもの。R123単独のビルド、現行上流mainの実行、GUIでの描画は未検証。[再現コマンドと資源](../experiments/vesuvius/r009/20261116-reader-impact01/README.md)

## 取得の経路

R121の旧入力原票とR123完了時のファイルハッシュを先に照合した。WSL UbuntuでR125の既存実拡張と通常のパッケージ初期化を使った。OMEはWindowsの隔離先に公式PyPI wheelを取得し、既存のWindows制限runnerで読んだ。新CT・描画・ビルド・GPU・有料計算・外部書込は0。担当の計測壁時間は導入を含め172.711秒、追加作業と原票は最終照合時350,374,694 B、C空き8,263,979,008 B。ローカルで測った公式配布・公式資料の応答本文107,556,657 B。D:と過去の根拠は読取のみ。[取得・導入原票](../experiments/vesuvius/r009/20261116-reader-impact01/ome-install-retry.json)

## メモ

- 2026-11-16 [一次] R121の旧出力とR123の修正後・既定対照の実ファイルを確認。旧出力には `--resume` 試験のL0のみ播種条件に由来する `.zgroup` 欠落がある。保存現物に加え、修正後のコピーへ旧 `.zattrs` だけを移した対照を用意し、3出力のL0がSHA-256で一致することを記した小JSONを保存して読み戻した。
- OME-Zarr 0.21.0の公式配布wheel一式は取得済み。初回は展開時の保守見積595,934,662 Bが当初のC上限を超え、導入前に停止。主担当が本試験のC追加上限を640 MiBへ変更した。C空き下限2 GiBを維持し、取得済みwheelからオフラインで再試行する。
- 取得済みwheel全件のSHA-256を再照合してオフライン導入に成功した。両readerの結果JSONを再読込し、同じ入力原票のSHA、全直接L0の一致と有効対照の最粗L5の一致、実行後も全入力が不変であることを照合した。
