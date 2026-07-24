# Literature review

**Purpose:** concise synthesis for ScoutLabs decisions
**Primary reviewed source:** [ScoutLabs Research Dossier](research-dossier.md)
**Research cut-off inherited from the dossier:** 24 July 2026

This review does not replace the dossier. It maps its reviewed evidence to local-data
compatibility, product value, limitations, and the experiment registry. The dossier's
[full bibliography](research-dossier.md#28-full-bibliography) remains the canonical
bibliography; citations below use the same primary sources and recommendation IDs
`R1`–`R10`.

## Method assessment

| Method or topic | Evidence level | Data requirements | Local-data compatibility | Expected product value | Principal limitations | Recommendation classification | Experiments |
|---|---|---|---|---|---|---|---|
| StatsBomb event representation | A | Ordered event UUIDs, periods, timestamps, possessions, teams, players, locations, related events, and conditional subobjects | High; `Documented and observed`, subject to the field audit | Canonical source for direct metrics, sequences, and action maps | Selective event recording; conditional and version-varying fields; no continuous movement | Strong candidate for MVP (`R2`, `R9`) | `EXP-PASS-001`, `EXP-LOSS-001`, `EXP-DEF-001` |
| SPADL | A/B | Provider events convertible to standardized actions, results, body parts, coordinates, and game state | High after an audited converter | Reproducible research representation for action-value models | Conversion choices can discard provider detail and create a second semantic layer | Candidate requiring experiment (`R4`) | `EXP-VAEP-001` |
| Atomic-SPADL | B | SPADL plus finer action decomposition | Technically high | Research into granular attribution | Higher volume and explanation burden; incremental product value unproven | Research only | `EXP-VAEP-001` |
| Provider expected goals | A | Shot locations and context encoded by StatsBomb; supplied `shot.statsbomb_xg` | High where shot field occurs; `Documented and observed` | Direct shooting-quality summaries and input to derived xA | Provider model is not reproduced here; calibration may vary across population/version | Strong candidate for MVP as a provider value (`R2`) | `EXP-XA-001`, `EXP-GK-001` |
| Derived expected assists | A/B plus C inference | Verified shot-assist/shot relationship and linked shot `shot.statsbomb_xg` | High in principle; `VAL-REL-001` completed structural link resolution, while semantic flag reconciliation and metric-specific coverage remain open | Explainable chance-creation metric | Not a commercial provider xA field; depends on provider xG and reliable links | Strong candidate, pending experiment (`R5`) | `EXP-XA-001` |
| Expected Threat (xT) | A/D | Successful move actions, start/end zones, possession/transition logic, training population | High after normalization | Interpretable action-value enrichment for passing and carrying | Grid, sample, calibration, training population, and transition assumptions affect values | Candidate requiring experiment (`R4`) | `EXP-XT-001` |
| VAEP | A/B | SPADL sequences, contextual action features, scoring/conceding labels, trained probability models | High after conversion | Values on-ball actions beyond goals and assists | Training, calibration, leakage, and explanation burden; possible redundancy with direct metrics | Candidate requiring experiment (`R4`) | `EXP-VAEP-001` |
| Atomic-VAEP | B | Atomic-SPADL action decomposition plus trained scoring/conceding models | Technically compatible after an audited Atomic-SPADL conversion | Research into finer action attribution | Additional conversion, modeling, and explanation burden; incremental analyst value unproven | Research only | `EXP-VAEP-001` as a diagnostic comparator |
| Other possession-value methods | A/D | Varies; EPV requires synchronized tracking, while temporal xT and cooperative methods require richer model protocols | Event-only variants vary; tracking EPV is incompatible | Long-term research reference | Complexity, recency, data incompatibility, and weak MVP explainability | Research only or rejected for current data (`R10`) | `EXP-XT-001`, `EXP-VAEP-001` |
| Passing value and difficulty | A | Event-based value can use sequences; modern expected-pass difficulty needs synchronized player positions | Value models are compatible; proper tracking-based xPass is not | Separates territorial or outcome value from raw completion | Event-only difficulty is a different construct; direct metrics remain necessary | xT/VAEP experimental; proper xPass rejected for current data (`R4`, `R10`) | `EXP-PASS-001`, `EXP-XT-001`, `EXP-VAEP-001` |
| Progressive passes and carries | A/B/C | Direction-normalized start/end coordinates, action type/outcome, explicit geometric rule | High; geometry is present, but the label is ScoutLabs-derived | Transparent progression and entry dimensions | No universal definition; fixed distance, goal-distance, zone, and xT rules disagree | Strong candidate after comparison (`R2`, `R9`) | `EXP-PROG-001`, `EXP-ENTRY-001` |
| Possession-sequence participation | A/C | Ordered events, provider possession IDs/teams, players, action types, and relationship evidence | High after order/possession checks | Buildup and shot-ending possession context | Participation is not causal contribution; window and role definitions can duplicate activity volume | Candidate requiring experiment | `EXP-SEQUENCE-001` |
| Recorded defending and pressing | A | Pressure, counterpress, duel, interception, recovery, block, clearance, location, outcome, sequence context | Medium to high for recorded actions | Direct activity, location, and context profiles | Unrecorded positioning, cover, team shape, closing speed, and complete pressure intensity are absent | Event proxies are strong candidates; tracking-grade claims rejected (`R7`, `R10`) | `EXP-DEF-001` |
| Spatial event profiles | A/B/C | Direction-normalized event start/end locations, event family, outcome, sufficient sample | High | Action maps, zones, route summaries, and an additive similarity channel | They measure recorded activity rather than occupation; grid, KDE, and sample choices affect results | Direct maps strong candidate; similarity candidate requiring experiment (`R2`) | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` |
| StatsBomb 360 context | A | Event UUID, `freeze_frame[].location`, teammate, actor, goalkeeper, and `visible_area[]` | Partial: 426 files in the existing 3,961-match inventory | Selected-event context and explanation | Event-linked snapshots only; partial visibility and coverage; non-actor identities absent; possible flag anomalies | Candidate requiring experiment (`R6`) | `EXP-360-001`, `EXP-360-002` |
| Transparent distance similarity | B/C | Player-team-season features, comparison groups, scaling, weights, missingness policy | High after admitted features exist | Explainable candidate retrieval with decomposable differences | Sensitive to scale, redundancy, weights, minutes, population, and context | Strong baseline candidate (`R1`, `R3`) | `EXP-SCALE-001`, `EXP-DIST-001`, `EXP-SIM-001` |
| PCA, clustering, and embeddings | B/C | Sufficient clean feature matrix and stable cohorts | Technically compatible | Internal redundancy diagnostics, exploratory archetypes, future nonlinear research | Latent components and clusters are not inherently football concepts; embeddings reduce transparency | Research only | `EXP-REDUND-001`, `EXP-SIM-001` |
| Comparison populations and reliability | A/B/C | Position history, player-team-season unit, minutes, denominators, competitions, seasons, candidate filters | High after minutes and positions are validated | Prevents decontextualized percentiles and unstable retrieval | Position labels are incomplete roles; thresholds differ by metric; no MVP league-strength adjustment | Strong governance requirement (`R1`, `R3`) | `EXP-MIN-001`, `EXP-THRESH-001`, `EXP-SHRINK-001` |
| Explanation and recruitment validation | A/B/C | Versioned feature contributions, configuration, warnings, structured expert cases, negative controls | High in principle; requires product-specific evidence | Makes rankings inspectable and supports analyst control | Face validity is not causal validation; expert disagreement and contextual confounding remain | Required before admission (`R3`) | `EXP-SIM-002`, `EXP-SIM-003` |

## Event representations

StatsBomb events provide ordered, possession-aware observations with conditional
event-specific objects and relationships. They are a strong basis for direct metrics,
sequencing, and spatial action summaries, but they are not a continuous description of
all players or the ball. The official [event specification](https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Events%20v4.0.0.pdf)
and [data specification](https://github.com/hudl/open-data/blob/master/doc/StatsBomb%20Open%20Data%20Specification%20v1.1.pdf)
govern field semantics; the local audit governs observed availability. This distinction
supports `R2`, `R9`, and the evidence policy in
[research methodology](research-methodology.md#3-evidence-hierarchy).

SPADL and Atomic-SPADL offer provider-independent action representations through the
author-maintained [`socceraction` project](https://socceraction.readthedocs.io/en/stable/).
SPADL is suitable for reproducible xT/VAEP research. Atomic-SPADL's finer decomposition
may aid attribution, but it is not automatically interpretable enough for a product
surface. Neither representation should silently replace the richer provider source
record.

## Expected goals, expected assists, and possession value

StatsBomb shot xG is a provider-supplied value. ScoutLabs can aggregate it directly and,
after relationship validation, derive expected assists as the xG of linked assisted
shots. That derivation must retain the StatsBomb xG provenance and must not be described
as an available proprietary xA field (`R5`).

[Expected Threat](https://karun.in/blog/expected-threat.html) assigns value through
zone-to-zone changes in scoring threat. It is compatible with event coordinates and
relatively intuitive, but values depend on the grid, transition logic, action filter,
training population, and evaluation. Recent dossier evidence specifically motivates
quality testing before scouting use. `EXP-XT-001` therefore compares calibration,
population sensitivity, and incremental value against direct zone-entry metrics.

[VAEP](https://doi.org/10.1145/3292500.3330758) values actions through changes in
short-horizon scoring and conceding probabilities. It is broader than xT and has a
reproducible SPADL implementation, but it adds model and explanation complexity.
`EXP-VAEP-001` must test direct features alone against direct features plus VAEP and
record whether any gain survives ablation and football review.

Atomic-VAEP applies the same value framework to Atomic-SPADL's finer action
decomposition. It may improve attribution around receptions and ball movement, but the
additional granularity is not automatically useful or explainable to a recruitment
analyst. It remains a research-only diagnostic inside `EXP-VAEP-001`, not a separate
product candidate.

Tracking-based EPV, proper expected-pass difficulty, temporal possession value, and
cooperative contribution approaches describe important research frontiers. They do not
become local capabilities merely because the literature exists. In particular,
[spatio-temporal expected passes](https://doi.org/10.1007/s10618-021-00810-3) require
continuous player positions that the local event stream does not supply (`R10`).

## Passing, progression, and creation

Pass completion, progressive actions, entries, line-breaking, key passes, shot assists,
and xA are contested concepts. The literature supports explicit, versioned definitions
rather than one universal label:

- `EXP-PASS-001` audits failure outcomes and special denominators.
- `EXP-PROG-001` compares goal-distance, fixed-x, zone-advance, and xT-gain variants.
- `EXP-ENTRY-001` tests outside-to-inside final-third and penalty-area entries.
- `EXP-XA-001` validates the provider links required for derived xA.

The dossier cites Wyscout conventions as comparison evidence, not as a license to
rename StatsBomb fields. Provider-defined StatsBomb flags such as cross, cut-back,
switch, shot-assist, and through-ball technique remain provider values. Progressive
flags are ScoutLabs-derived. Research on
[repeatable progressive-pass clusters](https://doi.org/10.3233/JSA-220732) reinforces
that multiple stable descriptions may coexist.

## Defending and pressing

Recorded pressures, counterpress flags, recoveries, interceptions, duels, blocks, and
clearances support event-activity profiles. `EXP-DEF-001` must establish the event
taxonomy and compare clear opportunity denominators. It must not turn activity volume
into a claim of complete defensive quality.

Tracking research on
[counterpressing](https://doi.org/10.1007/s10618-021-00763-7) and
[pressure](https://doi.org/10.1007/s10618-017-0513-2) shows why full team structure,
closing speed, and off-ball behavior need synchronized locations. This evidence
supports the boundary in `R7` and `R10`: the product may expose recorded event proxies,
not tracking-grade pressing intensity.

## Possession sequencing

Provider possession identifiers and event order support reproducible grouping of
recorded actions. `EXP-SEQUENCE-001` compares whole-possession participation,
shot-ending participation, and bounded action windows. It keeps direct actor, secondary
participation, and inferred buildup roles separate. A player appearing in a sequence is
not evidence that the player caused its eventual outcome; sequence features must be
tested for redundancy with ordinary action volume.

## Spatial player profiles and 360 context

Direction-normalized event locations support named action maps, fixed-grid and tactical
zone shares, centroids for a specified event family, and pass/carry transition vectors.
They do not support a generic average position or tracking heatmap. `EXP-SPATIAL-001`
and `EXP-SPATIAL-002` evaluate whether histograms and transitions add stable information
beyond direct metrics.

The official [360 specification](https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20360%20Frames%20v1.0.0%20%281%29.pdf)
documents event-linked visible players and polygons. Only visible players are
represented; non-actor identities are absent; polygons and flags can be incomplete.
`EXP-360-001` defines usable-frame criteria before `EXP-360-002` tests nearest-visible
opponent, local density/support, and visible numerical balance. This is a selective
context layer under `R6`, never universal tracking or a source of commercial StatsBomb
360 metrics.

## Player similarity and comparison populations

The default analytical unit is player-team-season (`R1`). Combined player-season views
may be presented, but team-specific samples and multi-team composition must remain
visible. Candidate universes should be position-compatible, minute-aware, and
configurable; goalkeepers require a separate feature family and experimental path
(`R8`).

Weighted Euclidean and Manhattan distances are strong transparent baselines. Euclidean,
cosine, and Mahalanobis remain comparison methods. Nearest-neighbour retrieval is only
as valid as its features, scaling, weights, missingness, and candidate population.
[`scikit-learn` distance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html)
and [nearest-neighbour](https://scikit-learn.org/stable/modules/neighbors.html)
documentation supports mechanics, not football validity.

PCA can diagnose redundancy; clustering can explore repeated profiles; embeddings may
capture nonlinear structure. None should become the production ranking or explanation
space without demonstrating stable, incremental, interpretable value over transparent
baselines.

## Explainability and recruitment limitations

Similarity explanations must expose the candidate population, inputs, scaling, weights,
missing fields, coverage penalty, model version, strongest similarities, and strongest
differences. Transparent decompositions are preferred before model-agnostic explainers.
[LIME](https://doi.org/10.1145/2939672.2939778) and
[SHAP](https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html)
remain research-only unless a more complex model earns admission.

Recruitment interpretation remains bounded by team tactics, opponent and teammate
quality, selective historical coverage, mixed positions, survivorship, small samples,
and unavailable financial, medical, contractual, personality, and video information.
Methodological reviews of
[footballer attributes](https://doi.org/10.3233/JSA-200554) and
[talent identification](https://doi.org/10.1007/s40279-019-01113-w) support the need for
multiple evidence types and conservative claims. Statistical similarity is a
first-screening aid, never evidence of quality, fit, affordability, or likely transfer
success.

## Decision summary

- Preserve the player-team-season unit and direct event evidence (`R1`, `R2`).
- Test a decomposable nearest-neighbour baseline before complex similarity (`R3`).
- Keep xT and VAEP experimental (`R4`).
- Validate linked-shot xA rather than claim a provider xA field (`R5`).
- Restrict 360 to coverage-aware experiments (`R6`).
- Label pressure and counterpress outputs as recorded event proxies (`R7`).
- Separate goalkeeper research (`R8`).
- Version contested definitions (`R9`).
- Reject tracking-dependent claims under the present source boundary (`R10`).
