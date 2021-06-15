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
    data = sys.argv[3]
    keep_running = True
    tcp_sock = socket()

    while keep_running:
        try:
            tcp_sock = socket(AF_INET, SOCK_STREAM)
            tcp_sock.connect((ip, port))
            ret = tcp_sock.send(bytes(data, 'utf-8'))
            print("Sent {0} bytes to {1}:{2}".format(ret, ip, port))
        except KeyboardInterrupt as k:
            keep_running = False


if __name__ == "__main__":
    main()