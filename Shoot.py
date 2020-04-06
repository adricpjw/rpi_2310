import RPi.GPIO as GPIO    
import time

GPIO.setmode(GPIO.BOARD)

 
#stepper motor
coil_A_1_pin = 13
coil_A_2_pin = 11
coil_B_1_pin = 15
coil_B_2_pin = 12

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.output(coil_A_1_pin, 0)
GPIO.output(coil_A_2_pin, 0)
GPIO.output(coil_B_1_pin, 0)
GPIO.output(coil_B_2_pin, 0)

def up(delay, steps):  
    for i in range(0, steps):
        setStep(1, 0, 0, 0, delay)
        setStep(1, 1, 0, 0, delay)
        setStep(0, 1, 0, 0, delay)
        setStep(0, 1, 1, 0, delay)
        setStep(0, 0, 1, 0, delay)
        setStep(0, 0, 1, 1, delay)
        setStep(0, 0, 0, 1, delay)
        setStep(1, 0, 0, 1, delay)

def down(delay, steps):  
    for i in range(0, steps):
        setStep(1, 0, 0, 1, delay)
        setStep(0, 0, 0, 1, delay)
        setStep(0, 0, 1, 1, delay)
        setStep(0, 0, 1, 0, delay)
        setStep(0, 1, 1, 0, delay)
        setStep(0, 1, 0, 0, delay)
        setStep(1, 1, 0, 0, delay)
        setStep(1, 0, 0, 0, delay)


  
def setStep(w1, w2, w3, w4, delay):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)
  time.sleep(delay)

'''
if signal==1:
    down(0.01,5)
elif signal==-1:
    up(0.01,5)
else: 
   
    
'''    
down(0.01,5)
time.sleep(3)
up(0.01,5)
time.sleep(3)    
setStep(0, 0, 0, 0)

#sero
servo_point = 22
GPIO.setup(servo_point,GPIO.OUT)
pwm = GPIO.PWM(servo_point,50)
pwm.start(0)
pwm.ChangeDutyCycle(7)
time.sleep(5)
pwm.ChangeDutyCycle(2)
#DC Motor 1
GPIO.setup(33, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
#pwm2=GPIO.PWM(37, 100)
#pwm2.start(0)
GPIO.output(33, 1)
GPIO.output(36, 0)
GPIO.output(37, 1)
time.sleep(3)
GPIO.output(37, 0)
GPIO.cleanup()



