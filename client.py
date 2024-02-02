import socket
import json
import LEDapp, servo

SERVO_0 = 12
SERVO_1 = 13
SERVO_2 = 14
SERVO_3 = 15


class Client:

    def __init__(self, host='192.168.50.122', port=5000):
        self.host = host
        self.port = port
        self.client = None

        self.servo_0_rotation = 0
        self.is_first_step_servo_0 = True

        self.servo_1_rotation = 0
        self.is_first_step_servo_1 = True

        self.servo_2_rotation = 0
        self.is_first_step_servo_2 = True

        self.servo_3_rotation = 0
        self.is_first_step_servo_3 = True

        self.servo_4_rotation = 0
        self.is_first_step_servo_4 = True

    def start(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def receive_data(self):
        data = self.client.recv(1024)
        json_data = json.loads(data.decode('utf-8'))
        return json_data

    def process_data(self, data, led):

        actions = {
            'w': (0, 255, 0),
            'a': (255, 0, 0),
            's': (0, 0, 255),
            'd': (255, 255, 255),
        }
        servo_actions = {
            '1': {'chanel': SERVO_2, 'initial': 250, 'min': 90, 'final': 500, 'step': 5},
            '2': {'chanel': SERVO_2, 'initial': 250, 'min': 90, 'final': 500, 'step': -5},
            '4': {'chanel': SERVO_1, 'initial': 250, 'min': 90, 'final': 500, 'step': 5},
            '5': {'chanel': SERVO_1, 'initial': 250, 'min': 90, 'final': 500, 'step': -5},
            '3': {'chanel': SERVO_0, 'initial': 300, 'min': 90, 'final': 400, 'step': 5},
            '6': {'chanel': SERVO_0, 'initial': 300, 'min': 90, 'final': 400, 'step': -5},
        }

        key = data.get('key')
        is_first_step = data.get('is_first_step')

        if key in actions:
            colors = actions.get(key, 'Unknown command')
            led.colorWipe(*colors)
        elif key in servo_actions:
            _servo = servo_actions.get(key)
            self.move_servo(_servo, is_first_step)

    def stop(self):
        self.client.close()

    def move_servo(self, _servo, is_first_step):

        chanel = _servo.get('chanel')
        initial = _servo.get('initial')
        min = _servo.get('min')
        final = _servo.get('final')
        step = _servo.get('step')

        rotation = 0

        if is_first_step:
            if chanel == 12:
                self.servo_0_rotation = initial
                rotation = self.servo_0_rotation
            elif chanel == 13:
                self.servo_1_rotation = initial
                rotation = self.servo_1_rotation
            elif chanel == 14:
                self.servo_2_rotation = initial
                rotation = self.servo_2_rotation
            elif chanel == 15:
                self.servo_3_rotation = initial
                rotation = self.servo_3_rotation
        else:
            if chanel == 12:
                self.servo_0_rotation += step
                rotation = self.servo_0_rotation
            elif chanel == 13:
                self.servo_1_rotation += step
                rotation = self.servo_1_rotation
            elif chanel == 14:
                self.servo_2_rotation += step
                rotation = self.servo_2_rotation
            elif chanel == 15:
                self.servo_3_rotation += step
                rotation = self.servo_3_rotation

        if min + step < rotation < final + step:
            rotation += step
            servo.pwm.set_pwm(chanel, 0, rotation)


if __name__ == '__main__':
    client = Client()
    LED = LEDapp.LED()
    client.start()

    while True:
        data = client.receive_data()
        client.process_data(data, LED)
