P.HERC. 0211 — EXPANDED9 SUBMISSION
Confidential review material · 8 October 2026

START HERE
This Drive folder contains two full-resolution PNGs, this methodology, and one native mesh folder. Training/reproduction data live on Hugging Face; executable code and exact commands live on GitHub. There are no ZIP bundles.

Code and exact reproduction instructions:
https://github.com/priyankaranke/vesuvius-expanded9-training
Training CT, original labels, splits, validation and submission-only CT/probabilities:
https://huggingface.co/datasets/paranke/vesuvius-expanded9-training-data
Expanded9 weights and model documentation:
https://huggingface.co/paranke/vesuvius-expanded9-resunet
The private repositories require authorized read access. No GitHub Pro, HF Pro, paid dataset viewer or W&B account is needed. Private URLs alone do not grant access.

IMAGE AND MESH
The PNG basename matches the mesh folder:
PHerc0211-3305-r002-c01-manual-20261008-203736-legacyuv20-v1
The PNG is the viewer's direct native export: 2540 × 5560 pixels, Turbo overlay, Model contrast, opacity 0.48, CT window [0,200], and MAX of native planes 14–17. No generative imagery, upscaling or character retouching is used. The separate “-with-1cm-bar.png” changes only the bar rectangle in an empty black margin. At 9.362 µm/pixel, its 1068-pixel bar represents 9.998616 mm. The full image spans 23.77948 × 52.05272 mm.

Keep the five mesh-folder files together: x.tif, y.tif, z.tif, meta.json and Open in VC3D.volpkg.json. The first four form the complete native tifxyz. In VC3D choose File → Open Project, select the JSON, then double-click the surface. It connects the public PHerc0211 CT volume. The Drive download matched the source and reopened in VC3D.

METHOD
Will Stevens' patch-growing method supplied the initial surface; CT-supported points were added manually in VC3D. The edited surface received 50 Flatboi symmetric-Dirichlet iterations and legacy UV20 normalization. Energy fell from 8.2250676 to 8.0007594, with zero reported flipped triangles. Native CT rendering produced 31 planes at one-voxel intervals; Expanded9 uses planes 23 down to 8. Sigmoid probabilities from the central 96 pixels of 128-pixel windows are stitched at stride 64 with normalized Hann weights. Display-only contrast maps the covered region's 1st–99.5th percentiles through Turbo, then blends uniformly over CT at 48%. Saved probabilities remain unchanged; no prediction cleanup or OCR is applied.

TRAINING AND CONFIDENCE
Expanded9 is a 3D residual U-Net trained from scratch for 10 epochs / 74,160 updates on 112 representations across 12 parent-scroll groups, with equal-scroll sampling, augmentation and BCE + Dice loss. Labels include manual and teacher-derived material. NO TRAINING OR FINE-TUNING WAS DONE ON PHERC0211; it is absent from training and validation. Its HF directory is inference-only.

The 1.20 mm model window, excluded target scroll and visible CT fibers support false-positive inspection, without proving every prediction is ink. Historical PHerc0841 validation, with a 2 mm training exclusion, reported AP 0.0540611 / ROC-AUC 0.805088 on 1,334 patches. These labels are not independently certified ground truth.

HOW THE PIECES FIT TOGETHER
GitHub's numbered README provides all commands; no original workstation or other private repository is required.
1. download_data.py and materialize_dataset.py restore HF's complete prepared corpus: 113 representations, 130,645 CT tiles, labels and frozen split, about 30.6 GB. No training segment needs rendering. CT was restored in October from frozen recipes; September CT hashes are unavailable.
2. train_portable.py trains from random weights with local logs; export_checkpoint.py exports the final weights.
3. prepare_submission.py optionally rerenders from the Drive mesh and public CT; --reflatten also rebuilds flattening from supplied edited geometry.
4. rerun_inference.py computes predictions; reproduce_image.py exports through the viewer and checks both PNGs pixel-for-pixel.
Fresh viewer exports passed. Scratch retraining is not promised to yield identical weights; use the published checkpoint for the exact image. Full training/rendering/inference was not rerun for this documentation update. Keep confidential for prize review.
