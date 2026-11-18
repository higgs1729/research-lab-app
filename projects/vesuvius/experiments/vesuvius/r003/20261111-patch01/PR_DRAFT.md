# flatboi: use full-grid units for decimated initial UVs

Local draft only. No PR has been opened. Human review and human-authored usefulness commentary have not yet been supplied; the checkbox below is deliberately unchecked.

**In one sentence:** When a tifxyz surface is flattened with `0 < --keep < 100`, initialise UVs in the original grid's units so the coarse grid does not start artificially compressed.

**One real example:** An automated local run flattened the public PHerc0814 surface `20250929040153-auto_grown_20250929040153260`, using `--keep=1.5`, 50 iterations and the default symmetric-Dirichlet energy. The output's valid point count increased from 21,445 to 32,773 out of 41,349 valid input points, while the reported final mean L2 stretch remained 1.00064.

**Before:** `meshGrid(coarse)` supplies row/column indices in the decimated grid. Applying the original tifxyz scale directly makes initial UV distances too small by the stride (8 in this example). The disconnected pieces can expand over one another during optimisation.

**After this PR:** Multiply each coarse index by the stride before applying the original surface scale. At stride 1 the calculation is unchanged. This is a unit correction, not a component-packing algorithm or a guarantee that every input cell survives decimation.

**Proof:** Same input, settings, compiler and one-thread environment:

| Measurement | Main | This change |
| --- | ---: | ---: |
| Initial mean L2 stretch | 8.25439 | 1.0318 |
| Final mean L2 stretch | 1.00064 | 1.00064 |
| Output valid grid points | 21,445 | 32,773 |
| Input quad centres farther than 20 voxels from every output vertex | 19,062 / 39,312 | 9,483 / 39,312 |
| Input quad centres farther than 40 voxels from every output vertex | 12,823 / 39,312 | 6,388 / 39,312 |

Attach `20261111-coverage.png`: it shows the same original input grid in all panels. Red marks input quad centres more than 20 CT voxels from the nearest output vertex. This includes losses from coarse-grid sampling and UV lifting; it is not the issue author's non-collapsed-UV cell statistic.

An independent verifier re-read the saved TIFFs and reproduced the valid-point and quad-centre counts with exhaustive pairwise distances, separately from the original KD-tree calculation. The verifier did not rebuild or rerun flatboi. With `--keep=100`, the saved x/y/z TIFFs are byte-identical between both executables. The existing SLIM assembly checks passed. These are correctness runs from a QuickBuild O0 build; no speedup is claimed.

**Why / where this is useful:** Flatboi is used to flatten stored tifxyz surfaces, including through VC3D's SLIM flatten dialog. Restoring the correct initial units avoids one cause of material disappearing from decimated output. The attached case still has substantial losses, so users should not read a normal final stretch metric as proof of complete coverage.

**Human-authored commentary:** Not yet supplied.

- [ ] I personally verified that the example and proof above were produced by this PR on the stated data.

## Details

This implements the stride correction investigated by **alpaltian in [#2500](https://github.com/ScrollPrize/villa/issues/2500)**. The diagnosis and their 18-surface/20-surface experiments are their work. The figures above are a separate automated reproduction on the issue's main public input, not a claim to have discovered the cause.

Tested base: `7ad02f4f6e306b744ef6d2742dfe31fd55713ee5`. Distribution patch: `initial-uv-units-lf.patch` (SHA-256 `63a0bbf05520ca68d8f0602d4c296639e0e5b47f693217984c5a088354691874`). Only the TC initialisation in `volume-cartographer/libs/flatboi/flatboi.cpp` changes. The source grid, XYZ coordinates, target scale, SLIM energy, iterations and UV-lifting procedure remain the same.

Input prefix:
`https://vesuvius-challenge-open-data.s3.amazonaws.com/PHerc0814/segments/20250929040153-auto_grown_20250929040153260/mesh/intermediate/tifxyz_original/`

Download `meta.json`, `x.tif`, `y.tif`, `z.tif` (1,110,638 bytes total). For each executable:

```sh
WANDB_DISABLED=true OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PASTIX_NUM_THREADS=1 \
  flatboi INPUT --output=OUTPUT --keep=1.5
```

Repeat with `--keep=100` for the unchanged-path comparison. Use separate output directories.

Build: WSL Ubuntu 24.04, GCC 13, CMake 3.28.3, CPU-only, `QuickBuild`, `VC_QUICKBUILD_OPT_LEVEL=0`, `VC_BUILD_APPS=OFF`, `VC_BUILD_FLATBOI=ON`, `FLATBOI_BUILD_SLIM_TESTS=ON`, `VC_READER_ENABLE_CUDA=OFF`, `VC_OBJECT_STORE_BUILD_SERVER=OFF`. The exFAT build volume cannot create the native-header symlink, so generated header copies were replaced with includes of their unchanged originals for both executables. No such workaround is part of this patch.

Limitations: one public surface independently exercised here so far. The original report includes broader tests, but those are not counted as our verification. Point distances are not surface correspondences or area-weighted coverage; nearby distinct pieces can count as neighbours. The final L2 means agree at the printed precision, while Area Error differs slightly (0.017604 versus 0.0176075). Decimation still loses small components/boundary detail, UV lifting still reports 225 triangles without flattened UVs, and coarse initialisation changes can affect which local optimum is reached even for one connected piece. The patch does not solve those issues.
