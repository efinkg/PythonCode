import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail
from Thermometer import read_temp
import threading

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

GPIO.output(SOLENOID, GPIO.high)
time.sleep(5)
GPIO,output(SOLENOIND, GPIO.low)