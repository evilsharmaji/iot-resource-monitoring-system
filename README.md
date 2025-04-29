# 🌐 IoT-Integrated Resource Monitoring System

A real-time IoT-based solution to monitor essential resources like **water**, **energy**, and **inventory** using sensor networks, cloud-based analytics, and dashboards. This system integrates **ESP32**, **MQTT**, **Flask**, **InfluxDB**, **ML models**, and **Grafana/Plotly Dash** for complete insight and automation.

---

## 🚀 Features

- 📡 Real-time Data Acquisition (ESP32 + MQTT)
- 📊 Interactive Dashboards (Grafana / Plotly Dash)
- ⚠️ Anomaly Detection (using Isolation Forest)
- 🔮 Predictive Analytics (LSTM with TensorFlow)
- 📲 Automated Alerts via SMS (Twilio)
- 📦 Docker-Ready Deployment

---

## 🏗️ System Architecture

![System Architecture](images/system-architecture.png)

**Data Flow**:
ESP32 Sensors → MQTT → Flask API → InfluxDB → ML Models → Grafana Dashboard & Alerts


---

## 📦 Modules

### 1️⃣ IoT Data Acquisition

- **Hardware**: ESP32, DHT22 (temperature/humidity), Ultrasonic sensor (water level)
- **Communication**: MQTT via Mosquitto broker
- **Sample Payload**:
```json
{
  "temperature": 25.3,
  "humidity": 60.1,
  "water_level": 15.6
}

2️⃣ Backend & ML Engine
API: Python + Flask to receive and store data

Database: InfluxDB (optimized time-series DB)

ML Models:

Isolation Forest for anomaly detection

LSTM (TensorFlow) for prediction


3️⃣ Visualization & Alerts
Dashboards: Plotly Dash or Grafana

Alerts: Twilio (SMS), AWS SNS (Email)

UI Features:

Real-time graphs

Trend analysis

Anomaly markers

🧠 Machine Learning
🔍 Anomaly Detection:

model = IsolationForest()
df['anomaly'] = model.fit_predict(df[['temperature', 'humidity', 'water_level']])

📈 Prediction:

model = LSTM(...)
model.fit(X_train, y_train)

🐳 Docker Deployment

# docker-compose.yml
services:
  flaskapp:
    build: ./flask_app
    ports:
      - "5000:5000"
  influxdb:
    image: influxdb
    ports:
      - "8086:8086"

iot-resource-monitoring/
├── esp32/                  # C++ code for ESP32
├── flask_app/              # Flask API and ML code
├── dashboard/              # Dash/Grafana visualization
├── docker-compose.yml
├── README.md
└── images/                 # Architecture and screenshots

📲 Alert Example (Twilio SMS)
"🚨 Anomaly Detected: Water usage spike at 3:45 PM"

📚 References
MQTT

Grafana

ESP32 Arduino Core

InfluxDB

Twilio API

✨ Future Enhancements
🤖 Edge AI with TensorFlow Lite on ESP32

☁️ Multi-Tenant SaaS with AWS IoT Core

🔒 Blockchain-backed data logging

🤝 Contributors
Priyanshu Sharma (12311900)

Shivanshu Singh (12315457)

Swapnil Nikhij (12313309)
