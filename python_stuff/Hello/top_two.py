#!/user/bin/python3
def top_two(numlist):
    max = 0
    next = 0
    for x in numlist:
        if x > max:
            next = max
            max = x
    return max, next


mylist = [10, 23, 66, 4, 87, 200, 0]
first, second = top_two(mylist)
print("The two highest numbers from the list are: {0} and {1}.".format(first, second))
