import RPi.GPIO as GPIO
import time
from CoffeeDone import SendEmail
from Thermometer import read_temp
import threading

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(KETTLE, GPIO.OUT)
GPIO.setup(SOLENOID, GPIO.OUT)
GPIO.setup(GRINDER, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)


GPIO.output(SOLENOID, GPIO.HIGH)
time.sleep(5)
GPIO.output(SOLENOID, GPIO.LOW)
