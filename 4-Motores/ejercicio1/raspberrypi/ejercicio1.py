"""
Ejercicio1 - Escribe un programa en tu Raspberry que controle el giro de un vehículo mediante el uso de un joystick.
A) Joystick derecha -> Motor 1, Giro derecha
B) Joystick izquierda-> Motor 1, Giro izquierda
C) Joystick arriba -> Motor 2, Giro derecha
D) Joystick abajo -> Motor 2, Giro izquierda
by: David Iturriaga Sotelo
"""

import serial
import RPi.GPIO as GPIO
import time

arduino=serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1.0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

motores=(2,3,4,14)

for motor in motores:
    GPIO.setup(motor, GPIO.OUT)
    GPIO.output(motor,0)


while True:
    val=arduino.read()
    str_val=str(val,'UTF-8', errors='ignore')
    #print(str_val)
    if (str_val=="1"):
        GPIO.output(motores,(0,1,0,1))
        time.sleep(.1)
        print("Left")
    if (str_val=="2"):
        GPIO.output(motores,(1,0,1,0))
        time.sleep(.1)
        print("Right")
    if (str_val=="3"):
        GPIO.output(motores,(0,1,1,0))
        time.sleep(.1)
        print("Down")
    if (str_val=="4"):
        GPIO.output(motores,(1,0,0,1))
        time.sleep(.1)
        print("Up")
    GPIO.output(motores,0)
arduino.close()