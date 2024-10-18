#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid="ardilluda2";
const char* password = "01971101";

const char* server_ip = "192.168.0.105";
const int server_port = 65433;

WiFiClient cliente;

void setup() {
  Serial.begin(115200);

  Serial.println("Conectando a la red");
  WiFi.begin(ssid, password);

  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conexion establecida");
  Serial.println("Dirección IP");
  Serial.println(WiFi.localIP());
}

void loop() {
  

}
