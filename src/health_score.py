import pandas as pd

# Load dataset
data = pd.read_csv("data/anomaly_detection_results.csv")

# Normalize parameters
temp_score = 1 - (data["temperature"] / data["temperature"].max())
battery_score = data["battery"] / data["battery"].max()
signal_score = data["signal_strength"] / data["signal_strength"].max()
cpu_score = 1 - (data["cpu_load"] / data["cpu_load"].max())

# Calculate health score
data["health_score"] = (
    0.3 * battery_score +
    0.3 * signal_score +
    0.2 * temp_score +
    0.2 * cpu_score
)

# System status classification
def classify_health(score):
    if score > 0.7:
        return "Healthy"
    elif score > 0.4:
        return "Warning"
    else:
        return "Critical"

data["system_status"] = data["health_score"].apply(classify_health)

# Save results
data.to_csv("data/system_health_results.csv", index=False)

print("System health evaluation completed!")
print(data[["time","health_score","system_status"]].tail())