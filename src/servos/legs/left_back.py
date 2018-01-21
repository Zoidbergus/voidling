from right_front import point2pwm_rf


def point2pwm_lb(px, py, pz):
    return point2pwm_rf(-px, py, pz)
