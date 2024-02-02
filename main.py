import socket
import json
import time
import msvcrt

import keyboard

SERVO_0_EVENTS = ['3', '6']
SERVO_1_EVENTS = ['4', '5']
SERVO_2_EVENTS = ['1', '2']

class Server:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server = None
        self.conn = None
        self.addr = None

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        self.conn, self.addr = self.server.accept()

    def send_data(self, data):
        json_data = json.dumps(data)
        self.conn.sendall(json_data.encode('utf-8'))

    def stop(self):
        self.conn.close()
        self.server.close()

def clear_keyboard_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

if __name__ == '__main__':
    server = Server()
    server.start()

    used_events = []

    def send_keypress(event):
        if event.name in ['w', 'a', 's', 'd', '1', '2', '4', '5', '3', '6']:
            if event.name not in used_events:

                if event.name in SERVO_1_EVENTS:
                    for servo_event in SERVO_1_EVENTS:
                        used_events.append(servo_event)
                elif event.name in SERVO_2_EVENTS:
                    for servo_event in SERVO_2_EVENTS:
                        used_events.append(servo_event)
                elif event.name in SERVO_0_EVENTS:
                    for servo_event in SERVO_0_EVENTS:
                        used_events.append(servo_event)

                server.send_data({'key': event.name, 'is_first_step': True})
                clear_keyboard_buffer()  # Clear the keyboard buffer after sleep
            else:
                server.send_data({'key': event.name, 'is_first_step': False})
                clear_keyboard_buffer()  # Clear the keyboard buffer after sleep

    keyboard.on_press(send_keypress)
    while True:
        pass