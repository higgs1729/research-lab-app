# Grid-preserving component packing for flatboi

Local review supplement for R005. The optional --pack-components-preserve-grid mode places disconnected pieces in separate horizontal intervals. It keeps the original UV-to-grid mapping, then shifts the rasterizer's snapped coordinates by whole X cells. The existing integer edge tests and interpolation weights still apply. Source XYZ, triangle order and the TIFXYZ format stay the same. Output width can increase, and overlaps within a piece can remain.

## Apply and build

Use a clean villa checkout at 14d4e725df8b569e6fc8ceb3c04d130f705c1565 and create the checkout with core.autocrlf=false and core.eol=lf so the touched files use LF before applying patches. KIT points to the extracted supplement. The first patch is the frozen R005 implementation. The second adds the grid-preserving mode.

~~~sh
git rev-parse HEAD
git -c core.autocrlf=false -c core.eol=lf apply --check "$KIT/patches/01-pack-components.patch"
git -c core.autocrlf=false -c core.eol=lf apply "$KIT/patches/01-pack-components.patch"
git -c core.autocrlf=false -c core.eol=lf apply --check --whitespace=warn "$KIT/patches/02-preserve-grid.patch"
git -c core.autocrlf=false -c core.eol=lf apply --whitespace=warn "$KIT/patches/02-preserve-grid.patch"
~~~

The second patch preserves one trailing space from an existing logging statement. Git reports it in strict whitespace checks. Preserve the recorded bytes when verifying the hashes. [Preimages, postimages and patch hashes](SOURCE_HASHES.json)

Configure a fresh Volume Cartographer build following the fixed upstream instructions. Build the shared rasterizer definition and every binary that instantiates the changed UvGridRasterizer class from the same patched header. The CMake flatboi target depends on vc_core. If using vc_obj2tifxyz with that build, build it there as well. Keep the resulting binaries and libraries together. [Upstream build instructions](https://github.com/ScrollPrize/villa/blob/14d4e725df8b569e6fc8ceb3c04d130f705c1565/volume-cartographer/README.md)

~~~sh
cmake --build "$VILLA_BUILD" --target flatboi --parallel 1
FLATBOI="$VILLA_BUILD/bin/flatboi"
"$FLATBOI" "$SEG" --output="$DEFAULT_OUT" --keep=100 5
"$FLATBOI" "$SEG" --output="$LEGACY_OUT" --keep=100 5 --pack-components
"$FLATBOI" "$SEG" --output="$GRID_OUT" --keep=100 5 --pack-components-preserve-grid
~~~

Use separate new output directories. The two flags are mutually exclusive. SEG is a local TIFXYZ directory containing the four files from a selected input manifest. For recorded CPU conditions, pin to one CPU and set OMP_NUM_THREADS, OMP_THREAD_LIMIT, OPENBLAS_NUM_THREADS and PASTIX_NUM_THREADS to 1. The recorded runs used one CPU, a 4 GiB address-space limit, core dumps disabled, and a separate network namespace.

The saved WSL Ubuntu 24.04/GCC 13 experiment compiled flatboi.cpp and SurfaceMeshing.cpp with the same changed header and linked both objects into a separate ELF. It borrowed existing dependencies for other symbols. The added class members change its layout. Replacing only an old shared library could mix callers and definitions from different builds. The fresh CMake commands above describe the ordinary source-build route. The recorded result used the isolated ELF and its existing local dependencies.

In the saved build, an existing comment's superscript ² was misencoded in SurfaceMeshing.cpp. The packaged patch restores the upstream character. For each of the product and observation variants, the historical before/after preprocessing check produced identical bytes with comments removed. The exact source and preprocessor SHA-256 values are included. [Build provenance](SOURCE_HASHES.json)

## Evidence

Two PHerc0814 surfaces were run with keep100 and five SLIM iterations. Independent enumeration of every source triangle checked ownership, XYZ and weights. Both surfaces also ran on the product ELF and its XYZ TIFFs matched the observation build. The first surface's default and legacy packing modes were checked against their saved controls.

| Measurement | PHerc0814 first surface | PHerc0814 second surface |
| --- | ---: | ---: |
| Grid height × width | 172×553 → 172×683 | 252×2637 → 252×3033 |
| Original owners with the same source face and XYZ bits at the translated grid positions | 40,944 | 254,263 |
| Packed owner cells with matching weights and XYZ bits | 41,133 | 254,662 |
| Cross-component rejections | 189 → 0 | 399 → 0 |
| Same-component rejections | 1 → 1 | 358 → 358 |
| Newly exposed owner cells | 189 | 399 |

For the single-component PHerc0139 w035 surface, the default and grid-preserving product runs at keep100 and five iterations had the same 286×259 grid, 62,646 valid samples, three XYZ TIFF file hashes, decoded float32 bits, scale and SLIM energy. The generated metadata differed only by output UUID.

On one selected 64×64 PHerc0814 CT window, pure support for the two tracked pieces covered 1,408 pixels each. Across five depth offsets, all 14,080 corresponding sample positions, pre-rounding CT values and final pixels matched bit for bit. The original 1,280 mixed-support positions became invalid in both translated crops. Blue in the central-layer comparison marks invalid support. [CT comparison figure](images/ct-preservation-center.png)

The CT comparison covers one window and the linear surface interpolation path. The second piece's physical sheet correspondence and readability remain unresolved. Other windows, bicubic rendering, keep below 100, object-store use and extreme input ranges remain untested here. The figure comes from measured scan data and rendered output. Human use and terminal screenshots are outside this evidence. [Recorded metrics](RESULTS.json) · [Data and attribution](DATA.md) · [Optional observation and CT reproduction](OBSERVATION.md) · [Licenses](LICENSE_SCOPE.md)
