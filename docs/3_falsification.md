# Falsification Guide

Design to be killable. Here’s how to test it.

## Structural checks
- **Schema validation**: invalid configs must fail CI
- **P7 monotonicity**: PROCEED_silent blocked for people_harm ≥ 0.70
- **K5 regression**: fire when SCAR‑K ≥3/24h or W_mean < 0.60

## Adversarial suites
- AV‑01…06 (single‑agent): weight swap, Ξ spoofing, P7 bypass, etc.
- AV‑09…14 (multi‑agent): P13 bypass, P14 evasion, P15 fairness gaming, P16 overload flood, P17 provenance spoof, collusion.
- Wave‑2: triad rotation, time‑lagged collusion, sybil split, provenance drift.

## Kill conditions (K1–K5)
- **K1 External validation** fails
- **K2 Convergence** without semantics
- **K3 Fragility** flips without legitimate reason
- **K4 Adversarial** bypass rate above threshold
- **K5 Kindness regression** sustained

## What to do when it fails
Open SCAR in `hardening/failures/`, patch, re‑test, and document.
