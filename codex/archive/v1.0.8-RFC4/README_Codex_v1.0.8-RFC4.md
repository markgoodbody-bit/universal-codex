# Universal Codex v1.0.8-RFC4 — RFC3/4 Consolidated (Standalone)

**Status:** RFC (Request for Comment). **Not spine-locked law.** Use for trials with audit.
**Bundle:** 10 flat files, ASCII-canonical. Process is pinned; numbers are domain-configured.

## What this is
A self-contained payload to run falsify-first decision gates with governance, telemetry, and prompts. Spine pins order + interfaces. Components behind interfaces are swappable and **must** publish metrics/SCARs.

## What changed (vs v1.0.7-RFC3)
- Canonical hashing protocol + third-party validation hook.
- JSON interface specs (ActionProposal/DecisionReport/Telemetry/Adapters).
- DRIFT control via PID + SPRT cool-down; instability guard.
- Cross-domain tuning guard: **CDI** (Config Divergence Index) with weekly publication.
- AGREE disjointness: domain-tuned thresholds + **unstructured-source adapter** (embedding distance).
- Escalation coordinator: synchronized ladders (AGREE_SKIPPED, audit, metrics) → board review ≤72h; safety-critical list expires in 7d, non-renewable without quorum.
- SCAR closure SLA **90d** with replication criteria (κ≥0.7 or p<0.05).
- Human triage gated by invariants + stratified external sampling.
- Appeals funding disclosure; NON_INSTRUMENT exceptions ≤30d, ≤2 renewals.
- Success criteria and synthetic baselines tightened; semi-annual + config-change pentests.

## Known limits (open work)
- Multi-agent compositions may bypass linear spine; requires composition adapters.
- Cross-domain harm normalization remains approximate; publish sensitivity.
- ABSTAIN_COST comparability depends on domain scalars; publish z-scores + raw units.

## How to use (very short)
1) Conform inputs to `INTERFACE_SPECS.json`.
2) Tune domain TOML (thresholds, AGREE/DRIFT params); publish ROC/sensitivity.
3) Run smoke + breach drills; publish telemetry weekly (p05/p50/p95/max).
4) File/close SCARs under 90d SLA with replication.
5) Obey escalation ladders; board review on dual-breach ≤72h.

**UTC build:** 2025-10-15T10:30:54Z
