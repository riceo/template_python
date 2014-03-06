import sys
import argparse

parser = argparse.ArgumentParser(description='TEMPLATE DESCRIPTION')

parser.add_argument('arg1', help='arg 1')
parser.add_argument('-a', '--arg2', help='Another arg', default=1, type=int)

args = parser.parse_args()
