from left_front import point2pwm_lf


def point2pwm_rb(px, py, pz):
    return point2pwm_lf(-px, py, pz)
