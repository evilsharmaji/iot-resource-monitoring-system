import dash
from dash import dcc, html
from influxdb import InfluxDBClient
import pandas as pd
import plotly.express as px

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('iot_data')

app = dash.Dash(__name__)

def fetch_data():
    query = 'SELECT * FROM "resources" ORDER BY time DESC LIMIT 100'
    results = client.query(query)
    df = pd.DataFrame(list(results.get_points()))
    return df

app.layout = html.Div([
    html.H1("IoT Resource Monitoring Dashboard"),
    dcc.Interval(id='update', interval=5000, n_intervals=0),
    dcc.Graph(id='live-graph')
])

@app.callback(
    dash.dependencies.Output('live-graph', 'figure'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_graph(n):
    df = fetch_data()
    fig = px.line(df, x='time', y=['temperature', 'humidity', 'water_level'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
