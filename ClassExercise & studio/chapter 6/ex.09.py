'''Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.
'''
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if is_even(n):
        return False
    else:
        return True

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)