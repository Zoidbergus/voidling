from angles import point2angles, point2pwmLF, point2pwmRF, point2pwmLB, point2pwmRB
import time


#Define coordinates of the point to be reached
x = 5 
y = -2 
z = 22

start = time.time()

for huehue in range(12, 13):
    a,b,c = point2pwmLF(x,y,z)
    #a,b,c = point2angles(x,y,z)
    print "pwm LF: ", a, " ", b, " ", c
    #end = time.time() - start
    #print "time: ", end
    a,b,c = point2pwmRF(x,y,z)
    print "pwm RF: ", a, " ", b, " ", c
    a,b,c = point2pwmLB(x,y,z)
    print "pwm LB: ", a, " ", b, " ", c
    a,b,c = point2pwmRB(x,y,z)
    print "pwm RB: ", a, " ", b, " ", c
