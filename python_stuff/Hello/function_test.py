#!/user/bin/python3
def add(x, y):
    z = x + y
    print("Adding {0} + {1} equals {2}".format(x, y, z))


def find_max(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 0


x = 15
y = 10
add(x, y)
z = find_max(x, y)
print("The maximum value of {0} and {1} is {2}.".format(x, y, z))
a = find_max(x, z)
print("{0} and {1} are equal, therefore find_max() returns {2}.".format(x, z, a))
