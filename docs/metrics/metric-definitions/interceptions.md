# Interceptions

| Field | Value |
|---|---|
| Metric ID | `MET-DEF-INTERCEPTIONS` |
| Name | Interceptions |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts player-attributed interception evidence admitted by a versioned provider
event taxonomy. The candidate taxonomy must reconcile Interception events,
their outcomes, and the provider’s one-touch Pass type for an interception.

## Intended use

Totals/per 90, outcome splits, interception maps, Player Profile, Player
Explorer, Metric Leaders, Compare, sequence research, and similarity research.

## Prohibited interpretation

Until a taxonomy is selected, the count must not be labeled “interceptions won”
or compared across profiles. Even after selection it is not possession retained,
all reading of play, complete defensive quality, or continuous positioning.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
  `SRC-EVENT-BASE-TEAM-ID`, and `SRC-EVENT-BASE-LOCATION`.
- `SRC-INTERCEPTION-OUTCOME-ID` —
  `events[].interception.outcome.id`.
- `SRC-PASS-TYPE-ID` — `events[].pass.type.id`, including the documented
  Interception pass type candidate.
- `SRC-EVENT-BASE-COUNTERPRESS` and `SRC-EVENT-POSSESSION` — context.

## Prerequisites

`FEAT-INTERCEPTION`; unique valid event and actor/team; audited Interception
outcomes, Pass types, and cross-event deduplication rules.

## Formal definition

\[
INT_{p,t,s}^{(v)}=\sum_{e\in E_{p,t,s}}
I(\text{interceptionEvidence}^{(v)}(e))
\]

`EXP-DEF-001` must choose and version one of these alternatives:

1. all Interception events, with outcome as a split;
2. only Interception events whose outcome belongs to an audited successful set;
3. a deduplicated provider-complete taxonomy combining qualifying Interception
   events with qualifying one-touch Pass type Interception evidence.

No alternative is selected in this definition.

## Calculation steps

1. Select player-attributed Interception events and candidate Pass type evidence.
2. Validate event objects, outcome/type vocabulary, actor, and team.
3. Link or deduplicate representations according to taxonomy version.
4. Apply the selected attempt/success rule.
5. Retain source representation, outcome, location, counterpress, possession,
   and subsequent sequence evidence.
6. Aggregate total and per 90 only after the taxonomy is admitted.

## Numerator

Unique qualifying interception evidence under taxonomy version \(v\).

## Denominator

None for count/per 90. Outcome success and possession-adjusted variants require
separate denominators.

## Unit

Interceptions under a named taxonomy; optional per 90.

## Normalization

Expose total and per 90. Opponent-possession, opponent-action, or
out-of-possession adjustments remain competing `EXP-DEF-001` methods.

## Comparison group

Position-compatible player–team–season profiles with common taxonomy,
competitions/seasons, minute rule, and event coverage.

## Sample requirements

No validated threshold. Show minutes, total count, and outcome distribution.
Test through `EXP-DEF-001` and `EXP-THRESH-001`.

## Edge cases

- Whether every outcome counts or only successful outcomes is unresolved.
- A one-touch Pass type Interception can be a second representation of the same
  football action; the selected taxonomy must prevent double counting.
- Missing outcome may leave an attempt variant valid while making a successful
  variant unavailable.
- Interception followed by an immediate loss still counts; retention is separate.
- Ball Recovery, Block, Duel, and ordinary pass failures are not silently mapped
  to Interception.
- Duplicate event UUIDs count once and trigger quality handling.

## Missing-data handling

Missing actor/team/type excludes player attribution. Missing/malformed outcome
is reported; whether it remains eligible depends on the selected attempt or
successful taxonomy. Missing event files are not zero activity.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`,
`DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-DEF-001`, `EXP-THRESH-001`, and
  `EXP-REDUND-001`.
- Open gates: outcome and Pass-type vocabulary, representation deduplication,
  attempt/success selection, overlap with recoveries, immediate retention,
  opportunity denominators, and sample stability.

## Limitations

Recorded interceptions depend on opponent behavior, team system, possession
context, and provider event selection. Low counts can reflect lack of
opportunity rather than poor anticipation.

## References

- [Research dossier §§11.2–11.4 and 24](../../research/research-dossier.md)
- [Experiment registry: EXP-DEF-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-INTERCEPTION](../../data/feature-lineage.md)

## Examples

Illustrative only: four Interception events plus two Pass-type interception
records cannot be reported as six actions until relationship/deduplication and
outcome rules determine how many distinct qualifying interceptions exist.

## Changelog

- `0.1.0` — Competing provider-complete interception taxonomies registered; no
  default selected.
