# Initiate the communication with the driver, ready the pwm function

from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM
import threading


def init_servo_communication():
    global pwm
    pwm = PWM(0x70)
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

    global lock
    lock = threading.RLock()


def set_pwm(channel, on, off):
    with lock:
        pwm.setPWM(channel, on, off)
