#!/user/bin/python3
import fact


def main():
    print("Use_fact is being run directly by python, running factorial as a module")
    num = fact.factorial(5)
    print("The factorial of 5 is {0}.".format(num))


if __name__ == "__main__":
    main()
else:
    print("use_fact is being run as part of a module")
