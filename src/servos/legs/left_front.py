from src.servos.computing.pwm import point2pwm

# left front leg control functions


def point2pwm_lf(px, py, pz):
    pw1, pw2, pw3 = point2pwm(px, py, pz)

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
