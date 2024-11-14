#include <WiFi.h>

// Configuración de la red WiFi
const char* ssid = "ardilluda2";
const char* password = "01971101";

// Configuración del servidor en el puerto 65432
WiFiServer server(65432);
int currentPort = 65432; // Variable para almacenar el puerto actual

// Pines de los LEDs y botones
const int LedVerde = 21;
const int LedAmarillo = 22;
const int LedRojo = 23;
const int LedPrender = 18;
const int LedEncender = 19;

const int BotonEncenderLED = 14;
const int BotonPrenderLED = 13;

// Variables adicionales para el manejo de los comandos y el control de tiempos
bool buttonPressed = false;
bool firstButtonPressed = false;
bool clientConnected = false;
bool botonEncenderPresionado = false;  // Estado de si el botón está presionado
WiFiClient client;
unsigned long botonPreviousMillis = 0;
unsigned long previousMillis = 0;
const unsigned long debounceDelay = 50;

// Variables para el sistema "keep-alive"
unsigned long lastReceiveTime = 0;
const unsigned long connectionTimeout = 30000;  // Tiempo de espera de 30 segundos

// Estados del semáforo
enum State {
  VERDE,
  AMARILLO,
  ROJO
};

State currentState = VERDE;
unsigned long semaforoPreviousMillis = 0;
unsigned long previousAmarilloMillis = 0;
const unsigned long intervalVerde = 10000;
const unsigned long intervalRojo = 12000;

void setup() {
  Serial.begin(115200);

  // Configuración de los pines de los LEDs y botones
  pinMode(LedVerde, OUTPUT);
  pinMode(LedAmarillo, OUTPUT);
  pinMode(LedRojo, OUTPUT);
  pinMode(LedPrender, OUTPUT);
  pinMode(LedEncender, OUTPUT);

  pinMode(BotonEncenderLED, INPUT);
  pinMode(BotonPrenderLED, INPUT);

  // Conexión a la red WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConectado a WiFi");
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());

  // Iniciar el servidor y confirmar el puerto
  server.begin();
  Serial.print("Servidor iniciado en el puerto: ");
  Serial.println(currentPort);

  // Crear las tareas en los diferentes núcleos del ESP32
  xTaskCreatePinnedToCore(clientCommunicationTask, "ClientCommunication", 10000, NULL, 1, NULL, 0);
  xTaskCreatePinnedToCore(semaphoreTask, "SemaphoreControl", 10000, NULL, 1, NULL, 1);
}

void loop() {
  // El loop principal queda vacío, ya que todas las tareas están manejadas en los hilos
}

void clientCommunicationTask(void *pvParameters) {
  for (;;) {
    handleClientConnection();
    handleButtonLeds(millis());
    handleButtonHeld(); // Detección de botón presionado
    vTaskDelay(10 / portTICK_PERIOD_MS);  // Pequeño retardo para evitar consumo alto de CPU
  }
}

void semaphoreTask(void *pvParameters) {
  for (;;) {
    updateSemaforo(millis());
    vTaskDelay(10 / portTICK_PERIOD_MS);  // Retardo para evitar consumo alto de CPU
  }
}

void handleClientConnection() {
  if (!client || !client.connected()) {
    client = server.available();
    if (client) {
      clientConnected = true;
      Serial.println("Cliente conectado.");
      client.setTimeout(60000);  // Aumenta el tiempo de espera a 60 segundos
      lastReceiveTime = millis();  // Marca el tiempo de la conexión inicial
      
      // Enviar el estado actual de los LEDs al cliente al conectarse
      enviarEstadoLeds();
    }
  }

  if (client && client.connected() && client.available()) {
    String comando = client.readStringUntil('\n');
    comando.trim();
    Serial.print("Comando recibido: ");
    Serial.println(comando);

    if (comando == "KEEP_ALIVE") {
      lastReceiveTime = millis();  // Actualiza el tiempo de la última recepción
    } else if (comando == "BUTTON_PRESSED") {
      buttonPressed = true;
    } else if (comando == "PRIMER_BOTON") {
      firstButtonPressed = true;
    }
  }

  if (clientConnected && !client.connected()) {
    clientConnected = false;
    buttonPressed = false;
    firstButtonPressed = false;
    Serial.println("Cliente desconectado.");
  }
}

void handleButtonLeds(unsigned long currentMillis) {
  if (digitalRead(BotonEncenderLED) == LOW) {
    digitalWrite(LedEncender, HIGH);
  } else {
    digitalWrite(LedEncender, LOW);
  }

  // Verificar y enviar el estado de LedPrender cuando cambia el BotonPrenderLED
  if (digitalRead(BotonPrenderLED) == LOW) {
    digitalWrite(LedPrender, HIGH);
    enviarEstadoLeds();  // Enviar estado actualizado
  } else {
    digitalWrite(LedPrender, LOW);
    enviarEstadoLeds();  // Enviar estado actualizado
  }

  if (buttonPressed) {
    if (currentMillis - botonPreviousMillis >= debounceDelay) {
      digitalWrite(LedEncender, HIGH);
      delay(500);
      digitalWrite(LedEncender, LOW);
      buttonPressed = false;
      botonPreviousMillis = currentMillis;
    }
  }

  if (firstButtonPressed) {
    if (currentMillis - botonPreviousMillis >= debounceDelay) {
      digitalWrite(LedPrender, HIGH);
      delay(500);
      digitalWrite(LedPrender, LOW);
      firstButtonPressed = false;
      botonPreviousMillis = currentMillis;
    }
  }
}

void handleButtonHeld() {
  bool currentButtonState = digitalRead(BotonEncenderLED) == LOW;

  if (currentButtonState && !botonEncenderPresionado) {
    botonEncenderPresionado = true;
    if (client) client.println("BUTTON_HELD");
  } else if (!currentButtonState && botonEncenderPresionado) {
    botonEncenderPresionado = false;
    if (client) client.println("BUTTON_RELEASED");
  }
}

void enviarEstadoLeds() {
  if (client && client.connected()) {
    String estadoRojo = String(digitalRead(LedRojo));       // "1" si el LED rojo está encendido, "0" si está apagado
    String estadoAmarillo = String(digitalRead(LedAmarillo)); // "1" si el LED amarillo está encendido, "0" si está apagado
    String estadoVerde = String(digitalRead(LedVerde));     // "1" si el LED verde está encendido, "0" si está apagado
    String estadoPrender = String(digitalRead(LedPrender)); // Estado del LED Prender
    String estadoEncender = String(digitalRead(LedEncender)); // Estado del LED Encender
    String mensaje = "LED_ROJO:" + estadoRojo + ",LED_AMARILLO:" + estadoAmarillo + ",LED_VERDE:" + estadoVerde + ",LED_PRENDER:" + estadoPrender + ",LED_ENCENDER:" + estadoEncender;
    client.println(mensaje);  // Enviar estado de los LEDs
  }
}

void updateSemaforo(unsigned long currentMillis) {
  if (currentMillis - semaforoPreviousMillis >= 100) {
    semaforoPreviousMillis = currentMillis;

    switch (currentState) {
      case VERDE:
        digitalWrite(LedVerde, HIGH);
        digitalWrite(LedAmarillo, LOW);
        digitalWrite(LedRojo, LOW);
        enviarEstadoLeds();  // Envía el estado cuando cambia a verde
        if (currentMillis - previousMillis >= intervalVerde) {
          currentState = AMARILLO;
          previousMillis = currentMillis;
          previousAmarilloMillis = millis();
        }
        break;

      case AMARILLO:
        digitalWrite(LedVerde, LOW);
        digitalWrite(LedRojo, LOW);
        if (currentMillis - previousAmarilloMillis >= 600) {
          previousAmarilloMillis = currentMillis;
          digitalWrite(LedAmarillo, !digitalRead(LedAmarillo));

          static int blinkCountAmarillo = 0;
          if (digitalRead(LedAmarillo) == HIGH) {
            blinkCountAmarillo++;
          }

          if (blinkCountAmarillo >= 4) {
            digitalWrite(LedAmarillo, LOW);
            currentState = ROJO;
            previousMillis = currentMillis;
            blinkCountAmarillo = 0;
          }
        }
        break;

      case ROJO:
        digitalWrite(LedVerde, LOW);
        digitalWrite(LedAmarillo, LOW);
        digitalWrite(LedRojo, HIGH);
        enviarEstadoLeds();  // Envía el estado cuando el LED rojo cambia

        if (currentMillis - previousMillis >= intervalRojo) {
          currentState = VERDE;
          previousMillis = currentMillis;
        }
        break;
    }
  }
}
