'''Sum up all the negative numbers in a list.
'''

import random

def sumNegative(lst):
    sum = 0
    for e in lst:
        if e < 0:
            sum = sum + e
    return sum

lst = []
for i in range(100):
    lst.append(random.randrange(-1000, 1000))

print(sumNegative(lst))


'''def negative_sum(list):
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum

print ("negative sum in -10 -7 3 23 60:", negative_sum([-10,-7,3,23,60]))
'''