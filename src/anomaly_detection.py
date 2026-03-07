import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Load fault dataset
data = pd.read_csv("data/telemetry_fault_data.csv")

# -------------------------
# Method 1 : Threshold
# -------------------------

data["threshold_anomaly"] = 0

data.loc[data["temperature"] > 40, "threshold_anomaly"] = 1
data.loc[data["battery"] < 60, "threshold_anomaly"] = 1
data.loc[data["signal_strength"] < 75, "threshold_anomaly"] = 1


# -------------------------
# Method 2 : Z-Score
# -------------------------

z_temp = (data["temperature"] - data["temperature"].mean()) / data["temperature"].std()
z_battery = (data["battery"] - data["battery"].mean()) / data["battery"].std()
z_signal = (data["signal_strength"] - data["signal_strength"].mean()) / data["signal_strength"].std()

data["zscore_anomaly"] = ((abs(z_temp) > 3) | (abs(z_battery) > 3) | (abs(z_signal) > 3)).astype(int)


# -------------------------
# Method 3 : Isolation Forest
# -------------------------

features = data[["temperature", "battery", "signal_strength", "cpu_load"]]

model = IsolationForest(contamination=0.1)

data["isolation_anomaly"] = model.fit_predict(features)

# Convert output (-1 = anomaly)
data["isolation_anomaly"] = data["isolation_anomaly"].apply(lambda x: 1 if x == -1 else 0)


# Save results
data.to_csv("data/anomaly_detection_results.csv", index=False)

print("Anomaly detection completed!")

print(data[["temperature","battery","signal_strength","threshold_anomaly","zscore_anomaly","isolation_anomaly"]].tail())