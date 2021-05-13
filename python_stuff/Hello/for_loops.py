#!/user/bin/python3
testList = ["This ", "is ", "a ", "list."]
testSet = set()
testSet.add("This ")
testSet.add("is ")
testSet.add("a ")
testSet.add("set.")
testSet.add("This ")
testDict = {"first": "This ", "Second": "is ", "third": "a ", "fourth": "dictionary."}

for i in testList:
    print(i)
print("")
for i in testSet:
    print(i)
print("")
for i in testDict:
    print("{0}: {1}".format(i, testDict[i]))
