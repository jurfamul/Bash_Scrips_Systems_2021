#!/user/bin/python3
import sys


def my_input(prompt="", infile=sys.stdin):
    if prompt != "":
        sys.stdout.write("{0}/n".format(prompt))

    line = infile.readline()
    return line


def my_output(line):
    sys.stdout.write("{0}".format(line))
    sys.stderr.write("{0}".format(line))


inLine = my_input()
isFile = False

if len(inLine) > 20:
    isFile = True

my_output(inLine)

if isFile:
    while True:
        inLine = my_input()
        if "\n" in inLine:
            my_output(inLine)
        else:
            break
else:
    while True:
        inLine = my_input()
        if inLine == "quit\n":
            break
        my_output(inLine)
