import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose")
group.add_argument("--uper", action="store_length")
group.add_argument("--lower", action="store_length")
group.add_argument("--strict", action="store_length")


print parser.parse_args()
