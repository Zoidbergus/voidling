from servos.control.init_gpio import init_gpio_pins
from servos.control.pwm_control import init_servo_communication
from servos.control.power_control import init_servo_power, servo_power_off


def main():
    try:
        init_gpio_pins()
        init_servo_communication()
        init_servo_power()

        # program start

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