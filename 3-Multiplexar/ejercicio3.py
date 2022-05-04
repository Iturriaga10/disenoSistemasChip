"""
Ejercicio3 - Diseñar un circuito electrónico capaz de tomar información de un teclado matricial y mostrar los numero en los displays de 7 segmentos que construye en el ejercicio 1.
by: David Iturriaga Sotelo
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Filas = 4    #NUMERO DE FILAS
#Columnas = 4    #NUMERO DE COLUMNAS
Tecla = [['1','2','3','A'],
         ['4','5','6','B'],
         ['7','8','9','C'],
         ['*','0','#','D']]

FilaPin = [6,13,19,26]
ColumnaPin = [21,20,16,12]

for j in range(4):
    GPIO.setup(ColumnaPin[j], GPIO.OUT)
    GPIO.output(ColumnaPin[j], 1)

for i in range(4):
    GPIO.setup(FilaPin[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
try:
        while(True):
            for j in range(4):
                GPIO.output(ColumnaPin[j], 0)
                
                for i in range(4):
                    if (GPIO.input(FilaPin[i]) == 0):
                        print(Tecla[i][j])
                        while(GPIO.input(FilaPin[i]) == 0):
                            pass
                        
                GPIO.output(ColumnaPin[j], 1)
                
except KeyboardInterrupt:
    GPIO.cleanup()
