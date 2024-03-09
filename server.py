import socket
import threading
import time
import LEDapp
import ServoManager


class Server:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server = None
        self.stop_server = False
        self.led_app = LEDapp.LED()
        self.servo_manager = ServoManager.ServoManager()

    def handle_data(self, data):
        message = data.decode('utf-8')
        splitted_message = message.split('_')


        if message == 'action1':
            self.perform_action1()

        elif message == 'action2':
            self.perform_action2()

        elif splitted_message[0] in self.servo_manager.servo_actions:
            servo = self.servo_manager.servo_actions.get(splitted_message[0])
            print(servo)
            self.servo_manager.move_servo(servo, splitted_message[1])

        else:
            print(f"Unknown message: {message}")

    def perform_action1(self):
        self.led_app.colorWipe(0, 255, 0)

    def perform_action2(self):
        self.led_app.colorWipe(0, 0, 255)

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Server started at {self.host}:{self.port}")
        timer = threading.Timer(120, self.stop_server_definitive)  # Keine Notwendigkeit, stop_server hier zu übergeben
        timer.start()
        while True:
            try:
                conn, addr = self.server.accept()
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    self.handle_data(data)
                conn.close()
            except Exception as e:
                print(f"Error: {e}")
                break

    def stop_server_definitive(self):
        self.server.close()


if __name__ == '__main__':
    server = Server()
    server.start()