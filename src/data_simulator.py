import numpy as np
import pandas as pd

n = 500
time = np.arange(n)

temperature = []
battery = []
signal = []
cpu_load = []
phase = []

for t in time:

    # Launch Phase
    if t < 100:
        temperature.append(np.random.normal(30, 3))
        battery.append(np.random.normal(90, 2))
        signal.append(np.random.normal(85, 4))
        cpu_load.append(np.random.normal(70, 10))
        phase.append("launch")

    # Orbit Stabilization
    elif t < 200:
        temperature.append(np.random.normal(27, 2))
        battery.append(np.random.normal(88, 3))
        signal.append(np.random.normal(90, 2))
        cpu_load.append(np.random.normal(50, 8))
        phase.append("stabilization")

    # Normal Operation
    elif t < 400:
        temperature.append(np.random.normal(25, 2))
        battery.append(np.random.normal(85, 3))
        signal.append(np.random.normal(92, 2))
        cpu_load.append(np.random.normal(40, 6))
        phase.append("normal")

    # Fault Phase
    else:
        temperature.append(np.random.normal(45, 5))
        battery.append(np.random.normal(60, 10))
        signal.append(np.random.normal(70, 8))
        cpu_load.append(np.random.normal(80, 15))
        phase.append("fault")

data = pd.DataFrame({
    "time": time,
    "phase": phase,
    "temperature": temperature,
    "battery": battery,
    "signal_strength": signal,
    "cpu_load": cpu_load
})

data.to_csv("data/telemetry_data.csv", index=False)

print("Telemetry dataset with mission phases generated!")
print(data.head())