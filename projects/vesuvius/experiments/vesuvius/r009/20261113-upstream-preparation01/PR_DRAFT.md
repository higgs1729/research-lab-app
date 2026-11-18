# Resume single-part Zarr renders with missing pyramid levels

**In one sentence:** Resume a single-part Zarr render from its existing level 0 when pyramid initialization was interrupted, and get accurate OME metadata when the pyramid is disabled.

**One real example:** <!-- Author to supply their own use of the tool on real scroll data and the observed result. -->

**Before:** In the recorded PHerc0139 w035 case, the renderer resumed from an output containing only the group and level-0 array metadata. It wrote level 0 and exited with code 1 when it tried to write the missing level 1. With the pyramid disabled, the renderer also listed levels 1–5 in OME metadata even though it created only level 0.

**After this PR:** The resume path initializes missing arrays using the existing level-0 layout and codec and retains existing array metadata. With the pyramid disabled, the OME dataset list contains only level 0.

**Proof:** Automated tests used a 64 × 64 × 28 crop of real PHerc0139 w035 CT. For two copies of outputs saved at debugger stops, the candidate resumed with exit 0, and all 14 output files matched the uninterrupted run by SHA-256. The OME dataset list matched the six arrays present. On the level-0-metadata-only copy, the baseline exited with code 1 and reported “no Zarr array to write” for level 1. A separate run confirmed the level-0-only OME result for both a render and a metadata-only --pre run with the pyramid disabled.

<!-- Attach actual before and after screenshots from the author's verification, using the same scroll input and settings. -->

**Why / where this is useful:** <!-- Author to describe in their own words the scroll work that exposed this problem and why the fix helps. -->

- [ ] I personally verified that the example and proof above were produced by this PR on the stated data.

## Details

The single-part --resume path checks the existing level-0 shape, chunks and dtype before creating missing levels. The existing native pyramid helper and its Python binding expose the preservation mode, and the default call behavior remains the same. Lower-level pixels may be recomputed during resume.

The patch was checked against villa main at 14d4e725df8b569e6fc8ceb3c04d130f705c1565. The automated CLI evidence comes from an earlier build containing these changes and a separate crop validation change. The recorded crop supplied both positive dimensions. The modified pyramid implementation and header match the tested sources. The real Python extension, wrapper and regression-test body ran in isolation on Ubuntu CPython 3.12. The fixed main build and normal Python package installation remain to be exercised.

The interruption evidence covers two debugger stops with a single uncompressed level-0 chunk. The process's OS termination signal remains unconfirmed. Partial chunk writes, power loss and multi-part recovery were outside the test. AI assisted preparation and automated verification.
