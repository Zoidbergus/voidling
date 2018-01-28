from src.servos.computing.angles import point2angles


def point2pwm(px, py, pz):
    f0a, f1a, f2a = point2angles(px, py, pz)
    pw1 = round((f0a - 206.96867) / (-0.389896))
    pw2 = round((f1a - 179.36) / (-0.185))
    pw3 = round((f2a - 151.6) / (-0.312))
    return pw1, pw2, pw3
