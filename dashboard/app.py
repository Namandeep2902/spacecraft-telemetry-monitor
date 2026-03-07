import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/system_health_results.csv")

st.title("Spacecraft Telemetry Monitoring Dashboard")

st.subheader("System Status Overview")

# Show latest system status
latest_status = data.iloc[-1]["system_status"]
st.write("Current System Status:", latest_status)

# Telemetry Graph
st.subheader("Temperature Trend")

fig, ax = plt.subplots()
ax.plot(data["time"], data["temperature"])
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")

st.pyplot(fig)

# Battery Graph
st.subheader("Battery Level")

fig2, ax2 = plt.subplots()
ax2.plot(data["time"], data["battery"])
ax2.set_xlabel("Time")
ax2.set_ylabel("Battery")

st.pyplot(fig2)

# Signal Graph
st.subheader("Signal Strength")

fig3, ax3 = plt.subplots()
ax3.plot(data["time"], data["signal_strength"])
ax3.set_xlabel("Time")
ax3.set_ylabel("Signal Strength")

st.pyplot(fig3)

# Show raw data
st.subheader("Telemetry Data Table")
st.dataframe(data)

faults = pd.read_csv("logs/fault_log.csv")

st.subheader("Recent Fault Events")

st.dataframe(faults.tail(10))
if faults.shape[0] > 0:

    st.error("⚠ Anomaly detected in spacecraft telemetry!")

    latest_fault = faults.tail(1)

    st.write("Latest Fault:")
    st.dataframe(latest_fault)
# ---------------------------
# Live Anomaly Alerts
# ---------------------------

st.subheader("⚠ Anomaly Alerts")

latest = data.iloc[-1]

alerts = []

if latest["temperature"] > 40:
    alerts.append("⚠ Thermal anomaly detected")

if latest["battery"] < 60:
    alerts.append("⚠ Battery degradation detected")

if latest["signal_strength"] < 75:
    alerts.append("⚠ Communication instability detected")

if alerts:
    for alert in alerts:
        st.error(alert)
else:
    st.success("✅ No anomalies detected")