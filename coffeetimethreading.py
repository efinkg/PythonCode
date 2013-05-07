import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail
from Thermometer import read_temp

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
        
    def is_it_hot(self):
        GPIO.output(KETTLE, GPIO.HIGH)
        TEMP=read_temp()
        if TEMP < 65:
           print TEMP
           threading.Timer(10, is_it_hot)
        else:
           GPIO.output(KETTLE, GPIO.LOW)
    def grinding_coffee(self):
        t=0
        GPIO.output(GRINDER, GPIO.HIGH)
        while t < 18:
           TEMP=read_temp()
           if TEMP < 65:
               print TEMP
               GPIO.output(KETTLE, GPIO.HIGH)
           else:
               print TEMP
               GPIO.output(KETTLE, GPIO.LOW)
           threading.Timer(1, grinding_coffee)
           t+=1
        GPIO.output(GRINDER, GPIO.LOW)

    def brewing(self):
        print 'Solenoid off\nCoffee is brewing'
        threading.Timer(60, brewing)
        print "Your Coffee Has Been Brewing for One Minute"
        threading.Timer(60, brewing)
        print "Your Coffee Has Been Brewing for Two Minutes"
        threading.Timer(40, brewing)
        SendEmail()
        threading.Timer(20, brewing)
        print "Your Coffee Has Been Brewing for Three Minutes\nYour Coffee is Done Brewing, Please Collect"
        

    def init_threads:
        self.preFill = threading.Timer(PUMP, 19)
        self.fillHeating = threading.Timer(PUMP, 23)
        self.heatingFill = threading.Timer(KETTLE, 23)
        self.pourWater = threading.Timer(SOLENOID, 30)
        self.kettleHot = is_it_hot()
        self.grindingBeans = grinding_coffee()
    
    def makeCoffee(self):
        print 'Pumping'
        preFill.start()
        print 'Kettling'
        fillHeating.start()
        heatingFill.start()
        print 'Done pumping'
        kettleHot.start()
        print 'Done kettling'
        print 'Grinding'
        self.grindingBeans()
        print 'Done grinding\nSolenoid on'
        pourWater.start()
        
        
