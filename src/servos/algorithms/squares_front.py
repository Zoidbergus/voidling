from src.servos.control.leg_control import get_legs_threads


def do_move_front_legs_linear():
    #init
    lf, rf, lb, rb = get_legs_threads()
    lf.start()
    rf.start()

    
    lf
