Thank you for publishing the PHerc0211 meshes, inputs, and inference code.

The line2 mesh archive contains a parent record for `PHerc0211-crop1711-manual-20261026-1237-legacyuv20-v6`. In `mesh/parent/results.json`, `models.studio` records a full-parent output of shape `[4600,6060]`, with:

- probability SHA256: `0bf20b28456e449568b55ffdf4f51f87ace093cbc66f4e7a23b9a0547070f3e1`
- checkpoint SHA256: `ffffbf4fcb2f1eb91940a6899366cd0d22b2ea03987270d07dc2a205dbd91145` (the public Studio epoch 9 weights)
- geometry SHA256: `7ca0b190874dd574f08c9caf257e85d6b28250d4f1295bb03596975bbf5c36bd`

Is this historical full-parent probability map, with its coverage mask, available publicly? I found the current soft-loss line2 TIFF and the separate v9 map, but could not locate this older full-parent output. If available, a link and clarification of whether the recorded probability hash covers the serialized file or raw array bytes would help.

I am checking parent ROI `XYWH [4416,2048,384,256]` (half-open array slice `[2048:2304,4416:4800]`). Is there a published annotation or prior reading covering this region? It lies outside the distributed line2 crop, but that alone does not establish novelty. I have not confirmed new text there.

An existing reference would be very helpful; no new computation is requested.
