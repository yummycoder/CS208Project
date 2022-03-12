import argparse
import time

from importlib.machinery import SourceFileLoader
import socket

parser = argparse.ArgumentParser(description='Controller')
parser.add_argument('--myworker',   type=str, help='name of myworker module',    default='MyWorker.py')
parser.add_argument('--min_budget',   type=float, help='Minimum budget used during the optimization.',    default=9)
parser.add_argument('--max_budget',   type=float, help='Maximum budget used during the optimization.',    default=243)
parser.add_argument('--n_iterations', type=int,   help='Number of iterations performed by the optimizer', default=4)
parser.add_argument('--worker', help='Flag to turn this into a worker process', action='store_true')
parser.add_argument('--run_id', type=str, help='A unique run id for this optimization run. An easy option is to use the job id of the clusters scheduler.')
parser.add_argument('--nic_name',type=str, help='Which network interface to use for communication.')
parser.add_argument('--shared_directory',type=str, help='A directory that is accessible for all processes, e.g. a NFS share.')
parser.add_argument('--monitor', type=str, help='monitor', default='127.0.0.1')
parser.add_argument('--monitor_port', type=int, help='monitor_port', default=8080)

args=parser.parse_args()

un_success = True
while un_success:
    client_socket = socket.socket()  # instantiate
    client_socket.connect((args.monitor, args.monitor_port))  # connect to the monitor
    message = 'assign!' + args.myworker + '!' + str(args.min_budget) + '!' + str(args.max_budget) + '!' + str(args.n_iterations)
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    if data.startswith('wait!'):
        time.sleep(500)
    else:
        print(data)
        un_success = False
client_socket.close()


# w = foo.MyWorker(sleep_interval = 0, nameserver='127.0.0.1',run_id='example1')
# w.print()


