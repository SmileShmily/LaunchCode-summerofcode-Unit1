'''Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n.
So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.
'''
from test import testEqual

def sumTo(n):
    result = (n * (n + 1)) / 2
    return result

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)
