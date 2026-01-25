from typing import Dict, Optional

def validate_sequence(seq: str, residue_props: Dict) -> Optional[str]:
    """
    Validate a peptide sequence against known residue types.
    Args:
        seq: The sequence string to validate
        residue_props: Dictionary mapping residue codes to properties
    Returns:
        None if valid, error message if invalid
    """
    seq = seq.strip().upper()
    if not seq:
        return "Sequence cannot be empty."
    unknown = {aa for aa in seq if aa not in residue_props}
    if unknown:
        return f"Unknown residue types in sequence: {', '.join(sorted(unknown))}"
    return None