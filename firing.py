z#!/usr/bin/env python
import RPi.GPIO as GPIO    
import time
from Stepper import StepperMove
from servo import servoMove
from spinDC import DCMove
import rospy
from std_msgs.msg import String

GPIO.setmode(GPIO.BOARD)

# stepper motor GPIO Pins
A1 =13 
A2 =11
B1 =15
B2 =12

# servo GPIO Pin
servo_pin = 29

# L293D GPIO Pins
EN1 = 37
In1 = 33
In2 = 36

mover = StepperMove(A1,A2,B1,B2)
servo = servoMove(servo_pin)
spinner = DCMove(EN1,In1,In2)

val = ''

def getSignal(msg):
    global val
    val = msg.data

# Stepper movement up or down depending on camera feed 
def move(signal):
    if signal.data == '-1':
        mover.down(0.03,2)
        rospy.loginfo('Stepper moving up')
    elif signal.data == '1':
        mover.up(0.03,2)
        rospy.loginfo('Stepper moving down')

def main():
    global val
    rospy.init_node('aimingNode',anonymous = True)

    rospy.Subscriber('cmd_stepper',String,getSignal) #cmd_stepper published by targeting.py
    rate = rospy.Rate(10)
    
    toggle = True
    
    while toggle:
        if val != '10' and val: 
            move(val) 
        elif val == '10': # If payload is angled correctly
            rospy.loginfo('Calibration done! Firing')
            spinner.turnOn() # Turn on DC motors
            time.sleep(3) # Wait 3 seconds for DC Motors to full speed
            servo.act() # Use servos to push ball
            time.sleep(3)
            toggle = False
            GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
            
