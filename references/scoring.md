# Scoring methodology

## 1. Post-level relative performance

Prefer platform-local and account-local baselines.

- Engagement rate: `(likes + comments + shares) / views`
- View/follower ratio: `views / followers`
- Relative performance: `post views / median recent views for the same account`

Do not compute a metric when its required fields are missing.

## 2. Opportunity score

Use 0–100 components:

- Demand — repeated questions, saves/shares where meaningful, problem frequency
- Momentum — recent growth and recency of emerging terms/content
- Supply — how saturated the topic already is
- RelativePerformance — whether relevant posts outperform their local baselines
- Replicability — whether the concept supports a series rather than a single accident
- Fit — alignment to the user's stated goal, audience and production constraints

Suggested formula:

```text
OpportunityScore =
  0.25 * Demand
+ 0.20 * Momentum
+ 0.20 * (100 - Supply)
+ 0.15 * RelativePerformance
+ 0.10 * Replicability
+ 0.10 * Fit
```

## 3. Evidence confidence

Keep confidence separate from opportunity. Suggested labels:

- High: multiple sources/platform samples and consistent signals
- Medium: enough data for a directional conclusion but coverage is incomplete
- Low: small sample, weak fields, sparse comments or conflicting signals

A high opportunity score with low confidence should be presented as a testable hypothesis, not a fact.
