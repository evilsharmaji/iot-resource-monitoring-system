# 🌐 IoT-Integrated Resource Monitoring System

A real-time IoT-based solution to monitor essential resources like **water**, **energy**, and **inventory** using sensor networks, cloud-based analytics, and dashboards. This system integrates **ESP32**, **MQTT**, **Flask**, **InfluxDB**, **ML models**, and **Grafana/Plotly Dash** for complete insight and automation.

---

## 🚀 Features

- 📡 Real-time Data Acquisition (ESP32 + MQTT)
- 📊 Interactive Dashboards (Grafana / Plotly Dash)
- ⚠️ Anomaly Detection (Isolation Forest)
- 🔮 Predictive Analytics (LSTM + TensorFlow)
- 📲 SMS/Email Alerts (Twilio / AWS SNS)
- 🐳 Docker-Ready Deployment

---

## 🏗️ System Architecture


**Data Flow**:
```
ESP32 Sensors → MQTT → Flask API → InfluxDB → ML Models → Dashboard/Alerts
```

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
```


---

### 2️⃣ Backend & ML Engine

- **API**: Flask API receives data from sensors  
- **Database**: InfluxDB for time-series storage  
- **ML Models**:
  - Isolation Forest for anomaly detection  
  - LSTM (TensorFlow) for forecasting  



---

### 3️⃣ Visualization & Alerts

- **Dashboards**: Real-time dashboards with Plotly Dash or Grafana  
- **Alerts**: Configurable thresholds trigger SMS/Email notifications



---

## 🧠 Machine Learning Highlights

### 🔍 Anomaly Detection (Isolation Forest):
```python
model = IsolationForest()
df['anomaly'] = model.fit_predict(df[['temperature', 'humidity', 'water_level']])
```

### 📈 Prediction (LSTM):
```python
model = Sequential()
model.add(LSTM(...))
model.fit(X_train, y_train)
```

---

## 🐳 Docker Deployment

```yaml
version: '3'
services:
  flaskapp:
    build: ./flask_app
    ports:
      - "5000:5000"
  influxdb:
    image: influxdb
    ports:
      - "8086:8086"
```

---

## 📁 Folder Structure

```
iot-resource-monitoring/
├── esp32/                  # ESP32 sensor code (C++)
├── flask_app/              # Flask backend and ML scripts
├── dashboard/              # Dash or Grafana visualization
├── docker-compose.yml
├── README.md
└── images/                 # System diagrams and screenshots
```

---

## 📲 Alert Example (Twilio SMS)

> "🚨 Alert: Water level dropped below threshold at 14:22."

---

## 📚 References

- [MQTT](https://mqtt.org/)
- [Grafana](https://grafana.com/)
- [InfluxDB](https://www.influxdata.com/)
- [Twilio SMS API](https://www.twilio.com/docs/sms)
- [TensorFlow](https://www.tensorflow.org/)

---

## ✨ Future Enhancements

- 🤖 Edge AI with TensorFlow Lite on ESP32
- ☁️ Multi-Tenant SaaS with AWS IoT Core
- 🔐 Blockchain for tamper-proof logs

---

## 🤝 Contributors

- Priyanshu Sharma (12311900)
- Shivanshu Singh (12315457)
- Swapnil Nikhij (12313309)

---

