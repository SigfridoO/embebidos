#include <WiFi.h>
#include <ArduinoWebsockets.h>

using namespace websockets;

const char* ssid = "TuRedWiFi";
const char* password = "TuContraseñaWiFi";
const char* server = "ws://echo.websocket.org";

WebsocketsClient client;

void setup() {
  Serial.begin(115200);

  // Conexión Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi conectado.");

  // Conexión WebSocket
  if (client.connect(server)) {
    Serial.println("Conectado al servidor WebSocket.");
  }

  // Configurar manejador de mensajes
  client.onMessage([](WebsocketsMessage message) {
    Serial.print("Mensaje recibido: ");
    Serial.println(message.data());
  });

  // Enviar un mensaje inicial
  client.send("¡Hola servidor!");
}

void loop() {
  client.poll();

  // Enviar un mensaje cada 5 segundos
  static unsigned long lastTime = 0;
  if (millis() - lastTime > 5000) {
    client.send("Ping desde ESP32.");
    lastTime = millis();
  }
}
