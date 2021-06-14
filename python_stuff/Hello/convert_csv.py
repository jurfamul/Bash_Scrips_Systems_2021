#!/user/bin/python3
import sys
import csv


def main():
    inFileName = "pretend_data.csv"
    reader = None
    with open(inFileName, 'r') as inFile:
        reader = csv.reader(inFile)

        outFileName = "pretend_data.psv"
        writer = None
        with open(outFileName, 'w') as outFile:
            writer = csv.DictWriter(outFile, ["Name", "Grade"], delimiter='|')
            writer.writeheader()
            for row in reader:
                rowdict = {"Name": {row[0]: int(row[1])}}
                print(rowdict)
                writer.writerow(rowdict)


if __name__ == "__main__":
    main()