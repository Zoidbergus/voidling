#python script to return hand angles

from math import atan, acos, sqrt, pi, degrees

#point2angles(int px, int py, int pz)
#enter point in real space to be reached, returns angles
#f0a - leg rotation around large leg holding bolt
#f1a - leg lift, joint near the leg holding bol)
#f2a - leg stretch, joint at the end of the leg    
def point2angles(px, py, pz):
    l1=8.5
    l2=12
    l3=17

    if px != 0:
       f0 = atan(pz / px)
       xn = sqrt(px*px + pz*pz)
    else:
       f0 = pi/2
       xn = pz
    xn2 = xn-l1
    a = atan(py/(xn2))
    g = acos(((xn2*xn2)+(py*py)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(py*py)))))
    f2 = pi - acos(((l2*l2)+(l3*l3)-(xn2*xn2)-(py*py))/(2*l2*l3))
    f1 = a - g
    b = pi - f2
    g = acos(((xn2*xn2)+(py*py)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(py*py)))))
    f1c = f1 +2*g
    f2c = -f2
    if f0 < 0:
        f0a = -f0
    elif f0 > 0:
        f0a = (pi/2) + ((pi/2) - f0)
    f1a = pi - f1c
    f2a = b
    f0a = degrees(f0a)
    f1a = degrees(f1a)
    f2a = degrees(f2a)
    return f0a, f1a, f2a

def point2pwmLF(px, py, pz):
    f0a,f1a,f2a = point2angles(px, py, pz) 
    
    #correction of ratios - servo turn and joint turn
    pw1 = round((f0a - 196.63)/(-0.3521))
    pw2 = round((f1a - 179.36)/(-0.185))
    pw3 = round((f2a - 151.6)/(-0.312))

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

def point2pwmRF(px, py, pz):
    f0a,f1a,f2a = point2angles(px, py, pz)

    #correction of ratios - servo turn and joint turn
    pw1 = round((f0a - 196.63)/(-0.3521))
    pw2 = round((f1a - 179.36)/(-0.185))
    pw3 = round((f2a - 151.6)/(-0.312))
    
    #inverted leg
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

def point2pwmLB(px, py, pz):
    return point2pwmRF(-px, py, pz)

def point2pwmRB(px, py, pz):
    return point2pwmLF(-px, py, pz)

