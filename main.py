import socket
import json
import keyboard

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



if __name__ == '__main__':
    server = Server()
    server.start()

    def send_keypress(event):
        if event.name in ['w', 'a', 's', 'd']:
            server.send_data({'key': event.name})

    keyboard.on_press(send_keypress)

    while True:
        pass