#!/user/bin/python3
uInput1 = input("Enter the numerator: ")
uInt1 = int(uInput1)
uInput2 = input("Enter the denominator: ")
uInt2 = int(uInput2)

quotient = uInt1 / uInt2
remainder = uInt1 % uInt2

print("The quotient is {0} and the remainder is {1}".format(quotient, remainder))
