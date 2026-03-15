import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Spacecraft Telemetry Monitoring", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles/style.css")

data = pd.read_csv("data/system_health_results.csv")
faults = pd.read_csv("logs/fault_log.csv")

latest = data.iloc[-1]

st.title("🚀 Spacecraft Telemetry Monitoring Dashboard")

st.markdown("---")

thermal_status = "OK"
power_status = "OK"
comm_status = "OK"

if latest["temperature"] > 45:
    thermal_status = "⚠ Thermal Issue"

if latest["battery"] < 40:
    power_status = "⚠ Power Issue"

if latest["signal_strength"] < 60:
    comm_status = "⚠ Communication Issue"

health = round(latest["health_score"], 2)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Thermal System", thermal_status)
c2.metric("Power System", power_status)
c3.metric("Communication", comm_status)
c4.metric("Health Score", health)

st.markdown("---")

colA, colB = st.columns([3,1])

with colA:

    fig_temp = px.line(data, x="time", y="temperature", title="Temperature Telemetry")
    anomalies = data[data["threshold_anomaly"] == 1]

    fig_temp.add_scatter(
        x=anomalies["time"],
        y=anomalies["temperature"],
        mode="markers",
        marker=dict(color="red", size=6),
        name="Anomaly"
    )

    st.plotly_chart(fig_temp, use_container_width=True)

    fig_battery = px.line(data, x="time", y="battery", title="Battery Telemetry")
    st.plotly_chart(fig_battery, use_container_width=True)

    fig_signal = px.line(data, x="time", y="signal_strength", title="Signal Strength")
    st.plotly_chart(fig_signal, use_container_width=True)

with colB:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={'text': "System Health"},
        gauge={
            'axis': {'range': [0, 1]},
            'bar': {'color': "green"}
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    total_faults = faults.shape[0]
    high_faults = faults[faults["severity"] == "HIGH"].shape[0]

    st.metric("Total Faults", total_faults)
    st.metric("High Severity Faults", high_faults)

st.markdown("---")

st.header("Telemetry Data")

telemetry_view = data[
    ["time","temperature","battery","signal_strength","cpu_load","fault_type"]
]

st.dataframe(
    telemetry_view.tail(40),
    height=400,
    use_container_width=True
)

st.download_button(
    "Download Telemetry Data",
    telemetry_view.to_csv(index=False),
    "telemetry_data.csv"
)

st.markdown("---")

st.header("Recent Fault Events")

fault_view = faults[
    ["time","temperature","battery","signal_strength","cpu_load","severity"]
]

st.dataframe(
    fault_view.tail(10),
    height=300,
    use_container_width=True
)

if faults.shape[0] > 0:
    st.error("⚠ Anomaly detected in spacecraft telemetry")

st.markdown("---")

st.header("Fault Timeline")

fault_points = data[data["threshold_anomaly"] == 1]

fig_fault = px.scatter(
    fault_points,
    x="time",
    y="temperature",
    color="temperature",
    title="Detected Anomalies"
)

st.plotly_chart(fig_fault, use_container_width=True)

st.markdown("---")

if "fault_type" in faults.columns and faults["fault_type"].notna().any():

    st.header("Fault Distribution")

    fig_pie = px.pie(
        faults,
        names="fault_type",
        title="Fault Type Distribution"
    )

    st.plotly_chart(fig_pie, use_container_width=True)

st.sidebar.title("🚨 Live Alerts")

alerts = []

if latest["temperature"] > 40:
    alerts.append("⚠ Thermal anomaly detected")

if latest["battery"] < 60:
    alerts.append("⚠ Battery degradation detected")

if latest["signal_strength"] < 75:
    alerts.append("⚠ Communication instability detected")

if alerts:
    for alert in alerts:
        st.sidebar.error(alert)
else:
    st.sidebar.success("No anomalies detected")