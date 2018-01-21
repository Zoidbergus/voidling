#python script to control hand

from sympy import *
from sympy.geometry import *
import math

#arm parameters
l1 = 8.5
l2 = 12
l3 = 17

px = 5
py = -5
pz = 20
p1 = Point(px, py, pz) # test point to be reached

###### STEP 1 / get new coordinate #######
xn = sqrt(p1.x*p1.x + p1.z*p1.z)
f0 = atan(p1.z / p1.x)
print "x nove: ", xn.evalf()
print "f0 : ", (f0*180/pi).evalf()

#alfa
a = atan(p1.y / (xn-l1))
print "alfa : ", (a*180/pi).evalf()

#pw2 - second ankle
xn2 = xn-l1 # to compensate for the not moving arm
f2 = pi - acos(((l2*l2)+(l3*l3)-(xn2*xn2)-(p1.y*p1.y))/(2*l2*l3))
print "f2: ", (f2*180/pi).evalf()

#pw3 ? - first ankle
f1 = atan(p1.y/xn2) - acos(((xn2*xn2)+(p1.y*p1.y)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(p1.y*p1.y)))))
print "f1: ", (f1*180/pi).evalf()


#beta
b = pi - f2
print "beta: ", (b*180/pi).evalf()

#gamma
g = acos(((xn2*xn2)+(p1.y*p1.y)+(l2*l2)-(l3*l3))/(2*l2*(sqrt((xn2*xn2)+(p1.y*p1.y)))))
print "gamma: ", (g*180/pi).evalf()

#f1c,f2c
f1c = f1 +2*g
f2c = -f2
print "f1c: ", (f1c*180/pi).evalf()
print "f2c: ", (f2c*180/pi).evalf()

#f0a
if f0 < 0:
    f0a = -f0
if f0 > 0:
    f0a = (pi/2) + ((pi/2) - f0)
if f0 == 0:
    f0a = 90

#f1a
f1a = pi - f1c

#f2a
f2a = b

#####final angles:
print "f0a: ", (f0a*180/pi).evalf()
print "f1a: ", (f1a*180/pi).evalf()
print "f2a: ", (f2a*180/pi).evalf()

