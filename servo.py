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
        pwm.ChangeDutyCycle(12)
        time.sleep(3)
        pwm.ChangeDutyCycle(2)
        
    def cleanup(self):
        GPIO.cleanup()

