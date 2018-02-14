from math import floor
from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM
from src.servos.computing.angles import point2pwmLF, point2pwmRF
import time

# linear.py
# defines linear movement functions

# TODO: isolate functions, make test file to use them, remove time.sleep .. LEARN PYTHON THREADING


def abs_distance(point_a, point_b):
    dx = point_b[0] - point_a[0]
    dx = abs(dx)
    dy = point_b[1] - point_a[1]
    dy = abs(dy)
    dz = point_b[2] - point_a[2]
    dz = abs(dz)
    return dx, dy, dz


def used_axis_count(distance_x, distance_y, distance_z):
    count = 0
    if distance_x > 1:
        count += 1
    if distance_y > 1:
        count += 1
    if distance_z > 1:
        count += 1
    return count


def steps_count(dx, dy, dz):
    smallest_step = 0.2
    axis = used_axis_count(dx, dy, dz)
    number_of_steps = int(floor(((dx+dy+dz)/axis)/smallest_step))
    return number_of_steps


def speed2delay(speed):
    if speed < 20:
        speed = 20
    if speed > 100:
        speed = 100
    delay = 57.5 - (57.5/154)*speed
    delay = (round(delay))/1000
    return delay


def linearMoveLF(servo1, servo2, servo3, p1, p2, speed):
    dx,dy,dz = abs_distance(p1, p2)
#    print "dx: ", dx,"dy: ", dy, "dz: ", dz
    s = steps_count(dx, dy, dz)
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



