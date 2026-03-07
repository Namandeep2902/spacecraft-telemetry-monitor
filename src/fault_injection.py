import pandas as pd
import numpy as np

# Load telemetry dataset
data = pd.read_csv("data/telemetry_data.csv")

# Add new column
data["fault_type"] = "none"

# Thermal fault
thermal_indices = np.random.choice(data.index[-100:], 20)

data.loc[thermal_indices, "temperature"] += np.random.uniform(10, 20, 20)
data.loc[thermal_indices, "fault_type"] = "thermal"

# Battery degradation
battery_indices = np.random.choice(data.index[-100:], 20)

data.loc[battery_indices, "battery"] -= np.random.uniform(20, 30, 20)
data.loc[battery_indices, "fault_type"] = "power"

# Signal noise
signal_indices = np.random.choice(data.index[-100:], 20)

data.loc[signal_indices, "signal_strength"] -= np.random.uniform(15, 25, 20)
data.loc[signal_indices, "fault_type"] = "communication"

# Save updated dataset
data.to_csv("data/telemetry_fault_data.csv", index=False)

print("Fault injection completed!")
print(data.tail())