import RPi.GPIO as GPIO    
import time
import Stepper

GPIO.setmode(GPIO.BOARD)

#stepper motor
A1 = 
A2 = 
B1 = 
B2 = 

mover = StepperMove(A1,A2,B1,B2)
mover.up(0.03,10)
mover.cleanup()
