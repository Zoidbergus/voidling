from right_front import point2pwm_rf
import threading
# left back leg control functions


class LeftBackLeg(threading.Thread):
    print()


def point2pwm_lb(px, py, pz):
    return point2pwm_rf(-px, py, pz)
