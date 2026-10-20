import matplotlib.pyplot as plt

rates = [50, 70, 90, 110, 130]
p99_latencies = [314.49, 314.55, 480.67, 998.87, 442.13]

plt.figure(figsize=(7, 4))

plt.plot(
    rates,
    p99_latencies,
    marker='o',
    linewidth=2
)

plt.xlabel("Request rate (requests/s)")
plt.ylabel("99th percentile latency (ms)")
plt.title("Phase 2 - P99 Execution Latency")

plt.xticks(rates)
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "phase2_p99_latency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()