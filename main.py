import RPi.GPIO as GPIO

Relay_channel = [4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)
# GPIO.output(4, GPIO.HIGH)
