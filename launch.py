
import RPi.GPIO as GPIO    
import time

GPIO.setmode(GPIO.BOARD)

servo_point = 29
GPIO.setup(servo_point,GPIO.OUT)
pwm = GPIO.PWM(servo_point,50)
pwm.start(0)
pwm.ChangeDutyCycle(12)
time.sleep(3)
pwm.ChangeDutyCycle(2)
GPIO.cleanup()
