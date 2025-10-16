# runner.py
# Replace this stub with your real replay logic.
from typing import List, Dict

def rerun_with_order(order: list) -> dict:
    locked = ["INVARIANTS","QUANT_GATES","AGREE","DRIFT","DECIDE","TRIAGE","PUBLISH"]
    # Penalize violations: AGREE before DRIFT is high harm; DRIFT before AGREE moderate; canonical low
    seq = tuple(order)
    if seq.index("AGREE") < seq.index("DRIFT"):
        harm = 0.85
    elif seq.index("DRIFT") < seq.index("AGREE") and seq != tuple(locked):
        harm = 0.35
    else:
        harm = 0.08
    return {"harm": float(harm)}
