import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail

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
        print 'Pumping'
        GPIO.output(PUMP, GPIO.HIGH)
        time.sleep(19)
        print 'Kettling'
        GPIO.output(KETTLE, GPIO.HIGH)
        time.sleep(23)
        print 'Done pumping'
        GPIO.output(PUMP, GPIO.LOW)
        time.sleep(280)
        print 'Done kettling'
        GPIO.output(KETTLE, GPIO.LOW)
        print 'Grinding'
        GPIO.output(GRINDER, GPIO.HIGH)
        time.sleep(28)
        GPIO.output(GRINDER, GPIO.LOW)
        print 'Done grinding\nSolenoid on'
        GPIO.output(SOLENOID, GPIO.HIGH)
        time.sleep(30)
        GPIO.output(SOLENOID, GPIO.LOW)
        print 'Solenoid off\nCoffee is brewing'
        time.sleep(60)
        print "Your Coffee Has Been Brewing for One Minute"
        time.sleep(60)
        print "Your Coffee Has Been Brewing for Two Minutes"
        time.sleep(40)
        SendEmail()
        time.sleep(20)
        print "Your Coffee Has Been Brewing for Three Minutes\nYour Coffee is Done Brewing, Please Collect"
