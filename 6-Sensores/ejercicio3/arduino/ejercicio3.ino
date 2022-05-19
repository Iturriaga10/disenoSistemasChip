"""
Ejercicio3 - (Sensor Temperatura)
Escribe un programa en tu Raspberry que detecte la temperatura en al ambiente, la temperatura debe de ser mostrada en un LCD.
by: David Iturriaga Sotelo
"""

#define led 8
float valor;

void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  
  valor=analogRead(A1);
  Serial.println(valor);
  
  delay(200);
}