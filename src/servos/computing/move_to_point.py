def point2move(point, servo1=1, servo2=2, servo3=3):
    a,b,c = point2pwmLF(point[0], point[1], point[2])
    pwm.setPWM(servo1, 0, a)
    b1 = a + b
    pwm.setPWM(servo2, a, b1)
    c1 = b1 + c
    pwm.setPWM(servo3, b1, c1)
