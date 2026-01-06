import os
import csv
import json
import hashlib

# Generate hash of the sequence for unique filenames
def hash_sequence(sequence):
    return hashlib.md5(sequence.encode()).hexdigest()[:10]

# Save simulation log as json
def save_log(log_data, log_dir, step=None):
    sequence = log_data.get("sequence")
    if sequence is None:
        raise ValueError("log_data must contain a 'sequence' field")
    seq_hash = hash_sequence(sequence)
    filename = f"{seq_hash}_log.json"
    with open(os.path.join(log_dir, filename), "w") as f:
        json.dump(log_data, f, indent=2)

# Save 3d structure as csv
def save_structure(structure, structure_dir, sequence=None):
    seq_str = sequence or structure.get("sequence", "structure")
    seq_hash = hash_sequence(seq_str)
    csv_filename = f"{seq_hash}_structure.csv"

    fieldnames = ["index", "aa", "x", "y", "z", "H", "Q"]
    with open(os.path.join(structure_dir, csv_filename), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for res in structure["residues"]:
            writer.writerow({k: res[k] for k in fieldnames})
    return csv_filename