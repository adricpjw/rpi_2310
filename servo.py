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
        pwm.ChangeDutyCycle(12) #Turn 180 degrees
        time.sleep(3)
        pwm.ChangeDutyCycle(2) #Turn back
        
    def cleanup(self):
        GPIO.cleanup()

