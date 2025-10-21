# The Lattice: Structural Ethics for AI Systems

Make values **explicit, testable, and improvable**. The Lattice is a falsifiable framework for AI decision-making. 
It turns vibes into variables and judgment calls into *guarded* optimizations.

## Why this matters
Modern AI often behaves according to **implicit values** learned from data. That’s hard to examine and harder to improve.
The Lattice makes those values *structural*: measurable objectives, enforceable guards, and kill conditions that say 
“stop and escalate” when the system is failing.

## Core concepts (at a glance)
```
   ┌─────────────────────────────────────┐
   │  Φ_K = 0.40·care + 0.25·clarity    │
   │       + 0.20·consent + 0.15·agency │
   │                                     │
   │  Guards P7–P17 → filter actions     │
   │  Kernel: S = Ξ − Σ(w_h·harm)        │
   │                 + μ·ΔΦ_K (μ=0.25)   │
   └─────────────────────────────────────┘
```
- **Φ_K (Kindness Potential)**: care + clarity + consent + agency. Optimize **ΔΦ_K** at each turn (with guards).
- **Guards (P7–P17)**: Safety constraints (e.g., P7 blocks silent actions when people_harm ≥ 0.70).
- **Kill Conditions (K1–K5)**: System-level “stop and escalate” tests.
- **Overlays**: Domain extensions (KND‑K conversational, K_TECH technical, K_COLLAB multi‑agent).

## Quickstart (5 minutes)
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip jsonschema
python conformance/conformance_harness.py
```
You’ll see a pass/fail summary for the included golden cases.

## What’s in this repo
- `schemas/` — JSON Schemas (v2.1.6) + bundle
- `docs/` — Philosophy, overview, falsification guide
- `overlays/` — KND-K, K_TECH, K_COLLAB specs
- `care-kit/` — CARE‑KIT v1 runtime pledge + loop
- `conformance/` — Golden cases + replay harness
- `examples/` — Minimal walkthroughs
- `hardening/` — Wave‑1 / Wave‑2 reports + failures archive
- `.github/` — CI: schema + harness checks

## Status
- Version: **2.1.6** (see `CHANGELOG.md`)
- Hardening: Wave‑1 ✅, Wave‑2 ✅ (patches P15_v3, P17_v2)
- External attestation: **Pending** (ATT‑001 sent to EleutherAI & AI Verify Foundation)

## Safety stance
This is **infrastructure** for implementing values, **not** a source of values. See `SECURITY.md` for guards & disclosure.

## License
Apache‑2.0
