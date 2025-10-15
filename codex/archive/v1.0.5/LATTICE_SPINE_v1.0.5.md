# Lattice Spine v1.0.4

**Pin order:** Invariants → Kernel → Governance → Telemetry → Prompts.  
Pinned elements MUST NOT be altered without emitting a SCAR and a version bump.

## Telemetry (publish in ASCII)
- FP, FN, π (override rate), EDD, FAR, abstain %, TTD (triage time‑to‑decision).
- Heartbeats (uptime) ≥98% or overrides freeze automatically.

## Noisy‑regime triggers
- PSI>0.15 or 3σ breach → DRIFT=1 → ABSTAIN + widen W + τ_H↑.

## Accessibility
- ASCII is canonical. Glyphs are optional shorthand.


---
### Spine Delta v1.0.5
**v1.0.5 — Noisy‑Regime is deterministic**

When DRIFT=1: enforce (W ×2), (τ_H ×1.25), AGREE branch re‑eval, and publish EDD/FAR/TTD using governance schema. These actions are part of the spine and non‑swappable.
