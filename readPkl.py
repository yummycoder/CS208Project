import argparse
import pickle

from time import sleep

import math

parser = argparse.ArgumentParser(description='read file')
parser.add_argument('--run_id',type=str, help='run id')
args=parser.parse_args()

with open(args.run_id + '_results.pkl', 'rb') as f:
    res = pickle.load(f)
    id2config = res.get_id2config_mapping()
    incumbent = res.get_incumbent_id()

    print('Best found configuration:', id2config[incumbent]['config'])
    print('A total of %i unique configurations where sampled.' % len(id2config.keys()))
    print('A total of %i runs where executed.' % len(res.get_all_runs()))
    # print('Total budget corresponds to %.1f full function evaluations.' % (
    #             sum([r.budget for r in res.get_all_runs()]) / args.max_budget))