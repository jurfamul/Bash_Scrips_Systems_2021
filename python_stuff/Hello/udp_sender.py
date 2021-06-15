#!/user/bin/python3
import sys
from socket import socket, AF_INET, SOCK_DGRAM

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    data = None
    while data != "quit":
        data = input("input data to send to server: (type quit to exit): ")
        udp_sock = socket(AF_INET, SOCK_DGRAM)
        ret = udp_sock.sendto(bytes(data, 'utf-8'), (ip, port))
        print("sent {0} bytes to {1}:{2}.".format(ret, ip, port))


if __name__ == "__main__":
    main()