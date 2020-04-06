import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

class servoMove:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)

    def act(self):
        pwm = GPIO.PWM(pin,50)
        pwm.start(0)
        pwm.ChangeDutyCycle(7)
        time.sleep(5)
        pwm.ChangeDutyCycle(2)
        
    def cleanup(self):
        GPIO.cleanup()

#sero
servo_point = 22
GPIO.setup(servo_point,GPIO.OUT)
pwm = GPIO.PWM(servo_point,50)
pwm.start(0)
pwm.ChangeDutyCycle(7)
time.sleep(5)
pwm.ChangeDutyCycle(2)