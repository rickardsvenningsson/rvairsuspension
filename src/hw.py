# Air suspension controller - Hardware module

# Imports
import RPi.GPIO as GPIO
from sense_hat import SenseHat

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
   
###### SenseHat FUNCTIONS
def getPitch():
   sense = SenseHat()
   orientation = sense.get_orientation_degrees()
   return orientation['pitch']

def getRoll():
   sense = SenseHat()
   orientation = sense.get_orientation_degrees()
   return orientation['roll']
   
 
###### GPIO FUNCTIONS   
   
def sensorFeed_on():
   GPIO.output(12, GPIO.LOW)

def sensorFeed_off():
   GPIO.output(12, GPIO.HIGH)

def valveOutlet_on():
   GPIO.output(21, GPIO.LOW)

def valveOutlet_off():
   GPIO.output(21, GPIO.HIGH)      

def valveRL_on():
   GPIO.output(6, GPIO.LOW)

def valveRL_off():
   GPIO.output(6, GPIO.HIGH)      

def valveRR_on():
   GPIO.output(13, GPIO.LOW)

def valveRR_off():
   GPIO.output(13, GPIO.HIGH)      

def valveFF_on():
   GPIO.output(26, GPIO.LOW)

def valveFF_off():
   GPIO.output(26, GPIO.HIGH)      

def valveFBlock_on():
   GPIO.output(19, GPIO.LOW)

def valveFBlock_off():
   GPIO.output(19, GPIO.HIGH)      
