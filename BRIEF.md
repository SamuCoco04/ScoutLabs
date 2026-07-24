# ScoutLabs — Product Brief

**Status:** Approved foundation
**Version:** 1.0
**Owner:** Samuel Coco
**Language:** English
**Last updated:** 24 July 2026

---

## 1. Product statement

**ScoutLabs is an explainable football recruitment analytics platform that helps analysts discover, compare, rank and shortlist players using event data.**

Its primary workflow allows an analyst to select a reference player and season, find statistically similar alternativend organize the final decision in a structured shortlist.

---

## 2. Executive summary

Football event data contains valuable information about how players participate in possession, progression, chance creation, finishing, defending, pressing and transitions.

However, raw event files do not directly answer recruitment questions such as:

* Which players resemble a specific footballer?
* Which candidates could be investigated as possible replacements?
* Where are two apparently similar players meaningfully different?
* Which metrics explain a recommendation?
* How reliable is a comparison given the available minutes and data coverage?
* Which alternatives were considered before selecting the preferred candidate?

ScoutLabs transforms open football event data into an analytical workflow for the first stage of recruitment.

The platform will initially use StatsBomb Open Data. Its coverage and contextual information are more limited than those available to professional clubs through commercial providers and internal scouting systems. ScoutLabs will not conceal this limitation or present its results as final recruitment decisions.

Instead, the project will demonstrate how far a rigorous, reproducible and professionally designed scouting platform can go with the available information.

ScoutLabs is a decision-support tool. It does not replace video scouting, tactical analysis, live observation, medical assessment, personality evaluation, contractual research or the judgement of recruitment professionals.

---

## 3. Problem

A recruitment analyst trying to identify possible replacements or comparable players must normally combine several disconnected tasks:

1. Locate an appropriate set of candidates.
2. Process raw match and event data.
3. Calculate consistent player metrics.
4. account for minutes played and sample size.
5. Define meaningful comparison groups.
6. Normalize values across players.
7. Select metrics relevant to the footballing question.
8. Interpret spatial and contextual differences.
9. Compare multiple candidates.
10. Preserve the reasoning behind a final shortlist.

Without a specialized workflow, this process is time-consuming, difficult to reproduce and vulnerable to misleading comparisons.

Traditional aggregate statistics can also obscure important context. Two players may record similar totals while operating in different areas, performing different actions or playing under substantially different conditions.

At the opposite extreme, complex models may produce attractive rankings without explaining how they were generated or whether the underlying data supports the apparent precision.

ScoutLabs addresses this gap by combining:

* structured data processing;
* football-specific metrics;
* configurable comparison groups;
* explainable similarity;
* visual comparison;
* quality and coverage indicators;
* and analyst-controlled shortlists.

---

## 4. Vision

**Make data-assisted football recruitment understandable, traceable and reproducible.**

ScoutLabs should allow an analyst to understand not only the result of an analysis, but also:

* which source data was used;
* which players formed the candidate pool;
* which filters were applied;
* which metrics and dimensions were considered;
* how values were normalized;
* how each dimension contributed to the result;
* where the candidates differ;
* what information was unavailable;
* and which limitations affect the interpretation.

The long-term vision is to evolve from statistical similarity towards explainable compatibility with football roles, tactical systems, team styles and squad needs.

---

## 5. Product positioning

ScoutLabs is positioned as:

* an analytical first-screening tool;
* an explainable player discovery platform;
* a structured comparison environment;
* a portfolio-quality demonstration of football data engineering and software engineering;
* and a research platform for developing and validating football metrics.

ScoutLabs is not positioned as:

* an automatic transfer decision system;
* a replacement for professional scouting departments;
* a complete global player database;
* a source of definitive market, salary or contractual information;
* or a model that can determine whether a footballer will succeed at a club.

---

## 6. Product descriptor and message

### Brand descriptor

**ScoutLabs — Explainable football recruitment analytics**

### Primary product message

**Find, compare and shortlist football players with transparent, data-driven analysis.**

---

## 7. Project objectives

### 7.1 Product objective

Help a recruitment analyst perform an initial screening of possible alternatives, replacements and comparable player profiles.

### 7.2 Analytical objective

Develop player metrics and similarity methods that are:

* reproducible;
* explainable;
* position-aware;
* conscious of sample size;
* traceable to source data;
* and explicit about their limitations.

### 7.3 Data objective

Systematically investigate every dataset, entity, event type and documented field available in the initial source.

Every field must be evaluated and assigned an analytical, operational or explicitly excluded purpose.

### 7.4 Technical objective

Build a complete product that demonstrates:

* ingestion of external event data;
* data normalization;
* data-quality validation;
* analytical feature engineering;
* metric calculation;
* similarity and recommendation methods;
* persistent application workflows;
* API design;
* analytical visualization;
* automated testing;
* continuous integration;
* and deployment.

### 7.5 Portfolio objective

Demonstrate to football clubs and relevant technology companies the ability to:

* understand a real football problem;
* research the domain before implementation;
* transform raw data into a useful product;
* define and validate football metrics;
* create explainable analytical models;
* design a professional interface;
* document technical and product decisions;
* and use AI-assisted development while retaining human control over scope, methodology and quality.

---

## 8. Primary user

The primary user is a **recruitment analyst or scouting analyst**.

This user:

* understands football and common performance indicators;
* needs to reduce a broad player pool to a manageable set of candidates;
* may already have one or more candidate names;
* does not need to be a data scientist;
* needs to justify why a player deserves further investigation;
* expects to inspect the evidence behind a recommendation;
* and uses data as one input within a broader recruitment process.

The platform will initially support an individual analytical workflow rather than a collaborative club-wide process.

---

## 9. Primary job to be done

> When a team needs an alternative, replacement or comparable profile for a player, the analyst wants to identify plausible candidates, understand their similarities and differences, rank them according to their own judgement and create a structured shortlist for further scouting.

Secondary jobs include:

* comparing candidates already identified elsewhere;
* exploring players through filters and metrics;
* finding leaders in a specific analytical dimension;
* studying a player’s profile;
* comparing different seasons of the same player;
* analyzing where players perform their actions;
* and preserving why candidates were selected, downgraded or rejected.

---

## 10. Product principles

### 10.1 The analyst remains in control

ScoutLabs may suggest filters, dimensions and weights, but the analyst must be able to inspect and modify the criteria that materially affect a result.

### 10.2 Explain before persuading

A recommendation must be accompanied by evidence. A lower but understandable level of complexity is preferable to an opaque score that cannot be defended.

### 10.3 Similarity does not mean superiority

A player with a high similarity score is statistically close to the reference profile under a specific configuration. This does not mean that the player is better, cheaper, tactically suitable or ready to be signed.

### 10.4 The application does not make the final decision

ScoutLabs produces an application ranking. The analyst may create a different manual ranking and select a preferred candidate who was not ranked first by the model.

### 10.5 Percentiles require context

Every percentile must be associated with a clearly defined comparison group.

### 10.6 Avoid false precision

Scores and percentages must not imply more confidence than the data, sample size and methodology justify.

### 10.7 Limitations are part of the result

Missing files, partial coverage, low minutes, unavailable contextual data and methodological limitations must remain visible.

### 10.8 Preserve source and provenance

Provider-supplied data, normalized data and ScoutLabs-derived information must remain distinguishable.

### 10.9 Research before adoption

Metrics and models must be investigated, reproduced and validated before being treated as reliable product features.

### 10.10 Document negative results

An experiment that produces unreliable, redundant or uninterpretable information must be documented rather than silently discarded.

### 10.11 Data supports judgement

ScoutLabs narrows and structures a search. It does not replace football knowledge, contextual analysis or human judgement.

---

## 11. Main product areas

The MVP will contain four primary areas.

### 11.1 Discover

Discover will provide three entry points.

#### Similar Players

Select a reference player and generate a ranked set of statistically similar candidates.

#### Player Explorer

Search and filter the available player population without requiring a reference player.

#### Metric Leaders

Discover players who stand out in selected metrics or analytical dimensions without presenting them as complete tactical roles.

Examples may include:

* ball progression;
* chance creation;
* goal threat;
* possession security;
* defensive activity;
* pressing activity;
* or other validated dimensions.

### 11.2 Player Profile

Inspect the statistical, spatial and contextual profile of a player for a selected season and team.

### 11.3 Compare

Compare between two and four player-season profiles, including different seasons of the same player.

### 11.4 Shortlists

Create named recruitment shortlists, organize candidates, select a preferred option and preserve the reasoning behind the analyst’s decision.

---

## 12. Core MVP workflow

### 12.1 Select the reference profile

The analyst searches for and selects:

* a player;
* a season;
* the relevant team when the player represented more than one;
* and the position or positional group to analyze.

A statistical profile is defined by its context. It is not only the permanent identity of the player.

### 12.2 Review the reference profile

Before generating recommendations, the analyst can inspect:

* appearances;
* minutes;
* positions;
* key metrics;
* analytical dimensions;
* data coverage;
* and important warnings.

### 12.3 Configure the candidate universe

The analyst can configure:

* competitions;
* seasons;
* compatible positions;
* minimum minutes;
* included or excluded teams;
* and other validated filters supported by the dataset.

### 12.4 Select the analysis mode

#### Recommended mode

ScoutLabs proposes a validated configuration based on the player’s positional group.

The recommended configuration includes:

* analytical dimensions;
* default weights;
* minimum sample rules;
* and compatible candidate positions.

#### Custom mode

The analyst can modify:

* active analytical dimensions;
* dimension weights;
* candidate positions;
* minimum minutes;
* competitions;
* seasons;
* and other supported filters.

The first MVP will prioritize dimension-level control rather than exposing every individual metric as a separate weight.

### 12.5 Generate similar players

ScoutLabs returns an ordered set of candidates with:

* an overall similarity score;
* similarity by dimension;
* strongest similarities;
* most important differences;
* data-coverage indicators;
* sample-size warnings;
* and the comparison configuration.

### 12.6 Investigate candidates

The analyst opens candidate profiles and inspects:

* minutes and appearances;
* totals and normalized metrics;
* percentiles;
* spatial distributions;
* action maps;
* strengths;
* differences from the reference player;
* and relevant limitations.

### 12.7 Compare candidates

The analyst compares between two and four player-season profiles using:

* metric tables;
* percentiles;
* analytical dimensions;
* comparative visualizations;
* action maps;
* absolute and relative differences;
* data coverage;
* and sample warnings.

One player may be selected as the visual reference for the comparison.

### 12.8 Create a shortlist

The analyst creates a named shortlist and adds the candidates that deserve further investigation.

### 12.9 Rank and select candidates

ScoutLabs preserves two independent rankings:

* **ScoutLabs rank:** generated by the analytical configuration;
* **Analyst rank:** manually defined by the user.

The analyst can select one candidate as the **Preferred candidate**.

The preferred candidate becomes the shortlist’s main visual identity or cover. The other candidates remain visible as alternatives that were considered during the process.

---

## 13. Shortlist model

Each shortlist will contain:

* name;
* optional description;
* reference player;
* reference season and team;
* original search configuration;
* creation date;
* last modification date;
* candidates;
* ScoutLabs rank;
* analyst rank;
* candidate status;
* preferred candidate;
* analyst notes;
* reason for inclusion;
* and reason for rejection or downgrade when recorded.

### 13.1 Candidate statuses

The initial statuses will be:

* **Preferred**
* **Strong alternative**
* **Under review**
* **Rejected**

### 13.2 Preferred candidate

A shortlist can have one preferred candidate.

The preferred candidate:

* is selected by the analyst;
* does not have to be the first ScoutLabs result;
* appears as the main shortlist candidate;
* and visually represents the shortlist.

### 13.3 Alternatives

Alternative candidates remain ordered from strongest to weakest according to the analyst.

Their original ScoutLabs ranking must remain available for comparison.

### 13.4 Rejected candidates

Rejected candidates may remain in the shortlist history with an optional reason.

This helps preserve the analysis already performed and avoids reconsidering the same candidate without context.

---

## 14. Player profile scope

A player profile in the MVP should support:

* player identity available from the source;
* competition;
* season;
* team;
* positions;
* appearances;
* starts where derivable;
* minutes played;
* total metrics;
* per-90 metrics;
* rate and percentage metrics;
* comparison-group percentiles;
* analytical dimensions;
* spatial action distributions;
* action maps;
* data coverage;
* sample-size warnings;
* and metric definitions.

Player photographs are not required for the MVP.

The interface must support a neutral placeholder or generated identity representation until a stable, licensed image source is introduced.

---

## 15. Comparison scope

The MVP will support:

* a minimum of two profiles;
* a maximum of four profiles;
* different players;
* the same player across different seasons;
* different teams for the same player;
* and one selected visual reference.

Every compared profile must clearly display:

* player;
* team;
* season;
* competition;
* minutes;
* positional group;
* comparison group;
* and relevant data warnings.

Cross-competition comparison may be offered, but it must not imply that all competitions have equivalent difficulty or context.

League-strength adjustment is outside the initial MVP.

---

## 16. Data research and utilization objective

ScoutLabs will treat the available football data as a research asset rather than merely a source of conventional statistics.

The project will systematically inspect every available:

* dataset;
* file family;
* entity;
* nested object;
* event type;
* relationship;
* coordinate;
* qualifier;
* outcome;
* contextual field;
* and documented source field.

Every field must be evaluated and assigned at least one documented purpose or an explicit exclusion decision.

The allowed utilization classifications are:

* **Direct metric**
* **Derived feature**
* **Filter or grouping**
* **Visualization**
* **Relationship or sequencing**
* **Quality validation**
* **Traceability**
* **Currently unused**
* **Excluded with justification**

A field may have a primary classification and one or more secondary uses when appropriate.

The objective is not to display every source value in the product. The objective is to ensure that no available information is ignored without investigation.

Identifiers, metadata and technical fields may provide value through joins, validation, provenance or reproducibility rather than through a visible football metric.

---

## 17. Data layers

ScoutLabs will maintain a conceptual separation between the following layers.

### 17.1 Source data

The original provider files and values.

Source data must not be silently modified or confused with internally calculated information.

### 17.2 Normalized data

A consistent internal representation of:

* competitions;
* seasons;
* matches;
* teams;
* players;
* appearances;
* positions;
* possessions;
* events;
* coordinates;
* outcomes;
* and relationships.

### 17.3 Derived features

Reusable analytical properties calculated from source or normalized data.

Examples may include:

* action zones;
* distances;
* progression;
* possession phase;
* temporal context;
* spatial context;
* or event-sequence properties.

### 17.4 Metrics

Interpretable player, team or match indicators built from validated features.

### 17.5 Models

Versioned methods that combine features or metrics to produce:

* similarity;
* rankings;
* action values;
* spatial profiles;
* or later compatibility scores.

### 17.6 Product outputs

The information exposed through:

* profiles;
* searches;
* rankings;
* comparisons;
* maps;
* explanations;
* and shortlists.

---

## 18. Research expectations

The research scope may be broader than the visible MVP.

ScoutLabs will investigate:

* conventional descriptive metrics;
* per-90 and rate normalization;
* positional comparison groups;
* event sequencing;
* possession context;
* spatial distributions;
* progressive actions;
* chance creation;
* shooting and expected goals;
* defensive and pressing activity;
* transitions;
* possession value;
* Expected Threat;
* SPADL-style action normalization;
* VAEP and related action-value approaches;
* statistical similarity;
* spatial similarity;
* dimensionality reduction for analysis;
* and explainability methods.

Established methods must be treated as research references, not adopted automatically.

For every method, ScoutLabs must assess:

* compatibility with the available data;
* methodological assumptions;
* sample requirements;
* reproducibility;
* interpretability;
* positional relevance;
* sensitivity to context;
* implementation cost;
* and usefulness in the product workflow.

Experimental work may be rejected even when technically successful if it does not provide reliable, understandable or useful recruitment information.

---

## 19. Metric admission criteria

A metric may become user-facing only when it has:

* a clear football question;
* an unambiguous definition;
* documented source fields;
* a reproducible calculation;
* a stated unit and denominator;
* sufficient data coverage;
* an appropriate comparison group;
* known limitations;
* automated tests;
* validation evidence;
* and a defined product use.

Metrics that are highly correlated or conceptually redundant must be reviewed before both are exposed.

A metric should not be included merely because it is common in football analytics.

---

## 20. Explainability requirements

Every recommendation must make it possible to inspect:

* the candidate pool;
* applied filters;
* selected dimensions;
* dimension weights;
* metric definitions;
* normalization method;
* data version;
* model version;
* comparison group;
* most influential similarities;
* most influential differences;
* and relevant warnings.

ScoutLabs must distinguish between:

* provider-supplied values;
* direct aggregations;
* derived metrics;
* experimental features;
* and model outputs.

---

## 21. MVP capabilities

The MVP will include:

* reproducible ingestion of StatsBomb Open Data;
* competitions, seasons, matches, teams and players;
* player appearances and minutes;
* source-data coverage reporting;
* data-quality validation;
* documented source-to-output lineage;
* totals, rates and per-90 metrics;
* positional or role-compatible comparison groups;
* percentiles;
* player search;
* player filters;
* Similar Players;
* Player Explorer;
* Metric Leaders;
* player profiles;
* event-derived action maps;
* spatial summaries supported by the available data;
* recommended and custom similarity modes;
* explainable similarity results;
* direct comparison of two to four profiles;
* named shortlists;
* separate ScoutLabs and analyst rankings;
* one preferred candidate per shortlist;
* candidate notes and statuses;
* persistent shortlist data;
* light and dark themes;
* responsive web behavior;
* automated tests;
* continuous integration;
* a deployed demonstration;
* and documented case studies.

---

## 22. Out of scope for the MVP

The following are explicitly outside the initial MVP:

* mandatory user accounts;
* authentication and authorization;
* collaborative club workspaces;
* role-based access control;
* shared shortlists;
* real-time data;
* live match analysis;
* complete global player coverage;
* commercial provider integration;
* definitive transfer recommendations;
* market values;
* salaries;
* contract information;
* complete injury histories;
* personality and character assessment;
* medical assessment;
* native mobile applications;
* continuous player tracking;
* video scouting;
* automatic video clips;
* advanced tactical role suitability;
* complete team-fit analysis;
* league-strength adjustment;
* future-performance prediction;
* potential or resale-value prediction;
* fully automated AI-generated scouting reports;
* and unlicensed player photographs.

These capabilities may be added in later phases after the analytical core is validated.

---

## 23. Future product phases

### 23.1 Authentication and collaboration

Later versions may add:

* user accounts;
* analysts and teams;
* shared club workspaces;
* comments;
* assignments;
* shortlist ownership;
* audit history;
* and permissions.

### 23.2 Role Fit

Role Fit will evaluate compatibility with a defined football role through observable behavior.

Potential role definitions may be informed by:

* tactical literature;
* professional analysis;
* coaching references;
* and structured role systems such as those used by Football Manager.

External role descriptions must be translated into measurable behaviors rather than copied as authoritative formulas.

### 23.3 Team Fit

Team Fit will combine:

* player profile;
* team style;
* tactical requirements;
* spatial behavior;
* squad need;
* and role compatibility.

Every component must remain separately explainable.

### 23.4 Spatial similarity

Later research may compare players through:

* reception zones;
* action zones;
* progression routes;
* defensive action height;
* pressure zones;
* recovery zones;
* shot locations;
* and other validated spatial representations.

### 23.5 External enrichment

Later providers may contribute:

* current age;
* nationality;
* current squad;
* injuries;
* contract dates;
* financial estimates;
* and licensed photographs.

External data must preserve source attribution and temporal validity.

---

## 24. User experience direction

### 24.1 Language

The product interface and primary repository documentation will be in English.

### 24.2 Platform

ScoutLabs will be a desktop-first web application.

Tablet and mobile layouts must remain functional, but complex comparison and spatial analysis workflows will be optimized for larger screens.

### 24.3 Navigation

The primary navigation will expose:

* Discover
* Player Profile
* Compare
* Shortlists

### 24.4 Visual direction

The visual identity will communicate:

* analytical precision;
* football expertise;
* modern technology;
* confidence;
* and professional restraint.

ScoutLabs should not resemble:

* a betting platform;
* a football results application;
* a videogame interface;
* or a generic corporate dashboard.

### 24.5 Themes

The MVP will support:

* light theme;
* dark theme;
* system preference;
* manual theme selection;
* and persistent preference.

The complete visual system will be specified separately.

---

## 25. Authentication decision

Authentication is not part of the MVP.

The first release should allow evaluators to access and demonstrate the main analytical workflows without creating an account.

Shortlists must still be persistent enough to demonstrate the complete workflow. The exact persistence strategy will be decided during architecture and requirements work.

Authentication, personal accounts and collaborative persistence will be introduced in a later phase.

---

## 26. Constraints

* The initial data source is StatsBomb Open Data.
* Coverage is partial and primarily historical.
* Available competitions and seasons may not represent the full football market.
* Data availability may differ between matches.
* 360 information is available only for part of the dataset.
* Event locations describe recorded actions, not continuous player tracking.
* Some football behaviors cannot be measured directly.
* Comparisons between competitions may contain contextual bias.
* Player identity and biographical information may be incomplete or outdated.
* No commercial or contractual claims will be made without an appropriate source.
* The project must remain demonstrable without a commercial data subscription.
* Research ambition must not prevent delivery of a coherent MVP.

---

## 27. MVP success criteria

ScoutLabs will be considered functionally successful when:

1. A user can select a player-season reference profile.
2. A user can define or accept a candidate universe.
3. A user can run recommended and custom similarity searches.
4. The same data, configuration and model version produce the same ordered result.
5. Every candidate result includes an understandable explanation.
6. A user can inspect relevant metrics, percentiles and action maps.
7. A user can compare between two and four profiles.
8. A user can create a named shortlist.
9. ScoutLabs rank and analyst rank are stored independently.
10. A user can manually reorder candidates.
11. A user can select a preferred candidate.
12. The preferred candidate visually represents the shortlist.
13. Alternatives and rejected candidates preserve their context.
14. Data limitations and insufficient samples create visible warnings.
15. Every user-facing metric has a documented definition and lineage.
16. Every documented source field has a utilization or exclusion status.
17. Every model output has a model version.
18. The platform includes at least one meaningful use of:

    * event sequencing;
    * spatial event information;
    * and available 360 frames.
19. The main user journeys are covered by automated tests.
20. A public or accessible demo is deployed.
21. At least three distinct recruitment case studies are documented.
22. An external evaluator can complete the primary workflow without technical instructions.

---

## 28. Research success criteria

The analytical research phase will be considered complete enough to support the MVP when:

* all available source file families have been inspected;
* all observed event types have been catalogued;
* all documented and observed fields have been recorded;
* field coverage has been measured;
* missing and malformed data patterns have been documented;
* every field has a utilization classification;
* event relationships and sequencing opportunities have been evaluated;
* spatial fields have been assessed;
* available 360 information has been assessed;
* candidate metrics have been catalogued;
* important metric alternatives have been compared;
* similarity methods have been experimentally evaluated;
* rejected approaches have documented reasons;
* and the final MVP metric set has been justified.

---

## 29. Main risks and responses

### 29.1 Limited coverage

The available competitions may not support every intended case study.

**Response:** select demo cases according to verified coverage and display the available universe clearly.

### 29.2 Misleading comparisons

Players may appear similar because of context, role or competition effects not fully captured by the data.

**Response:** use appropriate comparison groups, expose differences, preserve context and avoid definitive conclusions.

### 29.3 Small samples

Per-90 metrics can exaggerate performance for players with few minutes.

**Response:** establish minimum-minute rules, expose sample size and investigate reliability penalties or exclusions.

### 29.4 Positional ambiguity

Players may appear in multiple positions or perform different functions within the same position label.

**Response:** preserve position history, investigate positional groups and avoid treating source position labels as complete tactical roles.

### 29.5 Cross-league bias

The MVP does not initially adjust for competition strength.

**Response:** communicate this limitation and avoid describing raw cross-league comparisons as directly equivalent.

### 29.6 Activity maps mistaken for tracking

Event maps can be mistaken for continuous positioning.

**Response:** label them as action maps, reception maps or zones of intervention and document their data origin.

### 29.7 Opaque similarity

A similarity score may become difficult to trust.

**Response:** show dimensional scores, influential metrics, configuration, model version and important differences.

### 29.8 Metric overload

Attempting to expose every calculated value could reduce usability.

**Response:** audit every field, but only expose metrics that satisfy the admission criteria and support a user task.

### 29.9 Research without delivery

The ambition to extract maximum value from the data could indefinitely expand the project.

**Response:** separate the research backlog from the approved MVP metric set and apply explicit milestone exit criteria.

### 29.10 Scope expansion

Authentication, photographs, tactical roles, AI reports and external providers could distract from the core workflow.

**Response:** preserve the defined MVP boundary until similarity, comparison and shortlists are complete.

---

## 30. Assumptions to validate

* A reference-player search is an intuitive starting point for recruitment analysis.
* Analysts value explanations more than isolated similarity percentages.
* Dimension-level customization provides sufficient control for the MVP.
* Recommended configurations reduce the initial learning curve.
* Two to four players cover the most useful direct comparison scenarios.
* Named shortlists remain valuable without multiuser collaboration.
* Analysts want to preserve rejected alternatives and reasons.
* Event-derived spatial information adds meaningful context.
* The available dataset can support convincing demonstration cases.
* Player-season-team is an appropriate analytical profile unit.
* Position-based candidate groups are sufficient before full tactical roles are introduced.
* Separating application and analyst rankings reflects a realistic decision process.

---

## 31. Open product questions

The following decisions will be resolved through requirements, research and design work:

* Which positional groups will the MVP use?
* Which dimensions will be available in the first recommended profiles?
* How will default dimension weights be selected and validated?
* What minimum-minute rules will apply?
* How will partial-season and multi-team profiles be represented?
* Which competitions and seasons will be selected for the main demo?
* Which metrics will be visible in Player Explorer and Metric Leaders?
* How will a similarity result be judged footballistically reasonable?
* How will metric redundancy be measured?
* Which similarity method will become the initial production baseline?
* How should spatial and statistical similarity interact?
* How will shortlists persist without authentication?
* Can users save search configurations in the MVP?
* Which actions require explanatory tooltips or methodology panels?
* What information appears on a candidate result card?
* What accessibility requirements apply to charts and pitch maps?
* Which external analysts or coaches can help validate the results?

---

## 32. Documentation and decision governance

This brief defines the approved product direction and scope.

Detailed decisions will be documented separately in:

* `docs/data/`
* `docs/research/`
* `docs/metrics/`
* `docs/requirements.md`
* `docs/business-rules.md`
* `docs/user-flows.md`
* `docs/visual-system.md`
* `docs/domain-model.md`
* `docs/architecture.md`
* `docs/testing-strategy.md`
* `docs/technical-roadmap.md`
* `docs/decisions/`
* and `AGENTS.md`.

Important decisions will be recorded through decision records containing:

* context;
* alternatives;
* decision;
* rationale;
* consequences;
* risks;
* and status.

AI development agents may:

* inspect the repository;
* investigate alternatives;
* identify uncertainties;
* propose options;
* implement approved decisions;
* and document completed work.

AI development agents may not unilaterally change:

* the product vision;
* the approved MVP boundary;
* core data principles;
* analytical definitions;
* or significant architectural decisions.

---

## 33. Definition of the product brief

This brief is complete enough to begin:

* source-data research;
* field auditing;
* coverage analysis;
* event taxonomy;
* data-quality definition;
* metric research;
* similarity research;
* user-flow definition;
* and requirements elicitation.

It does not authorize implementation of the complete product before those foundations have been reviewed.
