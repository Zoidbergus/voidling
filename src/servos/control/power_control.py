# power control of the engines
import time
import RPi.GPIO as GPIO


def init_servo_power():

    leds_pin = 9
    motor_power_pin = 24
    # Init GPIO

    GPIO.setup(leds_pin, GPIO.OUT)
    GPIO.setup(motor_power_pin, GPIO.OUT)

    GPIO.output(leds_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(leds_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(leds_pin, GPIO.HIGH)
    GPIO.output(motor_power_pin, GPIO.HIGH)
    print("Servo power On.")


def servo_power_off():
    leds_pin = 9
    motor_power_pin = 24

    GPIO.output(motor_power_pin, GPIO.LOW)
    GPIO.output(leds_pin, GPIO.LOW)

    print("Servo power Off.")
