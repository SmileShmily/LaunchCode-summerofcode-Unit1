''')

(GRADED) A year is a leap year if it is divisible by 4 unless it is a century that is not divisible by 400.
Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
'''
from test import testEqual

def isLeap(year):
    # your code here
    year = float(year)
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return False
        else:
            return True

testEqual(isLeap(1944), True)
testEqual(isLeap(2011), False)
testEqual(isLeap(1986), False)
testEqual(isLeap(1800), False)
testEqual(isLeap(1900), False)
testEqual(isLeap(2000), True)
testEqual(isLeap(2056), True)