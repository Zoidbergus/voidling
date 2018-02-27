from src.servos.legs.left_front import LeftFrontLeg
from src.servos.legs.right_front import RightFrontLeg
from src.servos.legs.left_back import LeftBackLeg
from src.servos.legs.right_back import RightBackLeg


def get_legs_threads():
    left_front = LeftFrontLeg()
    right_front = RightFrontLeg()
    left_back = LeftBackLeg()
    right_back = RightBackLeg()
    return left_front, right_front, left_back, right_back

