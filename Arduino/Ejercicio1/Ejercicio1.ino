
// Temporizadores

#define  numeroDeTON 16
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
int DO5 = 2;


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

int VA0 = 0;
int VA1 = 0;
int VA2 = 0;

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
  Serial.begin(9600);

  // Temporizadores
  TON[0].tiempo = (unsigned long) 1000;
  TON[1].tiempo = (unsigned long) 500;
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
  
  //Y0 = TON[0].salida;
  //Y1 = !Y0;
  Y0 = X0;
  Y1 = X1;
  Y2 = X2;
  Y3 = X3;
  Y4 = X4;
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
