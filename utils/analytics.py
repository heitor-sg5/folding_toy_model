import itertools
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# Build a contact graph from a final folded structure, where nodes are 
# residue indexes and edges are non-bonded nearest neighbours
def build_contact_graph(structure, lattice):
    # Extract residue list from structure dictionary
    residues = structure["residues"]

    # Map residue index (i.e. lattice coordinates)
    positions = {r["index"]: (r["x"], r["y"], r["z"]) for r in residues}
    graph = {}

    # Check all unordered residue pairs
    for i, j in itertools.combinations(positions.keys(), 2):
        if abs(i - j) <= 1:
            continue  # skip covalently bonded neighbours
        # Add edge if residues occupy neighbouring lattice sites
        if positions[j] in lattice.get_neighbours(positions[i]):
            graph[(i, j)] = 1.0  # binary contact
    return graph

# Compute a consensus contact graph across multiple independent runs
def consensus_contact_graph(graphs):
    consensus = defaultdict(float)
    # Count contact occurrences across runs
    for g in graphs:
        for edge in g:
            consensus[edge] += 1.0
    # Normalize by number of runs to obtain frequencies
    n = len(graphs)
    for edge in consensus:
        consensus[edge] /= n
    return dict(consensus)

# Convert a contact graph into a symmetric contact-frequency matrix
def contact_frequency_matrix(consensus, n_residues):
    M = np.zeros((n_residues, n_residues))

    # Matrix entry (i, j) = probability that residues i and j are in contact
    for (i, j), w in consensus.items():
        M[i, j] = w
        M[j, i] = w # enforce symmetry
    return M

# Plot the contact-frequency matrix as a 2D heatmap
def plot_contact_matrix(matrix):
    plt.figure(figsize=(7, 6))
    im = plt.imshow(matrix, origin="lower", cmap="viridis")
    plt.colorbar(im, label="Contact frequency")
    plt.xlabel("Residue index")
    plt.ylabel("Residue index")
    plt.title("Contact frequency matrix")
    plt.tight_layout()
    plt.show()

# Calls consensus  plotting functions and returns scores
def plot_contact_graphs(graphs, sequence):
    n_residues = len(sequence)
    # Build consensus contact graph across runs
    consensus = consensus_contact_graph(graphs)
    # Convert to matrix representation
    M = contact_frequency_matrix(consensus, n_residues)
    plot_contact_matrix(M) # plot the contact map

# Plot total energy over simulation steps
def plot_energy_vs_steps(trajectory):
    steps = [step["step"] for step in trajectory]
    energies = [step["total_energy"] for step in trajectory]
    plt.figure(figsize=(8, 5))
    plt.plot(steps, energies, linewidth=2)
    plt.xlabel("Step")
    plt.ylabel("Energy")
    plt.title("Metropolis MC Progression")
    plt.grid(True)
    plt.tight_layout()
    plt.show()