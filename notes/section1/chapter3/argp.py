import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first_number', help='first number to be added', type=int)
parser.add_argument('second_number', help='second number to be added', type=int)

args = parser.parse_args()

print(f'Args: {args}')
print(f'The sum is {args.first_number - args.second_number}')