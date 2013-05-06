import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Kettle = GPIO.setup(7, GPIO.OUT)
Pump = GPIO.setup(11, GPIO.OUT)
Grinder = GPIO.setup(12, GPIO.OUT)
Solenoid = GPIO.setup(13, GPIO.OUT)

GPIO.cleanup()
