import pandas as pd
import matplotlib.pyplot as plt

# Load anomaly detection dataset
data = pd.read_csv("data/anomaly_detection_results.csv")

# ---------------------------
# Temperature Graph
# ---------------------------

plt.figure(figsize=(10,5))
plt.plot(data["time"], data["temperature"], label="Temperature")

anomalies = data[data["threshold_anomaly"] == 1]

plt.scatter(anomalies["time"], anomalies["temperature"],
            color="red", label="Anomaly")

plt.title("Temperature vs Time")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()

plt.savefig("results/temperature_plot.png")
plt.show()


# ---------------------------
# Battery Graph
# ---------------------------

plt.figure(figsize=(10,5))
plt.plot(data["time"], data["battery"], label="Battery")

anomalies = data[data["threshold_anomaly"] == 1]

plt.scatter(anomalies["time"], anomalies["battery"],
            color="red", label="Anomaly")

plt.title("Battery Level vs Time")
plt.xlabel("Time")
plt.ylabel("Battery")
plt.legend()

plt.savefig("results/battery_plot.png")
plt.show()


# ---------------------------
# Signal Strength Graph
# ---------------------------

plt.figure(figsize=(10,5))
plt.plot(data["time"], data["signal_strength"], label="Signal")

anomalies = data[data["threshold_anomaly"] == 1]

plt.scatter(anomalies["time"], anomalies["signal_strength"],
            color="red", label="Anomaly")

plt.title("Signal Strength vs Time")
plt.xlabel("Time")
plt.ylabel("Signal Strength")
plt.legend()

plt.savefig("results/signal_plot.png")
plt.show()


print("Graphs generated successfully!")