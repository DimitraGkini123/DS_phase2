import matplotlib.pyplot as plt

rates = [50, 70, 90, 110, 130]
latencies = [70.86, 80.15, 94.44, 111.42, 73.89]

plt.figure(figsize=(7, 4))

plt.plot(
    rates,
    latencies,
    marker='o',
    linewidth=2
)

plt.xlabel("Request rate (requests/s)")
plt.ylabel("Average execution latency (ms)")
plt.title("Phase 2 - Average Execution Latency")

plt.xticks(rates)
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "phase2_average_latency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()