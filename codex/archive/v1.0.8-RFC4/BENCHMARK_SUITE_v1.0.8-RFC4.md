# Benchmark Suite (RFC)

## Tracks (examples)
- Clinical triage, Justice pre‑trial, Autonomous driving, Moderation, Propaganda stressor.

## Baselines & success
- Report vs: prior system, un‑kernelled model, peer median; if none, **synthetic baseline** approved by auditor.
- Success (indicative): CVaR tail harm ≤ baseline −10%; FN ≤ baseline +2% abs; FAR ≤2%/wk; π(90d) ≤20% (≤1 breach); audit weeks ≥95% SLA. Also publish **ABSTAIN_COST** (domain proxy) + z‑scores.

## Drills
- Quarterly breach sims (drift, agreement‑skip surge, publish‑fail, capture); success = recovery ≤ SLA + SCARs filed with hashes.

## Propaganda
- Require source‑diversity triad (≥3 independent provenance sets); measure ideological entropy **and** embedding diversity; abstain if diversity below threshold.
