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
            cls._instance = super(CoffeeMakerSingleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KETTLE, GPIO.OUT)
        GPIO.setup(SOLENOID, GPIO.OUT)
        GPIO.setup(GRINDER, GPIO.OUT)
        GPIO.setup(PUMP, GPIO.OUT)

    def on_after_wait(self, wait, durration, gpio):
        threading.Timer(wait, GPIO.output, [gpio, GPIO.HIGH]).start()
        threading.Timer(wait + durration, GPIO.output, [gpio, GPIO.LOW]).start()

    def is_it_hot(self):
        GPIO.output(KETTLE, GPIO.HIGH)
        TEMP=read_temp()
        if TEMP < 65:
           print TEMP
           threading.Timer(10, self.is_it_hot).start()
        else:
           GPIO.output(KETTLE, GPIO.LOW)
           self.on_after_wait(0, 30, SOLENOID)
           threading.Timer(180, SendEmail).start()

    def makeCoffee(self):
        #times in comments are relative to WHEN THIS METHOD IS CALLED
        self.on_after_wait(0, 42, PUMP) #imediately pump for 42 seconds
        self.on_after_wait(0, 18, GRINDER) #erm, any reason you do this after heating the water? seems like a waste
                                           #I mean, It's not on a critical path, so we can start it at any point before
                                           #18 seconds before the water is hot
        threading.Timer(19, self.is_it_hot).start() #start heating after 19 seconds

    def pins_off(self):
        for pin in [KETTLE, SOLENOID, GRINDER, PUMP]:
            GPIO.output(pin, GPIO.LOW)
        print 'pins low'

    def end_timers(self):
        print 'threads'
        '''for t in threading.enumerate():
            print t
            if isinstance(t, threading._Timer):
                print 'canceling'
                t.cancel()
                print 'joining'
                t.join()'''

    def force_stop(self):
        self.end_timers()
        self.pins_off()
