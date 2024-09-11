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
  Y1 = 1;
  delay(2000);
  actualizarSenalesDigitales();
  Y1 = 0;
  delay(2000);
  Y0 = X0;
  actualizarSenalesDigitales();
  leerSenalesAnalog();
  Serial.print("\nVA: ");
  Serial.print(VA0);
}

void actualizarSenalesDigitales() {
  X0 = digitalRead(DI0);
  
  digitalWrite(DO0, Y0);
  digitalWrite(DO1, Y1);
}

void leerSenalesAnalog() {
  VA0 = analogRead(AI0);
}
