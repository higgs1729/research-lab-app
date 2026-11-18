# R234: PHerc0211 adjacent-context feasibility

2026-11-15. Researcher `r234_pherc0211_context` (Astra/xhigh). The request and findings live in [research/234](../../../../research/234-pherc0211-adjacent-context-feasibility.md). No CT body, model input array, model weights or new predictions were downloaded or produced here. GPU and paid computation: 0.

## Decision

Select one **already public, unresolved response**: the curved upright at the right end of row two in the released v9 surface. Its upper right branch meets the surface mask boundary. This is a target for a finite observation of whether the same sheet continues, not a new letter or ink discovery. The known phi in the same row is the control. The upper-row and phi-neighbour native crops were inspected but are not additional follow-up candidates.

- Surface: `PHerc0211-crop1711-lines123-manual-20261028-1316-legacyuv20-v9`, 6020×1740 native pixels, 9.362 µm/voxel.
- Context crop: XYWH `[5600,680,420,480]`; missing-branch target: `[5820,800,160,160]`. Slice coordinates are half-open and are not transcriptions.
- Known-phi control: `[4640,780,320,300]`, identified by visual correspondence with the official figure's `διαφ` sequence. No exact image registration from the article to this surface is claimed.
- Node anchor: v9 grid `[42,298]` → native XYZ `[4210.22509765625,4210.63916015625,8398.435546875]`. Grid nodes are continuous canvas positions `(20c,20r)`; they are not integer pixel centres.

## Evidence map

| File | Meaning |
| --- | --- |
| `drive-folder-list.json`, `drive-plugin-results.json` | Connected Drive metadata/listing and README content; temporary signed URLs removed |
| `sources/drive-README.md` | Complete 5,897-byte author README, raw authenticated connector download |
| `sources/v9-mesh.zip`, `sources/v6-line2-mesh.zip` | Complete public ZIP responses; only selected small v9 members extracted |
| `sources/v9-probability-f32.tif` | Complete released float32 probability map, 38,709,184 bytes; file and all-pixel SHA match `reproduction.json` |
| `acquisitions.jsonl` | Direct public URLs, timestamps, HTTP headers, body bytes, SHA-256 |
| `source-check.json` | All 36 v9 and 38 v6 ZIP support-member SHA checks, exact raster-mask edge samples |
| `v9-inspection.json`, `inspect_v9.py`, `review/` | Deterministic non-generative native crops and quarter-scale orientation overview |
| `geometry-inspection.json`, `inspect_geometry.py` | Direct native XYZ grid anchors and limited coverage comparison against v6 parent |
| `candidate-plan.json` | The single next experiment, exact 26 CT keys/HEAD lengths, fixed 14 sections, resource limits and stop conditions |
| `lead-*.json`, `lead-article-images/` | Lead's separate raw-source, pixel, geometry, visual and plan verification |

The ZIP `labels.json` holds typographic row/scale-bar label glyphs; it is **not** a papyrological ink-label mask. The current v9 prediction is wholly prior public work. The author's earlier nine PHerc0211 evaluation segments are described in `sources/cpt-README-fixed.md`; its description of an unlabeled stitched crop is not proof that the later v9 region is unlabelled or unread by everyone. The article's green rectangle is not an exhaustive prior-publication boundary.

## Geometry and display limits

The published v9 normalized grid is 87×301 with scale `[0.05,0.05]`; v6 full parent is 230×303. Both point to the public `20250821151803-9.362um-1.2m-113keV-masked.zarr` scan. The v6 parent has only a small amount of nearby support at its corresponding right edge. A straight extrapolation from v9 beyond that edge finds physically nearby vertices at v6 columns around 90–93, far from the corresponding columns around 299–301; nearest XYZ is not evidence that those distant UV branches are the same sheet. No surface was extended or stitched here.

`reproduction.json`/`reproduce_submission.py` select rendered planes 23..8 of the 31-plane -15..+15 stack, i.e. offsets +8..-7 under the author's convention. CT background is max of planes 14..17. `orientation.json` records inherited normal sign -1 and explicitly `physical_face_verified:false`; this work has not independently proven recto/verso or rerun the pinned renderer. The next observations use grid-node anchors directly and avoid an uncertain pixel-centre interpolation contract.

The native colour crops use the public image-making recipe: p is unchanged, display-only 1–99.5 percentile limits, Turbo table and 48% overlay over CT clipped at 200. The raw 0..1 probability crops are also included. The author `results.json` is historical run metadata; its probability range/display numbers differ from the current released map. The actual release matches `reproduction.json`, and its measured maximum is 0.9474670291. No model execution or exact GPU-reproduction claim is made.

## Next observation, not executed

The lead adopted a CPU-only test of the right-edge sheet continuation. Candidate box XYZ `[4096,4096,8320]`–`[4352,4352,8576]` has 8 chunks; known-phi box `[3328,3200,8192]`–`[3712,3456,8576]` has 18. All 26 HEAD requests returned 200 and 2,097,152 bytes: **54,525,952 bytes (52 MiB)** total. CT bodies remain unacquired.

Four candidate and four known-control native XY sections, plus four candidate and two control tangent/normal sections, are fixed in the plan. Each has raw 0..255 and one fixed 46..169 display: 14 sections, 28 images. The oblique planes are observational planes, not new papyrus surfaces. Trilinear samples needing any corner outside the fixed boxes are missing; no extra chunks or box widening.

CPU1, expected peak RAM below 1 GiB, existing Windows runner's process commit limit 4 GiB, 15-minute wall limit, C new-save limit 96 MiB, minimum C free 2 GiB, GPU0 and additional cost US$0. Save CT chunks once and assemble box arrays in RAM. These are a proposal for R235; R234 performs no such CT observation. A clear continuation supports a later bounded extension only. Missing sheet, unresolved branching, or a failed known control ends this candidate without widening/extra models/repeated CT diagnosis.

`plan_followup.py` records the original HEAD-derived boxes. `add_fixed_sections.py` records the lead-requested tangent/normal addition. The authoritative final plan includes the fixed axial anchors and final resource distinction; rerunning acquisition/planning scripts creates a new observation and must not overwrite the frozen evidence.
