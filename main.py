import RPi.GPIO as GPIO
import gpioHandling
import requests
import time

try:
    print("GPIO Handler started")
    while True:
      #pass
        args = {'add': 1}
        r = requests.post('http://127.0.0.1:5000/EnergyCounterAddPulses', args)
        print(r.text);
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
    
