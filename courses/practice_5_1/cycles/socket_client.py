import json
import socket


def send(data):
    socket_object = socket.socket()
    socket_object.connect(("localhost", 35491))

    print("Connected to localhost")
    msg = json.dumps(data)
    socket_object.sendall(msg.encode())

    while True:
        block_size = 1000
        block_number = 0

        # Selected block to send
        block_data = data[block_number * block_size: (block_number + 1) * block_size]

        if block_data == b'':
            print("Connection closed")
            break
        block_number += 1
    socket_object.close()


big_data = list(range(100000))

while big_data:
    send(big_data)
