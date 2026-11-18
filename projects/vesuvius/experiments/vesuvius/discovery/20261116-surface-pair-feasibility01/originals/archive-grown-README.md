PHERC0211 — STUDIO SUBMISSION (FIRST LETTERS)
Confidential review material · 10 October 2026
Supersedes the 8 October Expanded9 package, which is kept in archive_2026-10-08_PHerc0211-3305-r002-c01-manual-v1/.

SOURCE SCROLL
PHerc0211, public volume 20250821151803-9.362um-1.2m-113keV-masked.zarr (9.362 µm/voxel). One scroll, one submission.

WHAT IS IN THIS FOLDER
- mesh_PHerc0211-P737m01st3-grown/ — the tifxyz mesh the image was made from (mesh id PHerc0211-P737m01st3-grown): x.tif, y.tif, z.tif (float32 native voxel
  coordinates of the public volume; −1 = no surface), meta.json, and "Open in VC3D.volpkg.json". Grid step 20 voxels
  (scale 0.05); the 2D parametrization is the canonical flatboi (50 symmetric-Dirichlet iterations, energy 8.0106 → 8.0015,
  0 flipped triangles) with legacy UV20 normalization, so the tifxyz already carries the low-distortion isometric
  parametrization. 11,264 nodes, 3.974 cm² (triangulated), i.e. the whole mesh is inside the 4 cm² budget.
  3D position (native voxels, x y z): bounding box [1812, 4309, 6486] – [3864, 4753, 9502], centroid ≈ (2963, 4654, 7908).
  In VC3D: File → Open Project, choose the JSON, double-click the surface; it connects the public PHerc0211 volume.
  Keep the five files together.
- PHerc0211-P737m01st3-grown_studio_turbo.png — the submission image, named after the mesh: 2180 × 3340 px at
  9.362 µm/px (the rendered surface is 2180 × 3120 px; the margin below it holds the 1 cm bar, 1068 px long). Produced
  programmatically from the CT volume and the mesh (section REPRODUCTION); no manual annotation, retouching, upscaling
  or generative imagery.
- preview_PHerc0211-P737m01st3-grown_studio_turbo.png — the same image downsampled to 1200 px height.
- PHerc0211-P737m01st3-grown_ct_rows_annotated.png — the fibre-visible CT rendering of the same mesh (same planes and
  window, no ink overlay) with the five text rows marked by thin baselines placed programmatically under each row's
  confident ink blobs, plus the 1 cm bar. The baselines do not touch the letters.
- PHerc0211-P737m01st3-grown_ct_layer.tif — the CT layer under the overlay (maximum of native planes 14–17,
  window [0, 200]), supplied so the overlay can be checked against the fibres without re-rendering. The raw float32
  probability map is available on request.
- PHerc0211-P737m01st3-grown_mesh.zip — extras for re-flattening: surface.obj (pre-flatten mesh with UVs),
  surface_flatboi.obj (flattened), mesh.npz / flat-mesh.npz, case.json, results.json (flatten report), input.json
  (orientation record, see below) and a copy of the normalized tifxyz.

THE LETTERS
Five rows of text cross the mesh (row centres at y ≈ 392, 923, 1412, 1910 and 2414 px; pitch ≈ 4.7 mm). On the
submission image Studio marks 30 letter-sized ink blobs, 15 of them confident (p ≥ 0.75 after the display contrast,
1.5–8 mm² each). Representative blobs, bounding boxes in pixels at 9.362 µm/px (a few are two touching letters):
  row 1: 300 × 353 px = 2.81 × 3.30 mm; 315 × 234 px = 2.95 × 2.19 mm
  row 2: 254 × 218 px = 2.38 × 2.04 mm; 443 × 443 px = 4.15 × 4.15 mm (two letters)
  row 3: 321 × 353 px = 3.01 × 3.30 mm; 262 × 284 px = 2.45 × 2.66 mm
  row 4: 477 × 327 px = 4.47 × 3.06 mm (two letters); 576 × 307 px = 5.39 × 2.87 mm (two letters)
  row 5: 147 × 258 px = 1.38 × 2.42 mm; 183 × 152 px = 1.71 × 1.42 mm
Letter height is therefore about 2–3.3 mm and line pitch about 4.7 mm, consistent with a Herculaneum prose hand.
We make no claim about the identity of individual letters.

REPRODUCTION
All code and data are in private repositories at the time of writing; read access is given to reviewers on request
and the Hugging Face repositories will be made public. No paid account is needed.
  Studio training stack (data preparation, training, inference, verification, pinned environment):
    https://github.com/priyankaranke/vesuvius-814-841-9b-studio-training
  Studio weights (epoch 9, model.safetensors) with the inference package (inference.py, model.py):
    https://huggingface.co/paranke/vesuvius-814-841-9b-resunet-studio-20260926
  Studio training data (labels, rendered CT tiles, plans, holdout):
    https://huggingface.co/datasets/paranke/vesuvius-814-841-9b-studio-training-data
  Segmentation code (CT grower, stitching, Will-driver tooling) and the render/inference runtime:
    https://github.com/priyankaranke/first-letters-grow-optimized (branches codex/scroll-pilot-20261009 and codex/grow-throughput)
    https://github.com/priyankaranke/first-letters-render-optimized
    https://github.com/priyankaranke/first-letters-inference-optimized

Steps, each deterministic given the mesh:
1. Render the mesh from the public volume with Volume Cartographer's vc_render_tifxyz (we use the renderer image
   ghcr.io/scrollprize/villa/volume-cartographer@sha256:bad516f6…): 31 native planes at one-voxel steps, output
   rendered-31/00.tif … 30.tif, 2180 × 3120 px each. The tifxyz in this folder is already flattened and normalized,
   so no re-flattening is needed to reproduce the image; the extras zip has the pre-flatten OBJ for anyone who wants
   to re-run flatboi (50 iterations, UV20).
2. Orientation: the surface's depth direction is fixed once per mesh from the geometry (global radial continuation
   of the training-side convention; never chosen with ink predictions). For this mesh normal_sign = −1, so the model
   reads planes 23 down to 8 (input.json: hann_indices).
3. Inference: the published Studio weights (epoch 9, model.safetensors, SHA-256 ffffbf4f…) in our tiled inference engine.
   Input = 16 uint8 planes in that order, clip(raw, 0, 200) / 255; 128 × 128 px windows at stride 64; the central
   96 × 96 px of each window are blended with a pixel-centred 2D Hann weight (overlapping windows averaged by weight);
   sigmoid output written as float32 probabilities. The engine runs the network in mixed FP8/BF16 precision on an NVIDIA
   GH200. The same weights with the same stride-64 Hann blending in BF16 reproduce this map to correlation 0.987 (mean
   absolute difference 0.025 in probability); the package's own inference.py uses plain stride-96 tiling instead.
   Inference is deterministic: a second run on the identical render reproduced the first to < 1e−5 everywhere.
4. Image: CT = maximum of native planes 14–17, window [0, 200]; the Studio probability is mapped through the Turbo
   colour table after a display-only contrast stretch (1st–99.5th percentile of the covered pixels) and blended at
   48 % opacity where the model has coverage; black outside the mesh; 1 cm bar added in the margin. Script:
   pherc0211_windings/analysis/make_turbo.py in first-letters-grow-optimized (branch codex/scroll-pilot-20261009).
   Saved probabilities are never modified; no prediction clean-up, thresholding or OCR is applied.

HOW THE SEGMENT WAS MADE (brief)
A spiral fit of the scroll was performed first. Promising segments from the spiral fit were grown with a hybrid
approach combining Will Stevens' patch grower (pipeline9, parameters unchanged) with CT-based surface growth (a front
propagated along the sheet, each node snapped to the papyrus face in the CT), and the resulting segments were refined
manually in VC3D so that they follow the surface. For this mesh: a Will chart seeded on a CT-grown surface was
hole-filled in VC3D, grown in place by the CT grower, edge-trimmed, and joined with the CT-grown continuation of the
same sheet above it; then flattened, rendered and inferred as above. Only geometry was edited by hand; no ink output
was touched.

HOW THE INK MODEL WAS MADE (brief)
Scroll similarity was computed with a self-supervised DINO model.
The model indicated that PHerc0814, PHerc0841 and
PHerc0009B were more similar to many of the target scrolls than the scrolls we already had labels on. Spiral fits
were run on PHerc0814 and PHerc0841 and regular surface growth on PHerc0009B to extract segments; these were labelled
manually (sparse ink / background labels), downscaled to approximately 9 µm, and used to train Studio from random
initialization: DeepResidualUNet (223 M parameters), 154,300 distinct patches / 424,425 training entries / 8,340 CT
tiles from the three scrolls (PHerc0814 175,956 entries, PHerc0841 160,533, PHerc0009B 87,936), BCE + Dice loss on the
central 96 px, 9 of 10 planned epochs (74,250 updates). The architecture was selected on the basis of refinements
done on Scroll 1; no Scroll 1 data was used in training. Full recipe, pinned environment, per-update log and the
exact-run comparison script are in the training repository.

NO OVERLAP, NO MEMORIZATION
- PHerc0211 is absent from Studio's training, validation and label sets in every form: the model was trained on
  PHerc0814, PHerc0841 and PHerc0009B only and never fine-tuned. The output on this mesh is generalization to an
  unseen scroll; there is no training region it could overlap.
- Window size: 128 × 128 px at ≈ 9.4 µm = 1.20 × 1.20 mm input, 0.90 × 0.90 mm kept per window, 16 planes deep.
  Letters here are 2–3.3 mm tall, so one window sees well under half a letter: the model classifies local ink
  texture and cannot assemble a letterform from memory.
- Independent model: Expanded9 (a separate network trained on other scrolls, also without PHerc0211) marks 69 % of
  Studio's letter-sized blobs in the best 2 × 2 cm window of this mesh; two models with different training data light
  the same strokes.
- Same text on independent surfaces: the rows on this mesh were also read on four other, separately grown meshes of
  the same sheet (CT growth from a reviewed segment, two CT-extended Will charts, and the pure Will chart this mesh
  started from); the letters are a property of the papyrus, not of one mesh.
- Held-out validation: on Studio's fixed holdout (PHerc0841 layer-03 approved labels, 2 mm exclusion from any
  training tile) the published epoch-9 weights give AP 0.7657 and ROC-AUC 0.8304 (verify_holdout.py in the training
  repository reproduces these numbers on the rebuilt data). The labels are manual and not independently certified.
  No k-fold on public ground-truth renders was run.

OTHER NOTES
Confidential until the prize is announced. The ink-detection result shown is the direct model output; readings and
letter counts above come from the probability map, not from any annotation.
