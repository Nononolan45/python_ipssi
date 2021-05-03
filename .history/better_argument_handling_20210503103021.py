import argparse

parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
parser.add_argument("--verbose")
parser.add_argument("--strict")
mxg = group.add_mutually_exclusive_group()
mxg.add_argument("--uper", action="store_true")
mxg.add_argument("--lower", action="store_true")


print parser.parse_args()
