# ScoutLabs Research Dossier

**Research cut-off:** 24 July 2026  
**Product:** ScoutLabs — Explainable football recruitment analytics  
**Primary source:** StatsBomb Open Data

## 1. Executive summary

ScoutLabs can derive substantial recruitment value from StatsBomb Open Data, but only if the product is explicit about what is directly observed, what is derived, what is model-based, and what remains unobservable without tracking. The local snapshot available to the project is meaningful for an MVP: ScoutLabs local StatsBomb inventory, generated 24 July 2026, reports 80 seasons, 3,961 matches, roughly 11,794 unique players, full event and lineup coverage for those matches, and 426 three-sixty files. That is enough to support event-first recruitment workflows and selective 360-enhanced analysis, but not enough to treat 360 as a universal context layer.

The strongest defensible MVP foundation is an explainable, player-team-season-centric workflow built on directly observable on-ball events, shot context, possession sequencing, position-aware comparison groups, sample warnings, and decomposable similarity. That aligns with the [ScoutLabs Product Brief](../../BRIEF.md), which emphasizes explainability, reproducibility, visible limitations, action maps, comparison groups, dimension-level control, analyst-controlled rankings, and meaningful use of sequencing, spatial information, and available 360 frames.

For recruitment, the most useful event-compatible metric families are passing, ball progression, chance creation, shooting, directly recorded defensive actions, goalkeeper shot-stopping and distribution, and action-location profiles. Stronger model-based layers such as Expected Threat (xT) and VAEP are compatible with event data and have strong academic pedigrees, but they still require product-specific experiments before deployment because model quality, cohort design, temporal scope, and explanation design materially affect scouting validity. Recent work specifically argues that xT quality should be quantified before using it for scouting applications.[^8][^9][^11][^23]

Several contested metrics do not have one universally accepted definition. Progressive passes and carries, line-breaking passes, key passes, shot assists, expected assists, cutbacks, crosses, and pass completion vary by provider or researcher. ScoutLabs should therefore document definitions explicitly, compare alternatives where they matter, and avoid silently treating one vendor convention as football truth. StatsBomb directly supplies categorical labels such as cross, cut-back, switch, shot-assist, goal-assist, and through-ball technique, but it does not directly supply progressive-pass or line-breaking-pass flags in the verified open schema.[^5][^6][^31]

The largest analytical boundary is the absence of continuous tracking. Event data can say where actions happened, in what order, under some tagged contexts, and sometimes with freeze-frame context; it cannot reliably recover full team shape, off-ball occupation, support angles between events, running power, marking responsibility, real pressing intensity, or latent tactical role without stronger assumptions. Tracking-based studies on pressure, pass difficulty, off-ball value, and counterpressing show that these questions become more robust once all players are continuously observed. Their existence is evidence that many appealing constructs are only partially approximable from events and 360 snapshots.[^15][^16][^17][^18]

The recommended product posture is conservative and layered. Put directly interpretable event metrics and decomposable similarity into the MVP; make xT, VAEP, role-aware weighting, spatial similarity, and 360-derived context methods that require experiments; keep tracking-dependent constructs, full defensive pressure models, advanced line-breaking, true off-ball role-fit, and future-performance prediction out of the current production scope. This conclusion is consistent with the product brief and with the methodological literature.[^19][^20][^23]

## 2. Research methodology

This dossier prioritizes evidence in the requested order: official StatsBomb and Hudl documentation first, then original peer-reviewed method papers, official documentation or repositories from method authors, reproducible implementations, recognized professional research, and high-quality technical publications. The attached StatsBomb specifications were used as the primary evidence for schema, field availability, provider labels, and limitations. The local inventory was used only for the project snapshot and coverage counts. Internet research was used to verify public versions of provider documents and locate primary methodological sources available through 24 July 2026.[^1][^2][^3][^4][^5][^6][^7]

The practical research question throughout was not “what is imaginable in football analytics?” but “what is responsibly supportable for ScoutLabs under the approved product boundary?” The [ScoutLabs Product Brief](../../BRIEF.md) states that the platform must remain explainable, reproducible, and explicit about limitations; must not imply false precision; must not expose every calculated metric; and must keep missing data, low minutes, contextual bias, and coverage limits visible. Those constraints materially shape every recommendation below.

When external literature and current open-data compatibility diverge, this dossier favors compatibility and explainability over maximal sophistication. Tracking-based methods are discussed when they clarify the frontier of what event data cannot do, but they are not promoted as current ScoutLabs production methods unless a defensible event-only approximation exists. That is a ScoutLabs product inference, not a claim that the tracking-based methods themselves are weak.[^15][^16][^17][^18]

Claims are separated into three types:

1. **Provider evidence:** a field, event, label, relationship, or caveat documented by StatsBomb or Hudl.
2. **External methodological evidence:** a definition, model, validation method, or limitation supported by a primary paper or method-author source.
3. **ScoutLabs inference:** a product or research recommendation derived from the evidence and the approved product constraints. These inferences are explicitly identified where they are not direct findings from a cited source.

No implementation, repository inspection, software architecture, or validation result is claimed in this dossier.

## 3. Evidence hierarchy

The strongest evidence comes from the StatsBomb specifications and public open-data repository, followed by peer-reviewed papers such as Decroos et al. on VAEP, Bransen and Van Haaren on pass valuation, PlayeRank on role-aware evaluation, Anzer and Bauer on expected passes, Bauer and Anzer on counterpressing detection, and methodological reviews of footballer attributes and talent identification.[^1][^8][^10][^13][^15][^16][^19][^20]

Official or author-maintained documentation for `socceraction` and scikit-learn is used mainly to assess method availability, assumptions, reproducibility, and common similarity families rather than as evidence that any method is football-valid for ScoutLabs.[^12][^27][^28][^29][^30]

Where evidence is newer or less mature, the report says so explicitly. Examples include 2026 work on xT quality, temporal xT, cooperative contribution models, and structural pass analysis. These are useful research signals, but they do not justify direct adoption into an explainable recruitment MVP without internal validation.[^23][^24][^25][^26]

Where no stable consensus exists, the issue is classified as contested or unresolved rather than presented as settled. This applies especially to progressive-action definitions, line-breaking passes, possession-adjusted defensive metrics, cross-league adjustment, minimum-minute policies, and the football validity of mathematically coherent similarity outputs.[^20][^21][^31]

Evidence levels used in the source-to-recommendation matrix are:

- **Level A:** official provider specification or original peer-reviewed method paper directly supporting the claim;
- **Level B:** official method documentation, reproducible author implementation, systematic review, or strong professional source;
- **Level C:** ScoutLabs inference grounded in Level A or B evidence but requiring product-specific validation;
- **Level D:** unresolved hypothesis, recent preprint, or method whose applicability to ScoutLabs remains uncertain.

## 4. StatsBomb Open Data capability assessment

StatsBomb Open Data is organized around competitions, matches, lineups, events, and three-sixty files, matching the structure described in the [ScoutLabs data-source documentation](../data-source.md). Coverage can be partial and files or fields may be absent. That matters because availability differs by match and the local snapshot contains only 426 three-sixty files for 3,961 matches.[^1]

### 4.1 Universally or broadly available layers

The competition, match, and lineup schemas expose identity and grouping information such as competition and season identifiers, gender, country, match date, kick-off time, match week, stage, stadium, referee, teams, managers, lineup rosters, shirt numbers, nationalities, and metadata versions.[^2][^3][^4][^6] These fields are not all recruitment metrics, but they provide value for filtering, provenance, grouping, data-quality checks, reproducibility, and interpretation.

The event layer is the analytical core. StatsBomb records ordered events with identifiers, match period, timestamp, minute, second, possession identifier, possession team, play pattern, team, player, event-time position, coordinates where applicable, duration where relevant, under-pressure and counterpress indicators where applicable, off-camera and out-of-bounds flags, related-event identifiers, and event-specific subobjects.[^5][^6]

The verified event families include passes, carries, dribbles, shots, pressures, duels, interceptions, recoveries, blocks, clearances, goalkeeper actions, Starting XI, substitutions, Tactical Shift, Player On, and Player Off.[^5][^6]

### 4.2 Event-conditional fields

Many useful fields are conditional rather than universal. Passes can include recipient, length, angle, height, end location, body part, type, technique, outcome, cross, cut-back, switch, shot-assist, and goal-assist. Carries include end location. Dribbles include outcome and optional nutmeg, overrun, and no-touch indicators. Shots include body part, technique, type, outcome, end location, freeze frame, and StatsBomb xG, with optional flags such as first-time, follows-dribble, aerial-won, open-goal, deflected, and other context-specific properties.[^5][^6]

ScoutLabs can therefore derive counts and rates, action distances and angles, progression, zone entries, possession-sequence participation, action-type mixes, under-pressure splits, counterpress-tagged event counts, shot-context splits, goalkeeper action families, and event-linked spatial maps. The product must preserve whether each value is provider-supplied, directly aggregated, or derived.

### 4.3 Possessions, ordering, and relationships

StatsBomb supplies possession identifiers and possession-team fields, allowing event sequences to be grouped without rebuilding every possession from scratch. Related-event identifiers support links between events such as a pass and shot, a dribble and dribbled-past event, or a shot and goalkeeper action. Timestamps and ordered event identifiers support sequence participation, buildup involvement, secondary creation, and contextual windows, although edge cases must be audited.[^5][^6]

Play-pattern fields include provider-derived categories. The schema documents a “From Counter” pattern based on turnover origin, directness, and territorial advance. This is analytically useful for transition-sensitive analysis, but it is provider logic rather than a raw observation and should be labeled accordingly.[^6]

### 4.4 Coordinates and direction

StatsBomb uses a fixed 120-by-80 coordinate system. The open 360 specification states that locations follow the attacking orientation of the linked event, with the actor’s team attacking from x=0 toward x=120.[^6][^7] ScoutLabs should normalize every profile to a common attacking direction before deriving progression, entries, centroids, zone transitions, or spatial similarity.

### 4.5 Shot freeze frames

Shot freeze frames are event-conditional and analytically valuable. A shot can include a freeze-frame array containing relevant players, their locations, team relationship, player identity, and position. This supports shot maps, xG profiles, shooting-context summaries, visible-defender counts, and some goalkeeper or obstruction context. It does not provide full post-shot ball-flight information or generic context for all event types.[^6]

### 4.6 StatsBomb 360 frames

Open 360 frames link a frame to an event UUID, include a visible-area polygon when available, and represent visible players through location, teammate, actor, and goalkeeper flags. Non-actor player identities are not supplied. The official specification warns that not all 22 players are visible, not all events receive a frame, visible-area polygons may be empty or missing, actor labels can be absent, and goalkeeper/team flags can contain rare inconsistencies.[^7]

Consequently, 360 can support selective event-context features, but it cannot be treated as a universal all-player tracking layer. Every 360-derived output must show coverage and must not be allowed silently to bias rankings toward competitions or players with more frame coverage.

### 4.7 What cannot be inferred without continuous tracking

Event data and sparse snapshots cannot reliably measure continuous team shape, movement between events, support angles over time, defender arrival times, running intensity, off-ball screening, complete marking responsibility, synchronized spacing dynamics, full receiving-option sets, or true pressure intensity. Tracking-based work on expected passes, counterpressing, pressure, and off-ball value demonstrates why those constructs require synchronized positional observations.[^15][^16][^17][^18]

ScoutLabs may build approximations from event locations or visible 360 context, but it must not present them as equivalent to continuous tracking measures.

## 5. Analytical-unit assessment

A pure **player** unit is too coarse for ScoutLabs. It combines seasons, teams, managers, competitions, positions, and tactical contexts into one profile and therefore obscures the conditions under which the observed behavior occurred.

A **player-season** unit is more useful, but becomes ambiguous when a player changes club during the season. An aggregate may be valuable for exploration, yet it hides whether the statistical profile was generated for team A, team B, or both.

A **player-team-season** unit is the strongest default for an explainable recruitment product. It handles mid-season transfers and tactical context better than player-only or player-season aggregation, while remaining understandable to analysts. This is a ScoutLabs inference aligned with the product brief and role-aware evaluation literature.[^13]

A **player-position-season** unit can reduce role mixing, but only if minutes by position are derived reliably. It also risks fragmenting samples and treating source position labels as complete tactical roles. StatsBomb records event-time positions, Starting XI formations, and Tactical Shift lineups, which can support position histories and primary-position shares, but not perfect tactical-role inference.[^5][^6]

A **role-specific sample** is potentially valuable when the role is defined through observable behavior rather than assumed from a label. It should remain an experimental layer because the current data does not directly observe many off-ball responsibilities.

Recommended treatment:

- store and expose player-team-season as the default analytical object;
- preserve team, competition, season, position mix, starts, and minutes by position;
- allow optional combined player-season views;
- allow position-compatible comparison groups;
- flag partial seasons and multi-team seasons visibly;
- retain Tactical Shift evidence where it changes position interpretation;
- avoid presenting position labels as complete tactical-role definitions.

## 6. Minutes, samples and normalization

### 6.1 Deriving appearances and minutes

StatsBomb provides enough ingredients to derive starts, substitute appearances, entries, exits, extra-time participation, and many incomplete appearances. Starting XI events define starters and formation snapshots; substitutions, Player On, and Player Off events describe changes; periods distinguish regulation halves, extra-time periods, and shootouts; timestamps are recorded with fine temporal resolution; and half-end metadata can indicate early video end or suspension.[^5][^6]

A robust minutes policy should:

- use the match’s actual period endpoints rather than assume every match lasts exactly 90 minutes;
- exclude shootout time from playing minutes;
- include extra time when a player was on the pitch;
- account for substitution entry and exit timestamps;
- handle dismissals through card and player-off evidence where available;
- preserve incomplete or interrupted appearances as a quality state;
- flag matches with missing or inconsistent lineup/event evidence;
- store both raw seconds and rounded display minutes.

Field auditing is required before claiming complete dismissal handling because card, substitution, Player Off, and video-end edge cases can interact.

### 6.2 Per-90 rates and denominators

Per-90 rates are useful for comparing exposure, but they are not reliability adjustments. A player with 150 minutes can produce an extreme per-90 value from very few actions. ScoutLabs should always show raw minutes, appearances, starts, and relevant action denominators beside normalized rates. This follows the product brief’s requirement to avoid false precision and the wider methodological warning against isolated indicators and weak sample design.[^20]

Success percentages should expose both numerator and denominator. A 90% pass-completion value from ten attempts should not be visually equivalent to 90% from one thousand attempts. The same principle applies to dribble success, aerial success, shot conversion, and goalkeeper save rates.

### 6.3 Minimum-minute thresholds

There is no single defensible universal threshold for every metric and position. Shooting, creation, defending, distribution, and goalkeeper shot-stopping have different opportunity structures. Therefore, default thresholds should be treated as explicit product conventions and validated empirically rather than labeled as universal scientific cut-offs.

A conservative MVP approach is to:

- use broad position-aware minimum-minute floors for candidate eligibility;
- retain low-minute profiles in exploration when useful;
- flag them as low reliability;
- apply metric-specific minimum denominators for percentages;
- test ranking stability across several thresholds;
- avoid hiding the threshold configuration from the analyst.

### 6.4 Shrinkage and reliability adjustment

Empirical-Bayes or related shrinkage is statistically attractive for noisy rates and small denominators, but its product effect must be tested. Shrinkage can improve stability while also making outputs harder to explain. It is therefore a **Candidate requiring experiment**, not an assumed MVP truth. Internal experiments should compare raw rates, shrinkage-adjusted rates, and explicit reliability penalties using same-player stability and analyst review.[^23]

### 6.5 Normalization layers

ScoutLabs should separate:

1. **Totals and raw counts** for transparency.
2. **Exposure-normalized values** such as per-90 rates, action shares, and success percentages.
3. **Comparison-context normalization** such as z-scores, robust-scaled values, or percentiles within a stated population.

Z-scores are interpretable when distributions are approximately well behaved, but can be distorted by heavy tails and extreme outliers. Robust scaling using medians and interquartile ranges is less sensitive to extremes. Percentiles are intuitive to analysts but lose information about the magnitude of gaps and depend completely on the comparison population. ScoutLabs should test all three for stability and explanation quality rather than choose one by convention alone.[^27]

### 6.6 Possession and opportunity adjustment

Possession-adjusted and opportunity-adjusted metrics are useful but not interchangeable. Defensive action volume is strongly affected by how much time a team spends without the ball. Passing volume is shaped by team possession and buildup structure. Shooting and dribbling have their own event opportunities.

ScoutLabs should reserve possession adjustment for metrics where the denominator has a clear football meaning, for example defensive actions per opponent-possession segment or per estimated out-of-possession time. Other families should use direct opportunities where possible: completions per pass attempt, successful dribbles per dribble attempt, goals per shot, or xA per shot assist. These are ScoutLabs conventions and must be documented as such.

### 6.7 Comparison populations and cross-competition use

Percentiles must always name the comparison group: position group, competition set, season set, minute threshold, and any age or team filters when those become available. Position-specific comparison groups are preferable to universal groups because the event opportunity and football meaning of the same metric differ by position.[^13]

Cross-competition comparisons should remain possible but visibly caveated. The current MVP does not include league-strength adjustment, and a percentile across different competitions must not imply equivalent opposition quality. Weak or opaque adjustment would be worse than an explicit warning and analyst judgment.

## 7. Passing and progression

Passing is one of the strongest families in StatsBomb Open Data. The verified schema provides intended recipient, pass length, angle, height, end location, cross, cut-back, switch, shot-assist, goal-assist, body part, pass type, technique, and structured outcomes.[^5][^6]

### 7.1 Pass completion

Pass completion is contested. Wyscout describes success for several pass categories through the next touch being made by a teammate. StatsBomb’s schema represents failure through outcomes such as Incomplete, Out, Pass Offside, Injury Clearance, and Unknown, so public implementations commonly infer completion from the absence of a failure outcome.[^6][^31]

ScoutLabs must document:

- which outcome values count as unsuccessful;
- whether deliberate clearances are excluded from the denominator;
- how offside passes are treated;
- whether incomplete data or unknown outcomes are excluded;
- whether crosses and set-piece deliveries share the same denominator.

### 7.2 Forward passes

A transparent event-compatible definition is geometric: a pass with positive goalward x-progression after attacking-direction normalization. Alternative definitions may require a minimum vertical component or exclude lateral passes with tiny positive change. ScoutLabs should expose the selected rule and avoid an undefined narrative label.

### 7.3 Progressive passes

Progressive-pass definitions differ. Wyscout uses goal-distance reduction thresholds of 30 metres when both points are in the team’s own half, 15 metres when the pass crosses halves, and 10 metres when both points are in the opponent’s half.[^31] Other approaches use simple territorial advance, start/end zones, or action value such as xT gain. Recent peer-reviewed work notes the lack of consistent descriptions and studies repeatable progressive-pass clusters.[^21]

StatsBomb Open Data does not provide a verified native progressive-pass flag. ScoutLabs should adopt one versioned default for the MVP, compare it against alternatives, and label it as ScoutLabs-derived rather than provider-supplied.

### 7.4 Line-breaking passes

Strong line-breaking definitions depend on opponent-line structure, defender arrangement, or structural disruption. Tracking-based structural pass research makes that dependency explicit.[^26] With event data and partial 360, ScoutLabs can research proxies based on verticality, penetrated zones, or visible opponents, but should not present them as fully observed line-breaking. Classification: **Research only** or **Candidate requiring experiment**, depending on the proxy.

### 7.5 Final-third and penalty-area passes

Final-third entries and penalty-area entries can be defined directly from normalized start and end coordinates. Wyscout’s glossary requires origin outside the target zone and the next touch inside it; StatsBomb can support a comparable event-derived definition through pass end location and event relationships.[^31] These are strong MVP candidates because the geometry is transparent.

### 7.6 Switches, through balls, crosses, and cutbacks

StatsBomb supplies provider-defined indicators for switches, crosses, cutbacks, and through-ball technique. The open specification describes a switch through large pitch-width displacement, while cross and cutback definitions depend on provider geometry and zones.[^5][^6] ScoutLabs should expose these as provider-defined fields, with a methodology note, rather than replace them with silent home-built heuristics.

### 7.7 Key passes, shot assists, and expected assists

Key pass, shot assist, and expected assist are not synonyms. Wyscout distinguishes a shot assist as the final action before a teammate’s shot and defines expected assist through the xG of the assisted shot, while its key-pass category is narrower and tied to an immediate clear chance.[^31]

StatsBomb records pass shot-assist and goal-assist indicators and links shots to assisted-shot identifiers. ScoutLabs can therefore recreate expected assists as the sum of StatsBomb xG from linked shots created by qualifying passes. That value should be labeled “ScoutLabs xA derived from linked StatsBomb shot xG,” not as a commercial provider xA field.[^5][^6]

### 7.8 Pass difficulty

Modern expected-pass models use synchronized player positions and sometimes richer orientation or temporal context. They are strong research benchmarks but are not properly reproducible from the current event-only dataset.[^15] A simplified event-only pass-difficulty model could be researched, but it would be a different construct and would require explicit validation.

### 7.9 Pass value

Pass value is more compatible with current data through event-based xT or VAEP than through full spatio-temporal expected-pass models. Direct metrics should remain visible even if action-value features are added, because a single value score can hide whether value came from volume, location, risk, or sequence context.[^8][^9][^10][^11][^14]

## 8. Carrying and dribbling

StatsBomb Data Version 1.1 includes carries with end locations, enabling carry counts, distances, maps, zone entries, and progression calculations.[^6]

Dribbles and carries must not be conflated. A dribble event represents an attempt to beat an opponent and includes Complete or Incomplete outcomes, with optional nutmeg, overrun, and no-touch indicators. The specification explicitly notes that dribbles do not represent every instance of moving with the ball; carries are the appropriate source for general ball movement.[^6]

### 8.1 Progressive carries

Progressive carries are contested in the same way as progressive passes. Wyscout applies 30/15/10-metre goal-distance thresholds by pitch context to progressive runs.[^31] StatsBomb Open Data does not provide a verified progressive-carry flag, but start/end geometry makes a documented derived definition possible.

ScoutLabs should compare at least:

- Wyscout-style goal-distance reduction;
- simple positive x-distance with a minimum threshold;
- entry into a more advanced tactical zone;
- xT gain from carry start to end.

The first three are easier to explain; xT-based progression may capture value but inherits model assumptions.

### 8.2 Advanced-zone entries

Carries into the final third, penalty area, central attacking zones, or other versioned zones are stronger MVP candidates than a generic “carry quality” score because they follow simple spatial logic and are easy to map.

### 8.3 Take-ons and successful dribbles

Successful dribbles should be calculated from dribble outcomes. Attempt volume and success rate should both be shown. Defensive dribbled-past events should not be treated as a complete mirror of all dribble attempts because the provider notes relationship asymmetries.[^6]

### 8.4 Possession retention and ball losses

Progression should be paired with retention because raw advance can overvalue high-turnover profiles. StatsBomb’s Dispossessed events, Miscontrols, incomplete dribbles, pass outcomes, related events, and possession ordering support loss summaries, although attribution rules must be documented.[^5][^6]

Potential MVP metrics include:

- carries followed by team retention within a short event window;
- dribble success rate;
- dispossessions and miscontrols per 90;
- losses per 100 on-ball actions;
- progression-to-loss ratio.

The exact event window and loss taxonomy are contested and require field auditing.

### 8.5 Progression under pressure

The under-pressure flag and pressure-overlap logic permit contextual splits for passes, carries, dribbles, and receptions where present. These are event-level context proxies, not continuous pressure-intensity measurements.[^6][^17] They are useful as descriptive splits and possible experimental similarity features.

## 9. Shooting and goal threat

The shot schema directly supports body part, technique, type, outcome, end location, first-time, follows-dribble, aerial-won, deflection, open-goal, freeze frame, and StatsBomb xG.[^5][^6]

### 9.1 Strong direct metrics

Strong event-compatible metrics include:

- shots and non-penalty shots;
- StatsBomb xG and non-penalty xG;
- goals and non-penalty goals;
- average xG per shot;
- shot locations and spatial distributions;
- body-part and technique shares;
- headers;
- first-time and follows-dribble shots;
- open-play, set-piece, and penalty splits;
- shot outcomes.

StatsBomb xG is provider-supplied and should be presented as source data, not as a ScoutLabs model.[^6]

### 9.2 Shot quality and selection

Average xG per shot is a simple measure of typical chance quality. Shot-location distributions, body-part mix, and context shares give a richer description of shot selection. ScoutLabs should avoid collapsing these into one “finishing quality” score because volume, selection, and execution are distinct.

### 9.3 Goals above expected

Goals minus xG is analytically useful but volatile in player-team-season samples. It should be shown descriptively with shots and xG, not presented as stable finishing talent without longitudinal evidence. Low-minute and low-shot warnings are essential.[^20]

### 9.4 One-on-one situations

A stable one-on-one field was not verified in the reviewed open specifications. ScoutLabs should classify this as **Unresolved** until the local field audit confirms availability or a documented approximation is designed. It must not infer one-on-ones from low xG, open-goal flags, or proximity alone.

### 9.5 Spatial shooting profiles

Shot maps, zone histograms, xG-weighted location maps, and body-part maps are strong MVP candidates. They are event activity maps, not continuous occupation heatmaps. Kernel density estimates may aid visualization but should not imply more spatial precision than the event sample supports.

## 10. Creation, sequences and possession value

Expected assists derived from linked shot xG are straightforward and high-value because StatsBomb records shot-assist relationships and shot xG. They are more defensible than using assists or pass completion alone as creativity proxies.[^5][^6][^31]

Secondary creation and buildup involvement are feasible because events are ordered, possession identifiers are supplied, and related events connect actions. ScoutLabs can derive sequence participation, pre-assist involvement, buildup actions in shot-ending possessions, and shares of actions within dangerous possessions. These are derived metrics and require documented sequence rules.

### 10.1 SPADL and Atomic-SPADL

SPADL provides a normalized action representation designed to make provider event data suitable for action-value models. Atomic-SPADL decomposes actions more finely. The `socceraction` project supplies reproducible converters and implementations for SPADL, Atomic-SPADL, xT, VAEP, and Atomic-VAEP.[^12]

SPADL is highly compatible with StatsBomb Open Data and valuable as a research normalization layer. Atomic-SPADL is more granular but creates additional explanation and validation burden.

### 10.2 Expected Threat

Expected Threat values ball movement by estimating how an action changes the probability of eventually scoring from pitch zones. Its grid structure can be intuitive to analysts and is compatible with event coordinates.[^9] However, xT depends on the training sample, grid, possession definition, transition assumptions, and evaluation procedure. Recent work stresses that model quality should be quantified before scouting deployment.[^23]

Assessment:

- **Required fields:** start/end locations, action type, outcome, possession or sequence logic;
- **Open Data compatibility:** high;
- **Complexity:** medium;
- **Training:** required for a data-specific transition model, unless using a fixed external grid;
- **Interpretability:** medium to high;
- **Recruitment usefulness:** promising for progression and creation;
- **Classification:** **Candidate requiring experiment**.

### 10.3 VAEP

VAEP values actions through changes in the probabilities of scoring and conceding in the near future. It was explicitly motivated by evaluating on-ball actions beyond goals and assists and is relevant to recruitment.[^8]

Assessment:

- **Required fields:** normalized action sequences, action context, outcomes, game state, and trained scoring/conceding models;
- **Open Data compatibility:** high after SPADL conversion;
- **Complexity:** medium to high;
- **Training:** required;
- **Interpretability:** medium, lower than direct metrics and basic xT;
- **Recruitment usefulness:** high potential;
- **Validation requirement:** high;
- **Classification:** **Candidate requiring experiment**.

### 10.4 Atomic-VAEP

Atomic-VAEP adds finer action decomposition and can improve attribution around receives and ball movement. Its additional granularity is not automatically useful to a recruitment analyst and can make explanations harder. Classification: **Research only** for the current product.

### 10.5 Alternative possession-value frameworks

EPV-style positional frameworks use synchronized player and ball locations to estimate instantaneous possession value and therefore represent a richer-data frontier rather than a current Open Data method.[^22] Temporal xT and cooperative or Shapley-style contribution models are methodologically interesting, but their added complexity and recent publication status make them research-only until reproduced and validated.[^24][^25]

The practical recommendation is to use direct sequence metrics and recreated xA in the MVP; test xT and VAEP through ablation and expert review; keep Atomic-VAEP, temporal xT, and cooperative contribution models in the research lane.

## 11. Defending and pressing

Event data can describe recorded defensive interventions, but not all defensive value. StatsBomb records pressures, Dribbled Past, duels, interceptions, recoveries, blocks, clearances, and goalkeeper defensive actions.[^5][^6]

### 11.1 Pressures and counterpressures

StatsBomb pressure events have a start location and duration. The provider’s under-pressure logic links pressure overlap to on-ball events. Counterpress flags identify certain actions within a short post-turnover context.[^6]

Defensible outputs include:

- pressure count and rate;
- pressure locations and height;
- counterpress-tagged action count;
- on-ball actions under pressure;
- pressured-pass or pressured-carry splits;
- outcomes following recorded pressure events;
- team and player pressure maps.

These are event-level proxies, not complete pressing models. Tracking-based pressure and counterpress research uses synchronized positional information and expert labels to model team structure and intensity more fully.[^16][^17]

### 11.2 Recoveries, interceptions, tackles, blocks, and clearances

The event taxonomy supports counts, rates, outcomes where defined, spatial distributions, and sequence involvement. Tackle metrics require careful taxonomy because StatsBomb represents tackles through Duel subtypes and separately records Dribbled Past and other events. A crude “tackles won” value should not be exposed without a documented event mapping.[^6]

Aerial activity should combine relevant Duel, Clearance, Miscontrol, Pass, and Shot evidence only after a field-level audit. Provider event models differ, so ScoutLabs should not assume that one event family contains every aerial contest.

### 11.3 Defensive-action height and sequence involvement

Mean or median x-location of pressures, recoveries, interceptions, tackles, and clearances can describe where recorded defensive activity occurs. These summaries can distinguish deep from aggressive action profiles, but they are not continuous defensive positioning.

Defensive sequence involvement can include actions in possessions that regain and retain the ball, actions preceding a transition, or defensive contributions in possessions ending with a shot. The sequence windows and causal language must remain conservative.

### 11.4 Possession-adjusted defending

Possession-adjusted defensive metrics can reduce the opportunity bias created by team possession share. Candidate denominators include opponent possession segments, estimated out-of-possession minutes, or opponent on-ball actions. No single formula is universal; ScoutLabs must select and version a convention, then test its stability and interpretability.

### 11.5 What event data misses

Event data does not record every useful defensive position, cover shadow, screened lane, decoy press, line control, recovery run, marking decision, or denied option. A defender can make an important contribution without generating a recorded event. Off-ball defensive evaluation therefore remains rejected for the current data when presented as a measured fact.[^18]

## 12. Goalkeeping

Goalkeepers require a separate feature family and probably a separate similarity model. The StatsBomb schema distinguishes goalkeeper actions such as collected claims, punches, keeper-sweeper actions, shots faced, shots saved, goals conceded, penalty saves, smothers, and save techniques or body-part details. These distributions are functionally different from outfield-player profiles.[^5][^6]

### 12.1 Shot stopping

A defensible open-data baseline can compare goals conceded with pre-shot xG faced because shot events contain StatsBomb xG and can be linked to goalkeeper actions. Useful summaries include:

- shots on target faced;
- goals conceded;
- xG faced;
- goals conceded minus xG faced;
- save rate with shots-faced denominator;
- shot-location and xG distributions faced;
- penalty and non-penalty splits;
- body-part or shot-type context.

Goals conceded minus xG faced is not a post-shot goalkeeper model. It evaluates outcomes against pre-shot chance quality and is influenced by finishing, shot placement, defensive pressure, sample size, and model calibration.

### 12.2 Post-shot models

Proper post-shot xG or “goals prevented” models require information about the shot’s final trajectory, placement, velocity, or richer goalkeeper positioning. Those fields were not verified as universally available in the Open Data specifications. Commercial provider metrics must not be attributed to the open dataset. Classification: **Rejected for current data** unless a future field audit verifies the necessary source variables.

### 12.3 Claims, punches, and area control

Claims, punches, smothers, and keeper-sweeper actions can describe recorded area-control activity. Their volume depends heavily on team defensive style, crossing exposure, opponent behavior, and goalkeeper opportunity. They should be presented with contextual denominators where possible and not as complete command-of-area measures.

### 12.4 Sweeping

Sweeper actions, goalkeeper clearances, and defensive actions outside or near the penalty area can describe recorded sweeping involvement. Action height and location maps are useful. True starting position, readiness, and unrecorded interventions remain unavailable without tracking.

### 12.5 Distribution

Goalkeepers generate passes, goal kicks, throws, launches, switches, and other distributions. A goalkeeper profile should include:

- pass and launch volume;
- completion by length or type;
- short/medium/long distribution shares;
- goal-kick and open-play splits;
- distribution under recorded pressure;
- end-zone and recipient-zone maps;
- progression and retention outcomes.

Distribution must sit beside, not replace, shot-stopping and area-control features. A goalkeeper similarity score dominated by generic passing volume would be poor recruitment design; that is a ScoutLabs inference from the distinct functional event families.

### 12.6 Pressure and positioning context

The under-pressure flag can support distribution-under-pressure splits. Selective 360 frames may approximate nearby visible opponents or available visible teammates, but cannot recover complete passing lanes or continuous goalkeeper positioning. Goalkeeper context features derived from 360 should remain experimental and coverage-aware.

### 12.7 Separate similarity path

At minimum, goalkeepers need separate metrics and comparison groups. A dedicated goalkeeper similarity model is likely preferable because the football dimensions, denominators, and sample risks differ sharply from outfield players. This is classified as **Candidate requiring experiment** until validated through goalkeeper-specific cases.

## 13. Spatial analysis

Spatial analysis is an excellent fit for ScoutLabs when labels are accurate. The product brief correctly distinguishes action maps from continuous tracking heatmaps.

### 13.1 Coordinate normalization

StatsBomb uses a fixed 120-by-80 coordinate system, and open 360 frames follow the attacking orientation of the linked event.[^6][^7] ScoutLabs should normalize every event to a common attacking direction before computing progression, entries, centroids, widths, depths, or similarity. Coordinate transformations and pitch-zone definitions must be versioned.

### 13.2 Action maps

Strong MVP visualizations include:

- pass start/end maps and pass networks where identity and sample support them;
- carry start/end maps;
- shot maps weighted by xG or outcome;
- pressure maps;
- recovery and interception maps;
- goalkeeper action maps;
- zone-entry and transition maps.

These maps represent recorded event activity. They do not show where the player spent time between actions.

### 13.3 Reception approximations

Pass recipients and pass end locations can support “pass receipt” or “reception approximation” maps. They should not be called positioning heatmaps because the player may move before receiving, not every reception is observed identically, and off-ball locations between events are absent.

### 13.4 Tactical zones and grids

Tactical zones, fixed grids, pitch thirds, penalty-area subzones, central/half-space/wide bands, and custom role-aware areas can produce explainable spatial summaries. Every zone system should be documented and versioned. Multiple grids may be useful for experiments, but the user-facing product should avoid exposing an uncontrolled catalog of nearly redundant maps.

### 13.5 Spatial histograms and kernel density estimation

Spatial histograms are simple and suitable for similarity because each player can be represented by normalized action shares across zones. Kernel density estimation can create smoother visual distributions but is sensitive to bandwidth, sample size, and boundary treatment. KDE should primarily be a visualization or research representation, not a default production feature until stability is tested.

### 13.6 Zone transitions

Start-zone to end-zone vectors for passes and carries bridge direct metrics and spatial similarity. Examples include buildup-to-midfield passes, wide-to-box entries, central progression, switches, and defensive recoveries followed by forward actions. Zone transitions are promising because they remain interpretable while describing routes rather than isolated action locations. Classification: **Candidate requiring experiment** as a similarity channel; direct transition counts can enter the MVP after definition audit.

### 13.7 Centroids, width, and depth

Centroids, average width, and average depth computed from event locations describe the spatial distribution of recorded actions, not continuous team or player occupation. They can be useful descriptors when the event family is named explicitly, such as “median pass-start x” or “pressure-location width,” but generic “average position” labels would be misleading.

### 13.8 Spatial player similarity

Spatial similarity can compare normalized histograms, zone-transition vectors, earth-mover-like distances, cosine similarity, or other distribution distances. It is promising because players with similar totals may act in different areas. However, it should initially be an additive experimental channel rather than the primary ranking kernel. The experiment must show incremental football validity over direct metrics and must handle sparse samples and differing action volumes.

## 14. StatsBomb 360

StatsBomb 360 should be treated as a selective context enhancer, not a universal state-space layer. ScoutLabs local StatsBomb inventory, generated 24 July 2026, contains 426 three-sixty files for 3,961 matches. The official specification warns that frames are event-linked, not continuous; not every event is covered; not all 22 players are visible; visible-area polygons may be unavailable; non-actor identities are absent; and actor or goalkeeper flags can contain rare inconsistencies.[^7]

### 14.1 Raw fields that can be used responsibly

The verified raw frame structure supports:

- event UUID;
- visible-area polygon;
- visible-player locations;
- teammate/opponent relationship;
- actor flag;
- goalkeeper flag.

ScoutLabs must not attribute proprietary StatsBomb 360 metrics to Open Data.

### 14.2 Defensible derived features

For covered events, the raw frames can support:

- number of visible teammates;
- number of visible opponents;
- actor location;
- nearest visible opponent distance;
- nearest visible teammate distance;
- local visible-opponent density within a documented radius;
- local visible-teammate support within a documented radius;
- local numerical balance;
- number of visible passing options under a documented geometric rule;
- approximate free space around the actor;
- visible-area coverage ratio;
- whether a relevant zone was inside the camera-visible polygon;
- approximate pressure-context categories.

These features are geometrically derivable, but their football validity is not automatic. “Visible passing option,” for example, requires a rule for distance, angle, obstruction, teammate location, and whether the target lies inside the visible area. Without identity for non-actors, player-specific off-ball attribution is not possible.

### 14.3 Visible-area handling

The visible-area polygon is essential for avoiding false absence claims. An opponent outside the visible polygon is unobserved, not absent. Derived counts should therefore distinguish:

- visible count;
- visible-area coverage;
- whether the relevant search radius is fully visible;
- whether the frame is usable for the chosen feature.

Frames with inadequate visible area should be excluded from the relevant metric rather than converted to zero.

### 14.4 Pressure approximation

Nearest visible opponent and local density can approximate local pressure context at selected events. They do not measure pressing intensity, closing speed, body orientation, or future movement. The product language should use terms such as “visible nearby opponents” or “local visible density,” not “true pressure.”

### 14.5 Coverage and selection bias

Because 360 coverage is partial by match, competition, event, and camera view, player aggregates can become biased toward covered contexts. A 360-derived profile should show:

- number of eligible events;
- number and share with usable frames;
- competition and season coverage;
- visible-area usability rate;
- whether the metric is excluded from global similarity due to insufficient coverage.

### 14.6 Recommended product role

The best initial use is modest: contextual badges, example event explanations, selective 360 panels, and a small set of experimental features. Global player ranking should not depend heavily on sparse 360 coverage. Classification: **Candidate requiring experiment**.

## 15. Player-similarity approaches

ScoutLabs should research, not prematurely choose, a final production algorithm. The baseline family should be distance-based similarity on normalized, position-aware feature vectors because it is transparent and decomposable.[^27][^28]

### 15.1 Euclidean distance

Euclidean distance is simple and easy to decompose into per-feature squared differences. It works well when features are sensibly scaled and the geometry of the feature space is meaningful. It is sensitive to outliers, redundant variables, and high-dimensional concentration.

- **Scaling:** mandatory;
- **Correlated variables:** can double-count dimensions;
- **Missing values:** requires imputation, exclusion, or pairwise policy;
- **User weights:** straightforward;
- **Interpretability:** high;
- **Complexity:** low;
- **MVP suitability:** high as a baseline, not a final selection.

### 15.2 Weighted Euclidean distance

Weighted Euclidean distance allows dimension or feature families to reflect analyst priorities. It is directly decomposable and matches the product’s requirement that weights remain visible. The main risk is arbitrary or unstable weighting.

- **Scaling:** mandatory;
- **Correlated variables:** still problematic;
- **Missing values:** must preserve denominator fairness;
- **User weights:** excellent support;
- **Interpretability:** very high;
- **Complexity:** low;
- **MVP suitability:** strong baseline candidate.

### 15.3 Manhattan distance

Manhattan distance sums absolute differences. It is often less dominated by one extreme feature than squared Euclidean distance and remains easy to explain.

- **Scaling:** mandatory;
- **Correlated variables:** still double-counted;
- **Missing values:** explicit policy required;
- **User weights:** straightforward;
- **Interpretability:** high;
- **Complexity:** low;
- **MVP suitability:** strong baseline comparator.

### 15.4 Cosine similarity

Cosine similarity compares vector direction rather than absolute magnitude. It can emphasize profile shape, which may be useful after suitable normalization, but may treat two players with very different levels as similar if their relative metric pattern is alike.

- **Scaling:** still important, depending on vector construction;
- **Correlated variables:** unresolved;
- **Missing values:** difficult without consistent vectors;
- **User weights:** possible through transformed features;
- **Interpretability:** medium;
- **Complexity:** low;
- **MVP suitability:** useful experiment, not automatically preferable.

### 15.5 Mahalanobis distance

Mahalanobis distance accounts for covariance and can reduce double-counting from correlated variables. It is sensitive to covariance estimation, small positional cohorts, multicollinearity, and distribution shift.[^27]

- **Scaling:** embedded through covariance but preprocessing still matters;
- **Correlated variables:** explicit strength;
- **Missing values:** difficult;
- **User weights:** less intuitive;
- **Interpretability:** medium to low;
- **Complexity:** medium;
- **MVP suitability:** **Candidate requiring experiment**.

### 15.6 Nearest-neighbour retrieval

Nearest-neighbour methods provide a natural retrieval workflow once a distance function and candidate universe are defined. The algorithm does not validate the football meaning of the space; feature design, comparison groups, minutes, and weighting remain decisive.[^28]

For ScoutLabs, the output should preserve:

- reference profile;
- candidate universe and filters;
- normalized feature vector;
- distance metric;
- weights;
- missing-data policy;
- top contributing similarities and differences;
- model and metric-definition versions.

### 15.7 PCA

Principal component analysis can diagnose redundancy, visualize feature structure, and construct lower-dimensional research spaces.[^29] Components are linear combinations and are harder for analysts to interpret than direct football dimensions. PCA should therefore remain an internal research or diagnostic layer, not the default explanation space.

### 15.8 Clustering

Clustering can discover archetypes or substyles, especially within position groups. The progressive-pass clustering literature demonstrates practical, interpretable use of repeatable action clusters.[^21] Clustering is better suited to taxonomy, exploration, and validation than to replacing reference-player nearest-neighbour retrieval. Classification: **Research only** as a ranking engine; potentially useful as an exploratory aid.

### 15.9 Embeddings

Learned embeddings may capture nonlinear relationships, but they are less transparent, need substantial clean data, and often lack a direct metric-level explanation. For a recruitment MVP centered on analyst trust, embedding-heavy similarity should remain **Research only** unless it clearly outperforms transparent baselines and gains a defensible explanation layer.

### 15.10 Hybrid statistical-spatial similarity

A hybrid can combine direct statistical features with spatial histograms or zone-transition vectors. This addresses cases where totals look similar but action locations differ. It must be tested against simpler baselines, control for duplicated information, and expose the contribution of each channel. Classification: **Candidate requiring experiment**.

### 15.11 Missing values and coverage

Missing fields must never be silently treated as zeros. Candidate policies include:

- exclude metrics lacking adequate coverage for either profile;
- renormalize distance over common features with a visible coverage penalty;
- use explicit missingness indicators;
- impute only when the statistical and football assumptions are defensible;
- exclude candidates whose usable-feature coverage falls below a threshold.

The explanation must show which dimensions were omitted and how that affected the score.

### 15.12 Position-specific models

Position-compatible comparison groups are strongly recommended. Separate feature families or weights may be needed for centre-backs, full-backs, midfielders, wide attackers, forwards, and goalkeepers. However, rigid source positions can hide hybrid roles. Position groups should constrain the candidate universe while allowing analyst overrides and preserving mixed-position evidence.

## 16. Similarity-validation methods

Mathematical coherence does not prove football validity. A model can be internally consistent, stable, and still retrieve candidates that do not answer a recruitment question. Validation must combine numerical behavior, football face validity, and analyst usefulness.[^20]

### 16.1 Same-player different-season tests

Adjacent or comparable seasons of the same player are useful positive controls. When role and context remain broadly similar, those profiles should often appear among close neighbours. Failure may indicate poor scaling, excessive context sensitivity, feature instability, or an inappropriate candidate universe. Success is not conclusive because a player can genuinely change role or performance.

### 16.2 Expert assessment

Structured review by scouts or recruitment analysts is necessary. PlayeRank provides a precedent for comparing model outputs with professional scout evaluations.[^13] ScoutLabs should use predefined cases, consistent rating forms, and disagreement logging rather than informal anecdotal approval.

### 16.3 Known stylistic examples

Curated examples can test whether the model retrieves plausible styles. These examples should be documented before examining results to reduce confirmation bias. The purpose is not to create a circular “ground truth,” but to detect obvious feature or weighting failures.

### 16.4 Synthetic profiles

Synthetic profiles can isolate how a metric or dimension changes the ranking. For example, increasing only progression while holding other dimensions constant should produce predictable changes. Synthetic tests validate mechanics and explainability, not football truth.

### 16.5 Nearest-neighbour stability

Neighbour lists should be tested under:

- bootstrap or resampled matches;
- removal of a small number of fixtures;
- alternative minute thresholds;
- small weight perturbations;
- alternative scaling methods;
- alternative comparison groups;
- correlated-feature removal;
- missing-data scenarios.

Large ranking changes under small perturbations should be surfaced as instability rather than hidden.

### 16.6 Sensitivity to minutes

The same player’s profile can be recalculated at increasing minute checkpoints. Stable dimensions should converge; volatile metrics should remain flagged. This experiment can inform minimum-minute rules and reliability warnings.

### 16.7 Sensitivity to weights

Recommended weights should be compared with uniform weights, role-specific alternatives, and analyst-defined variants. The product should show when a candidate’s rank depends heavily on one dimension.

### 16.8 Sensitivity to comparison groups

The same reference player should be tested within position-specific, competition-specific, and broader multi-competition populations. Percentiles and neighbours may change because normalization changes. The interface must make that dependence visible.

### 16.9 Negative controls

Obviously dissimilar positions, synthetic noise profiles, randomized metric vectors, or deliberately incompatible role examples should not appear as top matches under normal settings. If they do, the model may be driven by generic activity volume or scaling artifacts.

### 16.10 Cluster consistency

If clustering is researched, stability across random seeds, samples, feature subsets, and seasons should be measured. A visually attractive cluster is not a valid football archetype unless it is repeatable and interpretable.

### 16.11 Recruitment case studies

Documented case studies should record the reference player, football question, candidate universe, exclusions, feature configuration, ranking, analyst review, and reasons for acceptance or rejection. Case studies should include negative or inconclusive outcomes.

### 16.12 Validation conclusion

No single test proves validity. A production candidate should demonstrate mechanical correctness, reasonable stability, expert plausibility, understandable explanations, and usefulness in narrowing a scouting search. Even then, similarity means statistical proximity under a configuration, not superiority, affordability, tactical fit, or transfer success.

## 17. Explainability

ScoutLabs should explain similarity at four levels:

1. **Global similarity:** overall score, candidate universe, metric version, and configuration.
2. **Dimensional similarity:** progression, creation, shooting, defending, pressing, possession security, or goalkeeping families.
3. **Metric-level contribution:** which observed features increased or decreased similarity.
4. **Limitations:** low minutes, missing fields, partial 360, excluded families, contextual bias, and unstable rankings.

This structure follows directly from the [ScoutLabs Product Brief](../../BRIEF.md) and is more appropriate for recruitment analysts than black-box explanation jargon.

### 17.1 Decomposable contributions

Weighted Euclidean, Manhattan, and similar transparent distances can be decomposed by metric and family. ScoutLabs can show whether similarity comes from passing volume, chance creation, carrying routes, action zones, or defensive interventions. The same panel should show the strongest differences, not only supporting evidence.

### 17.2 Ranking differences

When ScoutLabs ranking and analyst ranking differ, the product should preserve both. It should show the statistical reasons for the model order and allow the analyst to record a different judgment without overwriting the original output.

### 17.3 Custom weights

Custom weights must be visible in the result. The explanation should show default versus modified weights and how the ranking changed. Individual-metric weighting across a large catalog should be deferred until dimension-level control is validated, because excessive configurability can create accidental or post-hoc rankings.

### 17.4 Missing-data effects

The product should state:

- which metrics were unavailable;
- which dimensions were partially calculated;
- whether the score was renormalized;
- any coverage penalty;
- whether 360 context was excluded;
- whether two candidates were compared on different effective feature sets.

### 17.5 Sample reliability

Every profile should display minutes, appearances, starts, event denominators, and low-sample warnings. Reliability adjustments or shrinkage must be distinguished from raw values. A compact confidence or stability indicator may be useful only if its calculation is transparent.

### 17.6 Model-agnostic explanation

LIME and SHAP are established model-agnostic explanation methods.[^32][^33] They should not be default MVP requirements because the first responsibility is to choose methods whose mechanics are already understandable. They become relevant only if a more complex model demonstrates meaningful improvement over transparent baselines. Classification: **Research only** for the initial product.

## 18. Recruitment and data limitations

### 18.1 Team and tactical context

Observed event outputs are shaped by team possession, buildup structure, manager demands, teammate quality, opponent quality, game state, and role. A player may appear passive because the team has little possession, or highly progressive because the system channels most buildup through that player. Role-aware and methodological literature reinforces that isolated indicators rarely capture the complete football problem.[^13][^20]

### 18.2 Position labels

Source positions are useful grouping evidence, not complete tactical roles. Players can change position within a match, perform hybrid functions, or share a label while behaving differently. ScoutLabs should preserve position histories and use observable behavior to refine, not overwrite, source labels.

### 18.3 Competition strength

League-strength adjustment is unresolved and explicitly outside the current MVP. Cross-league comparisons must not imply equivalent opposition quality. A visible warning and analyst judgment are preferable to an opaque adjustment that has not been validated.

### 18.4 Sample and survivorship bias

The Open Data universe is historical and selective rather than a balanced representation of the global recruitment market. ScoutLabs local StatsBomb inventory, generated 24 July 2026, contains a mixture of competitions, seasons, tournaments, and historical matches. Candidate discovery is therefore limited to the actual covered universe. Players, teams, or leagues absent from the dataset cannot be assessed.

Survivorship bias also affects interpretation: players with sufficient minutes in well-covered competitions are more likely to appear in reliable comparisons than fringe, injured, youth, or lower-league players.

### 18.5 Opponent and teammate quality

Event metrics do not isolate player ability from the quality of teammates and opponents. A creator’s xA depends partly on team possession and shot selection; a defender’s intervention volume depends on opposition and team structure; a goalkeeper’s shots faced depend on defensive quality. Contextual splits can help but do not solve attribution.

### 18.6 Historical and schema coverage

Data versions and field availability may differ across matches. Provider fields can be conditional, missing, deprecated, or introduced in later data versions. Every metric requires field-level coverage auditing and a documented admission decision.

### 18.7 Missing recruitment information

StatsBomb Open Data does not provide a complete current view of:

- transfer fees or salary;
- contract dates;
- medical history;
- current injuries;
- personality and adaptation;
- training behavior;
- current availability;
- agent or ownership conditions;
- work permits;
- live video evidence;
- complete current squad context.

ScoutLabs is therefore an analytical first-screening and comparison tool, not a transfer-decision system. Similarity does not mean superiority, affordability, tactical fit, or readiness to sign.

## 19. Strong candidates for the MVP

The following are classified as **Strong candidate for MVP**:

1. **Player-team-season profiles** with visible team, competition, season, position mix, minutes, starts, and coverage warnings. This handles transfers and context better than player-only aggregation.
2. **Direct event metrics and rates** for passing, carrying, dribbling, shooting, recorded defending, pressures, and goalkeeper actions, subject to a field-level definition audit.[^5][^6]
3. **Totals, per-90 values, success rates, and denominators** shown together rather than relying on one normalized view.
4. **Position-aware comparison groups** with the exact comparison population shown beside percentiles.
5. **Documented spatial entries and action-zone summaries**, including final-third and penalty-area passes and carries.
6. **Provider-defined switches, crosses, cutbacks, through balls, shot assists, and goal assists**, with provider/source labels preserved.[^5][^6]
7. **Shooting and creation metrics**, including shots, non-penalty shots, StatsBomb xG, non-penalty xG, shot assists, and ScoutLabs-derived xA from linked shot xG.
8. **Recorded defensive-action metrics and locations**, provided they are not described as complete defensive quality.
9. **Event pressure and counterpress proxies**, explicitly labeled as recorded event activity rather than full pressing models.
10. **Goalkeeper-specific feature families** for pre-shot shot stopping, distribution, recorded claims/punches, sweeping, and action maps.
11. **Event-derived action maps and zone summaries**, labeled as event maps rather than tracking heatmaps.
12. **A decomposable nearest-neighbour baseline** using scaled, position-aware feature families, with weighted Euclidean and Manhattan included in the initial comparison set.[^27][^28]
13. **Global, dimensional, and metric-level explanations** showing both similarities and differences.
14. **Visible sample and coverage warnings**, including low minutes, small denominators, missing fields, partial 360, and cross-competition caveats.
15. **Separate ScoutLabs and analyst rankings**, with one preferred candidate and preserved decision rationale, as required by the product brief.
16. **Versioned metric definitions, comparison groups, and model configurations** so historical results remain reproducible.

These methods are strong candidates, not exempt from testing. Each metric still needs a clear football question, source fields, formula, denominator, coverage audit, comparison group, limitations, and product purpose.

## 20. Candidate methods requiring experiments

The following are classified as **Candidate requiring experiment**:

1. **xT-based action value features** for passing and carrying. They are compatible with event data and potentially intuitive, but model quality and incremental value must be quantified.[^9][^23]
2. **VAEP-based action value features.** The literature and reproducible tooling are strong, but explanation and validation are more demanding than for direct metrics.[^8][^12]
3. **Shrinkage or reliability adjustment** for low-minute and low-denominator profiles.
4. **Robust scaling versus z-scores versus percentile-based family aggregation.** The choice should be based on stability and analyst understanding.
5. **Possession-adjusted defensive metrics** using alternative denominators such as opponent possessions, opponent actions, or estimated out-of-possession minutes.
6. **Opportunity-adjusted progression or creation metrics** beyond simple attempts and success rates.
7. **Hybrid statistical-spatial similarity** combining direct metrics with spatial histograms or zone-transition vectors.
8. **Spatial distance alternatives** for activity distributions, including cosine or earth-mover-like comparisons.
9. **360-derived context features** such as nearest visible opponent, visible passing-option counts, local density, or local numerical balance, restricted to adequately visible frames.[^7]
10. **Mahalanobis distance and covariance-aware similarity**, especially where direct metrics are strongly correlated.[^27]
11. **Cosine similarity** as a shape-oriented comparator to Euclidean and Manhattan baselines.
12. **A dedicated goalkeeper similarity model**, rather than only goalkeeper-specific features.
13. **Position- or role-family default weights**, tested against uniform and analyst-modified weights.
14. **Reception approximations and spatial route features** as similarity inputs.
15. **Event-only line-breaking proxies**, provided they are labeled as approximations and compared against 360-supported subsets.
16. **Stability or reliability indicators** shown to users, only if their calculation can be explained.

A candidate should move toward the MVP only when it improves recruitment usefulness over a simpler alternative, remains understandable, and survives sensitivity testing.

## 21. Research-only methods

The following are classified as **Research only**:

1. **Atomic-SPADL and Atomic-VAEP as user-facing features.** They are reproducible and analytically interesting, but too granular for the initial explanation layer.[^12]
2. **Semi-Markov or temporal xT variants.** These are scientifically promising but more complex than current MVP needs.[^24]
3. **Cooperative or restricted-Shapley shot-action contribution models.** They are remote from the current explanation and validation baseline.[^25]
4. **Archetype clustering as a ranking engine.** Clustering is more appropriate for discovery and taxonomy than reference-player retrieval.[^21][^30]
5. **Embedding-heavy latent player representations** without a transparent decomposition layer.
6. **PCA components as user-facing football dimensions.** PCA is useful diagnostically, but its components are not inherently meaningful football concepts.[^29]
7. **KDE-based spatial similarity as the main retrieval method**, pending sample and bandwidth stability work.
8. **Tracking-inspired structural pass proxies** derived only from partial 360, until a reliable validation subset is established.[^26]
9. **Model-agnostic explainers such as LIME or SHAP** before a complex model demonstrates clear value over transparent baselines.[^32][^33]
10. **Football Manager terminology as evidence.** It may later inform tactical vocabulary or role hypotheses, but it is not scientific validation.

Research-only methods may be reproduced and documented, but should not be allowed to create an impression of validated product capability.

## 22. Deferred methods

The following are classified as **Deferred**:

1. **League-strength adjustment.** The product brief places it outside the initial MVP, and weak adjustment risks false equivalence.
2. **Full Role Fit scoring.** This needs a validated role ontology and observable behavioral definitions.
3. **Team Fit scoring.** This requires player profile, team style, tactical requirements, squad need, and contextual evidence beyond the current core.
4. **Spatial similarity as a primary first-class product surface.** It should be researched additively before becoming a central workflow.
5. **Large-catalog individual-metric weighting.** Dimension-level control should be validated first.
6. **External enrichment for contracts, injuries, finances, current squad, nationality, age, and licensed photographs.** These require separate sources, licensing, temporal validity, and provenance.
7. **Collaborative club workspaces, shared shortlists, permissions, and audit history**, as defined in later product phases.
8. **Automatic video clips and video-scouting workflows.** They require separate media sources and rights.
9. **Current or real-time recruitment coverage.** The initial source is historical Open Data.
10. **Potential, resale-value, or future-performance models.** These require broader outcomes, context, and careful ethical and methodological design.

Deferred does not mean rejected permanently; it means outside the current analytical foundation or data boundary.

## 23. Rejected methods for the current data

The following are classified as **Rejected for current data**:

1. **Tracking-grade pressure or pressing-intensity models** presented as current production metrics. They require continuous positional information.[^16][^17]
2. **Proper modern xPass or pass-difficulty models** requiring synchronized player locations and richer temporal context.[^15]
3. **Fully observed line-breaking or structural-disruption metrics** from event data alone.[^26]
4. **Off-ball defensive quality, support, screening, or tactical role-fit claims** presented as measured facts from event data.[^18]
5. **Continuous team shape, width, depth, compactness, or formation dynamics** inferred from sparse events or event-linked 360 frames.
6. **Post-shot xG or commercial goals-prevented metrics** without the verified trajectory and placement fields required to reproduce them.
7. **Complete goalkeeper positioning analysis** from event locations alone.
8. **Universal 360-based rankings** across players who do not share comparable frame coverage.
9. **Future-performance, potential, or resale-value prediction** in the current MVP.
10. **Definitive tactical suitability or transfer recommendations.** Similarity is not suitability or superiority.
11. **Event maps labeled as player-tracking heatmaps.** Recorded actions do not measure continuous occupation.
12. **Treating missing fields as zero** in rankings or similarity.
13. **Presenting provider-supplied commercial 360 metrics as if they existed in Open Data.**
14. **Using Football Manager as scientific evidence.**

Rejection protects the product from claims that the current data cannot support. These methods should be revisited only if ScoutLabs obtains richer data or a new validated evidence base.

## 24. Contested definitions

ScoutLabs should maintain a versioned metric-definition registry. At minimum, the following definitions are contested:

| Concept | Defensible alternatives | Current ScoutLabs position |
|---|---|---|
| Pass completion | Next touch by teammate; absence of explicit failure outcome; denominator excluding special outcomes | Adopt a documented StatsBomb-outcome rule after field audit; show denominator. |
| Forward pass | Any positive goalward x-change; minimum forward threshold; angle-based classification | Use explicit normalized geometry; test threshold variants. |
| Progressive pass | Wyscout 30/15/10-metre rule; fixed x-gain; zone advance; xT gain | One versioned MVP default after experiment; alternatives documented.[^21][^31] |
| Progressive carry | Wyscout-style distance-to-goal reduction; fixed advance; zone entry; xT gain | Same policy as progressive passes; provider-independent label.[^31] |
| Line-breaking pass | Passing an opponent line; structural disruption; bypass count; simplified vertical/zone proxy | Do not claim full line-breaking from events; proxy remains experimental.[^26] |
| Final-third pass | End point in final third; origin outside plus end/next touch inside | Prefer explicit outside-to-inside entry definition. |
| Penalty-area pass | End point in box; origin outside plus end/next touch inside | Prefer explicit outside-to-inside entry definition. |
| Switch | Provider flag; minimum lateral displacement; change of flank | Use StatsBomb provider flag in the MVP.[^5][^6] |
| Cross | Provider geometry; pass from wide zone toward penalty area; any aerial box delivery | Use StatsBomb provider flag; do not silently replace it.[^5][^6] |
| Cutback | Provider geometry; backward pass from byline/box; custom spatial heuristic | Use StatsBomb provider flag; document its source.[^5][^6] |
| Through ball | Provider technique; geometric pass behind defence; line-breaking proxy | Use StatsBomb technique field; keep structural claims separate.[^5][^6] |
| Key pass | Any final pass before a shot; pass creating a clear chance; provider-specific category | Do not merge key pass with shot assist; define the label used.[^31] |
| Shot assist | Last action before a teammate shot; provider-linked qualifying pass | Use StatsBomb shot-assist/link logic after edge-case audit. |
| Expected assists | Provider xA model; xG of linked assisted shots; pass-probability model | Recreate from linked StatsBomb shot xG and label derivation. |
| Pass difficulty | Event-only logistic model; tracking-based xPass; provider model | Proper tracking-based version rejected; event-only model experimental.[^15] |
| Pass value | xT gain; VAEP; direct sequence outcomes; EPV | Direct sequence metrics first; xT/VAEP experiments.[^8][^9][^22] |
| Carry retention | Team keeps possession at next event; within N events; until possession end | Audit alternatives and state event window. |
| Ball loss | Dispossessed only; dispossessed plus miscontrol; any possession-ending failed action | Maintain an explicit event taxonomy and denominator. |
| Pressure | Recorded StatsBomb Pressure event; under-pressure flag; tracking-derived pressure | Use event labels as proxies, never as full pressing intensity.[^6][^17] |
| Tackle won | Duel/Tackle outcome; possession won; no immediate opponent retention | Do not expose until provider taxonomy mapping is documented. |
| Possession-adjusted defending | Per opponent possession; per opponent on-ball action; per out-of-possession minute | Candidate experiment; formula must remain visible. |
| Goals above expected | Goals minus xG; non-penalty goals minus npxG; shrinkage-adjusted finishing | Show descriptive raw value with sample warning; no stable-talent claim. |
| Goalkeeper goals prevented | Goals conceded minus pre-shot xG faced; post-shot model residual | Use only a clearly labeled pre-shot baseline; do not call it post-shot goals prevented. |
| Average position | Mean event location; mean touch location; continuous tracking location | Use event-family-specific centroid labels, never generic tracking language. |
| Spatial similarity | Grid histogram distance; KDE distance; zone-transition similarity; learned embedding | Experimental additive channel; no final method selected. |

ScoutLabs should not attempt to eliminate all disagreement by declaring one universal football definition. The defensible approach is to choose a reproducible default for each admitted metric, identify prominent alternatives, preserve version history, and allow later experiments or club-specific preferences without rewriting historical results.

## 25. Recommended experiment backlog

Experiments should be versioned, reproducible, and evaluated against a simpler baseline. Each experiment must log the candidate universe, comparison group, source coverage, feature list, metric definitions, normalization, weights, missing-data policy, minute threshold, model version, and qualitative case review.

### Priority 1 — Data and metric admission

1. Audit every event family and conditional field across the local snapshot.
2. Derive starts, substitutions, extra-time minutes, Player On/Off cases, dismissals, and interrupted-match flags; compare against known match examples.
3. Audit pass outcomes and establish the pass-completion denominator.
4. Audit event links used for shot assists and recreated xA.
5. Audit carry, dribble, dispossession, miscontrol, and loss relationships.
6. Audit goalkeeper event taxonomy and shots-faced links.
7. Produce coverage tables by competition, season, match, event type, and field.

### Priority 2 — Baseline normalization and similarity

8. Compare StandardScaler-style z-scores, robust scaling, and percentile-based family aggregation.[^27]
9. Compare Euclidean, weighted Euclidean, Manhattan, cosine, and Mahalanobis on the same position-aware feature set.[^27][^28]
10. Measure nearest-neighbour overlap and rank correlation across scaling methods.
11. Test feature-family weighting versus individual-metric weighting.
12. Remove highly correlated or conceptually redundant metrics and measure ranking change.
13. Test pairwise missing-feature renormalization against explicit coverage penalties.

### Priority 3 — Reliability

14. Recalculate profiles at increasing minute checkpoints and measure feature convergence.
15. Test candidate eligibility thresholds by position family.
16. Compare raw rates, shrinkage-adjusted rates, and visible reliability penalties.
17. Bootstrap matches and measure neighbour-list stability.
18. Test percentage metrics under minimum-denominator rules.

### Priority 4 — Football validity

19. Run same-player different-season retrieval tests.
20. Create positive stylistic cases and negative controls before observing results.
21. Conduct structured expert review with consistent scoring criteria.
22. Record reasons experts accept or reject top candidates.
23. Test whether broad-position restrictions improve usefulness without hiding legitimate hybrid profiles.
24. Document inconclusive and negative findings.

### Priority 5 — Possession value

25. Reproduce a basic xT model on the available event data.[^9]
26. Evaluate xT calibration and ranking sensitivity by training population.[^23]
27. Reproduce VAEP through SPADL and compare direct metrics versus direct metrics plus VAEP.[^8][^12]
28. Run ablation studies to determine whether action-value features improve expert usefulness.
29. Compare xT, VAEP, and direct zone-entry features for overlap and redundancy.

### Priority 6 — Spatial similarity

30. Compare fixed-grid histograms, tactical-zone shares, and zone-transition vectors.
31. Test cosine, Manhattan, and distribution-aware distances on spatial features.
32. Measure stability under lower action samples.
33. Determine whether spatial features improve retrieval beyond direct metrics.
34. Test separate spatial channels for passes, carries, shots, pressures, and defensive actions.

### Priority 7 — StatsBomb 360

35. Produce event- and match-level frame coverage reports.
36. Validate visible-area polygon handling.
37. Define and test nearest-visible-opponent and local-density features.
38. Define visible-passing-option rules and reject frames with inadequate visibility.
39. Compare 360 context with event under-pressure tags where both exist.
40. Test whether 360 features improve explanations or merely reflect coverage differences.
41. Prevent 360 metrics from entering global similarity when coverage is inadequate.

### Priority 8 — Goalkeepers

42. Build goalkeeper-only feature families and comparison groups.
43. Test pre-shot xG faced, save-rate, claims, sweeping, and distribution stability.
44. Compare one generic similarity engine with a goalkeeper-specific model.
45. Develop goalkeeper case studies and negative controls.

## 26. Unresolved research questions

The following remain classified as **Unresolved**:

1. Which default distance metric produces the most useful and stable candidate lists after the final feature audit?
2. How should default dimension weights differ by positional group?
3. Should player-team-season always be the default when one team sample is very small?
4. How should combined player-season views aggregate multiple teams without hiding context?
5. What minimum-minute and minimum-opportunity policies are appropriate for each metric family?
6. Which reliability adjustment is understandable enough for analysts?
7. How much incremental recruitment value do xT and VAEP add after direct metrics and zone entries are included?
8. Does xT trained across the entire Open Data snapshot generalize sensibly across competitions and eras?
9. Which possession-adjusted defensive denominator is most defensible and stable?
10. Can an event-only line-breaking proxy provide useful information without misleading users?
11. How should mixed-position seasons enter position-specific comparison groups?
12. How much spatial detail improves similarity before sample noise dominates?
13. Should spatial and statistical similarities be combined into one score or shown as separate channels?
14. Which 360 features remain stable after visible-area and coverage filtering?
15. How much 360 coverage is enough for a player-level aggregate?
16. Can 360-derived context improve explanation without introducing competition-coverage bias?
17. What is the best validation protocol when expert opinions disagree?
18. How should ScoutLabs communicate ranking instability to non-data-scientist analysts?
19. Which metrics are sufficiently redundant that only one should be user-facing?
20. How should historical data-version differences affect comparison groups?
21. Can goalkeeper similarity be validated with the available shots-faced samples?
22. What documented case studies provide the strongest external evidence that statistical similarity helps real recruitment decisions?
23. How should a future league-strength adjustment be validated without creating false precision?
24. Which role terms from tactical literature can be translated into observable behavior without treating labels as formulas?
25. What new evidence would be required before any research-only method is promoted?

No unresolved question should be converted into an implicit production assumption.

## 27. Source-to-recommendation matrix

### R1

- **Recommendation ID:** R1
- **Recommendation:** Use player-team-season as the default profile unit with preserved position history.
- **Classification:** Strong candidate for MVP
- **Supporting sources:** [ScoutLabs Product Brief](../../BRIEF.md); PlayeRank.[^13]
- **Evidence level:** Level A/B plus ScoutLabs inference.
- **Compatibility with StatsBomb Open Data:** High.
- **Expected product value:** High.
- **Confidence:** High.
- **Limitations:** Tactical role remains only partially observed; small post-transfer samples can be unstable.
- **Required experiment or follow-up:** Validate presentation for multi-team and mixed-position seasons.

### R2

- **Recommendation ID:** R2
- **Recommendation:** Put direct event metrics and simple, accurately labeled spatial summaries into the MVP.
- **Classification:** Strong candidate for MVP
- **Supporting sources:** StatsBomb event and data specifications; product metric-admission criteria.[^5][^6]
- **Evidence level:** Level A.
- **Compatibility with StatsBomb Open Data:** Very high.
- **Expected product value:** High.
- **Confidence:** High.
- **Limitations:** Conditional fields and data-version differences require auditing; event maps are not continuous positioning.
- **Required experiment or follow-up:** Complete field coverage and taxonomy audit before metric admission.

### R3

- **Recommendation ID:** R3
- **Recommendation:** Use a decomposable nearest-neighbour baseline before more complex similarity models.
- **Classification:** Strong candidate for MVP
- **Supporting sources:** scikit-learn distance and nearest-neighbour documentation; product explainability requirements.[^27][^28]
- **Evidence level:** Level B/C.
- **Compatibility with StatsBomb Open Data:** High.
- **Expected product value:** High.
- **Confidence:** High that a transparent baseline is necessary; unresolved which distance is best.
- **Limitations:** Sensitive to scaling, feature redundancy, weights, and candidate population.
- **Required experiment or follow-up:** Compare Euclidean, weighted Euclidean, Manhattan, cosine, and Mahalanobis under stability and expert tests.

### R4

- **Recommendation ID:** R4
- **Recommendation:** Treat xT and VAEP as experimental enrichment, not default truth.
- **Classification:** Candidate requiring experiment
- **Supporting sources:** xT, VAEP, comparison literature, and xT-quality research.[^8][^9][^11][^23]
- **Evidence level:** Level A/D.
- **Compatibility with StatsBomb Open Data:** High.
- **Expected product value:** Medium to high.
- **Confidence:** Medium.
- **Limitations:** Training-population dependence, calibration, explanation complexity, and possible redundancy with direct progression metrics.
- **Required experiment or follow-up:** Reproduce both, conduct ablation studies, and assess expert usefulness.

### R5

- **Recommendation ID:** R5
- **Recommendation:** Recreate expected assists from linked shot xG rather than claim an unavailable proprietary xA field.
- **Classification:** Strong candidate for MVP
- **Supporting sources:** StatsBomb pass/shot linkage and xG schema; Wyscout definition comparison.[^5][^6][^31]
- **Evidence level:** Level A/B.
- **Compatibility with StatsBomb Open Data:** High.
- **Expected product value:** High.
- **Confidence:** High, subject to link audit.
- **Limitations:** Depends on precise shot-assist and related-event handling; reflects the provider’s shot xG model.
- **Required experiment or follow-up:** Verify all linked-shot, own-goal, deflection, set-piece, and missing-link edge cases.

### R6

- **Recommendation ID:** R6
- **Recommendation:** Keep 360-derived metrics experimental and never universalize them across uncovered players.
- **Classification:** Candidate requiring experiment
- **Supporting sources:** StatsBomb Open Data 360 Frames Specification; ScoutLabs local StatsBomb inventory, generated 24 July 2026.[^7]
- **Evidence level:** Level A.
- **Compatibility with StatsBomb Open Data:** Partial.
- **Expected product value:** Medium.
- **Confidence:** High.
- **Limitations:** Sparse coverage, event-linked snapshots, limited camera visibility, non-actor identities absent, and possible flag inconsistencies.
- **Required experiment or follow-up:** Coverage-weighted evaluation on usable frames only.

### R7

- **Recommendation ID:** R7
- **Recommendation:** Use recorded pressures and counterpress flags as event-level proxies, not full pressing models.
- **Classification:** Strong candidate for MVP for proxies; Rejected for current data for full pressing models
- **Supporting sources:** StatsBomb pressure definition; tracking-based pressure and counterpress literature.[^6][^16][^17]
- **Evidence level:** Level A.
- **Compatibility with StatsBomb Open Data:** Medium to high for proxies; low for full models.
- **Expected product value:** Medium.
- **Confidence:** High.
- **Limitations:** Misses unrecorded off-ball pressure, team shape, closing speed, and coordinated pressing behavior.
- **Required experiment or follow-up:** Test whether pressure-context splits add analyst value and remain stable.

### R8

- **Recommendation ID:** R8
- **Recommendation:** Give goalkeepers a separate feature family and test a separate similarity path.
- **Classification:** Strong candidate for MVP for features; Candidate requiring experiment for a separate model
- **Supporting sources:** StatsBomb goalkeeper and shot schema; product explainability goals.[^5][^6]
- **Evidence level:** Level A/C.
- **Compatibility with StatsBomb Open Data:** High for direct features.
- **Expected product value:** High.
- **Confidence:** Medium to high.
- **Limitations:** No verified open post-shot xG; sparse shots-faced samples; substantial team context.
- **Required experiment or follow-up:** Build goalkeeper-only validation cases and compare generic versus dedicated similarity.

### R9

- **Recommendation ID:** R9
- **Recommendation:** Preserve contested definitions explicitly and version them.
- **Classification:** Strong candidate for MVP
- **Supporting sources:** StatsBomb provider definitions; Wyscout glossary differences; product lineage requirements.[^5][^6][^31]
- **Evidence level:** Level A/B.
- **Compatibility with StatsBomb Open Data:** High.
- **Expected product value:** High.
- **Confidence:** High.
- **Limitations:** Additional documentation and migration work.
- **Required experiment or follow-up:** Create the metric-definition registry before exposing contested labels.

### R10

- **Recommendation ID:** R10
- **Recommendation:** Reject tracking-dependent claims in the current product unless they are clearly labeled approximations and validated.
- **Classification:** Rejected for current data
- **Supporting sources:** Expected-pass, pressure, counterpressing, off-ball, EPV, and structural-pass literature; product exclusions.[^15][^16][^17][^18][^22][^26]
- **Evidence level:** Level A.
- **Compatibility with StatsBomb Open Data:** Low for the proper methods.
- **Expected product value:** High because it prevents misleading claims.
- **Confidence:** High.
- **Limitations:** Restricts attractive tactical features and may disappoint users expecting tracking-grade analysis.
- **Required experiment or follow-up:** Revisit only if ScoutLabs later obtains continuous tracking or sufficiently rich contextual data.

## 28. Full bibliography

The bibliography below is deduplicated. All URLs were reviewed during the research process. Access date for every external source: **24 July 2026**.

1. **Hudl / StatsBomb.** *StatsBomb Open Data*. Official GitHub repository. https://github.com/hudl/open-data
2. **StatsBomb.** *Open Data Competitions Specification v2.0.0*. StatsBomb API specification, last updated 1 May 2019. https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Competitions%20v2.0.0.pdf
3. **StatsBomb.** *Open Data Matches Specification v3.0.0*. StatsBomb API specification, last updated 26 March 2019. https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Matches%20v3.0.0.pdf
4. **StatsBomb.** *Open Data Lineups Specification v2.0.0*. StatsBomb API specification, last updated 1 May 2019. https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Lineups%20v2.0.0.pdf
5. **StatsBomb.** *Open Data Events Specification v4.0.0*. StatsBomb API specification, last updated 8 May 2019. https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Events%20v4.0.0.pdf
6. **StatsBomb.** *StatsBomb Data Specification v1.1*. StatsBomb Data Specification, last updated 13 May 2019. https://github.com/hudl/open-data/blob/master/doc/StatsBomb%20Open%20Data%20Specification%20v1.1.pdf
7. **StatsBomb.** *Open Data 360 Frames Specification v1.0.0*. StatsBomb API specification, last updated 17 November 2021. https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20360%20Frames%20v1.0.0%20%281%29.pdf
8. **Decroos, Tom; Bransen, Lotte; Van Haaren, Jan; Davis, Jesse.** “Actions Speak Louder Than Goals: Valuing Player Actions in Soccer.” *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 2019. DOI: 10.1145/3292500.3330758. https://doi.org/10.1145/3292500.3330758
9. **Singh, Karun.** “Introducing Expected Threat (xT).” Method-author technical essay, 2019. https://karun.in/blog/expected-threat.html
10. **Bransen, Lotte; Van Haaren, Jan.** “Measuring Soccer Players’ Contributions to Chance Creation by Valuing Their Passes.” *Journal of Quantitative Analysis in Sports*, 2020. DOI: 10.1515/jqas-2018-0020. https://doi.org/10.1515/jqas-2018-0020
11. **Van Roy, Maxim; Robberechts, Pieter; Decroos, Tom; Davis, Jesse.** “Valuing On-the-Ball Actions in Soccer: A Critical Comparison of xT and VAEP.” Workshop paper, 2020. https://eos.cs.kuleuven.be/sites/eos.cs.kuleuven.be/files/xt-vs-vaep-aits.pdf
12. **KU Leuven DTAI.** *socceraction: Convert soccer event stream data to SPADL and value actions with xT, VAEP and Atomic-VAEP*. Official documentation and repository. https://socceraction.readthedocs.io/en/stable/ and https://github.com/ML-KULeuven/socceraction
13. **Pappalardo, Luca; Cintia, Paolo; Ferragina, Paolo; Massucco, Emanuele; Pedreschi, Dino; Giannotti, Fosca.** “PlayeRank: Data-Driven Performance Evaluation and Player Ranking in Soccer via a Machine Learning Approach.” *ACM Transactions on Intelligent Systems and Technology*, 2019. DOI: 10.1145/3343172. https://doi.org/10.1145/3343172
14. **Goes, Floris R.; Kempe, Matthias; Meerhoff, Laurentius A.; Lemmink, Koen A. P. M.** “Not Every Pass Can Be an Assist: A Data-Driven Model to Measure Pass Effectiveness in Professional Soccer Matches.” *Big Data*, 2019. DOI: 10.1089/big.2018.0067. https://doi.org/10.1089/big.2018.0067
15. **Anzer, Gabriel; Bauer, Pascal.** “Expected Passes: Determining the Difficulty of a Pass in Football Using Spatio-Temporal Data.” *Data Mining and Knowledge Discovery*, 2022. DOI: 10.1007/s10618-021-00810-3. https://doi.org/10.1007/s10618-021-00810-3
16. **Bauer, Pascal; Anzer, Gabriel.** “Data-Driven Detection of Counterpressing in Professional Football.” *Data Mining and Knowledge Discovery*, 2021. DOI: 10.1007/s10618-021-00763-7. https://doi.org/10.1007/s10618-021-00763-7
17. **Andrienko, Gennady; Andrienko, Natalia; Budziak, Grzegorz; Dykes, Jason; Fuchs, Georg; von Landesberger, Tatiana; Weber, Hendrik.** “Visual Analysis of Pressure in Football.” *Data Mining and Knowledge Discovery*, 2017. DOI: 10.1007/s10618-017-0513-2. https://doi.org/10.1007/s10618-017-0513-2
18. **Wu, Lucas; Swartz, Tim.** “Evaluation of Off-the-Ball Actions in Soccer.” *Statistica Applicata – Italian Journal of Applied Statistics*, 2023. DOI: 10.26398/IJAS.0035-008. https://doi.org/10.26398/IJAS.0035-008
19. **Wakelam, Edward; Steuber, Verena; Wakelam, James.** “The Collection, Analysis and Exploitation of Footballer Attributes: A Systematic Review.” *Journal of Sports Analytics*, 2022. DOI: 10.3233/JSA-200554. https://doi.org/10.3233/JSA-200554
20. **Bergkamp, Tom L. G.; Niessen, A. Susan M.; den Hartigh, Ruud J. R.; Frencken, Wouter G. P.; Meijer, Rob R.** “Methodological Issues in Soccer Talent Identification Research.” *Sports Medicine*, 2019. DOI: 10.1007/s40279-019-01113-w. https://doi.org/10.1007/s40279-019-01113-w
21. **Deb, B.; Fernandez-Navarro, J.; McRobert, A. P.; Jarman, I.** “Finding Repeatable Progressive Pass Clusters and Application in International Football.” *Journal of Sports Analytics*, 2024. DOI: 10.3233/JSA-220732. https://doi.org/10.3233/JSA-220732
22. **Fernández, Javier; Bornn, Luke; Cervone, Dan.** “A Framework for the Fine-Grained Evaluation of the Instantaneous Expected Value of Soccer Possessions.” *Machine Learning*, 2021. DOI: 10.1007/s10994-021-05989-6. https://doi.org/10.1007/s10994-021-05989-6
23. **van Arem, K. et al.** “Model Quality in Football: Quantifying the Quality of an Expected Threat Model.” arXiv preprint, 2026. DOI: 10.48550/arXiv.2604.21087. https://doi.org/10.48550/arXiv.2604.21087
24. **Le Coz, S.; Boustila, F.; Imbach, F.** “A Semi-Markov Framework for Modeling Football Possessions and Temporal Expected Threat.” *Scientific Reports*, 2026. DOI: 10.1038/s41598-026-52938-1. https://doi.org/10.1038/s41598-026-52938-1
25. **Cefis, M.; Metulini, R.; Carpita, M.** “A Model-Based Restricted Shapley Value to Measure the Players’ Contribution to Shot Actions in Football.” *Computational Statistics*, 2026. DOI: 10.1007/s00180-026-01783-x. https://doi.org/10.1007/s00180-026-01783-x
26. **Karakuş, Oktay; Arkadaş, Hasan.** “Structural Pass Analysis in Football: Learning Pass Archetypes and Tactical Impact from Spatio-Temporal Tracking Data.” arXiv preprint, 2026. DOI: 10.48550/arXiv.2603.28916. https://doi.org/10.48550/arXiv.2603.28916
27. **scikit-learn developers.** *pairwise_distances — scikit-learn API documentation*. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html
28. **scikit-learn developers.** *Nearest Neighbors — scikit-learn User Guide*. https://scikit-learn.org/stable/modules/neighbors.html
29. **scikit-learn developers.** *PCA — scikit-learn API documentation*. https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
30. **scikit-learn developers.** *KMeans — scikit-learn API documentation*. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
31. **Hudl Wyscout.** *Wyscout Data Glossary*. Entries reviewed for progressive pass, progressive run, pass into final third, pass into penalty area, key pass, shot assist, and through pass. https://dataglossary.wyscout.com/
32. **Ribeiro, Marco Tulio; Singh, Sameer; Guestrin, Carlos.** “‘Why Should I Trust You?’ Explaining the Predictions of Any Classifier.” *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016. DOI: 10.1145/2939672.2939778. https://doi.org/10.1145/2939672.2939778
33. **Lundberg, Scott M.; Lee, Su-In.** “A Unified Approach to Interpreting Model Predictions.” *Advances in Neural Information Processing Systems 30*, 2017. https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html

### Local ScoutLabs sources

- [ScoutLabs Product Brief](../../BRIEF.md)
- [ScoutLabs data-source documentation](../data-source.md)
- ScoutLabs local StatsBomb inventory, generated 24 July 2026.

[^1]: Hudl / StatsBomb, *StatsBomb Open Data*, official GitHub repository, continuously maintained; stable URL: https://github.com/hudl/open-data; accessed 24 July 2026.
[^2]: StatsBomb, *Open Data Competitions Specification v2.0.0*, StatsBomb API specification, last updated 1 May 2019; stable URL: https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Competitions%20v2.0.0.pdf; accessed 24 July 2026.
[^3]: StatsBomb, *Open Data Matches Specification v3.0.0*, StatsBomb API specification, last updated 26 March 2019; stable URL: https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Matches%20v3.0.0.pdf; accessed 24 July 2026.
[^4]: StatsBomb, *Open Data Lineups Specification v2.0.0*, StatsBomb API specification, last updated 1 May 2019; stable URL: https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Lineups%20v2.0.0.pdf; accessed 24 July 2026.
[^5]: StatsBomb, *Open Data Events Specification v4.0.0*, StatsBomb API specification, last updated 8 May 2019; stable URL: https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20Events%20v4.0.0.pdf; accessed 24 July 2026.
[^6]: StatsBomb, *StatsBomb Data Specification v1.1*, StatsBomb Data Specification, last updated 13 May 2019; stable URL: https://github.com/hudl/open-data/blob/master/doc/StatsBomb%20Open%20Data%20Specification%20v1.1.pdf; accessed 24 July 2026.
[^7]: StatsBomb, *Open Data 360 Frames Specification v1.0.0*, StatsBomb API specification, last updated 17 November 2021; stable URL: https://github.com/hudl/open-data/blob/master/doc/Open%20Data%20360%20Frames%20v1.0.0%20%281%29.pdf; accessed 24 July 2026.
[^8]: Tom Decroos, Lotte Bransen, Jan Van Haaren, and Jesse Davis, “Actions Speak Louder Than Goals: Valuing Player Actions in Soccer,” *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 2019, DOI: 10.1145/3292500.3330758; stable URL: https://doi.org/10.1145/3292500.3330758; accessed 24 July 2026.
[^9]: Karun Singh, “Introducing Expected Threat (xT),” method-author technical essay, 2019; stable URL: https://karun.in/blog/expected-threat.html; accessed 24 July 2026.
[^10]: Lotte Bransen and Jan Van Haaren, “Measuring Soccer Players’ Contributions to Chance Creation by Valuing Their Passes,” *Journal of Quantitative Analysis in Sports*, 2020, DOI: 10.1515/jqas-2018-0020; stable URL: https://doi.org/10.1515/jqas-2018-0020; accessed 24 July 2026.
[^11]: Maxim Van Roy, Pieter Robberechts, Tom Decroos, and Jesse Davis, “Valuing On-the-Ball Actions in Soccer: A Critical Comparison of xT and VAEP,” workshop paper, 2020; stable URL: https://eos.cs.kuleuven.be/sites/eos.cs.kuleuven.be/files/xt-vs-vaep-aits.pdf; accessed 24 July 2026.
[^12]: KU Leuven DTAI, *socceraction: Convert Soccer Event Stream Data to SPADL and Value Actions with xT, VAEP and Atomic-VAEP*, official documentation and repository; stable URLs: https://socceraction.readthedocs.io/en/stable/ and https://github.com/ML-KULeuven/socceraction; accessed 24 July 2026.
[^13]: Luca Pappalardo, Paolo Cintia, Paolo Ferragina, Emanuele Massucco, Dino Pedreschi, and Fosca Giannotti, “PlayeRank: Data-Driven Performance Evaluation and Player Ranking in Soccer via a Machine Learning Approach,” *ACM Transactions on Intelligent Systems and Technology*, 2019, DOI: 10.1145/3343172; stable URL: https://doi.org/10.1145/3343172; accessed 24 July 2026.
[^14]: Floris R. Goes, Matthias Kempe, Laurentius A. Meerhoff, and Koen A. P. M. Lemmink, “Not Every Pass Can Be an Assist: A Data-Driven Model to Measure Pass Effectiveness in Professional Soccer Matches,” *Big Data*, 2019, DOI: 10.1089/big.2018.0067; stable URL: https://doi.org/10.1089/big.2018.0067; accessed 24 July 2026.
[^15]: Gabriel Anzer and Pascal Bauer, “Expected Passes: Determining the Difficulty of a Pass in Football Using Spatio-Temporal Data,” *Data Mining and Knowledge Discovery*, 2022, DOI: 10.1007/s10618-021-00810-3; stable URL: https://doi.org/10.1007/s10618-021-00810-3; accessed 24 July 2026.
[^16]: Pascal Bauer and Gabriel Anzer, “Data-Driven Detection of Counterpressing in Professional Football,” *Data Mining and Knowledge Discovery*, 2021, DOI: 10.1007/s10618-021-00763-7; stable URL: https://doi.org/10.1007/s10618-021-00763-7; accessed 24 July 2026.
[^17]: Gennady Andrienko et al., “Visual Analysis of Pressure in Football,” *Data Mining and Knowledge Discovery*, 2017, DOI: 10.1007/s10618-017-0513-2; stable URL: https://doi.org/10.1007/s10618-017-0513-2; accessed 24 July 2026.
[^18]: Lucas Wu and Tim Swartz, “Evaluation of Off-the-Ball Actions in Soccer,” *Statistica Applicata – Italian Journal of Applied Statistics*, 2023, DOI: 10.26398/IJAS.0035-008; stable URL: https://doi.org/10.26398/IJAS.0035-008; accessed 24 July 2026.
[^19]: Edward Wakelam, Verena Steuber, and James Wakelam, “The Collection, Analysis and Exploitation of Footballer Attributes: A Systematic Review,” *Journal of Sports Analytics*, 2022, DOI: 10.3233/JSA-200554; stable URL: https://doi.org/10.3233/JSA-200554; accessed 24 July 2026.
[^20]: Tom L. G. Bergkamp, A. Susan M. Niessen, Ruud J. R. den Hartigh, Wouter G. P. Frencken, and Rob R. Meijer, “Methodological Issues in Soccer Talent Identification Research,” *Sports Medicine*, 2019, DOI: 10.1007/s40279-019-01113-w; stable URL: https://doi.org/10.1007/s40279-019-01113-w; accessed 24 July 2026.
[^21]: B. Deb, J. Fernandez-Navarro, A. P. McRobert, and I. Jarman, “Finding Repeatable Progressive Pass Clusters and Application in International Football,” *Journal of Sports Analytics*, 2024, DOI: 10.3233/JSA-220732; stable URL: https://doi.org/10.3233/JSA-220732; accessed 24 July 2026.
[^22]: Javier Fernández, Luke Bornn, and Dan Cervone, “A Framework for the Fine-Grained Evaluation of the Instantaneous Expected Value of Soccer Possessions,” *Machine Learning*, 2021, DOI: 10.1007/s10994-021-05989-6; stable URL: https://doi.org/10.1007/s10994-021-05989-6; accessed 24 July 2026.
[^23]: K. van Arem et al., “Model Quality in Football: Quantifying the Quality of an Expected Threat Model,” arXiv preprint, 2026, DOI: 10.48550/arXiv.2604.21087; stable URL: https://doi.org/10.48550/arXiv.2604.21087; accessed 24 July 2026.
[^24]: S. Le Coz, F. Boustila, and F. Imbach, “A Semi-Markov Framework for Modeling Football Possessions and Temporal Expected Threat,” *Scientific Reports*, 2026, DOI: 10.1038/s41598-026-52938-1; stable URL: https://doi.org/10.1038/s41598-026-52938-1; accessed 24 July 2026.
[^25]: M. Cefis, R. Metulini, and M. Carpita, “A Model-Based Restricted Shapley Value to Measure the Players’ Contribution to Shot Actions in Football,” *Computational Statistics*, 2026, DOI: 10.1007/s00180-026-01783-x; stable URL: https://doi.org/10.1007/s00180-026-01783-x; accessed 24 July 2026.
[^26]: Oktay Karakuş and Hasan Arkadaş, “Structural Pass Analysis in Football: Learning Pass Archetypes and Tactical Impact from Spatio-Temporal Tracking Data,” arXiv preprint, 2026, DOI: 10.48550/arXiv.2603.28916; stable URL: https://doi.org/10.48550/arXiv.2603.28916; accessed 24 July 2026.
[^27]: scikit-learn developers, *pairwise_distances — scikit-learn API Documentation*; stable URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html; accessed 24 July 2026.
[^28]: scikit-learn developers, *Nearest Neighbors — scikit-learn User Guide*; stable URL: https://scikit-learn.org/stable/modules/neighbors.html; accessed 24 July 2026.
[^29]: scikit-learn developers, *PCA — scikit-learn API Documentation*; stable URL: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html; accessed 24 July 2026.
[^30]: scikit-learn developers, *KMeans — scikit-learn API Documentation*; stable URL: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html; accessed 24 July 2026.
[^31]: Hudl Wyscout, *Wyscout Data Glossary*, entries reviewed for progressive pass, progressive run, pass into final third, pass into penalty area, key pass, shot assist, and through pass; stable URL: https://dataglossary.wyscout.com/; accessed 24 July 2026.
[^32]: Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin, “‘Why Should I Trust You?’ Explaining the Predictions of Any Classifier,” *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, DOI: 10.1145/2939672.2939778; stable URL: https://doi.org/10.1145/2939672.2939778; accessed 24 July 2026.
[^33]: Scott M. Lundberg and Su-In Lee, “A Unified Approach to Interpreting Model Predictions,” *Advances in Neural Information Processing Systems 30*, 2017; stable URL: https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html; accessed 24 July 2026.
