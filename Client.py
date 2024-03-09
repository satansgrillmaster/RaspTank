import socket

class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port

        self.connect()


    def connect(self):
        for i in range(100):
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
            self.client.sendall(b'' + str(i).encode('utf-8'))
            self.client.close()

if __name__ == '__main__':
    client = Client()
