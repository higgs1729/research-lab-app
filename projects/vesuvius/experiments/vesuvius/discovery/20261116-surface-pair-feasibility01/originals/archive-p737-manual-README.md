PHERC0211 — THIN15 SUBMISSION (FIRST LETTERS)
Confidential review material · 14 October 2026 · surface revision 3 (1701)
Supersedes the previous Studio package, which is kept in archive_2026-10-14_superseded_Studio_submission/.
The earlier Expanded9 package remains in archive_2026-10-08_PHerc0211-3305-r002-c01-manual-v1/.

SOURCE SCROLL
PHerc0211, public volume 20250821151803-9.362um-1.2m-113keV-masked.zarr (9.362 µm/voxel). One scroll, one submission.

WHAT IS IN THIS FOLDER
- mesh_PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3/ — the tifxyz mesh the image was made from (mesh id PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3): x.tif, y.tif, z.tif (float32 native voxel
  coordinates of the public volume; −1 = no surface), meta.json, and "Open in VC3D.volpkg.json". Grid step 20 voxels
  (scale 0.05); the 2D parametrization is the canonical flatboi (50 symmetric-Dirichlet iterations, energy 8.1169 → 8.0018,
  0 flipped triangles) with legacy UV20 normalization, so the tifxyz already carries the low-distortion isometric
  parametrization. 11,044 valid nodes, 3.785 cm² (triangulated), i.e. the whole mesh is inside the 4 cm² budget.
  3D position (native voxels, x y z): bounding box [1397, 4061, 6571] – [3943, 4750, 9413], centroid ≈ (2836, 4608, 7966).
  In VC3D: File → Open Project, choose the JSON, double-click the surface; it connects the public PHerc0211 volume.
  Keep the five files together.
- PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3_thin15_turbo.png — the submission image, named after the mesh: 2780 × 3140 px at
  9.362 µm/px (the rendered surface is 2780 × 2920 px; the margin below it holds the 1 cm bar, 1068 px long). Produced
  programmatically from the CT volume and the mesh (section REPRODUCTION); no manual annotation, retouching, upscaling
  or generative imagery.
- preview_PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3_thin15_turbo.png — the same image downsampled to 1200 px height.
- PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3_ct_rows_annotated.png — the fibre-visible CT rendering of the same mesh (same planes and
  window, no ink overlay) with five row guides placed programmatically in low-response gaps below the Thin15 probability bands,
  plus the 1 cm bar. These guides are annotations, not a transcription.
- PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3_ct_layer.tif — the CT layer under the overlay (maximum of native planes 14–17,
  window [0, 200]), supplied so the overlay can be checked against the fibres without re-rendering. The raw float32
  probability map is available on request.
- PHerc0211-P737m01st3-manual-20261014-1701-legacyuv20-v3_mesh.zip — extras for re-flattening: surface.obj (pre-flatten mesh with UVs),
  surface_flatboi.obj (flattened), mesh.npz / flat-mesh.npz, case.json, results.json (flatten report), input.json
  (orientation record, see below) and a copy of the normalized tifxyz.

THE LETTERS
Five rows of ink-like responses cross the mesh (Thin15 vertical-profile peaks at y ≈ 335, 755, 1316, 1785 and
2320 px; mean pitch ≈ 4.6 mm). The CT companion marks these five bands with guides derived from the Thin15 map.
The earlier Studio blob counts and bounding boxes are retained with the archived submission; they are not
measurements of this revision. We make no claim about the identity of individual letters.

REPRODUCTION
All code and data are in private repositories at the time of writing; read access is given to reviewers on request
and the Hugging Face repositories will be made public. No paid account is needed.
  Thin15 training stack (data preparation, training, inference, verification, pinned environment):
    https://github.com/priyankaranke/vesuvius-814-841-9b-studio-thin15-w96-training
  Thin15 weights (epoch 5, model.safetensors) with the inference package (inference.py, model.py):
    https://huggingface.co/paranke/vesuvius-814-841-9b-resunet-studio-thin15-w96-20261011
  Thin15 training data (labels, rendered CT tiles, plans, holdout):
    https://huggingface.co/datasets/paranke/vesuvius-814-841-9b-studio-thin15-w96-training-data
  Segmentation code (CT grower, stitching, Will-driver tooling) and the render/inference runtime:
    https://github.com/priyankaranke/first-letters-grow-optimized (branches codex/scroll-pilot-20261009 and codex/grow-throughput)
    https://github.com/priyankaranke/first-letters-render-optimized
    https://github.com/priyankaranke/first-letters-inference-optimized

Steps to reproduce the image:
1. Render the mesh from the public volume with Volume Cartographer's vc_render_tifxyz (we use the renderer image
   ghcr.io/scrollprize/villa/volume-cartographer@sha256:bad516f6…): 31 native planes at one-voxel steps, output
   rendered-31/00.tif … 30.tif, 2780 × 2920 px each. The tifxyz in this folder is already flattened and normalized,
   so no re-flattening is needed to reproduce the image; the extras zip has the pre-flatten OBJ for anyone who wants
   to re-run flatboi (50 iterations, UV20).
2. Orientation: the surface's depth direction is fixed once per mesh from the geometry (global radial continuation
   of the training-side convention; never chosen with ink predictions). Revision 3 inherits that convention by matching
   its geometry to the original P737 surface. For this mesh normal_sign = −1, so the model reads planes 23 down to 8
   (input.json: hann_indices). The physical recto/verso face has not been independently verified.
3. Inference: the published Thin15 weights (epoch 5, model.safetensors, SHA-256
   4089ad2641f607cf6704d26b32f7cee17c85336938de70e3ac6b45907e41632f), using the published inference.py.
   Input = 16 uint8 planes in that order, clip(raw, 0, 200) / 255; 96 × 96 px windows at stride 32; the central
   64 × 64 px of each window are blended with a pixel-centred 2D Hann weight (overlapping windows averaged by weight);
   sigmoid output written as float32 probabilities and masked to the surface. This map used BF16 precision,
   batch size 32, on an NVIDIA GH200. The earlier Studio precision and repeatability comparisons do not apply here.
4. Image: CT = maximum of native planes 14–17, window [0, 200]; the Thin15 probability is mapped through the Turbo
   colour table after a display-only contrast stretch (1st–99.5th percentile of the covered pixels) and blended at
   48 % opacity where the model has coverage; black outside the mesh; 1 cm bar added in the margin. Script:
   make_submission_images.py and turbo.json in the mesh zip, preserving the previous submission's display style.
   Saved probabilities are never modified; no prediction clean-up, thresholding or OCR is applied.

HOW THE SEGMENT WAS MADE (brief)
A spiral fit of the scroll was performed first. Promising segments from the spiral fit were grown with a hybrid
approach combining Will Stevens' patch grower (pipeline9, parameters unchanged) with CT-based surface growth (a front
propagated along the sheet, each node snapped to the papyrus face in the CT), and the resulting segments were refined
manually in VC3D so that they follow the surface. For this mesh: a Will chart seeded on a CT-grown surface was
hole-filled in VC3D, grown in place by the CT grower, edge-trimmed, and joined with the CT-grown continuation of the
same sheet above it. Subsequent manual corrections and re-flattenings produced the frozen 14 October 1701 revision 3
used here; it was then rendered and inferred as above. Only geometry was edited by hand; no ink output was touched.

HOW THE INK MODEL WAS MADE (brief)
Scroll similarity was computed with a self-supervised DINO model.
The model indicated that PHerc0814, PHerc0841 and
PHerc0009B were more similar to many of the target scrolls than the scrolls we already had labels on. Spiral fits
were run on PHerc0814 and PHerc0841 and regular surface growth on PHerc0009B to extract segments; these were labelled
manually (sparse ink / background labels), downscaled to approximately 9 µm, and used to train Thin15 from random
initialization: DeepResidualUNet (223 M parameters), 154,300 distinct patches / 424,425 training entries / 8,340 CT
tiles from the three scrolls (PHerc0814 175,956 entries, PHerc0841 160,533, PHerc0009B 87,936), BCE + Dice loss on the
central 64 px of 96 px windows, 5 epochs (41,250 updates). Thin15 applies 15 % local-width thinning to the training
ink labels while protecting their skeleton; removed ink becomes background. The architecture was selected on the basis of refinements
done on Scroll 1; no Scroll 1 data was used in training. Full recipe, pinned environment, per-update log and the
model configuration are in the training repository.

NO OVERLAP, NO MEMORIZATION
- PHerc0211 is absent from Thin15's training, validation and label sets in every form: the model was trained on
  PHerc0814, PHerc0841 and PHerc0009B only and never fine-tuned. The output on this mesh is generalization to an
  unseen scroll; there is no training region it could overlap.
- Window size: 96 × 96 px at ≈ 9.4 µm = 0.90 × 0.90 mm input, 0.60 × 0.60 mm kept per window, 16 planes deep.
  The model classifies local ink texture; the window dimensions alone do not prove the absence of memorization.
- Independent model (earlier submission): Expanded9, trained on other scrolls without PHerc0211, marked 69 % of
  the earlier Studio map's letter-sized blobs in its best 2 × 2 cm window. That historical comparison is preserved
  with the archive; it has not been recomputed for this revision's Thin15 image.
- Same text on independent surfaces: the rows on this mesh were also read on four other, separately grown meshes of
  the same sheet (CT growth from a reviewed segment, two CT-extended Will charts, and the pure Will chart this mesh
  started from); the letters are a property of the papyrus, not of one mesh.
- Held-out validation: on the fixed holdout (PHerc0841 layer-03 approved labels, 2 mm exclusion from any
  training tile) the published Thin15 epoch-5 weights give AP 0.7683 and ROC-AUC 0.8327 on the original labels,
  measured over the central 32 px (model-config.json). The labels are manual and not independently certified.
  No k-fold on public ground-truth renders was run.

OTHER NOTES
Confidential until the prize is announced. The ink-detection result shown is the direct model output; readings and
row guides above come from the probability map, not from any hand-drawn annotation.

