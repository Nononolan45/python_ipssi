import argparse

parser = argparse.ArgumentaddParser();
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", required=False)
group.add_argument("--uper", action="store_length", required=False)
group.add_argument("--lower", action="store_length", required=False)
group.add_argument("--strict", action="store_length", required=False)

