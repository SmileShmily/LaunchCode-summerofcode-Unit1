'''Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value.
 (Note: there is a builtin function named max but pretend you cannot use it.)
'''

import random

def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(max(lst))
