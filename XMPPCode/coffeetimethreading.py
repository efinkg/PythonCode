#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import sys
import time
from CoffeeEmail import SendCoffeeDoneEmail
from Thermometer import read_temp
import threading
from threading import Timer

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

class CoffeeMaker(object):

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CoffeeMaker, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def __init__(self):
        self.active_timers = []
        self.stopping = True
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KETTLE, GPIO.OUT)
        GPIO.setup(SOLENOID, GPIO.OUT)
        GPIO.setup(GRINDER, GPIO.OUT)
        GPIO.setup(PUMP, GPIO.OUT)

    def on_after_wait(self, wait, durration, gpio):
        self.add_timer(Timer(wait, GPIO.output, [gpio, GPIO.HIGH]))
        self.add_timer(Timer(wait + durration, GPIO.output, [gpio, GPIO.LOW]))

    def is_it_hot(self):
        GPIO.output(KETTLE, GPIO.HIGH)
        TEMP=read_temp()
        if TEMP < 67:
           print TEMP
           self.add_timer(Timer(10, self.is_it_hot))
        else:
           GPIO.output(KETTLE, GPIO.LOW)
           self.on_after_wait(0, (12/5)*self.ozCoffee, SOLENOID)
           self.add_timer(Timer(180, self.finish))

    def makeCoffee(self, ozCoffee):
        self.stopping = False
        self.ozCoffee = ozCoffee
        #times in comments are relative to WHEN THIS METHOD IS CALLED
        self.on_after_wait(0, (17/5)*self.ozCoffee, PUMP) #imediately pump for 42 seconds
        self.on_after_wait(19, (7/6)*self.ozCoffee, GRINDER) #erm, any reason you do this after heating the water? seems like a waste
                                           #I mean, It's not on a critical path, so we can start it at any point before
                                           #18 seconds before the water is hot
        self.add_timer(Timer(19, self.is_it_hot)) #start heating after 19 seconds

    def finish(self):
        self.active_timers = []
        SendCoffeeDoneEmail()

    def pins_off(self):
        for pin in [KETTLE, SOLENOID, GRINDER, PUMP]:
            GPIO.output(pin, GPIO.LOW)
        print 'Pins Low'

    def end_timers(self):
    #    print 'Stop Running Stuff'
    #    for t in threading.enumerate():
    #        if isinstance(t, threading._Timer):
    #            t.cancel()
    #            t.join()
        for timer in self.active_timers:
            timer.cancel()
            timer.join()
        self.active_timers = []


    def force_stop(self):
        self.stopping = True
        self.end_timers()
        time.sleep(.5)
        self.pins_off()
        
    def add_timer(self, timer):
        if not self.stopping:
            self.active_timers.append(timer)
            timer.start()
