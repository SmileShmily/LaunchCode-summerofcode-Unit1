'''Now write the function is_odd(n) that returns True when n is odd and False otherwise.
'''
from test import testEqual

def is_odd(n):
    # your code here
    if n % 2 == 0:
        return False
    else:
        return True
testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)