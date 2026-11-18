# R211の実行と順位の契約

- R210の凍結manifestを最終 next-plan.json のハッシュ根拠に使う。R210 lead-plan-review.json の計画SHAは説明注記追記前。入力契約と検出器はレビュー時SHAと一致。新PNGと12借用PNG、箱資料のSHAを前検査する。
- 固定 run_map の finalize 入口で1始まりの元候補indexと丸め前の軸を記録し、元の finalize へ委譲する。検出・score計算・候補採否は固定ソース。両順位の同点はこの同じ元index順。zmeanがNoneの候補は最後。polygon境界上の箱中心は含む。無向軸差は丸め前の値を使う。
- 統計はfloat32のPNG/255、CT正値マスク、二枚の等重み、各標準偏差に1e-6。図は元uint8を維持。上位3の和集合を面/順・元indexで整列後、乱数seed 20261114で一回シャッフルする。番号付き図に順位を載せない。長い領域は縮小全体図を原寸タイルと区別する。
- tools/research/run_windows.py のCPU1・commit4GiBに外側300秒を加える。保存先全体を各カード生成後に512MiBと照合。三つの入力面の検出は計5回、既存コードの一実行。外部計算・CT取得・推論なし。
