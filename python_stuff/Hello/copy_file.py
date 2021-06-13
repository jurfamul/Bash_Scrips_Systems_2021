#!/user/bin/python3
import sys
fileName = input("Please Input file name: ")

try:
    inFile = open(fileName, 'r')
except Exception as e:
    sys.stderr.write(str(e))
finally:
    if inFile is None:
        sys.stderr.write("Error: could not open file {0}".format(fileName))

outFileName = fileName + ".copy"

try:
    outFile = open(outFileName, 'w')
except Exception as e:
    sys.stderr.write(str(e))
finally:
    if outFile is None:
        sys.stderr.write("Error: could not open file {0}".format(fileName))


for line in inFile:
    outFile.write(line)

inFile.close()
outFile.close()

