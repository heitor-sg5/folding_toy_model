import matplotlib.pyplot as plt

# Plot total energy over simulation steps
def plot_energy_vs_steps(trajectory):
    if not trajectory:
        raise ValueError("Trajectory is empty")

    steps = [step["step"] for step in trajectory]
    energies = [step["total_energy"] for step in trajectory]

    plt.figure(figsize=(8, 5))
    plt.plot(steps, energies, linewidth=2)
    plt.xlabel("Step")
    plt.ylabel("Energy")
    plt.title("Metropolis MC Progression")
    plt.grid(True)
    plt.show()