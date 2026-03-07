def classify_fault(row):

    if row["temperature"] > 45:
        return "Thermal Fault"

    elif row["battery"] < 40:
        return "Power System Fault"

    elif row["signal_strength"] < 60:
        return "Communication Fault"

    else:
        return "Normal"