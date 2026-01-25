from typing import List, Dict
import pandas as pd

def energy_trace_from_trajectory(trajectory: List[Dict]) -> pd.DataFrame:
    """Extract energy trace from trajectory."""
    return pd.DataFrame(
        {
            "step": [s["step"] for s in trajectory],
            "energy": [s["total_energy"] for s in trajectory],
            "accepted": [bool(s["accepted"]) for s in trajectory],
        }
    )