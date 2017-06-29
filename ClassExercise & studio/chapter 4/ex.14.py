'''Use a for statement to print 10 random numbers.
'''

import random

values="012345678910"
for i in range(0, 10):
    # random.choice returns a random character.
    letter = random.choice(values)
    print(letter)

