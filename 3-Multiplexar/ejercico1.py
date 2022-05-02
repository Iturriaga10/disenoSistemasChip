"""
Ejercicio1 - 
by: David Iturriaga Sotelo
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

segments = (24,12,19,21,23,22,15)

for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 1)

digits = (26,18,16,13)

for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, 0)

num =  {' ':(1,1,1,1,1,1,1),
        '0':(0,0,0,0,0,0,1),
        '1':(1,0,0,1,1,1,1),
        '2':(0,0,1,0,0,1,0),
        '3':(0,0,0,0,1,1,0),
        '4':(1,0,0,1,1,0,0),
        '5':(0,1,0,0,1,0,0),
        '6':(0,1,0,0,0,0,0),
        '7':(0,0,0,1,1,1,1),
        '8':(0,0,0,0,0,0,0),
        '9':(0,0,0,0,1,0,0)}

try:
        while True:
            x = [num['4'], num['5'], num['6'], num['9']]
            
            for digit in range(4):
                GPIO.output(digits[digit], 1)
                GPIO.output(segments, x[digit])
                
                time.sleep(0.001)
                GPIO.output(digits[digit], 0)
        

except KeyboardInterrupt:
        GPIO.cleanup()

----------

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
