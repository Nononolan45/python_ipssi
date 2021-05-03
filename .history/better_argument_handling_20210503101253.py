import argparse

parser = argparse.ArgumentaddParser();
parser.add_argument("--verbose", required=False)
parser.add_argument("--uper", action="store_length", required=False)
parser.add_argument("--lower", action="store_length", required=False)
parser.add_argument("--strict", action="store_length", required=False)

