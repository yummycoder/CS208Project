import hpbandster.core.monitor as hpm
import argparse

parser = argparse.ArgumentParser(description='Run monitor')
parser.add_argument('--shared_directory',type=str, help='A directory that is accessible for all processes, e.g. a NFS share.')
args=parser.parse_args()

monitor = hpm.Monitor(share_dir=args.shared_directory)
monitor.start()