#!/user/bin/python3
import sys


def my_input(prompt="", infile=sys.stdin):
    if prompt != "":
        sys.stdout.write("{0}/n".format(prompt))

    line = infile.readline()
    return line


def my_output(line):
    sys.stdout.write("{0}".format(line))


inLine = my_input()
lines = [inLine]

while True:
    inLine = my_input()
    if inLine == "quit\n":
        break
    lines.append(inLine)
    my_output(inLine)


for file in sys.argv:
    if file is not sys.argv[0]:
        with open(file, 'w') as outFile:
            for line in lines:
                outFile.write(line)
