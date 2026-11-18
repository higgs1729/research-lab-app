# PHerc1203 Readability Atlas

**Where is a sealed Herculaneum scroll most likely to be readable — *before* anyone spends effort segmenting it?**

A CPU-only diagnostic for the [Vesuvius Challenge](https://scrollprize.org). It measures, per location
in a scroll's CT volume, whether the local geometry could yield a readable single papyrus sheet in the
62-layer depth window the ink model consumes — no segmentation, no GPU, no ink model. Applied to
**PHerc1203** (the finest-scanned scroll still sealed and eligible for First Letters), calibrated
against **PHerc1667** (a scroll already virtually unwrapped and read end-to-end).

> **Result in one line:** PHerc1203 is mostly packed too tightly to read today, with rare readable
> pockets — and the public `auto_grown` segmentation surfaces all sit in the dead zones. The single
> best pocket is *comparable to or better than* known-readable PHerc1667 material under this pipeline.
> This is a map of readability *potential* (geometry), **not** a claim that any letters were read.

## The metric

For each surface column, peak-center a 62-layer window on the brightest band along the local normal.
A column is **readable-class** when:

- **occupancy** ≤ 0.5 — the papyrus does not fill the whole depth window (there are dark inter-sheet gaps), and
- **band-prominence** ≥ 0.55 — there is one clear bright band, not a smear.

A site's `frac_readable` = the fraction of its bright columns that are readable-class. It extends the
[readability gate](https://github.com/robertlangdonn/vesuvius-readability-gate) from a single-surface
judge to a scroll-wide survey.

## The calibration (the load-bearing step)

The metric is only trustworthy if it separates a scroll we *know* can be read from one that is still
sealed. Run identically on both:

| scroll | sites | median `frac_readable` | p90 | sites ≥ 0.2 |
|---|---|---|---|---|
| **PHerc1667** (read end-to-end) | 60 | **0.35** | 0.94 | 62% |
| **PHerc1203** (sealed) | 240 | **0.004** | 0.17 | 10% |

A ~90× median gap. A read scroll lights up; the sealed one does not.

![readability distribution](figures/readability_distribution.png)

## The survey

240 stratified PHerc1203 sites: mostly packed (median 0.004), with **rare readable pockets** — the
best reaches 0.89, and 13 of 240 sites exceed 0.40. The 22 public `auto_grown` surfaces all fail a
basin probe (no readable sheet within ±100 voxels along the normal × ±24 tangential), i.e. they sit in
packed dead zones. Their speckle is a *placement* failure, not a model failure.

![packed vs pocket](figures/dead_vs_pocket.png)

## Is the best pocket real? (robustness panel)

Identical 384³ pipeline on five readable-PHerc1667 anchors, five dead-PHerc1203 controls, and the top
three PHerc1203 pockets:

| group | median `frac_readable` | median largest connected component |
|---|---|---|
| PHerc1667 readable anchors | 0.30 | 2950 cells |
| PHerc1203 dead controls | 0.014 | 25 cells |
| PHerc1203 top pockets | 0.14 | 573 cells |

The **best pocket** (`frac_readable` 0.33, component 3943) lands *inside* the readable-1667 anchor
distribution. Pockets 2–3 are intermediate. (This is one top pocket vs a small control panel —
"comparable to", not "statistically indistinguishable".)

Top candidate dig sites (L0 voxel coordinates) are in [`data/top_dig_sites.csv`](data/top_dig_sites.csv).

## Honest limitations

- Measures readability **potential / geometry, not ink**. No letters were read; no surface was grown or
  rendered.
- Absolute sheet area is **pipeline-limited** — the same pipeline undercounts even on readable
  PHerc1667 — so coherence is reported *relative to the 1667 anchor*, not as an absolute area.
- Best-pocket coherence is n=1 vs a small panel — a strong candidate, not a finished result.

## Usage

```bash
pip install numpy scipy tifffile imagecodecs zarr fsspec aiohttp pillow
python scripts/survey.py            # scroll-wide frac_readable survey (streams public CT)
python scripts/calibrate_1667.py    # calibration against the read scroll
python scripts/robustness_panel.py  # anchors vs controls vs pockets
```

Everything streams bounded blocks from the public open-data bucket — no full-scroll download.

**Note on the PHerc1203 coordinate frame:** its `tifxyz` segment maps index the volume as
`(axis0, axis1, axis2) = (x.tif, z.tif, y.tif) × 2` — different from PHerc1667's `(z, y, x) × 1`.
Solved empirically; always self-check that depth-0 sampling lands on bright material before trusting a
resample.

## License

MIT — see [LICENSE](LICENSE). Built on public Vesuvius Challenge open data.
