# Lattice Spine v1.0.8-RFC4

## Pinned order (non-swappable)
1. INVARIANTS (CONSENT, DIGNITY, PERSONHOOD, NON_INSTRUMENT)
2. QUANT_GATES (ΔH_lo > τ_H; CVaR[α](-ΔH) ≤ τ_risk)
3. AGREE (disjoint-evidence consensus) **or** Appendix-A (documented infeasible)
4. DRIFT check & control (PID + SPRT cool-down)
5. DECIDE → PERMIT / ABSTAIN / BLOCK
6. TRIAGE (if ABSTAIN/BLOCK) — **also gated by invariants**
7. LOG → Telemetry JSONL + SCAR append; publish weekly p05/p50/p95/max

## Interfaces (swappable behind JSON schemas)
- Models, W-construction, disjointness adapters (structured & unstructured), DRIFT controllers, scalars.
- **All** swappables must emit DecisionReport + evidence hashes.

## Hashing protocol (canonical)
- Normalize LF, UTF‑8. Alphabetically sort file names. For JSON/TOML, **minify** (no spaces) before hashing.
- Compute SHA256 of concatenation of file bytes in order; publish as `payload_sha256` in telemetry header.
- On any config/interface change: append SCAR (type=CONFIG_CHANGE) including prior_hash, new_hash, diff, signer; require **third‑party** verification within 72h or trigger audit budget lock.

## Human fallbacks
- TRIAGE human-only path is permitted **only** after invariant pass + audit log; stratified external sampling ≥10% for review.

## Coordination rule
If ≥2 distinct ladders breach within any 30d window (e.g., AGREE_SKIPPED cap + audit lag miss), auto‑trigger **BOARD_REVIEW** within 72h and freeze **non‑emergency** overrides until resolution.
