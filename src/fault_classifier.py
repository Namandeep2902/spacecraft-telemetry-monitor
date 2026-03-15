import pandas as pd

df = pd.read_csv("data/anomaly_detection_results.csv")

def classify_fault(row):

    if row["temperature"] > 45:
        return "Thermal Fault"

    elif row["battery"] < 40:
        return "Power System Fault"

    elif row["signal_strength"] < 60:
        return "Communication Fault"

    else:
        return "Normal"

df["fault_class"] = df.apply(classify_fault, axis=1)

df.to_csv("data/fault_classification.csv", index=False)

print("Fault classification completed")