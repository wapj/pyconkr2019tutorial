import time
from socket import *


def echo_server(address):
    sock = socket()
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.bind(address)
    sock.listen(5)

    while True:
        client, addr = sock.accept()  # blocking
        echo_handler(client, addr)  # blocking


def echo_handler(client, addr):
    print("Connection from", addr)
    with client:
        while True:
            data = client.recv(100000)  # blocking
            if not data:
                break
            client.send(b"1\n")
            time.sleep(1)  # blocking GIL 을 우회함
            client.send(b"2\n")
            time.sleep(1)
            client.send(b"3\n")
            time.sleep(1)
            client.sendall(b"[server response] " + data)  # blocking
        print("Connection closed")
