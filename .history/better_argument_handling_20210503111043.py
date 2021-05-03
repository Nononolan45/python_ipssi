import sys

print(sys.argv)
if sys.argv[1] == "--verbose":
    print("# processing file ")
    filin = open(sys.argv[3], "r");
    lignes = filin.readline()
    # if sys.argv[2] == "--upper":
    #     for ligne in lignes:
    #         print(ligne.upper())
    # elif sys.argv[2] == "--lower":
    #     for ligne in lignes:
    #         print(ligne.lower())

filin.close()
# parser = argparse.ArgumentParser()
# # group = parser.add_mutually_exclusive_group()
# parser.add_argument("--verbose")
# parser.add_argument("--strict")
# mxg = group.add_mutually_exclusive_group()
# mxg.add_argument("--uper", action="store_true")
# mxg.add_argument("--lower", action="store_true")


# print parser.parse_args()
