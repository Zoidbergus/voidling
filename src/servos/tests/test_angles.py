from src.servos.computing.angles import point2angles
import time

# Debug script to verify computations


def test_leg_rotation_computation():
    y = -2
    z = 22
    start = time.time()
    for x in range(-5, 6):
        a, b, c = point2angles(x, y, z)
        print "angle for x: ", x, ", is: ", a
    end = time.time() - start
    print "time: ", end


def test_leg_lift_computation():
    x = 0
    z = 20.5
    start = time.time()
    for y in range(-22, -5):
        a, b, c = point2angles(x, y, z)
        print "angles for [0,", y, ",", z, "]: ",  a, "\t", b, "\t", c
    end = time.time() - start
    print "time: ", end


def test_leg_stretch_computation():
    x = 0
    y = -8
    start = time.time()
    for z in range(10, 30):
        a, b, c = point2angles(x, y, z)
        print "angles for [0,", y, ",", z, "]: ",  a, "\t", b, "\t", c
    end = time.time() - start
    print "time: ", end


if __name__ == "__main__":
    # test_leg_rotation_computation()
    test_leg_lift_computation()
    # test_leg_stretch_computation()


