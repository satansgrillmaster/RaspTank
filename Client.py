import socket

class Client:
    def __init__(self, host='127.0.0.1', port=9000):
        self.host = host
        self.port = port

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

if __name__ == '__main__':
    client = Client()
    client.connect()