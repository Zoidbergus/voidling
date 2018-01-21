from src.servos.computing.angles import point2angles


def point2pwm_lf(px, py, pz):
    f0a, f1a, f2a = point2angles(px, py, pz)

    # correction of ratios - servo turn and joint turn
    pw1 = round((f0a - 196.63) / (-0.3521))
    pw2 = round((f1a - 179.36) / (-0.185))
    pw3 = round((f2a - 151.6) / (-0.312))

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
