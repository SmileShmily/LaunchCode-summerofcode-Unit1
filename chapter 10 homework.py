'''
Chapter 10 Assignment
Write a function to find the sum of all the even numbers in a list.

Normally we start you off by providing the function definition statement, e.g.:

-----------------------------------------------------------------------------------------
def launch_rockets(destination, num_passengers):
# your code here
-----------------------------------------------------------------------------------------

But in this case we will leave that up to you! So you will need to write that `def` line yourself.
 Make sure you give your function the name `sum_evens`, so that the tests work.
  Your function should accept one argument, the list of numbers to be summed.
'''
# TODO
# define a function called sum_evens, which receives one argument, a list of numbers.
# your function should return the sum of all the even numbers in the list
#data= [2,3,4]
def sum_evens(data):
    "Sum up all the even numbers in a list."
    return sum(i for i in data if i % 2 == 0)
#print(sum_evens(data))

6
1
Your code passed all the tests!
