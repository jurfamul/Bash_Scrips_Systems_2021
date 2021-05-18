#!/user/bin/python3
from sys import argv
print("The number of command line arguments is: {0}".format(len(argv)))
print("The length of the first command line argument is: {0}".format(len(argv[1])))
print("List of command line arguments: {:}".format(argv))