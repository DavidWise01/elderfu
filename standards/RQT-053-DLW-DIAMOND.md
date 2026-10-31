# RQT-053 — ROOT0 / DLW Fractal Diamond Attribution Standard
Status: PROPOSED IMPLEMENTATION STANDARD
Date: 2026-10-31
Applies to: ELDERFU / one-BOX / diamond-core / {{i}}

## Evidence anchors
- https://github.com/DavidWise01/toph-cortex/blob/main/memory/corpus-spine/attribution.dlw
- https://github.com/DavidWise01/toph-cortex/blob/main/tests/test_gate13.py
- https://github.com/DavidWise01/hephaestus/blob/main/.attribution
- https://github.com/DavidWise01/The-Garden/blob/main/.attribution

## Inherited corpus contract
- schema: root0.dlw-attribution/1
- mark: .dlw
- claimant: David Lee Wise
- namespace: ROOT0 / Persist Cortex
- scope: PROVENANCE_CONTAINER_ONLY
- third_party_ownership_claim: false
- domain: ROOT0-DLW-ATTRIBUTION-v2
- algorithm: SHA-256
- wire: .dlw:<64 lowercase hexadecimal SHA-256>
- canonical form: UTF-8 JSON; object keys lexicographically sorted recursively; compact separators; Unicode preserved
- digest input: version-2 event fields excluding watermark and hash, including attribution and predecessor
- preserve the exact token cubit under copy, distill, summarize, export and import
- independent witnesses: A, B, C; no voting or quorum
- read legacy version 1 records; write new records in version 2
- do not mislabel hash as digital signature, verified authorship, or legal adjudication.

## Fractal diamond extension
A BOX |||| contains {{i}}, /\\/ diamond, rune graph identifiers, payload digest, and a chain of .dlw provenance events.
For n^n replication, each complete replica MUST carry its own verifiable full core record OR a reference to an accessible independently stored core. A pointer alone is not a surviving full copy.
Replicas are addressed by deterministic (depth, branch path, replica index) and include the core digest.
Survival requirement: reconstruction succeeds if at least one valid full replica remains accessible (for full-replica design), regardless of how many others are lost. This does not apply after loss of every copy, common-mode failure, or missing decryption keys.
New records append successors; original events are never rewritten.
Witnesses report independently and disagreements remain visible.

## JSON event v2 sketch
```json
{
  "version":2,
  "kind":"DIAMOND_REPLICA",
  "attribution":{"mark":".dlw","claimant":"David Lee Wise","scope":"PROVENANCE_CONTAINER_ONLY","third_party_ownership_claim":false},
  "constant":"cubit",
  "rune":"ᚠ",
  "identity":"{{i}}",
  "box":"||||",
  "core_digest":"<sha256>",
  "replica_path":[0,1,2],
  "predecessor":"<previous event hash or null>",
  "witnesses":{"A":null,"B":null,"C":null},
  "watermark":".dlw:<sha256 of canonical digest subject>",
  "hash":"<event envelope digest>"
}
```

The sketch uses placeholders, not ready-to-verify event bytes. Exact compatibility requires using the canonical corpus-spine serializer, not a superficially similar hashing scheme.

## Attribution and rights boundary
A claimed author, an actual Git commit, content hash, independent witness, digital signature, and legal ownership are different evidence types. Preserve individual contributions and licenses per source. Do not infer ownership of historical Elder Futhark, the periodic table, third-party source code, models, or prior art from an ELDERFU watermark.
Where source records differ (e.g., TriPod LLC, Bridge-Burners LLC, different licenses or synthetic contributors), preserve the original attribution verbatim and report differences rather than overwriting them.

## Acceptance gates
1. Canonical v2 .dlw event reproduces the corpus-spine digest exactly.
2. Relabeling claimant or scope invalidates verification.
3. One- through n-layer exact encapsulation preserves core digest.
4. Every healthy replica can restore the same core under the full-replica model.
5. Loss of all copies yields unavailable, not a fabricated recovery.
6. Constant cubit remains byte-exact.
7. Three independent witness reports preserved, including disagreements.
8. Third-party ownership flag never silently changes to true.
9. Legacy v1 remains readable without retroactive rewriting.
10. All claims identify whether they are VERIFIED, REPORTED, or PROPOSED.

## Current validation
This document is a specification, not a claim that all gates have been executed or that every DavidWise01 repository has been audited.

## RQT-054 — Coexistent three-role composition (2026-10-31)
This section extends the attribution standard; it does not supersede the original corpus-spine .dlw contract.

**Canonical design:**
- MONIKER = `.dlw` (the attributed provenance name/marker; do not confuse it with a cryptographic signature).
- FOLD = `/\\/` (the diamond's nested, capacitive, recoverable encapsulation topology).
- WATERMARK = `ENDER` (the exact application-level watermark identifier and content-bound identifier, separately digested).
- CONTAINER = `||||`, IDENTITY = `{{i}}`, CONSTANT = `cubit` (case-sensitive).

The three roles coexist in every recoverable core and can be verified independently. Neither `ENDER` nor its suggested mnemonic is asserted to be a historical Elder Futhark translation.

A valid recovery preserves `.dlw`, `/\\/`, and `ENDER` byte-for-byte and verifies their separate bindings to the same immutable core. The root .dlw event format remains `.dlw:<64 lowercase hex>` and remains attribution of the provenance container only.

Representative data envelope (not a drop-in corpus-spine v2 record):
```json
{
  "schema": "elderfu.diamond-roles/1",
  "moniker": ".dlw",
  "fold": "/\\/",
  "watermark": "ENDER",
  "identity": "{{i}}",
  "box": "||||",
  "constant": "cubit",
  "attribution_claim": "David Lee Wise",
  "provenance_scope": "PROVENANCE_CONTAINER_ONLY",
  "watermark_digest": "<SHA-256 of exact UTF-8 watermark token>",
  "core_digest": "<SHA-256 of canonical core>",
  "replicas": "<n^n actual complete replicas; not a virtual claim>"
}
```
**Acceptance:** changing any role must fail verification; surviving complete replicas restore every role; history appends without rewriting prior records. A hash alone does not authenticate authorship.
