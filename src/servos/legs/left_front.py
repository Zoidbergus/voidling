import threading

from src.servos.computing.pwm import point2pwm
from src.servos.control.pwm_control import set_pwm
from src.servos.computing.linear import abs_distance, steps_count, speed2delay
import time

# left front leg control functions


class LeftFrontLeg(threading.Thread):
    # chodia mu pwm a on ich robi

    # servo channels
    s1 = 1
    s2 = 2
    s3 = 3

    def run(self):
        print("Left leg started.")
        self.point2pwm_lf(8, 15, 20)

    @staticmethod
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

        return [int(pw1), int(pw2), int(pw3)]

    def point2move(self, point):
        [a, b, c] = self.point2pwm_lf(point[0], point[1], point[2])
        set_pwm(self.s1, 0, a)
        b1 = a + b
        set_pwm(self.s2, a, b1)
        c1 = b1 + c
        set_pwm(self.s3, b1, c1)

    def linear_move(self, p1, p2, speed):
        dx, dy, dz = abs_distance(p1, p2)
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

            new_point = [npx, npy, npz]
            self.point2move(new_point)
            time.sleep(d)

        self.point2move(p2)
