import RPi.GPIO as GPIO
import sys

# This is the GPIO channel that I use 
Relay_channel = [4]

# Sets up the GPIO config
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.HIGH)

# You can use these two functions in the application
def on():
    GPIO.output(4, GPIO.LOW)

def off():
    GPIO.output(4, GPIO.HIGH)

if len(sys.argv) != 2:
  print("Invalid arguments!")
  quit()

if sys.argv[1] == "on":
  on()
elif sys.argv[1] == "off":
  off()
