#!/user/bin/python3
mylist =[4, 3, 2, 1]
newlist = list(map(lambda x: list(range(x, 0, -1)), mylist))
print(newlist)
