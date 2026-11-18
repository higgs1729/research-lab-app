# Reject incomplete manual crops in vc_render_tifxyz

Local draft. AI-assisted preparation. The human example, motivation, verification and screenshots remain to be supplied.

**In one sentence:** A mistyped manual crop fails immediately with a message telling the operator to supply both positive dimensions.

**One real example:**

**Before:** In a recorded research test on PHerc0814, omitting `--crop-height` from a 128 × 128 crop selected the 13,600 × 3,440 canvas. The instrumented run stopped at crop selection.

**After this PR:** The same incomplete crop is rejected before opening the input. With both dimensions supplied, the saved real-CT run rendered three 128 × 128 TIFFs. All three matched the saved reference by SHA-256 and decoded pixels.

**Proof:**

**Why / where this is useful:**

- [ ] I personally verified that the example and proof above were produced by this PR on the stated data.

## Details

The patch validates the four manual crop values before opening the inputs. All-zero defaults, valid manual crops, and the help and TIFF merge entry points retain their existing paths. The existing regression harness exercised 18 cases in the prior investigation. Nine invalid cases failed before opening input.

The renderer source after application to villa main `14d4e725df8b569e6fc8ceb3c04d130f705c1565` matches the source compiled for the saved real-data test. The historical test used its existing build dependencies. A fresh build of the fixed main and pre/post terminal screenshots are pending. See the local reproduction notes for the research evidence.
