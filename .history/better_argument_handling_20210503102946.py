import argparse

parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
parser.add_argument("--verbose")
parser.add_argument("--uper", action="store_true")
parser.add_argument("--lower", action="store_true")
parser.add_argument("--strict")


print parser.parse_args()
