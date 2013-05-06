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

class killPins:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClimateControlSingleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def turnOff(self):
        GPIO.output(PUMP, GPIO.LOW)
        GPIO.output(GRINDER, GPIO.LOW)
        GPIO.output(KETTLE, GPIO.LOW)
        GPIO.output(SOLENOID, GPIO.LOW)

        import sys
        sys.exit("Error message")
