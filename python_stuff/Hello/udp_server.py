#!/user/bin/python3
import sys
from socket import socket, AF_INET, SOCK_DGRAM

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    udp_sock = socket(AF_INET, SOCK_DGRAM)
    udp_sock.bind((ip, port))

    while True:
        data, (client_ip, client_port) = udp_sock.recvfrom(100)
        print("Received {0} bytes from {1}:{2}".format(len(data), client_ip, client_port))
        print("The message is {0}".format(data))
        udp_sock.sendto(data, (client_ip, client_port))


if __name__ == "__main__":
    main()