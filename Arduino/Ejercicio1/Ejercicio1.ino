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

void leerDatos();
void actualizarSenalesDigitales();
void leerSenalesAnalog();

void setup() {

  // Puerto Serie
  
  pinMode(DI0, INPUT);
  pinMode(DI1, INPUT);

  pinMode(DO0, OUTPUT);
  pinMode(DO1, OUTPUT);

  // Configuracion del puerto serie
  Serial.begin(9600);

  // Temporizadores
    TON[0].tiempo = (unsigned long)1 * 400;
}

void loop() {



  // Procesando la comunicación
  leerDatos();

  
  Y0 = X0;
  actualizarSenalesDigitales();
  leerSenalesAnalog();


  //   
  // TON[0].entrada = ###########;    // Señal de entrada al TON
  // actualizarTON(0);

}

void leerDatos() {
  byte caracter = 0;
  while(Serial.available() > 0) {
    caracter = Serial.read();
    Serial.write(caracter + 10);
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
