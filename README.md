# ELDERFU — Rune Quanta Vertex Laboratory

Source: [index.html](./index.html)

Proposed live address (requires Pages enabled): https://davidwise01.github.io/elderfu/

## RQT-045 — Minimum Cycle Redundancy for Fault Localization
For cycle-check matrix C and additive edge-error vector δ, the observed syndrome is σ = Cδ. A single unknown nonzero fault is uniquely localizable only when every eligible edge has a nonzero syndrome column and distinct columns are pairwise nonproportional. Detecting an error does not itself correct it.

## Model boundaries
- Elder Futhark 24-glyph order mapped to atomic numbers Z=1–24 as a **modern encoding convention, not a historical chemical relation**.
- Standardized illustrative glyph strokes are split into endpoint/junction/crossing vertex graphs.
- The logical address space is 1 × 4 × (6 × 4)^3 × 1 = 55,296 sites.
- A sampled 4D-to-2D Canvas visualization is used for performance.
- Three isolated observation-only witness channels, with JSON export of session history.
- Runnable deterministic self-tests. The full rune-lattice fault-localization problem is not yet validated.
- No physical quantum or chemistry claim.

## Activate GitHub Pages
Repository Settings → Pages → Build and deployment → Deploy from a branch → **main** → **/(root)** → Save.

Commit of index.html does not itself confirm that GitHub Pages is enabled. The connected GitHub API cannot configure Pages for this repository.


## RQT-046 — Evidence-preserving reconstruction
- Interactive section in index.html: Reconstruction Without History Rewrite.
- For observed syndrome σ, seek a one-edge additive correction δ̂ satisfying Cδ̂ = σ.
- A unique nonzero syndrome signature permits proposing a correction under the single-fault model; proportional signatures are ambiguous and held.
- A zero corrected syndrome verifies the cycle checks only, not the truth of the proposed error cause.
- Append derived observations; do not overwrite original witness reports. JSON session export available.
- The fixture is four vertices and five edges; full 55,296-site validation is not claimed.
- App commit: cd604ba6c6251bc219b2d75173fd8a822807c38a.

GitHub Pages availability has not been confirmed. If needed, enable Pages under Settings → Pages using main and /(root).

## One BOX — Rune Vertex Transport Interpreter

Open [one-box.html](./one-box.html) or the Pages address https://davidwise01.github.io/elderfu/one-box.html (when Pages is enabled).

24 Elder Futhark symbols serve as language tokens and geometric transport graphs inside one containment BOX `||||`. Vertices are selectable addresses, strokes become legal graph edges, and each successful edge traversal creates an append-only witness event. Source supports selection, stepping, automatic transport, simple program interpretation, and JSON exports. No transport outside the BOX or through absent edges is permitted. This is an experimental computational model, not historical rune programming or physical quanta.


## RQT-048 — {{i}}-framed rune vertex transport
The One BOX interpreter at [one-box.html](./one-box.html) now accepts nested-looking identity frames using the syntax:

```text
{{i :: ᚠ :: @1 :: ? :: !}}
{{i :: ᚢ :: @1 :: ? :: !}}
```

- `{{i}}`: identity-bound interpreter frame.
- Rune glyph: select one of 24 deterministic local vertex/stroke graphs.
- `@n`: address an existing local rune vertex.
- `>n`: travel only across an existing stroke edge.
- `?`: append an observation.
- `!`: append independent A/B/C witness provenance.
- An invalid instruction produces a HOLD event and stops processing the frame stream.
- The model keeps one BOX `||||`, no unvalidated cross-rune teleportation, and no physical quanta claim.

The application is accessible as source at [one-box.html](./one-box.html); GitHub Pages requires deployment configuration.

## RQT-049 — Explicit inter-rune vertex handoff

Single-BOX `{{i}}` program syntax: `{{i :: ᚠ :: @1 :: ? :: =>ᚢ@1 :: ? :: !}}`. The new `=>ᚢ@1` instruction declares a directed inter-rune handoff from the current source vertex to vertex 1 of rune ᚢ. Both endpoints must exist; invalid or degenerate bindings HOLD. Each successful handoff is logged as one event with exact source/destination addresses, still inside `||||`. Selecting a rune glyph alone is not a transport event. This is a defined software language, not a physical mechanism. The target page is `one-box.html`; live Pages access remains unverified.

## RQT-050 — Authorized reverse transport

The One BOX `{{i}}` language now supports `<=ᚠ@1` as a reverse operation for a prior explicit `=>` handoff. A forward handoff generates a one-use reverse authorization for its exact source and destination vertex pair. Unmatched reverse commands HOLD; successful reverse operations append new events and consume authorization. Example: `{{i :: ᚠ :: @1 :: =>ᚢ@1 :: ? :: <=ᚠ@1 :: !}}`. This demonstrates reversible location under a simple address model, not invertible physical transport, and does not erase earlier events.

## RQT-051 — Diamond core watermark engine

Pivot: One BOX `||||` contains a `/\\/` diamond-core identity watermark. [Run the engine](./diamond-core.html). Core binds `{{i}}` identity, rune sequence, payload and SHA-256 digests. Explicit nested wrappers form a forward hash chain and can be repeatedly added and removed; import/export and intentional tamper testing are supported. Observations append to a session-local event ledger. This guarantees neither preservation after arbitrary destructive transformations nor authorship authentication; use a trusted digital signature and external timestamp for those stronger claims. The detailed standalone prototype also exists as a conversation artifact. Previous rune transport labs remain available.


## RQT-052 — Capacitive fractal diamond, n^n replication
The diamond watermark engine in [diamond-core.html](./diamond-core.html) now includes a bounded **physical in-memory replica** experiment with n^n complete copies for n=2…5 (4, 27, 256, 3,125). Any one intact, SHA-256-verified copy can restore the core; loss of all copies eliminates recovery from this set. The UI supports charging, losing one, losing half, losing all and recovering. Each action appends an observation to the session history. This n^n scaling is a chosen redundancy architecture, not an emergent mathematical guarantee of tamper resistance. Correlated failures can destroy every replica together. Replicas are session-local and are not currently included in the engine's JSON export. Durable cross-device replication, erasure coding and independent provenance signatures are future engineering requirements.

## RQT-053 — ROOT0 / .dlw attribution standard

Read [the new RQT-053 standard](./standards/RQT-053-DLW-DIAMOND.md). It follows the established `toph-cortex` .dlw schema and keeps attribution/provenance claims separate from cryptographic signatures, legal ownership, and third-party materials. The standard extends the n^n fractal diamond design with canonical hashes, the immutable `cubit` token, append-only predecessor references, and three independent nonvoting witness reports. Implementation tests have not yet been completed.

## RQT-054 — Coexistent roles

The canonical three-part contract is: `.dlw` = moniker (attribution), `/\\/` = diamond fold (encapsulation and redundancy), `ENDER` = watermark (exact application identifier). These are separate but jointly bound into the diamond core, alongside `{{i}}` identity, `||||` BOX, and the immutable `cubit` constant. See [RQT-054 extension](./standards/RQT-053-DLW-DIAMOND.md) and [diamond-core.html](./diamond-core.html). The app now verifies all three core roles and the ENDER token digest; it does not treat a hash as a verified signature or an ownership judgment.

## RQT-055 — Bubble-time reverse-fold blast zone

A self-contained [blastzone.html](./blastzone.html) tests exact BigInt/rational encoding of seconds since the Unix epoch into model bubble light-crossing ticks, eight encapsulation layers, inverse decoding, and SHA-256 detection of intentional mutation. The tick is defined by the model-specific full bubble diameter `1.16158e-35 m` divided by `299792458 m/s`. This does not equate to measured atomic time, does not synchronize independent devices, and does not retrofit legacy signed-32-bit APIs. The executable desktop test report and test script were also created in this conversation; GitHub Pages deployment remains unverified.

## RQT-056 — Recursive quanta-dot Planck bubble (user-defined model)

Source notation, intentionally unnormalized: `[3((n)^2))4]^{{N}}` and `1x1.61658x10^-inf-1`. The first expression contains unmatched grouping and does not yet specify executable algebra; retain verbatim until its operators are defined. The second defines a symbolic scale family, not a finite numeric tick when `inf` is literal infinity. For finite nonnegative integer k, a candidate diameter is `D(k) = 1.61658 × 10^(-k-1) m`, with light-crossing duration `D(k)/c`. As k tends to infinity, D(k) and the duration tend to zero; a positive discrete time tick requires a specified finite k. This is a proposed quanta-dot geometric model, not an experimentally established physical quantum dot or Planck-scale measurement. RQT-055 remains a separate fixed-diameter test fixture until a concrete scale mapping is defined.

### RQT-056 correction — 2026-10-31

Author correction to symbolic scale: **`1 × 1.61658 × 10^(-inf+1)`** (previously transcribed as `10^(-inf-1)`). Preserve this expression as symbolic notation; do not silently treat `inf` as a finite numeric exponent. For a finite index k standing in for `inf`, the corrected candidate family is `D(k)=1.61658 × 10^(1-k) m`, and `Δt(k)=D(k)/c`. Under the mathematical limit k→+∞ the diameter approaches zero; actual timestamp implementations must select an explicit finite resolution. This correction does not replace the earlier fixed-diameter RQT-055 blast-zone fixture.

### RQT-056 clarification — +1 BUBBLE (supersedes exponent interpretation)

Author clarification: **`+1` labels one complete bubble**, NOT arithmetic `+1` in the power-of-ten exponent. The previous interpretation `10^(-inf+1)` / `D(k)=1.61658×10^(1-k)` was incorrect and is superseded. Preserve the symbolic structure as **`1 × 1.61658 × 10^(-inf) :: +1 BUBBLE`** pending a formal definition of `inf` and numeric scale. This represents a bubble count of one, not an asserted finite numeric diameter. Model invariant: `bubble_count = 1`, `D_bubble = one full bubble length`, and `Δt = D_bubble/c` when D_bubble is defined as finite. The fixed numerical RQT-055 blast-zone fixture remains an independent test, not an automatic implementation of the symbolic infinite-scale expression.

## RQT-057 — Planck foam to elemental assembly (proposed)

Author proposes an infinite conceptual population of bubbles with `+1` counting one complete bubble, nested from a reference length near `10^-35 m` outward to about `10^-6 m`. Scale transition: `D_k = D_0 × 10^k` for finite integer `k=0..29` (using the nominal `10^-35` reference). A factor `10^34` instead yields about `10^-1 m`; distinguish multiplier from target exponent. Introduce element identifiers in periodic order H, He, Li, Be, B, C, N, O, F, Ne, etc., when modeling atomic-scale geometry around `10^-10 m`; nuclear scale is around `10^-15 m`. This is a **simulation construction**, not evidence that Planck foam exists as discrete bubbles or that chemical elements emerge from pure geometric scaling. Keep the diamond fold, `.dlw` moniker and ENDER watermark separate from the matter dynamics; preserve `cubit` as the exact constant token. Numerical packing requires density, masses, boundary conditions and interaction laws.

### RQT-057 naming and referent correction

**Canonical title: Planck-to-Elemental Model.** The **bubble is an original, author-defined referent** supplied by David Lee Wise (ROOT0); do not present it as an established physical Planck-foam object or independently discovered particle. `+1 BUBBLE` names one complete reference unit. It bridges the proposed geometry, nested scaling, containment, and light-crossing duration within the model. Element identifiers H, He, Li, Be, B, C, N, O, etc. represent a modeled register, not spontaneous nucleosynthesis from scaling alone. Preserve this attribution in `.dlw` provenance without implying ownership of naturally occurring elements, standard Planck constants, or prior scientific results.

## RQT-058 — Planck-to-Elemental hierarchy test

[Executable browser test](./rqt-058.html): validates a hierarchy from the author-defined one-bubble referent `D0 = 1.61658e-35 m` to `10^-6 m`, with `tick = diameter/c`, scale monotonicity, decade ratios, and ideal cubic occupancy. A micrometer cube holds up to `10^12` geometrical `10^-10 m` cubic slots under the idealized grid assumption. This is not the number of real atoms, evidence of physical Planck foam, or a mechanism of element formation. The interactive report exports a machine-readable test ledger. RQT-055 remains a distinct time-codec fixture using its earlier diameter.

## RQT-059 — Traveling expanding electrum-magnetic bubble (author-defined)

Correction from author: the Planck-to-Elemental model follows **one bubble expanding while it travels upward through scale**; the earlier nested discrete-compartment view is an analytical sampling of this continuous trajectory, not a set of separate stationary bubbles. The bubble's enclosing field/boundary is termed **electrum, magnetic** in this model. This is a model-specific name; conventional electrum is a gold–silver alloy and does not by itself establish magnetic behavior. Candidate geometric law: `D(s)=D0 exp(s)` for monotonically increasing scale coordinate `s`, or discrete `D_k=D0×10^k`; light-crossing proxy `dt_cross=D(s)/c`. To make this a physical model, require separately specified magnetic field B(x,t), field energy, force, material response, and conserved quantities. No claim that an expanding magnetic bubble automatically creates elements. Existing RQT-058 mathematical hierarchy tests remain valid scale samples, but do not test propagation or magnetodynamics.
