import sys
import os.path 
del sys.argv[0]
list_arg = [arg for arg in sys.argv if arg.find('--') != -1]
list_filename = [arg for arg in sys.argv if arg.find('--') == -1]

if '--strict' in list_arg: 
    list_files_not_readable = [file for file in list_filename if not os.path.isfile(file)]
    if len(list_files_not_readable) > 0:
        print 'could not read the following files : ' + ', '.join(list_files_not_readable)
else:
    # for file in list_files_not_readable:file_name

# if sys.argv.index('--verbose') :
# if sys.argv[1] == "--verbose":
#     print("# processing file ")
#     filin = open(sys.argv[3], "r");
#     lignes = filin.readline()
#     # if sys.argv[2] == "--upper":
#     #     for ligne in lignes:
#     #         print(ligne.upper())
#     # elif sys.argv[2] == "--lower":
#     #     for ligne in lignes:
#     #         print(ligne.lower())

# filin.close()
# parser = argparse.ArgumentParser()
# # group = parser.add_mutually_exclusive_group()
# parser.add_argument("--verbose")
# parser.add_argument("--strict")
# mxg = group.add_mutually_exclusive_group()
# mxg.add_argument("--uper", action="store_true")
# mxg.add_argument("--lower", action="store_true")


# print parser.parse_args()
