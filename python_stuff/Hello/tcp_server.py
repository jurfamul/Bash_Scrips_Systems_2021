#!/user/bin/python3
import sys
from socket import socket, AF_INET, SOCK_STREAM
import threading


class TCPClient(threading.Thread):
    def __init__(self, client_sock, client_address):
        super(TCPClient, self).__init__()
        self.client_sock = client_sock
        self.client_address = client_address
        self.keep_running = True

    def run(self):
        while self.keep_running:
            try:
                data = self.client_sock.recv(4096)

                if len(data) == 0:
                    self.client_sock.close()
                else:
                    self.client_sock.send(data)
            except Exception as e:
                self.keep_running = False


def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.bind((ip, port))
    tcp_sock.listen(100)
    client_threads = []
    quit = False

    while not quit:
        try:
            client_sock , (client_ip, client_port) = tcp_sock.accept()
            temp_client_thread = TCPClient(client_sock, (client_ip, client_port))
            client_threads.append(temp_client_thread)
            temp_client_thread.start()
            print("starting thread")
        except KeyboardInterrupt as k:
            quit = True


if __name__ == "__main__":
    main()