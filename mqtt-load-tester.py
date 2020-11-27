import argparse

# <HOST> <PORT> <TOPIC> <MESSAGE> <FREQUENCY>

parser = argparse.ArgumentParser()

parser.add_argument('host', type=str)
parser.add_argument('--port', default=1833, type=int)
parser.add_argument('topic', type=str)
parser.add_argument('--message', default='', type=str)
parser.add_argument('--frequency', default=10, type=int)

args = parser.parse_args()
print(args.accumulate(args.integers))