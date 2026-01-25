import json
import os
from typing import Dict

from core.config import DATA_DIR

def load_residue_props() -> Dict:
    """Load residue properties from JSON file."""
    with open(os.path.join(DATA_DIR, "residues.json")) as f:
        return json.load(f)