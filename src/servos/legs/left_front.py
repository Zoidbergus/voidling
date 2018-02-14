from src.servos.computing.pwm import point2pwm
import threading
import time

# left front leg control functions


class LeftFrontLeg(threading.Thread):
    # chodia mu pwm a on ich robi

    def run(self):
        print("hi there")
        time.sleep(3)
        print("hi there again")
        LeftFrontLeg.fire(self)

    def fire(self):
        time.sleep(4)
        print("fire")


def point2pwm_lf(px, py, pz):
    pw1, pw2, pw3 = point2pwm(px, py, pz)

    if pw1 < 150:
        pw1 = 150
    elif pw1 > 450:
        pw1 = 450
    if pw2 < 150:
        pw2 = 150
    elif pw2 > 380:
        pw2 = 380
    if pw3 < 150:
        pw3 = 150
    elif pw3 > 350:
        pw3 = 350

    return int(pw1), int(pw2), int(pw3)
