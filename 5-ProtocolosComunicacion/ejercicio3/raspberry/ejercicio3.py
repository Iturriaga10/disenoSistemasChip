from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

led_status = False

@app.route("/")
def turnon_led():

    if led_status:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    
    not led_status
    
    return "Success"