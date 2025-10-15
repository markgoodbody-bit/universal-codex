#!/usr/bin/env python3
"""Bootstrap FN vs pi cap.
Input CSV columns: override:int (1 if override), fn:int (1 if false negative), domain:str

Example:
  python tools/evals/bootstrap_pi_curves.py --csv logs/decisions.csv --domain clinical --baseline_fn 0.10 --delta 0.02
"""
import argparse, csv, random, json

def simulate(sample, pi_cap):
    total = len(sample)
    overrides = [r for r in sample if r['override']==1]
    allowed = int(pi_cap * total)
    blocked = max(0, len(overrides) - allowed)
    fn_extra = sum(r['fn'] for r in overrides[:blocked])
    fn_rate = (sum(r['fn'] for r in sample) + fn_extra) / total
    return fn_rate

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--domain', required=True)
    ap.add_argument('--baseline_fn', type=float, required=True)
    ap.add_argument('--delta', type=float, default=0.02)
    ap.add_argument('--boot', type=int, default=1000)
    args = ap.parse_args()

    rows = []
    with open(args.csv, newline='') as f:
        rd = csv.DictReader(f)
        for r in rd:
            if r.get('domain') != args.domain: continue
            rows.append({'override': int(r['override']), 'fn': int(r['fn'])})
    if not rows:
        raise SystemExit('no rows for domain')

    pis = [x/100 for x in range(5,26)]  # 0.05..0.25
    out = []
    for pi in pis:
        fn_samples = []
        for _ in range(args.boot):
            sample = [rows[random.randrange(len(rows))] for __ in range(len(rows))]
            fn_samples.append(simulate(sample, pi_cap=pi))
        fn_samples.sort()
        fn95 = fn_samples[int(0.975*len(fn_samples))-1]
        safe = fn95 <= (args.baseline_fn + args.delta)
        out.append({'pi': pi, 'fn95': fn95, 'safe': safe})

    safe_pis = [r for r in out if r['safe']]
    best = max(safe_pis, key=lambda r: r['pi']) if safe_pis else None
    print(json.dumps({'curve': out, 'recommended_pi': best}, indent=2))

if __name__ == '__main__':
    main()
