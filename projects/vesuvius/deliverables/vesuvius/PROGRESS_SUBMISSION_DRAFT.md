# November 2026 Progress Prize — draft, not submitted

Official form: https://docs.google.com/forms/d/e/1FAIpQLSeB6MC_--4UCCEGc3zalX57-uE4puRcE_vJoYJCrEt4uYaaaw/viewform

This draft uses the independently verified geometric and local CT results. The upstream PR route has separate human-use and review requirements; this submission proposes an independent public contribution and does not claim to meet those PR requirements.

## Submission fields

Full name: 竹内智哉

Email: use the verified submitting account; not yet selected or entered.

Team description: Individual research effort using AI agents for investigation, implementation and verification. A separate AI agent checked the implementation and saved experiments. No human collaborator, human use of the tool or human code review is claimed.

Discord display name: not established; leave the optional field blank.

Public contribution URL: not yet published. Intended repository: `higgs1729/vesuvius-flatboi-component-packing`. Prepared release: `flatboi-component-packing-release-20261112`. The earlier private product snapshot remains immutable.

Contribution:

> This change adds an optional `--pack-components` flag to flatboi. When disconnected surface pieces overlap after flattening, rasterization can discard samples from one piece and connect adjacent output samples from different pieces. The flag translates the pieces into separate horizontal intervals before the existing rasterizer runs, while retaining their source XYZ, faces and SLIM settings. It is off by default.
>
> The experiments used two public PHerc0814 meshes: `20250929040153-auto_grown_20250929040153260` and `20250928235953-auto_grown_20250928235953722`, at full resolution with five SLIM iterations. Cross-component raster rejections fell from 189 and 399 to zero; adjacent output grid edges joining different components fell from 106 and 284 to zero. The output becomes wider. Within-component overlaps remain, including one and 356 observed rejection pairs.
>
> A local CT comparison follows one edge selected before viewing the scan: the before image contains 1,280 pixels interpolating between components about 304 scan voxels apart; the after crops have no mixed pixels. A separate AI agent checked all 39,760 valid CT samples and the 15 output TIFFs. The crops track original faces rather than being pixelwise aligned. Whether the second component follows one correct papyrus sheet remains unresolved.
>
> This gives users a single explicit option for separating disconnected pieces within the existing flatboi pipeline. Evidence includes real CT images, an ownership image, public input URLs/hashes, a one-file patch, separate observation patches, measurements and build/run instructions. Ink readability, human adoption and improvement on every surface have not been established. The evaluation code supports this product change and is not the standalone contribution. The original implementation additions are offered under MIT; modified upstream Volume Cartographer retains GPLv3, and the scan-derived material retains the dataset terms.

## Items to resolve before submission

- Obtain explicit authorization for public release and external submission, including the prepared licensing scope. The form's terms checkbox has not been selected.
- Publish the prepared contribution to the stated GitHub account and put the verified resulting URL in the form.
- Use the verified submitting email/account. Name is taken from the user's maintained identity record; the optional Discord field remains blank.

No form has been filled or sent and no message has been sent to the organizers. The contribution's eligibility and any award are the organizers' decision.
