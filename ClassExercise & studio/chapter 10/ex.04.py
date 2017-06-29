'''Write a function to count how many odd numbers are in a list.
'''

import random

def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

# make a random list to test the function
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))
