import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)

# Input 23 - input for energy counter
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def pin23callback(channel):
    try:
        args = {'add': 1}
        r = requests.post('http://malina.local:5000/EnergyCounterAddPulses', args)
        print(r.text);
    except:
        print('Request was not sent propperly')
    
GPIO.add_event_detect(23, GPIO.FALLING, callback=pin23callback, bouncetime=300)