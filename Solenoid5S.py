import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(KETTLE, GPIO.OUT)
GPIO.setup(SOLENOID, GPIO.OUT)
GPIO.setup(GRINDER, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)

GPIO.output(PUMP, GPIO.LOW)
GPIO.output(KETTLE, GPIO.LOW)
GPIO.output(GRINDER, GPIO.LOW)
GPIO.output(SOLENOID, GPIO.LOW)

t=0
while t < 5:
    GPIO.output(SOLENOID, GPIO.HIGH)
    time.sleep(1)
    t+=1

GPIO.output(SOLENOID, GPIO.LOW)
