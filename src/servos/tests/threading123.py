import threading
import time


class MyThread (threading.Thread):

    def __init__(self, speed=0.1):
        self._speed_cache = 2
        self.speed = 1
        self.lock = threading.RLock()
        super(MyThread, self).__init__()

    def set_speed(self, speed):  # you can use a proper setter if you want
        with self.lock:
            self.speed = speed

    def run(self):
        while True:
            with self.lock:
                if self.speed == 0:
                    print("Speed dropped to 0, exiting...")
                    break
                # just so we don't continually print the speed, print only on change
                if self.speed != self._speed_cache:
                    print("Current speed: {}".format(self.speed))
                    self._speed_cache = self.speed
            time.sleep(0.1)  # let it breathe


try:
    input = raw_input  # add for Python 2.6+ compatibility
except NameError:
    pass

current_speed = 3  # initial speed

blink_thread = MyThread(current_speed)
blink_thread.start()

while current_speed != 0:  # main loop until 0 speed is selected
    time.sleep(0.1)  # wait a little for an update
    current_speed = int(input("Enter 0 to Exit or 1/2/3 to continue\n"))  # add validation?
    blink_thread.set_speed(current_speed)