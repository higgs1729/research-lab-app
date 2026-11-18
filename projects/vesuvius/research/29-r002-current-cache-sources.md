# R002 永続ディスクキャッシュの容量制御は上流で実装済み

2026-11-11 19:15–19:17 JST。ScrollPrize/villa の公開 GitHub 資料とコードを取得した。取得時の `main` は `c86cbd14bb34e0124684d3d97b03b310c947819a` で、R001 のコード取得時のコミットと同じ。リモート参照を `git ls-remote` で確認した。Issue・PR・コメントとコミット固定のコードは [取得記録](../experiments/vesuvius/r002/20261111-source-review/manifest.json) に保存した。

## 判断

**R002は不採用。** CLI 描画で永続キャッシュがSSDを埋める問題に対し、[#2290](https://github.com/ScrollPrize/villa/pull/2290) がディスク容量上限と空き容量下限を適用した。2026-11-01 15:36 UTCにマージ済み（[マージコミット](https://github.com/ScrollPrize/villa/commit/ecb10eaae1cc297d6e080dc0b77006001be6673c)）。PR著者は空のキャッシュから連続で3本を実描画し、1 GiBの設定で最終キャッシュ量が約12 GBから約1 GBになったと報告した。これは当方の再実測ではない。

## 現行 main の照合

- `vc_render_tifxyz` はリモートZarrを `Volume::NewFromUrl` で開き、`sourceOpenOptions()` を実際のピラミッド読込に渡す。設定は `VC3D.ini` の `[perf]` から取得し、`remote_cache_max_gib` と `remote_cache_min_free_gib` を同じキャッシュルートのオプションに設定する。既定は容量上限なし、空き容量下限20 GiB。レンダラーの `--cache-gb` はRAMの設定。 [レンダラー](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/volume-cartographer/apps/src/vc_render_tifxyz.cpp#L1136-L1162) · [Volume](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/volume-cartographer/core/src/Volume.cpp#L504-L519) · [設定の読み込み](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/volume-cartographer/core/src/RemoteCacheSettings.cpp#L224-L272) · [既定値](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/volume-cartographer/core/include/vc/core/util/RemoteCacheSettings.hpp#L11-L17)
- `render_ink.py` は `-j` で複数のレンダラーを起動できる。現在の `vc_reader` は同一キャッシュルートのSQLiteインデックスをプロセス間で共有し、登録とFIFO回収をトランザクションで直列化する。チャンクが利用可能な予算を超える場合はディスクに保存せず配信する。空き容量下限に達した際も、チャンクのネットワーク読込を継続しながら保存を控える実装になっている。設定の適用単位はキャッシュルート。並行時の実効上限やI/Oは今回測定していない。 [ラッパー](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/spiral-fitting/render_ink.py#L592-L624) · [予算設定の適用](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/src/cpp/sources/caches.cpp#L298-L314) · [SQLite共有](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/src/cpp/disk_cache.hpp#L22-L71) · [保存と回収](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/src/cpp/disk_cache.hpp#L119-L152) · [空き容量下限](https://github.com/ScrollPrize/villa/blob/c86cbd14bb34e0124684d3d97b03b310c947819a/vc_reader/src/cpp/disk_cache.hpp#L520-L532)

## 関連する既存作業

- [#2294](https://github.com/ScrollPrize/villa/issues/2294) は取得時open。ディスクの指摘は旧コミット `322cb08` 時点。コメントの試作にはRAM用フラグも含まれたが、現在openの [#2446](https://github.com/ScrollPrize/villa/pull/2446) は後処理のRAMだけを扱う。PR本文がディスク側を #2290 で対応済みと明記し、RAM用フラグもPRから除外した。取得したPRの議論は自動投稿のみ。 [初期試作のコメント](https://github.com/ScrollPrize/villa/issues/2294#issuecomment-6486484831)
- [#2478](https://github.com/ScrollPrize/villa/issues/2478) は取得時open、コメント0件。描画前に取得量とキャッシュ済みチャンク数を見積もる提案。マージ済みの [#1905](https://github.com/ScrollPrize/villa/pull/1905) は先読みをサンプリング対象チャンクに絞る改善。いずれも #2290 の設定による容量制御とは別の機能。

この判断は公開資料と静的なコード照合に基づく。実装、ビルド、実データ取得、実行、外部投稿は行っていない。
