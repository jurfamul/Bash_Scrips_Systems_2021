#!/user/bin/python3
import mycsv


def main():
    inFileName = "pretend_data.csv"
    data = None
    with open(inFileName, 'r') as inFile:
        data = mycsv.parse_csv(inFile)

    for line in data:
        print("{0} has grade {1}".format(line[0], line[1]))


if __name__ == "__main__":
    main()
