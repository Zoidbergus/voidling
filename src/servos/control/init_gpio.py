import RPi.GPIO as GPIO


def init_gpio_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print("GPIO initialized.")
