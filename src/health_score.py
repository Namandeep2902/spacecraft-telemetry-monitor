import pandas as pd

# load anomaly detection data
df = pd.read_csv("data/anomaly_detection_results.csv")

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# normalize parameters
df["temp_score"] = 1 - normalize(df["temperature"], 20, 60)
df["battery_score"] = normalize(df["battery"], 20, 100)
df["signal_score"] = normalize(df["signal_strength"], 40, 100)
df["cpu_score"] = 1 - normalize(df["cpu_load"], 0, 100)

# weighted health index
df["health_score"] = (
    0.3 * df["temp_score"] +
    0.3 * df["battery_score"] +
    0.2 * df["signal_score"] +
    0.2 * df["cpu_score"]
)

# system status
def system_status(score):
    if score > 0.75:
        return "Healthy"
    elif score > 0.5:
        return "Warning"
    else:
        return "Critical"

df["system_status"] = df["health_score"].apply(system_status)

df.to_csv("data/system_health_results.csv", index=False)

print("Advanced health evaluation completed!")
print(df[["health_score","system_status"]].tail())