import servo

class ServoManager:
    SERVO_0 = 12
    SERVO_1 = 13
    SERVO_2 = 14
    SERVO_3 = 15

    servo_actions = {
        'clawright': {'chanel': SERVO_2},
        'clawleft': {'chanel': SERVO_2},
        'armdown1': {'chanel': SERVO_1},
        'armup1': {'chanel': SERVO_1},
        'armdown2': {'chanel': SERVO_0},
        'armup2': {'chanel': SERVO_0},
    }

    def __init__(self):

        self.servo_0_rotation = 350
        self.servo_1_rotation = 300
        self.servo_2_rotation = 250

        servo.pwm.set_pwm(self.SERVO_0, 0, self.servo_0_rotation)

        servo.pwm.set_pwm(self.SERVO_1, 0, self.servo_1_rotation)

        servo.pwm.set_pwm(self.SERVO_2, 0, self.servo_2_rotation)

    def move_servo(self, _servo, move_pos):
        chanel = _servo.get('chanel')
        servo.pwm.set_pwm(chanel, 0, int(move_pos))

