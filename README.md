# The Lattice: Structural Ethics for AI Systems
[![Release](https://img.shields.io/github/v/release/markgoodbody-bit/universal-codex)](../../releases)

Make values **explicit, testable, and improvable**. The Lattice is a falsifiable framework for AI decision-making. 
It turns vibes into variables and judgment calls into *guarded* optimizations.

## Why this matters
Modern AI often behaves according to **implicit values** learned from data. Thatâ€™s hard to examine and harder to improve.
The Lattice makes those values *structural*: measurable objectives, enforceable guards, and kill conditions that say 
â€œstop and escalateâ€ when the system is failing.

## Core concepts (at a glance)
```
   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
   â”‚  Î¦_K = 0.40Â·care + 0.25Â·clarity    â”‚
   â”‚       + 0.20Â·consent + 0.15Â·agency â”‚
   â”‚                                     â”‚
   â”‚  Guards P7â€“P17 â†’ filter actions     â”‚
   â”‚  Kernel: S = Îž âˆ’ Î£(w_hÂ·harm)        â”‚
   â”‚                 + Î¼Â·Î”Î¦_K (Î¼=0.25)   â”‚
   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```
- **Î¦_K (Kindness Potential)**: care + clarity + consent + agency. Optimize **Î”Î¦_K** at each turn (with guards).
- **Guards (P7â€“P17)**: Safety constraints (e.g., P7 blocks silent actions when people_harm â‰¥ 0.70).
- **Kill Conditions (K1â€“K5)**: System-level â€œstop and escalateâ€ tests.
- **Overlays**: Domain extensions (KNDâ€‘K conversational, K_TECH technical, K_COLLAB multiâ€‘agent).

## Quickstart (5 minutes)
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip jsonschema
python conformance/conformance_harness.py
```
Youâ€™ll see a pass/fail summary for the included golden cases.

## Whatâ€™s in this repo
- `schemas/` â€” JSON Schemas (v2.1.6) + bundle
- `docs/` â€” Philosophy, overview, falsification guide
- `overlays/` â€” KND-K, K_TECH, K_COLLAB specs
- `care-kit/` â€” CAREâ€‘KIT v1 runtime pledge + loop
- `conformance/` â€” Golden cases + replay harness
- `examples/` â€” Minimal walkthroughs
- `hardening/` â€” Waveâ€‘1 / Waveâ€‘2 reports + failures archive
- `.github/` â€” CI: schema + harness checks

## Status
- Version: **2.1.6** (see `CHANGELOG.md`)
- Hardening: Waveâ€‘1 âœ…, Waveâ€‘2 âœ… (patches P15_v3, P17_v2)
- External attestation: **Pending** (ATTâ€‘001 sent to EleutherAI & AI Verify Foundation)

## Safety stance
This is **infrastructure** for implementing values, **not** a source of values. See `SECURITY.md` for guards & disclosure.

## License
Apacheâ€‘2.0
