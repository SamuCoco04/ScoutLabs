# Metric definition registry

Each file in this directory is the canonical, versioned specification for one
foundational metric. The [catalogue](../metric-catalog.md) provides the compact
cross-category view; these files own calculation detail, disputed alternatives,
edge cases, and prohibited interpretations.

## Current definitions

### Availability

- [Appearances](appearances.md) — `MET-AVAIL-APPEARANCES`
- [Starts](starts.md) — `MET-AVAIL-STARTS`
- [Minutes played](minutes-played.md) — `MET-AVAIL-MINUTES`

### Passing, progression, and creation

- [Completed passes](completed-passes.md) — `MET-PASS-COMPLETED`
- [Pass completion rate](pass-completion-rate.md) —
  `MET-PASS-COMPLETION-RATE`
- [Progressive passes](progressive-passes.md) — `MET-PROG-PASSES`
- [Progressive carries](progressive-carries.md) — `MET-PROG-CARRIES`
- [Final-third entries](final-third-entries.md) —
  `MET-PROG-FINAL-THIRD-ENTRIES`
- [Penalty-area entries](penalty-area-entries.md) —
  `MET-PROG-PENALTY-AREA-ENTRIES`
- [Shot assists](shot-assists.md) — `MET-CREATE-SHOT-ASSISTS`
- [Derived expected assists](derived-expected-assists.md) —
  `MET-CREATE-DERIVED-XA`

### Shooting

- [Non-penalty shots](non-penalty-shots.md) —
  `MET-SHOOT-NON-PENALTY-SHOTS`
- [Non-penalty xG](non-penalty-xg.md) —
  `MET-SHOOT-NON-PENALTY-XG`

### Defending and pressing

- [Pressures](pressures.md) — `MET-PRESS-PRESSURES`
- [Counterpress actions](counterpress-actions.md) —
  `MET-PRESS-COUNTERPRESS-ACTIONS`
- [Ball recoveries](ball-recoveries.md) — `MET-DEF-BALL-RECOVERIES`
- [Interceptions](interceptions.md) — `MET-DEF-INTERCEPTIONS`

### Goalkeeping

- [Goalkeeper xG faced](goalkeeper-xg-faced.md) — `MET-GK-XG-FACED`

## Governance

- Start new definitions from [_template.md](_template.md).
- Use exact `SRC-`, `FEAT-`, `DQ-`, `EXP-`, and completed `VAL-` identifiers.
- Use `Status: Proposed` when the formula, taxonomy, or edge cases remain
  disputed; name the competing definitions and experiment.
- Do not add a validation result until the cited validation has completed.
- Never change a calculation while retaining the same semantic version.
- Examples in definition files are formula illustrations, not claims about the
  local dataset or player performance.
