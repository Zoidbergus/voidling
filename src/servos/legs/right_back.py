from left_front import point2pwm_lf
import threading
# right back leg control functions


class RightBackLeg(threading.Thread):
    print()


def point2pwm_rb(px, py, pz):
    return point2pwm_lf(-px, py, pz)
