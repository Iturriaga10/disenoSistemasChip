"""
Ejercicio3 - Escribe un programa en tu Raspberry que mueva un motor a pasos.
A) Por pasos Derecha / Izquierda
B) Continuó Derecha / Izquierda 
by: David Iturriaga Sotelo
"""

import RPi.GPIO as GPIO
import time

input_btn = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(input_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [GPIO.setup(2, GPIO.OUT),
        GPIO.setup(3, GPIO.OUT),
        GPIO.setup(4, GPIO.OUT),
        GPIO.setup(14, GPIO.OUT)]

FilaPin = [2,3,4,14]

secuencia = [[1,0,0,0],
             [0,1,0,0],
             [0,0,1,0],
             [0,0,0,1]]

secuencia2 = [[0,0,0,1],
              [0,0,1,0],
              [0,1,0,0],
              [1,0,0,0]]

while True:
    if GPIO.input(input_btn) == GPIO.LOW:
        for j in range(len(secuencia)):
            for i in range(len(pins)):
                #print(f' {FilaPin[i]} - {secuencia[j][i]}')
                GPIO.output(FilaPin[i], secuencia[j][i])
                time.sleep(.01)
            time.sleep(.001)
    elif GPIO.input(input_btn) == GPIO.HIGH:
        for j in range(len(secuencia2)):
            for i in range(len(pins)):
                #print(f' {FilaPin[i]} - {secuencia[j][i]}')
                GPIO.output(FilaPin[i], secuencia2[j][i])
                time.sleep(.01)
            time.sleep(.001)    
