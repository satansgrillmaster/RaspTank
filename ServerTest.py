import socket
import threading
import time


class Server:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server = None
        self.stop_server = False

    def handle_client(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            self.handle_data(data)
        conn.close()

    def handle_data(self, data):
        message = data.decode('utf-8')
        splitted_message = message.split('_')


        if message == 'action1':
            self.perform_action1()

        elif message == 'action2':
            self.perform_action2()

        else:
            print(f"Unknown message: {message}")

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Server started at {self.host}:{self.port}")
        while True:
            try:
                conn, addr = self.server.accept()
                print(f"Connection received from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(conn,))
                client_thread.start()
            except Exception as e:
                print(f"Error: {e}")
                break

    def stop_server_definitive(self):
        self.server.close()


if __name__ == '__main__':
    server = Server()
    server.start()