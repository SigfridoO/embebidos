// EEPROM
#include <EEPROM.h>


// Temporizadores

#define  numeroDeTON 32
struct temporizador {
    byte entrada;
    byte salida;
    unsigned long tiempo;
    unsigned long tiempoActual;
} TON[numeroDeTON];
struct temporizadorAux {
    byte bandera;
    unsigned long tiempo_Aux1;
    unsigned long tiempo_Aux2;
} TON_Aux[numeroDeTON];

void actualizarTON (int);

// Digitales
int DI0 = 36;
int DI1 = 39;
int DI2 = 34;
int DI3 = 35;
int DI4 = 13;


int DO0 = 26;
int DO1 = 27;
int DO2 = 14;
int DO3 = 12;
int DO4 = 9;
int DO5 = 2;  // LED DE LA tarjeta ESP-32


// Analogicas
int AI0 = 32;
int AI1 = 33;
int AI2 = 25;

//Variables
int X0;
int X1;
int X2;
int X3;
int X4;

int Y0;
int Y1;
int Y2;
int Y3;
int Y4;
int Y5;

// variables virtuales
#define NUMERO_RC 80
int RC[NUMERO_RC];

#define NUMERO_M 80
int M[NUMERO_M];

int VA0 = 0;
int VA1 = 0;
int VA2 = 0;

#define numeroAnalog 3
float m[numeroAnalog];
float b[numeroAnalog];


void actualizarSenalesDigitales();
void leerSenalesAnalog();

// Comunicación
/*
 *  CI|R  I  E |TI|NU|DATOS .....................  |LG|V| CF
    00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18
    CI -- Caracter Inicial
    TI    Tipo de instrucción
    NU    Numero de instrucción
    LG   Longitud
    V  Verificación
    CF  Caracter f
*/

#define bufferIndiceMaximo 120
byte bufferLectura[bufferIndiceMaximo];
int bufferIndice = 0;

byte bufferInstruccion[bufferIndiceMaximo];
int bufferIndiceInstruccion = 0;

void leerInstruccionDeBuffer(byte *, int *, byte *, int *);
void obtenerInstruccion();

char caracterDeInicio = '*';
char caracterDeFin = '?';

void colocarDatosEnBuffer();
void imprimirTrama(byte *, int , int );
byte obtenerByteDeArregloByte(byte* );


#define ADMINISTRACION 48 // 0
#define SOLICITAR_VERSION 49  //1
#define ENVIAR_VERSION 50   //2


#define CONTROL 49        // 1
#define SOLICITAR_TEMPERATURA 49 //1
#define ENVIAR_TEMPERATURA 50 //2
#define MOD_BANDERA 52 //4


void enviarTemperatura();

// Memoria EEPROM
#define TAMANIO_MEMORIA_EEPROM 512
#define EEPROM_ANALOG 0 

void escribirVariablesAnalogicasEnEEPROM (int, float, float);
void leerVariablesAnalogicasEnEEPROM (int);

int obtenerDireccionMemoriaEEPROM(int);


// Serial1
#define TXD1 21
#define RXD1 19

HardwareSerial mySerial(1);

// Comunicación WIFI
#include <WiFi.h>
#include <WiFiClient.h>

//const char* ssid="ardilluda2";
const char* ssid="ardilluda";
const char* password = "01971101";

const char* server_ip = "192.168.0.115";
const int server_port = 65440;

WiFiClient cliente;

enum EstadoWifi {
  SIN_CONEXION = 0,
  CONECTANDO = 1,
  CONEXION_ESTABLECIDA = 2,
  CLIENTE_DESCONECTADO = 3,
  CLIENTE_COMUNICADO = 4
};
EstadoWifi estadoConexionWifi = SIN_CONEXION;

void controlWifi(void *);

// Comunicacion Bluetooth

void setup() {

  // Puerto Serie
  
  pinMode(DI0, INPUT);
  pinMode(DI1, INPUT);
  pinMode(DI2, INPUT);
  pinMode(DI3, INPUT);
  pinMode(DI4, INPUT);

  pinMode(DO0, OUTPUT);
  pinMode(DO1, OUTPUT);
  pinMode(DO2, OUTPUT);
  pinMode(DO3, OUTPUT);
//  pinMode(DO4, OUTPUT);
//  pinMode(DO5, OUTPUT);

  // Configuracion del puerto serie
  Serial.begin(115200);

  mySerial.begin(115200, SERIAL_8N1, RXD1, TXD1);

  
  EEPROM.begin(TAMANIO_MEMORIA_EEPROM);
  escribirVariablesAnalogicasEnEEPROM(2, 34.5, -3.45); // (indice, m, b)
  leerVariablesAnalogicasEnEEPROM (2);

  // Temporizadores
  TON[0].tiempo = (unsigned long) 1000;
  TON[1].tiempo = (unsigned long) 500;



  TON[24].tiempo = (unsigned long) 1000; // Temporizador para Wifi
  // Tarea para el manejo de la comunicación WIFI
  xTaskCreatePinnedToCore(controlWifi, "ControlWifi", 8192, NULL, 1, NULL, 0);
}




void loop() {



  // Procesando la comunicación
  colocarDatosEnBuffer();
  leerInstruccionDeBuffer(bufferLectura, &bufferIndice, bufferInstruccion, &bufferIndiceInstruccion);


  // Temporizador
  TON[0].entrada = !TON[1].salida;
  actualizarTON(0);

  TON[1].entrada = TON[0].salida;
  actualizarTON(1);
  
  Y4 = TON[0].salida;
  //Y1 = !Y0;
  RC[0] = (X0||RC[0]||M[0]) && !X1 & !M[1];
  Y0 = RC[0];

  // Reseteo de las variables digitales virtuales
  M[0]=0;
  M[1]=0;
  //Y1 = X1;
  //Y2 = X2;
  //Y3 = X3;
  //Y4 = X4;
  //Serial.println(TON[1].tiempoActual);
  
  actualizarSenalesDigitales();
  leerSenalesAnalog();



}

void colocarDatosEnBuffer() {
  byte caracter = 0;
  int aux = 0;
  while(Serial.available() > 0) {
    caracter = Serial.read();
    bufferLectura[bufferIndice++] = caracter;

    if (bufferIndice  + 1 > bufferIndiceMaximo) {
      aux = bufferIndiceMaximo >> 1;
      for (int i = aux; i < bufferIndiceMaximo + 1; i++) {
        bufferIndice = i - aux;
        bufferLectura[bufferIndice] = bufferLectura[i];
      }
    }
  }
  //imprimirTrama(bufferLectura, 0, bufferIndice);
}

void imprimirTrama(byte *ptrTrama, int inicio, int tamanio) {
  Serial.print("\n>>");
  for (int k = inicio; k < inicio + tamanio ; k++) {
    Serial.write(ptrTrama[k]);
  }
}

void leerInstruccionDeBuffer(byte *ptrBufferLectura, int *ptrBufferIndice, byte *ptrBufferInstruccion, 
  int *ptrTamanioBufferInstruccion) {
    int i  = 0;
    int k = 0;

    int encontrado = -1;

    if (ptrBufferLectura[*ptrBufferIndice-1] == caracterDeFin) {
      for (k = *ptrBufferIndice; k >= 0; --k) {
        if (ptrBufferLectura[k] == (byte) caracterDeInicio) {
          encontrado = k; 
          //Serial.print(encontrado);
          if (encontrado >= 0) {
            *ptrTamanioBufferInstruccion = 0;

            for(int j = k; j < *ptrBufferIndice; j++) {
              ptrBufferInstruccion[*ptrTamanioBufferInstruccion] = ptrBufferLectura[j];
              (*ptrTamanioBufferInstruccion )++;
              
            }
            //imprimirTrama(ptrBufferInstruccion,0, *ptrTamanioBufferInstruccion );
            obtenerInstruccion();
            *ptrBufferIndice = k;
          }
          
        }
        
      }
    }
    
 }


void obtenerInstruccion(){
  int *tamanio;
  byte *cadena;

  int tipoDeInstruccion = 0;
  int numeroDeInstruccion = 0;

  tamanio = &bufferIndiceInstruccion;
  cadena = bufferInstruccion;

  tipoDeInstruccion =obtenerByteDeArregloByte(cadena + 4);
  numeroDeInstruccion = obtenerByteDeArregloByte(cadena + 5);
  //Serial.print(*tamanio);
//  Serial.print("TI: ");
//  Serial.print(tipoDeInstruccion);
//  Serial.print(" NI: ");
//  Serial.print(numeroDeInstruccion);
//  Serial.print("<<");

  byte indice = 0;
  byte valor = 0;

  switch(tipoDeInstruccion){
    
    case ADMINISTRACION:
        switch(numeroDeInstruccion) {
          case SOLICITAR_VERSION:
            Serial.print("La version es 0.0.1 ESP32 Sigfrido");
            break;
        }
        break;
      
    case CONTROL:
        switch(numeroDeInstruccion) {
          case SOLICITAR_TEMPERATURA:
            enviarTemperatura();
            break;

          case MOD_BANDERA:
            indice =obtenerByteDeArregloByte(cadena + 6) ;
            valor = obtenerByteDeArregloByte(cadena + 7) ;

            M[indice] = valor;
           break;
        }
      break;
  }
}

void enviarTemperatura() {
  //Serial.print("La temperatura es: ");
  Serial.print(VA0 /7.5);
}

byte obtenerByteDeArregloByte(byte* arreglo) {
  byte *punteroByte;
  punteroByte = (byte *) arreglo;
  return *punteroByte;
}


void actualizarSenalesDigitales() {
  X0 = digitalRead(DI0);
  X1 = digitalRead(DI1);
  X2 = digitalRead(DI2);
  X3 = digitalRead(DI3);
  X4 = digitalRead(DI4);
  
  digitalWrite(DO0, Y0);
  digitalWrite(DO1, Y1);
  digitalWrite(DO2, Y2);
  digitalWrite(DO3, Y3);
  digitalWrite(DO4, Y4);
  digitalWrite(DO5, Y5);
}

void leerSenalesAnalog() {
  VA0 = analogRead(AI0);
}



// Temporizadores

void actualizarTON (int i) {
     if (TON [i].entrada)
   {
        if (!TON_Aux[i].bandera) {
           TON_Aux[i].bandera = true;
           TON_Aux[i].tiempo_Aux1 = millis ();  
        }
        TON_Aux[i].tiempo_Aux2 = millis ();
        TON [i].tiempoActual = TON_Aux[i].tiempo_Aux2 - TON_Aux[i].tiempo_Aux1;

        if (TON [i].tiempoActual > TON [i].tiempo) {
            TON [i].salida = true;
        }
    } else {
        TON [i].salida = false;
        TON_Aux[i].bandera = false;
    }

}

// EEPROM
void escribirVariablesAnalogicasEnEEPROM (int indice, float m, float b) {
  int direccion1 = 2 * indice * sizeof(float) + obtenerDireccionMemoriaEEPROM(EEPROM_ANALOG);
  int direccion2 = (2 * indice + 1 )* sizeof(float) + obtenerDireccionMemoriaEEPROM(EEPROM_ANALOG);

  Serial.print("Imprimiendo VA ");
  Serial.print(indice);
  Serial.print(" ");
  Serial.print(direccion1);
  Serial.print(" ");
  Serial.print(m);
  Serial.print("\t\t");
  Serial.print(direccion2);
  Serial.print(" ");
  Serial.print(b);
  Serial.print("\n");

  EEPROM.writeFloat(direccion1, m);
  EEPROM.writeFloat(direccion2, b);

  EEPROM.commit();
  
}


void leerVariablesAnalogicasEnEEPROM (int indice) {
  float m = 0;
  float b = 0;

  
  int direccion1 =  2 * indice * sizeof(float) + obtenerDireccionMemoriaEEPROM(EEPROM_ANALOG);
  int direccion2 = (2 * indice + 1 )* sizeof(float) + obtenerDireccionMemoriaEEPROM(EEPROM_ANALOG);

   m = EEPROM.readFloat(direccion1);
   b = EEPROM.readFloat(direccion2);


  Serial.print("Leyendo VA-");
  Serial.print(indice);
  Serial.print(" ");
  Serial.print(direccion1);
  Serial.print(" ");
  Serial.print(m);
  Serial.print("\t\t");
  Serial.print(direccion2);
  Serial.print(" ");
  Serial.print(b);
  Serial.print("\n");
 
}


int obtenerDireccionMemoriaEEPROM(int opcion) {
  int direccionInicial = 0;
  switch(opcion) {
    case EEPROM_ANALOG:
      direccionInicial = 0;    
      break;
  }
  return direccionInicial;
}

// -------------------- Wifi
void controlWifi(void *pvParametros) {
    
  EstadoWifi estadoActual;
  while(true) {

    // Manejo de la conexión wifi
    RC[60] = (M[60] || RC[60]) && !M[61];

    // Manejo de la conexión con el servidor socket
    RC[61] = RC[60] & (M[62] || RC[61]) && !M[63];


    M[60] = 0;
    M[61] = 0;

    M[62] = 0;
    M[63] = 0;

    // Temporizador
    TON[24].entrada = !TON[24].salida;
    actualizarTON(24);
    
    if (TON[24].salida) {
  
      mySerial.print("Estado conexion: ");
      mySerial.print(estadoConexionWifi);

      mySerial.print(" RC[60]: ");
      mySerial.print(RC[60]);

      mySerial.println();
      
      estadoActual = estadoConexionWifi;
      
      switch(estadoActual) {
        case SIN_CONEXION:
          if (RC[60]) {
            estadoConexionWifi = CONECTANDO;
            mySerial.println("Conectando a la red");
            WiFi.begin(ssid, password);
            //estadoConexionWifi = RC[60] ? CONECTANDO : SIN_CONEXION;
          }
          break;

        case CONECTANDO:

          if (RC[60]) {
             if (WiFi.status() != WL_CONNECTED){
              mySerial.print(".");
            } else {
              estadoConexionWifi = CONEXION_ESTABLECIDA;
              mySerial.println("");
              mySerial.println("Conexion establecida");
              mySerial.println("Dirección IP");
              mySerial.println(WiFi.localIP());
            }
          } else {
            estadoConexionWifi = SIN_CONEXION;
            WiFi.disconnect();
          }
          break;
        
        case CONEXION_ESTABLECIDA:

          if (RC[60]) {
            if (RC[61]) {
                if (!cliente.connected()){
                    Serial.print("Conexión perdidad, reconectando");
                    cliente.connect(server_ip, server_port);
                } else {
                    estadoConexionWifi = CLIENTE_COMUNICADO;
                }
            } 
            
          } else {
            estadoConexionWifi = SIN_CONEXION;
            WiFi.disconnect();
          }
          break;
        
        
        case CLIENTE_DESCONECTADO:
        
          break;
        
        case CLIENTE_COMUNICADO:
          break;
        

      }
    
    } // fin del if
      
  delay(1);
  }
  
}
