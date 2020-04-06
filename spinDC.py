import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class DCMove:

  def __init__(self,EN1,In1,In2):
    self.EN1 = EN1
    self.In1 = In1
    self.In2 = In2

    GPIO.setup(EN1, GPIO.OUT)
    GPIO.setup(In1, GPIO.OUT)
    GPIO.setup(In2, GPIO.OUT)

    GPIO.output(EN1, 0)
    GPIO.output(In1, 1)
    GPIO.output(In2, 0)

  def turnOn(self):
    GPIO.output(EN1, 1)

  def turnOff(self):
    GPIO.output(EN1, 0)