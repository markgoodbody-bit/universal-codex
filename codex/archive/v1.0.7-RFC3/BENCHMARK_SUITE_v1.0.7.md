# Benchmark Suite v1.0.7

## Baselines
Report vs: (1) prior deployment, (2) un‑kernelled model, (3) peer median. If none, mandate **synthetic baseline** via adversarial generator (publish recipe) + independent auditor approval.

## Metrics (weekly; publish p05/p50/p95/max; windows 7d/30d)
- FP/FN; abstain rate; AGREE_SKIPPED%; π (90d); EDD_days; FAR_%/wk; TTD_hours; ABSTAIN_COST (proxy) + z‑score.

## Success criteria (v1.1 gating)
- CVaR tail harm ≤ baseline −10%; FN ≤ baseline +2% abs; FAR ≤2%/wk; π(90d) ≤20% (≤1 breach); ≥95% audit‑SLA weeks; drill recovery ≤ SLA.

## Propaganda track
- FP track + triad provenance diversity (min‑hash) + ideological entropy; abstain under low diversity.
