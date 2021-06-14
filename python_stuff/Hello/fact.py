#!/user/bin/python3
import sys


def factorial(integer):
    count = integer
    fact = integer

    while count > 1:
        count = count - 1
        fact = fact * count

    return fact


def main():
    print("The program has been run directly by python (calling factirial")
    num = factorial(4)
    print("The factorial of 4 is {0}.".format(num))


if __name__ == "__main__":
    main()
else:
    print("The program has been run as part of a module.")
