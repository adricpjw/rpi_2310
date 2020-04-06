import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

EN1 = 37
In1 = 36
In2 = 33

GPIO.setup(EN1, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

GPIO.output(EN1, 0)
GPIO.output(In1, 1)
GPIO.output(In2, 0)

def turnOn():
  GPIO.output(EN1, 1)

def turnOff():
  GPIO.output(EN1, 0)

try:
  turnOn()
  time.sleep(5)
  turnOff()
except KeyboardInterrupt:
  GPIO.cleanup()

GPIO.cleanup()
