def point2moveLF(p1, s1=1, s2=2, s3=3):
    a,b,c = point2pwmLF(p1[0], p1[1], p1[2])
    pwm.setPWM(s1, 0, a)
    b1 = a + b
    pwm.setPWM(s2, a, b1)
    c1 = b1 + c
    pwm.setPWM(s3, b1, c1)
    return 0