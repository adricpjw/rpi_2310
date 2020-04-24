import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class DCMove:

  def __init__(self,EN1,In1,In2):
    # Can be used for Enable2, Input3, Input4 as well
    # Note that GPIO mode is set to BOARD
    self.EN1 = EN1 #Enable 1
    self.In1 = In1 #Input 1
    self.In2 = In2 #Input 2

    GPIO.setup(EN1, GPIO.OUT)
    GPIO.setup(In1, GPIO.OUT)
    GPIO.setup(In2, GPIO.OUT)

    # Default state = Off
    # Reverse wiring polarity to spin opposite direction
    GPIO.output(EN1, 0)
    GPIO.output(In1, 1)
    GPIO.output(In2, 0)

  def turnOn(self):
    GPIO.output(EN1, 1)

  def turnOff(self):
    GPIO.output(EN1, 0)