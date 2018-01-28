from src.servos.computing.pwm import point2pwm
# right front leg control functions


def point2pwm_rf(px, py, pz):
    pw1, pw2, pw3 = point2pwm(px, py, pz)

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
