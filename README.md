**Spacecraft Telemetry Monitoring System**
1. Overview:

This project implements a telemetry monitoring dashboard for analyzing spacecraft system data and detecting anomalies in subsystem behavior. Spacecraft continuously generate telemetry data from onboard sensors such as temperature sensors, power systems, and communication modules. Monitoring this data is essential to ensure spacecraft stability and mission safety.
The system processes telemetry data, identifies abnormal patterns, and presents the results through an interactive dashboard. It allows users to visualize subsystem performance, monitor system health, and track fault events.

2. Objectives:

The primary objectives of this project are:
Monitor spacecraft telemetry signals from multiple subsystems
Detect abnormal system behavior using machine learning techniques
Provide an interactive dashboard for system monitoring
Visualize telemetry trends and detected anomalies
Maintain a record of detected fault events

3. Features:
 
Telemetry data visualization for temperature, battery level, and signal strength
Subsystem health monitoring for thermal, power, and communication systems
Anomaly detection based on telemetry signal patterns
Fault timeline visualization showing when anomalies occurred
Live alert panel highlighting detected issues
Interactive dashboard built using Streamlit

4. Technologies Used:

Python
Pandas – data processing and analysis
Scikit-learn – anomaly detection models
Streamlit – interactive dashboard development
Plotly – interactive data visualization
Matplotlib – additional plotting support
GitHub – version control and project management

5. Project Structure:
   
spacecraft-telemetry-monitor
│
├── dashboard
│   └── app.py
│
├── data
│   └── system_health_results.csv
│
├── logs
│   └── fault_log.csv
│
├── src
│   └── anomaly_detection.py
│
├── requirements.txt
└── README.md

7. Dashboard Components:

The dashboard provides the following monitoring components:
Subsystem Status - Displays the health status of thermal, power, and communication subsystems along with an                    overall system health score.
Telemetry Trends - Shows time-series graphs for temperature, battery level, and signal strength.
Fault Monitoring - Displays recent detected faults and anomaly events.
Fault Timeline -   Visualizes when anomalies occurred during telemetry monitoring.
Live Alerts -      Highlights critical subsystem issues detected by the system.

7. Running the Project Locally:

Clone the repository - git clone https://github.com/Namandeep2902/spacecraft-telemetry-monitor.git
Navigate to the project directory - cd spacecraft-telemetry-monitor
Install required dependencies - pip install -r requirements.txt
Run the dashboard -  streamlit run dashboard/app.py

8. Live Application: 

The deployed dashboard can be accessed here:
https://spacecraft-telemetry-monitorgit.streamlit.app/

9. Future Improvements:

Possible improvements for the system include -
Real-time telemetry streaming simulation
Advanced anomaly detection algorithms
Predictive spacecraft health analysis
Automated alert notifications
Historical telemetry analytics

10. Author:

Developed as part of a telemetry monitoring and anomaly detection project using Python and machine learning techniques.
