from math import floor
from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM
from src.servos.computing.angles import point2pwmLF, point2pwmRF
import time

# linear.py
# defines linear movement functions

# TODO: isolate functions, make test file to use them


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




