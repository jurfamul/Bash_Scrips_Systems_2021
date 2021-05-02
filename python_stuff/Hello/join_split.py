#!/user/bin/python3
myString = "This,is,a,list,5"
splitList = myString.split(",")
print(splitList)
joinString = " ".join(splitList)
print(joinString)
print("%d"%(splitList[4]))
