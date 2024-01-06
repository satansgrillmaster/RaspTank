import socket
import json
from server import LEDapp


class Client:
    def __init__(self, host='192.168.50.122', port=5000):
        self.host = host
        self.port = port
        self.client = None

    def start(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def receive_data(self):
        data = self.client.recv(1024)
        json_data = json.loads(data.decode('utf-8'))
        return json_data

    def process_data(self, data, led):
        actions = {
            'w': led.colorWipe(0, 255, 0),
            'a': led.colorWipe(255, 0, 0),
            's': led.colorWipe(0, 0, 255),
            'd': led.colorWipe(255, 255, 255),
        }
        key = data.get('key')
        print(actions.get(key, 'Unknown command'))


    def stop(self):
        self.client.close()

if __name__ == '__main__':
    client = Client()
    LED = LEDapp.LED()
    client.start()

    while True:
        data = client.receive_data()
        client.process_data(data, LED)