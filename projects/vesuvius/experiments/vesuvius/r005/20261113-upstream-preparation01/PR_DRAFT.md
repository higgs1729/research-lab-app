# Optional component packing in flatboi

**In one sentence:** Let users place disconnected surface pieces side by side before rasterization with the opt-in --pack-components flag.

**One real example:** <!-- Author to describe their own use on real scroll data and what happened. -->

**Before:** In two PHerc0814 surfaces flattened at full resolution, disconnected pieces landed on top of or next to each other in the output grid.

**After this PR:** The flag translates each connected piece in UV after the solver runs. It preserves the source XYZ and mesh connectivity. The output can be wider, the sampling grid can shift, and overlaps within a piece can still occur.

**Proof:** In the automated before and after measurements, grid edges joining different pieces fell from 106 and 284 to zero, and raster rejections between pieces fell from 189 and 399 to zero. At one edge selected from geometry before viewing the CT, 1,280 pixels in the before crop mixed support from two pieces. Each separate after crop had zero mixed pixels. The crops track the same source faces through different output grids. The comparison figures show source ownership and rendered CT, with paper correspondence for the second piece still unresolved.

<!-- Attach the author's actual before and after screenshots. The existing ownership and CT images are automated comparison figures. -->

**Why / where this is useful:** <!-- Author to write the use case in their own words. -->

- [ ] I personally verified that the example and proof above were produced by this PR on the stated data.

## Details

The patch changes only flatboi.cpp and applies to villa main 14d4e725df8b569e6fc8ceb3c04d130f705c1565. The flag defaults to off. The tested product source matches the applied source, and the counts used separate observation builds. The initial UV stride behavior reported in #2500 is outside this change. Readability has not been established. AI assisted preparation and automated verification.
