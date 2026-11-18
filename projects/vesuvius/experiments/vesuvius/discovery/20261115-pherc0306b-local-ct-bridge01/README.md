# R228 native CT bridge check

Result: H0 (V5Rc d=0) versus H1 (the U5 L1-side proxy) remains unresolved. The predeclared stopping rule closes repeated local geometry diagnostics for this candidate. No new letter, ink claim or correction.

Native XYZ bounds are inclusive X2952..3312, Y3792..4016, Z8336..8424. `native-cube-zyx.npy` is uint8, shape (89,225,361), at 8.64 um/voxel, with complete support and no interpolation/fill. Origin is ZYX (8336,3792,2952).

Open `sheets/Z-01.png` through `Z-10.png` in order: all 89 consecutive XY planes, X right and Y down, native 1:1. Then `sheets/X-U2-01.png`, `X-U3-01.png`, and `X-U5-L1-01.png` through `03.png`: 39 YZ planes, Y right and Z down, displayed 2x nearest. Each sheet lists exact plane coordinates. Empty final-page cells contain no data and are not CT pixels.

`raw/` contains all 128 native PNGs. `enlarged/` holds eight fixed 3x nearest pairs, raw left and geometry marks right. Cyan points mark the V5Rc reference path only when the point rounds to that native fixed-axis plane; pink marks the single approximate L1 seed. There are no off-plane projected lines. Pixel brightness remains DN 0..255 in all artifacts. When an application scales the PNG, use its 100% view to preserve the stated display scale.

`plan.json` and `fixed-path.json` were frozen before new CT acquisition/rendering. Six source chunks from R226 were reused; three missing chunks (6 MiB) were acquired with the existing R204 HEAD/GET reader. `input-references.json`, `ct-acquisition.json`, and `stack-result.json` retain provenance. `visual-review.json` separates observation from the two hypotheses. The parent froze `lead-visual-review.json` before receiving the agent's verdict and independently assembled the full cube in `lead_verify.py`; `lead-numeric-check.json` reports exact equality.

Reproduction entry points are `prepare_plan.py`, `acquire_missing.py`, and `render_stack.py`. Their exclusive-create outputs intentionally prevent overwriting this saved run. Bounded runs used `python -X utf8 -B tools/research/run_windows.py <new-log> <script>` with CPU1 and 4 GiB process commit. Registration is left to the parent.
