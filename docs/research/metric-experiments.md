# Metric experiment registry

**Registry version:** 1.0
**Execution state:** protocol backlog only
**Evidence foundation:** [Research dossier](research-dossier.md)
**Governance:** [Research methodology](research-methodology.md)

Every experiment below has status `Planned`. No experiment has been executed, no result
is reported, and no metric or model admission decision follows from this registry.
Dataset subsets always mean the versioned local StatsBomb Open Data snapshot after the
listed data-quality exclusions; generated artifacts must remain under ignored
`reports/`.

## Authoritative experiment IDs

| Experiment ID | Title | Status |
|---|---|---|
| EXP-MIN-001 | Playing-time reconstruction | Planned |
| EXP-PASS-001 | Pass-completion semantics | Planned |
| EXP-PROG-001 | Progressive-action definitions | Planned |
| EXP-ENTRY-001 | Final-third and penalty-area entries | Planned |
| EXP-XA-001 | Linked-shot expected assists | Planned |
| EXP-LOSS-001 | On-ball loss taxonomy | Planned |
| EXP-SEQUENCE-001 | Possession-sequence participation | Planned |
| EXP-DEF-001 | Defensive-action and opportunity taxonomy | Planned |
| EXP-GK-001 | Goalkeeper event and shots-faced taxonomy | Planned |
| EXP-SCALE-001 | Scaling and comparison-population normalization | Planned |
| EXP-DIST-001 | Distance-family comparison | Planned |
| EXP-REDUND-001 | Feature redundancy and ablation | Planned |
| EXP-MISS-001 | Missing values and coverage penalties | Planned |
| EXP-SIM-001 | End-to-end transparent retrieval baseline | Planned |
| EXP-THRESH-001 | Minute and opportunity thresholds | Planned |
| EXP-SHRINK-001 | Shrinkage and visible reliability treatment | Planned |
| EXP-SIM-002 | Same-player seasons, stability, and negative controls | Planned |
| EXP-SIM-003 | Structured expert and case-study review | Planned |
| EXP-XT-001 | Expected Threat reproduction and quality | Planned |
| EXP-VAEP-001 | SPADL/VAEP reproduction and ablation | Planned |
| EXP-SPATIAL-001 | Spatial representation and distance | Planned |
| EXP-SPATIAL-002 | Zone-transition vectors | Planned |
| EXP-360-001 | Coverage and usable-frame criteria | Planned |
| EXP-360-002 | Context-feature hypotheses | Planned |
| EXP-GK-002 | Goalkeeper-specific retrieval | Planned |

## Priority index

| Priority | Experiments | Decision area |
|---:|---|---|
| 1 | `EXP-MIN-001`, `EXP-PASS-001`, `EXP-PROG-001`, `EXP-ENTRY-001`, `EXP-XA-001`, `EXP-LOSS-001`, `EXP-SEQUENCE-001`, `EXP-DEF-001`, `EXP-GK-001` | Data and metric admission |
| 2 | `EXP-SCALE-001`, `EXP-DIST-001`, `EXP-REDUND-001`, `EXP-MISS-001`, `EXP-SIM-001` | Baseline normalization and retrieval |
| 3 | `EXP-THRESH-001`, `EXP-SHRINK-001` | Sample reliability |
| 4 | `EXP-SIM-002`, `EXP-SIM-003` | Football validity |
| 5 | `EXP-XT-001`, `EXP-VAEP-001` | Possession value |
| 6 | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` | Spatial similarity |
| 7 | `EXP-360-001`, `EXP-360-002` | Event-linked 360 context |
| 8 | `EXP-GK-002` | Goalkeeper similarity |

## Priority 1 — Data and metric admission

### EXP-MIN-001 — Playing-time reconstruction

- **Research question:** `RQ-MIN-001`: which event and lineup evidence supports
  reproducible appearances, starts, playing seconds, and minutes by position?
- **Hypothesis:** a period-aware state machine using Starting XI, substitutions, Player
  On, Player Off, dismissals, and actual period ends can reconstruct defensible exposure
  while flagging incomplete evidence.
- **Metric, feature, or model:** `FEAT-APPEARANCE`, `FEAT-START`, `FEAT-MINUTES`,
  `FEAT-MINUTES-BY-POSITION`; `MET-AVAIL-APPEARANCES`, `MET-AVAIL-STARTS`,
  `MET-AVAIL-MINUTES`.
- **Competing definitions:** fixed 90-minute assumption; match-period endpoints;
  event-state reconstruction; lineup-plus-event hybrid.
- **Source fields:** `matches[].match_id`, `lineups[].lineup[].player_id`,
  `events[].period`, `events[].timestamp`, `events[].duration`,
  `events[].type.name`, `events[].player.id`, `events[].substitution.replacement.id`,
  `events[].tactics.lineup[]`.
- **Dataset subset:** all valid matches with readable lineup and event files, stratified
  by regulation, extra time, shootout, substitution, dismissal, and incomplete-video
  evidence.
- **Candidate population:** every player named in a lineup or player-change event.
- **Sample rules:** exclude shootout time; retain extra time; keep inconsistent matches
  as flagged audit cases rather than silently imputing them.
- **Method:** implement alternative state reconstructions in an isolated audit, compare
  player totals and manually inspect a preregistered edge-case sample.
- **Baseline:** fixed 90 minutes for starters, substitution timestamp arithmetic, no
  extra-time or interruption handling.
- **Evaluation criteria:** no negative/overlapping intervals; team on-pitch counts are
  explainable; edge cases are flagged; repeated runs are identical; manual cases agree
  with source evidence.
- **Expected output:** interval-level discrepancy table, edge-case taxonomy, proposed
  playing-time algorithm version, and unresolved-case rate.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare, quality reporting.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No decision; the minutes algorithm and metric admission remain pending.
- **Follow-up:** complete `VAL-LINEUP-001` and the minutes-specific edge-case audit before
  any exposure-normalized metric is validated.

### EXP-PASS-001 — Pass-completion semantics

- **Research question:** `RQ-PASS-001`: which outcomes and exceptional pass types belong
  in attempts, completions, failures, or exclusions?
- **Hypothesis:** an explicit StatsBomb-outcome mapping will be more reproducible and
  interpretable than assuming all missing outcomes are equivalent without auditing
  special cases.
- **Metric, feature, or model:** `FEAT-PASS-ATTEMPT`, `FEAT-PASS-COMPLETED`,
  `FEAT-PASS-COMPLETION-RATE`; `MET-PASS-ATTEMPTS`, `MET-PASS-COMPLETED`,
  `MET-PASS-COMPLETION-RATE`.
- **Competing definitions:** absence of a failure outcome; next teammate touch; exclusion
  of clearances, offside, injury clearances, or unknown outcomes.
- **Source fields:** `events[].type.name`, `events[].pass.outcome.name`,
  `events[].pass.type.name`, `events[].pass.recipient.id`,
  `events[].related_events[]`, `events[].possession`, `events[].team.id`.
- **Dataset subset:** every observed Pass event, stratified by outcome, type, set play,
  cross, and competition-season.
- **Candidate population:** outfield players and goalkeepers with at least one eligible
  pass.
- **Sample rules:** report numerator and denominator; do not coerce unknown/missing
  evidence to success; audit rare outcomes separately.
- **Method:** enumerate outcome/type combinations, implement competing denominators, and
  measure player-level rate and rank changes.
- **Baseline:** completion inferred only from absent `pass.outcome`.
- **Evaluation criteria:** exhaustive outcome mapping; no unclassified observed outcome;
  stable totals; interpretable denominator; sensitivity reported by position and sample.
- **Expected output:** versioned pass-attempt/completion taxonomy and comparison table.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No decision; pass metrics remain `Proposed`.
- **Follow-up:** admit one default only after field coverage and rare-outcome review.

### EXP-PROG-001 — Progressive-action definitions

- **Research question:** `RQ-PROG-001`: which transparent geometric rule best supports
  progressive pass and carry comparison?
- **Hypothesis:** a versioned goal-distance or x-progression rule will be more stable and
  explainable than treating xT gain as synonymous with progression.
- **Metric, feature, or model:** `FEAT-PASS-X-PROGRESSION`,
  `FEAT-PROGRESSIVE-PASS`, `FEAT-CARRY-X-PROGRESSION`,
  `FEAT-PROGRESSIVE-CARRY`; `MET-PROG-PASSES`, `MET-PROG-CARRIES`.
- **Competing definitions:** Wyscout-style 30/15/10 goal-distance reduction; fixed
  positive x threshold; start/end tactical-zone advance; positive xT gain.
- **Source fields:** `events[].location`, `events[].pass.end_location`,
  `events[].carry.end_location`, `events[].pass.outcome.name`, `events[].type.name`.
- **Dataset subset:** completed passes and carries with valid two-dimensional start/end
  coordinates after attacking-direction normalization.
- **Candidate population:** eligible player-team-season profiles within position groups.
- **Sample rules:** exclude invalid coordinate shapes and unresolved direction; report
  attempts and qualifying actions; test minimum action denominators.
- **Method:** calculate every definition on the same actions; compare prevalence,
  player ranks, feature correlations, and preregistered action examples.
- **Baseline:** fixed positive x-distance with a declared minimum.
- **Evaluation criteria:** deterministic classification; interpretable edge cases;
  stable ranking under match resampling; controlled redundancy with zone entries/xT.
- **Expected output:** action-level disagreement matrix and recommendation for a
  versioned default or a documented unresolved decision.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare, action maps.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No definition selected.
- **Follow-up:** route xT-based alternatives to `EXP-XT-001` and test admitted definition
  under `EXP-THRESH-001`.

### EXP-ENTRY-001 — Final-third and penalty-area entries

- **Research question:** `RQ-PROG-001`: which outside-to-inside rule consistently
  identifies passes and carries entering advanced zones?
- **Hypothesis:** direction-normalized outside-to-inside geometry yields an explainable
  metric with less ambiguity than counting every action ending inside the zone.
- **Metric, feature, or model:** `FEAT-FINAL-THIRD-ENTRY`,
  `FEAT-PENALTY-AREA-ENTRY`; `MET-PROG-FINAL-THIRD-ENTRIES`,
  `MET-PROG-PENALTY-AREA-ENTRIES`.
- **Competing definitions:** endpoint inside; origin outside and endpoint inside; origin
  outside and next teammate touch inside; action-type-specific entry rules.
- **Source fields:** `events[].location`, `events[].pass.end_location`,
  `events[].carry.end_location`, `events[].pass.outcome.name`,
  `events[].related_events[]`, `events[].possession`.
- **Dataset subset:** valid passes and carries with start/end coordinates.
- **Candidate population:** eligible player-team-season profiles, reported separately
  for passes and carries before any combined total.
- **Sample rules:** normalized 120-by-80 coordinates; explicit boundary inclusivity;
  invalid shapes excluded and counted.
- **Method:** compare definitions action by action and inspect boundary, unsuccessful
  pass, and next-touch edge cases.
- **Baseline:** origin outside and successful action endpoint inside the named zone.
- **Evaluation criteria:** reproducible boundary handling; low unexplained disagreement;
  stable player ranks; labels remain specific to final-third or penalty-area entry.
- **Expected output:** versioned zone geometry, action examples, and pass/carry entry
  definitions.
- **Related product surfaces:** Player Profile, Similar Players, Metric Leaders,
  Compare, action maps.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No definition selected.
- **Follow-up:** use the selected zones consistently in `EXP-SPATIAL-001` and
  `EXP-SPATIAL-002`.

### EXP-XA-001 — Linked-shot expected assists

- **Research question:** `RQ-CREATE-001`: which provider links reliably identify the
  assisted shot whose StatsBomb xG can be attributed to the creator?
- **Hypothesis:** combining explicit shot-assist fields, assisted-shot IDs, key-pass IDs,
  and resolved related-event links will support a reproducible ScoutLabs-derived xA.
- **Metric, feature, or model:** `FEAT-SHOT-ASSIST`, `FEAT-DERIVED-XA`;
  `MET-CREATE-SHOT-ASSISTS`, `MET-CREATE-DERIVED-XA`.
- **Competing definitions:** provider `pass.shot_assist`; direct assisted-shot/key-pass
  identifier; resolved related event; final qualifying action in the possession.
- **Source fields:** `events[].id`, `events[].related_events[]`,
  `events[].pass.shot_assist`, `events[].pass.assisted_shot_id`,
  `events[].shot.key_pass_id`, `events[].shot.statsbomb_xg`,
  `events[].shot.outcome.name`.
- **Dataset subset:** all Pass and Shot events, including set plays, deflections,
  own-goal edge cases, and records with missing or conflicting links.
- **Candidate population:** players with at least one qualifying shot-assist link.
- **Sample rules:** only resolved, same-match event UUIDs; missing xG is not zero; report
  orphan, one-to-many, and conflicting links.
- **Method:** build each link path, reconcile them, manually review disagreements, and
  aggregate linked shot xG only after a canonical relationship rule is chosen.
- **Baseline:** sum `shot.statsbomb_xg` for shots directly referenced by an explicit
  pass-assisted-shot identifier.
- **Evaluation criteria:** high link resolution; no cross-match links; duplicate
  attribution prevented; edge-case policy documented; aggregates reproduce from source.
- **Expected output:** relationship audit, exclusion taxonomy, and versioned derived-xA
  definition with provider-xG provenance.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No xA metric admitted; it must not be described as provider-supplied.
- **Follow-up:** complete `VAL-REL-001` and source-field occurrence checks.

### EXP-LOSS-001 — On-ball loss taxonomy

- **Research question:** `RQ-LOSS-001`: which actions and sequence outcomes constitute
  an attributable ball loss?
- **Hypothesis:** a versioned taxonomy combining explicit failure events with bounded
  possession transitions is more interpretable than either Dispossessed-only counts or
  every possession-ending action.
- **Metric, feature, or model:** `FEAT-BALL-LOSS`;
  `MET-LOSS-BALL-LOSSES`.
- **Competing definitions:** Dispossessed only; Dispossessed plus Miscontrol and failed
  Dribble; all failed on-ball actions; loss within an N-event retention window;
  possession-ending failed action.
- **Source fields:** `events[].type.name`, `events[].possession`,
  `events[].possession_team.id`, `events[].team.id`,
  `events[].pass.outcome.name`, `events[].dribble.outcome.name`,
  `events[].related_events[]`.
- **Dataset subset:** all on-ball and possession-change events with valid ordering.
- **Candidate population:** players with eligible on-ball actions.
- **Sample rules:** own-team continuation is not a loss; missing sequence evidence is
  unknown, not retained; separately report explicit provider events and inferred losses.
- **Method:** construct action-level classifications under every definition, inspect
  sequence disagreements, and compare per-90 and per-100-on-ball-action rankings.
- **Baseline:** explicit Dispossessed, Miscontrol, and incomplete Dribble events only.
- **Evaluation criteria:** exclusive categories; reproducible attribution; sensible
  sequence examples; stable rates; denominator and inferred component remain visible.
- **Expected output:** loss taxonomy, attribution examples, and definition sensitivity.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No loss definition selected.
- **Follow-up:** test redundancy with progression and pass-risk features in
  `EXP-REDUND-001`.

### EXP-SEQUENCE-001 — Possession-sequence participation

- **Research question:** `RQ-SEQUENCE-001`: which bounded possession definition supports
  an interpretable participation feature without converting temporal proximity into
  causal credit?
- **Hypothesis:** provider possession IDs plus ordered event roles can support stable,
  named participation in shot-ending and advanced possessions when direct action and
  inferred sequence evidence remain separate.
- **Metric, feature, or model:** `FEAT-POSSESSION-PARTICIPATION`;
  `MET-SEQUENCE-POSSESSION-PARTICIPATION`.
- **Competing definitions:** any on-ball action in a provider possession; involvement in
  a shot-ending possession; final N actions before a shot; successful actions only;
  direct creator versus secondary/buildup participation.
- **Source fields:** `events[].id`, `events[].index`, `events[].period`,
  `events[].timestamp`, `events[].possession`, `events[].possession_team.id`,
  `events[].team.id`, `events[].player.id`, `events[].type.name`,
  `events[].related_events[]`, shot outcomes.
- **Dataset subset:** matches passing event-order, timestamp, possession-team, and
  relationship quality rules.
- **Candidate population:** players with validated minutes and at least one eligible
  on-ball event in a qualifying possession.
- **Sample rules:** no sequence crosses match or period boundaries; shootouts separated;
  missing/contradictory possession evidence is excluded and counted; causal language is
  prohibited.
- **Method:** compute competing possession and fixed-window definitions, compare
  action-level overlap, resample matches, and inspect preregistered shot-ending and
  turnover sequences.
- **Baseline:** share/count of provider possessions in which the player records at least
  one eligible on-ball event, with shot-ending participation reported separately.
- **Evaluation criteria:** deterministic membership; no cross-boundary sequences;
  interpretable role labels; acceptable match-resample stability; limited redundancy
  with direct activity volume.
- **Expected output:** versioned participation taxonomy, sequence examples, stability
  report, and explicit exclusions.
- **Related product surfaces:** Player Profile, Similar Players, Compare, methodology,
  internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No possession-participation definition selected.
- **Follow-up:** test redundancy in `EXP-REDUND-001` and football interpretation in
  `EXP-SIM-003`.

### EXP-DEF-001 — Defensive-action and opportunity taxonomy

- **Research question:** `RQ-DEF-001`: which recorded events and opportunity denominators
  support defensible defensive and pressing profiles?
- **Hypothesis:** explicit event-family metrics plus named spatial/opportunity context
  will be more stable and honest than an aggregate defensive-quality score.
- **Metric, feature, or model:** `FEAT-PRESSURE`, `FEAT-COUNTERPRESS`,
  `FEAT-BALL-RECOVERY`, `FEAT-INTERCEPTION`, `FEAT-DEFENSIVE-ACTION-HEIGHT`;
  `MET-PRESS-PRESSURES`, `MET-PRESS-COUNTERPRESS-ACTIONS`,
  `MET-DEF-BALL-RECOVERIES`, `MET-DEF-INTERCEPTIONS`,
  `MET-DEF-ACTION-HEIGHT`.
- **Competing definitions:** event counts per 90; per opponent possession; per opponent
  action; estimated out-of-possession exposure; alternative Duel/Tackle and aerial
  mappings.
- **Source fields:** `events[].type.name`, `events[].location`,
  `events[].counterpress`, `events[].duel.type.name`,
  `events[].duel.outcome.name`, `events[].interception.outcome.name`,
  `events[].ball_recovery.recovery_failure`, `events[].possession_team.id`.
- **Dataset subset:** every defensive, pressure, duel, aerial, and possession-context
  event with valid team/player evidence.
- **Candidate population:** position-compatible player-team-season profiles; goalkeepers
  separated where event meaning differs.
- **Sample rules:** record direct activity separately from opportunity adjustment;
  unrecorded defense is not zero defensive value; minimum event denominators tested.
- **Method:** audit event/subtype coverage; calculate competing denominators; compare
  rank, position effects, and stability; review selected event sequences.
- **Baseline:** raw event-family counts and per-90 rates.
- **Evaluation criteria:** exhaustive observed taxonomy; no tracking-grade claim;
  denominators are reproducible; adjustments improve stability without hiding context.
- **Expected output:** defensive taxonomy, denominator comparison, spatial-height
  definition, and explicit exclusions.
- **Related product surfaces:** Player Profile, Similar Players, Player Explorer,
  Metric Leaders, Compare, pressure/recovery maps.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No possession-adjusted formula or tackle/aerial composite selected.
- **Follow-up:** carry selected features into `EXP-SIM-001` only after quality review.

### EXP-GK-001 — Goalkeeper event and shots-faced taxonomy

- **Research question:** `RQ-GK-001`: which shot, goalkeeper, claim, sweeping, and
  distribution events form a reproducible goalkeeper profile?
- **Hypothesis:** resolved shot-to-goalkeeper relationships plus goalkeeper-specific
  denominators support a defensible pre-shot baseline, while post-shot claims remain
  unsupported.
- **Metric, feature, or model:** `FEAT-GK-SHOT-FACED`, `FEAT-GK-XG-FACED`;
  `MET-GK-XG-FACED` and candidate goalkeeper activity metrics.
- **Competing definitions:** shot-on-target outcome mapping; explicit goalkeeper-event
  link; team goalkeeper on pitch; pre-shot xG faced versus unavailable post-shot value.
- **Source fields:** `events[].id`, `events[].related_events[]`,
  `events[].shot.outcome.name`, `events[].shot.statsbomb_xg`,
  `events[].shot.type.name`, `events[].goalkeeper.type.name`,
  `events[].goalkeeper.outcome.name`, `events[].player.id`,
  `events[].position.name`.
- **Dataset subset:** all Shot and Goal Keeper events in matches with validated
  goalkeeper participation.
- **Candidate population:** goalkeeper-team-season profiles.
- **Sample rules:** penalty/non-penalty splits; unresolved links reported; own goals and
  missing xG handled explicitly; minimum shots-faced denominators tested later.
- **Method:** enumerate goalkeeper subtypes/outcomes, resolve shot relationships, inspect
  unmatched cases, and calculate direct activity and pre-shot xG-faced candidates.
- **Baseline:** shots faced and sum of linked StatsBomb pre-shot xG.
- **Evaluation criteria:** exhaustive observed taxonomy; reproducible one-to-one or
  documented one-to-many handling; no proprietary post-shot metric claim; stable samples.
- **Expected output:** goalkeeper taxonomy, link audit, denominator policy, and explicit
  unsupported fields/claims.
- **Related product surfaces:** goalkeeper Player Profile, Similar Players, Compare,
  Metric Leaders, goalkeeper maps.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No goalkeeper metric family validated.
- **Follow-up:** complete `VAL-REL-001`, `DQ-SHOT-GK-LINK` checks, then use admitted
  features in `EXP-GK-002`.

## Priority 2 — Baseline normalization and retrieval

### EXP-SCALE-001 — Scaling and comparison-population normalization

- **Research question:** `RQ-NORM-001`: which transformation preserves useful
  differences without letting outliers or cohort composition dominate?
- **Hypothesis:** robust scaling or z-scores within named position-compatible populations
  will be more stable than percentile-only vectors, while percentiles may remain better
  for display.
- **Metric, feature, or model:** all admitted direct features and candidate
  `MOD-SIM-BASELINE-V0` inputs.
- **Competing definitions:** standard z-score; robust median/IQR scaling; percentile
  rank; transformed skewed rates; family-level versus metric-level aggregation.
- **Source fields:** admitted `FEAT-*` values plus player-team-season, position,
  competition, season, minutes, and event-denominator provenance.
- **Dataset subset:** complete eligible player-team-season feature matrix after metric
  admission, split by preregistered position populations.
- **Candidate population:** outfield position-compatible cohorts; goalkeepers excluded
  and handled by `EXP-GK-002`.
- **Sample rules:** use only profiles passing selected exposure and coverage floors;
  fit transformations within the declared comparison population; prevent reference/test
  leakage in resampling.
- **Method:** compare distributions, rank correlations, neighbour overlap, perturbation
  stability, and analyst-readable explanations across transformations.
- **Baseline:** z-score each admitted metric within its position-compatible population.
- **Evaluation criteria:** deterministic output; bounded outlier influence; stable
  neighbours; retained football differences; transformation can be explained and
  inverted or contextualized.
- **Expected output:** scaling comparison, selected research default if supported, and
  explicit percentile display policy.
- **Related product surfaces:** Similar Players, Player Explorer, Metric Leaders,
  Player Profile, Compare, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No scaling method selected.
- **Follow-up:** pass all variants unchanged into `EXP-DIST-001` and measure interaction
  rather than optimizing each stage in isolation.

### EXP-DIST-001 — Distance-family comparison

- **Research question:** `RQ-SIM-001`: which transparent distance produces stable and
  football-plausible nearest neighbours on the same admitted feature set?
- **Hypothesis:** weighted Euclidean and Manhattan will offer the best initial balance
  of decomposition and robustness; other distances may reveal useful failure modes.
- **Metric, feature, or model:** `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** Euclidean; weighted Euclidean; Manhattan; cosine;
  Mahalanobis; family-level versus metric-level weights.
- **Source fields:** scaled admitted feature vector, comparison group, weights, usable
  feature mask, minutes, and coverage metadata.
- **Dataset subset:** fixed player-team-season matrix and fixed position-compatible
  candidate populations from `EXP-SCALE-001`.
- **Candidate population:** eligible outfield profiles, with the reference excluded from
  its own neighbours.
- **Sample rules:** identical features and candidates for every method; no silent
  imputation; deterministic tie-breaking.
- **Method:** retrieve top-k neighbours for every method; compare overlap, rank
  correlation, per-feature contribution, perturbation stability, positive cases, and
  negative controls.
- **Baseline:** unweighted Euclidean on scaled features.
- **Evaluation criteria:** stable top-k sets; interpretable contribution accounting;
  rejection of obvious negative controls; limited sensitivity to single features;
  acceptable expert-review burden.
- **Expected output:** method-by-method retrieval matrix, disagreement cases, and no
  production selection unless all later validation gates pass.
- **Related product surfaces:** Similar Players, Compare, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No final distance selected.
- **Follow-up:** integrate missingness and coverage policies from `EXP-MISS-001`, then
  preregister cases for `EXP-SIM-002` and `EXP-SIM-003`.

### EXP-REDUND-001 — Feature redundancy and ablation

- **Research question:** `RQ-SIM-001`: which correlated or conceptually overlapping
  features double-count the same football behavior?
- **Hypothesis:** family-aware redundancy removal will improve ranking stability and
  explanation clarity without materially reducing retrieval usefulness.
- **Metric, feature, or model:** candidate inputs to `MOD-SIM-BASELINE-V0`, including
  direct, rate, progression, creation, defensive, and spatial features.
- **Competing definitions:** pairwise correlation threshold; rank correlation; variance
  inflation; PCA diagnostics; domain-led grouping; leave-one-feature/family-out ablation.
- **Source fields:** versioned admitted feature matrix and feature lineage.
- **Dataset subset:** eligible player-team-season profiles, analyzed within each
  position-compatible population.
- **Candidate population:** all eligible outfield cohorts; goalkeeper features handled
  separately.
- **Sample rules:** minimum cohort size for covariance/correlation; resample by match or
  profile as appropriate; do not select thresholds after seeing preferred candidates.
- **Method:** quantify statistical dependence, annotate conceptual overlap, remove one
  feature/family at a time, and measure neighbour/rank/explanation changes.
- **Baseline:** complete candidate feature set.
- **Evaluation criteria:** reduced duplication; stable retrieval; no loss of an
  independently meaningful football dimension; simpler contribution explanations.
- **Expected output:** redundancy graph, retained/excluded feature decisions, and
  sensitivity table.
- **Related product surfaces:** Similar Players, Compare, Metric Leaders, methodology,
  internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No feature excluded or admitted by this registry.
- **Follow-up:** version any retained feature set before `EXP-SIM-001`.

### EXP-MISS-001 — Missing values and coverage penalties

- **Research question:** `RQ-SIM-001`: how should similarity treat unavailable features
  without converting missingness to football inactivity?
- **Hypothesis:** common-feature distance with a visible coverage penalty and minimum
  usable-feature floor will be more honest than zero imputation or unrestricted pairwise
  renormalization.
- **Metric, feature, or model:** `MOD-SIM-BASELINE-V0` input mask, coverage score, and
  explanation.
- **Competing definitions:** candidate exclusion; common-feature renormalization;
  explicit coverage penalty; missingness indicators; defensible imputation; family-level
  omission.
- **Source fields:** per-feature value, availability reason, source coverage, metric
  denominator, 360 eligibility, and quality-rule outcome.
- **Dataset subset:** eligible feature matrix with naturally missing cases plus
  preregistered synthetic masking scenarios.
- **Candidate population:** position-compatible profiles spanning high and partial
  coverage.
- **Sample rules:** distinguish not observed, structurally inapplicable, excluded by
  quality, and true zero; never silently replace missing with zero.
- **Method:** apply every policy to identical queries; measure ranking shift, effective
  feature overlap, bias toward high/low coverage, and explanation completeness.
- **Baseline:** exclude candidates below a fixed family-coverage floor; compute distance
  over common admitted features.
- **Evaluation criteria:** no missing-as-zero behavior; comparable effective dimensions;
  coverage effect visible; limited ranking manipulation by systematic missingness.
- **Expected output:** missingness taxonomy, coverage policy candidates, bias report,
  and explanation requirements.
- **Related product surfaces:** Similar Players, Player Profile, Compare, quality
  reporting, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No missing-value policy selected.
- **Follow-up:** combine the supported policy with distance experiments and
  `EXP-360-002`.

### EXP-SIM-001 — End-to-end transparent retrieval baseline

- **Research question:** `RQ-SIM-001` and `RQ-EXPLAIN-001`: can a fully versioned,
  decomposable nearest-neighbour pipeline reproduce rankings and explanations?
- **Hypothesis:** a position-aware, scaled, family-weighted retrieval baseline can
  produce deterministic results whose overall, dimensional, and feature contributions
  sum consistently.
- **Metric, feature, or model:** `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** weighted Euclidean and Manhattan baseline candidates;
  Euclidean, cosine, and Mahalanobis comparators; uniform and family weights.
- **Source fields:** player-team-season identity, candidate filters, admitted feature
  vector, scaling version, weights, missingness mask, coverage, minutes, and model
  version.
- **Dataset subset:** fixed audit snapshot after Priority 1 admission decisions and
  Priority 2 preprocessing protocols.
- **Candidate population:** position-compatible player-team-season profiles; combined
  multi-team views tested separately; goalkeepers excluded.
- **Sample rules:** selected minute and denominator thresholds are recorded; reference
  excluded; all filters and ties reproducible; no partial 360 features in the baseline.
- **Method:** implement a research-only retrieval run, reproduce it from a manifest,
  reconcile overall distance with family/feature contributions, and test small weight
  perturbations.
- **Baseline:** scaled direct-feature weighted Euclidean retrieval with uniform family
  weights.
- **Evaluation criteria:** byte-equivalent manifest; identical ordered result on rerun;
  contribution arithmetic reconciles; differences and warnings are exposed; no claim of
  quality or fit.
- **Expected output:** research manifest, top-k retrieval artifacts, contribution
  decomposition, and explanation schema.
- **Related product surfaces:** Similar Players, Compare, methodology, internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** `MOD-SIM-BASELINE-V0` remains `Proposal`.
- **Follow-up:** run reliability and football-validity experiments before any model
  status transition.

## Priority 3 — Reliability

### EXP-THRESH-001 — Minute and opportunity thresholds

- **Research question:** `RQ-RELIABILITY-001`: which eligibility thresholds produce
  acceptably stable profiles by position and metric family?
- **Hypothesis:** position- and family-aware exposure floors plus visible low-sample
  warnings will outperform one universal minute threshold.
- **Metric, feature, or model:** all per-90/rate metrics, candidate eligibility, and
  `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** universal minute floors; position-specific minute floors;
  metric-specific event-denominator floors; continuous warning bands; no exclusion.
- **Source fields:** `FEAT-MINUTES`, appearances, starts, metric numerator/denominator,
  position mix, and match-level contributions.
- **Dataset subset:** profiles recalculated at increasing minute and event-opportunity
  checkpoints.
- **Candidate population:** outfield position groups and goalkeepers analyzed separately.
- **Sample rules:** thresholds preregistered; match chronology preserved; repeated
  samples drawn at match level; low samples retained for stability measurement.
- **Method:** calculate feature convergence, rank correlation, neighbour overlap, and
  confidence intervals across thresholds and opportunity floors.
- **Baseline:** one broad minimum-minute floor with numerator/denominator displayed.
- **Evaluation criteria:** chosen rules reduce extreme instability; do not erase useful
  cohorts without evidence; remain simple enough to explain; goalkeeper exceptions
  explicit.
- **Expected output:** convergence curves, eligibility trade-off table, and proposed
  warning/exclusion bands.
- **Related product surfaces:** Similar Players, Player Explorer, Metric Leaders,
  Player Profile, Compare.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No threshold approved.
- **Follow-up:** validate candidate rules with `EXP-SIM-002` and expert review.

### EXP-SHRINK-001 — Shrinkage and visible reliability treatment

- **Research question:** `RQ-RELIABILITY-001`: does shrinkage improve stability enough
  to justify its assumptions and explanation cost?
- **Hypothesis:** empirical-Bayes shrinkage may stabilize noisy rates, but a visible
  reliability penalty or warning may preserve analyst understanding better.
- **Metric, feature, or model:** low-denominator percentage/rate features and similarity
  inputs.
- **Competing definitions:** raw rate; empirical-Bayes or hierarchical shrinkage;
  reliability-weighted feature; unchanged value plus warning; candidate exclusion.
- **Source fields:** metric numerator/denominator, minutes, position population, match
  contributions, and comparison-group distribution.
- **Dataset subset:** metrics with meaningful event denominators, analyzed at increasing
  sample sizes.
- **Candidate population:** eligible and near-threshold profiles within position groups.
- **Sample rules:** priors fit without target leakage; goalkeeper and outfield families
  separated; raw values always retained.
- **Method:** compare temporal/match-resample stability, calibration where applicable,
  neighbour changes, and explanation comprehension.
- **Baseline:** raw rate plus numerator, denominator, and low-sample warning.
- **Evaluation criteria:** measurable stability gain; no systematic suppression of valid
  outliers; reproducible prior; explanation judged understandable; raw evidence visible.
- **Expected output:** reliability comparison and retain/reject decision for each family.
- **Related product surfaces:** Similar Players, Player Profile, Compare, methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No shrinkage method selected.
- **Follow-up:** if unsupported or opaque, retain the transparent baseline and document
  the negative result.

## Priority 4 — Football validity

### EXP-SIM-002 — Same-player seasons, stability, and negative controls

- **Research question:** `RQ-SIM-002`: does the baseline retrieve sensible positive
  controls while rejecting incompatible or randomized controls?
- **Hypothesis:** comparable seasons of the same player should often be close when role
  and context remain stable, while randomized profiles and incompatible positions should
  not dominate results.
- **Metric, feature, or model:** `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** adjacent-season positives; known stable-role positives;
  random vectors; shuffled features; incompatible positions; synthetic one-feature
  perturbations.
- **Source fields:** versioned feature vectors, player identity, team, season, position
  mix, minutes, candidate population, and retrieval contributions.
- **Dataset subset:** preregistered multi-season players plus synthetic and negative
  controls; no cases selected after viewing results.
- **Candidate population:** the declared position-compatible universe and deliberately
  incompatible control universes.
- **Sample rules:** sufficient minutes in both seasons; role/team changes annotated;
  bootstrap and fixture-removal samples retained.
- **Method:** measure rank/recall of positive controls, negative-control intrusion,
  top-k overlap under perturbations, and reasons for failures.
- **Baseline:** end-to-end configuration from `EXP-SIM-001`.
- **Evaluation criteria:** deterministic mechanics; low negative-control intrusion;
  stability within preregistered tolerance; failures traceable to football or data
  context rather than hidden.
- **Expected output:** positive/negative-control report, instability cases, and no single
  aggregate claim of football validity.
- **Related product surfaces:** Similar Players, Compare, methodology, internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No model status transition.
- **Follow-up:** submit the same cases and explanations to `EXP-SIM-003`.

### EXP-SIM-003 — Structured expert and case-study review

- **Research question:** `RQ-SIM-002` and `RQ-EXPLAIN-001`: are retrieved candidates and
  explanations useful and appropriately limited for recruitment first-screening?
- **Hypothesis:** structured blind review with fixed questions will identify useful
  dimensions and failure modes more reliably than informal anecdotal approval.
- **Metric, feature, or model:** `MOD-SIM-BASELINE-V0`, explanation schema, and
  position/candidate rules.
- **Competing definitions:** uniform versus position-family weights; broad versus narrow
  candidate positions; model order versus analyst order; explanation detail levels.
- **Source fields:** fixed retrieval artifacts, configuration, contributions, minutes,
  coverage, spatial summaries, and warnings.
- **Dataset subset:** preregistered positive, ambiguous, negative, multi-team,
  mixed-position, cross-competition, and goalkeeper case studies.
- **Candidate population:** fixed per case before reviewers see results.
- **Sample rules:** consistent forms; reviewers record relevant expertise; disagreement
  retained; no result substitution after feedback.
- **Method:** blinded or order-balanced review of top-k candidates and explanations,
  scoring plausibility, usefulness, clarity, missing context, and harmful interpretation.
- **Baseline:** transparent direct-feature baseline with uniform family weights.
- **Evaluation criteria:** predefined usefulness and explanation thresholds; documented
  disagreement; no prohibited interpretation; accepted and rejected candidates have
  recorded reasons.
- **Expected output:** case-study records, reviewer matrix, disagreement log, changes
  proposed as new experiment versions, and negative findings.
- **Related product surfaces:** Similar Players, Player Profile, Compare, Shortlists,
  methodology.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No metric or model approved.
- **Follow-up:** product owner reviews evidence only after mechanical and stability gates
  pass.

## Priority 5 — Possession value

### EXP-XT-001 — Expected Threat reproduction and quality

- **Research question:** `RQ-VALUE-001`: does a locally trained xT representation add
  calibrated and explainable information beyond direct progression and zone entries?
- **Hypothesis:** a basic, versioned xT grid can add sequence-sensitive movement value,
  but rankings will vary materially with grid and training population.
- **Metric, feature, or model:** `FEAT-XT-ACTION-VALUE`,
  `MET-VALUE-XT-GAIN`, pass/carry xT aggregation, and
  `MOD-SIM-BASELINE-V0` enrichment.
- **Competing definitions:** fixed external grid; locally trained grid; alternative grid
  resolutions; successful moves only; possession-transition variants; direct zone-entry
  baseline.
- **Source fields:** `events[].location`, `events[].pass.end_location`,
  `events[].carry.end_location`, `events[].pass.outcome.name`,
  `events[].possession`, `events[].type.name`, shot/goal outcomes.
- **Dataset subset:** valid, ordered event streams split by competition/era and a
  preregistered train/evaluation policy.
- **Candidate population:** player-team-season profiles with sufficient eligible move
  actions; outfield positions evaluated separately.
- **Sample rules:** no evaluation leakage into transition estimates; coordinate and
  possession quality checks must pass; training-population variants retained.
- **Method:** reproduce basic xT, quantify transition/value stability and calibration,
  aggregate player gains, then compare direct-only versus direct-plus-xT retrieval.
- **Baseline:** direct progressive actions and final-third/penalty-area entries without
  action-value features.
- **Evaluation criteria:** reproducible grid; reported calibration/quality; stable enough
  across training populations; incremental retrieval/expert value; explainable action
  examples; no negative-value suppression without justification.
- **Expected output:** model manifest, grid and quality diagnostics, sensitivity report,
  ablation, and accept/reject decision for further research.
- **Related product surfaces:** methodology and internal research; Player Profile and
  Similar Players only after admission.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** xT remains a research candidate, not a provider field or product metric.
- **Follow-up:** compare overlap and disagreement with `EXP-PROG-001`,
  `EXP-ENTRY-001`, and `EXP-VAEP-001`.

### EXP-VAEP-001 — SPADL/VAEP reproduction and ablation

- **Research question:** `RQ-VALUE-001`: does VAEP add useful, stable information beyond
  direct metrics and xT at an acceptable explanation cost?
- **Hypothesis:** VAEP may capture broader on-ball action value, but much of its
  recruitment signal may overlap direct features and be harder to explain.
- **Metric, feature, or model:** SPADL conversion, VAEP action value, optional
  Atomic-SPADL diagnostic, and similarity enrichment.
- **Competing definitions:** direct metrics; direct plus xT; direct plus VAEP;
  direct plus both; SPADL versus research-only Atomic-SPADL representation.
- **Source fields:** ordered event type/result, coordinates, body part, possession,
  period/time, game state, team, player, and future scoring/conceding labels required by
  the versioned converter/model.
- **Dataset subset:** matches passing schema/order rules with preregistered
  training/validation/test splits that prevent match and temporal leakage.
- **Candidate population:** eligible player-team-season profiles with sufficient
  converted actions.
- **Sample rules:** converter failures and dropped events reported; model training and
  evaluation populations fixed; direct source identifiers retained for traceability.
- **Method:** reproduce a documented SPADL/VAEP pipeline, verify conversion samples,
  evaluate probability models, aggregate action values, and run feature-family ablations.
- **Baseline:** admitted direct metrics and zone entries; xT comparator from
  `EXP-XT-001`.
- **Evaluation criteria:** reproducible conversion; probability quality reported;
  incremental stability and expert usefulness; contribution explanations recoverable;
  no leakage; limitations understandable.
- **Expected output:** conversion audit, model card candidate, model-quality report,
  ablation table, and documented negative results.
- **Related product surfaces:** methodology and internal research; no product surface
  before admission.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** VAEP remains a candidate requiring experiment; Atomic-VAEP remains a
  research-only diagnostic.
- **Follow-up:** reject user-facing use if transparent direct/xT baselines are equally
  useful or explanations remain inadequate.

## Priority 6 — Spatial similarity

### EXP-SPATIAL-001 — Spatial representation and distance

- **Research question:** `RQ-SPATIAL-001`: which event-family spatial representation is
  stable and incrementally useful for player similarity?
- **Hypothesis:** normalized tactical-zone shares or fixed-grid histograms will be more
  stable and interpretable than KDE, while separate family channels will outperform one
  pooled activity map.
- **Metric, feature, or model:** `FEAT-ACTION-ZONE`,
  `FEAT-SPATIAL-HISTOGRAM`; `MET-SPATIAL-ACTION-ZONE-PROFILE`; additive
  spatial channel for `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** tactical zones; fixed grids at multiple resolutions; KDE;
  event centroids/width/depth; cosine, Manhattan, and distribution-aware distances;
  pooled versus event-family channels.
- **Source fields:** `events[].location`, event-specific end locations,
  `events[].type.name`, outcome, team/player, and attacking-direction context.
- **Dataset subset:** valid locations from passes, carries, shots, pressures, recoveries,
  interceptions, and selected goalkeeper actions, each named separately.
- **Candidate population:** eligible player-team-season profiles within position groups.
- **Sample rules:** minimum actions per representation; invalid coordinates excluded and
  counted; resample by match; KDE bandwidth and pitch-boundary correction fixed.
- **Method:** generate each representation, compare resample stability and distance
  sensitivity, and measure retrieval gain over direct metrics through ablation.
- **Baseline:** tactical-zone action shares with Manhattan distance, separated by event
  family.
- **Evaluation criteria:** stable under lower samples; interpretable differences;
  limited boundary artifacts; incremental neighbour/expert value; no duplicate weighting
  of direct features.
- **Expected output:** representation comparison, stability curves, action-family maps,
  and decision on whether a spatial channel merits further research.
- **Related product surfaces:** Player Profile action maps, Similar Players, Compare,
  internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No spatial similarity representation selected.
- **Follow-up:** use consistent zone definitions from `EXP-ENTRY-001` and assess route
  information in `EXP-SPATIAL-002`.

### EXP-SPATIAL-002 — Zone-transition vectors

- **Research question:** `RQ-SPATIAL-001`: do pass/carry start-to-end zone transitions
  add interpretable route information beyond action-location histograms and totals?
- **Hypothesis:** sparse, normalized transition vectors will distinguish progression
  routes missed by marginal start-location histograms.
- **Metric, feature, or model:** `FEAT-ZONE-TRANSITION`;
  `MET-SPATIAL-ZONE-TRANSITIONS`; additive spatial/route channel for
  `MOD-SIM-BASELINE-V0`.
- **Competing definitions:** fixed-grid transitions; tactical-zone transitions;
  pass/carry separated or combined; raw counts, per-90 rates, or within-family shares;
  cosine versus Manhattan distance.
- **Source fields:** `events[].location`, `events[].pass.end_location`,
  `events[].carry.end_location`, outcome, player/team, event type.
- **Dataset subset:** valid completed passes and carries with normalized start/end
  coordinates.
- **Candidate population:** eligible player-team-season profiles within position groups.
- **Sample rules:** minimum transition count; rare cells pooled only by a declared rule;
  failed passes treated separately; no direction inference from unvalidated coordinates.
- **Method:** construct alternative sparse vectors, resample matches, compare distance
  stability, and ablate them against direct progression and spatial histograms.
- **Baseline:** separate pass and carry tactical-zone transition shares.
- **Evaluation criteria:** route differences are explainable; lower-sample stability
  meets preregistered bounds; incremental value survives redundancy removal.
- **Expected output:** transition dictionary, sparse-vector version, maps, stability and
  retrieval-ablation report.
- **Related product surfaces:** Player Profile, Similar Players, Compare, action maps.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No transition feature admitted.
- **Follow-up:** test a separate spatial score before considering combination with the
  statistical score.

## Priority 7 — Event-linked 360 context

### EXP-360-001 — Coverage and usable-frame criteria

- **Research question:** `RQ-360-001`: which 360 frames are sufficiently linked and
  visible for a specified contextual feature?
- **Hypothesis:** feature-specific visible-area criteria will exclude materially biased
  frames that a simple non-empty-frame rule would accept.
- **Metric, feature, or model:** 360 coverage denominators and usable-frame masks for
  `FEAT-360-NEAREST-OPPONENT` and `FEAT-360-NUMERICAL-BALANCE`.
- **Competing definitions:** any linked frame; non-empty freeze frame; valid polygon;
  actor present; search radius fully inside visible polygon; feature-specific usability.
- **Source fields:** `three-sixty[].event_uuid`,
  `three-sixty[].freeze_frame[].location`,
  `three-sixty[].freeze_frame[].teammate`,
  `three-sixty[].freeze_frame[].actor`,
  `three-sixty[].freeze_frame[].keeper`, `three-sixty[].visible_area[]`,
  `events[].id`.
- **Dataset subset:** every local 360 file and its corresponding event file. Completed
  `VAL-360-001` through `VAL-360-003` establish parse, UUID-link, coordinate,
  polygon, and flag findings; they do not establish feature-specific usability or
  representative coverage.
- **Candidate population:** matches, competitions, seasons, event types, and players
  represented in linked frames.
- **Sample rules:** unresolved event links, invalid locations/polygons, absent actors,
  and partial search areas are counted separately; unobserved space is never empty space.
- **Method:** consume the completed structural-validation findings, define
  feature-specific masks, calculate usable coverage by source slice, and quantify
  coverage bias for each proposed feature.
- **Baseline:** event UUID resolves and `freeze_frame` is non-empty.
- **Evaluation criteria:** deterministic links and masks; every exclusion has a reason;
  coverage bias by competition/event/player is quantified; visible-area logic is tested.
- **Expected output:** frame/link/visibility audit, usable-frame specification, and
  coverage-bias report.
- **Related product surfaces:** quality reporting, methodology, internal research;
  selective 360 panels only after later validation.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** No 360 frame is presumed usable from file presence alone.
- **Follow-up:** resolve or explicitly accept the failures and limitations recorded by
  `VAL-360-001` through `VAL-360-003`, then complete this feature-specific coverage
  experiment before `EXP-360-002`.

### EXP-360-002 — Context-feature hypotheses

- **Research question:** `RQ-360-001`: do geometry-only features from usable visible
  snapshots add stable explanation value without coverage bias?
- **Hypothesis:** nearest visible opponent and local visible numerical balance may add
  context for covered actions, but universal player aggregates will be too selective.
- **Metric, feature, or model:** `FEAT-360-NEAREST-OPPONENT`,
  `FEAT-360-VISIBLE-SUPPORT`, `FEAT-360-NUMERICAL-BALANCE`;
  `MET-360-NEAREST-VISIBLE-OPPONENT`,
  `MET-360-VISIBLE-NUMERICAL-BALANCE`; research hypotheses for visible support,
  density, and passing options.
- **Competing definitions:** nearest opponent distance; fixed-radius visible density;
  teammate-minus-opponent balance; visible teammate support; geometry-only passing-option
  rules; event under-pressure tag as comparator.
- **Source fields:** usable frame fields from `EXP-360-001`, linked
  `events[].location`, `events[].type.name`, `events[].under_pressure`,
  event outcome, team/player.
- **Dataset subset:** only feature-specific usable, resolved frames; uncovered eligible
  events retained in the coverage denominator.
- **Candidate population:** players/events meeting preregistered usable-frame count and
  coverage-share floors; competition/season coverage reported.
- **Sample rules:** non-actor identities are not inferred; only visible players counted;
  missing/unseen is not zero; goalkeeper/actor flag anomalies excluded or flagged.
- **Method:** compute alternative geometry features, compare with event tags/outcomes,
  resample matches, measure coverage associations, and test explanation examples.
- **Baseline:** event `under_pressure` and direct event outcome, with no 360 feature in
  global similarity.
- **Evaluation criteria:** reproducible geometry; stable at required samples; no strong
  competition-coverage proxy; visible-area caveat remains explicit; incremental
  explanation value.
- **Expected output:** feature distributions, stability/bias report, example panels, and
  accept/reject decision for restricted use.
- **Related product surfaces:** selective Player Profile and Compare context panels,
  methodology, internal research.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** 360 features remain experimental and excluded from the global baseline.
- **Follow-up:** promote only through a coverage-aware metric/model experiment with an
  explicit absent-coverage path.

## Priority 8 — Goalkeeper similarity

### EXP-GK-002 — Goalkeeper-specific retrieval

- **Research question:** `RQ-GK-001`: does a goalkeeper-specific feature family and
  candidate universe outperform a generic similarity engine?
- **Hypothesis:** separating shot stopping, distribution, area actions, and sweeping will
  yield more coherent candidates than applying outfield dimensions or generic weights.
- **Metric, feature, or model:** proposal for a goalkeeper-specific configuration using
  `FEAT-GK-SHOT-FACED`, `FEAT-GK-XG-FACED`, admitted distribution, claim, and sweeping
  features.
- **Competing definitions:** generic engine with goalkeeper features; dedicated
  goalkeeper weights/distance; pre-shot xG-faced and save-rate alternatives; opportunity
  adjustments.
- **Source fields:** admitted outputs from `EXP-GK-001`, goalkeeper passes, locations,
  minutes, shots faced, linked shot xG, claims, punches, smothers, and sweeper events.
- **Dataset subset:** goalkeeper-team-season profiles with validated minutes and
  goalkeeper taxonomy.
- **Candidate population:** goalkeepers only, with explicit minimum minutes and
  shots/action denominator rules.
- **Sample rules:** penalty/non-penalty splits; team-context caveats; no post-shot xG;
  partial 360 context excluded from the baseline.
- **Method:** compare generic and dedicated retrieval, bootstrap matches, test known
  cases/negative controls, and conduct goalkeeper-aware expert review.
- **Baseline:** scaled direct goalkeeper features with weighted Euclidean and uniform
  family weights.
- **Evaluation criteria:** stable lists; coherent dimension contributions; improvement
  over generic configuration; no domination by distribution volume; expert usefulness.
- **Expected output:** goalkeeper retrieval comparison, case studies, explanation
  examples, and model-path decision.
- **Related product surfaces:** goalkeeper Similar Players, Player Profile, Compare,
  Metric Leaders.
- **Status:** `Planned`.
- **Result:** Not run.
- **Decision:** no goalkeeper similarity model selected; model status remains `Proposal`.
- **Follow-up:** repeat on new data if current shots-faced samples do not support stable
  conclusions.

## Dossier backlog coverage

This matrix maps every item in the dossier's
[recommended experiment backlog](research-dossier.md#25-recommended-experiment-backlog)
to a registry record. Mapping is not evidence of execution.

| Dossier item | Covered by |
|---:|---|
| 1. Event-family and conditional-field audit | Completed `VAL-SCHEMA-001` and exhaustive field audit; findings remain prerequisites to all Priority 1 experiments |
| 2. Starts, changes, extra time, dismissals, interrupted matches | `EXP-MIN-001` |
| 3. Pass outcomes and denominator | `EXP-PASS-001` |
| 4. Shot-assist links and xA | `EXP-XA-001` |
| 5. Carry, dribble, dispossession, miscontrol, losses | `EXP-LOSS-001` |
| 6. Goalkeeper taxonomy and shot links | `EXP-GK-001` |
| 7. Coverage tables | Completed `VAL-FILE-001`, `VAL-SCHEMA-001`, `VAL-COORD-001`, 360 validations, and data coverage documentation |
| 8. z-score, robust scaling, percentiles | `EXP-SCALE-001` |
| 9. Euclidean, weighted Euclidean, Manhattan, cosine, Mahalanobis | `EXP-DIST-001` |
| 10. Neighbour overlap and rank correlation | `EXP-SCALE-001`, `EXP-DIST-001` |
| 11. Family versus metric weighting | `EXP-DIST-001`, `EXP-SIM-001` |
| 12. Correlated/redundant metrics | `EXP-REDUND-001` |
| 13. Missing-feature policies and coverage penalties | `EXP-MISS-001` |
| 14. Increasing-minute convergence | `EXP-THRESH-001` |
| 15. Position-family eligibility floors | `EXP-THRESH-001` |
| 16. Raw rates, shrinkage, reliability penalties | `EXP-SHRINK-001` |
| 17. Match bootstrap and neighbour stability | `EXP-SIM-002` |
| 18. Minimum denominators for percentages | `EXP-THRESH-001`, `EXP-SHRINK-001` |
| 19. Same-player seasons | `EXP-SIM-002` |
| 20. Positive examples and negative controls | `EXP-SIM-002` |
| 21. Structured expert review | `EXP-SIM-003` |
| 22. Expert acceptance/rejection reasons | `EXP-SIM-003` |
| 23. Broad-position restrictions | `EXP-SIM-003` |
| 24. Inconclusive and negative findings | All experiments under the negative-result policy |
| 25. Basic xT reproduction | `EXP-XT-001` |
| 26. xT quality and population sensitivity | `EXP-XT-001` |
| 27. SPADL/VAEP reproduction | `EXP-VAEP-001` |
| 28. Action-value ablation and expert usefulness | `EXP-XT-001`, `EXP-VAEP-001`, `EXP-SIM-003` |
| 29. xT/VAEP/direct-entry overlap | `EXP-XT-001`, `EXP-VAEP-001`, `EXP-REDUND-001` |
| 30. Grids, tactical zones, transitions | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` |
| 31. Spatial distance alternatives | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` |
| 32. Lower spatial samples | `EXP-SPATIAL-001`, `EXP-SPATIAL-002` |
| 33. Incremental spatial retrieval | `EXP-SPATIAL-001` |
| 34. Separate spatial event-family channels | `EXP-SPATIAL-001` |
| 35. 360 event/match coverage | `EXP-360-001` |
| 36. Visible-area handling | `EXP-360-001` |
| 37. Nearest opponent and local density | `EXP-360-002` |
| 38. Visible passing options and visibility rejection | `EXP-360-001`, `EXP-360-002` |
| 39. 360 context versus under-pressure tags | `EXP-360-002` |
| 40. 360 explanation value versus coverage bias | `EXP-360-002` |
| 41. Prevent inadequate 360 from global similarity | `EXP-MISS-001`, `EXP-360-002` |
| 42. Goalkeeper feature families and populations | `EXP-GK-001`, `EXP-GK-002` |
| 43. Goalkeeper stability by family | `EXP-GK-001`, `EXP-GK-002` |
| 44. Generic versus goalkeeper-specific engine | `EXP-GK-002` |
| 45. Goalkeeper cases and negative controls | `EXP-GK-002`, `EXP-SIM-003` |

## Registry rule

Results must replace `Not run` only after the experiment reaches `Completed` under
[research methodology](research-methodology.md#4-experiment-lifecycle). A new result
must name its immutable run artifact and completed `VAL-` records. Until then, every
metric remains `Proposed` or `Researching`, and every model remains `Proposal`.
