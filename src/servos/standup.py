#!/usr/bin/python

from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM
from src.servos.computing.angles import point2pwmLF, point2pwmRF
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

#off je (4096, 0)
#SERVA:
#  LF: 1 2 3
#  LB: 5 6 7
#  RB: 8 9 10
#  RF: 12 13 14

time.sleep(3)

try:
  #STEP 0 - put legs up
  a,b,c = point2pwmLF(0, -2, 22)
  pwm.setPWM(1, 0, a)
  pwm.setPWM(2, 0, b)
  pwm.setPWM(3, 0, c)
  pwm.setPWM(8, 0, a)
  pwm.setPWM(9, 0, b)
  pwm.setPWM(10, 0, c)
  a,b,c = point2pwmRF(0, -2, 22)
  pwm.setPWM(5, 0, a)
  pwm.setPWM(6, 0, b)
  pwm.setPWM(7, 0, c)
  pwm.setPWM(12, 0, a)
  pwm.setPWM(13, 0, b)
  pwm.setPWM(14, 0, c)
  time.sleep(3)
  #STEP 1 - put legs on the floor
  a,b,c = point2pwmLF(5, -5, 20)
  pwm.setPWM(1, 0, a)
  pwm.setPWM(2, 0, b)
  pwm.setPWM(3, 0, c)
  time.sleep(0.5)
  pwm.setPWM(8, 0, a)
  pwm.setPWM(9, 0, b)
  pwm.setPWM(10, 0, c)
  time.sleep(0.5)
  a,b,c = point2pwmRF(5, -5, 20)
  pwm.setPWM(5, 0, a)
  pwm.setPWM(6, 0, b)
  pwm.setPWM(7, 0, c)
  time.sleep(0.5)
  pwm.setPWM(12, 0, a)
  pwm.setPWM(13, 0, b)
  pwm.setPWM(14, 0, c)
  time.sleep(2)
  #STEP 2 - LIFT
  a,b,c = point2pwmLF(5, -10, 20)
  pwm.setPWM(1, 0, a)
  pwm.setPWM(2, 0, b)
  pwm.setPWM(3, 0, c)
  pwm.setPWM(8, 0, a)
  pwm.setPWM(9, 0, b)
  pwm.setPWM(10, 0, c)
  a,b,c = point2pwmRF(5, -10, 20)
  pwm.setPWM(5, 0, a)
  pwm.setPWM(6, 0, b)
  pwm.setPWM(7, 0, c)
  pwm.setPWM(12, 0, a)
  pwm.setPWM(13, 0, b)
  pwm.setPWM(14, 0, c)
  time.sleep(15)
  #STEP 3 - sit down
  a,b,c = point2pwmLF(5, -5, 20)
  pwm.setPWM(1, 0, a)
  pwm.setPWM(2, 0, b)
  pwm.setPWM(3, 0, c)
  #time.sleep(0.5)
  pwm.setPWM(8, 0, a)
  pwm.setPWM(9, 0, b)
  pwm.setPWM(10, 0, c)
  #time.sleep(0.5)
  a,b,c = point2pwmRF(5, -5, 20)
  pwm.setPWM(5, 0, a)
  pwm.setPWM(6, 0, b)
  pwm.setPWM(7, 0, c)
  #time.sleep(0.5)
  pwm.setPWM(12, 0, a)
  pwm.setPWM(13, 0, b)
  pwm.setPWM(14, 0, c)
  time.sleep(2)
  #STEP 4 - turn off engines
  pwm.setPWM(1, 4096, 0)
  pwm.setPWM(2, 4096, 0)
  pwm.setPWM(3, 4096, 0)
  pwm.setPWM(8, 4096, 0)
  pwm.setPWM(9, 4096, 0)
  pwm.setPWM(10, 4096, 0)
  pwm.setPWM(5, 4096, 0)
  pwm.setPWM(6, 4096, 0)
  pwm.setPWM(7, 4096, 0)
  pwm.setPWM(12, 4096, 0)
  pwm.setPWM(13, 4096, 0)
  pwm.setPWM(14, 4096, 0)
except KeyboardInterrupt:
  GPIO.output(motorPowerPin, GPIO.LOW)
  GPIO.output(ledsPin, GPIO.LOW)
  print "\n Exiting program, turning off engines."
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)
