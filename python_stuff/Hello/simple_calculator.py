#!/user/bin/python3
uInput1 = input("Enter the first number: ")
uInt1 = int(uInput1)
uInput2 = input("Enter your desired operation (+-*/): ")
uInput3 = input("Enter the second number: ")
uInt3 = int(uInput3)

if uInput2 == "+":
    sum = uInt1 + uInt3
    print("{0} + {1} = {2}".format(uInt1, uInt3, sum))
elif uInput2 == "-":
    diff = uInt1 - uInt3
    print("{0} - {1} = {2}".format(uInt1, uInt3, diff))
elif uInput2 == "*":
    mult = uInt1 * uInt3
    print("{0} * {1} = {2}".format(uInt1, uInt3, mult))
elif uInput2 == "/":
    div = uInt1 / uInt3
    print("{0} / {1} = {2}".format(uInt1, uInt3, div))
else:
    print("error: invalid operator detected. Please try again.")
