from right_front import point2pwm_rf

# left back leg control functions


def point2pwm_lb(px, py, pz):
    return point2pwm_rf(-px, py, pz)
