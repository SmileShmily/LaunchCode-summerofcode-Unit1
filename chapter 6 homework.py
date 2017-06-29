'''
Chapter 6 Assignment
A year is a leap year if it is divisible by 4, unless it is a century that is not divisible by 400.

For example:
1956 is a leap year because 1956 is divisible by 4.
1957 is not a leap year, because it is not divisible by 4.
1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is a century and 1900 is not divisible by 400.
1600 is a leap year, because 1600 is divisible by 4 and 1600 is divisible by 400

Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
'''
'''
def isLeap(year):
    # your code here
    year = float(year)
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return False
        else:
            return True
result1=isLeap(1986)
result2=isLeap(1957)
result3=isLeap(1900)
result4=isLeap(2011)
print(result1,result2,result3,result4)

'''
'''
def isLeap(year):
    if year % 400 == 0:
        print("It's a leap year")
    elif year % 4 == 0 and not year % 100 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
result=isLeap(2056)
print(result)
'''

def isLeap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400! = 0):
                return True
            return False
        return True
    return False
result=isLeap(2056)
print(result)



def isLeap(year):
    return False if year % 4 else True if year % 100 else not year % 400
#1 Your code passed all the tests!