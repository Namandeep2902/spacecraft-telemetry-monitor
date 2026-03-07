import pandas as pd

# anomaly detection results load karo
df = pd.read_csv("data/anomaly_detection_results.csv")

# sirf anomalies filter karo
faults = df[df["isolation_anomaly"] == 1]

# important columns select karo
fault_log = faults[[
    "time",
    "temperature",
    "battery",
    "signal_strength",
    "cpu_load"
]]

# severity add karo
fault_log["severity"] = "HIGH"

# logs folder me save karo
fault_log.to_csv("logs/fault_log.csv", index=False)

print("Fault log generated successfully!")
print(fault_log.tail())