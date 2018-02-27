from servos.control.init_gpio import init_gpio_pins
from servos.control.pwm_control import init_servo_communication
from servos.control.power_control import init_servo_power, servo_power_off
from servos.control.leg_control import init_legs_threads

# TODO: Make thread classes with all the relevant functions ... and init_legs_threads() ?
# TODO: Start those classes in main program .. part of init ?
# TODO: Make simple testing function with two legs moving in linear .. ikr ?
# TODO: Test it in main


def main():
    try:
        init_gpio_pins()
        init_servo_communication()
        init_servo_power()
        init_legs_threads()

        # program start

        # do_move_front_legs_linear()

        # program end

        servo_power_off()
    except KeyboardInterrupt:
        servo_power_off()
        print "\n Exiting program, turning off engines."
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()