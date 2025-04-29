from flask import Flask, request, jsonify
from influxdb import InfluxDBClient
import datetime

app = Flask(__name__)
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('iot_data')

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    point = [{
        "measurement": "resources",
        "tags": {"source": "ESP32"},
        "time": datetime.datetime.utcnow().isoformat(),
        "fields": {
            "temperature": float(data['temperature']),
            "humidity": float(data['humidity']),
            "water_level": float(data['water_level'])
        }
    }]
    client.write_points(point)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
