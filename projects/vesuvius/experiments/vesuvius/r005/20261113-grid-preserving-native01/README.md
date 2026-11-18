# R005 元の格子を保つネイティブ成分配置試作

[研究150](../../../../research/150-r005-grid-preserving-native-prototype.md)の原票。試作の `--pack-components-preserve-grid` は、元のUVから既存の式で固定小数点へ丸め、成分ごとにX方向へ整数セル移動する。走査範囲も同じ整数で移す。描画には既存 `UvGridRasterizer` の同じ整数辺判定・面順・重心計算を使う。出力範囲と元写像の寸法を分け、許容範囲を超えるとエラーで終了する。Yは元の位置。出力TIFXYZのXYZと名目scaleに既存形式を使う。既定と `--pack-components` が独立した従来の経路に入り、両flagの同時指定は拒否する。

## 固定ソースとビルド

- `grid-preserving-prototype.patch` の基点は、R148固定ソースのSurfaceMeshingヘッダー・本体と、R005既存公開パッチ適用後の `flatboi.cpp`。既存の公開差分に続けて試作差分を適用する。`observation.patch` は試作適用後に重ねる。双方の適用結果を `source-sha256.json` に保存した。
- ビルド用ソースは `.work/r005-grid-preserving-native01/product/` と `trace/`。`stage.py` はそこにある試作の原文と凍結済み元ソースから差分と観測版を生成した。新しい作業ディレクトリにソースを再作成する場合は、元ソースへ上記の差分を順に適用し、`source-sha256.json` と照合する。
- `build01` 時点のC:コピーでは既存コメントの `²` が文字化けしていた。元の文字へ戻し、該当一行を除いた試作差分とソースSHAを上に置いた。`comment-encoding/` に実測時の差分・ソースSHAと、既存コンパイル条件による両版のコメント除去後前処理出力が各々バイト一致した記録を保存した。実測ELFは `build01` のもの。
- `UvGridRasterizer` のインスタンスレイアウトは変わる。隔離ELFではオブジェクトを生成するflatboiと全メソッドのSurfaceMeshingの2 TUを同じ変更済みヘッダーでビルドし、新定義を実行ELFへ直接リンクした。D:の既存 `libvc_core` 等はその他の依存に用いた。ELFがクラスの実定義を持つことと、両TUの `.d` がC:のヘッダーを指すことを確認した。全体配布でこのヘッダーの旧レイアウトを使うバイナリ（別ELFの `vc_obj2tifxyz` など）へ、新しい共有ライブラリだけを差し替える使い方は未検証。今回の作業は隔離flatboiのみ。[実行ELFのシンボル](build01/abi-executable-definitions.log)

## 再実行

PowerShellから `C:/dev/kensyoukin` で実行する。新しいタグを指定する。`build01` は既存の成功したビルドを再利用するときのタグ。

```powershell
$r150 = 'experiments/vesuvius/r005/20261113-grid-preserving-native01'
$wslEntry = "/mnt/c/dev/kensyoukin/$r150/native_trial.py"
wsl -d Ubuntu --exec python3 -B $wslEntry build build02
wsl -d Ubuntu --exec python3 -B $wslEntry run run03 build02
$r103 = 'experiments/vesuvius/r005/20261112-ct-render01'
$relative = '../20261113-grid-preserving-native01'
python -B "$r103/run_windows.py" "$relative/verify03-process.json" "$relative/verify.py" run03 verify03
```

`native_trial.py` は固定D:ソース・CMakeの既存コンパイル/リンク・ライブラリを読み、C:の隔離ディレクトリにのみコンパイル・リンク・実行出力を作る。CPU affinity 1、数値ライブラリ1スレッド、AS 4 GiB、core 0、ネットワーク分離。計測上限はビルド600秒、1回の試験セット300秒。固定入力とバイナリをSHA-256照合する。失敗した実行先のログを保存し、新しいタグで再開する。

## 観測と判定

観測版の `output.obj_uv_diagnostics.json` の `source_grid_uvs` は配置前の元UV。`grid_packing_vertex_components` と `grid_packing_component_order` は元頂点の成分IDと配置順。`raster_trace.json` の `source_grid_shape_yx`・元UV boundsと、元面ごとの `face_shift_x_cells` が対応する。`owner_weights_row_major` は元面IDが非負の所有セルだけを行優先で並べ、整数辺判定が必要とする頂点順にC++が実際に使ったfloat32ウェイトを保存する。`verify.py` は元格子と入力三角形から既存の固定点計算でウェイトを再構成し、実出力XYZ・所有元面・拒否記録を照合する。露出した点は移動先XY、移動前格子XY、元面ID・成分を保存する。

現行flatboiの `.obj` はレポート名の基点で、配置済みUVを持つOBJは生成しない。SLIMのenergyとヒートマップは元UVの段階に属する。通常のTIFXYZ以外の対応情報は観測版にのみ保存した。下流の曲面補間・CT、文字判読、未検証入力の一般化はこの実験の対象外。

## 実行結果と履歴

- `run02/` は固定二面の新モード、第一面の既定・既存pack・観測なし新モードの生出力。`verify-all.json` は元格子との全数照合・露出点全件・既定/従来動作と観測のSHA比較。`build01/` は2種類のELFの作成条件・SHA・D:依存の前後一致、`manifest.json` は成果一式のSHAを含む。`record.json` はlab登録候補。
- 初回の差分生成はWindows既定のcp932による読取で停止した。`stage.py` でUTF-8を明示して生成した。元コメント一行は上記の照合後に差分から除いた。
- `run01` は `--help` の終了コードを1と仮定したため、実際の正常終了0でランナーが止まった。元面の実行は `run02` のみ。二面目の照合は保存診断に `fine_positions` キーがなく初回停止した。失敗ログを保管し、二面の元頂点を別の固定入力配列 `X` へ照合する検査で完了した。製品出力の再生成は行っていない。
- コンパイル・リンク77.694秒、コメント修正の前処理照合24.395秒、ネイティブ試験202.518秒、最終照合3.148秒。コンパイル・リンク最大RSS 1,571,307,520バイト、ネイティブ最大RSS 1,029,238,784バイト。追加取得0バイト、クラウド支出0円。
