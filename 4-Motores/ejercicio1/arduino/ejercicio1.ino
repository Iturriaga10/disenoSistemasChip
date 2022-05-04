"""
Ejercicio1 - Escribe un programa en tu Raspberry que controle el giro de un vehículo mediante el uso de un joystick.
A) Joystick derecha -> Motor 1, Giro derecha
B) Joystick izquierda-> Motor 1, Giro izquierda
C) Joystick arriba -> Motor 2, Giro derecha
D) Joystick abajo -> Motor 2, Giro izquierda
by: David Iturriaga Sotelo
"""

#include <SoftwareSerial.h>

int X;        // variable para almacenar valor leido del eje X
int Y;        // variable para almacenar valor leido del eje y
int Z;

void setup(){
  Serial.begin(115200);
}

void loop(){
  
  X = analogRead(A0);     // lectura de valor de eje x
  Y = analogRead(A1);     // lectura de valor de eje x
  if (X <= 100){         // si X esta en la zona izquierda   
    Serial.print(1);
  }
  if(X >= 950){          // si X esta en la zona derecha
    Serial.print(2);
  }
  if (Y <= 100){         // si Y esta en la zona de abajo
    Serial.print(3);
  } 
  if (Y >= 950){          // si Y esta en la zona de arriba
    Serial.print(4);
  }      
  delay(100);
}
