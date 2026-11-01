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

## RQT-060 — Single-bubble walk and conditional natural occupancy

Author correction: electrum is **part of** the traveling bubble, not the bubble itself or necessarily the whole boundary. Follow one initially empty reference bubble continuously upward in scale. At each sample radius, ask whether specified particles/fields and physical conditions permit a nuclear, atomic, or molecular configuration. Do not insert particular elements merely because a geometric threshold was crossed. Inputs required to derive actual filling: particle inventories or inflow; energy/temperature; pressure/density; electromagnetic field configuration (including optional electrum component); interaction dynamics; boundary conditions. Diameter-only containment is a necessary geometric condition, not sufficient for creation or stable binding. The original Planck bubble remains an author-defined referent, not established physical foam. Earlier characterization of electrum as the bubble's entire boundary is superseded.

## RQT-061 — First conditional occupancy test

[Run the single-bubble walkthrough](./rqt-061.html). One original bubble expands while traveling through scale. Tested explicit inventories: empty, proton only, and proton+electron. Hydrogen ground-state reference diameter is twice the Bohr radius (~1.058e-10 m); 1e-10 m is slightly smaller, 1e-9 m accommodates that reference geometrically. Exact eight-check report is provided in the conversation as `rqt061-results.json`. The check verifies source accounting and geometric thresholds; it does not simulate capture, radiation, magnetic containment, actual matter synthesis, or a physically realized electrum field. Inputs beyond geometry are still needed.

## RQT-062 — Particle motion inside one expanding bubble

[Interactive motion simulation](./rqt-062.html) models a fixed proton and moving electron with softened classical Coulomb attraction and velocity-Verlet integration, plus a growing illustrated bubble radius. It exposes orbit, velocity-derived motion, classical energy and its relative numerical drift; an audit runs 100, 1,000 and 10,000 steps. The electrum component is reserved but has no magnetic field equation yet. The simulated bubble radius is visual and does not impart a force on the electron. A negative classical total energy does not establish stable quantum hydrogen, photon emission, or actual formation from initially separated free particles.

## RQT-063 — Moving reflective bubble boundary

[Interactive wall-coupling laboratory](./rqt-063.html). A classical softened Coulomb proton/electron toy model now includes an explicit radial moving-wall reflection; wall-relative radial velocity is reflected, and the change in particle energy at collision is recorded as wall work. Compare no wall, fixed wall and outward-moving wall; a 15,000-step in-browser audit reports collision counts, finite state and energy-balance residual. This is a prescribed boundary, **not** a solution of electrodynamics, and electrum remains an unspecified component. Wall work accounts for energy transfer; particle mechanical energy is not conserved in isolation. Reflections plus finite timestep/projection can introduce numerical error, so the audit is diagnostic, not proof of exact energy conservation or real atom formation.

## RQT-064 — Magnetic component / Lorentz coupling

[Interactive lab](./rqt-064.html). One expanding bubble with optional model-specific 'electrum' magnetic component represented by a uniform out-of-plane field (0, 1, or 5 tesla). A fixed proton and electron are propagated with Coulomb half-kicks and Boris magnetic velocity rotation. Comparisons include wall off/on; work from an expanding reflective wall is counted separately from energy drift. A six-case numerical audit runs 10,000 steps per case and reports finite states, collisions and residuals. Magnetic force is perpendicular to velocity and ideally does no mechanical work; the combined numerical scheme may drift. This is a prescribed toy field, not a self-consistent Maxwell field or atomic-formation demonstration.

## RQT-065 — Magnetic flux dilution during one-bubble expansion

[Interactive three-way flux lab](./rqt-065.html): compares no magnetic field, a fixed 5 T field, and a prescribed conserved-flux field `B(R)=B0(R0/R)^2` as a single bubble expands. The electron trajectory is computed with softened Coulomb attraction and Boris magnetic rotation. Reports radius growth, B, equatorial flux, particle position relative to bubble, and mechanical energy drift. The conserved-flux case obeys its mathematical definition by construction; changing B would normally induce an E field under Faraday's law, which is not modeled. No physical full-system energy-conservation claim or magnetic self-containment is established. Electrum is only the name for a component in this user-defined model.

## RQT-066 — Faraday-induced electric field during bubble growth

[Interactive RQT-066 experiment](./rqt-066.html): three modes (static B, diluted B without induction as a deliberately incomplete control, and diluted B with a Faraday-induced azimuthal electric field). For prescribed spatially uniform interior B(t)=B0(R0/R)^2, dB/dt=-2Bu/R and Ephi=-r/2 dB/dt. A Coulomb+Boris orbit integrates electron velocity and tracks electric work q∫E·v dt against its mechanical-energy change. The in-browser audit runs 15,000 steps in each mode. Important limitation: this is a prescribed *local* field, not a self-consistent finite-bubble Maxwell solution; its external source energy and radiation are omitted. The numerical outcomes are not yet independently verified.

## RQT-067 — Electromagnetic energy ledger

[Run RQT-067](./rqt-067.html). For prescribed uniform internal field and spherical volume, U_B=B²(4πR³/3)/(2μ₀). With B=B0(R0/R)², U_B R = U_B0 R0 is an algebraic model invariant. The lab extends the Faraday induction simulation with field energy and a residual 'externalWorkRequired = ΔE_particle + ΔU_B'. This external work is **inferred from the ledger**, not independently solved; it cannot constitute a nontrivial closed-system energy-conservation test. A self-consistent Maxwell boundary, field stresses, source work, and radiation are still missing. Results require runtime verification.

## RQT-068 — Magnetic stress and expansion-work boundary

[Interactive laboratory](./rqt-068.html) compares an *assumed isotropic effective* pressure `p_eff=−dU_B/dV=u_B/3` with the local magnetic energy density `u_B=B²/(2μ₀)` under the imposed B∝R⁻² law and spherical volume. Numerically checks U_B R invariance at R/R0=1,2,4,10. Using u_B as uniform pressure produces three times the effective integrated expansion work: this marks an invalid substitution, not demonstrated energy creation. Real Maxwell stress tensor is anisotropic, `T_ij=(B_i B_j−½δ_ij B²)/μ₀`; a self-consistent magnetic bubble requires external fields, boundary/surface currents and force balance. The pressure result derives from the imposed energy law and is not an independent physical expansion mechanism. Browser checks not yet independently executed.

## RQT-069 — Surface force balance (post-freeze extension)

[Run RQT-069](./rqt-069.html). This is a NEW extension after the `freeze/pte-rqt-068-v1.0.0` snapshot, which is not modified. For an assumed uniform magnetic field along the z axis inside a sphere, the normal Maxwell traction is `t_n(theta)=u_B(2 cos²(theta)-1)`, with `u_B=B²/(2μ0)`. A spherical area average gives `-u_B/3`, with opposite signs at equator/poles; hence no uniform pressure or uniform surface tension can cancel this directional interior traction at every latitude. A complete boundary force balance needs exterior magnetic fields and Maxwell-stress jump, surface current or anisotropic material forces, and a shape/expansion equation. A four-case test at radius factors 1, 2, 4, 10 checks the assumed flux scaling and spherical mean numerically. Neither a self-consistent Maxwell solution nor dynamic equilibrium is established.

### Development chain
RQT-058 geometric scale samples → RQT-059/060 single traveling bubble and electrum-component correction → RQT-061 conditional particle occupancy → RQT-062 Coulomb motion → RQT-063 moving reflective boundary → RQT-064 Lorentz/Boris magnetic motion → RQT-065 imposed flux dilution → RQT-066 Faraday-induced E → RQT-067 energy ledger → RQT-068 pressure vs anisotropic stress (frozen) → RQT-069 directional surface balance (current).

## RQT-070 — Four-interface 4×4/3×3 lattice (post-freeze)

Author supplies `inner/inner :: inner/outer :: outer/inner :: outer/outer :: ([[4x4]]^4)^{{3x3}}^3` with four force channels `weak, medium, strong, nuclear`. [Interactive structural lab](./rqt-070.html) preserves exact syntax and names. An **illustrative tensor-product interpretation** computes `16^4=65,536`, `9^3=729`, `65,536×729=47,775,744` address pairs; this is NOT an equivalence to the literal nested exponent operator without author definition. Four interfaces × four force channels produce 16 unique symbolic mappings. Medium has no standard force-law identification. Nuclear may name a residual nuclear interaction but is not treated as a fundamental interaction independent of the strong force without definition. Electrum remains one bubble component, not the whole bubble. This structural address test neither predicts field forces nor resolves Maxwell boundary stresses; RQT-068 frozen branch is unmodified.

## RQT-071 — Conservative four-interface exchange

[Interactive laboratory](./rqt-071.html). Preserves the authored `([[4x4]]^4)^{{3x3}}^3` register and regions II, IO, OI, OO. Test topology II↔IO↔OI↔OO (an assumption, not a force law) permits integer energy/matter transfers only between adjacent interfaces when sufficient source inventory exists; every accepted event debits source and credits destination. Three separate witnesses A/source, B/destination, C/aggregate record observations without voting or quorum. Structural audit executes six accepted transfers, rejects nonadjacent and overdrawn transfers, checks aggregate E and N remain 40 each. The units are symbolic; weak, medium, strong, nuclear are four named channels whose physical couplings are not specified. Not a claim of measured energy or matter conservation in an expanding physical bubble. Frozen `freeze/pte-rqt-068-v1.0.0` untouched.

## RQT-072 — Charge and three-axis momentum transfer

[Run RQT-072](./rqt-072.html). Four interfaces II / IO / OI / OO exchange symbolic conserved E, N, signed Q and vector P=(Px,Py,Pz) between adjacent source/destination regions, with A/source B/destination C/global independent witnesses, no quorum. Integer-ledger audit exercises six accepted and two rejected transfers and exact total preservation. This is structural bookkeeping; physical charge-current/field momentum and realistic force laws remain unspecified. Explicit author requirement: **draw full ASCII for every subsequent natural boundary**, including in the GitHub page and assistant response, recorded in [standards/ASCII-EVERY-BOUNDARY.md](./standards/ASCII-EVERY-BOUNDARY.md). Preserves earlier RQT-068 freeze.

## RQT-073 — Particle, field, and bubble recoil momentum

[Interactive lab and full ASCII](./rqt-073.html). Splits specified vector impulse among particle, electromagnetic field and bubble boundary so their sum remains zero in all x/y/z axes. An audit exercises 15 accepted axis/fraction examples plus one invalid-share rejection. This is ledger conservation by construction, not an independent Lorentz/Maxwell field calculation. Electromagnetic momentum density in vacuum is `g=ε0(E×B)=S/c²`; self-consistent field and stress-boundary flux remain future work. Standard [ASCII every boundary](./standards/ASCII-EVERY-BOUNDARY.md) followed. Frozen RQT-068 branch unchanged.

## RQT-074 — Field-first correction (author-directed)

All elementary particles are represented as excitations of fields, not as independent substances added to a separate complete field momentum. Electron, quark, photon, gluon, W/Z and Higgs fields participate; protons, neutrons and atoms are composite systems, not individual elementary fields. Track excitation and interface flux in `inner/inner`, `inner/outer`, `outer/inner`, `outer/outer`. Prevent double-counting particle momentum when included in the field stress-energy. A complete conserved system requires field stress-energy plus appropriate boundary/sources, not just an electromagnetic E×B term. Electrum remains only a component in the author-defined traveling bubble. Preserve `([[4x4]]^4)^{{3x3}}^3` and the W/M/S/N model-channel names, without equating medium and nuclear to distinct fundamental forces. Future boundaries must include full ASCII per standards/ASCII-EVERY-BOUNDARY.md.

## RQT-075 — Field excitation dispersion versus imposed confinement

[ASCII and interactive analytical laboratory](./rqt-075.html) tests one prescribed expanding bubble `R(t)=R0+ut`, using a 1D nonrelativistic Gaussian Schrödinger packet as a surrogate for a localized excitation. Free packet width `σ(t)=σ0 sqrt(1+(ℏt/(2mσ0²))²)` versus an *externally imposed* stationary harmonic trap width σ0; probability inside [-R,R] is `erf(R/(sqrt(2)σ))`. Parameters: R0=3a0, σ0=a0/2, u=2e5 m/s, t=2e-16 s. Analytic result: free packet width ~16.57× initial, while confining reference width is constant. No real electrum trapping mechanism or self-consistent bubble field is established. Four-interface W/M/S/N routing and full ASCII standard preserved. Frozen RQT-068 untouched.

## RQT-077 — Odd/even B/T zipper nesting and reversible transport

[Run ASCII interactive zipper test](./rqt-077.html). Author layout: B/T top-left and bottom-left; center `{{n}}`; top-right `{{n²-1}}` odd; bottom-right `{{n²}}` even, for even n. Cases n=2,4,6,8 yield 3/4, 15/16, 35/36, 63/64. Nested symbolic wrappers `B(T(B(T({{n}}))))` are added and removed reversibly without modifying center or paired values. All parity and round-trip identities follow algebraically; this is a logical transport model, not verified molecular DNA or chemical dynamics or a Hodge ring isomorphism. Full ASCII included per standard; frozen RQT-068 unchanged.

## RQT-080 — Gravity-curvature scaling comparison

[Full ASCII interactive test](./rqt-080.html) compares the author expression `C(n)=pi*sqrt(n)/1.616158` against Schwarzschild invariant curvature `K(r)=48 G² M²/(c⁴r⁶)` for fixed M and explicitly assumed `n=r/r0`. C/C1 grows as sqrt(n); K/K1 falls as n^-6. The comparison rejects identification of the two quantities under this n interpretation, not other possible meanings of n. C has unspecified physical dimensions and is not a validated gravitational curvature equation. Frozen RQT-068 untouched.
