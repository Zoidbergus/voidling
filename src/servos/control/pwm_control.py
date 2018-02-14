# Initiate the communication with the driver, ready the pwm function

from src.servos.lib.Adafruit_PWM_Servo_Driver import PWM


def init_servo_communication():
    pwm = PWM(0x70)
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
