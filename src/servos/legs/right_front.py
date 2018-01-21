from src.servos.computing.angles import point2angles


def point2pwm_rf(px, py, pz):
    f0a, f1a, f2a = point2angles(px, py, pz)

    # correction of ratios - servo turn and joint turn
    pw1 = round((f0a - 196.63) / (-0.3521))
    pw2 = round((f1a - 179.36) / (-0.185))
    pw3 = round((f2a - 151.6) / (-0.312))

    # inverted leg
    pw1 = (300 - pw1) + 300
    pw2 = (300 - pw2) + 300
    pw3 = (300 - pw3) + 300

    if pw1 < 150:
        pw1 = 150
    elif pw1 > 450:
        pw1 = 450
    if pw2 < 220:
        pw2 = 220
    elif pw2 > 450:
        pw2 = 450
    if pw3 < 250:
        pw3 = 250
    elif pw3 > 450:
        pw3 = 450

    return int(pw1), int(pw2), int(pw3)
