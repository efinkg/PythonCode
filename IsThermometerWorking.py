import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail
from ThermometerTesting import read_temp

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

class CoffeeMakerSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClimateControlSingleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KETTLE, GPIO.OUT)
        GPIO.setup(SOLENOID, GPIO.OUT)
        GPIO.setup(GRINDER, GPIO.OUT)
        GPIO.setup(PUMP, GPIO.OUT)

    def on_for_seconds(self, gpio, seconds):
        GPIO.output(gpio, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(gpio, GPIO.LOW)
    
    def makeCoffee(self):

        TEMP = read_temp()
        GPIO.output(KETTLE, GPIO.HIGH)
        while TEMP < 155:
           print TEMP
           time.sleep(10)
           TEMP=read_temp()
        GPIO.output(KETTLE, GPIO.LOW)
        t=0
        while t < 18:
           TEMP=read_temp()
           if TEMP < 155:
               print TEMP
               GPIO.output(KETTLE, GPIO.HIGH)
           else:
               print TEMP
               GPIO.output(KETTLE, GPIO.LOW)
           time.sleep(1)
           t+=1
maker = CoffeeMakerSingleton()
maker.makeCoffee()

