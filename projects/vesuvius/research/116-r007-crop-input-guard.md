Status: resolved
担当: 研究・実装（R116 Sol/high）

# R007: 不完全なcrop指定による意図しない全面描画を防ぐ

## 依頼

2026-11-12。R006は固定小領域の通常処理全体で採用基準を満たさず保留した。次の一件は研究107の予備候補、`vc_render_tifxyz` のcrop指定の確認と小さい修正にする。幅または高さを落とした指定が全面描画へ進むなら、入力を開く前に明確なエラーにする。

主担当は現行main `0080fa393724575d4f19059d91402757f9351b28` を確認した。rendererのGit blob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` は手元の試験済みソースと一致。幅・高さとも正の場合だけmanualに入る処理が残る。GitHubでcropとrendererを絞ったissue/PR検索では同じ入力検証の修正は見つからなかった（検索範囲内）。[一次資料と検索結果](../experiments/vesuvius/r007/20261112-crop-preflight01/sources.json) · [現行と手元の対応](../experiments/vesuvius/r007/20261112-crop-preflight01/source-match.json)

最初にGUI・スクリプトの実際の呼出し、CLIのhelpを確認し、不完全指定が意図された仕様か調べる。意図的な利用や既存対策が見つかれば実装せず根拠を返す。同じ入力ミスの実ユーザー報告はまだ見つかっておらず、影響を既知の現場事故として書かない。

## 最小限の仕様

正常な完全指定と全省略を保持する。すべて0の明示指定も既定の全画面指定と同じに扱い、x/y省略で原点から切る正常な使い方を拒否しない。幅・高さの片方だけが正、負の幅/高さ、非零の位置だけでサイズがない場合は早期にエラーにする。負の原点がcanvasとの交差で有効な切出しになる現動作は保持する。auto-crop、merge-tiff-parts、helpの既存用途を壊さない。

修正はrendererの引数検証に限定し、正常な描画の計算・丸め・reader APIを変えない。D:元ソース/ビルドは読み取り専用、C:にコピーしたソースと差分を保存する。R006の再利用試作を混ぜない。

## 再現と確認

保存済みPHerc0814の面で、crop128×128の引数からheightだけを落とした変更前が選ぶcanvasサイズを確認する。全面の実描画やCT取得は行わず、crop選択を記録して出力作成・サンプリングの前に終了する観測差分を別に置く。正常128×128、全省略、明示的全0、負原点を含む有効な交差、auto-cropの対照を確かめる。

変更後の不完全指定は存在しないvolume/segmentationを指定してもcropの診断で非ゼロ終了し、画像出力が作られないことをネイティブCLIで確かめる。正常128×128は保存CTだけを使って小数層を実描画し、元の対応する対照TIFFと一致を確認する。help・既存の引数エラーも必要な範囲で確認する。テストは実際の引数解析とcrop選択を通し、条件式だけを複製したテストにしない。

費用の見積は追加クラウド0円、取得0。CPU1/AS4GiB、今回ビルド合計300秒、各CLI試験30秒、正常小領域描画120秒。既存rendererの単一TU compile/linkを借り、D:依存物に書き込まない。C: fixtureはR115 `C:/dev/kensyoukin/.work/r006-zarr-whole-process01/run01/ct.zarr` が使える。既存の全101 offset coverageに含まれる範囲だけを使う。大規模ビルドや新依存を導入しない。

採用の目安は、現行の不完全指定による全面選択の再現、変更後の読み込み前拒否、正常入力と画素の維持。防いだ選択ピクセル数は示せるが、実測していないCT転送量や料金の削減を主張しない。結果は次の独立検証まで候補扱いとする。

モデル/effortはSol/highを選ぶ。既存の問題箇所・ビルド手順があり、CLI既定値と既存呼出しの解釈を含む小さい修正で、新しいアルゴリズム設計は不要なため。追加subagentは禁止。依頼を残し、仕様確認・差分・再現・検証・費用・限界を追記してresolvedへ更新する。

## 2026-11-12 作業記録

[一次・手元ソース] GUIの `CommandLineToolRunner.cpp` は幅・高さが正のときに4値を送る。ベンチの `bench_render_tifxyz.cpp` はcropを送るなら4値を要求する。MCPの `flatten.py` はcropを渡さず、既存のtraining catalogは4値を0にする例を含む。公式READMEの描画例もcropを省略している。この範囲で不完全指定に依存する呼出しは見つからなかった。旧helpの宣言は4値とも既定0で、幅・高さは互いの要件を書いていない。元CLIのhelpは環境障害で取得できなかった。

[一次・差分] 元blob `3c0d4250ea484c616f4f8e2c260f7ce2a07f99d6` を照合してC:へコピーし、crop引数をmerge分岐の直後・入力を開く前に検査する差分を生成した。幅と高さがともに正なら既存のmanual選択を通し、4値とも0なら既定値を維持する。auto-cropとの既存排他条件とcanvas交差は元の位置に残した。観測差分は別で、crop選択後にreturnし、画像出力とサンプリングへ進まない。製品差分と元版・修正版への観測差分は `git apply --check` が通った。[再現手順と差分](../experiments/vesuvius/r007/20261112-crop-input-guard01/README.md)

元バイナリの `--help` 起動でWSLが `WSL_E_DISTRO_NOT_FOUND` を返した。登録一覧とHKCUのLxssには `docker-desktop` のみ。Ubuntuの既存VHDの所在は限定した読み取り確認で特定できなかった。D:の元ソース・バイナリとC:のfixtureは確認済み。環境への変更、新規CT取得、追加クラウド支出は0。ネイティブのビルド、全面選択の再現、早期エラーと既存挙動、少数層の対照TIFF一致は未検証のため `claimed` を継続する。既存Ubuntuと依存物が利用可能になれば、上記再現手順の `run_trial.py run01` から続ける。[環境原票](../experiments/vesuvius/r007/20261112-crop-input-guard01/environment-stop.json)

## 2026-11-13 結論

[一次・ネイティブ実行] Ubuntu復元後に準備済みの `run_trial.py run01` を実行した。旧版は `--crop-height 128` だけを落とすと、PHerc0814の固定面で `(0, 0, 13600, 3440)` を選択した。意図した128×128の16,384画素／層に対し、全面は46,784,000画素／層。観測版をcrop選択直後で止めたため、全面の画像作成・サンプリング・転送の計測はしていない。実利用での発生件数は未確認。[復元確認](../experiments/vesuvius/20261113-wsl-restored01/result.json) · [選択原票](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/crop-selection.json)

修正版は、無効な8種類のZarr指定と1件のTIFF指定を、volumeとsegmentationが存在しない状態で `--crop-width and --crop-height must both be positive for a manual crop` と診断し、終了コード1、画像出力なしで終了した。元と修正版の観測で、完全指定、全省略、全0、原点省略、負原点のclip、auto-cropの6選択は一致。help、既存の引数エラー、TIFF mergeも通過した。通常CLIで実描画した128×128の3 TIFFは既存対照 `049.tif`〜`051.tif` と全ファイルSHA-256・復号画素が一致した。merge後のTIFFも中央対照と一致した。[診断原票](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/cli-missing-height.log) · [画素対照](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/summary.json)

既存R005のO0ビルド条件で1ファイルを3版ビルドした。ビルド124.694秒、描画0.532秒、最大RSSはそれぞれ1,583,865,856 bytesと78,790,656 bytes。CPU1・AS 4 GiB、D:は既存入力・依存物の読み取り、生成物はC:。追加CT取得0 bytes、クラウド支出0円。ローカル電力・モデル利用費は未算定。成果は独立検証待ちの実装候補とする。[試験結果・独立検証手順](../experiments/vesuvius/r007/20261112-crop-input-guard01/run01/README.md) · [索引用候補](../experiments/vesuvius/r007/20261112-crop-input-guard01/record-run01.json)
