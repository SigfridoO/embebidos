#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid="ardilluda2";
const char* password = "01971101";

const char* server_ip = "192.168.0.115";
const int server_port = 65440;

int contador = 0;

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

  if (cliente.available()){
    String respuesta = cliente.readStringUntil('\n');
    Serial.print("Respuesta del servidor : " + respuesta);
  }
  
  if (!cliente.connected()){
    Serial.print("Conexión perdidad, reconectando");
    cliente.connect(server_ip, server_port);
  }
  /*
  contador++;
  Serial.print("Contador: ");
  Serial.println(contador);

  cliente.print(contador);
  delay(1000);*/
  if (Serial.available() > 0 ){
    char buffer[64];
    int bytesRead = Serial.readBytesUntil('\n', buffer, sizeof(buffer) - 1);
    buffer[bytesRead] = '\0';
    cliente.print(String(buffer));
  }
}
