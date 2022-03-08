import socket
import argparse

parser = argparse.ArgumentParser(description='check the runs and workers of them')
parser.add_argument('--host',   type=float, help='monitor address',    default='127.0.0.1')
parser.add_argument('--port',   type=float, help='monitor port',    default=8080)

args = parser.parse_args()

client_socket = socket.socket()  # instantiate
client_socket.connect((args.host, args.port))  # connect to the server
message = 'create!0!0!0!0\n'
client_socket.send(message.encode())
client_socket.close()
data = client_socket.recv(1024).decode()
while data:  # receive response
    data = client_socket.recv(1024).decode()
    print(data)

