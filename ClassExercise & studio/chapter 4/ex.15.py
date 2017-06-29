'''Repeat the above exercise but this time print 10 random numbers between 25 and 35.
'''

import random

values=[25,26,27,28,29,30,31,32,33,34,35]
for i in range(0, 10):
    # random.choice returns a random character.
    letter = random.choice(values)
    print(letter)
