# runner.py
# Replace this stub with your real replay logic.
from typing import List, Dict

def rerun_with_order(order: List[str]) -> Dict[str, float]:
    # order like ["QUANT_GATES","AGREE","DRIFT"]
    # TODO: replay one decision through the pipeline in the given order
    # and compute harm metric used by the SPRT harness.
    raise NotImplementedError("Implement decision replay and harm computation")
