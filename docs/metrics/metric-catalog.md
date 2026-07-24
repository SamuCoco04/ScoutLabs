# Candidate metric catalogue

**Catalogue version:** `0.1.0`  
**Scope:** definitions and research candidates, not implemented product metrics  
**Maturity:** every entry is `Proposed` or `Researching`; none is
`Approved for MVP`

This catalogue translates the product questions in the
[Product Brief](../../BRIEF.md) and evidence in the
[research dossier](../research/research-dossier.md) into versioned metric
candidates. Individual files own the full foundational definitions; this file
is the canonical cross-category registry.

## How to read the catalogue

Each category has two keyed tables:

1. **Definition** records Metric ID, name, football question, conceptual
   definition/formula, numerator, denominator, unit, normalization, maturity,
   and version.
2. **Lineage and admission** records source fields, features, provenance,
   comparison group, positional relevance, sample requirement, observed
   coverage, quality dependencies, limitations, evidence, product surfaces,
   experiments, and validation.

Together those rows provide every required catalogue field for every Metric ID.
Category is supplied by the section heading.

“Observed coverage: not quantified” is deliberate: this documentation task has
not calculated player metrics or their eligible conditional denominators.
Source-level measurements belong in the
[coverage report](../data/coverage-report.md). Presence of a source family is
not substituted for metric coverage. No zero, percentage, or completeness claim
is inferred.

Shared rules:

- Default analytical unit: player–team–season; combined player–season views
  retain contributing teams and aggregate numerators/denominators before rates.
- `per 90 = total × 5,400 / validated player seconds`; rounded display minutes
  are never used as a denominator.
- Rate metrics retain numerator and denominator. Zero denominator returns
  unavailable.
- Comparison normalization is fitted to a named population containing position
  group, competition/season scope, sample rules, and metric version.
- Missing records are never silently zero. Conditional-field eligibility and
  excluded records are reported.
- Validation is “None” unless a completed `VAL-` record exists. A planned
  experiment is not validation.

## Availability and minutes

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-AVAIL-APPEARANCES | Appearances | In how many covered matches did the player enter the field? | Count distinct valid matches with reconciled Starting XI, substitution-replacement, Player On, or reliable actor evidence: \(\sum_m I(\text{on-pitch evidence})\). | Matches with on-pitch evidence | None | Matches | Total only; sample context, not per 90 | Proposed | `0.1.0` |
| MET-AVAIL-STARTS | Starts | In how many covered matches did the player begin on the field? | Count distinct valid matches whose team Starting XI `tactics.lineup` contains the player. | Starting-XI matches | None | Matches | Total; optional starts/appearances requires a separate rate | Proposed | `0.1.0` |
| MET-AVAIL-MINUTES | Minutes played | How much evidenced on-pitch time did the player have? | Sum validated on-pitch intervals over actual endpoints for periods 1–4; exclude period 5; divide raw seconds by 60. | Validated on-pitch seconds | 60 seconds/minute | Minutes backed by raw seconds | Base exposure; per-90 consumers use raw seconds | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-AVAIL-APPEARANCES` | `SRC-LINEUP-PLAYER-ID`, `SRC-EVENT-TACTICS-LINEUP`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-SUBSTITUTION-REPLACEMENT-ID` → `FEAT-APPEARANCE` | ScoutLabs-derived participation state | No performance percentile; all positions; preserve team/season and covered matches | None to calculate; downstream gates are metric-specific | Not quantified; participation algorithm not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-LINEUP-CONSISTENCY`, `DQ-STARTING-XI-CONSISTENCY`, `DQ-SUBSTITUTION-CONSISTENCY`, `DQ-PLAYER-ON-OFF`, `DQ-EXTRA-TIME`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO` | Roster presence is not participation; event evidence can conflict | Dossier §§5–6; R1, R2, R9 | Player Profile, Player Explorer, Compare, Similar Players warnings | `EXP-MIN-001` | None |
| `MET-AVAIL-STARTS` | `SRC-EVENT-TACTICS-LINEUP`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-LINEUP-PLAYER-ID` → `FEAT-START` | Direct aggregation of provider tactical snapshot | No performance percentile; all positions | None to calculate | Not quantified; Starting XI reconciliation not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-LINEUP-CONSISTENCY`, `DQ-STARTING-XI-CONSISTENCY`, `DQ-EVENT-TYPE-OBJECT`, `DQ-INCOMPLETE-VIDEO` | Starting position is a snapshot, not a complete role | Dossier §§5–6; R1, R2 | Player Profile, Player Explorer, Compare, Similar Players warnings | `EXP-MIN-001` | None |
| `MET-AVAIL-MINUTES` | `SRC-EVENT-TACTICS-LINEUP`, `SRC-EVENT-BASE-PERIOD`, `SRC-EVENT-BASE-TIMESTAMP`, `SRC-EVENT-BASE-MINUTE`, `SRC-EVENT-BASE-SECOND`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-SUBSTITUTION-REPLACEMENT-ID`, `SRC-SUBSTITUTION-OUTCOME-ID`, `SRC-PLAYER-OFF-PERMANENT`, `SRC-HALF-END-EARLY-VIDEO-END`, `SRC-HALF-END-MATCH-SUSPENDED` → `FEAT-MINUTES` | ScoutLabs-derived interval aggregation | Sample context for every position; threshold may be position/metric-specific | No minimum to calculate; eligibility unresolved | Not quantified; complete interval algorithm and edge cases not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-STARTING-XI-CONSISTENCY`, `DQ-SUBSTITUTION-CONSISTENCY`, `DQ-PLAYER-ON-OFF`, `DQ-EVENT-TIMESTAMP-ORDER`, `DQ-PERIOD-BOUNDARY`, `DQ-STOPPAGE-TIME`, `DQ-EXTRA-TIME`, `DQ-SHOOTOUT`, `DQ-DISMISSAL`, `DQ-INCOMPLETE-VIDEO` | Dismissals, interrupted video, duplicate changes, actual endpoints, and extra time require validation | Dossier §6; R1, R2, R9 | All analytical product surfaces and quality warnings | `EXP-MIN-001`, `EXP-THRESH-001`, `EXP-SHRINK-001` | None |

Detailed definitions: [appearances](metric-definitions/appearances.md),
[starts](metric-definitions/starts.md), and
[minutes played](metric-definitions/minutes-played.md).

## Passing and circulation

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-PASS-ATTEMPTS | Pass attempts | How often did the player attempt an eligible recorded pass? | Count unique valid Pass events under versioned pass-type eligibility. | Eligible Pass events | None | Attempts | Total and per 90 | Proposed | `0.1.0` |
| MET-PASS-COMPLETED | Completed passes | How often did the player complete an eligible pass? | Count eligible Pass events with structurally valid Pass object and absent provider failure outcome. | Completed eligible passes | None | Passes | Total and per 90 | Proposed | `0.1.0` |
| MET-PASS-COMPLETION-RATE | Pass completion rate | What share of eligible attempts were completed? | \(100\times\text{completed}/\text{attempts}\); unavailable at zero attempts. | `MET-PASS-COMPLETED` | `MET-PASS-ATTEMPTS` | Percent | Opportunity rate; never per 90; raw numerator/denominator shown | Proposed | `0.1.0` |
| MET-PASS-FORWARD | Forward passes | How often did completed passing move the ball goalward? | Count eligible completed passes with normalized \(x_{end}-x_{start}>T_v\); threshold \(T_v\) is unresolved. | Completed passes satisfying forward rule | None | Passes | Total and per 90 | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-PASS-ATTEMPTS` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-PASS-TYPE-ID` → `FEAT-PASS-ATTEMPT` | Direct aggregation with ScoutLabs eligibility | Position-compatible; goalkeeper distribution split from outfield use | No validated minimum; show minutes and attempts | Not quantified; pass eligibility has not been calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO` | Set pieces, clearances, and provider pass types affect meaning | Dossier §7; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-PASS-001`, `EXP-THRESH-001` | None |
| `MET-PASS-COMPLETED` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-PASS-TYPE-ID`, `SRC-PASS-OUTCOME-ID` → `FEAT-PASS-COMPLETED` | Direct aggregation of provider outcome convention | Position-compatible; same pass-eligibility version | No validated minimum | Not quantified; outcome vocabulary audit pending | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO` | Outcome absence is schema semantics; volume reflects role/team possession | Dossier §§7.1, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-PASS-001`, `EXP-THRESH-001` | None |
| `MET-PASS-COMPLETION-RATE` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-PASS-TYPE-ID`, `SRC-PASS-OUTCOME-ID` → `FEAT-PASS-ATTEMPT`, `FEAT-PASS-COMPLETED`, `FEAT-PASS-COMPLETION-RATE` | ScoutLabs-derived rate from direct counts | Position-compatible; identical eligibility and minimum-attempt policy | Minimum attempts unresolved; numerator/denominator always shown | Not quantified; outcome/denominator audit pending | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO`; denominator-invariant test required | Conservative choices can inflate rate; not pass difficulty/value | Dossier §§6.2, 7.1, 24; R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-PASS-001`, `EXP-THRESH-001`, `EXP-SHRINK-001` | None |
| `MET-PASS-FORWARD` | `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-PASS-LENGTH`, `SRC-PASS-ANGLE` → `FEAT-PASS-COMPLETED`, `FEAT-FORWARD-PASS` | ScoutLabs-derived geometry | Position-compatible; same direction and threshold version | No validated minimum | Not quantified; geometry/threshold not applied | `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-INCOMPLETE-VIDEO` | Tiny positive x-change can be narratively misleading; no rule selected | Dossier §7.2 and §24; R9 | Player Profile, Player Explorer, Compare, internal research | `EXP-PROG-001`, `EXP-REDUND-001` | None |

Detailed definitions:
[completed passes](metric-definitions/completed-passes.md) and
[pass completion rate](metric-definitions/pass-completion-rate.md).

## Ball progression

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-PROG-PASSES | Progressive passes | How often did completed passing materially reduce distance to goal? | Count completed passes with \(d(start,goal)-d(end,goal)\ge T_v(start,end)\); competing threshold rules remain open. | Passes satisfying versioned progression rule | None | Passes | Total and per 90 | Proposed | `0.1.0` |
| MET-PROG-CARRIES | Progressive carries | How often did recorded carrying materially reduce distance to goal? | Count carries satisfying the versioned progression rule; no default rule selected. | Carries satisfying versioned progression rule | None | Carries | Total and per 90 | Proposed | `0.1.0` |
| MET-PROG-FINAL-THIRD-ENTRIES | Final-third entries | How often did a pass or carry enter the attacking third from outside? | Count completed passes/carries with \(x_{start}<80\) and \(x_{end}\ge80\) on normalized 120×80 coordinates. | Outside-to-inside eligible actions | None | Entries | Total, pass/carry split, and per 90 | Proposed | `0.1.0` |
| MET-PROG-PENALTY-AREA-ENTRIES | Penalty-area entries | How often did a pass or carry enter the opponent box from outside? | Count eligible actions where start is outside and end satisfies \(x\ge102,18\le y\le62\). | Outside-to-inside eligible actions | None | Entries | Total, pass/carry split, and per 90 | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-PROG-PASSES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-PASS-TYPE-ID`, `SRC-PASS-LENGTH`, `SRC-PASS-ANGLE` → `FEAT-PASS-X-PROGRESSION`, `FEAT-PROGRESSIVE-PASS` | ScoutLabs-derived geometry | Position-compatible; common rule/pitch/eligibility version | No threshold validated; show completed passes and minutes | Not quantified; competing definitions not executed | `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-INCOMPLETE-VIDEO` | Not provider-supplied; not line breaking; sensitive to starting zone | Dossier §§7.3, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-PROG-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |
| `MET-PROG-CARRIES` | `SRC-EVENT-BASE-LOCATION`, `SRC-CARRY-END-LOCATION` → `FEAT-CARRY-X-PROGRESSION`, `FEAT-PROGRESSIVE-CARRY` | ScoutLabs-derived geometry | Position-compatible; common rule/pitch version | No threshold validated; show carries and minutes | Not quantified; competing definitions not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-INCOMPLETE-VIDEO` | Provider carries are event segments, not trajectories; not dribbles | Dossier §§8.1, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-PROG-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |
| `MET-PROG-FINAL-THIRD-ENTRIES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-CARRY-END-LOCATION` → `FEAT-FINAL-THIRD-ENTRY` | ScoutLabs-derived fixed-zone transition | Position-compatible; common zone/action eligibility | No threshold validated; show eligible actions/minutes | Not quantified; entry calculation not executed | `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-INCOMPLETE-VIDEO` | Action endpoint is not guaranteed next touch/retention | Dossier §§7.5, 8.2, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-ENTRY-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |
| `MET-PROG-PENALTY-AREA-ENTRIES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-CARRY-END-LOCATION` → `FEAT-PENALTY-AREA-ENTRY` | ScoutLabs-derived fixed-zone transition | Position-compatible, high relevance to attacking roles; common zone version | No threshold validated; sparse for some positions | Not quantified; entry calculation not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-INCOMPLETE-VIDEO` | Fixed box geometry does not imply a chance or receiver control | Dossier §§7.5, 8.2, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-ENTRY-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |

Detailed definitions: [progressive passes](metric-definitions/progressive-passes.md),
[progressive carries](metric-definitions/progressive-carries.md),
[final-third entries](metric-definitions/final-third-entries.md), and
[penalty-area entries](metric-definitions/penalty-area-entries.md).

## Chance creation

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-CREATE-SHOT-ASSISTS | Shot assists | How often did a qualifying pass directly set up a teammate shot? | Count unique Pass events with shot-assist or goal-assist flag whose evidence resolves to a same-team Shot under versioned link reconciliation. | Resolved qualifying passes | None | Shot assists | Total and per 90 | Proposed | `0.1.0` |
| MET-CREATE-DERIVED-XA | Derived expected assists | What pre-shot xG was attached to shots directly created by qualifying passes? | Sum `shot.statsbomb_xg` over unique resolved shots linked to qualifying shot-assisting passes. | Sum of provider xG | None | Expected goals as derived xA | Total and per 90; retain xG/link version | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-CREATE-SHOT-ASSISTS` | `SRC-EVENT-BASE-ID`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-RELATED-EVENTS`, `SRC-PASS-SHOT-ASSIST`, `SRC-PASS-GOAL-ASSIST`, `SRC-PASS-ASSISTED-SHOT-ID`, `SRC-SHOT-KEY-PASS-ID` → `FEAT-SHOT-ASSIST` | Direct provider flags plus ScoutLabs link reconciliation | Position-compatible; most relevant to creative roles, still available to all | No validated minimum; show minutes and resolved-link count | Not quantified; link/flag reconciliation not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-UNRESOLVED`, `DQ-PASS-SHOT-LINK` | Final-pass-only; provider tagging and team shot volume matter | Dossier §§7.7, 10, 24; R5, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-XA-001`, `EXP-THRESH-001` | None |
| `MET-CREATE-DERIVED-XA` | `SRC-EVENT-BASE-ID`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-RELATED-EVENTS`, `SRC-PASS-SHOT-ASSIST`, `SRC-PASS-GOAL-ASSIST`, `SRC-PASS-ASSISTED-SHOT-ID`, `SRC-SHOT-KEY-PASS-ID`, `SRC-SHOT-XG`, `SRC-SHOT-TYPE-ID`, `SRC-SHOT-OUTCOME-ID` → `FEAT-SHOT-ASSIST`, `FEAT-DERIVED-XA`, `FEAT-SHOT-XG` | ScoutLabs-derived link aggregation of provider xG | Position-compatible; common link and provider-xG version | No validated minimum; show shot assists, linked shots, minutes, coverage | Not quantified; derived xA not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-UNRESOLVED`, `DQ-PASS-SHOT-LINK`, `DQ-PROVIDER-VERSION`, `DQ-INCOMPLETE-VIDEO` | Not provider xA; inherits provider xG and credits only final pass | Dossier §§7.7, 10, 24; R5 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-XA-001`, `EXP-THRESH-001`, `EXP-SHRINK-001` | None |

Detailed definitions:
[shot assists](metric-definitions/shot-assists.md) and
[derived expected assists](metric-definitions/derived-expected-assists.md).

## Carrying and dribbling

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-CARRY-CARRIES | Carries | How often was the player recorded moving with the ball between event points? | Count unique valid Carry events. | Carry events | None | Carries | Total and per 90 | Proposed | `0.1.0` |
| MET-CARRY-DRIBBLE-ATTEMPTS | Dribble attempts | How often did the player attempt to beat an opponent in recorded events? | Count unique valid Dribble events regardless of outcome. | Dribble events | None | Attempts | Total and per 90 | Proposed | `0.1.0` |
| MET-CARRY-DRIBBLE-SUCCESS-RATE | Dribble success rate | What share of recorded Dribble attempts had the audited successful outcome? | \(100\times\text{successful dribbles}/\text{dribble attempts}\). | Successful-outcome Dribbles | Valid Dribble attempts | Percent | Opportunity rate; never per 90 | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-CARRY-CARRIES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-CARRY-END-LOCATION` → `FEAT-CARRY` | Direct event count | Position-compatible; role and team possession materially affect volume | No validated minimum | Not quantified; carry metric not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO` | Provider event segments are not continuous trajectories or Dribbles | Dossier §8; R2 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-THRESH-001`, `EXP-REDUND-001` | None |
| `MET-CARRY-DRIBBLE-ATTEMPTS` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-DRIBBLE-OUTCOME-ID` → `FEAT-DRIBBLE-ATTEMPT` | Direct event count | Position-compatible; especially opportunity-sensitive by role | No validated minimum; show minutes/attempts | Not quantified; dribble metric not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO` | Dribble is an opponent-beating attempt, not all ball movement | Dossier §§8, 24; R2 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-LOSS-001`, `EXP-THRESH-001` | None |
| `MET-CARRY-DRIBBLE-SUCCESS-RATE` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-DRIBBLE-OUTCOME-ID` → `FEAT-DRIBBLE-ATTEMPT`, `FEAT-DRIBBLE-SUCCESS` | ScoutLabs-derived rate from provider outcome | Position-compatible; identical outcome and denominator version | Minimum attempts unresolved; show numerator/denominator | Not quantified; outcome vocabulary not applied | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO`; outcome-domain validation required | Small samples; outcome does not measure downstream retention/value | Dossier §§6.2, 8.3, 24; R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-LOSS-001`, `EXP-THRESH-001`, `EXP-SHRINK-001` | None |

## Shooting and goal threat

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-SHOOT-NON-PENALTY-SHOTS | Non-penalty shots | How often did the player shoot outside penalties and shootouts? | Count Shot events where canonical shot type is not Penalty and period is not 5. | Eligible Shot events | None | Shots | Total and per 90 | Proposed | `0.1.0` |
| MET-SHOOT-NON-PENALTY-XG | Non-penalty xG | What aggregate provider pre-shot xG did those shots carry? | Sum `shot.statsbomb_xg` over `MET-SHOOT-NON-PENALTY-SHOTS`. | Sum of provider xG | None | Expected goals | Total and per 90; provider version retained | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-SHOOT-NON-PENALTY-SHOTS` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-PERIOD`, `SRC-SHOT-TYPE-ID`, `SRC-SHOT-OUTCOME-ID` → `FEAT-SHOT`, `FEAT-NON-PENALTY-SHOT` | Direct aggregation with explicit exclusions | Position-compatible; goalkeeper/outfield separation; attacking relevance varies | No validated minimum; show minutes/shots | Not quantified; shot exclusion metric not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO` | Volume reflects role and team chances; no shot quality | Dossier §9; R2 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-THRESH-001`, `EXP-SHRINK-001` | None |
| `MET-SHOOT-NON-PENALTY-XG` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-PERIOD`, `SRC-SHOT-TYPE-ID`, `SRC-SHOT-OUTCOME-ID`, `SRC-SHOT-XG` → `FEAT-NON-PENALTY-SHOT`, `FEAT-SHOT-XG`, `FEAT-NON-PENALTY-XG` | Direct aggregation of provider value | Position-compatible; common provider version/coverage | No validated minimum; show shots, minutes, xG coverage | Not quantified; npxG not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-SHOOTOUT`, `DQ-PROVIDER-VERSION`, `DQ-INCOMPLETE-VIDEO` | Inherits xG calibration; mixes volume and chance quality | Dossier §9; R2 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-THRESH-001`, `EXP-SHRINK-001`, `EXP-REDUND-001` | None |

Detailed definitions:
[non-penalty shots](metric-definitions/non-penalty-shots.md) and
[non-penalty xG](metric-definitions/non-penalty-xg.md).

## Possession security and losses

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-LOSS-BALL-LOSSES | On-ball losses | How often was an eligible player action followed by a version-defined loss attributable to that player? | Count the union of selected Dispossessed, Miscontrol, incomplete Dribble, failed-pass, and possession-ending cases under taxonomy \(v\), deduplicated by action/sequence. No taxonomy is selected. | Versioned attributable loss events | None for count; optional per on-ball actions is separate | Losses | Total, per 90, and experimental per 100 eligible on-ball actions | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-LOSS-BALL-LOSSES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-DRIBBLE-OUTCOME-ID`, `SRC-PASS-OUTCOME-ID`, `SRC-EVENT-POSSESSION`, `SRC-EVENT-RELATED-EVENTS` → `FEAT-BALL-LOSS` | ScoutLabs-derived event/sequence taxonomy | Position-compatible; use action-opportunity context; goalkeeper distribution may need separate splits | Minimum minutes/actions unresolved | Not quantified; candidate taxonomy not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-UNRESOLVED`, `DQ-INCOMPLETE-VIDEO` | Attribution and retention window are contested; risk/opportunity affects volume | Dossier §§8.4, 24; R9 | Player Profile, Player Explorer, Compare, internal research | `EXP-LOSS-001`, `EXP-THRESH-001`, `EXP-REDUND-001` | None |

## Defending

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-DEF-BALL-RECOVERIES | Ball recoveries | How often was a recorded recovery not explicitly marked failed? | Count Ball Recovery events where `recovery_failure` is not true, subject to audited absence semantics. | Successful recorded recoveries | None | Recoveries | Total and per 90 | Proposed | `0.1.0` |
| MET-DEF-INTERCEPTIONS | Interceptions | How often did the player record qualifying interception evidence? | Count unique evidence under a versioned taxonomy comparing all Interception events, successful outcomes only, and a deduplicated provider-complete variant including Pass type Interception. No default selected. | Qualifying deduplicated interception evidence | None | Interceptions | Total and per 90 | Proposed | `0.1.0` |
| MET-DEF-ACTION-HEIGHT | Defensive-action height | Where, goalward, did the player’s selected recorded defensive actions occur? | Median normalized x of a versioned set of pressures, recoveries, interceptions, duel/tackle, block, and clearance locations. | Sum is not used; ordered eligible x locations | Eligible located defensive actions | StatsBomb x-coordinate (median) | Median; optional zone shares, never per 90 | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-DEF-BALL-RECOVERIES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-BALL-RECOVERY-FAILURE`, `SRC-EVENT-BASE-COUNTERPRESS`, `SRC-EVENT-POSSESSION` → `FEAT-BALL-RECOVERY` | Direct event aggregation with ScoutLabs success convention | Position-compatible; contextual opportunity differs greatly | No validated minimum; show attempts/successes/minutes | Not quantified; recovery semantics not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO` | Not every regain; immediate retention not guaranteed | Dossier §§11.2–11.4; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-DEF-001`, `EXP-THRESH-001`, `EXP-REDUND-001` | None |
| `MET-DEF-INTERCEPTIONS` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-INTERCEPTION-OUTCOME-ID`, `SRC-PASS-TYPE-ID`, `SRC-EVENT-POSSESSION` → `FEAT-INTERCEPTION` | ScoutLabs-derived provider-event taxonomy | Position-compatible; taxonomy, outcome, representation, and opportunity context shown | No validated minimum; show source/outcome counts and minutes | Not quantified; taxonomy/deduplication not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-ASYMMETRIC`, `DQ-INCOMPLETE-VIDEO` | No default attempt/success mapping; recorded evidence is not complete anticipation | Dossier §§11.2–11.4, 24; R2, R9 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-DEF-001`, `EXP-THRESH-001`, `EXP-REDUND-001` | None |
| `MET-DEF-ACTION-HEIGHT` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-DUEL-TYPE-ID`, `SRC-DUEL-OUTCOME-ID`, `SRC-BALL-RECOVERY-FAILURE`, `SRC-INTERCEPTION-OUTCOME-ID` → `FEAT-ACTION-ZONE`, `FEAT-DEFENSIVE-ACTION-HEIGHT` | ScoutLabs-derived spatial summary | Position-compatible; action-family mix and team context must match or be exposed | Minimum located actions unresolved | Not quantified; taxonomy and spatial aggregate not executed | `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE` | Event centroid is not average defensive position; family mix can move median | Dossier §§11.3, 13.7; R2, R10 | Player Profile, Compare, action maps, Similar Players research | `EXP-DEF-001`, `EXP-SPATIAL-001`, `EXP-THRESH-001` | None |

Detailed definitions:
[ball recoveries](metric-definitions/ball-recoveries.md) and
[interceptions](metric-definitions/interceptions.md).

## Pressing and counterpressing

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-PRESS-PRESSURES | Pressures | How often did the player record a provider Pressure event? | Count unique valid player-attributed Pressure events. | Pressure events | None | Recorded pressures | Total and per 90 | Proposed | `0.1.0` |
| MET-PRESS-COUNTERPRESS-ACTIONS | Counterpress actions | How often did the player record an action explicitly tagged `counterpress: true`? | Count unique player-attributed events with the provider flag true across audited eligible event types. | Tagged events | None | Tagged actions | Total and per 90 | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-PRESS-PRESSURES` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-EVENT-BASE-DURATION`, `SRC-EVENT-BASE-UNDER-PRESSURE`, `SRC-EVENT-BASE-COUNTERPRESS` → `FEAT-PRESSURE` | Direct provider event count | Position-compatible; team-possession/opponent context visible | No validated minimum | Not quantified; pressure metric not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-INCOMPLETE-VIDEO` | Event proxy, not tracking pressure or success | Dossier §11.1; R7, R10 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-DEF-001`, `EXP-THRESH-001`, `EXP-REDUND-001` | None |
| `MET-PRESS-COUNTERPRESS-ACTIONS` | `SRC-EVENT-BASE-COUNTERPRESS`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-EVENT-POSSESSION` → `FEAT-COUNTERPRESS` | Direct aggregation of provider flag | Position-compatible; show tagged event-type mix and team context | No validated minimum; potentially sparse | Not quantified; conditional flag metric not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-PROVIDER-VERSION`, `DQ-INCOMPLETE-VIDEO` | Missing flag is not proof of no real counterpress; overlaps Pressure | Dossier §§11.1, 24; R7, R10 | Player Profile, Player Explorer, Metric Leaders, Compare, Similar Players | `EXP-DEF-001`, `EXP-THRESH-001`, `EXP-REDUND-001` | None |

Detailed definitions: [pressures](metric-definitions/pressures.md) and
[counterpress actions](metric-definitions/counterpress-actions.md).

## Aerial activity

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-AERIAL-DUELS | Recorded aerial duels | How often did the player participate in an aerial contest represented by the event taxonomy? | Count deduplicated events mapped by taxonomy \(v\) from Duel type/outcome and corroborating provider aerial evidence; mapping unresolved. | Versioned aerial-contest records | None; an outcome rate would use eligible contests | Aerial duels | Total and per 90 | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-AERIAL-DUELS` | `SRC-DUEL-TYPE-ID`, `SRC-DUEL-OUTCOME-ID`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID` → `FEAT-AERIAL-DUEL` | ScoutLabs-derived taxonomy over provider events | Position-compatible; goalkeeper and outfield contexts separated | Minimum contests unresolved; numerator/denominator shown for any rate | Not quantified; cross-event aerial taxonomy not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-ASYMMETRIC` | Provider event families may represent winner/loser asymmetrically; double-count risk; other aerial-won qualifiers require explicit admission | Dossier §11.2; R9 | Player Profile, Player Explorer, Compare, internal research | `EXP-DEF-001`, `EXP-THRESH-001` | None |

## Possession value

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-VALUE-XT-GAIN | xT gain | How much model-estimated scoring threat did eligible ball-moving actions add? | Sum positive/optionally signed \(\text{xT}(end)-\text{xT}(start)\) over eligible completed passes/carries under a specific trained model; aggregation choice unresolved. | Model-dependent action-value deltas | None | Expected-threat units | Total and per 90; model and training population mandatory | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-VALUE-XT-GAIN` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-CARRY-END-LOCATION`, `SRC-EVENT-POSSESSION` → `FEAT-XT-ACTION-VALUE` | ScoutLabs model-derived; no model selected | Position-compatible and model/training-population compatible | Minimum minutes/actions and model calibration unresolved | Not quantified; no ScoutLabs xT model implemented/evaluated | `DQ-EVENT-INDEX-ORDER`, `DQ-POSSESSION-TEAM`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REPRODUCIBILITY` | Model/training/grid dependent; may duplicate direct progression; no production xT | Dossier §§10.2, 20; R4 | Internal research; potential future methodology/Profile only after admission | `EXP-XT-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |

## Spatial profile

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-SPATIAL-ACTION-ZONE-PROFILE | Action-zone profile | In which named pitch zones did a player record a selected action family? | Vector \(h_z=n_z/\sum_z n_z\) for valid direction-normalized action locations under grid/zone version \(v\). | Located eligible actions per zone | All located eligible actions in family | Vector of shares | L1-normalized within action family; raw counts retained | Researching | `0.1.0` |
| MET-SPATIAL-ZONE-TRANSITIONS | Zone-transition profile | Along which zone-to-zone routes did the player move the ball? | Matrix/vector \(T_{ij}=n_{ij}/\sum_{ij}n_{ij}\) for eligible completed passes/carries from zone \(i\) to \(j\). | Eligible actions per start/end-zone pair | All eligible located actions | Vector/matrix of shares | L1-normalized; pass/carry and raw counts retained | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-SPATIAL-ACTION-ZONE-PROFILE` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION` → `FEAT-ACTION-ZONE`, `FEAT-SPATIAL-HISTOGRAM` | ScoutLabs-derived spatial representation | Position- and action-family-compatible; same zone/grid version | Minimum located actions and stability unresolved | Not quantified; spatial profiles not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE` | Event activity map, not tracking occupation; sparse/boundary sensitive | Dossier §13; R2, R10 | Player Profile action maps, Compare, Similar Players research | `EXP-SPATIAL-001`, `EXP-THRESH-001` | None |
| `MET-SPATIAL-ZONE-TRANSITIONS` | `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-LOCATION`, `SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, `SRC-CARRY-END-LOCATION` → `FEAT-ACTION-ZONE`, `FEAT-ZONE-TRANSITION` | ScoutLabs-derived spatial representation | Position- and action-family-compatible; same zone and eligibility version | Minimum transitions and stability unresolved | Not quantified; transition vectors not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, `DQ-CONDITIONAL-FIELD` | Grid choice and sparse routes affect distance; not tactical movement between events | Dossier §§13.4, 13.6, 15.10; R2 | Player Profile route maps, Compare, Similar Players research | `EXP-SPATIAL-002`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |

## Sequence participation

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-SEQUENCE-POSSESSION-PARTICIPATION | Possession-sequence participation | In how many provider possession sequences did the player record an eligible action? | Count distinct match/team/possession keys containing at least one eligible player action; event eligibility version retained. | Unique eligible possessions with participation | None; team-possession share is a separate rate | Possessions | Total and per 90; optional share only with team-possession denominator | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-SEQUENCE-POSSESSION-PARTICIPATION` | `SRC-EVENT-POSSESSION`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-INDEX`, `SRC-EVENT-BASE-TIMESTAMP`, `SRC-EVENT-RELATED-EVENTS` → `FEAT-POSSESSION-PARTICIPATION` | ScoutLabs-derived grouping over provider possession IDs | Position-compatible; team possession volume and action eligibility visible | Minimum minutes/possessions unresolved | Not quantified; sequence feature not calculated | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-INDEX-ORDER`, `DQ-EVENT-TIMESTAMP-ORDER`, `DQ-POSSESSION-TEAM`, `DQ-INCOMPLETE-VIDEO` | An event in a possession is not causal contribution or off-ball participation | Dossier §§4.3, 10; R2, R10 | Player Profile, Compare, Similar Players research, internal research | `EXP-SEQUENCE-001`, `EXP-REDUND-001`, `EXP-THRESH-001` | None |

## 360 context

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-360-NEAREST-VISIBLE-OPPONENT | Nearest visible opponent distance | For usable event-linked frames, how far was the actor from the nearest visible opponent? | Per usable actor frame, \(\min_o d(actor,o)\); aggregate median with eligible/usable-frame coverage. | Ordered nearest-opponent distances | Usable frames for aggregation | StatsBomb pitch-coordinate distance | Median; event-type splits; never fill uncovered frames | Researching | `0.1.0` |
| MET-360-VISIBLE-NUMERICAL-BALANCE | Visible local numerical balance | In a fully visible local region, what was the visible teammate-minus-opponent count around the actor? | Per usable frame and radius \(r\), \(N_{teammate,r}-N_{opponent,r}\); aggregate mean/median under versioned visibility rule. | Sum/order of per-frame balance values | Usable frames | Visible-player count difference | Mean/median; eligible and usable frames shown | Researching | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-360-NEAREST-VISIBLE-OPPONENT` | `SRC-EVENT-BASE-ID`, `SRC-360-EVENT-UUID`, `SRC-360-FREEZE-FRAME-LOCATION`, `SRC-360-FREEZE-FRAME-TEAMMATE`, `SRC-360-FREEZE-FRAME-ACTOR`, `SRC-360-VISIBLE-AREA` → `FEAT-360-NEAREST-OPPONENT` | ScoutLabs-derived geometry on partial snapshots | Same event family and 360 competition/season coverage; position-compatible; not universal ranking | Minimum usable frames and visible-radius coverage unresolved | Not quantified at metric level; local 360 is partial and source report must be consulted | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-360-LINK-UNRESOLVED`, `DQ-360-ACTOR`, `DQ-360-COVERAGE`, `DQ-VISIBLE-AREA-POLYGON`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE` | Only visible players; event snapshot; no speed/orientation/identity for non-actor; selection bias | Dossier §14; R6, R10 | Selective Player Profile/Compare context and internal research; excluded from global similarity pending evidence | `EXP-360-001`, `EXP-360-002`, `EXP-SPATIAL-001` | None |
| `MET-360-VISIBLE-NUMERICAL-BALANCE` | `SRC-EVENT-BASE-ID`, `SRC-360-FREEZE-FRAME-LOCATION`, `SRC-360-FREEZE-FRAME-TEAMMATE`, `SRC-360-FREEZE-FRAME-ACTOR`, `SRC-360-VISIBLE-AREA` → `FEAT-360-NUMERICAL-BALANCE` | ScoutLabs-derived visible-player count | Same event family, radius, visibility, and covered population; position-compatible | Minimum usable frames and region visibility unresolved | Not quantified; feature not calculated and 360 coverage is partial | `DQ-360-LINK-UNRESOLVED`, `DQ-360-ACTOR`, `DQ-360-KEEPER-LABEL`, `DQ-360-COVERAGE`, `DQ-VISIBLE-AREA-POLYGON`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE` | Visible balance is not complete team numerical superiority; radius/occlusion sensitive | Dossier §14; R6, R10 | Selective context panels and internal research; not universal ranking | `EXP-360-001`, `EXP-360-002` | None |

## Goalkeeping

### Definition

| Metric ID | Name | Football question | Definition and conceptual formula | Numerator | Denominator | Unit | Normalization | Status | Version |
|---|---|---|---|---|---|---|---|---|---|
| MET-GK-XG-FACED | Goalkeeper xG faced | What provider pre-shot chance quality was carried by shots reliably linked to the goalkeeper? | Sum `shot.statsbomb_xg` over unique eligible opponent shots linked to audited goalkeeper shot-facing actions. | Sum of provider xG over linked shots | None; per-shot context uses eligible linked-shot count | Expected goals faced | Total, per 90, per-shot context, penalty/non-penalty splits | Proposed | `0.1.0` |

### Lineage and admission

| Metric ID | Source IDs → feature IDs | Origin | Comparison group and positional relevance | Required sample | Observed data coverage | Quality dependencies | Known limitations | Research support | Product surfaces | Experiments | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MET-GK-XG-FACED` | `SRC-EVENT-BASE-ID`, `SRC-EVENT-RELATED-EVENTS`, `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-PERIOD`, `SRC-SHOT-XG`, `SRC-SHOT-TYPE-ID`, `SRC-SHOT-OUTCOME-ID`, `SRC-GK-TYPE-ID`, `SRC-GK-OUTCOME-ID` → `FEAT-GK-SHOT-FACED`, `FEAT-GK-XG-FACED`, `FEAT-MINUTES` | ScoutLabs link aggregation of provider pre-shot xG | Goalkeeper-only; same taxonomy/provider version/minutes/shots/link coverage | Minimum minutes and shots faced unresolved | Not quantified; GK taxonomy/link aggregation not executed | `DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`, `DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-REL-UNRESOLVED`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO`, `DQ-PROVIDER-VERSION`, `DQ-SHOT-GK-LINK`, `DQ-STARTING-XI-CONSISTENCY`, `DQ-SUBSTITUTION-CONSISTENCY`, `DQ-PLAYER-ON-OFF`, `DQ-PERIOD-BOUNDARY`, `DQ-STOPPAGE-TIME`, `DQ-EXTRA-TIME`, `DQ-DISMISSAL` | Not post-shot xG/goals prevented; team defence and finishing affect context | Dossier §12; R8, R10 | Goalkeeper Player Profile, Player Explorer, Compare, Similar Players research | `EXP-GK-001`, `EXP-THRESH-001`, `EXP-GK-002` | None |

Detailed definition:
[goalkeeper xG faced](metric-definitions/goalkeeper-xg-faced.md).

## Admission summary

| Measure | Count |
|---|---:|
| Candidate Metric IDs | 32 |
| Proposed | 22 |
| Researching | 10 |
| Experimentally supported | 0 |
| Validated | 0 |
| Approved for MVP | 0 |
| Rejected | 0 |
| Deprecated | 0 |
| Individual foundational definition files | 18 |
| Metrics with quantified player-level observed coverage | 0 |

The counts above describe documentation state only. They are not data-coverage
or implementation results. Proposed status means the candidate has a
responsible initial definition; it does not mean product admission. Researching
status marks an unresolved taxonomy, formula, model, sample rule, or coverage
dependency.

## Contested alternatives and next gates

| Topic | Alternatives retained | Required evidence |
|---|---|---|
| Minutes | Actual event endpoints and state transitions; dismissal/Player Off precedence; partial-match policy | `EXP-MIN-001`, known-match fixtures, interval invariants |
| Pass completion | Outcome absence; special-type exclusions; unknown/injury-clearance handling | `EXP-PASS-001`, observed vocabulary and denominator reconciliation |
| Progression | 30/15/10-metre goal-distance reduction; fixed x-gain; zone advance; xT gain | `EXP-PROG-001`, coordinate conversion, stability, redundancy, expert review |
| Zone entries | Action endpoint versus next-teammate-touch/short retention | `EXP-ENTRY-001`, boundary/link/sequence fixtures |
| Shot assists/xA | Flag-first, link-first, or reconciled union; unusual shot chains | `EXP-XA-001`, bidirectional link audit and xG coverage |
| Losses | Narrow Dispossessed/Miscontrol versus broader action/possession taxonomy | `EXP-LOSS-001`, deduplication and attribution review |
| Defensive opportunity | Per 90, opponent possessions, opponent actions, estimated out-of-possession minutes | `EXP-DEF-001`, stability and interpretability |
| Similarity inputs | Scaling, redundancy, weights, missingness, minute thresholds | `EXP-SCALE-001`, `EXP-REDUND-001`, `EXP-MISS-001`, `EXP-THRESH-001` |
| Spatial profiles | Tactical zones, fixed grids, histograms, zone transitions | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` |
| 360 context | Usable-frame/visible-region rules, radius, coverage penalties | `EXP-360-001`, `EXP-360-002` |
| Goalkeeping | Shot-facing type/outcome taxonomy, link-first versus on-pitch reconciliation, penalty treatment | `EXP-GK-001`, `EXP-GK-002` |

No contested alternative becomes a default by appearing in this catalogue.
