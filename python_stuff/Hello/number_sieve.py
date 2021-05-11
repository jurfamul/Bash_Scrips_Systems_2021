#!/user/bin/python3
uInput1 = input("Enter the first number: ")
uNum1 = int(uInput1)
uNum2 = 0

while uNum2 <= 10:
    uInput2 = input("Enter the second number (greater than {0}): ".format(uNum1))
    uNum2 = int(uInput2)

fourMod = uNum1 % 4
sevenMod = uNum1 % 7

if fourMod == 0:
    fourHead = uNum1
else:
    fourHead = uNum1 + (4 - fourMod)

if sevenMod == 0:
    sevenHead = uNum1
else:
    sevenHead = uNum1 + (7 - sevenMod)

fourList = list(range(fourHead, uNum2, 4))
sevenList = list(range(sevenHead, uNum2, 7))
bothList = list(set(fourList) & set(sevenList))
numDict = {"4": fourList, "7": sevenList, "4&7": bothList}

print("Items in 4 only: ")
for i in numDict["4"]:
    print("        {0}".format(i))
print("Items in 7 only: ")
for i in numDict["7"]:
    print("        {0}".format(i))
print("Items in 4 and 7: ")
for i in numDict["4&7"]:
    print("        {0}".format(i))
