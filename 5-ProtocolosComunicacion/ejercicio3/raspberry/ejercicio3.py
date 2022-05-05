from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

@app.route("/<int:led_status>")
def turnon_led(led_status):

    if led_status == 1 :
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    
    
    return "Success"