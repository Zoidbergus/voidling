#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
#from angles import point2anglesLR, point2pwm
import time
import RPi.GPIO as GPIO
import sys
import os

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x70)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

ledsPin = 9
motorPowerPin = 24
#Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledsPin, GPIO.OUT)
GPIO.setup(motorPowerPin, GPIO.OUT)

GPIO.output(ledsPin, GPIO.HIGH)
GPIO.output(motorPowerPin, GPIO.HIGH)

time.sleep(1)
#GPIO.output(ledsPin, GPIO.LOW)


servoMin = 150  # Min pulse length out of 4096
servoMax = 450  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
channel = 1

while (True):
  try:
    x = raw_input('Enter Channel: ')
    x1 = int(x)
    if x < 0:
      x1 = 0
    elif x > 16:
      x1 = 0
    for chan in range(0, 15):
      pwm.setPWM(chan, 0, 300)
      time.sleep(3)
      print "Channel %d reset." % (chan)  
  except KeyboardInterrupt:
    GPIO.output(motorPowerPin, GPIO.LOW)
    GPIO.output(ledsPin, GPIO.LOW)
    print "\n Exiting program, turning off engines."
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
