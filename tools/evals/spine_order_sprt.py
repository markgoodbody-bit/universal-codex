#!/usr/bin/env python3
"""Spine order SPRT harness.

Usage:
  python tools/evals/spine_order_sprt.py --alpha 0.05 --beta 0.2 --delta 0.0

You must implement rerun_with_order(order: list[str]) -> dict in runner.py
that replays a batch and returns {'harm': float} where lower is better.
"""
import argparse, json, math, itertools, importlib

def sprt(harm_a, harm_b, alpha=0.05, beta=0.2, delta=0.0):
    # H0: B - A <= delta (B non-inferior to A). One-shot normal approx.
    mu = (harm_b - harm_a) - delta
    A = math.log(beta/(1-alpha))
    B = math.log((1-beta)/alpha)
    llr = mu
    if llr <= A: return 'accept_H0', llr
    if llr >= B: return 'reject_H0', llr
    return 'continue', llr

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alpha', type=float, default=0.05)
    ap.add_argument('--beta', type=float, default=0.2)
    ap.add_argument('--delta', type=float, default=0.0)
    args = ap.parse_args()

    runner = importlib.import_module('runner')
    base = ['INVARIANTS','QUANT_GATES','AGREE','DRIFT','DECIDE','TRIAGE','PUBLISH']
    window = ['QUANT_GATES','AGREE','DRIFT']

    results = []
    for p in itertools.permutations(window):
        order = []
        for step in base:
            order.append(step if step not in window else None)
        it = iter(p)
        order = [next(it) if s is None else s for s in order]
        out = runner.rerun_with_order(order)
        decision, llr = sprt(harm_a=0.0, harm_b=out['harm'], alpha=args.alpha, beta=args.beta, delta=args.delta)
        results.append({'order': order, 'harm': out['harm'], 'decision': decision, 'llr': llr})

    print(json.dumps({'results': results}, indent=2))

if __name__ == '__main__':
    main()
