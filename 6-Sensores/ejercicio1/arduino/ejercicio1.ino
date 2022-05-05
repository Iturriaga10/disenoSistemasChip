"""
Ejercicio1 - Escribe un programa en tu Raspberry que mueva un motor a pasos.
A) Por pasos Derecha / Izquierda
B) Continuó Derecha / Izquierda 
by: David Iturriaga Sotelo
"""

void setup() {
Serial.begin(9600);
}

void loop() {
  int value = analogRead(A0);  
  if(value > 350){
    Serial.println("On");
    }
  else{
    Serial.println("Off");
    }
  
  delay(250);
}
