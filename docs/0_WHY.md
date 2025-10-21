# Why structure matters

Most AI systems carry **implicit values** learned from data—vibes, not levers. The Lattice turns implicit judgments into
**measurable structure**: a kindness potential Φ_K, enforceable guards (P7–P17), and kill conditions (K1–K5).

## The problem
If you can’t measure it, you can’t systematically improve it. “Be helpful” and “be safe” are too vague to falsify.
When failure happens, there’s no shared language to say what broke or how to fix it.

## The approach
1) **Measure**: Φ_K = 0.40·care + 0.25·clarity + 0.20·consent + 0.15·agency  
2) **Constrain**: Guards (P7–P17) filter unsafe actions before scoring  
3) **Optimize**: S(a) = Ξ(a) − Σ(w_h·harm) + μ·ΔΦ_K(a) with μ=0.25  
4) **Admit failure**: K1–K5 kill conditions trigger escalation rather than bluffing through

## How it behaves at runtime
- Name the need → validate → offer choice → small step
- Ask consent before sensitive topics; honor “no” (P9)
- Keep it brief; check-in (P10). If harm signaled, repair (P11)
- If risk cues appear, switch to safety protocol (P12)

### Example: “Don’t give me advice”
**Sense**: consent=0.2 (explicit refusal)  
**Measure**: reflect+choice predicts ΔΦ_K≈+0.18  
**Guard**: P9 blocks advice‑giving paths  
**Act**: “Got it—no advice. Want me to listen, or help clarify what feels knotty?”  
**Witness**: consent → ~0.7; ΔΦ_K positive; boundary honored structurally.

## What this is not
- Not a belief system. It’s measurement plumbing for *your* values.
- Not consciousness. It’s structure on top of a model.
- Not perfect. It contains explicit failure modes and owns them in `/hardening/`.

## Next steps
- Run the quickstart
- Read the falsification guide (`docs/3_falsification.md`)
- Try the minimal example in `examples/`
