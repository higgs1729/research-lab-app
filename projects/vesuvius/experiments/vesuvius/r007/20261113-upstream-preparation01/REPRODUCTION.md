# R007 reproduction on saved PHerc0814 data

The research fixture uses the PHerc0814 CT crop and segment named in [small-render-process.json](../20261112-crop-input-guard01/run01/small-render-process.json). The original invocation and time bounds are recorded there. Use a fresh writable output directory for any repeat.

1. On a local checkout at `14d4e725df8b569e6fc8ceb3c04d130f705c1565`, confirm `git apply --check R007.patch`. For a new comparison, prepare separate before/after renderer binaries using the existing volume-cartographer build. The research application check reused the source and executed neither build.
2. For the archived before result, read [baseline-observe-missing-height.log](../20261112-crop-input-guard01/run01/baseline-observe-missing-height.log). The instrumented baseline stops after selecting a crop. To repeat that observation, use the saved `baseline-observe` binary with the real data and the [R116 command record](../20261112-crop-input-guard01/run01/baseline-observe-missing-height-process.json). It reports 13,600 × 3,440. Keep this bounded observation separate from a production before run.
3. With the patched renderer, run the saved real-data command below first without `--crop-height 128` and then with both dimensions. The incomplete invocation should exit 1, show the manual crop diagnostic and produce no image. The complete invocation should produce three TIFFs at 128 × 128. Compare their SHA-256 and pixels against the reference paths in the [independent audit](../20261113-crop-input-verification01/audit-02/result.json).

```bash
vc_render_tifxyz --volume "$ct" --segmentation "$segment" --tif-output "$new_output" \
  --scale 1 --group-idx 0 --num-slices 3 --slice-step 1 \
  --voxel-size 9.362 --voxel-unit micrometer --cache-gb 1 \
  --crop-x 7356 --crop-y 2272 --crop-width 128 --crop-height 128
```

The [saved 18-case check](../20261112-crop-input-guard01/check_cli.py) takes a patched renderer binary as its only positional argument. The saved before case measures selected dimensions. The product after case records early refusal, and the complete-crop case records real output. Actual terminal captures and the submitter's own use, motivation and attestation remain pending.
