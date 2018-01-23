from left_front import point2pwm_lf

# right back leg control functions


def point2pwm_rb(px, py, pz):
    return point2pwm_lf(-px, py, pz)
