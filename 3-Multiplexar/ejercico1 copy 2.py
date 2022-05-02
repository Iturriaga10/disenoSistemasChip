"""
Ejercicio1 - 
by: David Iturriaga Sotelo
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

try:
    while True:
        print("LED ON")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(2)
        
        print("LED OFF")
        GPIO.output(18, GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
	print("Fin")
    
GPIO.cleanup()