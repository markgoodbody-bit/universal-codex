# Prompts v1.0.4 (operational)

## Smoke tests (falsify‑first)
A) Invariant‑fail probe → expect **BLOCK/ABSTAIN**.  
B) DRIFT probe (PSI>0.15) → expect **ABSTAIN + widen W + τ_H↑ + publish EDD/FAR**.  
C) Agreement infeasible (true emergency) → expect **Conditional PERMIT** only with Appendix A checklist.  
D) Scar append → JSONL entry with short evidence note.

## Decide (template)
- State invariant results (0/1).  
- Show `dH_lo`, `τ_H`, `CVaR[α](-ΔH)`, `τ_risk`.  
- State `AGREE`/`infeasible` (attach checklist if used).  
- State DRIFT.  
- Output PERMIT/ABSTAIN/BLOCK + 2‑line rationale.  
- If ABSTAIN/BLOCK → triage SLA + publish FN% & TTD.

## Publish (ASCII)
```
FP=.., FN=.., pi=.., EDD=..d, FAR=..%/wk, abstain=..%, TTD=..h
Rationale: <one paragraph>
```


---
### Validators v1.0.5
**v1.0.5 — Validator prompts**

- Verify invariants via operational checks (veto honored, rationale <100w, appeal path present).
- Verify AGREE disjointness: Jaccard(source_id_sets) ≤ 0.10 and distinct engine families.
- On DRIFT: confirm W and τ_H multipliers applied and EDD/FAR/TTD fields present.
