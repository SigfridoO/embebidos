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
}

void loop() {



  // Procesando la comunicación
  leerDatos();

  
  Y0 = X0;
  actualizarSenalesDigitales();
  leerSenalesAnalog();

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
