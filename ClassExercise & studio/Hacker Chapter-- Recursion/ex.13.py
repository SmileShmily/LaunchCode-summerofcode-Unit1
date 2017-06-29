'''Pascal’s triangle is a number triangle with numbers arranged in staggered rows such that
anr=n!r!(n−r)!

This equation is the equation for a binomial coefficient. You can build Pascal’s triangle by adding the two numbers that are diagonally above a number in the triangle.
 An example of Pascal’s triangle is shown below.

        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

Write a program that prints out Pascal’s triangle. Your program should accept a parameter that tells how many rows of the triangle to print.
'''
#fangfa 1
def triangle(rows):

    for rownum in range (rows):
        newValue=1
        PrintingList = list()
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)
print(triangle(5))

#fangfa 2
import math

# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop,
    # while count <= rows: # can avoid initializing and incrementing
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1):
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result:
for row in pascals_triangle(5):
    print(row)



#fangfa 3
def pascals_triangle(n_rows):
    results = [] # a container to collect the rows
    for _ in range(n_rows):
        row = [1] # a starter 1 in the row
        if results: # then we're in the second row or beyond
            last_row = results[-1] # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row) # add the row to the results.
    return results
for i in pascals_triangle(6):
     print(i)


#fangfa 4
'''
def nextrow(lst):
    lag = 0
    for element in lst:
        yield lag + element
        lag = element
    yield element

row = [1]
for number in range(12):
    row = nextrow(row)
    print (row)
    '''
#fangfa 5
'''
def pascal(level):
    lst = [1]
    while len(lst) < level:
        lst = [1] + map(lambda x,y: x+y if y else 1, lst, lst[1:])
        print (lst)

pascal(14)
'''
