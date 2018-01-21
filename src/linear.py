from math import floor
from Adafruit_PWM_Servo_Driver import PWM
from angles import point2pwmLF, point2pwmRF
import time

pwm = PWM(0x70)

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

#p1=[2, -5, 20]
#print p1[1]
#p2=[5, 5, 12]

#x1=2
#y1=5
#z1=20

#x2=5
#y2=-5
#z2=12

def distance(a,b):
    dx = b[0] - a[0]
    dx = abs(dx)
    dy = b[1] - a[1]
    dy = abs(dy)
    dz = b[2] - a[2]
    dz = abs(dz)
    return dx, dy, dz

#dx,dy,dz = distance(p1,p2)

def usedAxis(dx,dy,dz):
    i = 0
    if dx > 1:
        i = i + 1
    if dy > 1:
        i = i + 1
    if dz > 1:
        i = i + 1
    return i

def stepsCount(dx, dy, dz):
    i = usedAxis(dx,dy,dz)
    nSteps = int(floor(((dx+dy+dz)/i)/0.2))
    print nSteps
    return nSteps

def speed2delay(speed):
    if speed < 20:
        speed = 20
    if speed > 100:
        speed = 100
    delay = 57.5 - (57.5/154)*speed
    delay = (round(delay))/1000
    return delay

def point2moveLF(p1, s1=1, s2=2, s3=3):
    a,b,c = point2pwmLF(p1[0], p1[1], p1[2])
    pwm.setPWM(s1, 0, a)
    b1 = a + b
    pwm.setPWM(s2, a, b1)
    c1 = b1 + c
    pwm.setPWM(s3, b1, c1)
    return 0

def point2moveRF(p1, s1=1, s2=2, s3=3):
    a,b,c = point2pwmRF(p1[0], p1[1], p1[2])
    pwm.setPWM(s1, 0, a)
    b1 = a + b
    pwm.setPWM(s2, a, b1)
    c1 = b1 + c
    pwm.setPWM(s3, b1, c1)
    return 0


def linearMoveLF(servo1, servo2, servo3, p1, p2, speed):
    dx,dy,dz = distance(p1, p2)
#    print "dx: ", dx,"dy: ", dy, "dz: ", dz
    s = stepsCount(dx, dy, dz)
    d = speed2delay(speed)
    npx = p1[0]
    npy = p1[1]
    npz = p1[2]
#    print dx, " ", dy, " ", dz
    for i in range(0, s):
        if p1[0] < p2[0]:
            npx = p1[0] + (float(dx)/s)*i
        elif p1[0] > p2[0]:
            npx = p1[0] - (float(dx)/s)*i
        if p1[1] < p2[1]:
            npy = p1[1] + (float(dy)/s)*i
        elif p1[1] > p2[1]:
            npy = p1[1] - (float(dy)/s)*i
        if p1[2] < p2[2]:
            npz = p1[2] + (float(dz)/s)*i
        elif p1[2] > p2[2]:
            npz = p1[2] - (float(dz)/s)*i

        npx = round(npx, 2)
        npy = round(npy, 2)
        npz = round(npz, 2)
        #print "x: ", npx, " y: ", npy, " z: ", npz
        newPoint = [npx, npy, npz]
        point2moveLF(newPoint, servo1, servo2, servo3)
        time.sleep(d)
    point2moveLF(p2, servo1, servo2, servo3)
    return 0

def linearMoveRF(servo1, servo2, servo3, p1, p2, speed):
    dx,dy,dz = distance(p1, p2)
#    print "dx: ", dx,"dy: ", dy, "dz: ", dz
    s = stepsCount(dx, dy, dz)
    d = speed2delay(speed)
    npx = p1[0]
    npy = p1[1]
    npz = p1[2]
#    print dx, " ", dy, " ", dz
    for i in range(0, s):
        if p1[0] < p2[0]:
            npx = p1[0] + (float(dx)/s)*i
        elif p1[0] > p2[0]:
            npx = p1[0] - (float(dx)/s)*i
        if p1[1] < p2[1]:
            npy = p1[1] + (float(dy)/s)*i
        elif p1[1] > p2[1]:
            npy = p1[1] - (float(dy)/s)*i
        if p1[2] < p2[2]:
            npz = p1[2] + (float(dz)/s)*i
        elif p1[2] > p2[2]:
            npz = p1[2] - (float(dz)/s)*i

        npx = round(npx, 2)
        npy = round(npy, 2)
        npz = round(npz, 2)
        #print "x: ", npx, " y: ", npy, " z: ", npz
        newPoint = [npx, npy, npz]
        point2moveRF(newPoint, servo1, servo2, servo3)
        time.sleep(d)
    point2moveRF(p2, servo1, servo2, servo3)
    return 0


#px=[0, -10.5, 20]
#point2move(px)
#time.sleep(2)
#p0=[0, -5, 17]
#point2move(p0)
#time.sleep(2)
#p1=[8, -10, 20]
#p2=[8, -10, 12]
#p3=[-8, -10, 12]
#p4=[-8, -10, 20]
#m = linearMove(p1, p2, 100)
#time.sleep(0.1)
#m = linearMove(p2, p3, 100)
#time.sleep(0.1)
#m = linearMove(p3, p4, 100)
#time.sleep(0.1)
#m = linearMove(p4, p1, 100)
#time.sleep(0.1)

#time.sleep(1)
#point2move(p0)
#time.sleep(1)
#point2move(px)

