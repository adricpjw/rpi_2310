import RPi.GPIO as GPIO    
import time
from Stepper import StepperMove

GPIO.setmode(GPIO.BOARD)

#stepper motor
A1 =12 
A2 =11
B1 =13
B2 =15

mover = StepperMove(A1,A2,B1,B2)
mover.up(0.03,10)
mover.cleanup()
