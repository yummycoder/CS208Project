import hpbandster.core.monitor_slave as hpm
import argparse

parser = argparse.ArgumentParser(description='run slave')
parser.add_argument('--nic_name',type=str, help='Which network interface to use for communication.')
parser.add_argument('--shared_directory',type=str, help='A directory that is accessible for all processes, e.g. a NFS share.')
parser.add_argument('--port',type=str, help='Which network interface to use for communication.')
parser.add_argument('--monitor',type=str, help='A directory that is accessible for all processes, e.g. a NFS share.')
parser.add_argument('--monitor_port',type=str, help='Which network interface to use for communication.')
args=parser.parse_args()

slave = hpm.Slave(nic_name=args.nic_name, port=args.port, monitor=args.monitor, monitor_port=args.monitor_port, share_dir=args.shared_directory)
slave.run()
