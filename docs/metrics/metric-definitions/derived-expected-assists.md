# Derived expected assists

| Field | Value |
|---|---|
| Metric ID | `MET-CREATE-DERIVED-XA` |
| Name | Derived expected assists |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Sums StatsBomb shot xG for teammate shots directly linked to qualifying
shot-assisting passes. It estimates the pre-shot chance quality created by those
passes.

## Intended use

Chance-creation totals/per 90, Player Profile, Player Explorer, Metric Leaders,
Compare, and similarity research, always labeled “ScoutLabs-derived xA from
linked StatsBomb shot xG.”

## Prohibited interpretation

This is not a provider-supplied xA field, pass-completion probability, causal
credit, total creative value, guaranteed assist probability, or a model trained
by ScoutLabs. It inherits the provider’s shot xG model.

## Source fields

All fields in [shot assists](shot-assists.md), plus:

- `SRC-SHOT-XG` — `events[].shot.statsbomb_xg`, provider-supplied pre-shot xG.
- `SRC-SHOT-TYPE-ID` and `SRC-SHOT-OUTCOME-ID` — linked-shot context and
  edge-case taxonomy.

## Prerequisites

`FEAT-SHOT-ASSIST`, `FEAT-DERIVED-XA`, `FEAT-SHOT-XG`; unique resolved
Pass-to-Shot relationship; numeric finite xG in its valid domain; consistent
match/team; versioned shot-assist policy.

## Formal definition

For qualifying pass set \(Q_{p,t,s}^{(v)}\) and its unique linked shot \(q(e)\):

\[
xA_{p,t,s}^{(v)}=\sum_{e\in Q_{p,t,s}^{(v)}}
\text{statsbomb\_xg}(q(e))
\]

Each linked shot contributes at most once to one qualifying pass under the
selected relationship policy. This is a direct aggregation of provider xG
through a ScoutLabs-derived link, not a newly fitted expected-assist model.

## Calculation steps

1. Construct qualifying, resolved shot assists using one version.
2. Join each pass to one teammate Shot in the same match.
3. Validate finite numeric `shot.statsbomb_xg` and shot taxonomy.
4. Deduplicate by qualifying pass/shot relationship.
5. Sum xG and retain shot-assist count, xG coverage, and source/model metadata.

## Numerator

Sum of provider-supplied StatsBomb xG over uniquely linked qualifying shots.

## Denominator

None for total/per 90. xA per shot assist is a separate rate and must show the
shot-assist denominator.

## Unit

Expected goals credited as derived expected assists; optional per 90.

## Normalization

Expose total and per 90. Do not combine values produced by materially different
provider xG versions without preserving/versioning that difference. Percentiles
require the same xA/link version and comparison group.

## Comparison group

Position-compatible player–team–season profiles with common link policy,
provider version treatment, competition/season scope, and minutes/sample rules.

## Sample requirements

No validated minimum. Show minutes, qualifying shot assists, linked shots, and
xG coverage. Test sparse-sample stability through `EXP-XA-001`,
`EXP-THRESH-001`, and `EXP-SHRINK-001`.

## Edge cases

- A valid shot-assist link with missing/invalid xG is excluded from xA but
  remains in shot-assist coverage reporting.
- Duplicate forward/reverse/related links contribute once.
- Conflicting candidate passes for one shot require investigation; do not split
  or duplicate xG silently.
- Own goals, penalties arising after a pass, deflected chains, nullified shots,
  and event corrections require taxonomy decisions.
- Goal outcome does not change the xG contribution.
- Combining team profiles requires summing xG, not averaging per-team xA.

## Missing-data handling

Return xA only over a declared eligible link set and expose both link-resolution
and xG-field coverage. A profile below a future coverage threshold is
unavailable for comparison; missing xG is never zero.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`,
`DQ-REL-UNRESOLVED`, `DQ-PASS-SHOT-LINK`, `DQ-PROVIDER-VERSION`, and
`DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-XA-001`, `EXP-THRESH-001`, and
  `EXP-SHRINK-001`.
- Open gates: link reconciliation, provider xG version handling, unusual shot
  chains, coverage, aggregation invariants, stability, and football review.

## Limitations

Only final-pass creation receives credit. The result depends on teammate shot
selection and the provider xG model and omits buildup, non-shot creation, and
unlinked actions.

## References

- [Shot-assists definition](shot-assists.md)
- [Research dossier §§7.7, 10, 24, and R5](../../research/research-dossier.md)
- [Experiment registry: EXP-XA-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-DERIVED-XA](../../data/feature-lineage.md)

## Examples

Illustrative only: three uniquely linked qualifying shots with StatsBomb xG
0.10, 0.25, and 0.05 yield 0.40 derived xA. Their actual outcomes do not change
that sum.

## Changelog

- `0.1.0` — Initial linked-shot-xG proposal; no proprietary xA claim.
