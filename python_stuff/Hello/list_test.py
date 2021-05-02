#!/user/bin/python3
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The element at index 4 is: {0}".format(myList[4]))
print("The element at index 8 is: {0}".format(myList[8]))
print(myList)
myList.pop()
print(myList)
myList.append(11)
print(myList)
myList.pop(4)
print(myList)
print("The length of myList is: {0}".format(len(myList)))