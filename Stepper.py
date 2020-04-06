import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class StepperMove:

    def __init__(self,A1,A2,B1,B2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2

    	GPIO.setup(self.A1, GPIO.OUT)
    	GPIO.setup(self.A2, GPIO.OUT)
    	GPIO.setup(self.B1, GPIO.OUT)
    	GPIO.setup(self.B2, GPIO.OUT)

    	GPIO.output(self.A1, 0)
    	GPIO.output(self.A2, 0)
    	GPIO.output(self.B1, 0)
    	GPIO.output(self.B2, 0)

    def setStep(self, w1, w2, w3, w4, delay):
        GPIO.output(self.A1, w1)
        GPIO.output(self.A2, w2)
        GPIO.output(self.B1, w3)
        GPIO.output(self.B2, w4)
        time.sleep(delay)

    def up(self, delay, steps):  
        for i in range(0, steps):
            self.setStep(1, 0, 0, 0, delay)
            self.setStep(1, 1, 0, 0, delay)
            self.setStep(0, 1, 0, 0, delay)
            self.setStep(0, 1, 1, 0, delay)
            self.setStep(0, 0, 1, 0, delay)
            self.setStep(0, 0, 1, 1, delay)
            self.setStep(0, 0, 0, 1, delay)
            self.setStep(1, 0, 0, 1, delay)

    def down(self, delay, steps):  
        for i in range(0, steps):
            self.setStep(1, 0, 0, 1, delay)
            self.setStep(0, 0, 0, 1, delay)
            self.setStep(0, 0, 1, 1, delay)
            self.setStep(0, 0, 1, 0, delay)
            self.setStep(0, 1, 1, 0, delay)
            self.setStep(0, 1, 0, 0, delay)
            self.setStep(1, 1, 0, 0, delay)
            self.setStep(1, 0, 0, 0, delay)

    def cleanup(self):
        setStep(0,0,0,0, 0.03)
        GPIO.cleanup()


    
