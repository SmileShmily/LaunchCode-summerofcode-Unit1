'''Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example,
 sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
'''
def sum_of_squares(xs) :
    return sum(i ** 2 for i in xs)
print (sum_of_squares([2, 3, 4]) )

