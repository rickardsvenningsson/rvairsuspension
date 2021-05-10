# Air suspension controller - Hardware module

# Imports
import RPi.GPIO as GPIO

# Variables
sensorFeed = 12
valveOutlet = 21
valveRL = 6
valveRR = 13
valveFF = 26
valveFBlock = 19

def init():
   # GPIO
   GPIO.setmode(GPIO.BCM)

   GPIO.setup(sensorFeed, GPIO.OUT)
   GPIO.setup(valveOutlet, GPIO.OUT)
   GPIO.setup(valveRL, GPIO.OUT)
   GPIO.setup(valveRR, GPIO.OUT)
   GPIO.setup(valveFF, GPIO.OUT)
   GPIO.setup(valveFBlock, GPIO.OUT)

   GPIO.output(sensorFeed, GPIO.HIGH)
   GPIO.output(valveOutlet, GPIO.HIGH)
   GPIO.output(valveRL, GPIO.HIGH)
   GPIO.output(valveRR, GPIO.HIGH)
   GPIO.output(valveFF, GPIO.HIGH)
   GPIO.output(valveFBlock, GPIO.HIGH)

def cleanup():
   # GPIO
   GPIO.cleanup()

   
def sensorFeed(value):
   if True == value:
      GPIO.output(sensorFeed, GPIO.LOW)
   else:
      GPIO.output(sensorFeed, GPIO.HIGH)
      