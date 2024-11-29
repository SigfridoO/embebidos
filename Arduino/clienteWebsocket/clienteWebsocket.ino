#include <WiFi.h>
#include <ArduinoWebsockets.h>
// by Gil Maimon

//using namespace websockets;

websockets::WebsocketsClient clientWebsocket;

const char* ssid = "ardilluda2";
const char* password = "01971101";
const char* server = "ws://192.168.0.115:8000/ws/chat/python/";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  
  Serial.println("");
  Serial.println("Conexion establecida");
  Serial.println("Dirección IP");
  Serial.println(WiFi.localIP());
  Serial.print("\nWi-Fi conectado.");

  if (clientWebsocket.connect(server)) {
    Serial.println("Conectado al servidor Websocket");
  }

  clientWebsocket.onMessage([](websockets::WebsocketsMessage message) {
      Serial.print("Mensaje recibido: ");
      Serial.print(message.data());
  });

  // Enviar mensaje inicial
  clientWebsocket.send("{\"type\": \"chat.message\", \"name\": \"arduino\", \"text\": \"hola\" }");

}

void loop() {
  // put your main code here, to run repeatedly:

}
