import socket
import json

class Client:
    def __init__(self, host='localhost', port=5000):
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

    def stop(self):
        self.client.close()

if __name__ == '__main__':
    client = Client()
    client.start()

    while True:
        data = client.receive_data()
        print(data)