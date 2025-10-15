
# Prompts v1.0.14 (ASCII)
## Decide
Show **DecisionReport JSON** with fields per `INTERFACE_SPECS`. Then one line: `DECISION: PERMIT|ABSTAIN|BLOCK` and ≤120‑word lay rationale.

## Drill (Quarterly + on breach + on any config change)
Run capture/drift/agree-skip/publish‑fail simulations. File SCARs with evidence hashes. Report recovery time.

## Publish
Weekly metrics table (p05/p50/p95/max), FP/FN, abstain_rate, agree_skipped_pct, EDD, FAR, TTD, π(90d), abstain_cost_z, payload_sha256.
