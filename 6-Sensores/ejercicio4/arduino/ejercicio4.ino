"""
Ejercicio4 - Sensor Barrera (CNY)
Escribe un programa en tu Raspberry que simule un vehículo seguidor de línea.
by: David Iturriaga Sotelo
"""

#define led 8
float valor;

void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  valor=analogRead(A0);
  if (valor < 800){
    Serial.print(1);
    digitalWrite(led,HIGH);
  }
  else{
    Serial.print(2);
    digitalWrite(led,LOW);
  }
  delay(100);
}
