#!/user/bin/python3
import random

def find_words_with_r(input_list):
    newlist = []
    for x in input_list:
        if 'r' in x:
            newlist.append(x)
    return newlist

numlist = []
randlist = [random.randint(1,100) for x in range(1, 1000)]
mystring = "There once was a dog named Rogerrr. He was a good boy, but his bite was worse than his bark!"
sevenlist = [x for x in randlist if x % 7 == 0]
eightlist = [x for x in randlist if x % 8 == 0]
print("The count of numbers divisible by 7 is {0}".format(len(sevenlist)))
print("The count of numbers divisible by 8 is {0}".format(len(eightlist)))
rlist = find_words_with_r(mystring.split(" "))
print("The words containing r in the string: ")
for x in rlist:
    print("{0}".format(x))
