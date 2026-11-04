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

## RQT-081 — Numeric gravity referent correction

Author supplies `sqrt6/1.61658x10^-35/2pi`. Under the explicitly stated interpretation `sqrt(6)/(1.61658e-35 * 2*pi)` the result is `2.41156268552647e34 m^-1` if the denominator's 1.61658e-35 carries meters. Its reciprocal length is `4.1466888088861324e-35 m`. This is inverse length, not established scalar spacetime curvature; further mapping to a metric or invariant is required. Alternative left-associative parsing differs, so parentheses are needed. RQT-068 freeze unchanged. Full ASCII in conversation.

## RQT-082 — Dimensional interpretation of numeric referent

Preserve author working expression `q = sqrt(6)/(2*pi*L0)` with `L0 = 1.61658e-35 m`. Exact numeric evaluation: `q=2.41156268552647e34 m^-1`, inverse characteristic length `1/q=4.1466888088861324e-35 m`, wave-number-associated wavelength `lambda=2*pi/q=2.6054414197439366e-34 m`, and square `q^2=5.815634586223639e68 m^-2`. These are dimensionally compatible candidates, **not physically identified quantities**; `q^2` cannot be asserted to equal spacetime scalar curvature or Einstein's field equations without a metric and mapping. If `q` is angular wavenumber, `lambda=2pi/q`. Preserve ASCII at every next bound; RQT-068 freeze unchanged.

## RQT-083 — Sphere curvature and Gauss–Bonnet consistency

Using the author working length L0=1.61658e-35 m and q=sqrt(6)/(2*pi*L0), take the explicitly *constructed* 2-sphere radius R=1/q=4.1466888088861324e-35 m. Gaussian curvature K=1/R²=q²=5.815634586223639e68 m^-2; intrinsic scalar curvature S=2K=1.1631269172447278e69 m^-2; area=4*pi*R²=2.1607909554921158e-68 m²; integrated Gaussian curvature K*A=4*pi; Euler characteristic (1/(2*pi))*integral=2. These identities pass analytically and numerically; they follow from the chosen sphere and are not a prediction of a gravitational field. Distinguish intrinsic 2D geometry, extrinsic embedding, and 4D Lorentzian spacetime curvature. No physical measurement or Einstein equation solved. Full ASCII displayed in conversation. RQT-068 frozen branch preserved.

## RQT-084 — Planck foam / bubble topology test

[Full-ASCII executable test](./rqt-084.html). Author-defined sub-Planck foam substrate below 10^-35m contrasted with one expanding referent bubble. A tetrahedral sphere mesh V-E+F=4-6+4=2 and 3x3 periodic torus cell mesh V-E+F=9-18+9=0. Same literal `{{i}}` can be transported between B/T containers without loss of *symbolic* identity. Distinct Euler characteristics prohibit a topology-preserving homeomorphism of sphere and torus. This does not establish actual foam, spontaneous emergence, or physically possible topology change. Preserves RQT-068 reference freeze and ASCII-every-boundary convention.

## RQT-085 — Canonical nested operator correction: brace / box / toroid

Author correction (overrides any implication that B and T are interchangeable surface shapes): canonical nesting is `{ [ ( i ) ] }`, written `{[(i)]}`:
- `{ ... }` BRACE = **Waldo manipulation / operator**.
- `[ ... ]` BOX = **space / containment**.
- `( ... )` TOROID = **state**.
- `i` = central referent / identity; `{{i}}` remains the project's separate identity-carrier notation where applicable.

```text
|||| {{i :: RQT-085 :: NESTED DIALECT}} ||||

   {   WALDO / MANIPULATION
       [   SPACE / BOX
           (   STATE / TOROID
                   i
           )   STATE
       ]   SPACE
   }   WALDO

       { [ ( i ) ] }

  OPERATE { }  -> LOCATE [ ] -> STATE ( )
  DO NOT CONFUSE WRAPPERS WITH HOMEOMORPHISMS
|||| .dlw / /\\/ / ENDER / cubit ||||
```

Prior RQT-084 sphere-vs-torus Euler-characteristic check remains valid as a mathematical comparison but **does not describe a mandatory geometry switch** in the author-defined nested syntax. No physical topology-change operation is implied by evaluating the nesting. This correction is append-only; frozen RQT-068 branch unchanged.

## RQT-086 — Waldo reversible state operations

[Interactive ASCII test](./rqt-086.html) preserves `{ [ ( i ) ] }` semantics: brace/Waldo manipulation, box/space, toroid/state. A reversible state vector translation `(x,y)->(x+2,y-3)` and its inverse are tested over 81 integer pairs while referent and box address remain unchanged. Noninvertible collapse and mismatched identity are marked disallowed conceptual cases; the live script exposes the identity mismatch boolean but is not an independent authorization framework. This is structural software logic, not physical topology change. Frozen RQT-068 untouched.

## RQT-087 — Hodge-first research scope correction

User confirms `{[(i)]}` Waldo/space/state language is being developed **for the Hodge Conjecture**. Future tests must prioritize finding algebraic cycles representing rational Hodge classes, not generic coordinate reversible transport. Proposed first discovery benchmark: X=CP1×CP1, unknown coefficients for alpha=5a+7b to be recovered from intersection pairings with known basis classes. Intersection with a returns 7, intersection with b returns 5 because a²=b²=0 and ab=[point]. Recover alpha=5a+7b and verify exact class equality. This is a known low-codimension example, not a general proof. Keep full ASCII every bound; preserve frozen RQT-068.

## RQT-088 — Recursive Hodge nesting, author correction

Canonical author expression, byte-for-byte: `[h(i[h2(i[h3(i{h+i})])])]`. Levels h > h2 > h3 extend recursively without a fixed symbolic stop. Box `[ ]` denotes space; toroid `( )` denotes state; brace `{ }` denotes Waldo manipulation; `i` preserves the referent. Recursive level labels `h2`, `h3` must NOT be confused with cup products `h^2`, `h^3` without an explicit interpretation map. For CP^m, H*(CP^m;Q)=Q[h]/(h^(m+1)), so h^k nonzero for 0<=k<=m and h^(m+1)=0. The nested language is a proposed encoding, not an established proof of the general Hodge conjecture. Test targets: CP² h² !=0,h³=0; CP³ h³ !=0,h⁴=0, and whether mapping preserves multiplication and cycle class. Frozen RQT-068 unchanged.

## RQT-089 — Hodge caliper: two independent period probes

[Interactive test](./rqt-089.html) on X=CP1×CP1 with H^2 basis a,b, a²=b²=0 and integral(a b)=1. If alpha=p a+q b, intersection pairings are integral(alpha a)=q and integral(alpha b)=p. Hence p and q are reconstructed, and alpha is class of p(point×CP1)+q(CP1×point) given conventional Poincaré dual bases. Code tests 361 integer pairs. This is a known elementary case, not proof of the full Hodge conjecture. Full ASCII and original brace=Waldo, box=space, toroid=state nesting retained; freeze RQT-068 unchanged.

## RQT-090 — Blind Hodge caliper, rational reconstruction

[Interactive full-ASCII test](./rqt-090.html). On X=CP1×CP1 with a²=b²=0 and ∫ab=1, seeded hidden rational class alpha=p a+q b is reconstructed solely from ∫alpha a=q and ∫alpha b=p. Exact normalized fractions; a 100-seed programmatic audit button; three independent conceptual witness reports for measurement, reconstruction, verification (not voting/quorum). Construction of rational linear combinations of algebraic fibers is a known case of Hodge and not a general result. `{[(i)]}` retains brace=Waldo, box=space, toroid=state; sub-Planck claims are unrelated to this proof. Frozen RQT-068 untouched.

## RQT-091 — Codimension-two rational Hodge caliper

[Full ASCII exact symbolic interactive test](./rqt-091.html) for X=CP²×CP², H*(X,Q)=Q[a,b]/(a³,b³). An unknown alpha=p a²+q ab+r b² yields intersection vector (r,q,p) with a²,ab,b². Matrix [[0,0,1],[0,1,0],[1,0,0]] has determinant -1 and exact inverse itself, reconstructing p,q,r. Their geometric representatives are p(point×CP²)+q(line×line)+r(CP²×point). Code exposes deterministic seeded tests and 100-case audit, not independently browser-verified. This entire class of examples has algebraic generators and does not resolve the Hodge conjecture for arbitrary varieties. Original `{[(i)]}` semantics and ASCII at each bound; frozen RQT-068 unaffected.

## RQT-092 — {{ i + h }} Hodge conjecture FAIL-STOP

[Interactive fail-stop](./rqt-092.html) · [ASCII / proof obligations](./rqt-092.md). Arbitrary smooth complex projective X; rational Künneth component h of the algebraic diagonal in Y=X×X. Conditioned on X being smooth projective, input/category, rationality, Hodge type pass by known Hodge/Künneth properties. Halt at missing independently verified codimension-d algebraic cycle whose class equals h. Later verification and universal proof gates not executed. A halt is not disproof; the total diagonal being algebraic is insufficient to establish its individual components are algebraic cycles. Preserve three witnesses, no quorum, immutable RQT-068 freeze.

## RQT-093 — Executed `{{ i + h }}` with exact arithmetic

[Executed proof-obligation record](./rqt-093.md) · [Reproducible Python test](./rqt-093.py). Concrete X=CP², Y=X×X: diagonal class a²+ab+b²; component witnesses point×CP², CP¹×CP¹, CP²×point. Exact intersection pairing matrix identity, diagonal pairing (1,1,1) — PASS. For arbitrary X, no cycle construction certified: **STOP**, not a counterexample or resolution of Hodge. Freeze RQT-068 unchanged.

## RQT-094 — Algebraic Künneth projector construction on elliptic E

[Executed exact Python check](./rqt-094.py) · [full ASCII and certificate boundary](./rqt-094.md). The multiplication maps [0],[1],[2] induce actions m^k on H^k(E,Q), k=0,1,2. Rational linear combinations of their (correctly oriented) graph correspondences yield degree projectors Pi0/Pi1/Pi2 with identity matrix in exact arithmetic. PASS on this established elliptic example. **STOP at general X**: no universal construction of corresponding algebraic degree projectors was supplied; the Hodge conjecture remains open. Preserve `{[(i)]}`, `{{ i + h }}`, 3 witnesses, no quorum, ASCII every boundary; RQT-068 freeze unchanged.

## RQT-095 — Fail-stop at Lefschetz inverse algebraicity

[Reproducible control test](./rqt-095.py) · [Full ASCII audit](./rqt-095.md). For CP³, L³:H⁰→H⁶ and L:H²→H⁴ give exact one-dimensional isomorphisms. Independent Python verification passed. Hard Lefschetz provides an abstract inverse on arbitrary smooth projective X, but no universal **algebraic correspondence** realizing that inverse is supplied. This is Lefschetz standard conjecture B, unresolved in general; thus **STOP** at algebraic witness. Not evidence against Hodge. `{{ i + h }}` and `{[(i)]}` maintained, no quorum, previous freeze unchanged.

## RQT-096 — Explicit algebraic Lefschetz inverse on CP¹×CP¹

[Exact executable audit](./rqt-096.py) · [Full ASCII proof-boundary record](./rqt-096.md). On S=CP¹×CP¹ with L=a+b, L²(1)=2ab, construct rational algebraic correspondence (1/2)[S×S], acting on H⁴(S)→H⁰(S) by integration to invert L². Exactly verified on three rational inputs with Python Fraction. This illustrates only the top-degree inverse on one known surface. STOP on an unprovided construction for arbitrary X; this does not settle the Lefschetz standard conjecture or Hodge conjecture. Preserve `{{ i + h }}`, `{[(i)]}`, three witnesses, no quorum, RQT-068 freeze.

## RQT-097 — Lefschetz lowering as algebraic correspondence

[Exact executable test](./rqt-097.py) · [Full ASCII and certificate](./rqt-097.md). For S=CP¹×CP¹ and L=a+b, the codimension-one cycle Z=pr1*L+pr2*L on S×S induces the lowering operator Λ: H⁴→H²→H⁰ with Λ(ab)=L, Λ(a)=Λ(b)=1, Λ(1)=0. Algebraic diagonal represents identity; (S×S)/2 inverts L²:H⁰→H⁴. This passes as a known surface case. The universal algebraic correspondence for arbitrary X remains unavailable: STOP, not disproof. Maintain `{{ i + h }}` and ASCII-every-boundary; frozen RQT-068 unchanged.

## RQT-098 — Quartic K3 primitive projection

[Exact Python audit](./rqt-098.py) · [Full ASCII and fail-stop](./rqt-098.md). On a smooth quartic K3 S with h²=4, the rational algebraic correspondence P=[Δ_S]-(1/4)pr1*h·pr2*h acts on H² as x↦x−(x·h/4)h, is idempotent, kills h and fixes primitive vectors. Independently executed 4/4 exact rational cases PASS. STOP at missing construction/certificate for arbitrary rational (2,2) Hodge class on S×S; not a counterexample, not a proof of universal Hodge. Freeze RQT-068 untouched.

## RQT-099 — Hodge-type gate before K3 tensor cycle search

[Reproducible script](./rqt-099.py) · [Full ASCII and fail-stop](./rqt-099.md). An abstract rank-two K3-type period plane has omega=e1+i e2. A rational endomorphism M=[[a,b],[c,d]] preserves the Hodge decomposition iff a=d and c=-b. Python exact checks: identity PASS, quarter-turn rotation PASS, reflection HODGE FAIL (3/3 expected classifications). First negative-control halt is Hodge-type failure. A positive abstract candidate does not supply an actual projective K3 realization or an algebraic cycle, so STOP at the realization/certificate gate. This neither proves nor refutes the Hodge conjecture. An Oct-2026 broad K3-product proof claim was withdrawn. Preserve `{{ i + h }}`, 3 witnesses, no quorum, ASCII every bound, RQT-068 freeze untouched.

## RQT-100 — Concrete Fermat quartic K3 automorphism and graph witness

[Exact reproducible SymPy test](./rqt-100.py) · [Full ASCII certificate](./rqt-100.md). Fermat quartic S:x⁴+y⁴+z⁴+w⁴=0, automorphism g:[x:y:z:w]↦[ix:y:z:w] preserves S, has order 4 and determinant i. Its algebraic graph Γ_g⊂S×S witnesses the associated Hodge correspondence, with g* on H^{2,0} acting by i via residue. This certifies one correspondence, not the algebraicity of every rational Hodge class on S×S. **STOP** at missing completeness of algebraic cycle span. Preserve `{{ i + h }}`, ASCII every boundary, 3 witnesses, no quorum, and RQT-068 freeze.

## RQT-101 — Fermat quartic 64 diagonal automorphism graphs

[Exact enumeration](./rqt-101.py) · [Full ASCII and fail-stop audit](./rqt-101.md). The group (μ₄)⁴/μ₄ yields 64 algebraic projective automorphisms of the Fermat quartic. On holomorphic 2-form, eigenvalue i^(a+b+c), with 16 maps at each phase. The rational span of the four phase actions on its rank-two transcendental subspace is dimension two (I,J). Each map has an explicit algebraic graph. **STOP**: no full 22-dimensional cohomology-action matrix or proof of complete rational Hodge cycle span on S×S has been supplied. Do not mistake this limited representation calculation for a general Hodge solution. Preserve `{{ i + h }}`, three witnesses, ASCII every boundary, no quorum, immutable RQT-068 freeze.

## RQT-102 — Fermat K3 self-product rational Hodge completeness

[Reproducible count](./rqt-102.py) · [Full ASCII and cycle-span proof](./rqt-102.md). For Fermat quartic K3 S, NS rank 20, T rank 2 with Q(i) Hodge endomorphisms. The rational degree-4 Hodge class dimension of S×S is 2 outer + 20² divisor products + 2 transcendental correspondences = **404**. Projected algebraic graphs of identity and quarter-turn provide the latter two directions; divisor inverse intersection matrix and Künneth projectors give algebraic projectors. Equality of cycle-span dimension and rational Hodge dimension **PASS** for this known special case. **STOP** at arbitrary smooth projective varieties: no universal argument. Broader October-2026 K3-product claim withdrawn, not used. `{[(i)]}`, `{{ i + h }}`, three witnesses, ASCII-every-boundary, no quorum; RQT-068 freeze unchanged.

## RQT-104 — Explicit cross-surface K3 algebraic graph

[Exact Python audit](./rqt-104.py) · [Full ASCII and proof boundary](./rqt-104.md). The diagonal projective map g=(1,2,3,4) sends S':x⁴+16y⁴+81z⁴+256w⁴=0 isomorphically to S:x⁴+y⁴+z⁴+w⁴=0. Exact 625-coordinate tests PASS; graph Γ_g is a certified algebraic cycle giving a rational Hodge isometry. **STOP** because the two differently written quartics are isomorphic, not a non-isomorphic comparison. Buskin's theorem independently establishes algebraicity of rational Hodge isometries even for non-isomorphic projective K3 surfaces; do not call those an open counterexample problem. The general Hodge conjecture remains open. Keep `{{ i + h }}`, full ASCII, witnesses, no quorum, RQT-068 freeze unchanged.

## RQT-105 — Non-isomorphic K3 surfaces with an explicit Hodge similarity

[Exact executable test](./rqt-105.py) · [Full ASCII and mathematical certificate](./rqt-105.md). Fermat quartic S has symplectic Nikulin involution [x:y:z:w]↦[x:y:−z:−w]; quotient has 8 A1 singularities and minimal resolution Y=Km(E_i×E_i). Quotient invariant equations: x⁴+y⁴+A²+B²=0, C²=AB. Published integral transcendental lattices T(S)=diag(8,8), T(Y)=diag(4,4) have different discriminants (64 vs 16), proving S and Y non-isomorphic. The rational degree-two quotient-to-resolution map has algebraic graph closure, providing a concrete Hodge similarity of multiplier 2 (not an isometry). Exact tests on 625 integer tuples and lattice arithmetic PASS. **STOP**: arbitrary rational Hodge correspondences for arbitrary K3 pairs not constructed; general Hodge remains open. Preserve `{{ i + h }}`, three witnesses, no quorum, full ASCII and frozen RQT-068.

## RQT-106 — Nikulin quotient / rational transcendental inverse

[Exact 25-vector model](./rqt-106.py) · [Full ASCII and fail-stop](./rqt-106.md). For the Fermat quartic Nikulin quotient-resolution correspondence Γ:S⇢Y, the algebraic graph and its transpose satisfy ΓᵗΓ=2id on T(S)⊗Q and ΓΓᵗ=2id on T(Y)⊗Q. Accordingly (1/2)Γᵗ inverts the transcendental map. Rational basis model with T(S)=diag(8,8), T(Y)=diag(4,4) passes 25 exact vectors; basis correspondence is a theorem-based normalization, not independently extracted period data. **STOP** on all of H²: ΓᵗΓ=id+ι* kills anti-invariant algebraic classes. Neither Hodge conjecture proved nor disproved. `{{ i + h }}` and `{[(i)]}` maintained; frozen RQT-068 unchanged.

## RQT-107 — Recover Nikulin eigenspaces with algebraic projectors

[Exact script](./rqt-107.py) · [Full ASCII and proof boundary](./rqt-107.md). Nikulin involution on Fermat K3 induces H²(S,Q)=H²_+⊕H²_- of ranks 14 and 8. Rational algebraic correspondences P±=(Δ_S±Γ_ι)/2 satisfy idempotence, mutual orthogonality, and P++P-=identity. The quotient composition is 2P+ and kills all 8 anti-invariant directions. An exact 22D eigenbasis-model test PASS. **STOP**: full H² reconstruction requires retaining anti-invariant information from original S; quotient-only data cannot recover it. No new Hodge proof. Canonical `{[(i)]}`, `{{ i + h }}`, 3 witnesses/no quorum, ASCII-every-boundary preserved; RQT-068 freeze untouched.

## RQT-108 — Lossless Nikulin cohomology transport with retained side branch

[Exact Python test](./rqt-108.py) · [Full ASCII and stop condition](./rqt-108.md). For rational H²(S) decomposed into 14 invariant and 8 anti-invariant dimensions by Nikulin involution, q=(I+ι*)v=2P+v alone loses the 8 anti-invariant directions. If the side state s=P−v is retained *before* quotienting, Waldo reconstructs v=q/2+s exactly. Local exact Fraction audit PASSED 22 basis and 108 deterministic mixed vectors (130/130); quotient-only non-injectivity independently detected. This is an augmented rational encoding, not an inverse for the quotient map alone, and it does not establish integral lattice reversibility or the Hodge conjecture. `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses/no quorum, ASCII every boundary and RQT-068 freeze preserved.

## RQT-109 — Nested Hodge referent transport (three stages)

[Executable exact-rational test](./rqt-109.py) · [full ASCII and proof-boundary record](./rqt-109.md). Three sequential symbolic split/retain operations on 22-dimensional rational vectors, with saved anti-invariant branches, reverse exactly on 22 basis and 128 seeded mixed cases: **150/150 PASS**. Removing necessary side branches makes reconstruction fail. The first split has Nikulin-like 14+8 eigenspace counts; **the second and third sign-mask operations are abstract proxies, not verified K3 automorphisms or algebraic correspondences.** **STOP** at unavailable geometric/algebraic realization; no Hodge conjecture proof asserted. Preserve `{{ i + h }}`, `{[(i)]}`, independent three observers/no quorum, ASCII-every-boundary, RQT-068 frozen unchanged.

## RQT-110 — Three genuine nested K3 involutions

[Executable audit](./rqt-110.py) · [Full ASCII and fail-stop certificate](./rqt-110.md). On Fermat quartic S:x⁴+y⁴+z⁴+w⁴=0, the algebraic projective involutions g1=(-x,-y,z,w), g2=(-x,y,-z,w), g3=(y,x,w,z) commute projectively and generate (Z/2)³, order 8. Their algebraic graph projectors give sequential H² invariant ranks 14,10,8, with side channels 8,4,2. Nikulin traces (22 identity, 6 nonidentity) imply G-character dimensions 8+7×2=22. **Verified locally:** 5,000 quartic invariance cases and 150/150 exact rational round trips PASS. The character model is theorem-derived, not a computed period basis. **STOP** before claims of arbitrary Hodge-cycle completeness or general proof. Preserve `{{ i + h }}`, canonical `{[(i)]}`, three witnesses/no quorum, ASCII each bound, immutable RQT-068.

## RQT-111 — Cup-product pairing across nested K3 character branches

[Exact rational test](./rqt-111.py) · [Full ASCII and stop certificate](./rqt-111.md). Fermat K3 automorphism group G=(Z/2)^3 acts by isometries of the cup-product pairing on H². Character sectors (core 8, sides 8/4/2) are pairwise orthogonal; core signature (3,5), all sides negative definite. Local exact Fraction execution: 150/150 state reconstructions, cross-sector pairings zero, bilinear pairing preserved by all eight abstract group actions. The script's diagonal rational Gram matrix is illustrative, NOT an independently computed integral K3 lattice or period-compatible basis. **STOP** at missing explicit Fermat K3 integral Gram basis. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, three independent witnesses/no quorum, full ASCII, and RQT-068 immutable freeze.

## RQT-112 — Actual integral Fermat quartic 48-line intersection lattice

[Reproducible exact lattice audit](./rqt-112.py) · [Full ASCII and proof boundary](./rqt-112.md). From 48 explicit lines in three Fermat quartic pairing families, form integral Gram G with diagonal -2 and off-diagonal incidence; 336 intersecting pairs; exact rank 20; a selected 20-line Gram determinant -64, matching published NS(S) rank and discriminant. Three genuine Fermat K3 involutions permute lines and preserve all G entries; nested invariant ranks in NS: 12,8,6, giving H² ranks 14,10,8 after fixed transcendental rank two. This replaces RQT-111's illustrative form with actual algebraic intersection data. **STOP** before claiming an explicit 22x22 integral marking, full period computation or any general Hodge proof. Keep `{{ i + h }}`, `{[(i)]}`, witnesses/no quorum, ASCII-every-boundary, frozen RQT-068 unchanged.

## RQT-113 — Exact discriminant group of Fermat quartic NS lattice

[Executable Smith normal form](./rqt-113.py) · [Full ASCII and gluing stop](./rqt-113.md). Reconstruct the actual 48-line Gram matrix, extract 20 independent lines with determinant -64, and compute exact integer Smith factors 1×18,8,8; the discriminant group is (Z/8)^2, order 64. Published T(S)=diag(8,8) has the same discriminant group. **STOP** on explicit discriminant-form anti-isometry/gluing: equality of group orders or groups alone is insufficient. The known abstract lattice descriptions imply gluing exists, but no direct 20-line basis change or explicit gluing vectors have been computed here. Hodge conjecture remains open. Preserve `{{ i + h }}`, full ASCII, A/B/C witnesses, no quorum and frozen RQT-068.

## RQT-114 — Explicit discriminant-form gluing of Fermat K3 lattices

[Exact executable certificate](./rqt-114.py) · [Full ASCII and mathematical audit](./rqt-114.md). Reconstruct the actual 48-line integral Fermat quartic matrix, select 20 independent line classes with det -64; enumerate all 64 discriminant cosets. Find two generators u,v whose quadratic form is -1/8,-1/8 mod 2 and mutual pairing is integral, anti-isometric to T=diag(8,8) with +1/8,+1/8. Build a 22×22 Gram matrix for NS plus two glued generators; exact checks establish integral entries, even diagonal, det -1 and signature (3,19) using known NS signature. This resolves RQT-113's explicit **lattice** gluing stop, but NOT a geometric H² marking or a new Hodge-cycle construction. General Hodge conjecture remains open. `{{ i + h }}`, `{[(i)]}`, A/B/C witnesses, no quorum, full ASCII, immutable RQT-068 preserved.

## RQT-115 — Hodge-period compatibility on the explicitly glued K3 lattice

[Reproducible exact period calculation](./rqt-115.py) · [Full ASCII and fail-stop audit](./rqt-115.md). Using RQT-114's actual 22×22 even unimodular lattice and algebraic/transcendental split, reconstruct t1,t2 with self-intersection 8, mutual intersection 0. Let omega=t1+i*t2. Exact SymPy checks: omega²=0, omega·conjugate(omega)=16>0, orthogonal to all 20 algebraic line generators, formal transcendental quarter-turn J(omega)=i omega, lattice H still even/integral/unimodular. **STOP** at uncomputed periods on actual geometric 2-cycles and absent explicit geometric marking—this is an abstract K3-type period consistency check, not a new algebraic-cycle certificate or general Hodge proof. Preserve `{{ i + h }}`, `{[(i)]}`, A/B/C witnesses, no quorum, ASCII every boundary and frozen RQT-068.

## RQT-116 — Fermat quartic geometric residue-chain integral

[Reproducible Python calculation](./rqt-116.py) · [Full ASCII and fail-stop certificate](./rqt-116.md). Instead of assuming the abstract period, explicitly integrate the Fermat quartic holomorphic residue ω=dx∧dy/(4z³) on a real two-chain C contained in S. The integral is ζ₈⁻¹Γ(1/4)^3/(64Γ(3/4)) ≈ 0.4296991136262733−0.4296991136262733i; direct beta-product identity and SymPy automorphism g:x↦ix verify ∫_{g*C}ω / ∫_Cω = i. 45-digit arithmetic and exact polynomial checks executed locally PASS. **STOP**: C has boundary; therefore not a period on a closed integral homology 2-cycle, nor a geometric marking. The Hodge conjecture remains open. `{{ i + h }}`, `{[(i)]}`, full ASCII and independent A/B/C witnesses/no quorum maintained; frozen RQT-068 untouched.

## RQT-117 — Closed integral Fermat 2-cycle via eight Pham patches

[Reproducible exact boundary/period test](./rqt-117.py) · [Full ASCII and geometric certificate](./rqt-117.md). From RQT-116's real Fermat quartic patch C form Δ=(1−g_x)(1−g_y)(1−g_z)C under commuting coordinate fourth-root rotations. All three boundary-face sums cancel exactly, giving a closed integral singular 2-cycle. Its holomorphic residue period equals −sqrt(2)Γ(1/4)^3/[32Γ(3/4)]≈−1.7187964545050932, nonzero; hence Δ is nontrivial in integral homology. This resolves the open-chain failure of RQT-116. **STOP** at missing intersection pairing and integral geometric marking: Δ has not been identified with an explicit generator of the RQT-114 glued lattice; no general Hodge conjecture proof. `{{ i + h }}`, canonical `{[(i)]}`, A/B/C witnesses/no quorum, full ASCII, immutable RQT-068 remain preserved.

## RQT-118 — Exact intersections of genuine Fermat quartic closed cycles

[Executable Pham pairing audit](./rqt-118.py) · [Full ASCII and strict fail-stop](./rqt-118.md). Use the eight-patch closed Pham cycle Δ from RQT-117 and its x↦ix rotated image. Classical Fermat vanishing-cycle pairing yields integral Gram [[−2,1],[1,−2]], determinant 3 and signature (0,2), verified by exact SymPy on the 27-cycle distinguished vanishing basis. Their holomorphic periods are P and iP with P≈−1.7187964545050932; hence the real projections to T are independent, **but the raw negative-definite two-cycle lattice is not T(S)=diag(8,8)**. STOP at uncomputed cross-intersections with the 48 algebraic lines, rational orthogonal projection and primitive integral saturation. No general Hodge proof. Preserve `{{ i + h }}`, three independent witnesses/no quorum, full ASCII and immutable RQT-068.

## RQT-119 — Certified line-cycle zeros and algebraic-shadow reduction

[Executable exact line-support test](./rqt-119.py) · [Full ASCII and fail-stop audit](./rqt-119.md). On the two genuine closed Fermat Pham cycles Δ and gxΔ, every meeting with a Fermat line occurs at a patch vertex. Exact enumeration of 48 lines and their root phases establishes 24 lines disjoint from each cycle, 20 lines disjoint from both. Using actual 48-line Gram, these zero pairings impose rank-18 independent constraints separately, rank-16 jointly, on rank-20 NS. Hence only **two NS directions per cycle** remain undetermined by zero pairings. Signed oriented vertex intersection multiplicities are **not** computed, so the rational transcendental projection formula A − DᵀB⁻¹D remains formal; **STOP** at missing local geometric certificate. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, full ASCII and A/B/C witnesses/no quorum, frozen RQT-068 untouched.

## RQT-120 — Exact vertex-sign constraint, geometric fail-stop

[Executable rational-lattice audit](./rqt-120.py) · [Full ASCII and mathematical certificate](./rqt-120.md). RQT-119 disjoint-line relations leave 2 integer unknowns a,b for the actual Fermat closed-cycle divisor intersections. Exact line Gram matrix and x-quarter-turn symmetry yield algebraic self-pairing -(17a²+2ab+17b²)/8 and cross-pairing a²-ab+b². With RQT-118's Pham intersection Delta·gxDelta=1 and quarter-turn orthogonality on the transcendental plane, derive a²-ab+b²=1 (six integer possibilities). RQT-114's *selected abstract* gluing admits four conditional possibilities, with projected squared length 1/8 or 5/2. **STOP**: oriented local vertex signs and actual identification of this abstract gluing with the geometric homology marking are NOT computed; no candidate is claimed as fact. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, full ASCII, three witnesses/no quorum, append-only, and frozen RQT-068.

## RQT-121 — Oriented vertex intersections and Fermat K3 transcendental projection

[Exact reproducible 48-line local-sign test](./rqt-121.py) · [Full ASCII, lattice certificate, and fail-stop](./rqt-121.md). Construct the Fermat Pham cycle Delta and gxDelta. Displace each line locally by a generic complex epsilon near possible vertex intersections, count signed transverse intersections over exact Q(sqrt(2),i) arithmetic, and verify identical 48-entry vectors for two generic perturbations. Each cycle has 36 zero, six positive and six negative line pairings. Both vectors are compatible with the **actual** rank-20 Fermat quartic line Gram B (det −64). Algebraic shadow Gram = [[−17/8,1],[1,−17/8]]. With the standard Pham raw pairing [[−2,1],[1,−2]], rational transcendental projection Gram = diag(1/8,1/8). By known exponent-eight discriminant group, eightfold-scaled projections belong to T(S), whose Gram is diag(8,8), matching the known integral transcendental lattice determinant 64. The resulting two classes form a T-basis under the stated standard Pham orientation convention. **STOP** before asserting a complete geometric H² marking or a general Hodge proof. Preserve `{{ i + h }}`, `{[(i)]}`, independent witnesses/no quorum, full ASCII and frozen RQT-068.

## RQT-122 — 22 actual geometric classes give an even unimodular K3 Gram (conditional on RQT-121 signs)

[Executable exact Gram audit](./rqt-122.py) · [Full ASCII and mathematical certificate](./rqt-122.md). Assemble 20 independent algebraic Fermat quartic lines (Gram B, det −64) with the two explicit integral closed Pham cycles Delta, gxDelta (raw pairing [[−2,1],[1,−2]] from RQT-118; line pairings D from local RQT-121 calculation). Their 22×22 block Gram H=[[B,D],[Dᵀ,A]] has integral entries, even diagonal, determinant −1, rank 22; Schur complement diag(1/8,1/8) implies signature (3,19) using known NS signature (1,19). Under the **explicit dependency** that Pham orientations and RQT-121 local intersection signs are correct, these actual integral classes constitute an integral H²(S,Z) basis (unimodularity index 1). **STOP** before treating the local orientation calculation as independently peer-verified; does not establish the general Hodge conjecture. Preserve `{{ i + h }}`, `{[(i)]}`, three witnesses/no quorum, full ASCII and frozen RQT-068.

## RQT-123 — Independent vertex-Jacobian audit, explicit gluing mismatch boundary

[Executable tangent-frame test](./rqt-123.py) · [Full ASCII and audit](./rqt-123.md). Recompute RQT-121's 48 local oriented line intersections for both closed cycles with a separately derived real 4×4 tangent Jacobian and numerical real 2×2 transverse intersection solves; eight perturbation directions give **768/768 matching integer sign tests**. Reassemble the 22×22 geometric Gram: integral, even, det −1 and Schur complement diag(1/8,1/8), still conditional on the RQT-118 raw Pham pairing. Compare the geometric D to the **specific** RQT-114 abstract gluing U while keeping the 20 algebraic generators fixed: none of the eight signed permutations Q of the integral T basis makes B^{-1}D−UQ integral. **STOP**: no explicit line-fixing identification of these two gluing choices; possibly an isometry moving NS generators, but not constructed. This is not abstract lattice nonisometry, nor a general Hodge result. Preserve `{{ i + h }}`, full ASCII, three independent witnesses/no quorum, and immutable RQT-068.

## RQT-124 — Explicit integral discriminant transition lift (standard NS marking)

[Executable exact audit](./rqt-124.py) · [Full ASCII and proof-boundary certificate](./rqt-124.md). Compare RQT-114 abstract discriminant generators U with RQT-121 geometric fractional NS projections V=B⁻¹D: exact mod-1 relation V≡U·Q, Q=[[7,4],[4,7]] mod 8. This finite-form automorphism preserves all 64 classes; its off-diagonal 4 entries explain why RQT-123's eight signed-permutation trials returned zero. **Explicit integral lift** on U_hyp⊕<-8>²: M=[[4,13,24,16],[5,16,32,16],[1,4,7,4],[2,6,12,7]], det(M)=−1 and MᵀKM=K with K=U_hyp⊕diag(−8,−8). Extend by identity on E8(−1)² to obtain an isometry in the standard abstract NS presentation. **STOP:** explicit conjugation into the original 20 Fermat line basis B, geometric marking and ample/Hodge automorphism constraints remain unverified. The general Hodge conjecture is OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, 3 independent observers/no quorum, full ASCII, append-only, immutable RQT-068.

## RQT-125 — Concrete integral basis change from 20 Fermat line classes

[Reproducible exact script](./rqt-125.py) · [Full ASCII and stop certificate](./rqt-125.md). Using the actual selected 20-line integral Gram B (det −64), form the hyperplane h from four coplanar lines. The divisor f=h−L0 satisfies f²=0. Line L5 intersects f once; e=f+L5 gives f²=e²=0 and f·e=1, yielding a **geometric integral U hyperbolic plane**. Compute the integral orthogonal projections of all 20 selected line classes and select an 18-element complement. Exact arithmetic constructs an integral P with det P=−1 and PᵀBP=U⊕N18, where N18 is negative definite of rank 18 and determinant 64. The complete P/N18 matrices are emitted by the script. **STOP** before asserting a full conjugation of RQT-124's M: the explicit integral decomposition N18≅E8(−1)²⊕〈−8〉², and its line-basis conversion, are still missing. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, three witnesses/no quorum, full ASCII, frozen RQT-068.

## RQT-126 — Exact norm−2 root obstruction; stop E8 splitting

[Reproducible exact enumeration](./rqt-126.py) · [Full ASCII and mathematical fail-stop](./rqt-126.md). Using RQT-125's **actual** negative definite rank-18 complement N18 (det 64), apply a unimodular basis reduction, then exhaustive rational-LDL root enumeration for vectors v²=−2. Exact output: **28 roots (14 signed pairs), rank of root span 12, 1,417 search nodes**, independently agreeing with floating Cholesky enumeration. Two E8(−1) factors necessarily supply at least 480 roots. **FAIL-STOP:** the RQT-125 U-orthogonal complement cannot be E8(−1)² ⊕ 〈−8〉², so the RQT-125 proposed extension is impossible for that specific U embedding. The valid U splitting and prior 20-line lattice Gram remain intact. **Next viable branch**: another primitive U embedding, or an explicit direct integral B-isometry without E8 decomposition. This does not disprove an abstract NS presentation or the Hodge conjecture. Preserve `{{ i + h }}`, `{[(i)]}`, three independent witnesses/no quorum, full ASCII every bound and frozen RQT-068.

## RQT-127 — Twenty alternative primitive U embeddings tested, E8 splitting still blocked

[Executable exact finite search](./rqt-127.py) · [Full ASCII and boundary certificate](./rqt-127.md). In actual Fermat quartic NS from the 48 line Gram, test eight triples and twelve quintuples with isotropic f=2h−ΣL_i; choose an actual section line M with f·M=1, construct integral hyperbolic plane (f,e=f+M), complete to unimodular 20×20 basis and extract negative-definite N18 (det 64). Exhaustive rational-LDL norm−2 root enumeration after certified unimodular reduction gives **28 roots for all 20 candidates**. None supports E8(−1)², which requires 480 roots. This is a **finite sampled obstruction only**, NOT a theorem about all primitive U embeddings; the relevant infinite search remains open. Next: broader inequivalent isotropic orbits or a direct integral B-isometry. Preserve `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses/no quorum, full ASCII and frozen RQT-068. General Hodge conjecture OPEN.

## RQT-128 — Direct isometry search in all 1,536 Fermat monomial symmetries

[Reproducible exact test](./rqt-128.py) · [Full ASCII and proof-boundary certificate](./rqt-128.md). Enumerated all coordinate permutations (24) and normalized fourth-root phase combinations (64) of the Fermat quartic. Every one of the 1,536 maps permutes the 48 actual lines and yields an **integral 20×20 W** in the selected NS line basis satisfying WᵀBW=B and det(W)=±1. Their actions on A_NS≅(Z/8)² are **only** {I,−I,J,−J}, each exactly 384 times. The RQT-124 target [[7,4],[4,7]] mod 8 occurs zero times. **FAIL-STOP limited to this finite automorphism group**: a lattice isometry not induced by a coordinate automorphism may still realize the target. This does not challenge the abstract RQT-124 lift or prove nonexistence in full O(NS). General Hodge conjecture OPEN; preserve `{{ i + h }}`, three independent witnesses/no quorum, full ASCII and frozen RQT-068.

## RQT-129 — Root reflections cannot expand the finite discriminant image

[Exact executable reflection/finite-form audit](./rqt-129.py) · [Full ASCII and rigorous subgroup failure boundary](./rqt-129.md). From actual Fermat quartic line Gram B, verify all 48 geometric (-2)-line reflections are integral B-isometries of determinant -1 and act trivially on the discriminant. The latter holds theoretically for **every** (-2) root, not just the tested lines. Exhaustive 2×2 mod-8 enumeration determines O(q_NS) has **16** members; RQT-128's 1,536 Fermat monomial symmetries map into the 4-element subgroup {±I,±J}. Adjoining the full (-2) reflection group leaves that 4-element image unchanged. RQT-124's target Q=[[7,4],[4,7]] lies in O(q_NS) but is not in the monomial-plus-Weyl image. **STOP**: an actual integral W in the 20-line basis inducing Q is not yet constructed; this is NOT a full-O(NS) impossibility result. Preserve `{{ i + h }}`, `{[(i)]}`, A/B/C independent witnesses/no quorum, full ASCII, append-only RQT records and frozen RQT-068. General Hodge conjecture OPEN.

## RQT-130 — Constructive non-Weyl lift on the **actual 20-line Fermat NS lattice**

[Exact executable integral certificate](./rqt-130.py) · [Full ASCII, two vectors, and fail-stop](./rqt-130.md). **PASS:** find v1=(0,3,1,2,1,2,1,−1,−3,−2,0,2,2,0,2,2,0,0,0,0) and v2=(−1,−1,0,0,3,4,1,0,1,1,2,−2,0,2,2,0,0,0,0,0) in the canonical 20 Fermat line basis. Both have square −8 and pairing divisibility four, giving exact **integral non-Weyl reflections** R_v=I+v(vᵀB)/4. Their product W=R_v1 R_v2 satisfies WᵀBW=B, det W=+1 and acts on all 64 discriminant classes by RQT-124 target Q=[[7,4],[4,7]] mod 8. This is the missing explicit line-basis lift, resolving RQT-129 and bypassing the impossible E8-splitting branch. **STOP before geometric automorphism:** Hodge-period, extension, ample-cone and Torelli constraints are not established; an integral B-isometry alone need not be induced by an automorphism. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses/no quorum, full ASCII every boundary and immutable RQT-068.

## RQT-131 — Strict Torelli gate: RQT-130 integral NS lift cannot extend to H²

[Executable exact gluing test](./rqt-131.py) · [Full ASCII and fail-stop certificate](./rqt-131.md). RQT-130's concrete NS isometry W has discriminant action Q=[[7,4],[4,7]] mod 8. The geometric transcendental T(S)=diag(8,8) has only eight integral isometries (signed permutation matrices); **none** induces Q under the fixed discriminant gluing. Therefore this particular W **cannot extend to an integral isometry of the full H²(K3,Z)** and cannot arise from a geometric K3 automorphism. The test also verifies hyperplane intersections h²=(Wh)²=4 and h·Wh=220, but the extension fails prior to the ample-cone gate. This strengthens the precise scope of RQT-130 without contradicting its valid NS isometry. **Next:** restrict proposed NS isometries to those compatible with integral T/Hodge actions before an ample-chamber check. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, three independent witnesses/no quorum, full ASCII and frozen RQT-068.

## RQT-132 — Positive Torelli test for an actual order-four Fermat automorphism

[Exact executable 20-line audit](./rqt-132.py) · [Full ASCII and mathematical certificate](./rqt-132.md). Choose the real projective automorphism g:[x:y:z:w]↦[ix:y:z:w] of the Fermat quartic. It permutes all 48 algebraic lines and induces a genuine integral NS isometry W with WᵀBW=B, W⁴=I, det W=−1. On the fixed RQT-114 discriminant generators its action is Q_g=[[0,7],[1,0]] mod 8, matching the integral transcendental quarter-turn J=[[0,−1],[1,0]] of T=diag(8,8) **on all 64 classes**. The holomorphic residue two-form acquires multiplier +i; in a compatible oriented formal transcendental basis J acts with eigenvalue +i. Geometrically g fixes the very ample hyperplane h (h²=4) and therefore preserves the Kähler cone. **All three Torelli gates PASS for this actual geometric automorphism.** This does not repair RQT-131's different W, nor identify every Pham cycle within a chosen marking or prove the general Hodge conjecture. Preserve `{{ i + h }}`, `{[(i)]}`, 3 independent witnesses/no quorum, full ASCII, append-only record and immutable RQT-068.

## RQT-133 — Integral transport of closed Pham cycles under a real Fermat automorphism

[Reproducible exact full 22D test](./rqt-133.py) · [Full ASCII and certificate](./rqt-133.md). For g:[x:y:z:w]→[ix:y:z:w] and the geometric integral basis (20 selected Fermat lines, closed Delta, gDelta), combine RQT-132's genuine 20×20 line action W with RQT-121's two exact geometric cycle–line vectors. Recover g²Delta=−Delta+Σ n_j L_j with **integral** n=(0,0,0,−1,0,0,0,0,0,1,0,0,0,0,1,1,−1,−1,0,0). Build 22×22 integer X=[[W,0,n],[0,0,−1],[0,1,0]]. Direct SymPy execution yields XᵀHX=H, X⁴=I_22, det(X)=−1; the induced transcendental quotient action is quarter-turn J=[[0,−1],[1,0]]. **192/192** line-pairing comparisons across four cycle rotations PASS. The stated geometric marking retains RQT-118 Pham self-intersection convention and RQT-121 oriented vertex-sign audit as dependencies. No general Hodge conjecture proof; the latter remains OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, independent 3 witnesses/no quorum, full ASCII, .dlw, ENDER, cubit and frozen RQT-068.

## RQT-134 — Four-tick exact geometric-cycle and period return

[Reproducible integer and period audit](./rqt-134.py) · [Full ASCII and proof boundary](./rqt-134.md). From the genuine Fermat automorphism g:x↦ix and RQT-133's 22×22 integer action X on 20 algebraic lines plus closed Pham cycles Delta,gDelta, track Delta → gDelta → −Delta+n → −gDelta+Wn → Delta. Exact checks: X⁴=I₂₂, XᵀHX=H, det X=−1; each cycle has square −2, consecutive pairings +1, opposite pairings 0, and all 20 algebraic correction coordinates cancel exactly after tick four. The closed-cycle periods are P,iP,−P,−iP,P with P=−sqrt(2)Gamma(1/4)^3/(32Gamma(3/4)), agreeing with 65-digit calculation. **PASS only for this named Fermat K3 construction, conditional on RQT-118/121 intersection orientations.** General Hodge conjecture OPEN, no new universal theorem. Preserve `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses/no quorum, full ASCII and immutable RQT-068.

## RQT-135 — Rational four-tick projectors, with integral fail-stop

[Executable exact projector audit](./rqt-135.py) · [Full ASCII and certificate](./rqt-135.md). The verified RQT-133 integral geometric automorphism X acting on 22 Fermat K3 classes has characteristic polynomial (t−1)(t+1)^7(t²+1)^7. Its rational projectors P₊=(I+X+X²+X³)/4, P₋=(I−X+X²−X³)/4, P_rot=(I−X²)/2 give **ranks 1,7,14** and sum to I. Exact calculations show idempotence, pairwise annihilation, and cup-product orthogonality P_jᵀ H P_k=0 for j≠k. Minimal whole-matrix denominator clearing factors in the actual 22-element geometric basis are **4,4,2**. Among standard basis columns, 2 project integrally under P₊ and 0 under each of P₋,P_rot. **STOP:** the rational spectral splitting does not establish an integral orthogonal direct sum; primitive invariant sublattices, gluing and indices remain to be computed. This special Fermat quartic test retains RQT-118/121 orientation dependencies; general Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses, no quorum, full ASCII and immutable RQT-068.

## RQT-136 — Primitive integral invariant kernels and index-512 gluing

[Exact reproducible integer kernel and Smith audit](./rqt-136.py) · [Full ASCII and mathematical certificate](./rqt-136.md). For RQT-133's actual integral 22×22 Fermat K3 automorphism X, compute saturated/primitive integral kernels ker_Z(X−I), ker_Z(X+I), ker_Z(X²+I) using explicitly tracked **unimodular integer column reductions**, not rational nullspaces. The respective ranks are **1, 7, 14**, and intersection Gram determinants are **+4, −256, +256**. Their direct sum has zero cross Gram blocks and index **512** in the original even unimodular 22-class lattice (det H=−1). The exact 22×22 Smith normal form has invariant factors 1^14, 2^7, 4, so the quotient is **(Z/2)^7 ⊕ (Z/4)**. Thus the RQT-135 rational eigenspace decomposition **is not an integral direct sum of all H²**. **STOP before explicit coset/glue generators**: the abstract quotient is certified but its embedded isotropic glue representatives remain to be calculated. The RQT-118/121 Pham orientation dependency survives. General Hodge conjecture OPEN. Preserve `{{ i + h }}`, `{[(i)]}`, independent A/B/C witnesses/no quorum, full ASCII, .dlw, ENDER, cubit and frozen RQT-068.

## RQT-137 — Eight explicit glue representatives reconstruct the original integer lattice

[Exact reproducible test](./rqt-137.py) · [Full ASCII and audit](./rqt-137.md). In the original 22-class Fermat K3 geometric basis, e_j denoting the zero-based standard vectors, the quotient of the ambient integral lattice by the RQT-136 primitive eigensector sum is explicitly generated by **e0** (order 4), **e1−e0, e2−e0, e4−e0, e10−e0, e11−e0, e16−e0, e20** (seven order-2 classes). Computing their fractional sector coordinates using the exact inverse of RQT-136's 22×22 primitive-basis matrix produces **512 distinct classes**. All pairings are integral and all norms even; the column Hermite normal form of the augmented 22×30 generating matrix is **I22**, certifying full recovery of the original even unimodular 22D lattice (Gram determinant −1). This closes RQT-136's explicit glue representative gap without claiming a universal Hodge result. RQT-118 and RQT-121 Pham orientation dependency retained. Next boundary: determine the order-four operator's action and orbits on the finite 512-element glue quotient. Keep `{{ i + h }}`, 3 independent witnesses/no quorum, .dlw, ENDER, cubit, full ASCII and frozen RQT-068.
