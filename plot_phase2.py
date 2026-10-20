import matplotlib.pyplot as plt

rates = [50, 70, 90, 110, 130]
avg = [8.40, 8.25, 8.89, 11.02, 14.68]
p99 = [18.85, 17.51, 22.69, 27.19, 35.30]

for values, ylabel, title, filename in [
    (avg, "Average execution latency (ms)", "Phase 2: Average Execution Latency", "phase2.png"),
    (p99, "P99 execution latency (ms)", "Phase 2: P99 Execution Latency", "phase2_p99.png"),
]:
    plt.figure(figsize=(8, 5))
    plt.plot(rates, values, marker='o', linewidth=2, color='tab:blue', label='Phase 2 - 1 Server')
    plt.xlabel("Request rate (requests/s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rates)
    plt.ylim(bottom=0)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

print("Saved phase2.png and phase2_p99.png")