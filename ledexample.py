import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(18, GPIO.LOW)
time.sleep(5)
GPIO.output(18, GPIO.HIGH)
GPIO.cleanup()
time.sleep(2)
