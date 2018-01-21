# python script to return hand angles

from math import atan, acos, sqrt, pi, degrees

# point2angles(int px, int py, int pz)
# enter point in real space to be reached, returns angles
# f0a - leg rotation around large leg holding bolt
# f1a - leg lift, joint near the leg holding bol)
# f2a - leg stretch, joint at the end of the leg

# TODO: define functions to be used: point2angles, correct_angles
# TODO: make a function to correct angles/ratios
# TODO: think about how to program better function to compute the legs
# TODO: make a test on angles (after you get PWM working)


def point2angles(px, py, pz):
    l1 = 8.5
    l2 = 12
    l3 = 17
    if px != 0:
        f0 = atan(pz / px)
        xn = sqrt(px*px + pz*pz)
    else:
        f0 = pi/2
        xn = pz
    xn2 = xn-l1
    a = atan(py/xn2)
    g = acos(((xn2*xn2)+(py*py)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(py*py)))))
    f2 = pi - acos(((l2*l2)+(l3*l3)-(xn2*xn2)-(py*py))/(2*l2*l3))
    f1 = a - g
    b = pi - f2
    g = acos(((xn2*xn2)+(py*py)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(py*py)))))
    f1c = f1 + 2*g
    f2c = -f2
    if f0 < 0:
        f0 = -f0
    elif f0 > 0:
        f0 = (pi/2) + ((pi/2) - f0)
    f1a = pi - f1c
    f2a = b
    f0a = degrees(f0)
    f1a = degrees(f1a)
    f2a = degrees(f2a)

    return f0a, f1a, f2a



