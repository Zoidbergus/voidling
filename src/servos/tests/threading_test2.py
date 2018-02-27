
import threading
import time


lock2 = threading.RLock()
pwm = 0


def set_speed(speed):
    with lock2:
        global pwm
        pwm = pwm + speed
        print(pwm)


class LeftLeg(threading.Thread):

    def __init__(self):
        self._x_cache = 0
        self.x = 1
        self.lock = threading.RLock()
        super(LeftLeg, self).__init__()

    def run(self):
        for x in range(1, 100):
            # print(x)
            time.sleep(0.1)
            set_speed(0.1)

    def move(self, poitn):
        print("I have moved", poitn)
        set_speed(5)


class RightLeg(threading.Thread):
    def run(self):
        for x in range(1, 10):
            # print(x)
            time.sleep(1)
            set_speed(10)


def do_stuff(number):
    print(number)


if __name__ == "__main__":
    print("beginning")
    left = LeftLeg()
    right = RightLeg()
    left.move(123)
    left.start()
    right.start()

