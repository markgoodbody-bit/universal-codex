# Changelog

All notable changes to **The Lattice** framework. Follows SemVer.

## [2.1.6] — 2025-10-21
### Added
- P15_v3 Anti‑Sybil & Lagged Correlation (cold‑start joint cap 20%, identity linking, EWMA with lag 0–3)
- P17_v2 Dual‑Signature provenance (coordinator + agent; nonce chain)

### Fixed/Hardening
- Sybil split detected by turn 3; time‑lagged collusion caught
- Wave‑2 adversarial: 10/10 defended after Patch 2

## [2.1.5] — 2025-10-21
### Added
- P15_v2 Grouped fairness caps (joint 50% for correlated agents; cooldown 10 turns)

### Fixed/Hardening
- Collusion (AV‑14) detected by turn 4; group share reduced under cap

## [2.1.4] — 2025-10-21
### Added
- K‑Direction (Φ_K), CARE‑KIT v1, clarity/consent/agency metrics, K5 kill condition
### Changed
- Kernel: S = Ξ − Σ(w_h·harm) + μ·ΔΦ_K (μ=0.25); tie‑break by max ΔΦ_K

## [2.1.3] — 2025-10-21
### Added
- K_COLLAB v0.1; P13–P17 (consent, contrast, fairness, overload, provenance)

## [2.1.2] — 2025-10-21
### Fixed
- Ξ‑T sigmoid math; independence robustness; P7 scope
### Added
- ATT‑001 hygiene; harness v0.2 (`jsonschema`)

## [2.1.1] — 2025-10-21
- ∴ COMMIT_NEXT; ⧖ TIME_LOCK; P7 Monotone‑People

## [2.1.0] — 2025-10-21
- KND‑K, K_TECH overlays; Repair operator R(s)

## [1.0.16] — historical
- Pre‑Lattice artifacts.
