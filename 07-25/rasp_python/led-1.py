import RPi.GPIO as GPIO
from time import sleep

PIN = 26
GPIO.setmode(GPIO .BCM)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)
try:
   while True:
       print(" LED ON \n")
       GPIO.output(PIN, 1)
       sleep(0.5)
       print(" LED OFF \n")
       GPIO.output(PIN, 0)
       sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()
