#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from angles import point2pwm
import time
import RPi.GPIO as GPIO


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x70)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 450  # Max pulse length out of 4096

ledsPin = 9
motorPowerPin = 24
#Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledsPin, GPIO.OUT)
GPIO.setup(motorPowerPin, GPIO.OUT)

GPIO.output(ledsPin, GPIO.HIGH)
GPIO.output(motorPowerPin, GPIO.HIGH)


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

############ CODE #################

a,b,c = point2pwm(0, -5, 17)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(8, -10.5, 20) #A
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(0, -5, 17)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(8, -10.5, 12) #B
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(0, -5, 17)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(-8, -10.5, 12) #C
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(0, -5, 17)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(-8, -10.5, 20) #D
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(0, -5, 17)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
a,b,c = point2pwm(0, -10.5, 20)
pwm.setPWM(1, 0, a)
pwm.setPWM(2, 0, b)
pwm.setPWM(3, 0, c)
time.sleep(2)
