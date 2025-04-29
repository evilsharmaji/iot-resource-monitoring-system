import pandas as pd
from sklearn.ensemble import IsolationForest
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('iot_data')

query = 'SELECT * FROM "resources" ORDER BY time DESC LIMIT 100'
results = client.query(query)
points = list(results.get_points())

df = pd.DataFrame(points)
model = IsolationForest(contamination=0.1)
df['anomaly'] = model.fit_predict(df[['temperature', 'humidity', 'water_level']])
anomalies = df[df['anomaly'] == -1]
print(anomalies)
