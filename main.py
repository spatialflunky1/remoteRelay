import RPi.GPIO as GPIO

# This is the GPIO channel that I use 
Relay_channel = [4]

# Sets up the GPIO ports for use
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)

# You can use these two functions in the application
def on():
    GPIO.output(4, GPIO.LOW)

def off():
    GPIO.output(4, GPIO.HIGH)
