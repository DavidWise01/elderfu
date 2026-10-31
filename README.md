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
