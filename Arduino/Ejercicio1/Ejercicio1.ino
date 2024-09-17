
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

int DO0 = 26;
int DO1 = 14;

// Analogicas
int AI0 = 32;

//Variables
int X0;

int Y0;
int Y1;

int VA0 = 0;

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

void colocarDatosEnBuffer();
void imprimirTrama(byte *, int , int );

void setup() {

  // Puerto Serie
  
  pinMode(DI0, INPUT);
  pinMode(DI1, INPUT);

  pinMode(DO0, OUTPUT);
  pinMode(DO1, OUTPUT);

  // Configuracion del puerto serie
  Serial.begin(9600);

  // Temporizadores
  TON[0].tiempo = (unsigned long) 1000;
  TON[1].tiempo = (unsigned long) 500;
}

void loop() {



  // Procesando la comunicación
  colocarDatosEnBuffer();


  // Temporizador
  TON[0].entrada = !TON[1].salida;
  actualizarTON(0);

  TON[1].entrada = TON[0].salida;
  actualizarTON(1);
  
  Y0 = TON[0].salida;
  Y1 = !Y0;
  //Serial.println(TON[1].tiempoActual);
  
  actualizarSenalesDigitales();
  leerSenalesAnalog();



}

void colocarDatosEnBuffer() {
  byte caracter = 0;
  while(Serial.available() > 0) {
    caracter = Serial.read();
    bufferLectura[bufferIndice++] = caracter;
  }

  imprimirTrama(bufferLectura, 0, bufferIndice);
}

void imprimirTrama(byte *ptrTrama, int inicio, int tamanio) {
  Serial.print("\n>>");
  for (int k = inicio; k < inicio + tamanio ; k++) {
    Serial.write(ptrTrama[k]);
  }
}


void actualizarSenalesDigitales() {
  X0 = digitalRead(DI0);
  
  digitalWrite(DO0, Y0);
  digitalWrite(DO1, Y1);
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
