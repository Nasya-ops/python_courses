import sys
import json
import socket

server_socket = socket.socket()

print("Server socket created")

ip = "127.0.0.1"

port = 35491

server_socket.bind((ip, port))

print("Server socket bound with with ip {} port {}".format(ip, port))

server_socket.listen()

count = 0

while True:
    try:
        client_connection, client_address = server_socket.accept()
        count += 1
        print(f"Accepted {count} {client_address} connections so far")
        while True:
            data = client_connection.recv(1024)
            if data != b'':
                print(json.loads(data.decode()))
                msg1 = "Hi Client! Read everything you sent".encode()
                msg2 = "Now I will close your connection".encode()
                client_connection.send(msg1)
                client_connection.send(msg2)
                client_connection.close()
                print("Connection closed")
                break

    except KeyboardInterrupt:
        print('Server socket close')
        server_socket.close()
        sys.exit()
