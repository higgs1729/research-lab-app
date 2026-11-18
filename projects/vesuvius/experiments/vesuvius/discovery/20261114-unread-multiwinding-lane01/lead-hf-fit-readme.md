---
license: cc-by-nc-4.0
pretty_name: Eligible scroll spiral fits (PHerc0191, PHerc0826)
---

# Spiral fits for PHerc0191 and PHerc0826, published as unvalidated geometry

Four spiral-fitting runs on two prize-eligible scrolls, released as tifxyz meshes so that anyone can render them,
run a detector on them, or measure them against their own fit. **PHerc0191 has no other published mesh set.**

These are **surfaces produced, not coverage and not usable area.** The winding density is unresolved and the audit
below says so on the author's own numbers. Read that section before using the area figures for anything.

## What is here

Per run: `meshes/fitted/wNNN/{x,y,z}.tif` plus `meta.json` per winding, the flattened samples, the render archives,
`satisfaction_metrics_fitted.json`, and the fit checkpoint.

| run | scroll | window | windings | raw surface produced |
|---|---|---|---|---|
| 2026-09-15_PHerc0191_slice-11600-12400_0-patch_w90 | PHerc0191 | z 11600-12400 | 90 | 415.63 cm2 |
| 2026-09-15_PHerc0826_slice-6528-7328_0-patch | PHerc0826 | z 6528-7328 | 90 | 564.77 cm2 |
| 2026-09-15_PHerc0826_slice-8928-9728_0-patch | PHerc0826 | z 8928-9728 | 90 | 510.89 cm2 |
| 2026-09-15_PHerc0826_slice-9328-10128_0-patch | PHerc0826 | z 9328-10128 | 90 | 506.37 cm2 |

The three PHerc0826 windows overlap in z, so **their figures do not add.**

## Provenance

- PHerc0191 volume: `20250821151635-9.362um-1.2m-113keV-masked.zarr`, shape 18977 x 8387 x 8387, voxel 9.362 um.
- Umbilicus for PHerc0191: Drobkov's 64-point manual curve, commit `a34224b76865`, file sha256 `b67a3aae154b9d27`.
  PHerc0826 uses the official umbilicus.
- Fitter: villa pinned at `757f70c0`. Each run took 1.5 to 1.9 hours on one A40.
- Prior art: gmDevi fitted the same PHerc0191 volume on Kaggle and published no meshes. This is not the first fit of
  that scan; it is the first published mesh set for it.

## Winding density is unresolved, and the answer depends on the threshold

12 rays from the umbilicus at z = 12000, counting bright peaks in the raw scan between the innermost and outermost
winding of the fit, at three peak-prominence thresholds.

| ray | our windings | strict peaks (k3) | mid (k2) | permissive (k1) | autocorr period (vx) | count from period |
|---|---|---|---|---|---|---|
| 15° | 74 | 24 | 32 | 48 | 27 | 32.7 |
| 45° | 74 | 28 | 37 | 56 | 27 | 36.6 |
| 75° | 70 | 22 | 36 | 57 | 41 | 28.6 |
| 105° | 70 | 35 | 49 | 71 | 30 | 47.7 |
| 135° | 69 | 34 | 43 | 67 | 29 | 49.1 |
| 165° | 73 | 31 | 52 | 67 | 32 | 43.6 |
| 195° | 72 | 23 | 34 | 46 | 27 | 42.3 |
| 225° | 71 | 42 | 52 | 76 | 27 | 65.6 |
| 255° | 70 | 42 | 56 | 77 | 23 | 76.9 |
| 285° | 64 | 34 | 43 | 65 | 37 | 33.4 |
| 315° | 72 | 32 | 46 | 59 | 32 | 34.2 |
| 345° | 71 | 37 | 49 | 63 | 24 | 46.2 |

Read both directions, because they disagree:

- Against the **strict** peak count (k3) the fit has more windings than there are peaks on **all 12 rays**, 64-74
  against 22-42. On that reading the fit is roughly two to three times over-packed.
- Against the **permissive** count (k1) the fit is at or below the peak count on **4 of 12 rays** (105, 225, 255, 285).
- The autocorrelation period gives an independent sheet count of 28.6 to 76.9, which **brackets** our 64-74 from
  both sides depending on the ray.

So the honest statement is not "the fit is 2-3x over-packed". It is that **sheet counting in this scan is
threshold-dependent over a factor of three, and nobody has pinned the threshold.** Our median winding pitch is
10.5 voxels against a scan peak pitch of 14-19. Treat every mesh here as unvalidated geometry until that is settled.

## Two further negatives, published as they came out

**Winding numbering does not transfer between overlapping windows.** Across 400 shared slices, no winding of the
second PHerc0826 fit matches a single winding of the first with 0.8 or more of its points; median share 0.28, offsets
-6 to +18, while the surfaces themselves largely coincide at median 3.42 voxels. The test is confounded: consecutive
windings sit a median 7.3 voxels apart with 31 of 89 pairs under 5 voxels.

**A pre-registered A/B on winding count failed three of its four predictions.** Arm B at 45 windings produced the
same surfaces as arm A at 90: 45 of 45 matching at offset 0, share 1.0, median distance 0.00 voxels.
`shell_outer_winding_idx` sets how far outward the fit exports, not winding density, so area follows extent
(99.79 cm2 against 415.63). The fourth prediction, about render quality, is moot because the surfaces are identical.

**Against pscamillo's published PHerc0826 meshes**, measured one way only: 99.8, 99.7 and 90.9 percent of his mesh
points lie within 20 voxels of one of our surfaces (median 3.7, 4.4, 4.5), though only 71, 58 and 23 percent lie
within 5 voxels of the winding they mostly land on. The reverse distance was never measured.

## Licence and credit

Released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) by Carson Rodrigues. The selection, processing and every added field are his work; rows taken from the sources keep their own licences.

- **Credit is required.** Cite the dataset as below and link to this page in anything that uses it.
- **Non-commercial use only.** Commercial use, including training a model that is sold or served commercially, needs written permission from the author: open a discussion on this page.

```bibtex
@misc{rodrigues2026eligiblescrollspiralfits,
  author       = {Rodrigues, Carson},
  title        = {Eligible scroll spiral fits (PHerc0191, PHerc0826)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/rodriguescarson/eligible-scroll-spiral-fits}}
}
```
