import argparse

parser = argparse.ArgumentParser(description="A simple greeting tool")
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--count", type=int, default=1, help="How many times to greet")

args = parser.parse_args()

for i in range(args.count):
    print(f"Hello, {args.name}!")
