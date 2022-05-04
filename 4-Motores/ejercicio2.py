"""
Ejercicio2 - Escribe un programa en tu Raspberry que simulé el funcionamiento de un robot Araña.
by: David Iturriaga Sotelo
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)

LED = GPIO.PWM(12, 50)
duty = 0 
LED.start(duty)

try:
	while True:
		duty += 5
		if duty > 100:
			duty = 0
		LED.ChangeDutyCycle(duty)
		time(.05)
except KeyboardInterrupt:
	print("Fin")

LED.stop()
GPIO.cleanup()

