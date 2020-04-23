#!/usr/bin/env python
import RPi.GPIO as GPIO    
import time
from Stepper import StepperMove
from firing import servoMove
from spinDC import DCMove
import rospy
from std_msgs.msg import String

GPIO.setmode(GPIO.BOARD)

#stepper motor
A1 = 13 
A2 = 11
B1 = 15
B2 = 12

servo_pin = 22

EN1 = 37
In1 = 33
In2 = 36

mover = StepperMove(A1,A2,B1,B2)
servo = servoMove(servo_pin)
spinner = DCMove(EN1,In1,In2)

#Full Run Test:

#Stepper test:
try:
    mover.up(0.03,10)
    time.sleep(1)
    mover.down(0.03,5)
    time.sleep(1)
except:
    pass

try:
    servo.act()
except:
    pass

try:
    spinner.turnOn()
    time.sleep(3)
    spinner.turnOff()
    time.sleep(1)
except:
    pass

