'''Write a function that will return the number of digits in an integer.
'''
def findNumDigits(n):
    n_str = str(n)
    return len(n_str)


print(findNumDigits(50))
print(findNumDigits(20000))
print(findNumDigits(1))