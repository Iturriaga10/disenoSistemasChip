import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (8,18,10,9,11,25,22)

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
    
for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 1)

digits = (7,24,23,27)

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
        '9':(0,0,0,0,1,0,0),
        'A':(0,0,0,1,0,0,0),
        'B':(1,1,0,0,0,0,0),
        'C':(0,1,1,0,0,0,1),
        'D':(1,0,0,0,0,1,0),
        '*':(1,1,1,1,1,1,1),
        '#':(1,0,0,1,0,0,0)}

x = [num[' '], num[' '], num[' '], num[' ']]
position = 0

try:
        while True:
            
            for j in range(4):
                GPIO.output(ColumnaPin[j], 0)
                for i in range(4):
                    if (GPIO.input(FilaPin[i]) == 0):
                        print(Tecla[i][j])
                        x[position] = num[str(Tecla[i][j])]
                        
                        if position >= 3:
                            position = 0
                        else:
                            position +=1
                        while(GPIO.input(FilaPin[i]) == 0):
                            pass
                        
                GPIO.output(ColumnaPin[j], 1)    
            
            for digit in range(4):
                GPIO.output(digits[digit], 1)
                GPIO.output(segments, x[digit])
                
                time.sleep(0.001)
                GPIO.output(digits[digit], 0)
        
            
            
            

except KeyboardInterrupt:
        GPIO.cleanup()

