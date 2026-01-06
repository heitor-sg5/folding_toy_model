import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt

# Plot 3d structure of peptide
def plot_3d(filename, local_energies=None):
    df = pd.read_csv(filename)
    fig = plt.figure(figsize=(14, 6))

    # Plot hydrophobicity
    ax1 = fig.add_subplot(121, projection='3d')
    H = df["H"].values
    H_clipped = np.clip(H, -1.8, 1.8)
    colors_H = cm.coolwarm((H_clipped + 2.0) / 4.0)
    ax1.scatter(df["x"], df["y"], df["z"], c=colors_H, s=50)

    # Connect residue points
    for i in range(len(df) - 1):
        ax1.plot(
            [df["x"][i], df["x"][i+1]],
            [df["y"][i], df["y"][i+1]],
            [df["z"][i], df["z"][i+1]],
            "k-"
        )

    ax1.set_title("Residue Hydrophobicity")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")

    mappable_H = cm.ScalarMappable(cmap="coolwarm")
    mappable_H.set_array([-1.8, 1.8])
    plt.colorbar(mappable_H, ax=ax1, shrink=0.6, label="Hydrophobicity")

    # Plot local interaction energies
    if local_energies is not None:
        # Map each residue index to its local energy
        ax2 = fig.add_subplot(122, projection='3d')
        E = df["index"].map(lambda i: local_energies.get(i, 0.0)).values
        E_clipped = np.clip(E, -1.0, 1.0)
        colors_E = cm.coolwarm((E_clipped + 1.0) / 2.0)
        ax2.scatter(df["x"], df["y"], df["z"], c=colors_E, s=50)

        # Connect residue points
        for i in range(len(df) - 1):
            ax2.plot(
                [df["x"][i], df["x"][i+1]],
                [df["y"][i], df["y"][i+1]],
                [df["z"][i], df["z"][i+1]],
                "k-"
            )

        ax2.set_title("Local Interaction Energy")
        ax2.set_xlabel("X")
        ax2.set_ylabel("Y")
        ax2.set_zlabel("Z")

        mappable_E = cm.ScalarMappable(cmap="coolwarm")
        mappable_E.set_array([-1.0, 1.0])
        plt.colorbar(mappable_E, ax=ax2, shrink=0.6, label="Local Energy")

    plt.tight_layout()
    plt.show()