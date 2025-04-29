#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define TRIGPIN 5
#define ECHOPIN 18

const char* ssid = "AIPROJECT";
const char* password = "PASSWORD789";
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32Client");
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(TRIGPIN, OUTPUT);
  pinMode(ECHOPIN, INPUT);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

float readWaterLevel() {
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  long duration = pulseIn(ECHOPIN, HIGH);
  return duration * 0.034 / 2;
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float level = readWaterLevel();

  String payload = "{\"temperature\":" + String(t) + ",\"humidity\":" + String(h) + ",\"water_level\":" + String(level) + "}";
  client.publish("iot/resources", payload.c_str());

  delay(5000);  // 5 sec interval
}
