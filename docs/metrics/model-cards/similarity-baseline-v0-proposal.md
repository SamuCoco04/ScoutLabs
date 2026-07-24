# Similarity baseline v0 proposal

**Model ID:** `MOD-SIM-BASELINE-V0`

| Field | Value |
|---|---|
| Model ID | `MOD-SIM-BASELINE-V0` |
| Name | Explainable player-profile nearest-neighbour baseline |
| Version | `0.1.0` |
| Status | Proposal |
| Owner | ScoutLabs research |

This card specifies a comparison design. No algorithm, weights, feature set, or
production model has been selected, trained, or validated.

## Intended use

Research whether transparent distance-based retrieval can produce stable,
football-plausible candidate lists for an analyst who selects a reference
player–team–season profile. If admitted later, the method could support Similar
Players and explanations in Player Profile and Compare.

## Prohibited use

Similarity is not quality, performance rank, potential, tactical fit, team fit,
affordability, medical readiness, personality assessment, or transfer advice.
The model must not be used to claim that a candidate is better than the
reference player or will succeed after a transfer.

## Analytical unit

The default unit is player–team–season. A player with multiple teams has
separate profiles; a combined player–season view, if evaluated, must retain the
contributing team profiles and minutes. Goalkeepers are excluded from outfield
retrieval and evaluated through `EXP-GK-002`.

## Candidate population

The query configuration must retain:

- compatible position groups, with mixed-position evidence and analyst override;
- competition and season filters;
- a candidate minimum-minutes rule selected only after `EXP-THRESH-001`;
- the source snapshot and metric versions;
- exclusions and coverage reasons;
- no self-profile result unless the experiment explicitly tests same-player
  seasons.

League-strength equivalence is not assumed. Cross-competition results require a
visible warning.

## Input features

The initial comparison set is not fixed. Candidate families are availability
context (shown, not weighted as playing style), passing/circulation,
progression, creation, carrying/dribbling, shooting, possession security,
recorded defending, pressure/counterpress activity, spatial summaries, and a
separate goalkeeper family. Only metrics with adequate lineage and quality may
enter the vector.

Possible inputs are the versioned candidates in
[the metric catalogue](../metric-catalog.md), including
`MET-PASS-COMPLETION-RATE`, `MET-PROG-PASSES`, `MET-PROG-CARRIES`,
`MET-PROG-FINAL-THIRD-ENTRIES`, `MET-PROG-PENALTY-AREA-ENTRIES`,
`MET-CREATE-DERIVED-XA`, `MET-SHOOT-NON-PENALTY-SHOTS`,
`MET-SHOOT-NON-PENALTY-XG`, `MET-DEF-BALL-RECOVERIES`,
`MET-DEF-INTERCEPTIONS`, `MET-PRESS-PRESSURES`, and
`MET-PRESS-COUNTERPRESS-ACTIONS`.

The proposal-level mapping is explicit but is not a frozen model input set:

| Candidate metrics (all `0.1.0`) | Candidate features (all `0.1.0`) |
|---|---|
| `MET-PASS-COMPLETION-RATE` | `FEAT-PASS-COMPLETION-RATE` |
| `MET-PROG-PASSES`, `MET-PROG-CARRIES` | `FEAT-PROGRESSIVE-PASS`, `FEAT-PROGRESSIVE-CARRY` |
| `MET-PROG-FINAL-THIRD-ENTRIES`, `MET-PROG-PENALTY-AREA-ENTRIES` | `FEAT-FINAL-THIRD-ENTRY`, `FEAT-PENALTY-AREA-ENTRY` |
| `MET-CREATE-DERIVED-XA` | `FEAT-DERIVED-XA` |
| `MET-SHOOT-NON-PENALTY-SHOTS`, `MET-SHOOT-NON-PENALTY-XG` | `FEAT-NON-PENALTY-SHOT`, `FEAT-NON-PENALTY-XG` |
| `MET-DEF-BALL-RECOVERIES`, `MET-DEF-INTERCEPTIONS` | `FEAT-BALL-RECOVERY`, `FEAT-INTERCEPTION` |
| `MET-PRESS-PRESSURES`, `MET-PRESS-COUNTERPRESS-ACTIONS` | `FEAT-PRESSURE`, `FEAT-COUNTERPRESS` |

`EXP-REDUND-001` must remove conceptual duplicates and quantify correlated
families before a candidate vector is frozen. Sparse 360 metrics cannot enter a
global baseline unless `EXP-360-001` and `EXP-360-002` establish comparable
coverage.

## Preprocessing

`EXP-SCALE-001` compares z-score scaling, robust scaling, and percentile-based
family aggregation fitted only on the configured candidate population. Raw
totals, per-90 values, success rates, and percentiles remain distinguishable.
Scaling parameters are retained with every result. Winsorization or other
outlier treatment is prohibited unless versioned and experimentally justified.

No data from the reference query outcome, expert labels, or future seasons may
leak into preprocessing.

## Missing-data policy

Missing is never zero. `EXP-MISS-001` compares:

1. excluding profiles below a minimum usable-feature threshold;
2. distance on common eligible features with weight renormalization and an
   explicit coverage penalty;
3. defensible imputation with a missingness indicator.

Every result must expose omitted features, effective feature-weight coverage,
and whether profiles were compared on different vectors. The proposal selects
none of these policies.

## Weighting

Dimension weights are visible, normalized to sum to one, non-negative, and
versioned. Uniform family weights and position-specific candidate weights must
be compared. Custom analyst weights must be retained beside defaults.
`EXP-REDUND-001` tests double counting; `EXP-SIM-003` tests explanation and
football usefulness. No default weights are selected here.

## Algorithm candidates

Weighted Euclidean and Manhattan are the two baseline candidates.

For scaled vectors \(x\) and \(y\), eligible feature set \(J\), and normalized
non-negative weights \(w_j\):

\[
d_{WE}(x,y)=\sqrt{\sum_{j \in J} w_j(x_j-y_j)^2}
\]

\[
d_{M}(x,y)=\sum_{j \in J} w_j|x_j-y_j|
\]

Unweighted Euclidean, cosine, and Mahalanobis are required comparison
experiments under `EXP-DIST-001`. Mahalanobis requires stable covariance
estimation and regularization; cosine may obscure level differences; ordinary
Euclidean tests the effect of weights. None is the production choice.
Nearest-neighbour retrieval orders eligible candidates by the selected
distance, with deterministic tie handling.

No distance-to-0–100 similarity transformation is defined. Such a transform
would require calibration and must not imply probability or confidence.

## Output

An experimental result must retain:

- ordered candidate IDs and raw distance;
- reference and candidate analytical-unit identifiers;
- candidate-universe filters and exclusion count;
- source, metric, feature, preprocessing, and model versions;
- minutes and usable-feature coverage;
- family and feature contributions;
- strongest similarities and differences;
- low-sample, missingness, cross-competition, and instability warnings.

## Explanation

Weighted Euclidean contribution is \(w_j(x_j-y_j)^2\); Manhattan contribution
is \(w_j|x_j-y_j|\). Contributions are aggregated into named football families,
shown both as shares and underlying standardized differences. Explanations must
show differences that weaken similarity as prominently as supporting evidence.

The analyst must be able to inspect the comparison group, raw metric values,
normalization, active weights, omitted features, coverage penalty, and model
version. Mathematical contribution is not causal explanation.

## Required validation gates

The proposal cannot advance beyond `Proposal` until all applicable gates pass:

1. **Mechanical correctness:** deterministic retrieval, scaling isolation,
   contribution sums, tie handling, missingness, and version retention.
2. **Metric admission:** every input has completed lineage, coverage, tests, and
   appropriate maturity; disputed metrics retain their versions.
3. **Sensitivity:** `EXP-SCALE-001`, `EXP-DIST-001`, `EXP-REDUND-001`,
   `EXP-MISS-001`, `EXP-THRESH-001`, and `EXP-SHRINK-001`.
4. **Stability:** bootstrap/removal-of-match neighbour overlap and rank
   correlation; small perturbations cannot be hidden.
5. **Positive and negative controls:** `EXP-SIM-002` same-player seasons,
   pre-registered stylistic cases, incompatible-position controls, synthetic
   mechanics, and noise controls.
6. **Expert review:** structured, repeatable assessment through `EXP-SIM-003`,
   including disagreements and negative results.
7. **Goalkeeper separation:** `EXP-GK-002` before any goalkeeper retrieval.
8. **Product review:** explanations and warnings are understandable and support
   screening without implying transfer advice.

No completed `VAL-` record currently validates this model.

## Sensitivity plan

Measure top-k overlap, rank correlation, distance contribution shifts, and
exclusion/coverage changes across scaling, distances, feature ablations,
correlation pruning, minute thresholds, match bootstraps, family weights,
position groups, competitions, missingness, and partial-season profiles. Report
heterogeneous and negative results rather than averaging them away.

## Limitations

Event metrics reflect opportunity, team style, role, teammates, opponents,
competition, and sample. Position labels are incomplete role proxies. Open Data
is a selective historical universe. Per-90 scaling does not create reliability.
Partial 360 coverage can create selection bias. Transparent distance does not
make the feature space football-valid.

## Decision risks

- A plausible score can create false authority: retain raw distances, warnings,
  and analyst control.
- Redundant volume metrics can dominate: apply `EXP-REDUND-001` and family-level
  contribution limits.
- Sparse profiles can look extreme: apply explicit eligibility and stability
  rules.
- Cross-competition proximity can imply equivalence: display context and no
  unvalidated league-strength correction.
- A candidate can be statistically close but unsuitable: repeat the prohibited
  interpretations in every user-facing result.

## Reproducibility

Every run records source snapshot/commit, ScoutLabs code commit, analytical-unit
IDs, candidate query, exact `MET-`/`FEAT-` versions, scaler parameters, missing
policy, weights, distance, tie rule, software environment, random seeds used by
resampling, timestamp, and ordered output. A model artifact must be immutable
once referenced.

## Dependencies

Data and feature lineage is defined in
[feature lineage](../../data/feature-lineage.md). The proposal depends on
`SRC-COMPETITION-ID`, `SRC-SEASON-ID`, `SRC-MATCH-ID`,
`SRC-MATCH-HOME-TEAM-ID`, `SRC-MATCH-AWAY-TEAM-ID`,
`SRC-LINEUP-TEAM-ID`, `SRC-LINEUP-PLAYER-ID`,
`SRC-EVENT-TACTICS-LINEUP`, `SRC-SUBSTITUTION-REPLACEMENT-ID`,
`SRC-PLAYER-OFF-PERMANENT`, `SRC-EVENT-BASE-ID`,
`SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
`SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-PERIOD`,
`SRC-EVENT-BASE-TIMESTAMP`, `SRC-EVENT-BASE-LOCATION`,
`SRC-PASS-OUTCOME-ID`, `SRC-PASS-END-LOCATION`,
`SRC-CARRY-END-LOCATION`, `SRC-SHOT-TYPE-ID`, `SRC-SHOT-XG`,
`SRC-BALL-RECOVERY-FAILURE`, `SRC-INTERCEPTION-OUTCOME-ID`, and
`SRC-EVENT-BASE-COUNTERPRESS`, through the `FEAT-`/`MET-` `0.1.0` mappings
listed above.

Candidate-population eligibility and exposure additionally depend on
`FEAT-APPEARANCE`, `FEAT-START`, and `FEAT-MINUTES` `0.1.0`; they provide
context and sample gates and are not automatically weighted style dimensions.

Blocking quality dependencies include `DQ-ID-MISSING`, `DQ-ID-TYPE`,
`DQ-LINEUP-CONSISTENCY`, `DQ-STARTING-XI-CONSISTENCY`,
`DQ-SUBSTITUTION-CONSISTENCY`, `DQ-PLAYER-ON-OFF`,
`DQ-INCOMPLETE-VIDEO`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`,
`DQ-COORD-SHAPE`, and `DQ-COORD-RANGE`. A future run must also pin the
dataset manifest, every admitted metric and feature version, the ScoutLabs
commit, Python/runtime version, and exact numerical-library versions. No
similarity software or runtime dependency is selected or implemented by this
proposal.

## Related experiments

`EXP-SCALE-001`, `EXP-DIST-001`, `EXP-REDUND-001`, `EXP-MISS-001`,
`EXP-THRESH-001`, `EXP-SHRINK-001`, `EXP-SIM-001`, `EXP-SIM-002`,
`EXP-SIM-003`, `EXP-SPATIAL-001`, `EXP-SPATIAL-002`, `EXP-360-001`,
`EXP-360-002`, and `EXP-GK-002`; all are planned.

## References

- [Research dossier §§15–17 and recommendations R1, R3, R6, R8–R10](../../research/research-dossier.md)
- [Similarity research plan](../../research/similarity-research.md)
- [Experiment registry](../../research/metric-experiments.md)
- [Product brief §§10, 12, 20, and 29](../../../BRIEF.md)

## Changelog

- `0.1.0` — Initial proposal; no algorithm or production configuration selected.
