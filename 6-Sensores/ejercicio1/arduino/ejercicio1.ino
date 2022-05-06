"""
Ejercicio1 - (Fotorresistencia)
Escribe un programa en tu Raspberry que simulé el funcionamiento de una lámpara nocturna. 
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
