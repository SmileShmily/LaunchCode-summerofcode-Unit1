'''Write a function findHypot.
The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse.
(Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
'''
from test import testEqual
import math
def findHypot(a,b):
    # your code here
    return (a**2 + b**2)**0.5
testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)
