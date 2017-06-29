''')

(GRADED) Write a function areaOfCircle(r) which returns the area of a circle of radius r.
Make sure you use the math module in your solution.
'''
from test import testEqual
import math
# TODO: use def to define a function called areaOfCircle which takes an argument called r
    # TODO implment your function to return the area of a circle whose radius is r
def areaOfCircle(r):
    return math.pi * r** 2
t = areaOfCircle(0)
testEqual(t,0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(100)
testEqual(t,31415.926535897932)