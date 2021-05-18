#!/user/bin/python3
from functools import reduce
mylist = [5, 4, 3, 2, 1]
product = reduce(lambda x, y: x * y, mylist)
print("The product of the numbers in mylist is: {0}".format(product))
