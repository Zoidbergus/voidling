#!/usr/bin/python

from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x70)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

ledsPin = 9
motorPowerPin = 24
# Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledsPin, GPIO.OUT)
GPIO.setup(motorPowerPin, GPIO.OUT)

GPIO.output(ledsPin, GPIO.HIGH)
time.sleep(1)
GPIO.output(ledsPin, GPIO.LOW)


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
  x = raw_input('Enter PWM: ')
  x1 = int(x)
  if x < 150:
    x = 150
  elif x > 450:
    x = 450
  pwm.setPWM(channel, 0, x1)
  time.sleep(3)

