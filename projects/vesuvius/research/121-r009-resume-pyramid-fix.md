Status: resolved
担当: 研究・実装（2026-11-13、r009_resume_fix）
Blocked by: 120

# R009: 単一partのZarr再開で欠けたピラミッドを初期化する

## 依頼

2026-11-13（日本時間）。研究120で、`vc_render_tifxyz --resume` は出力先が存在しない初回とL0のみの出力で、L1を開けず終了1になると実証した。通常の同条件は成功してR115の全14ファイルと一致する。小さい修正で新規・部分・完成済み出力の再開を成立させる。

元ソースは研究119保存のblob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6`。製品差分は元rendererに対して作り、観測差分やR006試作を混ぜない。R007とは別の差分にして適用共存を確認する。既存のZarr writer/pyramid能力を先に調べて借り、不要な新APIや階層計算の複製を増やさない。ただしWriter::createのoverwrite=trueは削除を行い、falseでもメタデータを書き直すことがある。正常な既存L0や既存下位レベルのデータ・形式を壊す呼出しを避ける。resume時に既存L0と異なる既定圧縮設定を押し付けない。既存のmulti-part/--preの契約とpyramid無効指定を維持する。

固定入力はR115 C: CT、128×128・101層、正常対照は研究120のC: normal.zarrとR115元出力。失敗の生票と元バイナリは `experiments/vesuvius/r009/20261113-resume-reproduction01`、`.work/r009-resume-reproduction01/run01`。新規出力は別のC:作業先へ、D:依存物・元ソース・過去runは読み取りのみ。

実際のCLIで新規通常、新規--resume、L0のみの再開、途中でピラミッド初期化が中断した形（L0メタデータのみ等）、完成済みの再開を確認する。既存レベルが一部ある場合も壊さず補完できること、既存L0のSHAと更新時刻を維持することを確認する。完成出力の各レベルのshape・dtype・画素とOME属性が同じ対照になることが判定軸。pyramid無効とmulti-part/--preは必要最小限の回帰で確認する。実行結果を保存するための手順は再利用できる形で残す。新しい取得や全面描画、性能優位の主張は不要。

CPU1、AS4GiB、ビルド合計300秒、ネイティブ試験の合計120秒、C:作業128MiBを上限。core dump無効・ネットワーク分離。既存の単一TUビルド条件を借りる。追加クラウド見積0円、CT取得0、依存導入なし。範囲が膨らむ、上限、別の原因、既存APIでは正常なデータを保持できない等の問題は、根拠を保存して主担当へ戻す。

モデル/effortはgpt-6.1-sol / xhigh。再現と既存ビルド手順は確定しているが、部分出力と既存メタデータの保持・再作成の境界を設計するため、この依頼では高い検討量を選ぶ。追加subagent・外部送信禁止。依頼を保存し、結論・差分・試験・限界・費用を追記してresolvedへ。lab登録候補を主担当に返す。製品採用は別担当の独立検証後とする。

## 結論（2026-11-13 JST）

［一次・実行］単一partの `--resume` が、欠けたZarrピラミッドを補完するよう修正した。固定CT・128×128・101層では、新規通常、新規resume、L0のみ、ピラミッド初期化途中、完成済みの5ケースが終了0。いずれも研究120とR115の正常対照と、L0–L5のshape、dtype、復号画素、OME属性、および全14ファイルのSHA-256が一致した。既存L0ファイルのSHA-256と更新時刻を維持した。[試験原票](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/result.json)

［一次・実行］既存L0がgzipレベル7・ドット区切り、L1が無圧縮・スラッシュ区切り、L3が元のbloscの状態でも、L2・L4・L5がL0の設定で作成された。既存レベルのメタデータのSHA-256と更新時刻、既存チャンクのSHA-256を維持し、全6レベルの復号画素とOME属性は対照に一致した。`--pyramid false` はL0を維持しL1–L5を作らず、multi-partは `--pre` を要求した。`--pre` 後のpart 0も対照の14ファイルに一致した。[混在codecの前](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/mixed-codecs-resume-before.json) · [実行後](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/mixed-codecs-resume-after.json)

## 根拠・詳細

- ［一次・コード］元の `createPyramidLevels` は `Writer::create` を各レベルで呼ぶ。`overwrite=false` でも配列メタデータを書き直すため、単に `!resumeFlag` を外すと、保存済みの圧縮設定や区切りを変えてしまう。既存の階層計算に既存配列を保持するoverloadを加え、単一part再開時だけ `Writer::open` 済みL0の `createOptionsLike` を渡す。既存配列はshape・chunk shape・dtypeを照合し、メタデータ作成をスキップする。元の3引数の呼び出しとシンボルは維持した。通常実行、`--pre`、multi-partの既存初期化経路も従来どおり。[ネイティブ製品差分](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid.patch)
- ［一次・ビルド］研究119のrenderer blob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` を基点とした。R007とR009は両方の適用順で同じソースになった。変更したrendererとpyramidの2翻訳単位のみC:でビルドし、両方のコンパイラ依存ファイルで変更ヘッダーが選ばれたことを確認した。C:の2オブジェクトを既存D:ライブラリとリンクし、実行ファイルの3つの `createPyramidLevels` シンボルを確認した。[適用結果](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/source.json) · [ビルド結果](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/build-result.json)
- ［一次・差分照合］`vc_reader/AGENTS.md` の指示に合わせ、Pythonの既存 `create_pyramid_levels` に `preserve_existing=False` を追加する薄いバインディング、capability mapの追記、回帰テストを別添した。既定値は従来のC++呼び出しを通る。ネイティブ差分に続けて適用でき、Pythonの変更2ファイルは構文解析に通った。WSLにnanobind、Python開発ヘッダー、NumPy、pytestがなく、バインディングのコンパイル・pytestは未実行。[Python差分](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/resume-pyramid-python.patch) · [適用・構文確認](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/run01/python-patch-check.json)

## 取得の経路・限界・費用

再確認はWSLで `build.py runNN`、`check.py runNN` の順に新しい同一ラベルを指定する。実測バイナリと固定出力は `C:/dev/kensyoukin/.work/r009-resume-pyramid-fix01/run01` に残した。[再試験手順](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/README.md) · [lab登録候補](../experiments/vesuvius/r009/20261113-resume-pyramid-fix01/record.json)

試験対象は固定のZarr v2・uint8・1タイル。multi-partの実描画は2パート中で行を持つpart 0。L1以降のチャンクとrootのOME属性は既存処理で再計算されるため、下位チャンクとroot属性の更新時刻は比較条件から外した。既存の `.zarray` とL0全ファイルの更新時刻は照合した。他入力、実際の強制中断、全体ビルド、Python実行、R007合成版の実描画は未検証。製品採用は別担当の独立検証後。

CPU 1、AS 4 GiB、core dump 0、ネットワーク分離。ビルド220.718秒で最大RSS 1,583,583,232 bytes。ネイティブ10プロセスの壁合計35.040秒、試験全体81.260秒、最大RSS 96,739,328 bytes。全プロセス回収済み。C:作業42,161,084 bytes。固定入力・両正常対照のハッシュは試験前後で一致。D:は読み取りのみ。追加CT・依存導入なし、追加クラウド支出0円。

## メモ

- 2026-11-13、着手。保存rendererとD:のSHA-256が一致。既存createPyramidLevelsは各段で無条件にWriter::createを呼び、overwrite=falseでも既存メタデータを更新する。既存3引数の動作を維持し、単一part resume向けに欠落時だけ作成する選択肢を追加する。L0の保存形式はcreateOptionsLikeで受け継ぐ。主担当が変更対象2 TUのみのビルドを了承。実装と試験は未確認。
- 同日、差分・再試験手順・10プロセスの原票をC:へ保存。Python別添は適用と構文を確認。独立検証と採用判断は主担当へ引き継いだ。
