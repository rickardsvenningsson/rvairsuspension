# Air suspension controller - Hardware module

# Imports
import RPi.GPIO as GPIO

# Variables
#sensorFeed = 12
#valveOutlet = 21
#valveRL = 6
#valveRR = 13
#valveFF = 26
#valveFBlock = 19 

def init():
   # GPIO
   GPIO.setmode(GPIO.BCM)

   GPIO.setup(12, GPIO.OUT)
   GPIO.setup(21, GPIO.OUT)
   GPIO.setup(6, GPIO.OUT)
   GPIO.setup(13, GPIO.OUT)
   GPIO.setup(26, GPIO.OUT)
   GPIO.setup(19, GPIO.OUT)

   GPIO.output(12, GPIO.HIGH)
   GPIO.output(21, GPIO.HIGH)
   GPIO.output(6, GPIO.HIGH)
   GPIO.output(13, GPIO.HIGH)
   GPIO.output(26, GPIO.HIGH)
   GPIO.output(19, GPIO.HIGH)

def cleanup():
   # GPIO
   GPIO.cleanup()

   
def sensorFeed_on():
      GPIO.output(12, GPIO.LOW)

def sensorFeed_off():
      GPIO.output(12, GPIO.HIGH)
      