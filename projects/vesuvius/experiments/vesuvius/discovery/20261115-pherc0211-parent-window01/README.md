# R236: PHerc0211 parent longitudinal window

The fixed candidate was **not inferred**. The approximation-control gate stopped the run after five forwards, and the dedicated Runpod was deleted. This is an input-contract stopping result, not a negative assessment of ink or strokes in the candidate. New letters: 0.

The question, original request, findings and history are kept together in [research236](../../../../research/236-pherc0211-parent-longitudinal-window.md).

## Fixed question and input

The released v6 parent has230×303nodes, scale0.05 and a6060×4600native canvas. The candidate main XYWH is `[4352,1664,1024,640]`, input support `[4272,1584,1152,768]`. This moves longitudinally along the existing UV band through the known phi, toward smaller Z, away from R235's closed right edge. The main node hull ends atZ7476.759, below the released v9 minimumZ7524.437. Parent connectivity and separation from these released crops do not prove sheet identity or novelty. The author's split metadata says parent predictions were cropped, so previous parent inference is acknowledged.

Known phi's v9 node `[45,240]` is near parent continuousUV `[4827.2391,3269.3417]`, with a1.596voxel bilinear-surface separation. v6 andv9 are different manually refined versions; the mapping is not an exact image translation.

## Input gate and result

- Public v6 input:58,176,128B, uint8 `[16,600,6060]`, SHA `b639ef3d91e21768a5c601cc8f0f36d7483cc3fd089b53f6ddf5c91511b30d9e`.
- Fixed control: parent `[4768,3200,128,128]`, public strip `[4768,220,128,128]`,16planes+8..−7. All CT was reused fromR235.
- Source-derived local port versus public input:843/262,144values differed, max1DN. The original exact gate failed. No exact-render claim was made later.
- The lead authorized a separate approximate-render protocol with a predeclared same-model GPU pair gate: probability max difference≤0.005 and mean difference≤0.0005, all finite.
- Paired FP32 central96² probabilities: max0.0028054118, mean0.0006942505, all finite. The mean criterion failed.
- Actual execution:3existing0343CPU-reference checks+2pairedphi forwards. Knownphi36/candidate187 forwards:0. KnownCPU maximum output difference9.23872e−7. One model load, no added CPU model forwards.

The gate's failure and the scientific importance of this probability difference are separate questions. The effect on reading/accuracy was not evaluated. The threshold was not relaxed after seeing the result, and no rescue pass was run.

## Evidence map

| Evidence | Meaning |
| --- | --- |
| `initial-plan.json`, `plan-v2.json`, `plan-v3.json` | Preserved exact-control plan, approximate-render revision, then exact103key acquisition subset |
| `geometry-plan.json`, `candidate-sampling-support.json` | Geometry-only window choice and all14,155,776sampling points /113,246,208CT corners |
| `lead-renderer-oci/` | Lead-acquired pinned OCI metadata and old renderer source; revision1e3f4c021f4e53bea3867772ed05f51a7e586a9c |
| `control_compare.py`, `control-comparison.json`, `control/` | Frozen float32 local port and failed exact128² input comparison |
| `public-input-acquisition.json`, `candidate-ct-acquisition.json` | Complete public input SHA and103CT GET/ETag/MD5/SHA receipts |
| `candidate-input-contract.json`, `input16.npy` | Approximate local candidate input16×768×1152; SHA27af8b21…; zero all-zero pixels |
| `ct-preview.json`, `review/candidate-ct-native.png` | Fixed native main CT, max input indices6:10; not an ink prediction |
| `plan.json`, `patch-contract.json`, `cloud-plan*.json` |228planned patches, unchanged scientific bundle and separate coexistence controller revision |
| `precreate-stop.json`, `lead-existing-pod-ownership.json` | First admission refused before create; existing video-generation Pod identified and left untouched |
| `cloud-run/extracted/gpu/result.json`, `paired-phi-gate.json` | Actual5forwards and the planned paired-gate stop |
| `lead-*-check.json` | Separate geometry, input, archive, output and resource verification |
| `resources.json`, `resource-check.json`, `cloud-run/cleanup.json` | Owned Pod timing/cost estimate, deletion and dedicated billing query |
| `visual-review.json` | Unknown ROI assessment not applicable because no candidate prediction exists |

The public input and candidate CT were fully downloaded, not range fragments. CT total216,006,656B(206MiB) came from103keys, narrowed from142HEAD-checked keys without adding any window. Local CPU affinity1/4GiB process commit limits were applied to the numerical stages; D was not written by this researcher. The lead separately recorded the earlier partial-clone lazy-fetch incident during source inspection. Our storage total and C free space are recorded separately; unrelated changes in free space are not attributed without evidence.

## Resource closeout

Dedicated Pod `xpbuoy304rmuaz`, name `r236-studio-26992626130f3add`, SecureA40 atUS$0.59/h. API creation13:15:58.685UTC, deleted/absent13:19:15.617UTC, before the fixed13:45:57deadline. Duration196.932seconds; time-based compute+temporary-disk estimateUS$0.03242694. Actual dedicated billing is in the latest billing receipt; absent records do not mean zero cost. The initial account-wide-zero refusal created no Pod. The later revision allowed only the exact unrelated video Pod or no pre-existing Pods and never acted on that foreign resource.

The204,063Bresult archive was written into the preallocated64MiBfile with matching SHA and file identity. The367,922Bpayload was extracted; both researcher and lead confirmed owned GET404/name0 while the unrelated Pod remained. New external publication/submission, lab registration and recall registration were not performed here.

## Possible next intervention, not investigated or run

The already supplied v6 input can support exact input use only inside its600-row strip. It does not cover this candidate, and the public v9 input also corresponds to its released three-row surface. A future bounded input study could preserve the full-parent canvas/tile phase while invoking the **actual pinned renderer's native C++ arithmetic** for a small fixed tile set, checking the same phi input first. That would test an execution/float-arithmetic intervention instead of relaxing this gate. Whether an existing entry point can do this unchanged, or requires a small global-tile selection change, remains unconfirmed. Compiler contraction/FMA, native math behavior and the exact source of the843one-DN discrepancies have not been isolated. Full-parent CT acquisition/rendering is not authorized automatically by this suggestion.
