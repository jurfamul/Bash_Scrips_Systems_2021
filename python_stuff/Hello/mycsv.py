#!/user/bin/python3
import sys


def parse_csv(fh=sys.stdin, separator=","):
    csv_items = []
    for line in fh:
        line = line.rstrip()
        csv_items.append(line.split(separator))
    return csv_items


def main():
    items = parse_csv()
    print(str(items))


if __name__ == "__main__":
    main()
