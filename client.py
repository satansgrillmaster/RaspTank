import socket
import threading
import time


class Server:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server = None
        self.stop_server = False  # Definieren Sie stop_server als Attribut der Klasse

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Server started at {self.host}:{self.port}")
        timer = threading.Timer(5, self.stop_server_definitive)  # Keine Notwendigkeit, stop_server hier zu übergeben
        timer.start()
        while True:
            try:
                conn, addr = self.server.accept()
                print(f"Connection received from {addr}")
                conn.close()
            except Exception as e:
                print(f"Error: {e}")
                break

    def stop_server_definitive(self):
        self.server.close()


if __name__ == '__main__':
    server = Server()
    server.start()
