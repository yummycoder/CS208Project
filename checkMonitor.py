import socket
import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser(description='check the runs and workers of them')
parser.add_argument('--host',   type=str, help='monitor address',    default='127.0.0.1')
parser.add_argument('--port',   type=int, help='monitor port',    default=8080)

args = parser.parse_args()

client_socket = socket.socket()  # instantiate
client_socket.connect((args.host, args.port))  # connect to the server
message = 'show!0!0!0!0\n'
client_socket.send(message.encode())
sockFile = client_socket.makefile()
data = '-1'
x = PrettyTable()
x.field_names = ["runId", "min_budget", "max_budget", "worker"]
while data:  # receive response
    data = sockFile.readline()
    run = data.split('!')
    if len(run) != 4:
        break
    x.add_row([run[0], run[1], run[2], run[3]])

print(x)
client_socket.close()