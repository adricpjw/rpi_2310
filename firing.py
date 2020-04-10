#!/usr/bin/env python
import RPi.GPIO as GPIO    
import time
from Stepper import StepperMove
from servo import servoMove
from spinDC import DCMove
import rospy
from std_msgs.msg import String

GPIO.setmode(GPIO.BOARD)

#stepper motor
A1 =13 
A2 =11
B1 =15
B2 =12

servo_pin = 22

EN1 = 37
In1 = 33
In2 = 36

mover = StepperMove(A1,A2,B1,B2)
servo = servoMove(servo_pin)
spinner = DCMove(EN1,In1,In2)

val = ''

def getSignal(msg):
    global val = msg


def move(signal):
    if signal == '-1':
        mover.down(0.03,2)
    elif signal == '1':
        mover.up(0.03,2)


def main():
    global val
    rospy.init_node('aimingNode',anonymous = True)

    rospy.Subscriber('cmd_stepper',String,getSignal)
    rate = rospy.Rate(10)

    toggle = True
    
    while toggle:
        if val != '10' and val:
            move(val)
        elif val == '10':
            spinner.turnOn()
            time.sleep(2)
            servo.act()
            time.sleep(3)
            toggle = False
            GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
            
